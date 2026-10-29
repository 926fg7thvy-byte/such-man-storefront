/* ============================================================
   SUCH MAN — app.js
   Product card front/back swap, toast, email signup, scroll fade-up.
   ============================================================ */

(function () {
  "use strict";

  // ---- Product card interactions: FRONT/BACK swap ----

  var cards = document.querySelectorAll(".product-card");

  cards.forEach(function (card) {
    var frontView = card.querySelector(".product-front");
    var backView = card.querySelector(".product-back");
    var swapBtn = card.querySelector(".product-swap-btn");
    var concept = card.getAttribute("data-concept");

    function updateSwapIcon() {
      var isFront = frontView.style.opacity !== "0";
      var icon = swapBtn.querySelector("svg");
      if (isFront) {
        icon.setAttribute("viewBox", "0 0 24 24");
        icon.innerHTML = '<path d="M7 16l-4-4 4-4"/><path d="M7 8h10"/>';
      } else {
        icon.setAttribute("viewBox", "0 0 24 24");
        icon.innerHTML = '<path d="M7 16l-4-4 4-4"/><path d="M7 8h10"/>';
      }
    }

    // Click on card opens a detail modal
    card.addEventListener("click", function () {
      openDetail(concept);
    });

    // Swap button (within the card) toggles front/back
    if (swapBtn) {
      swapBtn.addEventListener("click", function (event) {
        event.stopPropagation();
        var isFrontVisible = frontView.style.opacity !== "0";
        frontView.style.opacity = isFrontVisible ? "0" : "1";
        frontView.style.transform = isFrontVisible ? "scale(0.95)" : "scale(1)";
        backView.style.opacity = isFrontVisible ? "1" : "0";
        backView.style.transform = isFrontVisible ? "scale(1)" : "scale(0.95)";
        updateSwapIcon();
      });
    }
  });

  // ---- Detail modal (overlay) ----

  var detailOverlay = document.createElement("div");
  detailOverlay.setAttribute("id", "concept-detail");
  detailOverlay.setAttribute("role", "dialog");
  detailOverlay.setAttribute("aria-modal", "true");
  detailOverlay.setAttribute("aria-hidden", "true");
  detailOverlay.setAttribute("tabindex", "-1");
  detailOverlay.className = "detail-overlay";

  var detailSheet = document.createElement("div");
  detailSheet.className = "detail-sheet";
  detailOverlay.appendChild(detailSheet);

  var detailViewport = document.createElement("div");
  detailViewport.className = "detail-viewport";
  detailSheet.appendChild(detailViewport);

  var detailViews = document.createElement("div");
  detailViews.className = "detail-views";
  detailViewport.appendChild(detailViews);

  var detailViewFront = document.createElement("div");
  detailViewFront.className = "detail-view";
  detailViewFront.innerHTML =
    '<div class="viewtag">Front view</div><img id="detail-front" src="" alt="">';
  detailViews.appendChild(detailViewFront);

  var detailViewBack = document.createElement("div");
  detailViewBack.className = "detail-view";
  detailViewBack.innerHTML =
    '<div class="viewtag">Back view</div><img id="detail-back" src="" alt="">';
  detailViews.appendChild(detailViewBack);

  var detailSwap = document.createElement("div");
  detailSwap.className = "detail-swap";
  detailSwap.setAttribute("role", "button");
  detailSwap.setAttribute("aria-label", "Swap front view to back view");
  detailSwap.tabIndex = "0";
  detailSwap.innerHTML =
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M7 16l-4-4 4-4"/><path d="M7 8h10"/></svg>';
  detailViewport.appendChild(detailSwap);

  var detailCraft = document.createElement("div");
  detailCraft.className = "detail-craft";
  detailSheet.appendChild(detailCraft);

  var detailKicker = document.createElement("p");
  detailKicker.className = "mono";
  detailCraft.appendChild(detailKicker);

  var detailTitle = document.createElement("h3");
  detailCraft.appendChild(detailTitle);

  var detailDesc = document.createElement("p");
  detailCraft.appendChild(detailDesc);

  var detailSpec = document.createElement("div");
  detailSpec.className = "detail-spec";
  detailCraft.appendChild(detailSpec);

  var detailClose = document.createElement("button");
  detailClose.className = "btn";
  detailClose.id = "detail-close";
  detailClose.textContent = "Close";
  detailCraft.appendChild(detailClose);

  document.body.appendChild(detailOverlay);

  var toast = document.getElementById("toast");
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- Concept data (verbatim phrase wording) ----

  var CONCEPTS = {
    "such-man-knows-code": {
      phrase: "SUCH MAN KNOWS CODE",
      kicker: "Drop 001 · The signature",
      desc: "The code is written in who we are. A clipped chest mark and a phrase set across the upper back.",
      fabric: "Washed-black heavyweight cotton",
      front: "Chest mark + stacked 'KNOWS CODE'",
      back: "Case-file stamp, 'NO EVIDENCE · NO CASE' at the button",
      edition: "Drop 001 · 25 numbered pieces"
    },
    "such-man-she-a-mi-cousin": {
      phrase: "SUCH MAN, SHE A MI COUSIN",
      kicker: "Drop 002 · The family story",
      desc: "A wide type lockup across the front; the family line sits on the upper back.",
      fabric: "Bone heavyweight cotton",
      front: "Wide type lockup across the front",
      back: "Family-line graphic on the upper back",
      edition: "Drop 002 · 25 numbered pieces"
    },
    "such-man-deh-deh": {
      phrase: "SUCH MAN DEH DEH",
      kicker: "Drop 003 · The disappearing act",
      desc: "The phrase in white; the question in ochre; a corner of island landscape with a question marker.",
      fabric: "Faded charcoal heavyweight cotton",
      front: "White phrase + ochre question mark",
      back: "Island outline with a question marker",
      edition: "Drop 003 · 25 numbered pieces"
    },
    "mi-innocent": {
      phrase: "MI INNOCENT",
      kicker: "Drop 004 · The case file",
      desc: "A proofreader&rsquo;s line beneath &lsquo;MI&rsquo;; &lsquo;NO COMMENT&rsquo; under &lsquo;INNOCENT&rsquo;; the case file stamped on the back.",
      fabric: "Charcoal heavyweight cotton",
      front: "Proofreader&rsquo;s line + &lsquo;NO COMMENT&rsquo;",
      back: "Case-file stamp, &lsquo;CASE STATUS: DISMISSED&rsquo;",
      edition: "Drop 004 · 25 numbered pieces"
    },
    "just-a-friend": {
      phrase: "JUST A FRIEND",
      kicker: "Drop 005 · The denial",
      desc: "A huge &lsquo;FRIEND&rsquo; inside a dotted surveillance ring, with a quiet advisory line beneath.",
      fabric: "Stone heavyweight cotton",
      front: "Surveillance-ring graphic around FRIEND",
      back: "Ring motif and the advisory line",
      edition: "Drop 005 · 25 numbered pieces"
    },
    "no-evidence-no-case": {
      phrase: "NO EVIDENCE, NO CASE",
      kicker: "Drop 006 · The exoneration",
      desc: "&ldquo;NO EVIDENCE&rdquo; above the dominant &lsquo;NO CASE&rsquo;; the back carries a double-ring case-file stamp.",
      fabric: "Washed-black heavyweight cotton",
      front: "Huge &lsquo;NO CASE&rsquo; + &lsquo;NO EVIDENCE&rsquo;",
      back: "Double-ring case-file stamp",
      edition: "Drop 006 · 25 numbered pieces"
    }
  };

  // ---- Modal open/close ----

  var lastFocusedElement = null;

  function openDetail(concept) {
    var data = CONCEPTS[concept];
    if (!data) return;

    lastFocusedElement = document.activeElement;

    detailTitle.textContent = data.phrase;
    detailKicker.textContent = data.kicker;
    detailDesc.textContent = data.desc;
    detailSpec.innerHTML =
      '<div><dt>Fabric</dt><dd id="concept-fabric"></dd></div>' +
      '<div><dt>Front</dt><dd id="concept-front"></dd></div>' +
      '<div><dt>Back</dt><dd id="concept-back"></dd></div>' +
      '<div><dt>Edition</dt><dd id="concept-edition"></dd></div>';
    document.getElementById("concept-fabric").textContent = data.fabric;
    document.getElementById("concept-front").textContent = data.front;
    document.getElementById("concept-back").textContent = data.back;
    document.getElementById("concept-edition").textContent = data.edition;

    // Use product mockup images for detail view
    var frontSrc = "assets/product-mockups/" + concept + "-front-mockup.png";
    var backSrc = "assets/product-mockups/" + concept + "-back-mockup.png";
    detailViewFront.querySelector("img").src = frontSrc;
    detailViewBack.querySelector("img").src = backSrc;
    detailViewFront.style.opacity = "1";
    detailViewFront.style.transform = "scale(1)";
    detailViewBack.style.opacity = "0";
    detailViewBack.style.transform = "scale(0.95)";
    currentConcept = concept;

    detailOverlay.setAttribute("aria-hidden", "false");
    detailOverlay.setAttribute("tabindex", "-1");
    detailOverlay.scrollTop = 0;
    document.body.style.overflow = "hidden";
    toast.classList.remove("show");

    setTimeout(function () {
      var swap = detailOverlay.querySelector(".detail-swap");
      if (swap) {
        swap.setAttribute("tabindex", "-1");
        swap.focus();
        swap.setAttribute("tabindex", "0");
      }
    }, 50);
  }

  function closeDetail() {
    detailOverlay.setAttribute("aria-hidden", "true");
    detailOverlay.setAttribute("tabindex", "-1");
    document.body.style.overflow = "";
    if (lastFocusedElement && lastFocusedElement.focus) {
      lastFocusedElement.focus();
    }
  }

  // ---- Card click opens detail ----

  var conceptCards = document.querySelectorAll(".product-card");
  conceptCards.forEach(function (card) {
    card.addEventListener("click", function () {
      openDetail(card.getAttribute("data-concept"));
    });
  });

  // ---- Close: Escape / overlay / close button ----

  if (detailClose) {
    detailClose.addEventListener("click", closeDetail);
  }
  detailOverlay.addEventListener("click", function (event) {
    if (event.target === detailOverlay) closeDetail();
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && detailOverlay.getAttribute("aria-hidden") !== "true") {
      closeDetail();
    }
  });

  // ---- Detail swap (within modal) ----

  var currentConcept = null;
  if (detailSwap) {
    detailSwap.addEventListener("click", function () {
      if (!currentConcept) return;
      var frontImg = document.getElementById("detail-front");
      var backImg = document.getElementById("detail-back");
      var isFrontShowing = frontImg.style.opacity !== "0";
      frontImg.style.opacity = isFrontShowing ? "0" : "1";
      frontImg.style.transform = isFrontShowing ? "scale(0.95)" : "scale(1)";
      backImg.style.opacity = isFrontShowing ? "1" : "0";
      backImg.style.transform = isFrontShowing ? "scale(1)" : "scale(0.95)";
    });
  }

  // ---- Toast ----

  setTimeout(function () {
    toast.classList.add("show");
  }, 1400);

  // ---- Email signup ----

  var emailForm = document.getElementById("email-form");
  var emailInput = document.getElementById("email-input");
  var emailError = document.getElementById("email-error");

  if (emailForm && emailInput) {
    emailForm.addEventListener("submit", function (event) {
      event.preventDefault();
      var email = emailInput.value.trim();
      if (!email) {
        emailError.textContent = "Please enter your email address.";
        emailInput.focus();
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        emailInput.focus();
        return;
      }
      emailError.textContent = "";
      emailForm.reset();
      toast.textContent = "Joined the crew — welcome.";
      toast.classList.add("show");
      emailInput.focus();
    });
  }

})();
