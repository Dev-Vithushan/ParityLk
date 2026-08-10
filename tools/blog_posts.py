"""Blog content. Each post renders to /blog/<slug>/index.html."""

POSTS = [
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
