TECHAI VIBES — SEO-ENHANCED STATIC WEBSITE

INCLUDED
- Responsive dark-tech homepage with your logo.
- Six individual, crawlable article URLs under /blog/ (not just client-side cards).
- Unique title and description per page, Open Graph/Twitter metadata, canonical URLs generated for your chosen domain, JSON-LD structured data, RSS feed, robots.txt and sitemap generator.
- About, Contact and Privacy starter pages.
- Search/filter UI, accessible skip links and reduced-motion support.
- PDF cards are marked “coming soon” until real PDFs are supplied, preventing broken download links.

IMPORTANT BEFORE PUBLISHING
1. Choose and connect your real domain with HTTPS.
2. Run from this folder: python3 scripts/generate_seo.py https://your-real-domain.com
   This generates sitemap.xml, updates robots.txt and inserts canonical/absolute structured-data URLs. Do not publish the site while the YOUR-DOMAIN-HERE placeholder remains in HTML/JSON-LD/feed.xml.
3. Replace placeholder Instagram/Facebook profile URLs in index.html with your actual profiles.
4. Review the Privacy page and add a monitored contact method. It is a starter template, not legal advice.
5. Replace sample articles with your own original experience, screenshots, tests and sources over time. The included guides are starter content and should be reviewed/expanded before publication.
6. Add the actual PDF files and update the PDF cards to working download links.
7. Deploy the entire folder to a static host. Keep article folders and assets paths unchanged.
8. Verify the domain in Google Search Console, submit https://your-real-domain.com/sitemap.xml, inspect key URLs, and monitor indexing and search performance.
9. Run PageSpeed Insights, Rich Results Test and URL Inspection after deployment. Recheck mobile usability, links, performance and metadata.

SEO NOTES
- Technical SEO helps crawling and understanding but does not guarantee indexing or ranking.
- Sitemap submission is a hint, not a guarantee. Ranking depends heavily on helpful original content, search intent, reputation, competition and ongoing improvements.
- Do not add fake reviews, invented author credentials, misleading schema or keyword stuffing.
- The current project is static: no CMS/admin dashboard, analytics, newsletter backend or automatic publishing system.

FILES
index.html, article.css, blog/*/index.html, about.html, contact.html, privacy.html, feed.xml, robots.txt, scripts/generate_seo.py, assets/, pdfs/.


MOBILE FIX + CONTENT DASHBOARD UPDATE
- Logo copied to root as techai-vibes-logo.png to simplify upload from mobile GitHub.
- Homepage image references updated to root logo.
- Mobile overflow/overlapping layout CSS safeguards added.
- admin.html is a local browser content planner for blog ideas and PDF resource ideas.
- IMPORTANT: admin.html uses localStorage and is not password-protected, does not sync across devices, and does not publish changes to the live site. Do not treat it as a secure production admin dashboard.
- Live site URL: https://techaivibes.github.io/
- Upload every file and folder in this folder to the ROOT of the GitHub repository.
