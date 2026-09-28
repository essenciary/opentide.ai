import re, cairosvg, io
from PIL import Image
body=open('src/body.html').read()
body=re.sub(r'^<title>.*?</title>\n','',body)
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>OpenTide &amp; Tide · The web framework and IDE for AI agents</title>
<meta name="description" content="OpenTide is the web framework for AI agents: your app runs live, agents change it through gated MCP tools, and every change is verified before it commits. Tide is the IDE reinvented for AI, built on top of it. Coming soon." />
<meta name="keywords" content="OpenTide, Tide, AI agents, web framework, AI IDE, MCP, Model Context Protocol, TypeScript, Deno, agentic coding, verified code changes" />
<meta name="author" content="Adrian Salceanu" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="https://opentide.ai/" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="OpenTide" />
<meta property="og:locale" content="en_GB" />
<meta property="og:url" content="https://opentide.ai/" />
<meta property="og:title" content="OpenTide · The web framework for AI agents" />
<meta property="og:description" content="Build apps with AI agents, one verified change at a time. OpenTide is the web framework for AI agents; Tide is the IDE reinvented for AI. Coming soon." />
<meta property="og:image" content="https://opentide.ai/img/og.png" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="OpenTide: Build apps with AI agents, one verified change at a time." />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="OpenTide · The web framework for AI agents" />
<meta name="twitter:description" content="Build apps with AI agents, one verified change at a time. OpenTide is the web framework for AI agents; Tide is the IDE reinvented for AI. Coming soon." />
<meta name="twitter:image" content="https://opentide.ai/img/og.png" />
<meta name="twitter:image:alt" content="OpenTide: Build apps with AI agents, one verified change at a time." />
<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="sitemap" type="application/xml" href="/sitemap.xml" />
<meta name="theme-color" content="#0A1638" />
<meta name="color-scheme" content="light dark" />
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://opentide.ai/#org",
      "name": "OpenTide",
      "url": "https://opentide.ai/",
      "logo": "https://opentide.ai/img/opentide-logo-512.png",
      "founder": { "@type": "Person", "name": "Adrian Salceanu", "url": "https://essenciary.com/" }
    },
    {
      "@type": "WebSite",
      "@id": "https://opentide.ai/#website",
      "url": "https://opentide.ai/",
      "name": "OpenTide",
      "description": "OpenTide is the web framework for AI agents: your app runs live, agents change it through gated MCP tools, and every change is verified before it commits. Tide is the IDE reinvented for AI, built on top of it. Coming soon.",
      "publisher": { "@id": "https://opentide.ai/#org" },
      "inLanguage": "en"
    },
    {
      "@type": "SoftwareApplication",
      "name": "OpenTide",
      "url": "https://opentide.ai/#opentide",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "macOS, Linux, Windows",
      "description": "The web framework for AI agents. Agents change a live, running app through gated MCP tools; every change is a typed mutation, verified before it commits and kept in an append-only log.",
      "programmingLanguage": "TypeScript",
      "publisher": { "@id": "https://opentide.ai/#org" }
    },
    {
      "@type": "SoftwareApplication",
      "name": "Tide",
      "url": "https://opentide.ai/#tide",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "macOS, Linux, Windows",
      "description": "The IDE reinvented for AI. Plan with acceptance criteria, build against the live app, and see every change verified before it counts as done.",
      "screenshot": "https://opentide.ai/img/tide/tide.webp",
      "publisher": { "@id": "https://opentide.ai/#org" }
    }
  ]
}
</script>
'''
open('index.html','w').write(head+body.replace('<link rel="preconnect" href="https://fonts.googleapis.com" />','<link rel="preconnect" href="https://fonts.googleapis.com" />',1).replace('<style>','<style>\n:root{color-scheme:light}',1).split('\n<header',1)[0]+'\n</head>\n<body>\n<header'+body.split('\n<header',1)[1]+'\n</body>\n</html>\n')
mark=open('img/opentide-mark.svg').read()
open('favicon.svg','w').write(mark)
for sz,name in [(32,'favicon-32.png'),(180,'apple-touch-icon.png')]:
    cairosvg.svg2png(bytestring=mark.encode(),write_to=name,output_width=sz,output_height=sz)
p=[cairosvg.svg2png(bytestring=mark.encode(),output_width=s,output_height=s) for s in (16,32,48)]
Image.open(io.BytesIO(p[2])).save('favicon.ico',sizes=[(16,16),(32,32),(48,48)])
inner=re.sub(r'<\?xml[^>]*>|<svg[^>]*>|</svg>','',mark).replace('ot-c','og-c')
og=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#0A1638"/>
<circle cx="1010" cy="470" r="150" fill="none" stroke="#F2A33A" stroke-width="34"/>
<path d="M0 470 C 180 490, 330 480, 520 452 C 700 426, 880 416, 1200 440 L1200 630 L0 630Z" fill="#86CBEA"/>
<path d="M0 520 C 200 506, 360 496, 560 502 C 760 508, 900 528, 1200 516 L1200 630 L0 630Z" fill="#2F6FC4"/>
<path d="M0 534 C 200 520, 360 510, 560 516 C 760 522, 900 542, 1200 530 L1200 630 L0 630Z" fill="#0D1F52"/>
<g transform="translate(80,90) scale(0.62)">{inner}</g>
<text x="232" y="170" font-family="Familjen Grotesk" font-size="64" fill="#fff"><tspan font-weight="400">Open</tspan><tspan font-weight="600">Tide</tspan></text>
<text x="80" y="300" font-family="Familjen Grotesk" font-weight="600" font-size="58" fill="#fff" letter-spacing="-1.5">Build apps with AI agents,</text>
<text x="80" y="368" font-family="Familjen Grotesk" font-weight="600" font-size="58" fill="#86CBEA" letter-spacing="-1.5">one verified change at a time.</text>
<text x="80" y="420" font-family="Familjen Grotesk" font-size="26" fill="#B8C8E2">OpenTide + Tide · Coming soon · opentide.ai</text>
</svg>'''
cairosvg.svg2png(bytestring=og.encode(),write_to='img/og.png')
open('CNAME','w').write('opentide.ai\n')
open('robots.txt','w').write('User-agent: *\nAllow: /\n\nSitemap: https://opentide.ai/sitemap.xml\n')
import datetime
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>https://opentide.ai/</loc>\n    <lastmod>'+datetime.date.today().isoformat()+'</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>\n</urlset>\n')
cairosvg.svg2png(bytestring=mark.encode(),write_to='img/opentide-logo-512.png',output_width=512,output_height=512)
cairosvg.svg2png(bytestring=mark.encode(),write_to='icon-192.png',output_width=192,output_height=192)
import json
open('site.webmanifest','w').write(json.dumps({"name":"OpenTide","short_name":"OpenTide","description":"The web framework for AI agents.","start_url":"/","display":"browser","background_color":"#0A1638","theme_color":"#0A1638","icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/img/opentide-logo-512.png","sizes":"512x512","type":"image/png"}]},indent=2)+'\n')
print('built')
