# Nosso Mundinho: guia do projeto

Jogo 3D de casal (Alvaro e Leticia, namoro à distância). Cada um joga no próprio iPhone 13 Pro Max pelo link do GitHub Pages: https://alvaro333x.github.io/nosso-mundinho/
Tudo em português do Brasil. O Alvaro não quer ter que escolher entre opções: decida e entregue pronto.

## Estrutura
- `src/hub_template.html`: **o código-fonte de verdade** (HTML + CSS + JS num arquivo só, ~530 KB). Edite aqui.
- `src/build.py`: gera `index.html` e `version.json` na raiz. Rode da raiz: `python3 src/build.py`.
  - Troca os marcadores `__VALID__`, `__ACC__` e `__ANSWERS__` (dicionário do Termo, a partir de `src/palavras.json` e `src/respostas.txt`), `__THREE__`, `__PEERJS__` e `"__ROOM__"` (`src/room.txt`).
- `index.html`: arquivo gerado. **Nunca edite à mão.**
- `three.min.js` (Three.js r149, UMD, `THREE` global), `peerjs.min.js` e `mqtt.min.js`: bibliotecas locais.
- `version.json`: `{"v":"X"}`. O app consulta esse arquivo e recarrega sozinho quando muda, mas só quando está no mundinho e sem janela aberta (função `maybeUpdate`).

## Publicar
1. Edite `src/hub_template.html` e suba `const VERSION = "X.Y"`.
2. `python3 src/build.py`
3. `node --check` no `<script>` principal (extraia o bloco que começa em `<script>\n` para um .js e confira).
4. `git add -A && git commit -m "..." && git push origin main && git push origin main:gh-pages` (o Pages serve a branch gh-pages).

## Arquitetura (seções do template, nesta ordem)
- **ESTADO LOCAL**: `S` fica no localStorage (`KEY="parquinho-v1"`). `DEF.players`: Alvaro `{build:1 (forte), hair:5, shirt:6 regata preta, acc:2 corrente}` e Leticia `{build:2 (vestido), hair:1 liso longo, shirt:8 amarelo, acc:1 girassol}`.
- **Ícones** (`ICONS`, `EMO2ICO`, `icon()`, `artify()`, `artText()`): emojis viram SVGs próprios. Use `artify(html)` / `artText(txt)` ao montar HTML.
- **Sons**: tudo é WebAudio sintetizado, `snd(nome, arg)`, mais `petSound(sp, vol)`. Sons reais de animais estão em `SAMPLES` (mp3 em base64, dataset ESC-50, CC BY-NC) e tocam com `playSample()`. Volume master .42 e música .22: o Alvaro pediu som baixo.
- **Online** (`NET`, `push(path,data)`, `pushMe({...})`, `screenNet`, `hubNet`): `makeP2PDB()` imita uma API de documentos (`doc().set/onSnapshot`) usando PeerJS (host/guest) e um relay MQTT (broker.emqx.io, mensagens retidas em `mundinho/<ROOM>/d/<path>`). Documentos novos precisam entrar na lista `paths` de `initNet`.
  - Docs: `hub/p0|p1` (posição, emote, petAct, fish, cine…), `jogos/<jogo>` (sessão: `seed`, `start`, `by`, `end`) e `jogos/<jogo>-p0|p1` (progresso de cada um). Também `pesca/p0|p1`, `jardim/canteiros`, coleções `pets` e `galeria`.
  - Sessões: `joinOrCreate(game, extra)` e `newSession(game, extra)`. Os convites aparecem em `refreshBanners`.
- **3D (Three r149)**:
  - Visual 2.0 (`GFX2`): `MeshToonMaterial` foi trocado por uma subclasse de `MeshStandardMaterial` (luz suave), com sRGB, ACES e `ColorManagement.legacyMode=false`. Cores de vértice fixas passam por `LIN()`.
  - Helpers: `MT(cor)`, `CM(cor)` (personagens), `mesh()`, `grp()`, `V3()` e `textTex()`.
  - Personagens: `buildChar(p)` monta tudo procedural; as poses ficam na tabela `POSE` e a animação em `animChar`/`animSwim`.
  - Bichinhos: `buildPet`, `animPet` e o comportamento por espécie em `PBEH`/`startAct`/`petTick` (o papagaio voa com `flyTo`; o jacaré mora no lago com `P.aqua`).
  - Mundo: `buildWorld()`, com árvores agrupadas por `flushTrees`, grama instanciada com vento (`windify`), lago com shader de água (`waterMaterial`, `rippleW`), fonte (`buildFountain`) e a casa do filme Diário de uma Paixão (`houseGroup`).
  - Interior da casa: fica em x=200 (`IN3`). O caminho atravessa a porta com nós de teleporte `{tp:true}`. Cinema só com YouTube sincronizado.
  - Andar: `walkW(i,x,z,onArrive,fromNet)`, que decide se vai nadar, andar no píer ou entrar em casa.
- **Jogos**: Termo (duelo, juntos, por código), Bingo, Caça-palavras, Quiz do casal (`quizGame`), Stop (`stopGame`), Desenha e adivinha (`drawGame`). Ficam nas barraquinhas `BOOTH3`, em volta da pracinha `GP3`, e abrem por `openStation`/`startOnline`.
- **Outros**: pesca com 15 peixes e raridades (`FISH`, `RARITY`, `startFish`, `fishDex`), ateliê com 2 cavaletes (`paintScreen(dono)`), jardim, pets, fonte dos desejos.

## Testes
- Servidor local: `python3 -m http.server 8080` na raiz.
- No Playwright (Chrome headless) use `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`. O headless é lento (FPS baixo), então dê tempo para as animações.
- Para testar dois celulares, abra duas abas com servidores locais: PeerJS (`peer --port 9000 --path /myapp`) e um broker MQTT por websocket (aedes). Antes do app carregar, injete `window.__PEER_OPTS={host:'127.0.0.1',port:9000,path:'/myapp',secure:false}; window.__MQTT_URL='ws://127.0.0.1:8884/mqtt'`.
- Mantenha o `version.json` local igual à `VERSION`, senão a página recarrega sozinha no meio do teste.

## Cuidados
- iPhone: zoom de toque duplo está bloqueado; câmera com 1 dedo gira, 2 dedos dão zoom (`ptrs` limpa “dedos fantasma”). Use `touch-action` e `pointer events`.
- Performance: o jogo roda no celular, então evite muitos draw calls (use instancing/merge, como em `flushTrees` e `buildGrass`).
- Não edite `index.html` direto. Sempre `src/` → `build.py`.
- Netflix foi removida a pedido (não dá para integrar). Não recoloque.

## Ideias pendentes
- Trocar árvores, arbustos, pedras, móveis e os peixes da pesca por modelos CC0 da Quaternius (`.glb`). Requer o GLTFLoader: use three r147 UMD + `examples/js/loaders/GLTFLoader.js` ou migre para ES modules. Cuidado: o estilo deles é facetado, e o Alvaro reclamou de visual “geométrico”.
- Mais minigames: Lig 4, Jogo da memória, Torneio de pesca, Batalha naval, Forca.
