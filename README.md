# opentide.ai

Static coming-soon site for OpenTide and Tide. No build step: serve the folder as is (GitHub Pages, Netlify, Cloudflare Pages).

- `index.html`: the whole site
- `img/`: logos, Tide screenshots (full + detail crops), OG image
- `CNAME`: opentide.ai (for GitHub Pages)
- `src/`: source used to generate `index.html`, favicons and the OG image (`python3 src/build.py`)

## Mailing list
The signup form posts to a Google Form (`SIGNUP_ENDPOINT` and `SIGNUP_FIELD` near the bottom of `index.html`). Emails appear under the form's Responses tab; link a Sheet there for a spreadsheet view.
