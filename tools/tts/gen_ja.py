# 日语录音：Kokoro jm_kumo（男声），音素用 jag2p.g2p（以数据里的假名读音为准），可断点续跑
import json, hashlib, os, re, subprocess, numpy as np, time
from kokoro_onnx import Kokoro
from jag2p import g2p
d = json.load(open('texts-ja.json'))
alt = {}
for t, a in d:
    t = t.strip()
    if t and (t not in alt or (a and not alt[t])): alt[t] = a
OUT = 'ja'; os.makedirs(OUT, exist_ok=True)
hid = lambda t: hashlib.md5(t.encode('utf-8')).hexdigest()[:10]
json.dump({t: hid(t) for t in alt}, open('map-ja.json', 'w'), ensure_ascii=False)
k = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
todo = [t for t in alt if not os.path.exists(f'{OUT}/{hid(t)}.ogg')]
print(len(alt), 'unique,', len(todo), 'to do', flush=True)
t0 = time.time(); phlog = open('ja-phonemes.tsv', 'a', encoding='utf-8')
for i, t in enumerate(todo):
    a = alt[t]
    src = a if (a and re.search(r'[A-Za-zＡ-Ｚａ-ｚ]', t)) else t
    try:
        ph = g2p(src, a if src == t else '')
        au, sr = k.create(ph, voice='jm_kumo', speed=1.0, is_phonemes=True)
    except Exception as e:
        print('ERR', repr(t), e, flush=True); continue
    phlog.write(f'{t}\t{a}\t{ph}\n'); phlog.flush()
    au = np.asarray(au, dtype=np.float32)
    nz = np.where(np.abs(au) > 0.01)[0]
    if len(nz): au = au[max(0, nz[0] - 1200): nz[-1] + 2400]
    au = au / max(1e-4, np.abs(au).max()) * 0.89
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 's16le', '-ar', str(sr), '-ac', '1', '-i', '-', '-c:a', 'libopus', '-b:a', '20k', '-application', 'voip', f'{OUT}/{hid(t)}.ogg'], input=(au * 32767).astype(np.int16).tobytes())
    if i % 200 == 0: print(i, round(time.time() - t0), 's', t[:20], flush=True)
print('DONE', len(os.listdir(OUT)), flush=True)
