# GDS Ottawa Website (Manual Code Site)

**GDS - Garage Doors & Openers Ottawa** — static HTML site built with manually added sections.

This folder is the **GDS manual website** project. It is separate from:
- **ottawagaragedoorrepair** — the other (Next.js) project; do not confuse the two.

## Contents
- `index.html` — Homepage (hero, services, FAQ, trust badges, social carousel, final CTA)
- `garage-door-installation.html` — Garage Door Installation service page
- `garage-door-spring-repair.html` — Garage Door Spring Repair service page
- `garage-door-cable-repair.html` — Garage Door Cable Repair service page
- `garage-door-opener.html` — Garage Door Opener service page
- `garage-door-maintenance.html` — Garage Door Maintenance service page
- `faq.html` — FAQ page (33 questions, How It Works, Contact Us)
- `about.html` — About Us page (story, timeline, testimonials, values, team, service areas, Contact Us)
- **23 suburb pages** — e.g. `kanata.html`, `barrhaven.html`, `orleans.html`, `carp.html`, `nepean.html`, `stittsville.html`, `gloucester.html`, `richmond.html`, `manotick.html`, `vanier.html`, `carleton-place.html`, `hunt-club.html`, `dunrobin.html`, `kemptville.html`, `metcalfe.html`, `greely.html`, `riverside-south.html`, `findlay-creek.html`, `alta-vista.html`, `westboro.html`, `rockcliffe-park.html`, `embrun.html`, `russell.html`. Content adapted from garagedoorsolutionsottawa.ca; each has local intro, trust bullets, neighbourhoods or “serving X and surrounding communities”, How It Works, and Contact Us.
- `css/style.css` — Main styles
- `js/main.js` — Scripts

## Open the site
Open `index.html` in your browser, or use:
`file:///C:/Users/smile/OneDrive/Desktop/gds-ottawa-website/index.html`

## Suburb pages (SEO, unique content)
- **Template:** `nepean.html` is the full template (all sections, schema, map, FAQ).
- **Data:** `suburb-data.json` — one entry per suburb (except Nepean): `name`, `slug`, `metaDescription`, `mapQuery`, `neighbourhoods`.
- **Build:** From the project folder run `node build-suburb-pages.js`. This reads `nepean.html` and `suburb-data.json`, then writes one HTML file per suburb (`kanata.html`, `barrhaven.html`, etc.) with:
  - Unique `<title>` and `<meta name="description">`
  - LocalBusiness + FAQ schema with suburb-specific `areaServed` and neighbourhoods
  - All body copy and headings using the suburb name and local neighbourhoods
  - Map sidebar and map stat with suburb neighbourhoods and count
  - Map iframe query set to the suburb’s `mapQuery`
- To add or edit a suburb: update `suburb-data.json` and re-run the script. Do not edit generated `*.html` files by hand if you plan to re-run the build.

## Project location
`C:\Users\smile\OneDrive\Desktop\gds-ottawa-website`
