const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector("#site-nav");
const routeLinks = document.querySelectorAll("a[href^='/']");
const navLinks = document.querySelectorAll(".site-nav a[href^='/']");
const year = document.querySelector("[data-year]");
const form = document.querySelector("[data-contact-form]");
const formStatus = document.querySelector("[data-form-status]");
const copyEmailButton = document.querySelector("[data-copy-email]");
const heroSlide = document.querySelector("[data-hero-slide]");
const heroImage = document.querySelector("[data-hero-image]");
const emailAddress = "info@paritylk.com";
const heroSlides = [
  {
    message: "We build websites",
    image: "assets/images/hero/hero-websites.png",
    alt: "Dark website design workspace with responsive web screens and delivery tools.",
  },
  {
    message: "We build mobile apps",
    image: "assets/images/hero/hero-mobile-apps.png",
    alt: "Dark mobile app development workspace with smartphone interfaces and code.",
  },
  {
    message: "We create social media content",
    image: "assets/images/hero/hero-content.png",
    alt: "Dark content creation workspace with planning boards, editing timeline, and social media analytics.",
  },
  {
    message: "We deploy cloud services",
    image: "assets/images/hero/hero-cloud.png",
    alt: "Dark cloud deployment workspace with server nodes, containers, and configuration panels.",
  },
  {
    message: "We monitor software solutions",
    image: "assets/images/hero/hero-support.png",
    alt: "Dark software monitoring workspace with dashboards, alerts, and support panels.",
  },
];
const routeMap = new Map([
  ["/", "top"],
  ["/services", "services"],
  ["/courses", "courses"],
  ["/cloud", "cloud"],
  ["/careers", "careers"],
  ["/support", "support"],
  ["/contact", "contact"],
]);
const animatedElements = document.querySelectorAll(
  ".proof-grid > div, .section-heading, .service-card, .course-card, .career-card, .cloud-checklist > article, .support-panel, .launch-stats > div, .contact-form"
);

const normalizePath = (path) => {
  const cleanPath = path.replace(/\/+$/, "");
  return cleanPath || "/";
};

const getRoutePath = (link) => normalizePath(new URL(link.href).pathname);

const scrollToRoute = (path, shouldUpdateHistory = true) => {
  const normalizedPath = normalizePath(path);
  const id = routeMap.get(normalizedPath);

  if (!id) {
    return false;
  }

  const target = document.getElementById(id);
  if (!target) {
    return false;
  }

  if (shouldUpdateHistory && normalizePath(window.location.pathname) !== normalizedPath) {
    window.history.pushState({ path: normalizedPath }, "", normalizedPath);
  }

  target.scrollIntoView({ behavior: "smooth", block: "start" });
  return true;
};

if (year) {
  year.textContent = new Date().getFullYear();
}

if (heroSlide) {
  heroSlide.textContent = heroSlides[0].message;

  heroSlides.slice(1).forEach((slide) => {
    const image = new Image();
    image.src = slide.image;
  });

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    let heroSlideIndex = 0;

    window.setInterval(() => {
      heroSlideIndex = (heroSlideIndex + 1) % heroSlides.length;
      const activeSlide = heroSlides[heroSlideIndex];

      heroSlide.classList.remove("is-changing");
      void heroSlide.offsetWidth;
      heroSlide.textContent = activeSlide.message;
      heroSlide.classList.add("is-changing");

      if (heroImage) {
        heroImage.classList.add("is-changing");
        heroImage.onload = () => {
          heroImage.classList.remove("is-changing");
        };
        heroImage.src = activeSlide.image;
        heroImage.alt = activeSlide.alt;
      }
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

if (routeLinks.length) {
  routeLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      if (
        event.defaultPrevented ||
        event.metaKey ||
        event.ctrlKey ||
        event.shiftKey ||
        event.altKey ||
        link.target === "_blank"
      ) {
        return;
      }

      const routePath = getRoutePath(link);

      if (!routeMap.has(routePath)) {
        return;
      }

      event.preventDefault();
      scrollToRoute(routePath);
    });
  });

  window.addEventListener("popstate", () => {
    scrollToRoute(window.location.pathname, false);
  });

  if (routeMap.has(normalizePath(window.location.pathname))) {
    window.requestAnimationFrame(() => {
      scrollToRoute(window.location.pathname, false);
    });
  }
}

if (navLinks.length) {
  const navMap = new Map();
  navLinks.forEach((link) => {
    const id = routeMap.get(getRoutePath(link));
    const section = document.getElementById(id);
    if (section) {
      navMap.set(id, link);
    }
  });

  const setActiveNav = (id) => {
    navLinks.forEach((link) => {
      const isActive = routeMap.get(getRoutePath(link)) === id;
      link.classList.toggle("is-active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  if ("IntersectionObserver" in window && navMap.size) {
    const visibleSections = new Map();
    const navObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const id = entry.target.id;
          if (entry.isIntersecting) {
            visibleSections.set(id, entry.intersectionRatio);
          } else {
            visibleSections.delete(id);
          }
        });

        const active = [...visibleSections.entries()].sort((a, b) => b[1] - a[1])[0];
        if (active) {
          setActiveNav(active[0]);
        }
      },
      { rootMargin: "-28% 0px -52% 0px", threshold: [0.1, 0.25, 0.5, 0.75] }
    );

    navMap.forEach((_, id) => navObserver.observe(document.getElementById(id)));
  }
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
  animatedElements.forEach((element, index) => {
    element.classList.add("animate-ready");
    element.style.setProperty("--delay", `${Math.min(index * 45, 220)}ms`);
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
