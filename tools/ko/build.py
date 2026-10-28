import re, json, os, sys
import g2pk2.g2pk2 as gg
gg.annotate = lambda s, m: s          # 没有 mecab，跳过词性标注（影响很小）
from g2pk2 import G2p
from korean_romanizer.romanizer import Romanizer
G = G2p()
D = os.path.dirname(os.path.abspath(__file__))
FIX = {}
if os.path.exists(D + '/fix.txt'):
    for l in open(D + '/fix.txt', encoding='utf8'):
        if '=' in l and not l.startswith('#'): a, b = l.rstrip('\n').split('=', 1); FIX[a] = b
TENSE = {1: 0, 4: 3, 8: 7, 10: 9, 13: 12}   # ㄲ→ㄱ ㄸ→ㄷ ㅃ→ㅂ ㅆ→ㅅ ㅉ→ㅈ（初声编号）
def untense(orig, pron):
    """罗马字按国家标准不标紧音：发音规则产生的紧音（如 독감→독깜）还原成松音"""
    if len(orig) != len(pron): return pron
    out = []
    for a, b in zip(orig, pron):
        if '가' <= a <= '힣' and '가' <= b <= '힣':
            ia, ib = (ord(a) - 0xAC00) // 588, (ord(b) - 0xAC00) // 588
            if ib in TENSE and TENSE[ib] == ia: b = chr(ord(b) - (ib - ia) * 588)
        out.append(b)
    return ''.join(out)
def rom(t):
    """先按发音规则变音（连音、鼻音化、紧音……），再转成罗马字"""
    if t in FIX: return FIX[t]
    t = re.sub(r'[()（）]', ' ', t)
    # 按词（空格）分开处理：国家标准只在词内部变音，不跨词
    r = ' '.join(Romanizer(untense(x, G(x))).romanize().replace('lr', 'll') for x in t.split())
    r = re.sub(r'\s+', ' ', r).strip()
    return r[:1].lower() + r[1:] if r else r
def build(src, dst, base):
    en = open(base, encoding='utf8').read(); keys = {}
    for m in re.finditer(r"S\('(\w+)',.*?`(.*?)`\);", en, re.S):
        keys[m.group(1)] = [l.split('|')[0].strip() for l in m.group(2).strip().split('\n') if l.strip()]
    out = []; seen = {}; cur = None; first = True
    for line in open(src, encoding='utf8'):
        line = line.rstrip('\n')
        if not line.strip(): continue
        if line.startswith('#'):
            cid, name = line[1:].split('|'); out.append(f"XC('ko', {json.dumps(cid)}, {json.dumps(name, ensure_ascii=False)}, {json.dumps(rom(name), ensure_ascii=False)});")
        elif line.startswith('@'):
            if not first: out.append(']);')
            first = False
            sid, name, foe, av, ln, lnzh = line[1:].split('|'); cur = sid; seen[sid] = []
            a = [sid, name, rom(name), foe, av, ln, rom(ln), lnzh]
            out.append("XS('ko', " + ', '.join(json.dumps(x, ensure_ascii=False) for x in a) + ', [')
        else:
            p = line.split('|'); k, w, ex = p[:3]; zh = p[3] if len(p) > 3 else ''
            assert k in keys[cur], (cur, k); seen[cur].append(k)
            out.append('  ' + json.dumps([k, w, rom(w), ex, rom(ex), zh], ensure_ascii=False) + ',')
    out.append(']);')
    for sid, ks in seen.items():
        miss = set(keys[sid]) - set(ks)
        if miss: print('MISSING', sid, miss)
    missing_sc = set(keys) - set(seen)
    if missing_sc: print('MISSING SCENES', missing_sc)
    open(dst, 'w', encoding='utf8').write('// 韩语词库（自动生成，源文件 ko/*.txt）\n' + '\n'.join(out) + '\n')
    print('wrote', dst, sum(len(v) for v in seen.values()))
W = '/mnt/user-data/outputs/word-cards'
os.makedirs(W + '/data/ko', exist_ok=True)
CH = [('people','01-people'),('appearance','02-appearance'),('health','03-health'),('home','04-home'),('city','05-city'),('food','06-food'),('study','07-study'),('work','08-work'),('transport','09-transport'),('sports','10-sports'),('leisure','11-leisure'),('environment','12-environment'),('nature','13-nature'),('reference','14-reference')]
only = sys.argv[1:]
for a, b in CH:
    if only and a not in only: continue
    if not os.path.exists(f'{D}/{a}.txt'): continue
    build(f'{D}/{a}.txt', f'{W}/data/ko/{b}.js', f'{W}/data/{b}.js')
