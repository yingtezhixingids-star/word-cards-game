import soundfile as sf, numpy as np, time
from kokoro_onnx import Kokoro
k = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
items = ['plate', 'Pass me a plate, please.', 'bowl', 'A bowl of rice, please.']
voices = [('美式女声A', 'af_heart', 'en-us'), ('美式女声B', 'af_bella', 'en-us'), ('美式男声A', 'am_michael', 'en-us'), ('美式男声B', 'am_fenrir', 'en-us'),
          ('英式女声', 'bf_emma', 'en-gb'), ('英式男声', 'bm_george', 'en-gb')]
gap = np.zeros(int(24000 * .7), dtype=np.float32)
t0 = time.time(); total = 0
for name, v, lang in voices:
    parts = []
    for it in items:
        a, sr = k.create(it, voice=v, speed=1.0, lang=lang); parts += [a, gap]; total += len(a) / sr
    sf.write(f'{name}-{v}.wav', np.concatenate(parts), 24000)
print('audio', round(total, 1), 's in', round(time.time() - t0, 1), 's')
