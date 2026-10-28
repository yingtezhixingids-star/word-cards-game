import re, glob, sys
D = '/mnt/user-data/outputs/word-cards/data/'
keys = {}
for f in glob.glob(D + '[0-9]*.js'):
    s = open(f).read()
    for m in re.finditer(r"S\('(\w+)',.*?`(.*?)`\);", s, re.S):
        keys[m.group(1)] = [l.split('|')[0].strip() for l in m.group(2).strip().split('\n') if l.strip()]
bad = 0; total = 0; seen = set()
for f in sorted(glob.glob('*.txt')):
    sid = None; qs = []
    def done():
        global bad
        if sid and len(qs) < 5: print(f, sid, 'only', len(qs), 'questions'); bad += 1
        if sid and len(set(k.lower() for k in qs)) != len(qs): print(f, sid, 'dup keys', qs); bad += 1
    for l in open(f):
        l = l.rstrip('\n')
        if not l.strip(): continue
        if l.startswith('@'):
            done(); sid = l[1:].strip(); qs = []; seen.add(sid)
            if sid not in keys: print(f, 'unknown scene', sid); bad += 1
            continue
        if '|' not in l: print(f, sid, 'no zh:', l); bad += 1; continue
        en, zh = l.split('|', 1)
        bs = re.findall(r'\{([^}]+)\}', en)
        if bs:
            k = bs[0].split('=')[0]
            if k.lower() not in [x.lower() for x in keys.get(sid, [])]: print(f, sid, 'bad key', k); bad += 1
            qs.append(k)
            for b in bs[1:]:
                k2 = b.split('=')[0]
                if k2.lower() not in [x.lower() for x in keys.get(sid, [])]: print(f, sid, 'bad key2', k2); bad += 1
    done(); total += 1
print('scenes done', len(seen), 'of', len(keys), 'problems', bad)
if len(sys.argv) > 1: print(sorted(set(keys) - seen))
