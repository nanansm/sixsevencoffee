# Trace angka "67" dari deck (hal. 27, kartu "Logo marun di atas kertas dulang") jadi path SVG
# Sumber pg-*.jpg sudah dihapus (hemat storage). Ekstrak ulang: cd ../05-aset-brand/dari-deck && pdfimages -j ../../00-brief/deck-67coffee.pdf pg
# Satuan output = piksel crop asli (crop 1100,745 di halaman 1920x1080)
import subprocess,re,os,json
from PIL import Image,ImageFilter
SRC='../05-aset-brand/dari-deck/pg-026.jpg'
S=10
im=Image.open(SRC).convert('RGB').crop((1100,745,1250,860))  # hanya angka (y 12-111)
big=im.resize((im.width*S,im.height*S),Image.LANCZOS).filter(ImageFilter.GaussianBlur(4))
bw=big.split()[1].point(lambda v:0 if v<150 else 255).convert('1')
p=os.environ.get('TMPDIR','/tmp')+'/angka.pbm';bw.save(p)
out=subprocess.run(['potrace','-s','-o','-','--flat','-t','200','-a','1.25','-O','1.2','-r',str(72*S),p],capture_output=True,text=True).stdout
g=re.search(r'<g transform="([^"]+)"',out).group(1);d=' '.join(re.findall(r' d="([^"]+)"',out))
json.dump({'g':g,'d':d},open('tools/logo-trace.json','w'))
print(g,len(d))
