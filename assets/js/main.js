(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var navigation = document.querySelector(".primary-nav");
  var navigationLinks = Array.prototype.slice.call(document.querySelectorAll('.primary-nav a[href^="#"]'));
  var scrollTopLinks = Array.prototype.slice.call(document.querySelectorAll("[data-scroll-top], .wordmark[href='#top']"));
  var floatingScrollTop = document.querySelector(".back-to-top");

  function setNavigation(open) {
    if (!toggle || !navigation) return;

    toggle.setAttribute("aria-expanded", String(open));
    navigation.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);

    var label = toggle.querySelector(".sr-only");
    if (label) label.textContent = open ? "Close navigation" : "Open navigation";
  }

  if (toggle && navigation) {
    toggle.addEventListener("click", function () {
      setNavigation(toggle.getAttribute("aria-expanded") !== "true");
    });

    navigation.addEventListener("click", function (event) {
      if (event.target.closest("a")) setNavigation(false);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setNavigation(false);
        toggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 980) setNavigation(false);
    });
  }

  function scrollToTop(event) {
    if (event) event.preventDefault();

    var reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: reducedMotion ? "auto" : "smooth"
    });

    if (history.replaceState) {
      try {
        history.replaceState(null, "", window.location.pathname + window.location.search);
      } catch (error) {
        // Scrolling still works when the page is opened directly from the filesystem.
      }
    }
    setNavigation(false);
  }

  scrollTopLinks.forEach(function (link) {
    link.addEventListener("click", scrollToTop);
  });

  function updateScrollTopVisibility() {
    if (!floatingScrollTop) return;
    floatingScrollTop.classList.toggle("is-visible", window.scrollY > 520);
  }

  window.addEventListener("scroll", updateScrollTopVisibility, { passive: true });
  updateScrollTopVisibility();

  if ("IntersectionObserver" in window && navigationLinks.length) {
    var sections = navigationLinks
      .map(function (link) { return document.querySelector(link.getAttribute("href")); })
      .filter(Boolean);

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;

        navigationLinks.forEach(function (link) {
          var active = link.getAttribute("href") === "#" + entry.target.id;
          link.classList.toggle("is-active", active);
          if (active) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        });
      });
    }, {
      rootMargin: "-25% 0px -60% 0px",
      threshold: 0
    });

    sections.forEach(function (section) { observer.observe(section); });
  }
})();
