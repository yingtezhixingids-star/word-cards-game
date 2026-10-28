"""生成卡片单词的 [重读音节, 音标]。短语的主重音位置见 phrase_stress()。"""
import re, json, lex
FUNC = set('a an the to of in on at for and or your my me you it is are be up out off down by with from this that'.split())
VERBS = set('turn get go put pick look take fill call calm come cool find give hold hurry run sit stand slow speed tidy try wake warm check set make do wash water walk watch mow read ride save sort brush comb catch change fly have help see wait let walk hang put'.split())
ADJ = set('''big black blue cold double electric fallen flat free fresh fried frozen full good grand great green grey hard high hot iced instant large light little long low main minced new nuclear
personal polar public red reusable roast scrambled shared short single smart smoked social soft solar sour special spare stained steamed stuffed sweet tropical white whole yellow boiled baked canned
classical colored cured checkered english chinese happy medium super united crescent connecting extra next opening wooden plastic rear-view one-way round-trip high-speed sabre-toothed non-slip
sun-dried three-pointer brown north south milky great silk formula ice world peking saudi monkey'''.split())
OVR = {}   # 短语 -> 标注（手工）
for l in open('phrases_ovr.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.strip() and not l.startswith('#'):
        k, v = l.split('=>'); OVR[k.strip()] = v.strip()

def fmt(o, mark1=True):
    if len(o) == 1:
        return ('ˈ' if mark1 else 'ˌ' if o[0][1][-1] in '12' else '') + o[0][0]
    if mark1 and not any(s[-1] in '12' for _, s in o): o = [(o[0][0], '1')] + list(o[1:])
    r = []
    for t, s in o:
        s = s[-1]
        r.append(('ˈ' if s == '1' and mark1 else 'ˌ' if s in '12' else '') + t)
    return '·'.join(r)

PARTS = set('up down off out in on away back over for after'.split())
def phrase_main(toks):
    lw = [t.lower() for t in toks]
    content = [i for i, t in enumerate(lw) if t not in FUNC]
    if not content: return len(toks) - 1
    if lw[0] in VERBS:
        if lw[-1] in PARTS and len(lw) == 2: return 1
        return content[-1] if len(content) > 1 else len(toks) - 1
    if lw[0] in ADJ: return content[-1]
    return content[0]   # 名词复合词：重音在前

HYPH = {  # 连字符词：主重音在哪一部分（默认第一部分）
    'full-time': 1, 'part-time': 1, 'duty-free': 1, 'sugar-free': 1, 'lactose-free': 1, 'self-service': 1, 'home-cooked': 1, 'non-alcoholic': 1,
    'short-sighted': 1, 'hard-working': 1, 'low-fat': 1, 'double-decker': 1, 'three-pointer': 1, 'non-slip': 1, 'one-way': 0, 'round-trip': 0,
    'rear-view': 0, 'sun-dried': 1, 'sabre-toothed': 1, 'high-speed': 1, 'daughter-in-law': 0, 'go-kart': 0}

def entry(en):
    parts = re.split(r'([ \-])', en)
    toks = [p for p in parts if p not in (' ', '-', '')]
    if len(toks) == 1:
        k, o, ph = lex.word_info(en)
        return fmt(o) if o else None, '/' + k + '/'
    sp = en.split(' ')
    if en in OVR: mainw = int(OVR[en])
    elif len(sp) == 1: mainw = 0
    else:
        mainw = phrase_main(sp)
    # 换算成部件序号
    main = 0; cnt = 0
    for wi, wd in enumerate(sp):
        hp = wd.split('-')
        if wi == mainw:
            main = cnt + (HYPH.get(wd.lower(), 0) if len(hp) > 1 else 0)
            if len(hp) > 1 and wd.lower() not in HYPH and len(sp) == 1:
                main = cnt + (len(hp) - 1 if hp[0].lower() in VERBS and hp[-1].lower() in ('up', 'off', 'out', 'in', 'on', 'down', 'through') and False else 0)
        cnt += len(hp)
    if len(sp) > 1 and mainw < len(sp) - 1 and '-' in sp[-1] and en not in OVR and sp[0].lower() not in VERBS:
        pass
    out, ipa = '', ''
    ti = 0; sep = ''
    for p in parts:
        if p in (' ', '-') or p == '':
            out += p; sep = ' ' if p == ' ' else ('' if p == '-' else sep); continue
        k, o, ph = lex.word_info(p)
        pi = parts.index(p)
        last_hyph = pi + 1 >= len(parts) or parts[pi + 1] != '-'
        hyph = sep == '' and ti > 0
        func = p.lower() in FUNC and p != 'IT' and not (hyph and last_hyph)
        if ti == main: s = fmt(o, True)
        elif func: s = fmt([(t, '0') for t, _ in o], False)
        else: s = fmt(o, False)
        # 音标：主重音词保留 ˈ，其他实词主重音改 ˌ，虚词去掉重音
        if ti == main: kk = k if 'ˈ' in k else 'ˈ' + k
        elif func: kk = k.replace('ˈ', '').replace('ˌ', '')
        else: kk = k.replace('ˈ', 'ˌ') if 'ˈ' in k else ('ˌ' + k if 'ˌ' not in k else k)
        out += s; ipa += (sep if ti > 0 else '') + kk; ti += 1; sep = ' '
    return out, '/' + ipa + '/'

if __name__ == '__main__':
    d = json.load(open('all.json'))
    seen = set(); res = []
    for w in d['words']:
        if w['en'] in seen: continue
        seen.add(w['en'])
        e = entry(w['en'])
        res.append(f"{w['en']} | {e[0]} | {e[1]}")
    open('card_words.txt', 'w').write('\n'.join(res))
    pm = {}
    for l in res:
        en, sy, _ = [x.strip() for x in l.split('|')]
        if ' ' in en and sy and sy != 'None':
            ws = sy.split(' ')
            for j, x in enumerate(ws):
                if 'ˈ' in x: pm[en.lower()] = j; break
    json.dump(pm, open('phr_main.json', 'w'), ensure_ascii=False)
    print(len(res))
