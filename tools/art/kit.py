# 单词卡牌插画工具：统一的扁平风格（粗描边、暖色、圆润）
# 画布 200x200，主体居中，底部一块柔和阴影
D = '#3b2f2a'          # 描边深棕
SW = 5                 # 描边粗细
C = dict(
    skin='#f2c9a0', skin2='#e0a97e', red='#e05a47', red2='#c23f2e', pink='#f29bb0', orange='#f0954a',
    yellow='#f2c14e', gold='#e0a93b', green='#6fae5a', green2='#4e8a3e', teal='#3fa7a0', blue='#4a8fc9',
    blue2='#2f6aa0', sky='#9fd0ec', purple='#8a6bbf', brown='#a5714b', brown2='#7a5034', white='#fbf7ee',
    cream='#f3e6c8', grey='#9aa3a8', grey2='#6d757a', light='#dfe3e4', black='#2e2a28', hair='#4a3426',
    greyhair='#c9c4bd', mint='#bfe3d0', lav='#d8cdf0', peach='#f7c9a8',
)
O = f'stroke="{D}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'
O3 = f'stroke="{D}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"'


def svg(inner, shadow=True):
    sh = '<ellipse cx="100" cy="184" rx="62" ry="9" fill="#000" opacity=".10"/>' if shadow else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">{sh}{inner}</svg>'


def circ(cx, cy, r, fill, o=O):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {o}/>'


def ell(cx, cy, rx, ry, fill, o=O, extra=''):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" {o} {extra}/>'


def rect(x, y, w, h, fill, r=8, o=O, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {o} {extra}/>'


def path(d, fill='none', o=O, extra=''):
    return f'<path d="{d}" fill="{fill}" {o} {extra}/>'


def line(x1, y1, x2, y2, w=SW, color=D):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'


def text(x, y, s, size=28, fill=D, weight=800, anchor='middle', family='Arial, sans-serif'):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def limb(points, color, w=13):
    """手脚：先画深色粗线做描边，再画彩色细线"""
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in points)
    return (f'<path d="{d}" fill="none" stroke="{D}" stroke-width="{w + 9}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def eyes(cx, cy, r, kind='dot'):
    ex = r * .36
    if kind == 'closed':
        return (path(f'M{cx-ex-6},{cy} Q{cx-ex},{cy+5} {cx-ex+6},{cy}', o=O3) +
                path(f'M{cx+ex-6},{cy} Q{cx+ex},{cy+5} {cx+ex+6},{cy}', o=O3))
    if kind == 'spiral':
        sp = lambda x: path(f'M{x},{cy} m-1,0 a2,2 0 1,1 3,0 a4,4 0 1,1 -7,0 a6,6 0 1,1 11,0', o='stroke="%s" stroke-width="2.5" stroke-linecap="round"' % D)
        return sp(cx - ex) + sp(cx + ex)
    if kind == 'x':
        xx = lambda x: line(x - 5, cy - 5, x + 5, cy + 5, 3.5) + line(x + 5, cy - 5, x - 5, cy + 5, 3.5)
        return xx(cx - ex) + xx(cx + ex)
    if kind == 'sad':
        return (circ(cx - ex, cy + 1, 4, D, '') + circ(cx + ex, cy + 1, 4, D, '') +
                line(cx - ex - 7, cy - 9, cx - ex + 4, cy - 12, 3) + line(cx + ex + 7, cy - 9, cx + ex - 4, cy - 12, 3))
    return circ(cx - ex, cy, 4.2, D, '') + circ(cx + ex, cy, 4.2, D, '')


def mouth(cx, cy, r, kind='smile'):
    w = r * .32
    if kind == 'smile':
        return path(f'M{cx-w},{cy} Q{cx},{cy+w*.9} {cx+w},{cy}', o=O3)
    if kind == 'grin':
        return path(f'M{cx-w},{cy-2} Q{cx},{cy+w*1.3} {cx+w},{cy-2} Z', fill='#fff', o=O3)
    if kind == 'frown':
        return path(f'M{cx-w},{cy+5} Q{cx},{cy-w*.5} {cx+w},{cy+5}', o=O3)
    if kind == 'o':
        return ell(cx, cy + 3, w * .45, w * .55, D, '')
    if kind == 'flat':
        return line(cx - w * .7, cy + 2, cx + w * .7, cy + 2, 3.5)
    if kind == 'wavy':
        return path(f'M{cx-w},{cy+3} q{w/4},-6 {w/2},0 t{w/2},0 t{w/2},0 t{w/2},0', o=O3)
    return ''


def head(cx, cy, r, mood='smile', skin=None, hair=None, style='short', eye='dot', blush=True, extra_face=''):
    skin = skin or C['skin']; hair = hair or C['hair']
    h = ''
    if style == 'long':
        h += path(f'M{cx-r-4},{cy+r*.9} Q{cx-r-8},{cy-r*1.1} {cx},{cy-r-6} Q{cx+r+8},{cy-r*1.1} {cx+r+4},{cy+r*.9} Z', fill=hair)
    s = circ(cx, cy, r, skin)
    if style in ('short', 'long'):
        s += path(f'M{cx-r},{cy-r*.05} Q{cx-r*.95},{cy-r*1.15} {cx},{cy-r-2} Q{cx+r*.95},{cy-r*1.15} {cx+r},{cy-r*.05} Q{cx+r*.5},{cy-r*.55} {cx},{cy-r*.5} Q{cx-r*.5},{cy-r*.55} {cx-r},{cy-r*.05} Z', fill=hair)
    elif style == 'bun':
        s = circ(cx, cy - r - 6, r * .38, hair) + s + path(f'M{cx-r},{cy-r*.05} Q{cx-r*.95},{cy-r*1.15} {cx},{cy-r-2} Q{cx+r*.95},{cy-r*1.15} {cx+r},{cy-r*.05} Q{cx+r*.5},{cy-r*.55} {cx},{cy-r*.5} Q{cx-r*.5},{cy-r*.55} {cx-r},{cy-r*.05} Z', fill=hair)
    elif style == 'bald':
        s += path(f'M{cx-r+2},{cy+r*.05} Q{cx-r-6},{cy-r*.35} {cx-r*.6},{cy-r*.55}', fill='none', o=f'stroke="{hair}" stroke-width="8" stroke-linecap="round"')
        s += path(f'M{cx+r-2},{cy+r*.05} Q{cx+r+6},{cy-r*.35} {cx+r*.6},{cy-r*.55}', fill='none', o=f'stroke="{hair}" stroke-width="8" stroke-linecap="round"')
    face = eyes(cx, cy + r * .05, r, eye) + mouth(cx, cy + r * .42, r, mood)
    if blush:
        face += ell(cx - r * .58, cy + r * .35, r * .15, r * .09, C['pink'], '', 'opacity=".75"') + ell(cx + r * .58, cy + r * .35, r * .15, r * .09, C['pink'], '', 'opacity=".75"')
    return h + s + face + extra_face


def torso(cx, top, w, h, color, collar=None):
    """上半身：圆肩的梯形"""
    x1, x2 = cx - w / 2, cx + w / 2
    d = f'M{x1+4},{top+h} L{x1},{top+18} Q{x1+2},{top} {x1+22},{top} L{x2-22},{top} Q{x2-2},{top} {x2},{top+18} L{x2-4},{top+h} Z'
    s = path(d, fill=color)
    if collar:
        s += path(f'M{cx-14},{top} L{cx},{top+18} L{cx+14},{top}', fill=collar, o=O3)
    return s


def bust(cx=100, top=40, shirt=None, mood='smile', hair=None, style='short', skin=None, eye='dot', collar=None, r=34, extra_face=''):
    """半身像：头+上半身"""
    shirt = shirt or C['blue']
    return torso(cx, top + r * 2 - 4, r * 3.1, 200 - (top + r * 2 - 4) - 14, shirt, collar) + head(cx, top + r, r, mood, skin, hair, style, eye, extra_face=extra_face)


def figure(cx, ground, pose='stand', shirt=None, pants=None, mood='smile', hair=None, style='short', skin=None, eye='dot', s=1.0):
    """全身小人。pose: stand / walk / run / armsup / sit / bow"""
    shirt = shirt or C['blue']; pants = pants or C['brown2']; skin = skin or C['skin']
    hy = ground - 150 * s; hr = 22 * s
    body_top = hy + hr + 2; hip = ground - 62 * s
    sh_l, sh_r = (cx - 18 * s, body_top + 10 * s), (cx + 18 * s, body_top + 10 * s)
    legs = {
        'stand': [[(cx - 10*s, hip), (cx - 12*s, ground - 6)], [(cx + 10*s, hip), (cx + 12*s, ground - 6)]],
        'walk':  [[(cx - 8*s, hip), (cx - 26*s, ground - 6)], [(cx + 8*s, hip), (cx + 22*s, ground - 26*s), (cx + 30*s, ground - 6)]],
        'run':   [[(cx - 6*s, hip), (cx - 34*s, ground - 18*s), (cx - 48*s, ground - 34*s)], [(cx + 8*s, hip), (cx + 28*s, ground - 30*s), (cx + 22*s, ground - 6)]],
        'armsup': [[(cx - 12*s, hip), (cx - 18*s, ground - 6)], [(cx + 12*s, hip), (cx + 18*s, ground - 6)]],
        'sit':   [[(cx - 10*s, hip), (cx - 40*s, hip + 2), (cx - 42*s, ground - 6)], [(cx + 10*s, hip), (cx - 20*s, hip + 6), (cx - 22*s, ground - 6)]],
        'bow':   [[(cx - 10*s, hip), (cx - 12*s, ground - 6)], [(cx + 10*s, hip), (cx + 12*s, ground - 6)]],
    }[pose]
    arms = {
        'stand': [[sh_l, (cx - 30*s, hip - 4*s)], [sh_r, (cx + 30*s, hip - 4*s)]],
        'walk':  [[sh_l, (cx - 30*s, hip - 14*s)], [sh_r, (cx + 32*s, hip - 20*s)]],
        'run':   [[sh_l, (cx - 36*s, body_top + 34*s), (cx - 30*s, body_top + 10*s)], [sh_r, (cx + 32*s, body_top + 40*s), (cx + 46*s, body_top + 24*s)]],
        'armsup': [[sh_l, (cx - 34*s, body_top - 14*s), (cx - 36*s, hy - 30*s)], [sh_r, (cx + 34*s, body_top - 14*s), (cx + 36*s, hy - 30*s)]],
        'sit':   [[sh_l, (cx - 30*s, hip - 4*s)], [sh_r, (cx + 26*s, hip - 8*s)]],
        'bow':   [[sh_l, (cx - 26*s, hip)], [sh_r, (cx + 26*s, hip)]],
    }[pose]
    g = ''.join(limb(l, pants, 13 * s) for l in legs)
    g += ''.join(ell(l[-1][0] + (3 if l[-1][0] >= cx else -3), l[-1][1] + 2, 11 * s, 6 * s, C['black'], O3) for l in legs if pose != 'run' or True)
    g += path(f'M{cx-22*s},{hip+4*s} L{cx-24*s},{body_top+12*s} Q{cx-22*s},{body_top} {cx-8*s},{body_top} L{cx+8*s},{body_top} Q{cx+22*s},{body_top} {cx+24*s},{body_top+12*s} L{cx+22*s},{hip+4*s} Z', fill=shirt)
    g += ''.join(limb(a, shirt, 12 * s) for a in arms)
    g += ''.join(circ(a[-1][0], a[-1][1], 7 * s, skin, O3) for a in arms)
    g += head(cx, hy, hr, mood, skin, hair, style, eye)
    return g


def sparkle(x, y, r=8, color=None):
    color = color or C['yellow']
    return path(f'M{x},{y-r} Q{x+r*.2},{y-r*.2} {x+r},{y} Q{x+r*.2},{y+r*.2} {x},{y+r} Q{x-r*.2},{y+r*.2} {x-r},{y} Q{x-r*.2},{y-r*.2} {x},{y-r} Z', fill=color, o=O3)


def cross(cx, cy, s, color=None):
    color = color or C['red']
    a = s / 3
    return path(f'M{cx-a/2},{cy-s/2} h{a} v{a} h{a} v{a} h-{a} v{a} h-{a} v-{a} h-{a} v-{a} h{a} Z', fill=color, o=O3)


def pill(cx, cy, w, h, c1, c2, rot=0):
    return (f'<g transform="rotate({rot} {cx} {cy})">' +
            path(f'M{cx},{cy-h/2} L{cx-w/2+h/2},{cy-h/2} A{h/2},{h/2} 0 0,0 {cx-w/2+h/2},{cy+h/2} L{cx},{cy+h/2} Z', fill=c1) +
            path(f'M{cx},{cy-h/2} L{cx+w/2-h/2},{cy-h/2} A{h/2},{h/2} 0 0,1 {cx+w/2-h/2},{cy+h/2} L{cx},{cy+h/2} Z', fill=c2) + '</g>')


def drop(cx, cy, s, color=None):
    color = color or C['sky']
    return path(f'M{cx},{cy-s} Q{cx+s*.75},{cy} {cx},{cy+s*.55} Q{cx-s*.75},{cy} {cx},{cy-s} Z', fill=color, o=O3)


def heart(cx, cy, s, color=None):
    color = color or C['red']
    return path(f'M{cx},{cy+s*.85} C{cx-s*1.3},{cy-s*.05} {cx-s*.75},{cy-s*1.05} {cx},{cy-s*.4} C{cx+s*.75},{cy-s*1.05} {cx+s*1.3},{cy-s*.05} {cx},{cy+s*.85} Z', fill=color)


def star(cx, cy, r, color=None, points=5, inner=.45):
    import math
    color = color or C['yellow']
    pts = []
    for i in range(points * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.pi / points * i - math.pi / 2
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{color}" {O3}/>'
