import soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
from misaki import ja
g2p = ja.JAG2P()
k = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
items = ['皿', 'お皿を取ってください。', 'おわん', 'ご飯を一杯ください。', 'カップ', 'お茶を一杯いかが？']
gap = np.zeros(int(24000 * .7), dtype=np.float32)
for v in ['jf_alpha', 'jf_gongitsune', 'jf_nezumi', 'jf_tebukuro', 'jm_kumo']:
    parts = []
    for it in items:
        ph = g2p(it); print(v, it, ph)
        a, sr = k.create(ph, voice=v, speed=1.0, is_phonemes=True); parts += [a, gap]
    sf.write(f'ja-{v}.wav', np.concatenate(parts), 24000)
