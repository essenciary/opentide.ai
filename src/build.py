import re, cairosvg, io
from PIL import Image
body=open('src/body.html').read()
body=re.sub(r'^<title>.*?</title>\n','',body)
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>OpenTide · The web framework for AI agents</title>
<meta name="description" content="OpenTide is the TypeScript web framework for AI agents. Tide is the IDE reinvented for AI, built on top of it. Coming soon." />
<link rel="canonical" href="https://opentide.ai/" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="OpenTide" />
<meta property="og:url" content="https://opentide.ai/" />
<meta property="og:title" content="OpenTide · The web framework for AI agents" />
<meta property="og:description" content="Build apps with AI agents, one verified change at a time. OpenTide and Tide are coming soon." />
<meta property="og:image" content="https://opentide.ai/img/og.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://opentide.ai/img/og.png" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
<meta name="theme-color" content="#0A1638" />
<meta name="color-scheme" content="light dark" />
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
open('robots.txt','w').write('User-agent: *\nAllow: /\n')
print('built')
