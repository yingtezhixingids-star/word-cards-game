import re, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rom import rom
FIX = {}
if os.path.exists(os.path.join(os.path.dirname(__file__), 'fix.txt')):
    for l in open(os.path.join(os.path.dirname(__file__), 'fix.txt'), encoding='utf8'):
        l = l.rstrip('\n')
        if '=' in l and not l.startswith('#'):
            a, b = l.split('=', 1); FIX[a.strip()] = b.strip()
import rom2
def _vocab():
    v=set()
    for f in ('health.txt','food.txt'):
        for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)),f),encoding='utf8'):
            p=l.strip().split('|')
            if len(p)>=3 and not l.startswith(('#','@')): v.add(p[1])
    return v
rom2.setup(FIX, _vocab())
def R(t): return rom2.rom(t)
def build(src, dst, base):
    en = open(base, encoding='utf8').read()
    keys = {}
    for m in re.finditer(r"S\('(\w+)',.*?`(.*?)`\);", en, re.S):
        keys[m.group(1)] = [l.split('|')[0].strip() for l in m.group(2).strip().split('\n') if l.strip()]
    out = []; cur = None; seen = {}
    for line in open(src, encoding='utf8'):
        line = line.rstrip('\n')
        if not line.strip(): continue
        if line.startswith('#'):
            cid, name = line[1:].split('|'); out.append(f"THC({json.dumps(cid)}, {json.dumps(name)}, {json.dumps(R(name))});")
        elif line.startswith('@'):
            sid, name, foe, av, ln, lnzh = line[1:].split('|'); cur = sid; seen[sid] = []
            out.append(f"THS({json.dumps(sid)}, {json.dumps(name)}, {json.dumps(R(name))}, {json.dumps(foe)}, {json.dumps(av)}, {json.dumps(ln)}, {json.dumps(R(ln))}, {json.dumps(lnzh)}, [")
        else:
            p = line.split('|'); k, th, ex = p[0], p[1], p[2]; zh = p[3] if len(p) > 3 else ''
            assert k in keys[cur], (cur, k)
            seen[cur].append(k)
            out.append('  ' + json.dumps([k, th, R(th), ex, R(ex), zh], ensure_ascii=False) + ',')
        if line.startswith('@') is False and False: pass
    # close scenes
    txt = []
    for l in out:
        if l.startswith('THS(') and txt and not txt[-1].startswith('THC('): txt.append(']);')
        txt.append(l)
    txt.append(']);')
    for sid, ks in seen.items():
        miss = set(keys[sid]) - set(ks)
        if miss: print('MISSING', sid, miss)
    open(dst, 'w', encoding='utf8').write('// 泰语词库（自动生成，源文件 th/*.txt）\n' + '\n'.join(txt) + '\n')
    print('wrote', dst, sum(len(v) for v in seen.values()))
W = '/mnt/user-data/outputs/word-cards'
os.makedirs(W + '/data/th', exist_ok=True)
D = os.path.dirname(os.path.abspath(__file__))
build(D + '/health.txt', W + '/data/th/03-health.js', W + '/data/03-health.js')
build(D + '/food.txt', W + '/data/th/06-food.js', W + '/data/06-food.js')
