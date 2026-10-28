import re, unicodedata
import tltk.nlp as n
from pythainlp.tokenize import word_tokenize, Tokenizer
from pythainlp.corpus.common import thai_words
from rom import syl
FIX = {}
VOCAB = set()
_tok = [None]
def setup(fix, vocab):
    FIX.update(fix); VOCAB.update(vocab)
    words = set(thai_words()) | set(fix) | set(vocab)
    _tok[0] = Tokenizer(custom_dict=words, engine='newmm')
def ipa_word(w):
    try: ipa = n.th2ipa(w).replace('<s/>', '').strip()
    except Exception: return None
    out = []
    for x in re.split(r'[\s.]+', ipa):
        if re.search(r'[1-5]$', x): out.append(syl(x))
    return ' '.join(out)
def rom_word(w):
    if w in FIX: return FIX[w]
    for k in sorted(FIX, key=len, reverse=True):
        if k in w and k != w:
            i = w.index(k); a, b = w[:i], w[i+len(k):]
            return ' '.join(x for x in [rom_word(a) if a else '', FIX[k], rom_word(b) if b else ''] if x)
    return ipa_word(w) or ''
def rom(th):
    phrases = []
    for part in th.strip().split():
        rep = part.count('ๆ'); part = re.sub(r'[^฀-๿]', '', part.replace('ๆ', ''))
        if not part: continue
        toks = [t for t in _tok[0].word_tokenize(part) if t.strip()]
        sy = [rom_word(t) for t in toks]
        if rep and sy: sy.append(sy[-1])
        phrases.append(' '.join(s for s in sy if s))
    return ', '.join(phrases)
