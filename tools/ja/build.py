import re, json, os, sys, unicodedata
from sudachipy import dictionary, tokenizer
import pykakasi
T = dictionary.Dictionary().create(); MODE = tokenizer.Tokenizer.SplitMode.C
KK = pykakasi.kakasi()
D = os.path.dirname(os.path.abspath(__file__))
FIX = {}
if os.path.exists(D + '/fix.txt'):
    for l in open(D + '/fix.txt', encoding='utf8'):
        if '=' in l and not l.startswith('#'): a, b = l.rstrip('\n').split('=', 1); FIX[a] = b
def hira(s): return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)
FIXR = [('なんを', 'なにを'), ('つらいですか', 'からいですか'), ('からしは つらい', 'からしは からい'), ('わたくし', 'わたし'),
  ('かずふさ', 'ひとふさ'), ('しゅが', 'たねが'), ('ムール かい', 'ムールがい'), ('いちふくろ', 'ひとふくろ'), ('いちパック', 'ひとパック'),
  ('いちきん', 'いっきん'), ('しょうが ゆ', 'しょうがゆ'), ('はちみつ ゆ', 'はちみつゆ'), ('ふぁーちう', 'ほあじゃお'), ('さらだゆ', 'さらだあぶら'),
  ('けいにくに ひが かよって', 'とりにくに ひが とおって'), ('のどあめはの どの', 'のどあめは のどの'), ('あす ', 'あした '),
  ('ろくこ', 'ろっこ'), ('じゅうふんかん', 'じゅっぷんかん'), ('ビタミン C', 'ビタミンC'), ('L サイズ', 'Lサイズ'),
  ('ひと きれ', 'ひときれ'), ('ひと さら', 'ひとさら'), ('あま すぎ', 'あますぎ'), ('つよ すぎ', 'つよすぎ'), ('おお すぎ', 'おおすぎ'), ('さーびすりょう', 'サービスりょう'), ('あかわいん', 'あかワイン'), ('しろわいん', 'しろワイン'), ('こなみるく', 'こなミルク'), ('やき かし', 'やきがし'), ('むし パン', 'むしパン'), ('あげ パン', 'あげパン'), ('ぺきん ダック', 'ペキンダック'), ('ぱんや', 'パンや'), ('ろくぽん', 'ろっぽん'), ('はちぽん', 'はっぽん'), ('いちまんほ', 'いちまんぽ'),
  ('ながしの もと', 'ながしの した'), ('お ひさま', 'おひさま'), ('よんつ', 'よっつ'), ('むいつ', 'むっつ'), ('ゆびわは かね', 'ゆびわは きん'),
  ('なながつ', 'しちがつ'), ('ななじ', 'しちじ'), ('あすは', 'あしたは'), ('ネット さい', 'ネットぎわ'), ('なんか', 'なにか'), ('なんも', 'なにも'),
  ('サイには かど', 'サイには つの'), ('ひと なつっこい', 'ひとなつっこい'), ('なんよう ひ', 'なんようび'), ('さいしゅうばす', 'さいしゅうバス'), ('いつから なんじ', 'なんじから なんじ'), ('ひが かよって', 'ひが とおって'), ('おいえ', 'おうち'), ('なんが', 'なにが'), ('ばんごはんは なん？', 'ばんごはんは なに？'), ('いちかい', 'いっかい'), ('じゅうかい', 'じゅっかい')]
SURF = {'何時': 'なんじ', '鶏肉': 'とりにく', '種': 'たね', '鉢': 'はち'}
NOSPACE = ('助詞', '助動詞', '補助記号', '接尾辞')
def kana(s, keep_kata=True):
    """句子的读音：汉字转成平假名，片假名保留；按词组加空格"""
    if s in FIX: return FIX[s]
    out = []; prev = None
    for m in T.tokenize(s, MODE):
        surf = m.surface(); pos = m.part_of_speech()[0]
        if re.fullmatch(r'[぀-ゟ゠-ヿー]+', surf): r = surf          # 本来就是假名
        elif surf in SURF: r = SURF[surf]
        elif surf == '箱' and (not out or prev in ('助詞', '補助記号', '連体詞')): r = 'はこ'
        elif re.search(r'[一-鿿々]', surf):
            r = hira(m.reading_form())
            for run in re.findall(r'[ァ-ヶー]+', surf):   # 片假名部分保留原样
                if hira(run) in r: r = r.replace(hira(run), run, 1)
        else: r = surf
        num = m.part_of_speech()[1] == '数詞'
        if out and pos not in NOSPACE and prev not in ('接頭辞', '数詞') and not re.fullmatch(r'[、。！？!?（）()]', surf) and not out[-1].endswith(('（', '(')): out.append(' ')
        out.append(r); prev = '数詞' if num else pos
    r = ''.join(out).replace(' 、', '、').replace('、 ', '、')
    for a, b in FIXR: r = r.replace(a, b)
    r = re.sub(r'よんじ(?!ゅう)', 'よじ', r).replace('よじゅう', 'よんじゅう').replace('よんじゅうしゅうねん', 'よんじゅっしゅうねん')
    return r
def romaji(k):
    r = ' '.join(x['hepburn'] for x in KK.convert(k) if x['hepburn'].strip())
    return re.sub(r'\s+', ' ', r).strip()
def word_rom(w, k):
    ro = romaji(k).replace(' ', '')
    seg = kana(w)
    if ' ' in seg and hira(seg.replace(' ', '')) == hira(k): ro = ' '.join(romaji(x).replace(' ', '') for x in seg.split(' '))
    return ro if w == k or hira(w) == hira(k) or re.fullmatch(r'[゠-ヿー]+', w) else f'{k} · {ro}'
def build(src, dst, base):
    en = open(base, encoding='utf8').read(); keys = {}
    for m in re.finditer(r"S\('(\w+)',.*?`(.*?)`\);", en, re.S):
        keys[m.group(1)] = [l.split('|')[0].strip() for l in m.group(2).strip().split('\n') if l.strip()]
    out = []; seen = {}; cur = None; first = True
    for line in open(src, encoding='utf8'):
        line = line.rstrip('\n')
        if not line.strip(): continue
        if line.startswith('#'):
            cid, name = line[1:].split('|'); out.append(f"XC('ja', {json.dumps(cid)}, {json.dumps(name, ensure_ascii=False)}, {json.dumps(kana(name), ensure_ascii=False)});")
        elif line.startswith('@'):
            if not first: out.append(']);')
            first = False
            sid, name, foe, av, ln, lnzh = line[1:].split('|'); cur = sid; seen[sid] = []
            a = [sid, name, kana(name), foe, av, ln, kana(ln), lnzh]
            out.append("XS('ja', " + ', '.join(json.dumps(x, ensure_ascii=False) for x in a) + ', [')
        else:
            p = line.split('|'); k, w, kw, ex = p[:4]; zh = p[4] if len(p) > 4 else ''
            for run in re.findall(r'[\u30a1-\u30f6ー]+', w):
                if hira(run) in kw and run != w: kw = kw.replace(hira(run), run, 1)
            assert k in keys[cur], (cur, k); seen[cur].append(k)
            ek = kana(ex)
            # 例句里出现了这个词、但自动读音和我给的读音不同 → 用我给的读音
            if w in ex and w not in ('日', '月', '湖') and not re.search(r'[A-Za-z0-9]', w):
                rw = kana(w).replace(' ', '')
                if hira(rw) != hira(kw) and kw.replace(' ', '') not in ek.replace(' ', ''):
                    pat = r'\s?'.join(re.escape(c) for c in rw)
                    ek2 = re.sub(pat, kw, ek, count=1)
                    if ek2 == ek: print('NOFIX', w, kw, ek)
                    ek = ek2
            out.append('  ' + json.dumps([k, w, word_rom(w, kw), ex, ek, zh, kw, ek.replace(' ', '')], ensure_ascii=False) + ',')
    out.append(']);')
    for sid, ks in seen.items():
        miss = set(keys[sid]) - set(ks)
        if miss: print('MISSING', sid, miss)
    open(dst, 'w', encoding='utf8').write('// 日语词库（自动生成，源文件 ja/*.txt）\n' + '\n'.join(out) + '\n')
    print('wrote', dst, sum(len(v) for v in seen.values()))
W = '/mnt/user-data/outputs/word-cards'
os.makedirs(W + '/data/ja', exist_ok=True)
CH = [('people','01-people'),('appearance','02-appearance'),('health','03-health'),('home','04-home'),('city','05-city'),('food','06-food'),('study','07-study'),('work','08-work'),('transport','09-transport'),('sports','10-sports'),('leisure','11-leisure'),('environment','12-environment'),('nature','13-nature'),('reference','14-reference')]
only = sys.argv[1:]
for a, b in CH:
    if only and a not in only: continue
    build(f'{D}/{a}.txt', f'{W}/data/ja/{b}.js', f'{W}/data/{b}.js')
