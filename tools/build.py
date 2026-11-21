# Rakit public/index.html biolink 67 Coffee (HTML statis, CSS inline)
# Jalankan dari root 05-biolink: python3 tools/build.py
# Style = deck Campaign Strategy 67 Coffee 2026-2027 (hal. 23 Warna & Huruf, hal. 27 Aturan Pakai)
import json
SITE = 'https://sixsevencoffee.pages.dev/'  # ganti ke domain asli saat domain dipasang
L = json.load(open('tools/tautan.json'))
T = json.load(open('tools/logo-trace.json'))

def ext(u):  # link kosong '#' tidak dibuka di tab baru
    return '' if u == '#' else ' target="_blank" rel="noopener"'

# Logo: angka 67 hasil trace deck + COFFEE + garis biji (satuan = piksel crop deck)
LOGO = f'''<svg class="logo" viewBox="6 8 136 146" role="img" aria-label="67 Coffee">
<g fill="currentColor"><g transform="{T['g']}"><path d="{T['d']}"/></g>
<text x="11" y="135.5" textLength="126" lengthAdjust="spacing" font-family="Jost,sans-serif" font-size="17.6">COFFEE</text>
<rect x="11" y="145.6" width="54" height="1.3"/><rect x="83" y="145.6" width="54" height="1.3"/>
<ellipse cx="74" cy="146.3" rx="3.9" ry="5.6" transform="rotate(24 74 146.3)"/></g>
<path d="M72.3 142q3 4.3 .3 8.8" fill="none" stroke="#EFE7DA" stroke-width=".9" stroke-linecap="round"/>
</svg>'''

# Ikon garis tunggal, ujung bulat (gaya "Dua Belas Ikon Kota")
def ik(name, cls='ik'):
    P = {
     'menu': '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M9 8h6M9 12h6M9 16h4"/>',
     'wa': '<path d="M4.5 19.5l1.2-3.6A8 8 0 1 1 8.6 19z"/><path d="M9.2 8.6c0 3.2 2.9 6.1 6 6.1l1.2-1.6-2.1-1-.9.9a4 4 0 0 1-2.3-2.3l.9-.9-1-2.1z"/>',
     'pin': '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
     'ig': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r=".6" fill="currentColor"/>',
     'tt': '<path d="M14 3.5v11.2a3.7 3.7 0 1 1-3.7-3.7"/><path d="M14 3.5c.4 2.7 2.3 4.4 5 4.6"/>',
     'panah': '<path d="M5 12h14M13 6l6 6-6 6"/>',
     'kedai': '<path d="M4 20V10M20 20V10M3 10h18l-1.5-5h-15z"/><path d="M3 10c0 1.4 1.3 2.2 2.5 2.2S8 11.4 8 10c0 1.4 1.3 2.2 2.5 2.2S13 11.4 13 10c0 1.4 1.3 2.2 2.5 2.2S18 11.4 18 10c0 1.4 1.2 2.2 2.5 2.2"/><path d="M10 20v-5h4v5M2.5 20h19"/>',
     'gelas': '<path d="M6.5 9h11l-1.3 11.5H7.8z"/><path d="M5.5 9h13M7 9l.6-2.5h8.8L17 9M13 6.5 14.5 2.5"/><path d="M7.2 13.5h9.6"/>',
     'cangkir': '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 10.5h1.5a2.3 2.3 0 0 1 0 4.6H16"/><path d="M9 3.5c-.8 1 .8 2 0 3M12.5 3.5c-.8 1 .8 2 0 3"/>',
     'motor': '<circle cx="6" cy="17" r="2.6"/><circle cx="18" cy="17" r="2.6"/><path d="M8.6 17h6.8M15.4 17l-2.4-7H9.5M13 10h3.5l1.5 7M7 13.5h4.5"/>',
     'bulan': '<path d="M15.5 4.5A7.8 7.8 0 1 0 19.5 16 6.3 6.3 0 0 1 15.5 4.5z"/><path d="M19 4v3M17.5 5.5h3"/>',
    }
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'


# 12 ikon kota hasil trace deck hal. 24 -> <symbol>, kotak seragam 90 supaya tebal garis konsisten
K = json.load(open('tools/ikon-trace.json'))
def _sym(n, v):
    ox, oy = (90 - v['w']) / 2, (90 - v['h']) / 2
    return f'<symbol id="k-{n}" viewBox="0 0 90 90"><g transform="translate({ox:.1f} {oy:.1f})"><g transform="{v["g"]}"><path d="{v["d"]}"/></g></g></symbol>'
def _tight(n, v):
    return f'<symbol id="t-{n}" viewBox="0 0 {v["w"]} {v["h"]}"><g transform="{v["g"]}"><path d="{v["d"]}"/></g></symbol>'
JALAN = ['lampu','kedai','vespa','malam']
SYMS = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + ''.join(_sym(n, v) for n, v in K.items()) + ''.join(_tight(n, K[n]) for n in JALAN) + '</svg>'
def kt(n, cls):
    v = K[n]
    return f'<svg class="{cls}" viewBox="0 0 {v["w"]} {v["h"]}" aria-hidden="true"><use href="#t-{n}"/></svg>'
def kk(n, cls='kk'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#k-{n}"/></svg>'

def tombol(no, ikon, judul, ket, url, label, utama=False, kota=False):
    c = 'tb utama' if utama else 'tb'
    i = kk(ikon, 'ik kota') if kota else ik(ikon)
    return f'''<li><a class="{c}" href="{url}"{ext(url)} aria-label="{label}">
{i}<span class="tx"><b>{judul}</b><small>{ket}</small></span>{ik('panah','pn')}</a></li>'''

def antar(nama, img, w, h, url):
    return f'''<li><a class="antar" href="{url}"{ext(url)} aria-label="Pesan 67 Coffee lewat {nama}">
<img src="/assets/{img}" alt="" width="{w}" height="{h}"><span>{nama}</span></a></li>'''

FONTS = [('Instrument Serif','instrument-serif-400','normal'),('Newsreader','newsreader-400','normal'),
         ('Newsreader','newsreader-400-i','italic'),('Courier Prime','courier-prime-400','normal'),
         ('Jost','jost-400','normal')]
FF = '\n'.join(f"@font-face{{font-family:'{f}';src:url(/fonts/{n}.woff2) format('woff2');font-style:{s};font-weight:400;font-display:swap}}" for f,n,s in FONTS)
FF += "\n@font-face{font-family:'Courier Prime';src:url(/fonts/courier-prime-700.woff2) format('woff2');font-weight:700;font-display:swap}"

CSS = FF + '''
:root{--kertas:#EFE7DA;--marun:#6E1621;--kalio:#2E1712;--krem:#F3E9D8;--kunyit:#F2A23A;--garis:rgba(110,22,33,.22)}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--kertas)}
body{min-height:100vh;background:var(--kertas) url(/assets/butir.webp);color:var(--kalio);font:400 16px/1.5 'Newsreader',Georgia,serif;-webkit-font-smoothing:antialiased;display:flex;flex-direction:column;overflow-x:hidden}
a{color:inherit;text-decoration:none}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.mono{font-family:'Courier Prime',monospace;font-weight:700;text-transform:uppercase;letter-spacing:.14em;font-size:12px;color:var(--marun)}
.kol{width:100%;max-width:440px;margin:0 auto;padding:0 22px}
.kk,.jalur svg,.jalan svg,.ik.kota{fill:currentColor}
/* kepala: logo */
.kepala{text-align:center;padding-top:56px}
.panggung{position:relative;width:236px;margin:0 auto}
.logo{width:120px;height:auto;color:var(--marun);display:block;margin:0 auto}
.tag{font-family:'Instrument Serif',Georgia,serif;font-size:clamp(34px,10.4vw,46px);line-height:1;color:var(--marun);margin-top:34px;white-space:nowrap;letter-spacing:-.01em;position:relative;display:inline-block}
.tag i{font-style:normal;position:relative}
.coret{position:absolute;left:-4%;right:-4%;bottom:-10px;width:108%;height:12px;fill:none;stroke:var(--marun);stroke-width:2.4;stroke-linecap:round}
.bag{margin-top:30px}
.bag>.mono{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.bag>.mono:after{content:"";flex:1;height:1px;background:var(--garis)}
ul{list-style:none}
.daftar li+li{margin-top:10px}
.tb{display:flex;align-items:center;gap:14px;min-height:70px;padding:12px 16px;background:var(--krem);border:1px solid var(--garis);border-radius:3px;transition:background .2s,transform .2s}
.tb:hover{background:#F7EFE2}.tb:active{transform:translateY(1px)}
.tb .no{font-family:'Courier Prime',monospace;font-weight:700;font-size:12px;letter-spacing:.1em;color:var(--marun);opacity:.75;width:20px}
.tb .ik{width:26px;height:26px;flex:none;fill:none;stroke:var(--marun);stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.tb .ik.kota{width:32px;height:32px;fill:var(--marun);stroke:none;margin:-3px}
.tb .tx{flex:1;display:flex;flex-direction:column;min-width:0}
.tb b{font-family:'Instrument Serif',Georgia,serif;font-weight:400;font-size:24px;line-height:1.1;color:var(--kalio)}
.tb small{font-family:'Courier Prime',monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--kalio);opacity:.78;margin-top:3px}
.tb .pn{width:18px;height:18px;flex:none;fill:none;stroke:var(--marun);stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;transition:transform .2s}
.tb:hover .pn{transform:translateX(3px)}
.tb.utama{background:var(--marun);border-color:var(--marun)}
.tb.utama:hover{background:#5E121C}
.tb.utama .no,.tb.utama b,.tb.utama small{color:var(--krem)}
.tb.utama .ik,.tb.utama .pn{stroke:var(--krem)}
.tiga{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.antar{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:9px;height:96px;background:var(--krem);border:1px solid var(--garis);border-radius:3px;transition:background .2s}
.antar:hover{background:#F7EFE2}
.antar img{height:30px;width:auto;max-width:72px}
.antar span{font-family:'Courier Prime',monospace;font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--kalio)}
main{flex:1;padding-bottom:52px}
/* pita marun: 12 ikon kota berjalan pelan */
.pita{background:var(--marun);color:var(--krem);overflow:hidden;padding:16px 0;border-top:1px solid var(--marun)}
.jalur{display:flex;width:max-content;animation:jalan 48s linear infinite}
.jalur svg{width:46px;height:46px;margin:0 19px;flex:none}
@keyframes jalan{to{transform:translateX(-50%)}}
/* kaki: jalan Cisangkuy malam */
.kaki{background:var(--kalio);color:var(--krem);text-align:center;padding:0 0 26px}
.jalan{display:flex;align-items:flex-end;justify-content:center;gap:26px;padding:56px 0 0;border-bottom:1.5px solid rgba(243,233,216,.55);position:relative;color:var(--krem)}
.jalan svg{flex:none}
.jalan .lp{height:92px;width:auto;margin-bottom:-1px}
.jalan .kd{height:96px;width:auto;margin-bottom:-1px}
.jalan .vs{height:50px;width:auto;margin-bottom:-1px}
.jalan .ml{position:absolute;height:34px;width:auto;right:8%;top:20px;opacity:.7}
.rentang{font-family:'Courier Prime',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;line-height:2;margin-top:26px;opacity:.9}
.sosmed{display:flex;justify-content:center;gap:12px;margin-top:20px}
.sosmed a{width:44px;height:44px;border:1px solid rgba(243,233,216,.35);border-radius:50%;display:grid;place-items:center;transition:background .2s}
.sosmed a:hover{background:rgba(243,233,216,.1)}
.sosmed svg{width:20px;height:20px;fill:none;stroke:var(--krem);stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.akun{font-family:'Courier Prime',monospace;font-size:12px;letter-spacing:.1em;margin-top:12px;opacity:.85}
.hak{font-family:'Courier Prime',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.6;margin-top:30px;padding-top:14px;border-top:1px solid rgba(243,233,216,.18)}
.titik{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--kunyit);margin-right:8px;vertical-align:1px}
@media(max-width:360px){.antar span{letter-spacing:0;font-size:11px}.tiga{gap:8px}}
@media(min-width:700px){.kepala{padding-top:72px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}.jalur{animation:none}}
'''

DESC = '67 Coffee, kedai kopi di Jl. Cisangkuy 58, Bandung. Menu, WhatsApp admin, delivery order, dan Direct Maps dalam satu halaman.'
LD = json.dumps({"@context":"https://schema.org","@type":"CafeOrCoffeeShop","name":"67 Coffee","url":SITE,
    "address":{"@type":"PostalAddress","streetAddress":"Jl. Cisangkuy No. 58","addressLocality":"Bandung","addressRegion":"Jawa Barat","addressCountry":"ID"},
    "sameAs":[L['INSTAGRAM']]}, ensure_ascii=False)

URUT = ['cup','es','vdrip','filter','biji','rendang','pagi','malam','lampu','kedai','vespa','kartu']
PITA = ''.join(kk(n) for n in URUT) * 2

HTML = f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>67 Coffee · Coffee in Between</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}">
<meta name="theme-color" content="#EFE7DA">
<meta property="og:type" content="website"><meta property="og:url" content="{SITE}">
<meta property="og:title" content="67 Coffee · Coffee in Between"><meta property="og:description" content="{DESC}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/instrument-serif-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/courier-prime-700.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
<script type="application/ld+json">{LD}</script>
</head>
<body>
{SYMS}
<main>
<div class="kol">
<header class="kepala">
<div class="panggung">
<h1><span class="sr">67 Coffee</span>{LOGO}</h1>
</div>
<p class="tag">Coffee <i>in Between.<svg class="coret" viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden="true"><path d="M3 7.5c30-4 62-5.2 96-3.6 30 1.3 58 1.6 98-1.2"/></svg></i></p>
</header>

<section class="bag" aria-label="Tautan utama">
<span class="mono">01 — Menu &amp; Admin</span>
<ul class="daftar">
{tombol('01','filter','Menu','Daftar menu &amp; harga',L['MENU'],'Lihat menu 67 Coffee',kota=True)}
{tombol('02','wa','WhatsApp Admin','Tanya &amp; pesan',L['WHATSAPP'],'Chat admin 67 Coffee lewat WhatsApp',utama=True)}
</ul>
</section>

<section class="bag" aria-label="Delivery order">
<span class="mono">02 — Delivery Order</span>
<ul class="tiga">
{antar('GoFood','ikon-gofood.svg',31,28,L['GOFOOD'])}
{antar('GrabFood','ikon-grabfood.svg',66,30,L['GRABFOOD'])}
{antar('ShopeeFood','ikon-shopeefood.svg',25,28,L['SHOPEEFOOD'])}
</ul>
</section>

<section class="bag" aria-label="Lokasi">
<span class="mono">03 — Lokasi</span>
<ul class="daftar">
{tombol('03','pin','Direct Maps','Google Maps',L['MAPS'],'Buka Direct Maps ke 67 Coffee di Google Maps')}
</ul>
</section>
</div>
</main>

<div class="pita" aria-hidden="true"><div class="jalur">{PITA}</div></div>
<footer class="kaki">
<div class="kol">
<div class="jalan" aria-hidden="true">{kt('lampu','lp')}{kt('kedai','kd')}{kt('vespa','vs')}{kt('lampu','lp')}{kt('malam','ml')}</div>
<p class="rentang">Jl. Cisangkuy No. 58, Bandung<br>Depan Narendang Prime</p>
<nav class="sosmed" aria-label="Media sosial 67 Coffee">
<a href="{L['INSTAGRAM']}"{ext(L['INSTAGRAM'])} aria-label="Instagram 67 Coffee">{ik('ig')}</a>
<a href="{L['TIKTOK']}"{ext(L['TIKTOK'])} aria-label="TikTok 67 Coffee">{ik('tt')}</a>
</nav>
<p class="akun">@sixseven.coffee</p>
<p class="hak"><i class="titik"></i>© 2026 67 Coffee</p>
</div>
</footer>
</body>
</html>
'''
open('public/index.html','w').write(HTML)
open('public/assets/favicon.svg','w').write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="2 -10 144 144"><rect x="2" y="-10" width="144" height="144" rx="26" fill="#6E1621"/><g fill="#EFE7DA" transform="translate(4 4)"><g transform="{T['g']}"><path d="{T['d']}"/></g></g></svg>''')
print('ok', len(HTML))
open('public/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
open('public/sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}</loc></url></urlset>\n')
