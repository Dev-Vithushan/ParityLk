const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector("#site-nav");
const year = document.querySelector("[data-year]");
const form = document.querySelector("[data-contact-form]");
const formStatus = document.querySelector("[data-form-status]");
const copyEmailButton = document.querySelector("[data-copy-email]");
const heroSlide = document.querySelector("[data-hero-slide]");
const emailAddress = "info@paritylk.com";
const heroMessages = [
  "We build websites",
  "We build mobile apps",
  "We create social media content",
  "We deploy cloud services",
  "We monitor software solutions",
];
const animatedElements = document.querySelectorAll(
  ".proof-grid > div, .section-heading, .summary-card, .service-card, .course-card, .career-card, .cloud-checklist > article, .support-panel, .launch-stats > div, .contact-form, .cta-band, .blog-card"
);
const header = document.querySelector("[data-header]");
const scrollProgress = document.querySelector("[data-scroll-progress]");
const hero = document.querySelector(".hero");
const heroContent = document.querySelector(".hero-content");
const counters = document.querySelectorAll("[data-count-to]");
const glowCards = document.querySelectorAll(
  ".service-card, .course-card, .career-card, .cloud-checklist article"
);
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (year) {
  year.textContent = new Date().getFullYear();
}

if (heroSlide) {
  heroSlide.textContent = heroMessages[0];

  if (!prefersReducedMotion.matches) {
    let heroSlideIndex = 0;

    window.setInterval(() => {
      heroSlideIndex = (heroSlideIndex + 1) % heroMessages.length;

      heroSlide.classList.remove("is-changing");
      void heroSlide.offsetWidth;
      heroSlide.textContent = heroMessages[heroSlideIndex];
      heroSlide.classList.add("is-changing");
    }, 2800);
  }
}

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  nav.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      nav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

if (form && formStatus) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!form.reportValidity()) {
      return;
    }

    const data = new FormData(form);
    const name = data.get("name");
    const sender = data.get("email");
    const company = data.get("company") || "Not provided";
    const phone = data.get("phone") || "Not provided";
    const project = data.get("project");
    const timeline = data.get("timeline");
    const budget = data.get("budget") || "Not provided";
    const message = data.get("message");
    const subject = encodeURIComponent(`ParityLk project inquiry - ${project}`);
    const body = encodeURIComponent(
      [
        "ParityLk project inquiry",
        "",
        `Name: ${name}`,
        `Email: ${sender}`,
        `Company: ${company}`,
        `Phone: ${phone}`,
        `Project type: ${project}`,
        `Timeline: ${timeline}`,
        `Budget / course fee range: ${budget}`,
        "",
        "Project brief:",
        `${message}`,
      ].join("\n")
    );

    formStatus.textContent = "Opening your email app...";
    window.location.href = `mailto:${emailAddress}?subject=${subject}&body=${body}`;
  });
}

if (copyEmailButton) {
  copyEmailButton.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(emailAddress);
      copyEmailButton.textContent = "Address copied";
      copyEmailButton.classList.add("is-copied");
      setTimeout(() => {
        copyEmailButton.textContent = "Copy address";
        copyEmailButton.classList.remove("is-copied");
      }, 1800);
    } catch {
      window.location.href = `mailto:${emailAddress}`;
    }
  });
}

if (animatedElements.length) {
  const groupCounts = new Map();

  animatedElements.forEach((element) => {
    const group = element.parentElement;
    const position = groupCounts.get(group) || 0;
    groupCounts.set(group, position + 1);

    element.classList.add("animate-ready");
    element.style.setProperty("--delay", `${Math.min(position * 80, 320)}ms`);
  });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -12% 0px", threshold: 0.12 }
    );

    animatedElements.forEach((element) => observer.observe(element));
  } else {
    animatedElements.forEach((element) => element.classList.add("is-visible"));
  }
}

if (header || scrollProgress || heroContent) {
  let scrollTicking = false;

  const renderScroll = () => {
    scrollTicking = false;
    const scrolled = window.scrollY;

    if (header) {
      header.classList.toggle("is-scrolled", scrolled > 24);
    }

    if (scrollProgress) {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const progress = scrollable > 0 ? Math.min(scrolled / scrollable, 1) : 0;
      scrollProgress.style.setProperty("--progress", progress.toFixed(4));
    }

    if (heroContent && hero && !prefersReducedMotion.matches) {
      const heroDepth = Math.min(scrolled, hero.offsetHeight);
      heroContent.style.setProperty("--hero-parallax", `${(heroDepth * 0.18).toFixed(1)}px`);
    }
  };

  const onScroll = () => {
    if (scrollTicking) {
      return;
    }

    scrollTicking = true;
    window.requestAnimationFrame(renderScroll);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  renderScroll();
}

if (counters.length && "IntersectionObserver" in window) {
  const runCount = (element) => {
    const target = Number(element.dataset.countTo);
    const suffix = element.dataset.countSuffix || "";

    if (!Number.isFinite(target)) {
      return;
    }

    if (prefersReducedMotion.matches) {
      element.textContent = `${target}${suffix}`;
      return;
    }

    const duration = 1100;
    const start = performance.now();
    element.classList.add("is-counting");

    const step = (now) => {
      const elapsed = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - elapsed, 3);
      element.textContent = `${Math.round(target * eased)}${elapsed === 1 ? suffix : ""}`;

      if (elapsed < 1) {
        window.requestAnimationFrame(step);
      }
    };

    window.requestAnimationFrame(step);
  };

  const counterObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          runCount(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.6 }
  );

  counters.forEach((counter) => {
    counter.textContent = "0";
    counterObserver.observe(counter);
  });
}

if (glowCards.length && window.matchMedia("(hover: hover)").matches) {
  glowCards.forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const bounds = card.getBoundingClientRect();
      card.style.setProperty("--pointer-x", `${event.clientX - bounds.left}px`);
      card.style.setProperty("--pointer-y", `${event.clientY - bounds.top}px`);
    });

    card.addEventListener("pointerleave", () => {
      card.style.removeProperty("--pointer-x");
      card.style.removeProperty("--pointer-y");
    });
  });
}
