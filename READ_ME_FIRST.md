# A.K.M. Amanullah — Research Portfolio Website

**Status: COMPLETE WEBSITE FILES, NOT YET HOSTED.** This ZIP contains an actual 3-page responsive portfolio, original project photos, research descriptions, publication links, an academic CV and a PDF portfolio. It works as a static site and needs no paid service or application server.

**Important:** The website cannot appear in Google until you publish it to a public HTTPS URL. A URL cannot be truthfully inserted into your CV until the site address exists. The included CV therefore has a clearly marked website-URL slot. **Do not submit that draft CV with its placeholder**. The optional configuration script below replaces the placeholder with a live clickable link and prepares search-engine files.

## Publish for free with GitHub Pages (recommended)

1. Make or sign in to your own GitHub account: https://github.com/
2. Click **New repository**. If your GitHub username is `YOUR-USERNAME`, give the repository the exact name `YOUR-USERNAME.github.io`. Set visibility to **Public**.
3. Unzip this package. Upload **the contents of the `Amanullah_Research_Website` folder** into that repository's **root** (not a nested website folder); ensure `index.html`, `style.css`, `research.html`, `worm-gearbox.html`, `assets/`, and `docs/` are at the root. Commit.
4. In the repository open **Settings → Pages**. Choose **Deploy from a branch**, branch **main**, folder **/(root)**, and Save. GitHub provides the live homepage at `https://YOUR-USERNAME.github.io/`. Use the exact URL GitHub displays, and visit it to confirm that all images and buttons work.
5. To make the site easier to find on Google, first configure its real public address as described below, then commit the updated files. Put that same URL in your CV, ORCID profile, faculty profile if permitted, email signature, and professional pages.

See official documentation: https://docs.github.com/en/pages/quickstart

## Activate the real portfolio link in your CV + Google search metadata

**Option A — automatic (preferred):** Run this inside the website folder, replacing the example with your ACTUAL live URL:

```bash
pip install python-docx beautifulsoup4
python configure_site.py --url https://YOUR-USERNAME.github.io/
```

Requires Python 3. LibreOffice is optional and needed only for automatic PDF export. The script updates the DOCX with a clickable live link, copies `Amanullah_CV_With_Live_Portfolio_Link.docx` into the site root, and generates `sitemap.xml`, `robots.txt` sitemap pointer, canonical links, absolute social preview image addresses and structured-data URLs. If LibreOffice is installed, it also generates a revised CV PDF. Re-upload/commit the updated site files.

**Option B — no programming required:** Open `docs/Amanullah_Research_CV_Fall2027.docx` in Word, replace `[ADD PUBLIC URL AFTER PUBLISHING]` with your actual URL, select it, and press Ctrl+K to make it a hyperlink. Save As PDF. The site works even if the optional metadata script is not run, although the script improves SEO setup. For the site's `robots.txt`, you can manually add `Sitemap: https://your-actual-domain/sitemap.xml` if you create an XML sitemap.

## Get indexed by Google

1. Open **Google Search Console** at https://search.google.com/search-console/ and add your live URL as a **URL-prefix property**.
2. Verify ownership using a Search Console HTML verification file uploaded to the repo root (or another offered method).
3. Use **URL Inspection** for your homepage and click **Request indexing**.
4. If you ran `configure_site.py`, open **Sitemaps**, submit `sitemap.xml`, then monitor indexing and errors.
5. Search for **`"A.K.M. Amanullah" "Mechanical Engineering"`** after Google has crawled the site. Link to it from relevant, credible profiles to help people and crawlers find it.

**No guaranteed Google timing or ranking:** Google's own guidance says crawling and indexing may take days to weeks, and submitting a sitemap or indexing request does not guarantee inclusion.

Google's guidance: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl

## What is on this website?

- `index.html` — academic landing page, first-author paper, highlighted research, project directory, timeline and contact.
- `research.html` — detailed, evidence-qualified research case studies and ICMIME accepted manuscripts.
- `worm-gearbox.html` — illustrated third-year, second-semester 3D-printed worm gearbox project and gallery.
- `assets/` — optimized images taken from the supplied photographs and original infographic artwork.
- `docs/` — academic CV (Word and PDF) and extended portfolio PDF.
- `style.css`, `script.js` — responsive design, project filters, gallery enlargement and navigation.
- `configure_site.py` — updates website SEO files and activates the website link in the CV.
- `robots.txt`, `.nojekyll` — crawler/hosting configuration.

## Content integrity and photo permissions

The *International Journal of Hydrogen Energy* article is a published peer-reviewed work. The four ICMIME 2026 papers are described as **accepted with proceedings forthcoming**, consistent with the author's statement and the December 2026 event date. The cooling manuscript is in preparation; the FCDI conference manuscript is not described as formally accepted or published. Model predictions are labeled as such, and the worm gearbox is **not** assigned fabricated ratio, torque, performance or efficiency data.

The photo gallery includes an image with fellow students. **Check that your classmates are comfortable with their image appearing on a public website before publishing.** If not, delete that gallery item and its image file, or substitute a gear-only photo.

These website files were prepared from provided research documents, CV, manuscripts and original photographs. Review dates and statuses when new publications appear.
