import re, glob, json
out = {}
for f in sorted(glob.glob('*.txt')):
    sid = None
    for l in open(f):
        l = l.rstrip('\n')
        if not l.strip(): continue
        if l.startswith('@'): sid = l[1:].strip(); out[sid] = []; continue
        en, zh = l.split('|', 1)
        m = re.search(r'\{([^}]+)\}', en)
        if not m:
            out[sid].append([en.strip(), zh.strip()]); continue
        k, _, surf = m.group(1).partition('=')
        surf = surf or k
        a, b = en[:m.start()], en[m.end():]
        plain = lambda s: re.sub(r'\{([^}=]+)(?:=([^}]+))?\}', lambda x: x.group(2) or x.group(1), s)
        out[sid].append([plain(a), surf, plain(b).rstrip(), zh.strip(), k])
js = '// 英语「听力填空」连贯短文：每个场景一段，[句子] 或 [前半, 空里的词, 后半, 中文, 卡片词]\n// 由 tools/stories/*.txt 生成（gen.py），别手改\nconst STORY_EN = ' + json.dumps(out, ensure_ascii=False, separators=(',', ':')).replace('],[', '],\n[').replace('":[[', '":[\n[') + ';\n'
open('/mnt/user-data/outputs/word-cards/data/stories-en.js', 'w').write(js)
print(len(out), sum(len(v) for v in out.values()), len(js))
