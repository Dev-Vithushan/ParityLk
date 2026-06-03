const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector("#site-nav");
const navLinks = document.querySelectorAll(".site-nav a[href^='#']");
const year = document.querySelector("[data-year]");
const form = document.querySelector("[data-contact-form]");
const formStatus = document.querySelector("[data-form-status]");
const copyEmailButton = document.querySelector("[data-copy-email]");
const emailAddress = "info@paritylk.com";
const animatedElements = document.querySelectorAll(
  ".proof-grid > div, .section-heading, .service-card, .course-card, .cloud-checklist > article, .support-panel, .launch-stats > div, .contact-form"
);

if (year) {
  year.textContent = new Date().getFullYear();
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

if (navLinks.length) {
  const navMap = new Map();
  navLinks.forEach((link) => {
    const id = link.getAttribute("href").slice(1);
    const section = document.getElementById(id);
    if (section) {
      navMap.set(id, link);
    }
  });

  const setActiveNav = (id) => {
    navLinks.forEach((link) => {
      const isActive = link.getAttribute("href") === `#${id}`;
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
