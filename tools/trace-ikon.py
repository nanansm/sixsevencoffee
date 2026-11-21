# Trace 12 ikon kota dari deck hal. 24 (baris garis marun di atas kertas) -> tools/ikon-trace.json
# Sumber gambar sudah dihapus dari VPS. Ambil ulang deck dari R2 mote-team berkas/65bec3cd-793b-47a2-9f62-3dab6c4c5360.pdf, lalu: mkdir -p ../05-aset-brand/dari-deck && cd ../05-aset-brand/dari-deck && pdfimages -j deck.pdf pg
import subprocess,re,os,json
from PIL import Image,ImageFilter
SRC='../05-aset-brand/dari-deck/pg-023.jpg'
NAMA=['cup','es','vdrip','filter','biji','rendang','pagi','malam','lampu','kedai','vespa','kartu']
CX=[186,326,467,608,748,889,1029,1170,1311,1451,1592,1733]
S=10;im=Image.open(SRC).convert('RGB');out={}
for n,cx in zip(NAMA,CX):
    c=im.crop((cx-68,378,cx+52,482))
    g=c.split()[1]
    bb=g.point(lambda v:255 if v<150 else 0).getbbox()
    c=c.crop((bb[0]-3,bb[1]-3,bb[2]+3,bb[3]+3))
    big=c.resize((c.width*S,c.height*S),Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
    bw=big.split()[1].point(lambda v:0 if v<160 else 255).convert('1')
    p=os.environ['TMPDIR']+f'/{n}.pbm';bw.save(p)
    o=subprocess.run(['potrace','-s','-o','-','--flat','-t','150','-a','1.2','-O','1.0','-r',str(72*S),p],capture_output=True,text=True).stdout
    out[n]=dict(w=c.width,h=c.height,g=re.search(r'<g transform="([^"]+)"',o).group(1),d=' '.join(re.findall(r' d="([^"]+)"',o)))
    print(n,c.size,len(out[n]['d']))
json.dump(out,open('tools/ikon-trace.json','w'))
