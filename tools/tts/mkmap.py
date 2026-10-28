# 把合成好的录音复制到 word-cards/audio/<语言>/，并生成 data/audio-<语言>.js 索引。用法：python3 mkmap.py [en ja ...]
import json, os, shutil, sys
W = '/mnt/user-data/outputs/word-cards'
for L in (sys.argv[1:] or ['en', 'ja']):
    m = json.load(open(f'map-{L}.json'))
    ok = {t: h for t, h in m.items() if os.path.exists(f'{L}/{h}.ogg') and os.path.getsize(f'{L}/{h}.ogg') > 200}
    os.makedirs(f'{W}/audio/{L}', exist_ok=True)
    for h in ok.values():
        d = f'{W}/audio/{L}/{h}.ogg'
        if not os.path.exists(d): shutil.copy(f'{L}/{h}.ogg', d)
    open(f'{W}/data/audio-{L}.js', 'w', encoding='utf-8').write(f'// 内置录音索引（Kokoro 合成）：文本 → audio/{L}/<文件名>.ogg\nwindow.AUD_{L.upper()} = ' + json.dumps(ok, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print(L, len(ok), 'of', len(m))
