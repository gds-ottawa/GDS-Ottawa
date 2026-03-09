# GDS Ottawa — Setup Before Go-Live

## 1. Contact form (Formspree)

All contact forms use a **single placeholder** so you only need to replace it once.

1. Go to [formspree.io](https://formspree.io) and create a form. Copy your form ID (e.g. `xyzabc12`).
2. In your editor, do a **Find and Replace** across the whole site:
   - **Find:** `REPLACE_WITH_YOUR_FORMSPREE_ID`
   - **Replace with:** your actual form ID (e.g. `xyzabc12`)
3. All 29 contact forms now use this same placeholder, so one find-and-replace updates the whole site.

**Result:** Form submissions will go to your Formspree inbox (or your connected email).

---

## 2. Optional: Google “Leave a review” link

The “Leave Us a Review on Google” button currently links to a Google search. For a direct review link:

1. Open [Google Business Profile](https://business.google.com), select your business.
2. Get your “Share review form” link (or the short link from the “Get more reviews” section).
3. Find and replace: `https://www.google.com/search?q=GDS+Garage+Doors+Openers+Ottawa+review` with your review URL.

---

## 3. After you migrate to your domain

- Confirm **canonical** URLs and **schema** `url` use `https://garagedoorsolutionsottawa.ca` (or your final domain).
- Upload **robots.txt** and **sitemap.xml** to the root of your site.
- In **Google Search Console**, add the property and submit the sitemap.
