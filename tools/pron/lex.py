"""英语发音词典：CMU → KK 音标；拼写分音节并标重音。"""
import re, cmudict
from wordfreq import zipf_frequency
ZF = lambda w: zipf_frequency(w, 'en')
CMU = cmudict.dict()
EXTRA = {}   # 手工补充：词 -> ARPAbet 字符串
for l in [x for f in ('extra_cmu.txt',) for x in open(__file__.replace('lex.py', f), encoding='utf-8')]:
    l = l.strip()
    if l and not l.startswith('#'):
        w, p = l.split(None, 1); EXTRA[w.lower()] = p.split()

V = {'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'}
KKV = {'AA': 'ɑ', 'AE': 'æ', 'AO': 'ɔ', 'AW': 'aʊ', 'AY': 'aɪ', 'EH': 'ɛ', 'EY': 'e', 'IH': 'ɪ', 'IY': 'i', 'OW': 'o', 'OY': 'ɔɪ', 'UH': 'ʊ', 'UW': 'u'}
KKC = {'B': 'b', 'CH': 'tʃ', 'D': 'd', 'DH': 'ð', 'F': 'f', 'G': 'g', 'HH': 'h', 'JH': 'dʒ', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'NG': 'ŋ',
       'P': 'p', 'R': 'r', 'S': 's', 'SH': 'ʃ', 'T': 't', 'TH': 'θ', 'V': 'v', 'W': 'w', 'Y': 'j', 'Z': 'z', 'ZH': 'ʒ'}
ONSETS = {tuple(x.split()) for x in '''P;B;T;D;K;G;F;V;TH;DH;S;Z;SH;ZH;HH;CH;JH;M;N;L;R;W;Y;P R;B R;T R;D R;K R;G R;F R;TH R;SH R;P L;B L;K L;G L;F L;S L;
T W;D W;K W;G W;S W;TH W;S P;S T;S K;S M;S N;S P R;S T R;S K R;S P L;S K W;P Y;B Y;K Y;F Y;M Y;HH Y;V Y;S K Y;HH W'''.replace('\n', '').split(';') if x.strip()}

def fixph(ph):
    out = []
    for i, p in enumerate(ph):
        nxt = ph[i + 1] if i + 1 < len(ph) else ''
        if p == 'ER0' and nxt[:2] in V: out += ['AH0', 'R']; continue
        out.append(p)
    vi = [i for i, p in enumerate(out) if p[:2] in V]
    if vi and out[vi[-1]] == 'AA0': out[vi[-1]] = 'AH0'
    return out

def pron(w):
    w = w.lower()
    if w in EXTRA: return EXTRA[w]
    if w in CMU: return fixph(CMU[w][0])
    return None

def syl_phones(ph):
    """把音素切成音节（最大首音原则），返回 [(音素列表, 重音)]"""
    idx = [i for i, p in enumerate(ph) if p[:2] in V]
    if not idx: return [(ph, None)]
    bounds = [0]
    for a, b in zip(idx, idx[1:]):
        cons = [p for p in ph[a + 1:b]]
        k = len(cons)
        while k > 0 and tuple(cons[len(cons) - k:]) not in ONSETS: k -= 1
        bounds.append(b - k)
    out = []
    for i, st in enumerate(bounds):
        en = bounds[i + 1] if i + 1 < len(bounds) else len(ph)
        seg = ph[st:en]
        s = next(p[-1] for p in seg if p[:2] in V)
        out.append((seg, s))
    return out

def kk_syl(seg, stress):
    r = ''
    for j, p in enumerate(seg):
        b = re.sub(r'\d', '', p)
        if b == 'ER': r += 'ɝ' if stress == '1' else 'ɚ'
        elif b == 'AH': r += 'ʌ' if stress in '12' else 'ə'
        elif b == 'IY' and j + 1 < len(seg) and seg[j + 1] == 'R': r += 'ɪ'
        elif b == 'UW' and j + 1 < len(seg) and seg[j + 1] == 'R': r += 'ʊ'
        elif b in KKV: r += KKV[b]
        else: r += KKC[b]
    return r

def kk(ph, cut=None):
    ss = syl_phones(ph) if not cut else syl_phones(ph[:cut]) + syl_phones(ph[cut:])
    one = sum(1 for _, s in ss if s is not None) <= 1
    r = ''
    for seg, s in ss:
        mark = '' if one else ('ˈ' if s == '1' else 'ˌ' if s == '2' else '')
        r += mark + kk_syl(seg, s)
    return r

# ---------- 拼写分音节 ----------
VOW = set('aeiouy')
DIG = ['tch', 'ch', 'sh', 'th', 'ph', 'wh', 'ck', 'gh', 'qu']
SPLITS = ['io', 'ia', 'iu', 'eo', 'ua', 'uo', 'oa', 'ie', 'ea', 'ue', 'oe', 'ye', 'ya', 'yi', 'eu', 'ei', 'ai', 'ui', 'oi', 'ee', 'oo', 'ao']

def groups(w):
    g = []; i = 0
    while i < len(w):
        ch = w[i]
        isv = ch in VOW and not (ch == 'y' and (i == 0 or (i + 1 < len(w) and w[i + 1] in 'aeiou' and i > 0 and w[i - 1] not in VOW)))
        if ch == 'u' and i > 0 and w[i - 1] == 'q': isv = False
        if isv:
            j = i
            while j + 1 < len(w) and w[j + 1] in VOW and not (w[j + 1] == 'y' and j + 2 < len(w) and w[j + 2] in 'aeiou'): j += 1
            g.append([i, j + 1])
            i = j + 1
        else: i += 1
    return g

def fit(w, g, n):
    g = [x[:] for x in g]
    # 多了：去掉不发音的 e
    def silent_e_candidates():
        c = []
        for k, (a, b) in enumerate(g):
            t = w[a:b]
            if t != 'e': continue
            if b == len(w) and k > 0 and not (a >= 2 and w[a - 1] == 'l' and w[a - 2] not in VOW): c.append((0, k))
            elif b == len(w) - 1 and w[b] in 'sd' and k > 0: c.append((1, k))
            elif k > 0 and b < len(w):
                vce = a >= 2 and w[a - 2] in VOW and w[a - 1] not in VOW
                c.append((2, k) if vce else (3, -k))
        return [(p, abs(k)) for p, k in sorted(c)]
    silent = []
    if len(g) > 1 and w[g[-1][0]:] == 'e' and fit.endcons and not (len(w) > 2 and w[-2] == 'l' and w[-3] not in VOW):
        silent.append(g[-1][0]); g.pop()
    elif len(g) > 1 and w[g[-1][0]:] == 'ue' and w[g[-1][0] - 1] in 'gq':
        silent.append(g[-1][0]); g.pop()
    while len(g) > n:
        c = silent_e_candidates()
        if not c: break
        silent.append(g[c[0][1]][0]); g.pop(c[0][1])
    fit.silent = silent
    tries = 0
    while len(g) < n and tries < 10:
        tries += 1; done = False
        for pat in SPLITS:
            for k, (a, b) in enumerate(g):
                t = w[a:b]
                p = t.find(pat)
                if p >= 0 and not (pat == 'io' and w[a + p + 2:a + p + 3] == 'n' and a + p > 0 and w[a + p - 1] in 'tsc'):
                    if pat in ('ia', 'io', 'ie') and w[a + p - 1:a + p] in ('c', 't', 's') and w[a + p + 2:a + p + 3] in ('n', 'l', 's') and k == len(g) - 1: continue
                    m = a + p + 1
                    g[k:k + 1] = [[a, m], [m, b]]; done = True; break
            if done: break
        if not done:
            # -le / -ism 等：找"辅音+l+e"或在辅音后加音节
            m = re.search(r'[^aeiouy](l|m|n)(e?s?)$', w)
            if m and (not g or g[-1][1] <= m.start(1)):
                g.append([m.start(1), m.start(1)]); continue
            break
    return g if len(g) >= n else None

def unitize(s):
    """把辅音串切成单位（双字母组合不拆）"""
    u = []; i = 0
    while i < len(s):
        for d in DIG:
            if s.startswith(d, i): u.append(d); i += len(d); break
        else: u.append(s[i]); i += 1
    return u

LEGAL = {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tr', 'thr', 'shr', 'sc', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tw', 'str', 'spr', 'scr', 'spl', 'qu', 'squ', 'wh', 'chr', 'sch'}
SHORT = {'AE', 'EH', 'IH', 'AA', 'AH', 'UH'}

def ortho(w, ph):
    """返回 [(拼写片段, 重音)]，失败返回 None"""
    ph = list(ph)
    for i in range(len(ph) - 1):   # fire / hour 写出来是一个音节
        if ph[i][:2] in ('AY', 'AW') and ph[i + 1] == 'ER0' and re.search(r'(ire|yre|our)', w): ph[i + 1] = 'R'
    vs = [p for p in ph if p[:2] in V]
    n = len(vs)
    if n <= 1: return [(w, vs[0][-1] if vs else '1')]
    fit.endcons = ph[-1][:2] not in V
    g = fit(w, groups(w), n)
    if not g: return None
    silent = fit.silent
    if len(g) > n:   # 拼写比读音多出的音节（如 choc-o-late）：算作不重读
        vs = [v[-1] for v in vs]; p1 = vs.index('1') if '1' in vs else 0
        for _ in range(len(g) - n): vs.insert(p1 + 1, '0')
        vs = ['X' + v for v in vs]; n = len(g)
    cuts = []
    for k in range(n - 1):
        a, b = g[k][1], g[k + 1][0]
        cons = w[a:b]
        if k == 0:
            pm = re.match(r'(dis|mis|trans|un)(?=[^aeiouy])', w)
            if pm and pm.end() > a and pm.end() <= b:
                cuts.append(pm.end()); continue
        se = [p for p in silent if a <= p < b]
        if se:
            cuts.append(se[-1] + 1); continue
        units = unitize(cons)
        if len(units) >= 1 and re.match(r'i(on|an|ou|al|a\b|ent|en)', w[b:]) and units[-1] in ('t', 's', 'c', 'ss', 'x', 'g', 'ci'):
            cuts.append(b - len(units[-1])); continue
        if cons in ('w', 'r') and (cons == 'w' or vs[k][:2] == 'ER' or (k + 1 < len(vs) and vs[k][:2] in V and False)):
            if cons == 'w' or w[a - 1:a] in 'e':
                cuts.append(b); continue
        stressed_short = vs[k][-1] == '1' and vs[k][:2] in SHORT and g[k][1] - g[k][0] == 1
        if len(units) == 0: cut = a
        elif len(units) == 1:
            cut = b if stressed_short and not (k + 1 == n - 1 and w[g[k + 1][0]:] in ('e',)) else a
            if units[0] in ('ck', 'ng', 'x'): cut = b
        else:
            # 末尾能作首音的最长串留给下一音节，但至少留一个辅音给前面
            best = len(units) - 1
            nxt_le = w[g[k + 1][0]:g[k + 1][1]] == 'e' and g[k + 1][1] == len(w) and units[-1] == 'l'
            for j in range(0 if not stressed_short else 1, len(units)):
                if nxt_le: best = len(units) - 2; break
                if ''.join(units[j:]) in LEGAL or len(units) - j == 1: best = j; break
            if len(units) == 2 and units[0] == units[1]: best = 1
            cut = a + len(''.join(units[:best]))
        cuts.append(cut)
    out = []; st = 0
    for k, c in enumerate(cuts + [len(w)]):
        out.append((w[st:c], vs[k][-1])); st = c
    if any(not x for x, _ in out): return None
    return out

SUFF = ['ing', 'ers', 'er', 'ed', 'ly', 'ful', 'ness', 'ment', 'less', 'y', 'es', 's', 'ist', 'ish']
def nvow(ph): return sum(1 for p in ph if p[:2] in V)

def norm1(ph):
    """多个主重音只留第一个，其余改成次重音"""
    seen = False; out = []
    for p in ph:
        if p.endswith('1'):
            if seen: p = p[:-1] + '2'
            seen = True
        out.append(p)
    return out

SUFPH = {'ing': [['IH', 'NG']], 'er': [['ER']], 'ers': [['ER', 'Z']], 'ed': [['D'], ['T'], ['IH', 'D'], ['AH', 'D']], 'ly': [['L', 'IY']],
         'ful': [['F', 'AH', 'L']], 'ness': [['N', 'AH', 'S'], ['N', 'IH', 'S']], 'ment': [['M', 'AH', 'N', 'T']], 'less': [['L', 'AH', 'S']],
         'y': [['IY']], 'es': [['IH', 'Z'], ['AH', 'Z'], ['Z']], 's': [['S'], ['Z']], 'ist': [['IH', 'S', 'T'], ['AH', 'S', 'T']], 'ish': [['IH', 'SH']]}
def bare(ph): return [re.sub(r'\d', '', p) for p in ph]

def split_parts(w, ph):
    """复合词 / 词根+后缀：按部件分音节，重音用整词的（读音必须能拼起来）"""
    n = nvow(ph); bw = bare(ph)
    best = None
    for i in range(3, len(w)):
        A, B = w[:i], w[i:]
        cands = []
        if A in CMU: cands.append(A)
        if B in SUFF and A + 'e' in CMU: cands.append(A + 'e')
        for Aw in cands:
            pa = pron(Aw); ba = bare(pa)
            if B in SUFF:
                if not any(ba + sp == bw for sp in SUFPH[B]): continue
                if ZF(Aw) < 3.8 and len(Aw) < 5: continue
                pb_n = n - nvow(pa)
                oa = ortho(Aw, pa)
                if not oa: continue
                if Aw != A: oa = oa[:-1] + [(oa[-1][0][:-1] if oa[-1][0].endswith('e') else oa[-1][0], oa[-1][1])]
                if pb_n == 0: parts = oa[:-1] + [(oa[-1][0] + B, oa[-1][1])]
                else: parts = oa + [(B, '0')]
            else:
                pb = pron(B)
                cons = lambda x: [p for p in bare(x) if p not in V]
                if not pb or len(B) < 3 or cons(pa) + cons(pb) != cons(ph) or nvow(pa) + nvow(pb) != n: continue
                st = [p[-1] for p in ph if p[:2] in V]; na = nvow(pa)
                if all(x == '0' for x in st[:na]) or all(x == '0' for x in st[na:]): continue   # 两半都要有重音才算复合词
                if ZF(A) < 4.0 or ZF(B) < 4.0: continue
                oa, ob = ortho(A, pa), ortho(B, pb)
                if not oa or not ob: continue
                parts = oa + ob
            if ''.join(t for t, _ in parts) != w: continue
            # 词根末尾是双写辅音（shop-ping）：拆在两个辅音中间
            if len(parts) >= 2 and len(parts[-2][0]) >= 2 and parts[-2][0][-1] == parts[-2][0][-2] and parts[-2][0][-1] not in 'aeiousl' and B in SUFF:
                parts[-2:] = [(parts[-2][0][:-1], parts[-2][1]), (parts[-2][0][-1] + parts[-1][0], parts[-1][1])]
            vs = [p[-1] for p in ph if p[:2] in V]
            if len(vs) != len(parts): continue
            parts = [(t, vs[k]) for k, (t, _) in enumerate(parts)]
            if B in ('er', 'y', 'ers') and re.search(r'(^|[^aeiouy])[aeiou](nt|nd|st|mp|nk|ft|pt|ct)$', A):
                continue   # cen-ter、hun-ter：交给普通规则
            cut = None if B in SUFF else len(pron(A))
            if best is None or len(A) > len(best[0]): best = (A, parts, cut)
    split_parts.cut = best[2] if best else None
    return best[1] if best else None

SYLO = {}
for _l in open(__file__.replace('lex.py', 'syl_ovr.txt'), encoding='utf-8'):
    _l = _l.strip()
    if _l and not _l.startswith('#'):
        _w, _s = _l.split(None, 1); SYLO[_w.lower()] = _s

def word_info(w):
    """单个词：(KK, 拼写音节[(片段,重音)]) 或 None"""
    lw = w.lower()
    if w == 'IT': return 'ˌaɪˈti', [('I', '2'), ('T', '1')], ['AY2', 'T', 'IY1']
    if lw in SYLO:
        ph = pron(lw)
        if not ph: return None
        o = []
        for part in SYLO[lw].split('·'):
            s = '1' if part.startswith('ˈ') else '2' if part.startswith('ˌ') else '0'
            o.append((part.lstrip('ˈˌ'), s))
        k = 0; o2 = []
        for t, s in o: o2.append((w[k:k + len(t)], s)); k += len(t)
        return kk(norm1(ph)), o2, ph
    ph = pron(lw)
    if not ph: return None
    if re.fullmatch(r'[A-Z0-9]{2,}', w):   # 字母缩写：每个字母一个音节，重音在最后
        vi = [i for i, p in enumerate(ph) if p[:2] in V]
        ph = [p[:-1] + ('1' if i == vi[-1] else '2') if i in vi else p for i, p in enumerate(ph)]
        if len(vi) == len(w): return kk(ph), [(c, ph[vi[j]][-1]) for j, c in enumerate(w)], ph
    ph = norm1(ph)
    o = split_parts(lw, ph) if len(lw) >= 5 else None
    cut = split_parts.cut if o else None
    if cut:   # 复合词后半部分至少有个次重音（tooth-ˌbrush）
        tail = [i for i in range(cut, len(ph)) if ph[i][:2] in V]
        if tail and all(ph[i][-1] == '0' for i in tail):
            pb = pron(w[len(w) - len(''.join(t for t, _ in o[len(o) - len(tail):])):].lower()) or []
            pv = [p[-1] for p in pb if p[:2] in V]
            j = pv.index('1') if '1' in pv else 0
            if j < len(tail):
                ph = list(ph); ph[tail[j]] = ph[tail[j]][:-1] + '2'
                k0 = len(o) - len(tail); o = list(o); o[k0 + j] = (o[k0 + j][0], '2')
    if not o: o = ortho(lw, ph)
    if o and w != lw:   # 保留原来的大小写
        k = 0; o2 = []
        for t, s in o: o2.append((w[k:k + len(t)], s)); k += len(t)
        o = o2
    return kk(ph, cut), o, ph
