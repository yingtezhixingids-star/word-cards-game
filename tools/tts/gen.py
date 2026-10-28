# 用 Kokoro af_heart 合成英语基础词/例句/提示，输出 Opus（ogg），可断点续跑
import json, hashlib, os, sys, subprocess, numpy as np, time
from kokoro_onnx import Kokoro
texts = []
for fn in ('texts.json', 'texts-adv.json'):   # 基础词 + 进阶词
    if not os.path.exists(fn): continue
    T = json.load(open(fn))
    for k in ('w', 'ex', 'hint', 'line'): texts += T.get(k, [])
    if T.get('sample'): texts.append(T['sample'])
uniq = list(dict.fromkeys(t.strip() for t in texts if t and t.strip()))
OUT = 'en'; os.makedirs(OUT, exist_ok=True)
hid = lambda t: hashlib.md5(t.encode('utf-8')).hexdigest()[:10]
json.dump({t: hid(t) for t in uniq}, open('map-en.json', 'w'), ensure_ascii=False)
k = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
todo = [t for t in uniq if not os.path.exists(f'{OUT}/{hid(t)}.ogg')]
print(len(uniq), 'unique,', len(todo), 'to do', flush=True)
t0 = time.time()
for i, t in enumerate(todo):
    try:
        a, sr = k.create(t, voice='af_heart', speed=1.0, lang='en-us')
    except Exception as e:
        print('ERR', repr(t), e, flush=True); continue
    a = np.asarray(a, dtype=np.float32)
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz): a = a[max(0, nz[0] - 1200): nz[-1] + 2400]
    a = a / max(1e-4, np.abs(a).max()) * 0.89
    pcm = (a * 32767).astype(np.int16).tobytes()
    p = subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 's16le', '-ar', str(sr), '-ac', '1', '-i', '-', '-c:a', 'libopus', '-b:a', '20k', '-application', 'voip', f'{OUT}/{hid(t)}.ogg'], input=pcm)
    if i % 200 == 0: print(i, round(time.time() - t0), 's', repr(t)[:40], flush=True)
print('DONE', len(os.listdir(OUT)), flush=True)
