// ============================================================
// SUCH MAN — storefront server + Groq AI API
// Node 18+; secrets are supplied only through environment vars.
// ============================================================
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const ROOT = __dirname;
const GROQ_MODEL = process.env.GROQ_MODEL || "llama-3.3-70b-versatile";
const GROQ_VISION_MODEL = process.env.GROQ_VISION_MODEL || "meta-llama/llama-4-scout-17b-16e-instruct";
const GROQ_MAX_TOKENS = Math.min(8192, Math.max(128, Number(process.env.GROQ_MAX_TOKENS) || 2048));
const RATE_LIMIT_MAX = Math.max(1, Number(process.env.GROQ_RATE_LIMIT_MAX) || 20);
const RATE_LIMIT_WINDOW = Math.max(1000, Number(process.env.GROQ_RATE_LIMIT_WINDOW) || 60000);
const rateLimits = new Map();

function send(res, code, body, type = "application/json; charset=utf-8") {
  res.writeHead(code, { "Content-Type": type, "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" });
  res.end(type.startsWith("application/json") ? JSON.stringify(body) : body);
}
function sendError(res, code, message) { send(res, code, { error: message }); }

function allowRequest(req) {
  const key = req.socket.remoteAddress || "unknown";
  const now = Date.now();
  let entry = rateLimits.get(key);
  if (!entry || now - entry.start >= RATE_LIMIT_WINDOW) entry = { start: now, count: 0 };
  entry.count += 1;
  rateLimits.set(key, entry);
  if (rateLimits.size > 10000) {
    for (const [ip, item] of rateLimits) if (now - item.start >= RATE_LIMIT_WINDOW) rateLimits.delete(ip);
  }
  return entry.count <= RATE_LIMIT_MAX;
}

function readJson(req, maxBytes = 1_000_000) {
  return new Promise((resolve, reject) => {
    let raw = "";
    let bytes = 0;
    req.setEncoding("utf8");
    req.on("data", chunk => {
      bytes += Buffer.byteLength(chunk);
      if (bytes > maxBytes) {
        reject(Object.assign(new Error("Request body too large"), { statusCode: 413 }));
        req.destroy();
        return;
      }
      raw += chunk;
    });
    req.on("end", () => {
      try { resolve(JSON.parse(raw || "{}")); }
      catch { reject(Object.assign(new Error("Invalid JSON body"), { statusCode: 400 })); }
    });
    req.on("error", reject);
  });
}

function validImageUrl(value) {
  if (typeof value !== "string" || value.length > 4096) return false;
  try {
    const url = new URL(value);
    return url.protocol === "https:" && !["localhost", "127.0.0.1", "::1"].includes(url.hostname);
  } catch { return false; }
}

async function groqChat(req, res) {
  if (req.method !== "POST") return sendError(res, 405, "Method not allowed");
  if (!allowRequest(req)) return sendError(res, 429, "Too many requests. Please try again shortly.");
  if (!process.env.GROQ_API_KEY) return sendError(res, 503, "Groq AI is not configured.");

  let input;
  try { input = await readJson(req); }
  catch (error) { return sendError(res, error.statusCode || 400, error.message || "Invalid request"); }

  const prompt = typeof input.prompt === "string" ? input.prompt.trim() : "";
  if (!prompt || prompt.length > 12000) return sendError(res, 400, "Provide a prompt of up to 12,000 characters.");

  const hasImage = Boolean(input.image_url);
  if (hasImage && !validImageUrl(input.image_url)) return sendError(res, 400, "image_url must be a valid HTTPS image URL.");

  const model = hasImage ? GROQ_VISION_MODEL : GROQ_MODEL;
  const userContent = hasImage
    ? [{ type: "text", text: prompt }, { type: "image_url", image_url: { url: input.image_url } }]
    : prompt;

  try {
    const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + process.env.GROQ_API_KEY,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model,
        messages: [
          { role: "system", content: "You are the SUCH MAN brand assistant. SUCH MAN is a Jamaican streetwear label with an authentic cultural voice and a premium global streetwear outlook. Write original, clear, commercially useful content. Do not invent product specifications, prices, stock, shipping promises, or brand facts." },
          { role: "user", content: userContent }
        ],
        max_tokens: GROQ_MAX_TOKENS,
        temperature: 0.7
      }),
      signal: AbortSignal.timeout(45000)
    });

    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const status = response.status === 429 ? 429 : 502;
      return sendError(res, status, status === 429 ? "Groq rate limit reached. Try again shortly." : "Groq could not complete the request.");
    }
    const message = data.choices && data.choices[0] && data.choices[0].message;
    if (!message || typeof message.content !== "string") return sendError(res, 502, "Groq returned an empty response.");
    return send(res, 200, { text: message.content, model });
  } catch (error) {
    const status = error.name === "TimeoutError" ? 504 : 502;
    return sendError(res, status, status === 504 ? "Groq request timed out." : "Unable to reach Groq.");
  }
}

function serveStatic(res, filePath, contentType) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      if (err.code === "ENOENT") return sendError(res, 404, "Not found");
      return sendError(res, 500, "Server error");
    }
    res.writeHead(200, { "Content-Type": contentType || "application/octet-stream", "Cache-Control": "no-cache", "X-Content-Type-Options": "nosniff" });
    res.end(data);
  });
}

const server = http.createServer((req, res) => {
  const pathname = new URL(req.url, "http://localhost").pathname;
  if (pathname === "/healthz" || pathname === "/_health") {
    return send(res, 200, { status: "READY", groqConfigured: Boolean(process.env.GROQ_API_KEY) });
  }
  if (pathname === "/api/groq/chat") return groqChat(req, res);

  if (req.method !== "GET" && req.method !== "HEAD") return sendError(res, 405, "Method not allowed");
  const requested = pathname === "/" ? "/index.html" : decodeURIComponent(pathname);
  const filePath = path.resolve(ROOT, "." + requested);
  if (!filePath.startsWith(ROOT + path.sep) && filePath !== path.join(ROOT, "index.html")) return sendError(res, 403, "Forbidden");

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) return serveStatic(res, path.join(ROOT, "index.html"), "text/html; charset=utf-8");
    const ext = path.extname(filePath).toLowerCase();
    const types = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".ico": "image/x-icon", ".txt": "text/plain; charset=utf-8" };
    serveStatic(res, filePath, types[ext] || "application/octet-stream");
  });
});

server.listen(PORT, () => console.log("SUCH MAN storefront listening on port " + PORT));
