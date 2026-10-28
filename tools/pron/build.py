import json
P = {}
for l in list(open('card_words.txt', encoding='utf-8')):
    if not l.strip(): continue
    en, sy, ipa = [x.strip() for x in l.split('|')]
    if en.lower() not in P: P[en.lower()] = [sy, ipa]
D = json.load(open('drafts.json'))
I = {k: v[1] for k, v in D.items()}
js = ('// 英语发音标注（美式 KK 音标）\n// PRON_EN[单词小写] = [分音节（ˈ主重音 ˌ次重音）, 音标]\n// INTON_EN[句子] = 语调标注：[重读音节] (弱读) ‿连读 | 停顿 ↘降调 ↗升调\n'
      '// 由 tools/pron 生成（words.py → draft.py → build.py），手工修正写在 syl_ovr.txt / phrases_ovr.txt / sent_ovr.txt\n'
      'const PRON_EN = ' + json.dumps(P, ensure_ascii=False, separators=(',', ':')).replace('],"', '],\n"') + ';\n'
      'const INTON_EN = ' + json.dumps(I, ensure_ascii=False, separators=(',', ':')).replace('","', '",\n"') + ';\n')
open('/mnt/user-data/outputs/word-cards/data/pron-en.js', 'w').write(js)
print(len(P), len(I), len(js.encode()))
