/* ============================================================
   SUCH MAN — app.js
   Concept detail dialog (modal), photo gallery, and toast.
   Redesigned: full-bleed original artwork, editorial layout.
   ============================================================ */

(function () {
  "use strict";

  var detail = document.getElementById("concept-detail");
  var detailFront = document.getElementById("detail-front");
  var detailBack = document.getElementById("detail-back");
  var detailTitle = document.getElementById("concept-title");
  var detailKicker = document.getElementById("concept-kicker");
  var detailDesc = document.getElementById("concept-desc");
  var detailFabric = document.getElementById("concept-fabric");
  var detailFrontLabel = document.getElementById("concept-front");
  var detailBackLabel = document.getElementById("concept-back");
  var detailEdition = document.getElementById("concept-edition");
  var detailClose = document.getElementById("detail-close");
  var detailSwap = document.getElementById("detail-swap");
  var toast = document.getElementById("toast");
  var yearEl = document.getElementById("year");

  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- concept data (verbatim phrase wording, concept-stage labels) ----

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
      desc: "A proofreader's line beneath 'MI'; 'NO COMMENT' under 'INNOCENT'; the case file stamped on the back.",
      fabric: "Charcoal heavyweight cotton",
      front: "Proofreader's line + 'NO COMMENT'",
      back: "Case-file stamp, 'CASE STATUS: DISMISSED'",
      edition: "Drop 004 · 25 numbered pieces"
    },
    "just-a-friend": {
      phrase: "JUST A FRIEND",
      kicker: "Drop 005 · The denial",
      desc: "A huge 'FRIEND' inside a dotted surveillance ring, with a quiet advisory line beneath.",
      fabric: "Stone heavyweight cotton",
      front: "Surveillance-ring graphic around FRIEND",
      back: "Ring motif and the advisory line",
      edition: "Drop 005 · 25 numbered pieces"
    },
    "no-evidence-no-case": {
      phrase: "NO EVIDENCE, NO CASE",
      kicker: "Drop 006 · The exoneration",
      desc: "\"NO EVIDENCE\" above the dominant 'NO CASE'; the back carries a double-ring case-file stamp.",
      fabric: "Washed-black heavyweight cotton",
      front: "Huge 'NO CASE' + 'NO EVIDENCE'",
      back: "Double-ring case-file stamp",
      edition: "Drop 006 · 25 numbered pieces"
    }
  };

  // ---- modal with proper keyboard accessibility and front/back swap ----

  var lastFocusedElement = null;
  var currentConcept = null;

  function openDetail(concept) {
    var data = CONCEPTS[concept];
    if (!data) return;

    lastFocusedElement = document.activeElement;

    detailTitle.textContent = data.phrase;
    detailKicker.textContent = data.kicker;
    detailDesc.textContent = data.desc;
    detailFabric.textContent = data.fabric;
    detailFrontLabel.textContent = data.front;
    detailBackLabel.textContent = data.back;
    detailEdition.textContent = data.edition;
    detailFront.src = "assets/product/" + concept + "/front.svg";
    detailBack.src = "assets/product/" + concept + "/back.svg";
    currentConcept = concept;
    detail.setAttribute("aria-hidden", "false");
    detail.setAttribute("tabindex", "-1");
    detail.scrollTop = 0;
    document.body.style.overflow = "hidden";
    toast.classList.remove("show");

    // Focus the swap button inside the dialog
    setTimeout(function () {
      var swap = detail.querySelector(".detail-swap");
      if (swap) {
        swap.setAttribute("tabindex", "-1");
        swap.focus();
        swap.setAttribute("tabindex", "0");
      }
    }, 50);
  }

  function closeDetail() {
    detail.setAttribute("aria-hidden", "true");
    detail.setAttribute("tabindex", "-1");
    document.body.style.overflow = "";
    if (lastFocusedElement && lastFocusedElement.focus) {
      lastFocusedElement.focus();
    }
  }

  // ---- card click opens detail ----

  var conceptCards = Array.prototype.slice.call(
    document.querySelectorAll(".products .product")
  );

  conceptCards.forEach(function (card) {
    card.addEventListener("click", function () {
      openDetail(card.getAttribute("data-concept"));
    });
  });

  // ---- close: Escape / overlay / close button ----

  if (detailClose) {
    detailClose.addEventListener("click", function () { closeDetail(); });
  }
  if (detail) {
    detail.addEventListener("click", function (event) {
      if (event.target === detail) closeDetail();
    });
  }
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && detail.getAttribute("aria-hidden") !== "true") {
      closeDetail();
    }
  });

  // ---- detail-swap: swap front/back artwork ----

  if (detailSwap) {
    detailSwap.addEventListener("click", function () {
      if (!currentConcept) return;
      var front = detailFront.src;
      var back = detailBack.src;
      var isFrontShowing = front.includes("front.svg");
      detailFront.src = isFrontShowing ? "assets/product/" + currentConcept + "/back.svg" : "assets/product/" + currentConcept + "/front.svg";
      detailBack.src = isFrontShowing ? "assets/product/" + currentConcept + "/front.svg" : "assets/product/" + currentConcept + "/back.svg";
    });
  }

  // ---- toast (simple, non-intrusive) ----

  setTimeout(function () {
    toast.classList.add("show");
  }, 1400);

})();
