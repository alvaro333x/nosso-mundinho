# Gera ../index.html a partir de hub_template.html
# Uso: python3 src/build.py   (rodar da raiz do repositório)
import json, os
D=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(D)
valid=json.load(open(os.path.join(D,'palavras.json'),encoding='utf-8'))['valid']
ans=[w for w in open(os.path.join(D,'respostas.txt'),encoding='utf-8').read().split() if w]
acc={k:v for k,v in valid.items() if k!=v}
t=open(os.path.join(D,'hub_template.html'),encoding='utf-8').read()
t=t.replace('__VALID__',' '.join(sorted(valid))).replace('__ACC__',json.dumps(acc,ensure_ascii=False,separators=(',',':'))).replace('__ANSWERS__',' '.join(ans))
room=open(os.path.join(D,'room.txt')).read().strip()
gh=t.replace('__PEERJS__','<script src="peerjs.min.js"></script><script src="mqtt.min.js"></script>').replace('__THREE__','<script src="three.min.js"></script>').replace('"__ROOM__"',json.dumps(room))
open(os.path.join(ROOT,'index.html'),'w',encoding='utf-8').write(gh)
v=t.split('const VERSION = "')[1].split('"')[0]
open(os.path.join(ROOT,'version.json'),'w').write(json.dumps({'v':v}))
print('ok: index.html gerado, versão',v)
