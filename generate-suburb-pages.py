# -*- coding: utf-8 -*-
"""Generate suburb pages from original garagedoorsolutionsottawa.ca content."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

# Suburb slug (filename) -> (Display name, neighbourhoods list or None for generic)
SUBURBS = [
    ("carp", "Carp", [
        "Carp village & surrounding farms", "Huntley & Corkery", "Fitzroy Harbour & Galetta",
        "Kinburn & Woodlawn", "Constance & Buckham's Bay", "Dunrobin, Stittsville fringes",
        "Rural routes throughout West Carleton"
    ]),
    ("nepean", "Nepean", [
        "Barrhaven & Chapman Mills", "Centrepointe & Merivale Gardens", "Fisher Glen & Longfields",
        "Craig Henry & Fallowfield", "Stonebridge & Half Moon Bay",
        "Beaverbrook, McKellar Park, McEwen, Davidson's Corners, and more"
    ]),
    ("richmond", "Richmond", None),
    ("manotick", "Manotick", None),
    ("orleans", "Orleans", [
        "Fallingbrook", "Queenswood Heights", "All Orleans neighbourhoods"
    ]),
    ("vanier", "Vanier", None),
    ("carleton-place", "Carleton Place", None),
    ("hunt-club", "Hunt Club", None),
    ("dunrobin", "Dunrobin", None),
    ("kemptville", "Kemptville", None),
    ("metcalfe", "Metcalfe", None),
    ("greely", "Greely", None),
    ("stittsville", "Stittsville", [
        "Amberwood Village & Amberway", "Blackstone & Crossing Bridge", "Jackson Trails & Forest Creek",
        "Fairwinds & Deer Run", "Potter's Key & Timbermere",
        "Bryanston Gate, Poole Creek Village, Rathwell Landing, and more"
    ]),
    ("barrhaven", "Barrhaven", [
        "Chapman Mills", "Half Moon Bay", "All Barrhaven neighbourhoods"
    ]),
    ("gloucester", "Gloucester", [
        "Blackburn", "Hamlet", "Cyrville", "Beacon Hill", "All Gloucester areas"
    ]),
    ("riverside-south", "Riverside South", None),
    ("findlay-creek", "Findlay Creek", None),
    ("alta-vista", "Alta Vista", None),
    ("westboro", "Westboro", None),
    ("rockcliffe-park", "Rockcliffe Park", None),
    ("embrun", "Embrun", None),
    ("russell", "Russell", None),
]

HEADER_NAV = """        <a href="index.html">Home</a>
        <div class="nav-dropdown">
          <a href="index.html#services" class="nav-dropdown-trigger">Services</a>
          <div class="nav-dropdown-menu">
            <a href="garage-door-installation.html">Garage Door Installation</a>
            <a href="garage-door-spring-repair.html">Garage Door Spring Repair</a>
            <a href="garage-door-cable-repair.html">Garage Door Cable Repair</a>
            <a href="garage-door-opener.html">Garage Door Opener</a>
            <a href="garage-door-maintenance.html">Garage Door Maintenance</a>
          </div>
        </div>
        <a href="faq.html">FAQ</a>
        <div class="nav-dropdown nav-dropdown-service-area">
          <a href="index.html#service-areas" class="nav-dropdown-trigger">Service Area <span aria-hidden="true">&#9660;</span></a>
          <div class="nav-dropdown-menu nav-dropdown-menu--scroll">
            <a href="carp.html">Carp</a>
            <a href="nepean.html">Nepean</a>
            <a href="richmond.html">Richmond</a>
            <a href="manotick.html">Manotick</a>
            <a href="orleans.html">Orleans</a>
            <a href="vanier.html">Vanier</a>
            <a href="carleton-place.html">Carleton Place</a>
            <a href="hunt-club.html">Hunt Club</a>
            <a href="dunrobin.html">Dunrobin</a>
            <a href="kemptville.html">Kemptville</a>
            <a href="metcalfe.html">Metcalfe</a>
            <a href="greely.html">Greely</a>
            <a href="stittsville.html">Stittsville</a>
            <a href="kanata.html">Kanata</a>
            <a href="barrhaven.html">Barrhaven</a>
            <a href="gloucester.html">Gloucester</a>
            <a href="riverside-south.html">Riverside South</a>
            <a href="findlay-creek.html">Findlay Creek</a>
            <a href="alta-vista.html">Alta Vista</a>
            <a href="westboro.html">Westboro</a>
            <a href="rockcliffe-park.html">Rockcliffe Park</a>
            <a href="embrun.html">Embrun</a>
            <a href="russell.html">Russell</a>
          </div>
        </div>
        <a href="about.html">About Us</a>
        <a href="index.html#gallery">Gallery</a>
        <a href="https://garagedoorsolutionsottawa.ca/blog" target="_blank" rel="noopener">Blog</a>
        <a href="index.html#contact">Contact Us</a>"""

def neighbourhoods_html(hoods):
    if hoods:
        return "\n      ".join(['<ul class="neighbourhoods">'] + ['<li>' + h + '</li>' for h in hoods] + ['</ul>'])
    return '<p>We serve <strong>' + name + '</strong> and all surrounding communities.</p>'

# Read kanata as template (skip kanata in loop)
with open(os.path.join(BASE, "kanata.html"), "r", encoding="utf-8") as f:
    template = f.read()

for slug, name, hoods in SUBURBS:
    if slug == "kanata":
        continue
    out = template
    out = out.replace("Garage Door Repair Kanata | Same-Day Service | GDS Ottawa", "Garage Door Repair " + name + " | Same-Day Service | GDS Ottawa")
    out = out.replace("Garage door repair & installation in Kanata, Ontario. Same-day service, 343-777-8893. Trusted since 2020. Kanata Lakes, Bridlewood, Beaverbrook & all Kanata neighbourhoods.", "Garage door repair & installation in " + name + ", Ontario. Same-day service, 343-777-8893. Trusted since 2020. Serving " + name + " and surrounding areas.")
    out = out.replace("Garage Door Repair Kanata | Same-Day Service | 343-777-8893", "Garage Door Repair " + name + " | Same-Day Service | 343-777-8893")
    out = out.replace("Garage Door Repair &amp; Installation in Kanata, Ontario — Same Day Services", "Garage Door Repair &amp; Installation in " + name + ", Ontario — Same Day Services")
    out = out.replace("in Kanata?", "in " + name + "?")
    out = out.replace("for Kanata homeowners", "for " + name + " homeowners")
    out = out.replace("right here in Kanata, Stittsville, and across", "in " + name + " and across")
    out = out.replace("Why Kanata Residents Choose GDS?", "Why " + name + " Residents Choose GDS?")
    out = out.replace("5+ Years Serving Kanata &amp; West Ottawa", "5+ Years Serving " + name + " &amp; Ottawa")
    out = out.replace("We proudly serve Kanata and the surrounding communities:", "We proudly serve " + name + " and the surrounding communities:")
    # Replace neighbourhoods block
    nh_start = out.find("<ul class=\"neighbourhoods\">")
    nh_end = out.find("</ul>", nh_start) + 5
    if hoods:
        new_block = "\n      ".join(['<ul class="neighbourhoods">'] + ['<li>' + h + '</li>' for h in hoods] + ['</ul>'])
        out = out[:nh_start] + new_block + out[nh_end:]
    else:
        out = out.replace("We proudly serve " + name + " and the surrounding communities:", "We proudly serve " + name + ".")
        out = out[:nh_start] + "<p>We serve <strong>" + name + "</strong> and all surrounding communities.</p>" + out[nh_end:]
    out = out.replace("in Kanata. Fast", "in " + name + ". Fast")
    out = out.replace("repair near me Kanata.", "repair near me " + name + ".")
    out = out.replace("repair in Kanata —", "repair in " + name + " —")
    out = out.replace("kanata.html", slug + ".html")
    with open(os.path.join(BASE, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("Wrote", slug + ".html")

print("Done. Kanata was skipped (already exists).")
