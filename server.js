// ============================================================
// SUCH MAN — static file server (Railway "npm start")
// Serves the concept storefront; /healthz returns 200 for Railway.
// ============================================================
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const ROOT = __dirname;

function sendError(res, code, message) {
  res.writeHead(code, { "Content-Type": "text/plain; charset=utf-8" });
  res.end(message);
}

function serveStatic(res, filePath, contentType) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      if (err.code === "ENOENT") return sendError(res, 404, "Not found");
      return sendError(res, 500, "Server error");
    }
    res.writeHead(200, {
      "Content-Type": contentType || "application/octet-stream",
      "Cache-Control": "no-cache",
    });
    res.end(data);
  });
}

const server = http.createServer((req, res) => {
  // health check (Railway)
  if (req.url === "/healthz" || req.url === "/_health") {
    return res.writeHead(200, { "Content-Type": "text/plain" }).end("READY");
  }

  let urlPath = req.url === "/" ? "/index.html" : req.url.split("?")[0];
  let filePath = path.join(ROOT, urlPath);

  // prevent path traversal
  if (!filePath.startsWith(ROOT)) return sendError(res, 403, "Forbidden");

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      // SPA fallback
      return serveStatic(res, path.join(ROOT, "index.html"), "text/html");
    }

    const ext = path.extname(filePath).toLowerCase();
    const types = {
      ".html": "text/html; charset=utf-8",
      ".css": "text/css; charset=utf-8",
      ".js": "text/javascript; charset=utf-8",
      ".json": "application/json; charset=utf-8",
      ".svg": "image/svg+xml",
      ".png": "image/png",
      ".ico": "image/x-icon",
      ".txt": "text/plain; charset=utf-8",
    };
    serveStatic(res, filePath, types[ext] || "application/octet-stream");
  });
});

server.listen(PORT, () => {
  console.log(`SUCH MAN storefront running on port ${PORT}`);
});
