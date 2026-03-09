/**
 * Build suburb pages from Nepean template.
 * Run: node build-suburb-pages.js
 * Reads suburb-data.json and nepean.html, outputs one HTML file per suburb.
 */

const fs = require('fs');
const path = require('path');

const DATA_PATH = path.join(__dirname, 'suburb-data.json');
const TEMPLATE_PATH = path.join(__dirname, 'nepean.html');
const OUT_DIR = __dirname;

function buildAreaServed(name, neighbourhoods) {
  const places = neighbourhoods.slice(0, 6).map(n => ({ '@type': 'Place', name: n }));
  return [{ '@type': 'City', name: name }, ...places];
}

function buildMapAreaList(neighbourhoods) {
  return neighbourhoods
    .map(n => `              <div class="map-area-item"><span>&#128205; ${n}</span><span class="map-response-badge">1hr</span></div>`)
    .join('\n');
}

function main() {
  const data = JSON.parse(fs.readFileSync(DATA_PATH, 'utf8'));
  let template = fs.readFileSync(TEMPLATE_PATH, 'utf8');

  for (const suburb of data.suburbs) {
    const { name, slug, metaDescription, mapQuery, neighbourhoods } = suburb;

    let html = template;

    // 1. Replace all "Nepean" with suburb name (case-sensitive, whole word where possible)
    html = html.split('Nepean').join(name);

    // 2. Replace all "nepean" with slug (for URLs, ids, etc.)
    html = html.split('nepean').join(slug);

    // 3. Meta description - replace the content attribute value
    const metaDescRegex = /<meta name="description" content="[^"]*">/;
    html = html.replace(metaDescRegex, `<meta name="description" content="${metaDescription.replace(/"/g, '&quot;')}">`);

    // 4. Schema areaServed - replace the array with suburb's name + neighbourhoods
    const areaServedArr = buildAreaServed(name, neighbourhoods);
    const areaServedStr = '[\n      ' + areaServedArr.map(p => JSON.stringify(p)).join(',\n      ') + '\n    ]';
    html = html.replace(/"areaServed": \[[\s\S]*?\],/, `"areaServed": ${areaServedStr},`);

    // 5. Map sidebar - replace neighbourhood list (after Name replace, heading is already "X Neighborhoods")
    const mapListStart = '<div class="map-areas-list">';
    const listStartIdx = html.indexOf(mapListStart);
    const listEndMarker = '\n            </div>';
    const listEndIdx = html.indexOf(listEndMarker, listStartIdx);
    if (listStartIdx !== -1 && listEndIdx !== -1) {
      const before = html.slice(0, listStartIdx + mapListStart.length);
      const after = html.slice(listEndIdx);
      const newList = '\n' + buildMapAreaList(neighbourhoods) + '\n            ';
      html = before + newList + after;
    }

    // 6. Map stat "X+ Neighborhoods" - replace number with neighbourhood count
    const count = neighbourhoods.length;
    const statNumRegex = /<span class="map-stat-number">\d+\+<\/span>\s*<span class="map-stat-label">[^<]+Neighborhoods<\/span>/;
    html = html.replace(statNumRegex, `<span class="map-stat-number">${count}+</span>\n          <span class="map-stat-label">${name} Neighborhoods</span>`);

    // 7. Map iframe - replace place in URL (template has Nepean%2C%20Ottawa%2C%20ON in src)
    const encodedQuery = encodeURIComponent(mapQuery).replace(/ /g, '%20');
    html = html.replace(/Nepean%2C%20Ottawa%2C%20ON/g, encodedQuery);

    // 8. FAQ "like X, Y, and Z" - use suburb's first 3 neighbourhoods for local SEO
    const likeNeighbourhoods = neighbourhoods.length >= 3
      ? `${neighbourhoods[0]}, ${neighbourhoods[1]}, and ${neighbourhoods[2]}`
      : neighbourhoods.join(', ');
    html = html.replace(/like Centrepointe, Craig Henry, and Bells Corners/g, `like ${likeNeighbourhoods}`);

    const outPath = path.join(OUT_DIR, `${slug}.html`);
    fs.writeFileSync(outPath, html, 'utf8');
    console.log('Written:', outPath);
  }

  console.log('Done. Generated', data.suburbs.length, 'suburb pages.');
}

main();
