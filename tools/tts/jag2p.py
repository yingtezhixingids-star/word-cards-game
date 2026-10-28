# 日语转音素：用 misaki 的 cutlet 流程，但每个词的读音以数据里人工核对过的假名为准（修正 日→ひ、私→わたくし 这类误读）
import re, jaconv, difflib
from misaki import ja
G = ja.JAG2P()
Word = ja.Word
def hira(s): return jaconv.kata2hira(s or '')
def g2p(text, kana=''):
    t = G._normalize_text(text)
    toks = [w for w in G.tagger(t)]
    items = []
    for w in toks:
        f = w.feature
        kn = hira(f.kana if f.kana and f.kana != '*' else w.surface)
        pr = hira(f.pron if f.pron and f.pron != '*' else (f.kana if f.kana and f.kana != '*' else w.surface))
        ct = 6 if w.char_type == 7 or not w.is_unk else w.char_type
        items.append([w.surface, pr, kn, ct])
    if kana:
        A = re.sub(r'\s', '', hira(kana))
        K = ''.join(it[2] for it in items)
        own = [i for i, it in enumerate(items) for _ in it[2]]
        sm = difflib.SequenceMatcher(None, K, A, autojunk=False)
        newr = {}
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal': continue
            if i2 > i1: ts = sorted(set(own[i1:i2]))
            else: ts = [own[i1 - 1]] if i1 > 0 else [0]
            # 扩展到受影响词的完整读音
            a = min(k for k in range(len(K)) if own[k] == ts[0]); b = max(k for k in range(len(K)) if own[k] == ts[-1]) + 1
            # 对应 A 的区间：用 i→j 的映射
            def mapj(i):
                for o, x1, x2, y1, y2 in sm.get_opcodes():
                    if x1 <= i < x2 or (i == x2 == len(K) and o != 'insert'):
                        return y1 + (i - x1 if o == 'equal' else 0)
                return len(A)
            ja_, jb = mapj(a) if a < len(K) else len(A), (mapj(b) if b < len(K) else len(A))
            seg = A[ja_:jb]
            for n, ti in enumerate(ts): newr[ti] = seg if n == 0 else ''
        for ti, seg in newr.items():
            if seg != items[ti][2]: items[ti][1] = seg
    words = [Word(s, pr, ct) for s, pr, kn, ct in items if s]
    tokens = G._romaji_tokens(words)
    out = ''.join(str(tok) for tok in tokens)
    ps = re.sub(r'\s+', ' ', out.strip()).replace('(', '«').replace(')', '»')
    ps = re.sub(r'(?<![!",.:;?»—…”]) (?=ʔ)|(?<=ʔ) (?!["«“])', '', ps)
    return ps
if __name__ == '__main__':
    import json
    for t, a in json.load(open('texts-ja.json'))[:0]: pass
    tests = [('誕生日', 'たんじょうび'), ('私のパーティーに来てください。', 'わたしのパーティーにきてください。'), ('母は九十歳です。', 'はははきゅうじゅうさいです。'), ('人の骨格には二百六本の骨があります。', 'ひとのこっかくにはにひゃくろっぽんのほねがあります。'), ('お皿を取ってください。', 'おさらをとってください。'), ('白髪', 'しらが'), ('Tシャツ', 'てぃーシャツ'), ('宝石は箱にしまっています。', 'ほうせきははこにしまっています。'), ('孫はパーカーがお気に入りです。', 'まごはパーカーがおきにいりです。'), ('今日は結婚四十周年の記念日です。', 'きょうはけっこんよんじゅっしゅうねんのきねんびです。'), ('腕時計', 'うでどけい'), ('絵を描く', 'えをかく')]
    for t, a in tests: print(t, '|', G(t), '=>', g2p(t, a))
