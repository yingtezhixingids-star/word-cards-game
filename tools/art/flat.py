# 写实扁平插画工具：无描边，真实比例和颜色，靠深浅两色表现立体感
import math

def _hex(c):
    c = c.lstrip('#'); return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))

def shade(c, f):
    """f<0 变暗，f>0 变亮"""
    r, g, b = _hex(c)
    if f < 0:
        r, g, b = (int(v * (1 + f)) for v in (r, g, b))
    else:
        r, g, b = (int(v + (255 - v) * f) for v in (r, g, b))
    return '#%02x%02x%02x' % (r, g, b)

P = dict(
    skin='#f1c7a3', skin_d='#dda27c', skin2='#c98d63', skin2_d='#a96f49', hair='#3a2a20', grey='#c8c3bc',
    white='#ffffff', off='#f4f1ea', paper='#fbf8f0', lgrey='#d9dcde', mgrey='#a7adb1', dgrey='#5d6469', ink='#2f3437',
    red='#d9453a', blue='#3c7fc1', navy='#28456b', teal='#2fa59b', green='#5ba644', dgreen='#3c7a2c', yellow='#f3c234',
    orange='#f08a24', pink='#ef8fa4', purple='#7a4fa0', brown='#8a5a35', wood='#c58b54', jean='#3b5f8f', gold='#d9a33a',
)


def svg(inner, shadow=True):
    sh = '<ellipse cx="100" cy="186" rx="64" ry="8" fill="#000" opacity=".12"/>' if shadow else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">{sh}{inner}</svg>'

def R(x, y, w, h, fill, r=0, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {extra}/>'

def Ci(cx, cy, r, fill, extra=''):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {extra}/>'

def E(cx, cy, rx, ry, fill, extra=''):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" {extra}/>'

def Pa(d, fill='none', extra=''):
    return f'<path d="{d}" fill="{fill}" {extra}/>'

def St(d, color, w, extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'

def L(x1, y1, x2, y2, color, w=3):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'

def T(x, y, s, size=20, fill='#2f3437', weight=700, anchor='middle', family='Arial, Helvetica, sans-serif', extra=''):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

def G(inner, tr):
    return f'<g transform="{tr}">{inner}</g>'

def hi(cx, cy, rx, ry, op=.45, rot=0):
    """高光"""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" opacity="{op}" transform="rotate({rot} {cx} {cy})"/>'

def leaf(x, y, l, w, ang, color):
    d = f'M0,0 Q{l*.5},{-w} {l},0 Q{l*.5},{w} 0,0 Z'
    return f'<g transform="translate({x},{y}) rotate({ang})">' + Pa(d, color) + St(f'M2,0 L{l*.85},0', shade(color, -.25), 1.5) + '</g>'


# ---------- 人物（简洁写实：小五官、真实比例） ----------
def face(cx, cy, r, mood='smile', skin=None):
    e = ''
    ex, ey = r * .34, cy - r * .02
    if mood == 'closed':
        e += St(f'M{cx-ex-4},{ey} q4,3 8,0', '#3a2a20', 2) + St(f'M{cx+ex-4},{ey} q4,3 8,0', '#3a2a20', 2)
    else:
        e += Ci(cx - ex, ey, 2.6, '#2b211b') + Ci(cx + ex, ey, 2.6, '#2b211b')
    if mood in ('smile', 'closed'):
        e += St(f'M{cx-r*.25},{cy+r*.42} q{r*.25},{r*.2} {r*.5},0', '#9a4a3a', 2.2)
    elif mood == 'sad':
        e += St(f'M{cx-r*.22},{cy+r*.52} q{r*.22},{-r*.16} {r*.44},0', '#9a4a3a', 2.2)
        e += L(cx - ex - 5, ey - 8, cx - ex + 3, ey - 10, '#3a2a20', 2) + L(cx + ex + 5, ey - 8, cx + ex - 3, ey - 10, '#3a2a20', 2)
    elif mood == 'o':
        e += E(cx, cy + r * .48, r * .1, r * .13, '#7a3a30')
    elif mood == 'flat':
        e += L(cx - r * .18, cy + r * .48, cx + r * .18, cy + r * .48, '#9a4a3a', 2.2)
    e += Pa(f'M{cx},{cy+r*.05} q{-r*.1},{r*.2} {r*.03},{r*.24}', 'none', f'stroke="{shade(skin or P["skin"], -.25)}" stroke-width="2" stroke-linecap="round"')
    return e

def headshape(cx, cy, r, skin=None, hair=None, style='short', mood='smile', ear=True):
    skin = skin or P['skin']; hair = hair or P['hair']
    s = ''
    if style == 'long':
        s += Pa(f'M{cx-r*1.05},{cy+r*1.3} Q{cx-r*1.3},{cy-r*1.2} {cx},{cy-r*1.12} Q{cx+r*1.3},{cy-r*1.2} {cx+r*1.05},{cy+r*1.3} Z', hair)
    if style == 'bun':
        s += Ci(cx, cy - r * 1.05, r * .45, hair)
    if ear:
        s += E(cx - r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08)) + E(cx + r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08))
    s += E(cx, cy, r * .92, r, skin)
    if style in ('short', 'long', 'bun'):
        s += Pa(f'M{cx-r*.95},{cy-r*.05} Q{cx-r*1.0},{cy-r*1.15} {cx},{cy-r*1.08} Q{cx+r*1.0},{cy-r*1.15} {cx+r*.95},{cy-r*.05} Q{cx+r*.7},{cy-r*.6} {cx+r*.1},{cy-r*.55} Q{cx-r*.6},{cy-r*.45} {cx-r*.95},{cy-r*.05} Z', hair)
    elif style == 'grey':
        s += Pa(f'M{cx-r*.95},{cy-r*.1} Q{cx-r*1.0},{cy-r*1.1} {cx},{cy-r*1.06} Q{cx+r*1.0},{cy-r*1.1} {cx+r*.95},{cy-r*.1} Q{cx+r*.6},{cy-r*.7} {cx},{cy-r*.68} Q{cx-r*.6},{cy-r*.7} {cx-r*.95},{cy-r*.1} Z', P['grey'])
    return s + face(cx, cy, r, mood, skin)

def arm(pts, sleeve, skin, w=13, hand=True):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    s = St(d, sleeve, w)
    if hand:
        x, y = pts[-1]
        s += Ci(x, y, w * .5, skin)
    return s

def person(cx, ground, top=None, shirt=None, pants=None, skin=None, hair=None, style='short', mood='smile',
           arms='down', legs='stand', coat=None, shoes='#2f2a27', s=1.0, extra_top=''):
    """站立人物。arms: down / up / wave / front / hips ; legs: stand / walk / run"""
    shirt = shirt or P['blue']; pants = pants or P['navy']; skin = skin or P['skin']
    H = 168 * s; hr = 15 * s
    hy = ground - H + hr
    sh_y = hy + hr + 9 * s; hip_y = ground - 70 * s
    g = ''
    # legs
    lw = 14 * s
    if legs == 'stand':
        lp = [[(cx - 8*s, hip_y), (cx - 9*s, ground - 6*s)], [(cx + 8*s, hip_y), (cx + 9*s, ground - 6*s)]]
    elif legs == 'walk':
        lp = [[(cx - 6*s, hip_y), (cx - 18*s, ground - 6*s)], [(cx + 6*s, hip_y), (cx + 14*s, hip_y + 34*s), (cx + 24*s, ground - 6*s)]]
    else:
        lp = [[(cx - 4*s, hip_y), (cx - 28*s, hip_y + 26*s), (cx - 44*s, hip_y + 46*s)], [(cx + 6*s, hip_y), (cx + 24*s, hip_y + 30*s), (cx + 16*s, ground - 6*s)]]
    for l in lp:
        g += St('M' + ' L'.join(f'{x},{y}' for x, y in l), pants, lw)
        x, y = l[-1]
        g += E(x + 4 * s, y + 3 * s, 10 * s, 5 * s, shoes)
    # torso
    tw = 34 * s
    g += Pa(f'M{cx-tw/2},{sh_y+4*s} Q{cx-tw/2},{sh_y-2*s} {cx-tw/2+8*s},{sh_y-3*s} L{cx+tw/2-8*s},{sh_y-3*s} Q{cx+tw/2},{sh_y-2*s} {cx+tw/2},{sh_y+4*s} L{cx+tw/2-2*s},{hip_y+4*s} L{cx-tw/2+2*s},{hip_y+4*s} Z', shirt)
    if coat:
        g += Pa(f'M{cx-tw/2-2*s},{sh_y+4*s} Q{cx-tw/2},{sh_y-3*s} {cx-tw/2+8*s},{sh_y-4*s} L{cx-5*s},{sh_y-4*s} L{cx-3*s},{hip_y+16*s} L{cx-tw/2-3*s},{hip_y+16*s} Z', coat)
        g += Pa(f'M{cx+tw/2+2*s},{sh_y+4*s} Q{cx+tw/2},{sh_y-3*s} {cx+tw/2-8*s},{sh_y-4*s} L{cx+5*s},{sh_y-4*s} L{cx+3*s},{hip_y+16*s} L{cx+tw/2+3*s},{hip_y+16*s} Z', coat)
    # neck
    g += R(cx - 4.5 * s, hy + hr * .7, 9 * s, 10 * s, shade(skin, -.08), 3)
    # arms
    sl = coat or shirt
    L_sh, R_sh = (cx - tw / 2 + 2 * s, sh_y + 3 * s), (cx + tw / 2 - 2 * s, sh_y + 3 * s)
    A = {
        'down': ([L_sh, (cx - tw/2 - 5*s, sh_y + 30*s), (cx - tw/2 - 4*s, hip_y + 2*s)], [R_sh, (cx + tw/2 + 5*s, sh_y + 30*s), (cx + tw/2 + 4*s, hip_y + 2*s)]),
        'up': ([L_sh, (cx - tw/2 - 12*s, sh_y - 18*s), (cx - tw/2 - 14*s, hy - 22*s)], [R_sh, (cx + tw/2 + 12*s, sh_y - 18*s), (cx + tw/2 + 14*s, hy - 22*s)]),
        'wave': ([L_sh, (cx - tw/2 - 5*s, sh_y + 30*s), (cx - tw/2 - 4*s, hip_y + 2*s)], [R_sh, (cx + tw/2 + 16*s, sh_y + 6*s), (cx + tw/2 + 20*s, hy - 12*s)]),
        'front': ([L_sh, (cx - tw/2 - 4*s, sh_y + 28*s), (cx - 4*s, sh_y + 36*s)], [R_sh, (cx + tw/2 + 4*s, sh_y + 28*s), (cx + 6*s, sh_y + 32*s)]),
        'hips': ([L_sh, (cx - tw/2 - 14*s, sh_y + 22*s), (cx - tw/2 + 2*s, hip_y - 4*s)], [R_sh, (cx + tw/2 + 14*s, sh_y + 22*s), (cx + tw/2 - 2*s, hip_y - 4*s)]),
        'run': ([L_sh, (cx - tw/2 - 10*s, sh_y + 22*s), (cx - tw/2 + 6*s, sh_y + 30*s)], [R_sh, (cx + tw/2 + 12*s, sh_y + 16*s), (cx + tw/2 + 22*s, sh_y - 4*s)]),
    }[arms]
    for a in A:
        g += arm(a, sl, skin, 11 * s)
    g += headshape(cx, hy, hr, skin, hair, style, mood) + extra_top
    return g


def bust(cx, cy, r=30, shirt=None, skin=None, hair=None, style='short', mood='smile', coat=None, collar=None, w=None):
    """胸像：用于表现表情和头部动作"""
    shirt = shirt or P['blue']; skin = skin or P['skin']
    w = w or r * 3.4
    top = cy + r * .95
    g = R(cx - r * .3, cy + r * .6, r * .6, r * .6, shade(skin, -.1), 4)
    g += Pa(f'M{cx-w/2},{200} L{cx-w/2},{top+r*.7} Q{cx-w/2},{top} {cx-w/2+r*.8},{top} L{cx+w/2-r*.8},{top} Q{cx+w/2},{top} {cx+w/2},{top+r*.7} L{cx+w/2},{200} Z', shirt)
    if coat:
        g += Pa(f'M{cx-w/2},{200} L{cx-w/2},{top+r*.7} Q{cx-w/2},{top} {cx-w/2+r*.8},{top} L{cx-r*.35},{top} L{cx-r*.1},{200} Z', coat)
        g += Pa(f'M{cx+w/2},{200} L{cx+w/2},{top+r*.7} Q{cx+w/2},{top} {cx+w/2-r*.8},{top} L{cx+r*.35},{top} L{cx+r*.1},{200} Z', coat)
    if collar:
        g += Pa(f'M{cx-r*.38},{top} L{cx},{top+r*.45} L{cx+r*.38},{top} Z', collar)
    return g + headshape(cx, cy, r, skin, hair, style, mood)


def pill(cx, cy, w, h, c1, c2, rot=0):
    """胶囊"""
    return (f'<g transform="rotate({rot} {cx} {cy})">' +
            Pa(f'M{cx},{cy-h/2} L{cx-w/2+h/2},{cy-h/2} A{h/2},{h/2} 0 0,0 {cx-w/2+h/2},{cy+h/2} L{cx},{cy+h/2} Z', c1) +
            Pa(f'M{cx},{cy-h/2} L{cx+w/2-h/2},{cy-h/2} A{h/2},{h/2} 0 0,1 {cx+w/2-h/2},{cy+h/2} L{cx},{cy+h/2} Z', c2) +
            hi(cx - w / 4, cy - h / 4, w / 6, h / 8, .5) + '</g>')
