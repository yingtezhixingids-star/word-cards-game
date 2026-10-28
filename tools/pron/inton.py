"""句子语调标注草稿：[重读音节] (弱读) ‿连读 | 停顿 ↘降调 ↗升调（箭头标在意群最重的词前）"""
import re, json, lex

WEAK = set('''a an the to of in on at for and or but as from by with than some is are am was were be been being has have had do does did can could will would shall should must
my your his her its our their me him us them you he she it we they i'm you're it's that's there's i'll we're they're he's she's let's
i've you've we've i'd you'll she'll he'll we'll they'll'''.split())
PLAIN = {'i', 'mr.', 'mrs.', 'ms.', 'dr.'}
WH = set('what where when who why how which whose'.split())
AUX = set('''is are am was were do does did can could will would shall should have has had may might must isn't aren't don't doesn't didn't can't won't
haven't hasn't wasn't weren't'''.split())
NEG = set("don't can't won't isn't aren't doesn't didn't haven't hasn't wasn't weren't shouldn't couldn't wouldn't mustn't not never no".split())
PART = set('up down off out away back on over around in'.split())
DEMO = set('this that these those there'.split())
REPORT = set('said says asked asks shouted shouts added adds replied replies answered whispered told'.split())
CONJ = set('and but because so when if after before while until or'.split())
POLITE = set('please thanks'.split())
VERBP = set('turn get go put pick look take fill call calm come cool find give hold hurry run sit stand slow speed tidy try wake warm check set make do wash water walk watch mow read ride save sort brush comb catch change fly have help see wait hang'.split())
SUBJ_AFTER_QUOTE = set('he she they i we the my his her mr. mrs. ms. dr. grandma grandpa'.split())

# 卡片短语（复合词）：主重音词以外的实词不重读
PHR = json.load(open(__file__.replace('inton.py', 'phr_main.json')))
def load_phrases(main_idx):
    for en, j in main_idx.items(): PHR[en.lower()] = j

def wtoks(s):
    """把句子切成 [(类型, 文字)]：w=词 p=标点 s=空格"""
    return [(('w' if re.match(r"[A-Za-z0-9é]", m) else 's' if m.isspace() else 'p'), m)
            for m in re.findall(r"[A-Za-z0-9é][A-Za-z0-9é'’.\-]*[A-Za-z0-9é]|[A-Za-z0-9é]|\s+|[^\sA-Za-z0-9é]", s)]

def fix_abbrev(toks):
    # "Mr." "Dr." 里的点保留在词上；其他词末的点分出来
    out = []
    for t, x in toks:
        if t == 'w' and x.endswith('.') and x.lower() not in ('mr.', 'mrs.', 'ms.', 'dr.', 't.'):
            out.append(('w', x[:-1])); out.append(('p', '.'))
        elif t == 'p' and x == '.' and out and out[-1][0] == 'w' and out[-1][1].lower() in ('mr', 'mrs', 'ms', 'dr', 'st', 't'):
            out[-1] = ('w', out[-1][1] + '.')
        else: out.append((t, x))
    return out

def info(word):
    w = word.replace('’', "'")
    lw = w.lower().rstrip('.')
    parts = re.split(r'(-)', w)
    if len(parts) > 1:   # 连字符词：按第一个实词部分算重音
        return None
    r = lex.word_info(w.rstrip('.'))
    if not r and lw.endswith("'s"): r = lex.word_info(w[:-2])
    return r

def stressed_span(word):
    """返回 (前, 重读音节, 后)"""
    r = info(word)
    if '-' in word:
        ps = word.split('-')
        # 复合：重音在第一个部分（check-up、T-shirt），形容词复合在最后（low-fat 由短语表决定，这里简化）
        first = ps[0]; rest = word[len(first):]
        a, b, c = stressed_span(first)
        return a, b, c + rest
    if not r or not r[1]: return '', word, ''
    o = r[1]
    if len(o) == 1:
        return '', word, ''
    k = 0; pos = 0
    for i, (t, s) in enumerate(o):
        if s[-1] == '1': k = i; break
    pre = ''.join(t for t, _ in o[:k]); mid = o[k][0]; post = word[len(pre) + len(mid):]
    return word[:len(pre)], word[len(pre):len(pre) + len(mid)], post

def phones(word):
    r = info(word.split('-')[-1]) if '-' in word else info(word)
    return r[2] if r else None

def annotate(sent):
    toks = fix_abbrev(wtoks(sent))
    words = [i for i, (t, x) in enumerate(toks) if t == 'w']
    lw = {i: toks[i][1].lower().replace('’', "'") for i in words}
    # —— 意群：按标点切 ——
    units = []; cur = []; punct_after = {}
    for i, (t, x) in enumerate(toks):
        if t == 'w': cur.append(i)
        elif t == 'p' and x in ',.?!;:' or (t == 'p' and x in '"“”' and cur):
            if cur: units.append(cur); punct_after[len(units) - 1] = x; cur = []
            elif units and x in '.?!': punct_after[len(units) - 1] = x
    if cur: units.append(cur); punct_after[len(units) - 1] = ''
    # 句末标点：每个意群往后找第一个 .?! 用来判断问句
    def end_mark(ui):
        last = units[ui][-1]
        for t, x in toks[last + 1:]:
            if t == 'p' and x in '.?!': return x
            if t == 'w': break
        return None
    # 长意群里在连词前停顿
    new_units = []
    for u in units:
        if len(u) >= 8:
            cut = None
            for k in range(3, len(u) - 2):
                if lw[u[k]] in CONJ: cut = k; break
            if cut: new_units += [u[:cut], u[cut:]]; continue
        new_units.append(u)
    split_from = {id(u) for u in new_units}
    units2 = new_units
    # —— 每个词的类别 ——
    cls = {}
    sent_words = [lw[i] for i in words]
    for ui, u in enumerate(units2):
        for k, i in enumerate(u):
            w = lw[i]; last = k == len(u) - 1
            if w in NEG or w in WH: c = 'S'
            elif w in PLAIN: c = 'P'
            elif w in DEMO: c = 'S' if last or (w != 'there' and k + 1 < len(u) and lw[u[k + 1]] in ('is', 'was', 'are', 'were')) else 'W'
            elif w in PART and last and k > 0 and lw[u[k - 1]] not in WEAK | {'the'}: c = 'S'
            elif w in PART and last and k > 1: c = 'S'
            elif w == 'let' and k + 1 < len(u) and lw[u[k + 1]] in ('me', 'us'): c = 'W'
            elif w in ('have', 'has', 'had') and k > 0 and lw[u[k - 1]] in ('have', 'has', 'had', 'do', 'does', 'did', 'will', 'to', 'you', 'we', 'they') and k + 1 < len(u) and lw[u[k + 1]] in ('a', 'an', 'the', 'some', 'any', 'your', 'my', 'lunch', 'breakfast', 'dinner', 'fun'): c = 'S'
            elif w in WEAK: c = 'W'
            elif w in REPORT: c = 'W'
            else: c = 'S'
            cls[i] = c
        if u and not any(cls[i] == 'S' for i in u) and not all(lw[i] in REPORT | {'he', 'she', 'they', 'i', 'we', 'you'} for i in u if True) or (u and len(u) <= 2 and not any(cls[i] == 'S' for i in u) and lw[u[0]] in ('and', 'but', 'or')):
            cls[u[-1]] = 'S'   # 整个意群都是虚词（And you?）：最后一个词重读
    # 复合词短语：非主重音的实词降为普通
    low = ' '.join(sent_words)
    phr_main = set(); phr_tail = set()
    for en, j in sorted(PHR.items(), key=lambda x: -len(x[0])):
        ew = en.split()
        if len(ew) < 2: continue
        for s in range(len(words) - len(ew) + 1):
            seg = [lw[words[s + q]].rstrip('.') for q in range(len(ew))]
            if [x.rstrip('s') for x in seg] == [x.rstrip('s') for x in ew] or seg == ew:
                for q in range(len(ew)):
                    idx = words[s + q]
                    if idx in phr_main or idx in phr_tail: continue
                    if q == j:
                        phr_main.add(idx)
                        if j > 0: cls[idx] = 'S'   # 动词短语的小品词、固定说法的重音词：put ON、how ARE you
                    elif j == 0 and cls.get(idx) == 'S': cls[idx] = 'P'; phr_tail.add(idx)   # 名词复合词：后半不重读
    # —— 主重音（核心）和语调 ——
    tone = {}
    first_word = lw[words[0]] if words else ''
    for ui, u in enumerate(units2):
        st = [i for i in u if cls[i] == 'S']
        # 引号后的转述部分（the doctor asked）：不标箭头
        prev_tok = None
        for t, x in reversed(toks[:u[0]]):
            if t != 's': prev_tok = x; break
        if prev_tok in ('"', '”') and ui > 0 and any(lw[i] in REPORT for i in u): continue
        if all(lw[i] in POLITE for i in u): continue
        if not st: continue
        nuc = st[-1]
        # 这个意群后面紧跟的标点
        after = None
        for t, x in toks[u[-1] + 1:]:
            if t == 'p': after = x; break
            if t == 'w': break
        if after in ('.', '!'): tn = '↘'
        elif after == '?':
            # 找这个问句的第一个词
            qs = u[0]
            for t, x in reversed(toks[:u[0]]):
                if t == 'p' and x in '.?!"“': break
            first = lw[u[0]]
            j = units2.index(u) if first not in AUX and first not in WH and first != 'and' else 0
            while j > 0:
                pu = units2[j - 1]
                gap = [x for t, x in toks[pu[-1] + 1:u[0]] if t == 'p']
                if any(g in '.?!"“”' for g in gap): break
                j -= 1; u0 = pu; first = lw[pu[0]]
            tn = '↗' if first in AUX else '↘'
        elif after in ('"', '”'):
            # 引号里的话没有句末标点（少见），按陈述
            tn = '↘'
        else: tn = '↗'
        tone[nuc] = tn
    # —— 输出 ——
    out = []
    for n, (t, x) in enumerate(toks):
        if t != 'w': out.append(x); continue
        c = cls[n]
        if c == 'W': s = '(' + x + ')'
        elif c == 'P': s = x
        else:
            a, b, cc = stressed_span(x)
            s = a + tone.get(n, '') + '[' + b + ']' + cc
        out.append(s)
    # 连读：同一意群里，辅音结尾 + 元音开头
    unit_of = {i: ui for ui, u in enumerate(units2) for i in u}
    res = ''
    for n, (t, x) in enumerate(toks):
        piece = out[n]
        if t == 's':
            a = n - 1; b = n + 1
            if a >= 0 and b < len(toks) and toks[a][0] == 'w' and toks[b][0] == 'w' and unit_of.get(a) == unit_of.get(b):
                pa, pb = phones(toks[a][1]), phones(toks[b][1])
                if pa and pb and pa[-1][:2] not in lex.V and pb[0][:2] in lex.V and toks[b][1].lower() not in ('i',) and lw[b] not in ('one', 'once'):
                    piece = '‿'
            # 意群边界停顿
            if a >= 0 and b < len(toks) and unit_of.get(b) is not None and unit_of.get(a, unit_of.get(b)) != unit_of.get(b):
                piece = ' | '
            elif a >= 0 and toks[a][0] == 'p' and toks[a][1] in ',;:' and b < len(toks):
                piece = ' | '
            elif a >= 0 and toks[a][0] == 'p' and toks[a][1] in '"”' and b < len(toks) and toks[b][0] == 'w' and units2 and any(n2 > a for n2 in unit_of):
                if unit_of.get(b) is not None and lw.get(b, '') and (lw[b] in SUBJ_AFTER_QUOTE or lw[b] in REPORT):
                    piece = ' | '
        res += piece
    res = re.sub(r'\s+\|\s+', ' | ', res)
    return res

def plain(a):
    return re.sub(r'\s+', ' ', re.sub(r'[\[\]()↗↘]|\s\|', '', a.replace('‿', ' ')))
