#!/usr/bin/env python3
"""Set the real site origin and generate sitemap.xml. Usage: python3 scripts/generate_seo.py https://example.com"""
from pathlib import Path
from urllib.parse import urlparse
import sys, re
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:
    raise SystemExit('Usage: python3 scripts/generate_seo.py https://your-real-domain.com')
url=sys.argv[1].rstrip('/')
p=urlparse(url)
if p.scheme!='https' or not p.netloc or p.path not in ('','/') or p.query or p.fragment or 'example' in p.netloc.lower() or 'your-domain' in p.netloc.lower():
    raise SystemExit('Pass your real HTTPS domain only, e.g. https://techaivibes.com')
origin=f'{p.scheme}://{p.netloc}'
# Replace structured-data/feed URL placeholders and add canonical links per HTML page.
for f in ROOT.rglob('*.html'):
    if 'scripts' in f.parts: continue
    rel=f.relative_to(ROOT).as_posix()
    if rel=='index.html': path='/'
    elif rel.endswith('/index.html'): path='/' + rel[:-10]
    else: path='/' + rel
    page_url=origin+path
    s=f.read_text()
    s=s.replace('https://YOUR-DOMAIN-HERE.example',origin)
    if 'rel="canonical"' not in s:
        s=s.replace('</head>',f'<link rel="canonical" href="{page_url}"></head>',1)
    f.write_text(s)
feed=ROOT/'feed.xml'
if feed.exists(): feed.write_text(feed.read_text().replace('https://YOUR-DOMAIN-HERE.example',origin))
# Sitemap contains only public HTML pages; PDFs are added only after real files exist.
urls=[]
for f in ROOT.rglob('*.html'):
    if 'scripts' in f.parts: continue
    rel=f.relative_to(ROOT).as_posix()
    path='/' if rel=='index.html' else ('/'+rel[:-10] if rel.endswith('/index.html') else '/'+rel)
    urls.append(origin+path)
urls=sorted(set(urls))
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls)+'</urlset>\n'
(ROOT/'sitemap.xml').write_text(xml)
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+origin+'/sitemap.xml\n')
print(f'Updated canonical URLs and generated sitemap.xml with {len(urls)} HTML URLs for {origin}')
