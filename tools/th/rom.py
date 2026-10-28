import re, unicodedata, tltk.nlp as n
INIT = [('kʰw','kw'),('kʰr','kr'),('kʰl','kl'),('pʰr','pr'),('pʰl','pl'),('tʰr','tr'),('kw','gw'),('kr','gr'),('kl','gl'),('pr','bpr'),('pl','bpl'),('tr','dtr'),
        ('pʰ','p'),('tʰ','t'),('kʰ','k'),('cʰ','ch'),('p','bp'),('t','dt'),('k','g'),('c','j'),('ʔ',''),('ŋ','ng'),('j','y'),
        ('b','b'),('d','d'),('m','m'),('n','n'),('f','f'),('s','s'),('h','h'),('r','r'),('l','l'),('w','w')]
VOW = [('iːa','ia'),('ia','ia'),('ɯːa','uea'),('ɯa','uea'),('uːa','ua'),('ua','ua'),
       ('aː','aa'),('iː','ii'),('ɯː','uue'),('uː','uu'),('eː','ee'),('ɛː','ae'),('oː','oo'),('ᴐː','aw'),('ɔː','aw'),('ɤː','oe'),
       ('a','a'),('i','i'),('ɯ','ue'),('u','u'),('e','e'),('ɛ','ae'),('o','o'),('ᴐ','aw'),('ɔ','aw'),('ɤ','oe')]
FIN = {'p':'p','t':'t','k':'k','m':'m','n':'n','ŋ':'ng','j':'i','w':'o','ʔ':'','':'','f':'f','s':'s','l':'n'}
TONE = {'1':'','2':'̀','3':'̂','4':'́','5':'̌'}
def syl(s):
    m = re.match(r'^(.*?)([1-5])$', s)
    if not m: return s
    body, tone = m.groups()
    ini = ''
    for a, b in INIT:
        if body.startswith(a) and len(body) > len(a): ini = b; body = body[len(a):]; break
    vow = None
    for a, b in VOW:
        if body.startswith(a): vow = b; body = body[len(a):]; break
    if vow is None: return ini + body
    fin = FIN.get(body, body)
    if fin == 'o' and vow.endswith('i'): fin = 'u'
    if fin == 'o' and vow in ('e', 'ee', 'ae'): fin = 'o'
    if fin == 'i' and vow in ('aw', 'oe', 'uea'): fin = 'y'
    # tone mark on first vowel letter
    v = vow[0] + TONE[tone] + vow[1:]
    return unicodedata.normalize('NFC', ini + v + fin)
FIXW = {}
def load_fix(d):
    for k, v in d.items(): FIXW[k] = v
def rom(th):
    keys = sorted(FIXW, key=len, reverse=True)
    if keys:
        for k in keys:
            if k in th:
                i = th.index(k)
                parts = [rom(th[:i]) if th[:i].strip() else '', FIXW[k], rom(th[i+len(k):]) if th[i+len(k):].strip() else '']
                lead = th[:i].endswith(' '); trail = th[i+len(k):].startswith(' ')
                r = parts[0] + (', ' if lead and parts[0] else (' ' if parts[0] else '')) + parts[1] + ((', ' if trail else ' ') + parts[2] if parts[2] else '')
                return r
    return rom0(th)
def rom0(th):
    out = []
    for part in re.split(r'\s+', th.strip()):
        rep = part.count('ๆ'); part = part.replace('ๆ', '')
        if not part: continue
        part = re.sub(r'[^\u0E00-\u0E7F]', '', part)
        if not part: continue
        try: ipa = n.th2ipa(part).replace('<s/>', '').strip()
        except Exception:
            from pythainlp.tokenize import word_tokenize
            ipa = ' '.join(n.th2ipa(w).replace('<s/>', '').strip() for w in word_tokenize(part) if w.strip())
        words = [w for w in re.split(r'[\s]+', ipa) if w]
        sy = []
        for w in words:
            for x in w.split('.'):
                x = x.strip()
                if x and re.search(r'[1-5]$', x): sy.append(syl(x))
        if rep and sy: sy.append(sy[-1])
        out.append(' '.join(sy))
    s = ', '.join(out)
    return s
if __name__ == '__main__':
    for t in ['ฉันเป็นหวัด', 'ข้าวผัด', 'ไข้หวัดใหญ่', 'เกี๊ยว', 'แอปเปิล', 'กินผักเยอะๆ', 'หายใจเข้า หายใจออก', 'ก๋วยเตี๋ยว', 'เคี้ยวช้าๆ','ร้านแว่น','สายตาสั้น','คอนแทคเลนส์']:
        print(t, '→', rom(t))
