# ParityLk Static Website

Static launch page for ParityLk, a provider for websites, mobile apps, student courses, cloud deployment, cloud troubleshooting, content creation, and support.

## Project

- Entry file: `index.html`
- Styles: `assets/css/styles.css`
- Script: `assets/js/main.js`
- Main visual: `assets/images/paritylk-workbench.png`
- Official logo assets: `assets/images/paritylk-navbar-logo.png`, `assets/images/paritylk-logo-official.png`, and `assets/images/paritylk-favicon.png`
- Fonts: DM Sans for body text and JetBrains Mono for technical labels
- Cloud platform logos: AWS, Azure, and Google Cloud SVGs are stored locally in `assets/images/cloud/`
- Course logos: Python, OpenAI, and Google Workspace SVGs are stored locally in `assets/images/courses/`
- Build step: none
- GitHub Pages custom domain file: `CNAME`

## Courses

- Basic Python: LKR 3,499 student price
- AI Tools Handling: LKR 8,999 student price
- Google Workspace Handling: LKR 4,999 student price
- Enrollment form: `https://docs.google.com/forms/d/17N6wnGqvJgEfEEybqApAn9Lc0SQNRYZYypg23pzFmXQ/viewform`

## Logo Sources

- AWS: Wikimedia Commons `Amazon Web Services Logo.svg`
- Azure: Wikimedia Commons `Microsoft Azure Logo.svg`
- Google Cloud: Wikimedia Commons `Google Cloud logo.svg`
- Python: `python.org/static/community_logos/python-logo-generic.svg`
- OpenAI: Wikimedia Commons `OpenAI Logo.svg`
- Google Workspace: Wikimedia Commons `Google Workspace Logo.svg`

These provider and course logos are trademarks of their respective owners. Use them only to identify supported platforms and course topics.

## Preview

Open `index.html` in a browser. No local server is required.

## Deploy to GitHub Pages

This site is ready for GitHub Pages from the repository root.

1. Create a GitHub repository, for example `ParityLk`.
2. Upload or push the full project contents to the repository root.
3. In GitHub, open the repository and go to Settings > Pages.
4. Under Build and deployment, set Source to `Deploy from a branch`.
5. Select the `main` branch and `/ (root)` folder, then save.
6. In Custom domain, use `paritylk.com`.
7. Enable `Enforce HTTPS` after GitHub finishes issuing the certificate.

The root `CNAME` file must contain only:

```text
paritylk.com
```

## Namecheap DNS

In Namecheap, open Domain List > Manage > Advanced DNS and add these Host Records:

| Type | Host | Value |
| --- | --- | --- |
| A Record | @ | 185.199.108.153 |
| A Record | @ | 185.199.109.153 |
| A Record | @ | 185.199.110.153 |
| A Record | @ | 185.199.111.153 |
| CNAME Record | www | your-github-username.github.io |

Replace `your-github-username` with the GitHub account or organization that owns the Pages site. Remove conflicting `A`, `CNAME`, URL Redirect, or parking records for `@` and `www`.

## Cloud Troubleshooting Checklist

- Confirm the domain points to the static host with the correct DNS records.
- Verify HTTPS/SSL is active after DNS propagation.
- Check redirects from `www` to the root domain, or the reverse if preferred.
- Confirm all static assets load with `200` responses.
- Clear CDN/browser cache after updating CSS, JavaScript, or images.
- Verify the fallback route if the site later becomes a single-page app.

## Before going live

- Contact mailbox: `info@paritylk.com`
- Replace the hero image with real portfolio imagery when available.
