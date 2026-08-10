#!/usr/bin/env python3
"""Generate ParityLk inner pages from a shared shell."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from visuals import VISUALS

ROOT = "/Users/vithushan/Documents/ParityLk"
VERSION = "multipage-1"

NAV = [
    ("/", "Home"),
    ("/services/", "Services"),
    ("/cloud/", "Cloud"),
    ("/support/", "Support"),
    ("/courses/", "Courses"),
    ("/careers/", "Careers"),
]


def nav_markup(active):
    rows = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        rows.append(f'            <a href="{href}"{current}>{label}</a>')
    cta_current = ' aria-current="page"' if active == "/contact/" else ""
    return "\n".join(rows), cta_current


SHELL = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <base href="/">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://paritylk.com{path}">
    <meta name="theme-color" content="#111111">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="assets/images/paritylk-logo-official.png">
    <link rel="icon" href="assets/images/paritylk-favicon.png?v=4" type="image/png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
      href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap"
      rel="stylesheet"
    >
    <link rel="stylesheet" href="assets/css/styles.css?v={version}">
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>

    <header class="site-header" data-header>
      <div class="container header-inner">
        <a class="brand" href="/" aria-label="ParityLk home">
          <img
            class="brand-logo"
            src="assets/images/paritylk-navbar-logo.png"
            width="128"
            height="54"
            alt=""
            aria-hidden="true"
          >
        </a>

        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
          <span class="nav-toggle-line"></span>
          <span class="nav-toggle-line"></span>
          <span class="sr-only">Toggle navigation</span>
        </button>

        <nav class="site-nav" id="site-nav" aria-label="Primary navigation">
          <div class="nav-links">
{nav}
          </div>
          <a class="nav-cta" href="/contact/"{cta_current}>Contact</a>
        </nav>
      </div>
      <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
    </header>

    <main id="main">
      <section class="page-hero" aria-labelledby="page-title">
        <div class="fx-grid" aria-hidden="true"></div>
        <div class="fx-glow fx-glow-a" aria-hidden="true"></div>
        <div class="fx-glow fx-glow-b" aria-hidden="true"></div>
        <div class="fx-line" aria-hidden="true"><span class="fx-traveler"></span></div>

        <div class="container page-hero-layout">
          <div class="page-hero-content">
            <p class="eyebrow">{eyebrow}</p>
            <h1 id="page-title">{heading}</h1>
            <p>{intro}</p>
            <div class="hero-actions">
{actions}
            </div>
          </div>

          <div class="hero-visual" aria-hidden="true">
            <span class="hv-panelgrid"></span>
            <span class="hv-glow hv-glow-a"></span>
            <span class="hv-glow hv-glow-b"></span>
            <svg viewBox="0 0 460 460" xmlns="http://www.w3.org/2000/svg" role="presentation">
              <defs>
                <linearGradient id="hvGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#f6c90e"></stop>
                  <stop offset="45%" stop-color="#ffb000"></stop>
                  <stop offset="100%" stop-color="#fff3b0"></stop>
                </linearGradient>
              </defs>
{visual}
            </svg>
            <span class="hv-badge"><span class="dot"></span> {badge}</span>
          </div>
        </div>
      </section>

{body}
    </main>

    <footer class="site-footer" aria-labelledby="footer-title">
      <div class="container footer-main">
        <div class="footer-brand">
          <a class="footer-logo" href="/" aria-label="ParityLk home">
            <img
              src="assets/images/paritylk-navbar-logo.png"
              width="128"
              height="54"
              alt=""
              aria-hidden="true"
            >
          </a>
          <h2 id="footer-title">Digital delivery for growing teams.</h2>
          <p>
            Websites, mobile apps, social content, deployments, monitoring, and practical
            software support for companies that need reliable execution.
          </p>
        </div>

        <nav class="footer-links" aria-label="Footer navigation">
          <div>
            <h3>Explore</h3>
            <a href="/services/">Services</a>
            <a href="/cloud/">Cloud</a>
            <a href="/support/">Our work</a>
            <a href="/courses/">Courses</a>
            <a href="/careers/">Careers</a>
          </div>
          <div>
            <h3>Services</h3>
            <a href="/services/">Websites</a>
            <a href="/services/">Mobile apps</a>
            <a href="/services/">Content creation</a>
            <a href="/services/">Monitoring</a>
          </div>
          <div>
            <h3>Careers</h3>
            <a href="/careers/">React Native Intern</a>
            <a href="/careers/">Flutter Intern</a>
            <a href="https://forms.gle/r8dBgu6D9do1oTmeA" target="_blank" rel="noopener">Apply interest</a>
          </div>
          <div>
            <h3>Contact</h3>
            <a href="mailto:info@paritylk.com">info@paritylk.com</a>
            <a href="/contact/">Request a consultation</a>
            <a href="/">Home</a>
          </div>
        </nav>
      </div>

      <div class="container footer-bottom">
        <p>&copy; <span data-year></span> ParityLk. All rights reserved.</p>
      </div>
    </footer>

    <script src="assets/js/main.js?v={version}"></script>
  </body>
</html>
"""

CTA = """      <section class="section{modifier}" aria-labelledby="cta-title">
        <div class="container">
          <div class="cta-band">
            <div>
              <h2 id="cta-title">{title}</h2>
              <p>{copy}</p>
            </div>
            <div class="cta-actions">
              <a class="button button-primary" href="/contact/">Start a project</a>
              <a class="button button-secondary" href="/">Back to home</a>
            </div>
          </div>
        </div>
      </section>
"""

SERVICE_CARDS = """      <section class="section" aria-label="Services">
        <div class="container service-grid" aria-label="Service list">
          <article class="service-card">
            <span class="service-icon web" aria-hidden="true"></span>
            <h3>Website Development</h3>
            <p>
              We build responsive business websites, landing pages, service pages,
              CMS-ready structures, and performance-focused pages for your domain.
            </p>
          </article>

          <article class="service-card">
            <span class="service-icon app" aria-hidden="true"></span>
            <h3>Mobile App Builds</h3>
            <p>
              We build mobile app screens, prototypes, customer portals, and mobile-first
              experiences that support real business workflows.
            </p>
          </article>

          <article class="service-card">
            <span class="service-icon content" aria-hidden="true"></span>
            <h3>Content Creation</h3>
            <p>
              We create content and help keep your company active on social media with
              posts, service copy, visuals, and consistent publishing plans.
            </p>
          </article>

          <article class="service-card">
            <span class="service-icon cloud" aria-hidden="true"></span>
            <h3>Software Support</h3>
            <p>
              We support software solutions after launch with updates, bug fixes,
              issue checks, user support, and practical maintenance.
            </p>
          </article>

          <article class="service-card">
            <span class="service-icon deploy" aria-hidden="true"></span>
            <h3>Deployment Setup</h3>
            <p>
              We help deploy websites, apps, and software solutions with hosting,
              domains, environments, SSL, launch checks, and release support.
            </p>
          </article>

          <article class="service-card">
            <span class="service-icon support" aria-hidden="true"></span>
            <h3>Monitoring</h3>
            <p>
              We help monitor live solutions with uptime checks, issue tracking,
              deployment verification, and follow-up support after release.
            </p>
          </article>
        </div>
      </section>

"""

CLOUD_BODY = """      <section class="section" aria-labelledby="cloud-title">
        <div class="container split-layout cloud-layout">
          <div class="section-heading align-left">
            <p class="eyebrow">Cloud</p>
            <h2 id="cloud-title">Cloud deployment, configuration, and environment maintenance.</h2>
            <p>
              ParityLk helps deploy websites, apps, and software services with the right
              cloud configuration, then maintains the environment so launches stay stable.
            </p>
            <div class="cloud-providers" aria-label="Cloud platforms supported">
              <span class="cloud-provider provider-aws" aria-label="AWS support">
                <img src="assets/images/cloud/aws.svg" width="512" height="307" alt="AWS logo">
              </span>
              <span class="cloud-provider provider-azure" aria-label="Microsoft Azure support">
                <img src="assets/images/cloud/azure.svg" width="187" height="54" alt="Microsoft Azure logo">
              </span>
              <span class="cloud-provider provider-gcp" aria-label="Google Cloud Platform support">
                <img src="assets/images/cloud/gcp.svg" width="512" height="79" alt="Google Cloud logo">
              </span>
            </div>
            <a class="button button-primary cloud-button" href="/contact/">Request cloud help</a>
          </div>

          <div class="cloud-checklist" aria-label="Cloud support areas">
            <article>
              <span>CONFIG</span>
              <div>
                <h3>Cloud Configuration</h3>
                <p>Set up hosting, DNS, SSL, redirects, storage, access, and environment settings.</p>
              </div>
            </article>
            <article>
              <span>DEPLOY</span>
              <div>
                <h3>Service Deployment</h3>
                <p>Deploy websites, mobile backends, APIs, and software services to cloud-ready environments.</p>
              </div>
            </article>
            <article>
              <span>MAINTAIN</span>
              <div>
                <h3>Environment Maintenance</h3>
                <p>Monitor deployments, fix cloud issues, review uptime, and keep environments working after launch.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

"""

SUPPORT_BODY = """      <section class="section" aria-labelledby="support-areas-title">
        <div class="container section-heading">
          <p class="eyebrow">Support</p>
          <h2 id="support-areas-title">What we watch, fix, and verify.</h2>
          <p>
            Support continues once a website, app, or service is live, so issues get
            checked, fixed, and verified instead of waiting for the next project.
          </p>
        </div>

        <div class="container cloud-checklist" aria-label="Support areas">
          <article>
            <span>UPTIME</span>
            <div>
              <h3>Monitoring</h3>
              <p>Uptime checks, issue tracking, and deployment verification on live solutions.</p>
            </div>
          </article>
          <article>
            <span>FIXES</span>
            <div>
              <h3>Updates and bug fixes</h3>
              <p>Updates, bug fixes, issue checks, and user support as part of practical maintenance.</p>
            </div>
          </article>
          <article>
            <span>RELEASE</span>
            <div>
              <h3>Release support</h3>
              <p>Launch checks, release support, and follow-up after every deployment.</p>
            </div>
          </article>
        </div>
      </section>

      <section class="section section-accent" aria-labelledby="work-title">
        <div class="container support-panel">
          <div>
            <p class="eyebrow">By the numbers</p>
            <h2 id="work-title">Project counts and active customer support.</h2>
          </div>
          <div class="support-content">
            <p>
              ParityLk works with growing companies that need practical digital delivery:
              websites, mobile apps, deployments, monitoring, and active support after launch.
            </p>
            <div class="launch-stats" aria-label="ParityLk project and customer statistics">
              <div>
                <strong data-count-to="3" data-count-suffix="+">3+</strong>
                <span>Active customers</span>
              </div>
              <div>
                <strong data-count-to="5">5</strong>
                <span>Websites delivered</span>
              </div>
              <div>
                <strong data-count-to="2">2</strong>
                <span>Mobile apps built</span>
              </div>
            </div>
          </div>
        </div>
      </section>

"""

COURSES_BODY = """      <section class="section" aria-label="Courses">
        <div class="container course-grid" aria-label="Course list">
          <article class="course-card">
            <div class="course-topline">
              <span class="course-badge">Starter</span>
              <span>For school students</span>
            </div>
            <span class="course-logo">
              <img src="assets/images/courses/python.svg" width="389" height="115" alt="Python logo">
            </span>
            <h3>Basic Python</h3>
            <p>
              Learn Python fundamentals, variables, conditions, loops, functions, and
              simple practice tasks for first-time programmers.
            </p>
            <div class="course-price">
              <strong>LKR 3,499</strong>
              <span>School student price</span>
            </div>
            <a
              class="course-link"
              href="https://docs.google.com/forms/d/17N6wnGqvJgEfEEybqApAn9Lc0SQNRYZYypg23pzFmXQ/viewform"
              target="_blank"
              rel="noopener"
            >
              Enroll interest
            </a>
          </article>

          <article class="course-card">
            <div class="course-topline">
              <span class="course-badge">Popular</span>
              <span>For industry persons</span>
            </div>
            <span class="course-logo">
              <img src="assets/images/courses/openai.svg" width="1180" height="320" alt="OpenAI logo">
            </span>
            <h3>AI Tools Handling</h3>
            <p>
              Use AI tools for workplace writing, research, content ideas, presentations,
              reporting, and responsible day-to-day productivity.
            </p>
            <div class="course-price">
              <strong>LKR 4,999</strong>
              <span>Industry learner price</span>
            </div>
            <a
              class="course-link"
              href="https://docs.google.com/forms/d/17N6wnGqvJgEfEEybqApAn9Lc0SQNRYZYypg23pzFmXQ/viewform"
              target="_blank"
              rel="noopener"
            >
              Enroll interest
            </a>
          </article>

          <article class="course-card">
            <div class="course-topline">
              <span class="course-badge">Workspace</span>
              <span>For industry persons</span>
            </div>
            <span class="course-logo">
              <img src="assets/images/courses/google-workspace.svg" width="3995" height="512" alt="Google Workspace logo">
            </span>
            <h3>Google Workspace Handling</h3>
            <p>
              Build confidence with Gmail, Drive, Docs, Sheets, Slides, Forms, Calendar,
              sharing, and collaboration workflows for professional teams.
            </p>
            <div class="course-price">
              <strong>LKR 4,999</strong>
              <span>Industry learner price</span>
            </div>
            <a
              class="course-link"
              href="https://docs.google.com/forms/d/17N6wnGqvJgEfEEybqApAn9Lc0SQNRYZYypg23pzFmXQ/viewform"
              target="_blank"
              rel="noopener"
            >
              Enroll interest
            </a>
          </article>
        </div>
      </section>

"""

CAREERS_BODY = """      <section class="section" aria-label="Open roles">
        <div class="container careers-grid" aria-label="Open career roles">
          <article class="career-card">
            <div class="career-topline">
              <span class="career-badge">Internship</span>
              <span>Mobile Development</span>
            </div>
            <h3>React Native Intern</h3>
            <p>
              Work with React Native app screens, reusable components, navigation flows,
              API integration support, bug fixing, and mobile-first user experience improvements.
            </p>
            <ul>
              <li>Basic JavaScript or TypeScript knowledge</li>
              <li>Interest in React Native and mobile UI development</li>
              <li>Willingness to learn Git, debugging, and deployment workflows</li>
              <li>Ability to use AI tools responsibly to research, prototype, and improve delivery speed</li>
              <li>Commitment to complete assigned tasks, communicate blockers early, and follow project timelines</li>
              <li>Confidence to speak clearly, share progress, and present completed work to the team</li>
            </ul>
            <a class="career-link" href="https://forms.gle/r8dBgu6D9do1oTmeA" target="_blank" rel="noopener">Apply interest</a>
          </article>

          <article class="career-card">
            <div class="career-topline">
              <span class="career-badge">Internship</span>
              <span>Mobile Development</span>
            </div>
            <h3>Flutter Intern</h3>
            <p>
              Support Flutter mobile app development with interface screens, widgets,
              app state, testing, issue fixes, and release preparation for mobile projects.
            </p>
            <ul>
              <li>Basic Dart or programming fundamentals</li>
              <li>Interest in Flutter widgets, layouts, and mobile app structure</li>
              <li>Comfort learning from code reviews and practical tasks</li>
              <li>Ability to use AI tools responsibly to explore solutions, document ideas, and speed up learning</li>
              <li>Commitment to regular practice, task ownership, and reliable communication during delivery work</li>
              <li>Confidence to speak clearly, join discussions, and present app screens or progress updates</li>
            </ul>
            <a class="career-link" href="https://forms.gle/r8dBgu6D9do1oTmeA" target="_blank" rel="noopener">Apply interest</a>
          </article>

          <article class="career-card">
            <div class="career-topline">
              <span class="career-badge">Internship</span>
              <span>Web Development</span>
            </div>
            <h3>Front-End Web Intern</h3>
            <p>
              Build responsive business websites and landing pages with clean HTML, CSS, and
              JavaScript, then help ship them to real client domains.
            </p>
            <ul>
              <li>Working knowledge of HTML, CSS, and basic JavaScript</li>
              <li>Interest in responsive layouts, accessibility, and page performance</li>
              <li>Willingness to learn Git, code review, and static site deployment</li>
              <li>Ability to use AI tools responsibly to research patterns and speed up delivery</li>
              <li>Attention to detail when matching a design and testing across screen sizes</li>
              <li>Confidence to share progress and walk the team through completed pages</li>
            </ul>
            <a class="career-link" href="https://forms.gle/r8dBgu6D9do1oTmeA" target="_blank" rel="noopener">Apply interest</a>
          </article>

          <article class="career-card">
            <div class="career-topline">
              <span class="career-badge">Internship</span>
              <span>Cloud &amp; Support</span>
            </div>
            <h3>Cloud Support Intern</h3>
            <p>
              Help configure hosting, DNS, and SSL, run deployment checks, and follow up on
              uptime and issue reports for live client services.
            </p>
            <ul>
              <li>Comfort with the command line and basic networking ideas like DNS and HTTPS</li>
              <li>Interest in AWS, Azure, or Google Cloud fundamentals</li>
              <li>Willingness to learn deployment pipelines, environments, and release checks</li>
              <li>Ability to use AI tools responsibly to investigate errors and document fixes</li>
              <li>Care in writing clear issue notes so problems can be traced and verified</li>
              <li>Confidence to report status during an active support or deployment task</li>
            </ul>
            <a class="career-link" href="https://forms.gle/r8dBgu6D9do1oTmeA" target="_blank" rel="noopener">Apply interest</a>
          </article>
        </div>
      </section>

"""

CONTACT_BODY = """      <section class="section" aria-labelledby="contact-title">
        <div class="container contact-layout">
          <div class="section-heading align-left">
            <p class="eyebrow">Direct line</p>
            <h2 id="contact-title">Prefer plain email?</h2>
            <p>
              Write to us directly instead of filling the form. Either way the brief reaches
              the same inbox, and the form simply opens your email app with the details filled in.
            </p>
            <div class="contact-card" aria-label="Direct email contact">
              <div>
                <span class="contact-label">Direct email</span>
                <a class="contact-link" href="mailto:info@paritylk.com">info@paritylk.com</a>
              </div>
              <button class="text-button copy-button" type="button" data-copy-email>
                Copy address
              </button>
            </div>
          </div>

          <form class="contact-form" data-contact-form>
            <div class="form-header">
              <p class="form-kicker">Project intake</p>
              <h3>Request a consultation</h3>
            </div>

            <div class="form-row">
              <label>
                Full name
                <input name="name" type="text" autocomplete="name" placeholder="Your name" required>
              </label>
              <label>
                Email address
                <input name="email" type="email" autocomplete="email" placeholder="you@company.com" required>
              </label>
            </div>

            <div class="form-row">
              <label>
                Company / institute
                <input name="company" type="text" autocomplete="organization" placeholder="Company, school, or campus">
              </label>
              <label>
                Phone
                <input name="phone" type="tel" autocomplete="tel" placeholder="+94 7X XXX XXXX">
              </label>
            </div>

            <div class="form-row">
              <label>
                Project type
                <select name="project" required>
                  <option value="">Select one</option>
                  <option>Website</option>
                  <option>Mobile app</option>
                  <option>Course enrollment</option>
                  <option>Cloud troubleshooting</option>
                  <option>Deployment setup</option>
                  <option>Content creation</option>
                  <option>Support</option>
                  <option>Multiple services</option>
                </select>
              </label>
              <label>
                Timeline
                <select name="timeline" required>
                  <option value="">Select timeline</option>
                  <option>Urgent support</option>
                  <option>1-2 weeks</option>
                  <option>2-4 weeks</option>
                  <option>1-2 months</option>
                  <option>Next course batch</option>
                  <option>Planning stage</option>
                </select>
              </label>
            </div>

            <label>
              Budget / course fee range
              <select name="budget">
                <option value="">Select range</option>
                <option>Under LKR 5,000</option>
                <option>LKR 5,000 - 25,000</option>
                <option>LKR 25,000 - 100,000</option>
                <option>LKR 100,000+</option>
                <option>Need guidance</option>
              </select>
            </label>

            <label>
              Project brief
              <textarea
                name="message"
                rows="5"
                placeholder="Tell us what you need, the course you are interested in, or any domain/cloud issue you want fixed."
                required
              ></textarea>
            </label>

            <div class="form-footer">
              <p>Response target: within one business day.</p>
              <button class="button button-primary form-button" type="submit">Prepare email</button>
            </div>
            <p class="form-status" data-form-status role="status" aria-live="polite"></p>
          </form>
        </div>
      </section>

"""

PAGES = [
    {
        "path": "/services/",
        "dir": "services",
        "title": "Services | Parity Lk",
        "description": "Website development, mobile app builds, content creation, software support, deployment setup, and monitoring from ParityLk.",
        "eyebrow": "Services",
        "heading": "Build, publish, and <span class=\"shine\">keep it running.</span>",
        "intro": "Six delivery services that cover the whole path: design and build, publish to the cloud, then support and monitor what is live.",
        "actions": [
            ('button button-primary', '/contact/', 'Start a project'),
            ('button button-secondary', '/cloud/', 'See cloud work'),
        ],
        "body": SERVICE_CARDS + CTA.format(
            modifier=" section-light",
            title="Need one of these for your team?",
            copy="Send a short brief and we will reply with scope, timeline, and a practical next step.",
        ),
    },
    {
        "path": "/cloud/",
        "dir": "cloud",
        "title": "Cloud | Parity Lk",
        "description": "Cloud configuration, service deployment, and environment maintenance on AWS, Microsoft Azure, and Google Cloud.",
        "eyebrow": "Cloud",
        "heading": "Deploy it properly, then <span class=\"shine\">keep it stable.</span>",
        "intro": "Hosting, DNS, SSL, redirects, storage, and access configured on AWS, Azure, or Google Cloud, with maintenance after the launch.",
        "actions": [
            ('button button-primary', '/contact/', 'Request cloud help'),
            ('button button-secondary', '/support/', 'See support work'),
        ],
        "body": CLOUD_BODY + CTA.format(
            modifier=" section-light",
            title="Stuck on a domain, SSL, or deployment issue?",
            copy="Describe the environment and the error. We check the configuration and give you the fix path.",
        ),
    },
    {
        "path": "/support/",
        "dir": "support",
        "title": "Our work and support | Parity Lk",
        "description": "ParityLk project counts, active customer support, monitoring, bug fixes, and release support after launch.",
        "eyebrow": "Our work",
        "heading": "Delivery that <span class=\"shine\">continues after launch.</span>",
        "intro": "Project counts, active customers, and the support work that keeps live websites, apps, and services running.",
        "actions": [
            ('button button-primary', '/contact/', 'Request support'),
            ('button button-secondary', '/services/', 'View services'),
        ],
        "body": SUPPORT_BODY + CTA.format(
            modifier="",
            title="Something live and broken?",
            copy="Send the issue with the environment details. Urgent support is one of the timeline options on the form.",
        ),
    },
    {
        "path": "/courses/",
        "dir": "courses",
        "title": "Courses | Parity Lk",
        "description": "Basic Python, AI Tools Handling, and Google Workspace Handling courses for school students and industry persons, priced in LKR.",
        "eyebrow": "Courses",
        "heading": "Practical digital courses <span class=\"shine\">in LKR.</span>",
        "intro": "Beginner-friendly learning paths for school students, university graduates, and industry persons who want useful day-to-day skills.",
        "actions": [
            ('button button-primary', 'https://docs.google.com/forms/d/17N6wnGqvJgEfEEybqApAn9Lc0SQNRYZYypg23pzFmXQ/viewform', 'Enroll interest'),
            ('button button-secondary', '/contact/', 'Ask about batches'),
        ],
        "body": COURSES_BODY + CTA.format(
            modifier=" section-light",
            title="Not sure which course fits?",
            copy="Tell us your level and what you want to do with the skill. We point you at the right starting course.",
        ),
    },
    {
        "path": "/careers/",
        "dir": "careers",
        "title": "Careers | Parity Lk",
        "description": "Careers at ParityLk: open roles across mobile, web, and cloud delivery, starting with internships and expanding to senior positions as the team grows.",
        "eyebrow": "Careers",
        "heading": "Build your career on <span class=\"shine\">real delivery work.</span>",
        "intro": "We hire across mobile, web, and cloud. Internships are open now, and senior roles will follow as the team grows — every position works on live client delivery.",
        "actions": [
            ('button button-primary', 'https://forms.gle/r8dBgu6D9do1oTmeA', 'Apply interest'),
            ('button button-secondary', '/services/', 'See what we build'),
        ],
        "body": CAREERS_BODY + CTA.format(
            modifier=" section-light",
            title="Do not see your role yet?",
            copy="Send a short note about your background and what you want to work on. We keep applications on file for roles opening later.",
        ),
    },
    {
        "path": "/contact/",
        "dir": "contact",
        "title": "Contact | Parity Lk",
        "description": "Contact ParityLk about websites, mobile apps, courses, cloud troubleshooting, deployment, content creation, or support.",
        "eyebrow": "Contact",
        "heading": "Tell us what you <span class=\"shine\">want to launch.</span>",
        "intro": "One short brief covers builds, course seats, cloud fixes, and support work. Response target: within one business day.",
        "actions": [
            ('button button-primary', 'mailto:info@paritylk.com', 'Email us directly'),
        ],
        "body": CONTACT_BODY,
    },
]


def action_markup(actions):
    rows = []
    for cls, href, label in actions:
        external = href.startswith("http")
        extra = ' target="_blank" rel="noopener"' if external else ""
        rows.append(f'              <a class="{cls}" href="{href}"{extra}>{label}</a>')
    return "\n".join(rows)


for page in PAGES:
    nav, cta_current = nav_markup(page["path"])
    visual, badge = VISUALS[page["path"]]
    html = SHELL.format(
        visual=visual.rstrip("\n"),
        badge=badge,
        title=page["title"],
        description=page["description"],
        path=page["path"],
        version=VERSION,
        nav=nav,
        cta_current=cta_current,
        eyebrow=page["eyebrow"],
        heading=page["heading"],
        intro=page["intro"],
        actions=action_markup(page["actions"]),
        body=page["body"].rstrip("\n"),
    )
    out_dir = os.path.join(ROOT, page["dir"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as handle:
        handle.write(html)
    print("wrote", os.path.join(page["dir"], "index.html"))
