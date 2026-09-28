# opentide.ai

Static coming-soon site for OpenTide and Tide. No build step: serve the folder as is (GitHub Pages, Netlify, Cloudflare Pages).

- `index.html`: the whole site
- `img/`: logos, Tide screenshots (full + detail crops), OG image
- `CNAME`: opentide.ai (for GitHub Pages)
- `src/`: source used to generate `index.html`, favicons and the OG image (`python3 src/build.py`)

## Mailing list
Set `SIGNUP_ENDPOINT` near the bottom of `index.html` to a Buttondown or Formspree form endpoint. Until then the form validates the email but tells visitors signups aren't open yet.
