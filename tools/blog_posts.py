"""Blog content. Each post renders to /blog/<slug>/index.html."""

POSTS = [
    {
        "slug": "introduction-to-the-cloud",
        "title": "Introduction to the cloud",
        "category": "Cloud",
        "date": "2026-08-10",
        "date_label": "10 August 2026",
        "read": "9 min read",
        "image": "assets/images/hero/hero-cloud.png",
        "image_alt": "Cloud deployment workspace showing server nodes, containers, and configuration panels.",
        "excerpt": (
            "What the cloud actually is, the three service models, what you pay for, "
            "and the handful of settings that decide whether your site stays up."
        ),
        "body": """
            <h2>Someone else's computer, rented by the minute</h2>
            <p>
              The cloud is a set of computers in data centres that you rent instead of buy. That
              is the whole idea. Everything else &mdash; the acronyms, the pricing calculators, the
              certification tracks &mdash; is detail layered on top of renting compute, storage, and
              network capacity from a company that runs it at scale.
            </p>
            <p>
              What makes it different from a server under a desk is not the hardware. It is that
              capacity arrives in minutes rather than weeks, you pay for what you use, and someone
              else handles the power, cooling, and failed disks.
            </p>

            <h2>The three service models</h2>
            <p>
              Nearly every cloud product fits one of three shapes, and the difference is simply how
              much of the stack you still manage:
            </p>
            <ul>
              <li>
                <strong>Infrastructure as a Service (IaaS)</strong> &mdash; you rent raw machines and
                disks. Maximum control, maximum responsibility: patching, scaling, and security
                are yours.
              </li>
              <li>
                <strong>Platform as a Service (PaaS)</strong> &mdash; you hand over code and the
                platform runs it. No servers to patch, less control over the environment.
              </li>
              <li>
                <strong>Software as a Service (SaaS)</strong> &mdash; you just use the finished
                product. Gmail and Google Workspace are SaaS; you manage accounts, nothing more.
              </li>
            </ul>
            <p>
              Most small businesses need far less IaaS than they expect. A static site on managed
              hosting with a CDN in front of it is cheaper, faster, and harder to break than a
              virtual machine you have to maintain.
            </p>

            <figure class="article-figure">
              <img src="assets/images/blog/cloud-service-models.svg" alt="Chart comparing IaaS, PaaS and SaaS by which layers you manage." loading="lazy" width="1200" height="620">
              <figcaption>The less of the stack you manage, the fewer things there are to keep patched.</figcaption>
            </figure>

            <h2>The three big providers</h2>
            <p>
              AWS, Microsoft Azure, and Google Cloud dominate, and for most projects the choice
              matters less than people think. The deciding factors are usually practical:
            </p>
            <ul>
              <li><strong>AWS</strong> &mdash; the widest service catalogue and the most documentation and community answers.</li>
              <li><strong>Azure</strong> &mdash; the natural fit if your organisation already runs Microsoft 365 and Active Directory.</li>
              <li><strong>Google Cloud</strong> &mdash; strong on data, analytics, and container tooling.</li>
            </ul>
            <div class="cloud-providers article-logos" aria-label="Cloud platforms we work with">
              <span class="cloud-provider">
                <img src="assets/images/cloud/aws.svg" width="512" height="307" alt="Amazon Web Services logo" loading="lazy">
              </span>
              <span class="cloud-provider">
                <img src="assets/images/cloud/azure.svg" width="187" height="54" alt="Microsoft Azure logo" loading="lazy">
              </span>
              <span class="cloud-provider">
                <img src="assets/images/cloud/gcp.svg" width="512" height="79" alt="Google Cloud logo" loading="lazy">
              </span>
            </div>

            <p>
              Pick the one your team can actually operate. A well-run setup on any of the three
              beats a neglected setup on the one with the best marketing.
            </p>

            <h2>The pieces you will actually touch</h2>
            <p>
              A typical website or app touches a small, predictable set of services:
            </p>
            <ul>
              <li><strong>Compute</strong> &mdash; where your code runs: a virtual machine, a container, or a serverless function.</li>
              <li><strong>Storage</strong> &mdash; object storage for images, uploads, and backups, billed by the gigabyte.</li>
              <li><strong>Database</strong> &mdash; a managed engine so backups and failover are not your problem.</li>
              <li><strong>DNS</strong> &mdash; the records that point your domain at all of the above.</li>
              <li><strong>CDN</strong> &mdash; caches copies of your site near your visitors, which is the single biggest speed win for an audience spread across regions.</li>
              <li><strong>Certificates</strong> &mdash; the SSL that puts the padlock in the address bar.</li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/blog/cloud-launch-checks.svg" alt="Checklist of DNS, SSL, redirects, environment variables and backups." loading="lazy" width="1200" height="560">
              <figcaption>Five configuration checks that prevent most small-site outages.</figcaption>
            </figure>

            <h2>What you are really paying for</h2>
            <p>
              Cloud billing catches people out because it is metered rather than fixed. The
              recurring surprises are almost always the same three:
            </p>
            <ul>
              <li><strong>Egress</strong> &mdash; moving data out of the provider costs money; moving it in usually does not.</li>
              <li><strong>Idle resources</strong> &mdash; a machine you provisioned for a test in March is still billing in August.</li>
              <li><strong>Over-provisioning</strong> &mdash; paying for capacity sized to a traffic spike that has not happened yet.</li>
            </ul>
            <p>
              Set a billing alert on day one. It takes two minutes and it is the difference between
              noticing a mistake at ten dollars and noticing it at three hundred.
            </p>

            <figure class="article-figure">
              <img src="assets/images/blog/cloud-costs.svg" alt="Chart of egress, idle resources and over-provisioning as sources of cloud cost." loading="lazy" width="1200" height="520">
              <figcaption>Alerts on billing and uptime are the two to configure before launch day.</figcaption>
            </figure>

            <h2>The settings that decide whether you stay up</h2>
            <p>
              In our experience most outages on small sites are not code failures. They are
              configuration:
            </p>
            <ul>
              <li>DNS records pointing at an old server after a migration.</li>
              <li>An SSL certificate that expired because nothing was set to renew it.</li>
              <li>A redirect loop between the www and non-www versions of a domain.</li>
              <li>Environment variables that exist locally and were never set in production.</li>
              <li>Storage permissions left open, or locked so tight the app cannot read its own files.</li>
            </ul>
            <p>
              None of these are difficult. They are simply easy to forget, which is why a launch
              checklist matters more than deep provider knowledge.
            </p>

            <h2>A reasonable starting point</h2>
            <ul>
              <li><strong>Static or brochure site:</strong> managed static hosting plus a CDN and automatic SSL. Cheap, fast, very little to break.</li>
              <li><strong>Site with a backend:</strong> a managed platform for the app and a managed database. Skip raw virtual machines until you have a reason.</li>
              <li><strong>Mobile app backend:</strong> managed APIs and storage, with alerting from the first release rather than the first outage.</li>
            </ul>
            <p>
              Whichever route you take, get three things in place before launch: automated
              backups, a billing alert, and an uptime check that tells you about a problem before
              a customer does.
            </p>

            <h2>If the cloud part is the blocker</h2>
            <p>
              Configuration is the piece most teams would rather hand over, and it is a large part
              of what we do &mdash; hosting, DNS, SSL, redirects, storage, access, and environments on
              AWS, Azure, or Google Cloud, then maintenance so it keeps working after launch. If
              something is live and broken right now, send the error and the environment details.
            </p>
        """,
    },
    {
        "slug": "what-is-paritylk",
        "title": "What is ParityLk, and what do we actually do?",
        "category": "Company",
        "date": "2026-08-04",
        "date_label": "4 August 2026",
        "read": "6 min read",
        "image": "assets/images/hero/hero-websites.png",
        "image_alt": "Dark workspace showing website layouts, delivery boards, and development tools.",
        "excerpt": (
            "A plain explanation of who we are, the work we take on, and how a project "
            "moves from a first message to something live and supported."
        ),
        "body": """
            <h2>Start with the name</h2>
            <p>
              Parity means being on equal footing. That is the idea behind the company: a small
              business in Sri Lanka should be able to launch a website, a mobile app, or a cloud
              setup that works as well as anything a larger company would ship. Not a cheaper
              imitation of it &mdash; the same standard of work, scoped to what you actually need.
            </p>
            <p>
              ParityLk is a digital delivery partner. In practice that means we build the thing,
              put it live, and stay available after launch, rather than handing over files and
              disappearing.
            </p>

            <h2>What we build</h2>
            <p>
              The work falls into six areas, and most projects touch two or three of them:
            </p>
            <ul>
              <li>
                <strong>Website development</strong> &mdash; responsive business sites, landing
                pages, service pages, and CMS-ready structures built for your own domain.
              </li>
              <li>
                <strong>Mobile app builds</strong> &mdash; app screens, prototypes, and customer
                portals for workflows that genuinely belong on a phone.
              </li>
              <li>
                <strong>Content creation</strong> &mdash; posts, service copy, and visuals, with a
                publishing plan so your channels stay active instead of going quiet after week two.
              </li>
              <li>
                <strong>Deployment setup</strong> &mdash; hosting, domains, environments, SSL, and
                the launch checks that catch problems before your customers do.
              </li>
              <li>
                <strong>Software support</strong> &mdash; updates, bug fixes, issue checks, and
                user support once real people are using the thing.
              </li>
              <li>
                <strong>Monitoring</strong> &mdash; uptime checks, issue tracking, and deployment
                verification so a broken release gets noticed by us, not by your customers.
              </li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/blog/service-areas.svg" alt="Six service areas grouped into build, publish and keep running." loading="lazy" width="1200" height="520">
              <figcaption>Six areas, grouped by the phase of delivery they belong to.</figcaption>
            </figure>

            <h2>Cloud work is its own thing</h2>
            <p>
              A surprising share of the problems we get asked about are not design or code
              problems at all. They are DNS records pointing at the wrong place, an SSL
              certificate that quietly expired, a redirect loop, or a deployment that worked
              locally and nowhere else.
            </p>
            <p>
              We configure and maintain environments on AWS, Microsoft Azure, and Google Cloud:
              hosting, DNS, SSL, redirects, storage, access, and the environment settings that
              hold it all together. If something is already live and broken, that is a fine
              first message to send us.
            </p>

            <figure class="article-figure">
              <img src="assets/images/blog/delivery-flow.svg" alt="Project flow from brief through scope, build, deploy and support." loading="lazy" width="1200" height="420">
              <figcaption>Every project runs this way, whatever it is we are building.</figcaption>
            </figure>

            <h2>Courses, because the skills gap is real</h2>
            <p>
              Alongside client work we run practical courses priced in LKR for school students,
              university graduates, and working professionals &mdash; Python fundamentals, using AI
              tools responsibly at work, and getting genuinely confident with Google Workspace.
              They exist because we kept meeting people who needed the skill more than they
              needed us to do the task for them.
            </p>

            <h2>How a project actually runs</h2>
            <p>
              There is no elaborate process here, and that is deliberate:
            </p>
            <ul>
              <li><strong>You send a brief.</strong> A few sentences is enough to start.</li>
              <li><strong>We reply with scope and timeline.</strong> Target is one business day.</li>
              <li><strong>We build in visible stages</strong>, so you see progress rather than a silent gap.</li>
              <li><strong>We deploy and run launch checks</strong> on the real domain and environment.</li>
              <li><strong>We stay on for support</strong> &mdash; monitoring, fixes, and follow-up releases.</li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/hero/hero-support.png" alt="Software monitoring workspace with dashboards, alerts, and support panels." loading="lazy" width="1672" height="941">
              <figcaption>After launch the work shifts to uptime checks, issue tracking, and follow-up releases.</figcaption>
            </figure>

            <h2>Where we are today</h2>
            <p>
              We are deliberately small: three or more active customers at any time, five websites
              delivered, and two mobile apps built. We would rather say that plainly than inflate
              it. It also means when you work with us you are dealing with the people doing the
              work, not an account manager relaying messages.
            </p>

            <h2>Getting started</h2>
            <p>
              Tell us what you want to launch, learn, or fix. Websites, mobile apps, a course
              seat, a cloud problem, or ongoing support &mdash; the same short brief covers all of
              it, and we aim to reply within one business day.
            </p>
        """,
    },
    {
        "slug": "introduction-to-digital-marketing",
        "title": "Introduction to digital marketing",
        "category": "Marketing",
        "date": "2026-07-28",
        "date_label": "28 July 2026",
        "read": "8 min read",
        "image": "assets/images/hero/hero-content.png",
        "image_alt": "Content planning workspace with editing timeline, publishing boards, and social analytics.",
        "excerpt": (
            "The channels, the funnel, and the handful of numbers worth tracking &mdash; a "
            "beginner's map for anyone about to spend their first marketing budget."
        ),
        "body": """
            <h2>What digital marketing actually means</h2>
            <p>
              Digital marketing is every way you reach customers through a screen: search results,
              social feeds, email, messaging apps, video, and your own website. That is it. The
              jargon around it is mostly people naming small pieces of that idea and selling them
              separately.
            </p>
            <p>
              The useful question is not "should we do digital marketing" but "which two channels
              deserve our attention this quarter, and how will we know if they worked".
            </p>

            <h2>The main channels</h2>
            <ul>
              <li>
                <strong>Search (SEO)</strong> &mdash; being found when someone types a problem you
                solve. Slow to build, cheap to keep, and the traffic is people already looking.
              </li>
              <li>
                <strong>Paid ads</strong> &mdash; buying attention on search or social. Fast, measurable,
                and it stops the moment you stop paying.
              </li>
              <li>
                <strong>Social media</strong> &mdash; regular presence where your customers already
                spend time. Best for trust and recall, worst for immediate sales.
              </li>
              <li>
                <strong>Content</strong> &mdash; articles, guides, and videos that answer real
                questions. Feeds search and social at the same time.
              </li>
              <li>
                <strong>Email and messaging</strong> &mdash; the only audience you own outright.
                Nothing else has that property; a platform can change its rules tomorrow.
              </li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/blog/marketing-funnel.svg" alt="Funnel diagram from awareness to retention with the metric for each stage." loading="lazy" width="1200" height="600">
              <figcaption>Match the message to the stage, or the budget goes to the wrong people.</figcaption>
            </figure>

            <h2>The funnel, without the mystique</h2>
            <p>
              Every customer moves through four rough stages, and most marketing failures are
              really a mismatch between the stage and the message:
            </p>
            <ul>
              <li><strong>Awareness</strong> &mdash; they learn you exist. Broad, cheap, low commitment.</li>
              <li><strong>Consideration</strong> &mdash; they compare you to alternatives. This is where detail wins.</li>
              <li><strong>Conversion</strong> &mdash; they buy, book, or enquire. Remove every unnecessary step here.</li>
              <li><strong>Retention</strong> &mdash; they come back and tell others. Cheapest growth you will ever get.</li>
            </ul>
            <p>
              Asking for a sale during awareness is why so much advertising feels pushy. Writing
              another awareness post for someone already comparing prices is why so much content
              feels useless.
            </p>

            <h2>The numbers worth tracking</h2>
            <p>
              Ignore most dashboards. Five numbers tell you nearly everything:
            </p>
            <ul>
              <li><strong>Traffic</strong> &mdash; how many people arrived, and from where.</li>
              <li><strong>Conversion rate</strong> &mdash; what share of them did the thing you wanted.</li>
              <li><strong>Cost per acquisition</strong> &mdash; what one new customer cost you.</li>
              <li><strong>Customer lifetime value</strong> &mdash; what that customer is worth over time.</li>
              <li><strong>Retention</strong> &mdash; how many come back without being paid for again.</li>
            </ul>
            <p>
              If cost per acquisition is below lifetime value, you have a business. If it is above,
              more spending makes the problem bigger, not smaller.
            </p>

            <figure class="article-figure">
              <img src="assets/images/blog/marketing-channels.svg" alt="Five channels feeding traffic into a website that converts it to enquiries." loading="lazy" width="1200" height="520">
              <figcaption>Every channel eventually points at your site, which makes it the first thing to fix.</figcaption>
            </figure>

            <h2>Your website is the hinge</h2>
            <p>
              Every channel eventually sends someone to your site, which makes it the one asset
              worth fixing first. A campaign pointing at a slow, confusing page is money spent
              filling a leaking bucket.
            </p>
            <p>
              Before spending on ads, check the basics: does the page load quickly on a phone on
              mobile data, is it obvious what you do within five seconds, and is the next step a
              single clear action?
            </p>

            <h2>A sensible first 90 days</h2>
            <ul>
              <li><strong>Weeks 1&ndash;2:</strong> fix the website basics &mdash; speed, mobile layout, clear contact path.</li>
              <li><strong>Weeks 3&ndash;4:</strong> set up analytics and decide what counts as a conversion.</li>
              <li><strong>Weeks 5&ndash;8:</strong> pick two channels. Publish consistently on one, test a small paid budget on the other.</li>
              <li><strong>Weeks 9&ndash;12:</strong> keep what produced enquiries, drop what did not, and start collecting emails.</li>
            </ul>

            <h2>Mistakes that cost the most</h2>
            <ul>
              <li>Being on six platforms badly instead of two properly.</li>
              <li>Spending on ads before the site converts.</li>
              <li>Measuring likes instead of enquiries.</li>
              <li>Stopping at week three, right before compounding starts.</li>
              <li>Renting an audience on a platform and never building an email list.</li>
            </ul>
            <p>
              Digital marketing rewards consistency far more than cleverness. Two channels, done
              properly for a year, will beat a brilliant campaign that runs for a month.
            </p>
        """,
    },
    {
        "slug": "website-or-mobile-app-first",
        "title": "Website or mobile app: which should you build first?",
        "category": "Guides",
        "date": "2026-07-21",
        "date_label": "21 July 2026",
        "read": "7 min read",
        "image": "assets/images/hero/hero-mobile-apps.png",
        "image_alt": "Mobile app development workspace showing phone interfaces and application code.",
        "excerpt": (
            "Apps feel like the serious choice, but they are usually the second one. How to "
            "tell which your business actually needs right now."
        ),
        "body": """
            <h2>The question behind the question</h2>
            <p>
              When someone asks whether they need an app, they usually mean something else: they
              want to look established, or they have seen a competitor launch one. Those are real
              motivations, but they are not requirements, and building on them is expensive.
            </p>
            <p>
              The honest test is simpler. A website is for people who do not know you yet. An app
              is for people who already do and will return often enough to justify installing
              something.
            </p>

            <h2>What a website is good at</h2>
            <ul>
              <li><strong>Being found.</strong> Search engines index websites. Nobody discovers you by browsing an app store for your category.</li>
              <li><strong>Zero friction.</strong> A link opens. An app needs a download, an account, and permission prompts.</li>
              <li><strong>One build, every device.</strong> Responsive pages work on phones, tablets, and desktops without separate work.</li>
              <li><strong>Cheap to change.</strong> Update the page and everyone sees it. No review queue, no waiting for users to update.</li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/blog/web-vs-app.svg" alt="Side by side comparison of what a website and a mobile app are each good at." loading="lazy" width="1200" height="560">
              <figcaption>Each column is a genuine strength; the question is which one you need now.</figcaption>
            </figure>

            <h2>What an app is genuinely better at</h2>
            <ul>
              <li><strong>Repeat use.</strong> If someone opens it several times a week, an icon on the home screen earns its place.</li>
              <li><strong>Device features.</strong> Camera, GPS, offline storage, and background sync are far stronger natively.</li>
              <li><strong>Notifications.</strong> The ability to reach someone directly &mdash; powerful, and easy to abuse.</li>
              <li><strong>Working offline.</strong> Field staff and delivery teams cannot depend on signal.</li>
            </ul>

            <h2>Cost is not the only difference</h2>
            <p>
              An app costs more to build, but the ongoing commitment is the part people
              underestimate. You are signing up for two platforms, store review processes, OS
              updates that break things annually, and users who never update. A website has none
              of that overhead.
            </p>
            <p>
              Ask yourself whether you want to maintain that for three years. If the answer is
              uncertain, the answer is a website.
            </p>

            <h2>A decision you can make in five minutes</h2>
            <p>Build the website first if:</p>
            <ul>
              <li>Most of your audience has not heard of you yet.</li>
              <li>People interact with you occasionally &mdash; a booking, a quote, a purchase now and then.</li>
              <li>You need to be found through search.</li>
              <li>Your budget covers one thing properly rather than two things partially.</li>
            </ul>
            <p>Build the app when:</p>
            <ul>
              <li>You have existing customers asking for it, not competitors having one.</li>
              <li>Your core workflow needs the camera, location, offline access, or notifications.</li>
              <li>Someone will use it weekly or more.</li>
              <li>You can commit to maintaining it beyond launch.</li>
            </ul>

            <figure class="article-figure">
              <img src="assets/images/blog/app-sequence.svg" alt="Sequence from shipping a website, to watching usage, to building a focused app." loading="lazy" width="1200" height="440">
              <figcaption>Site first, then evidence, then an app built around the habit it revealed.</figcaption>
            </figure>

            <h2>The sequence that usually works</h2>
            <p>
              Start with a responsive website that handles the whole customer journey on a phone.
              Watch what people actually repeat &mdash; the page they return to, the action they take
              again and again. That behaviour tells you what the app should be, and it is almost
              never the whole website in a smaller box.
            </p>
            <p>
              When the app comes, it is then a focused tool built around a proven habit rather
              than a guess. That is a much better second project than it would ever have been as
              a first one.
            </p>

            <h2>If you are still unsure</h2>
            <p>
              Describe how often a typical customer would use the thing and what they would do
              each time. That single answer usually settles it &mdash; and if it does not, send it
              over and we will tell you honestly which one we would build.
            </p>
        """,
    },
]
