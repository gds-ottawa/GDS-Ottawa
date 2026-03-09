# Pre-Migration Google & SEO Audit — GDS Ottawa Website

**Date:** February 2025  
**Purpose:** Fix or document issues that Google may flag before migrating to garagedoorsolutionsottawa.ca.

---

## ✅ Fixed in This Pass

### 1. **Broken “Leave a Review” link (would 404 / look like spam)**
- **Issue:** Many pages had `href="https://g.page/r/YOUR_GOOGLE_REVIEW_LINK/review"`, which is a placeholder and would 404 or point nowhere.
- **Fix:** Replaced with `https://www.google.com/search?q=GDS+Garage+Doors+Openers+Ottawa+review` so the link works and sends users to a search where they can find your Google listing.
- **Optional later:** If you have your real Google Business “Leave a review” URL (e.g. from Google Business Profile), replace that search URL with it for a direct review experience.

---

## ⚠️ Action Required Before / At Go-Live

### 2. **Contact form endpoint (Formspree placeholder)**
- **Issue:** Every contact form uses `action="https://formspree.io/f/your-form-id"`. Submissions will not reach you until this is updated.
- **Action:** Create a form at [Formspree](https://formspree.io), get your form ID (e.g. `xyzabc12`), then replace `your-form-id` in **all** HTML files that contain a contact form.  
- **Files to update (29):** All suburb pages, `contact-us.html`, `about.html`, `faq.html`, and the 5 service pages (`garage-door-installation.html`, `garage-door-spring-repair.html`, `garage-door-cable-repair.html`, `garage-door-opener.html`, `garage-door-maintenance.html`).  
- **Search for:** `formspree.io/f/your-form-id` and replace with `formspree.io/f/YOUR_REAL_FORM_ID`.

---

## ✅ Already in Good Shape (No Change Needed)

- **Structured data (Review snippets):** No `itemReviewed` inside nested Review objects and no incomplete Review microdata on review cards — previous fixes are in place.
- **Viewport:** All pages have a proper viewport meta tag.
- **Titles & meta descriptions:** Present and unique per page (e.g. suburb pages have location-specific titles and descriptions).
- **Contact / quote links:** “Get a Quote” and “Schedule appointment” point to your built `contact-us.html`, not the old site.
- **Mixed content:** No `http://` links; pages use HTTPS for external resources.
- **Form placeholders:** Input placeholders like “Your name”, “your@email.com” are normal UX text, not content placeholders — fine for Google.
- **Images:** No empty `alt=""` on images that need descriptions; decorative/icon usage is appropriate.

---

## 📋 Recommended Soon After Migration

1. **Canonical URLs**  
   - Some pages have `<link rel="canonical">`; ensure every important page has a canonical pointing to its final URL on `https://garagedoorsolutionsottawa.ca/...` (e.g. `https://garagedoorsolutionsottawa.ca/nepean` for `nepean.html`).

2. **Schema `url` and sameAs**  
   - In LocalBusiness (and any Organization) JSON-LD, set `"url"` (and `sameAs` if you use social links) to the live domain (e.g. `https://garagedoorsolutionsottawa.ca`) once the site is live.

3. **robots.txt**  
   - Add a `robots.txt` at the root (e.g. allow `/` and optionally reference your sitemap). This helps crawlers and can prevent accidental blocking.

4. **Sitemap**  
   - Add an `sitemap.xml` listing all important URLs (home, contact, services, suburbs, blog index, key blog posts). Submit it in Google Search Console after migration.

5. **Homepage “Service area” chips**  
   - The area chips on the homepage currently point to `https://garagedoorsolutionsottawa.ca/...`. After migration these will work. Optionally you can switch them to relative links (e.g. `nepean.html`, `carp.html`) so the same code works in any environment.

---

## Summary

| Item                               | Status / Action |
|------------------------------------|-----------------|
| YOUR_GOOGLE_REVIEW_LINK placeholder| ✅ Fixed site-wide |
| Formspree `your-form-id`           | ⚠️ Replace with real form ID before go-live |
| Review / LocalBusiness schema      | ✅ No known Google-flagging issues |
| Titles, descriptions, viewport    | ✅ OK |
| Form action (form submissions)     | ⚠️ Update Formspree ID in 29 files |

Once the Formspree form ID is set everywhere, the site is in good shape for migration from a “things Google might flag” perspective. After go-live, add or verify canonicals, sitemap, and robots.txt and resubmit in Search Console.
