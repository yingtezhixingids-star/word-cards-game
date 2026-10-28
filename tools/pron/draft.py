import json, inton, collections
d = json.load(open('all.json'))
order = [s for c, ss in d['order'] for s in ss]
by = collections.OrderedDict((s, []) for s in order)
seen = set()
for w in d['words']:
    if w['ex'] not in seen: seen.add(w['ex']); by[w['sc']].append(w['ex'])
for s, v in d['story'].items():
    for x in v:
        if x not in seen: seen.add(x); by[s].append(x)
OV = {}
for l in open('sent_ovr.txt', encoding='utf-8'):
    if '||' in l and not l.startswith('#'):
        a, b = [x.strip() for x in l.split('||')]; OV[a] = b
for l in open('visitdoctor.txt', encoding='utf-8'):
    if '||' in l and not l.startswith('#'):
        a, b = [x.strip() for x in l.split('||')]; OV[a] = b
out = {}; bad = 0
for s, v in by.items():
    for x in v:
        a = OV.get(x) or inton.annotate(x)
        if inton.plain(a) != x: bad += 1; print('MISMATCH', x, '|', a)
        out[x] = (s, a)
json.dump(out, open('drafts.json', 'w'), ensure_ascii=False)
print(len(out), bad)
