"""Run once in the release copy: python3 prepare_release.py https://www.example.de"""
from pathlib import Path
from urllib.parse import urlsplit
import sys,json,re,html
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parent
origin=sys.argv[1].rstrip('/') if len(sys.argv)>1 else ''
u=urlsplit(origin)
if u.scheme!='https' or not u.netloc or u.query or u.fragment:raise SystemExit('Provide the confirmed HTTPS origin, with the optional repository path.')
pages=json.loads((root/'release-pages.json').read_text())
def url(lang,slug):return origin+'/'+('fa/' if lang=='fa' else '')+(slug+'/' if slug else '')
for lang,slug,path in pages:
 p=root/path;s=p.read_text();s=re.sub(r'<!-- RELEASE SEO -->.*?<!-- END RELEASE SEO -->','',s,flags=re.S)
 tags='<!-- RELEASE SEO --><link rel="canonical" href="'+url(lang,slug)+'">'
 for l in [l for l in ['de','fa'] if any(a==l and b==slug for a,b,c in pages)]:tags+='<link rel="alternate" hreflang="'+l+'" href="'+url(l,slug)+'">'
 tags+='<link rel="alternate" hreflang="x-default" href="'+url('de',slug)+'"><meta property="og:url" content="'+url(lang,slug)+'"><!-- END RELEASE SEO -->'
 p.write_text(s.replace('</head>',tags+'</head>'))
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(url(l,s))+'</loc></url>' for l,s,p in pages)+'</urlset>')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n')
print('Canonical, reciprocal hreflang, og:url, sitemap and robots.txt ready for '+origin)
