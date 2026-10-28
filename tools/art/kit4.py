from kit3 import *
import math

def board_(x, y, w, h, col='#2f4a3a', inner=''):
    return R(x - 6, y - 6, w + 12, h + 12, '#8a5a35', 4) + R(x, y, w, h, col, 2) + inner + R(x + w * .3, y + h + 6, w * .4, 6, '#a8703e', 2)

def book_(x, y, s=1, col='#3c7fc1', rot=0):
    return G(R(-30, -40, 60, 80, col, 3) + R(-26, -40, 4, 80, shade(col, -.25)) + R(-30, 34, 60, 6, '#f6efe0') + R(-10, -24, 30, 6, '#ffffff', 2, 'opacity=".7"'), f'translate({x},{y}) rotate({rot}) scale({s})')

def open_book(cx, cy, s=1, col='#3c7fc1'):
    return G(Pa('M0,-40 L-70,-48 L-70,40 L0,48 Z', '#ffffff') + Pa('M0,-40 L70,-48 L70,40 L0,48 Z', '#f6f1e6') + Pa('M-70,40 L0,48 L70,40 L70,46 L0,54 L-70,46 Z', col) + ''.join(L(-60, -30 + k * 12, -10, -26 + k * 12, '#a7adb1', 2) + L(10, -26 + k * 12, 60, -30 + k * 12, '#a7adb1', 2) for k in range(6)), f'translate({cx},{cy}) scale({s})')

def pencil_(x, y, s=1, rot=0):
    return G(R(-60, -7, 100, 14, '#f3c234') + R(-60, -7, 100, 4, '#f8d860') + R(-74, -7, 16, 14, '#ef8fa4', 3) + R(-62, -7, 6, 14, '#c4cbd0') + Pa('M40,-7 L62,0 L40,7 Z', '#f6e2b8') + Pa('M54,-3 L62,0 L54,3 Z', '#2f3437'), f'translate({x},{y}) rotate({rot}) scale({s})')

def pen_(x, y, s=1, rot=0, col='#2f4a7a'):
    return G(R(-60, -8, 90, 16, col, 6) + R(-62, -10, 20, 20, '#d9a33a', 4) + Pa('M30,-8 L56,0 L30,8 Z', '#c4cbd0') + Pa('M48,-2 L58,0 L48,2 Z', '#2f3437') + R(-40, -12, 50, 4, '#d9a33a', 2), f'translate({x},{y}) rotate({rot}) scale({s})')

def flask(cx, base, w, liquid='#7cc05a', kind='cone'):
    if kind == 'cone':
        g = Pa(f'M{cx-8},{base-110} L{cx+8},{base-110} L{cx+8},{base-70} L{cx+w/2},{base} L{cx-w/2},{base} L{cx-8},{base-70} Z', '#eef6fa', 'opacity=".9"') + Pa(f'M{cx-w/2*.75},{base-28} L{cx+w/2*.75},{base-28} L{cx+w/2},{base} L{cx-w/2},{base} Z', liquid)
    else:
        g = Ci(cx, base - w / 2, w / 2, '#eef6fa', 'opacity=".9"') + R(cx - 8, base - w - 40, 16, 44, '#eef6fa', 3, 'opacity=".9"') + Pa(f'M{cx-w/2+3},{base-w/2+4} A{w/2-3},{w/2-3} 0 0,0 {cx+w/2-3},{base-w/2+4} Z', liquid)
    return g + R(cx - 10, (base - 112) if kind == 'cone' else (base - w - 42), 20, 6, '#c4cbd0', 2)

def tube(x, y, s=1, rot=0, liquid='#5aa1d4'):
    return G(R(-10, -60, 20, 110, '#eef6fa', 10, 'opacity=".9"') + R(-10, 0, 20, 50, liquid, 10) + R(-12, -64, 24, 8, '#c4cbd0', 3), f'translate({x},{y}) rotate({rot}) scale({s})')

def atom_(cx, cy, r, nuc='#e2463b'):
    g = ''.join(E(cx, cy, r, r * .36, 'none', f'stroke="#3c7fc1" stroke-width="3" transform="rotate({a} {cx} {cy})"') for a in (0, 60, 120))
    g += Ci(cx, cy, r * .2, nuc) + ''.join(Ci(cx + r * math.cos(math.radians(a)) * (1 if k == 0 else 1), cy + r * .36 * math.sin(math.radians(a)), 5, '#f3c234') for k, a in enumerate((0,)))
    for a in (0, 60, 120):
        t = math.radians(a)
        g += Ci(cx + r * math.cos(t), cy + r * math.sin(t), 5, '#f3c234')
    return g

def element_tile(sym, num, name_col='#5aa1d4', mass=''):
    return R(40, 40, 120, 120, name_col, 8) + R(48, 48, 104, 104, '#ffffff', 4) + T(62, 70, str(num), 16, '#2f3437', 700, 'start') + T(100, 128, sym, 54, '#2f3437', 900) + T(100, 148, mass, 12, '#5d6469', 700)

def crown(x, y, s=1, col='#f3c234'):
    return G(Pa('M-40,20 L-40,-10 L-20,10 L0,-24 L20,10 L40,-10 L40,20 Z', col) + R(-40, 16, 80, 10, shade(col, -.15)) + Ci(0, 4, 5, '#e2463b') + Ci(-24, 12, 4, '#3c7fc1') + Ci(24, 12, 4, '#5ba644'), f'translate({x},{y}) scale({s})')

def magnet_(x, y, s=1, rot=0):
    return G(St('M-30,40 L-30,0 A30,30 0 0,1 30,0 L30,40', '#e2463b', 22) + R(-41, 30, 22, 16, '#c4cbd0') + R(19, 30, 22, 16, '#c4cbd0'), f'translate({x},{y}) rotate({rot}) scale({s})')

def micro(x, y, s=1):
    return G(R(-40, 60, 80, 14, '#2f3437', 4) + St('M20,60 Q40,20 10,-20', '#3c7fc1', 14) + R(-20, 20, 40, 8, '#5d6469', 2) + G(R(-8, -60, 16, 60, '#e6ecef', 3) + R(-10, -66, 20, 10, '#2f3437', 3), 'rotate(-25)') + Ci(0, 40, 6, '#a7adb1'), f'translate({x},{y}) scale({s})')

def virus_(x, y, r, col='#7cc05a'):
    return ''.join(L(x + r * math.cos(a), y + r * math.sin(a), x + r * 1.35 * math.cos(a), y + r * 1.35 * math.sin(a), shade(col, -.2), 3) + Ci(x + r * 1.4 * math.cos(a), y + r * 1.4 * math.sin(a), r * .14, '#e2463b') for a in [k * math.pi / 6 for k in range(12)]) + Ci(x, y, r, col) + Ci(x - r * .3, y - r * .2, r * .2, shade(col, .3))

def ingots(c, sym, num):
    bar = lambda x, y: Pa(f'M{x-30},{y+14} L{x-20},{y-10} L{x+20},{y-10} L{x+30},{y+14} Z', c) + Pa(f'M{x-20},{y-10} L{x+20},{y-10} L{x+16},{y-4} L{x-16},{y-4} Z', shade(c, .25)) + hi(x - 10, y, 10, 3, .5)
    return bar(70, 160) + bar(130, 160) + bar(100, 134) + R(130, 24, 50, 50, '#ffffff', 6, f'stroke="{shade(c,-.2)}" stroke-width="4"') + T(155, 60, sym, 24, '#2f3437', 900) + T(136, 38, str(num), 10, '#5d6469', 700, 'start')


def fighead(x, ground, s):
    return x, ground - 153 * s, 15 * s

def suit_bust(cx, cy, r, suit='#2f3a4a', tie='#e2463b', hair='#3a2a20', style='short', m='smile', blush=None):
    g = body(cx, cy, r, suit) + Pa(f'M{cx-r*.35},{cy+r*1.02} L{cx},{cy+r*1.6} L{cx+r*.35},{cy+r*1.02} Z', '#ffffff')
    g += Pa(f'M{cx-r*.1},{cy+r*1.08} L{cx+r*.1},{cy+r*1.08} L{cx+r*.14},{cy+r*1.7} L{cx},{cy+r*1.85} L{cx-r*.14},{cy+r*1.7} Z', tie)
    return g + face_full(cx, cy, r, hair, style, 'dot', m, None, blush)

def monitor(x, y, w, h, inner='', scr='#9fd0ec', col='#2f3437'):
    return R(x, y, w, h, col, 6) + R(x + 6, y + 6, w - 12, h - 14, scr, 2) + inner + R(x + w / 2 - 6, y + h, 12, 14, '#5d6469') + R(x + w / 2 - 24, y + h + 12, 48, 6, '#5d6469', 3)

def laptop(cx, base, w, inner='', scr='#9fd0ec'):
    h = w * .62
    return R(cx - w / 2, base - h - 8, w, h, '#3a4048', 6) + R(cx - w / 2 + 6, base - h - 2, w - 12, h - 12, scr, 2) + inner + Pa(f'M{cx-w/2-12},{base-8} L{cx+w/2+12},{base-8} L{cx+w/2+4},{base} L{cx-w/2-4},{base} Z', '#a7adb1')

def phone_(cx, cy, w, h, inner='', scr='#9fd0ec', col='#2f3437'):
    return R(cx - w / 2, cy - h / 2, w, h, col, w * .16) + R(cx - w / 2 + 4, cy - h / 2 + 10, w - 8, h - 20, scr, 2) + inner + R(cx - 6, cy - h / 2 + 4, 12, 3, '#5d6469', 1)

def doc_(x, y, w, h, lines=6, col='#ffffff', fold=True, lc='#a7adb1'):
    g = Pa(f'M{x},{y} L{x+w-16},{y} L{x+w},{y+16} L{x+w},{y+h} L{x},{y+h} Z', col) if fold else R(x, y, w, h, col, 2)
    if fold: g += Pa(f'M{x+w-16},{y} L{x+w-16},{y+16} L{x+w},{y+16} Z', '#d9dcde')
    return g + ''.join(L(x + 10, y + 22 + k * (h - 34) / max(lines, 1), x + w - (10 if k % 3 else 24), y + 22 + k * (h - 34) / max(lines, 1), lc, 3) for k in range(lines))

def folder_(x, y, w, h, col='#f3c234'):
    return Pa(f'M{x},{y+8} L{x},{y-4} Q{x},{y-8} {x+4},{y-8} L{x+w*.35},{y-8} L{x+w*.42},{y} L{x+w},{y} L{x+w},{y+h} L{x},{y+h} Z', shade(col, -.15)) + R(x, y + 8, w, h - 8, col, 3)

def mic_(x, y, s=1, rot=0, col='#2f3437'):
    return G(R(-6, 0, 12, 60, col, 4) + E(0, -6, 16, 20, '#5d6469') + ''.join(L(-12, -14 + k * 6, 12, -14 + k * 6, '#8a9196', 1.5) for k in range(5)) + R(-10, 8, 20, 8, '#e2463b', 2), f'translate({x},{y}) rotate({rot}) scale({s})')

def gavel(x, y, s=1, rot=-30):
    return G(R(-4, 0, 8, 70, WOODD, 3) + R(-30, -16, 60, 26, '#8a5a35', 6) + R(-34, -18, 8, 30, '#6a3a20', 3) + R(26, -18, 8, 30, '#6a3a20', 3), f'translate({x},{y}) rotate({rot}) scale({s})')

def scales_(cx, cy, s=1, col='#d9a33a'):
    return G(R(-3, -50, 6, 100, col) + R(-30, 46, 60, 8, col, 3) + Ci(0, -54, 6, col) + L(-60, -40, 60, -40, col, 5) + L(-60, -40, -76, 0, col, 2) + L(-60, -40, -44, 0, col, 2) + L(60, -40, 44, 0, col, 2) + L(60, -40, 76, 0, col, 2) + Pa('M-80,0 L-40,0 Q-60,20 -80,0 Z', col) + Pa('M40,0 L80,0 Q60,20 40,0 Z', col), f'translate({cx},{cy}) scale({s})')

def camera_(cx, cy, s=1, col='#2f3437'):
    return G(R(-50, -30, 100, 66, col, 10) + R(-24, -42, 34, 16, col, 4) + Ci(4, 4, 26, '#5d6469') + Ci(4, 4, 18, '#1f2a35') + hi(-2, -2, 6, 4, .6) + R(30, -22, 12, 8, '#f3c234', 2) + R(-44, -38, 14, 8, '#a7adb1', 2), f'translate({cx},{cy}) scale({s})')

def tv_(x, y, w, h, inner='', scr='#9fd0ec'):
    return R(x, y, w, h, '#2f3437', 8) + R(x + 8, y + 8, w - 16, h - 16, scr, 3) + inner + L(x + w * .3, y + h, x + w * .2, y + h + 14, '#2f3437', 5) + L(x + w * .7, y + h, x + w * .8, y + h + 14, '#2f3437', 5)

def cloud_(cx, cy, s=1, col='#ffffff'):
    return G(Ci(-30, 6, 22, col) + Ci(0, -8, 30, col) + Ci(30, 6, 22, col) + R(-30, 6, 60, 22, col), f'translate({cx},{cy}) scale({s})')

def cursor_(x, y, s=1, col='#ffffff'):
    return G(Pa('M0,0 L0,40 L10,30 L18,48 L26,44 L18,27 L32,27 Z', col, 'stroke="#2f3437" stroke-width="3" stroke-linejoin="round"'), f'translate({x},{y}) scale({s})')

def briefcase(cx, cy, w, col='#8a5a35'):
    h = w * .7
    return R(cx - w * .2, cy - h / 2 - 12, w * .4, 16, 'none', 5, f'stroke="{shade(col,-.3)}" stroke-width="5"') + R(cx - w / 2, cy - h / 2, w, h, col, 6) + R(cx - w / 2, cy - h * .1, w, 5, shade(col, -.2)) + R(cx - 8, cy - h * .16, 16, 12, '#d9a33a', 2)

def calendar_(x, y, w, h, hl=None, col='#e2463b', hlcol='#e2463b'):
    g = R(x, y, w, h, '#ffffff', 6) + R(x, y, w, h * .22, col, 6) + R(x, y + h * .14, w, h * .08, col) + ''.join(R(x + w * .25 + k * w * .5 - 3, y - 6, 6, 14, '#5d6469', 3) for k in range(2))
    cw, chh = (w - 16) / 7, (h * .78 - 12) / 5
    for k in range(35):
        cx_, cy_ = x + 8 + (k % 7) * cw + cw / 2, y + h * .22 + 6 + (k // 7) * chh + chh / 2
        g += Ci(cx_, cy_, min(cw, chh) * .2, '#c4cbd0')
        if hl is not None and k in (hl if isinstance(hl, (list, tuple)) else [hl]):
            g += Ci(cx_, cy_, min(cw, chh) * .48, 'none', f'stroke="{hlcol}" stroke-width="3"')
    return g

def badge_card(x, y, s=1, col='#3c7fc1'):
    return G(L(0, -40, 0, -10, col, 3) + R(-16, -12, 32, 44, '#ffffff', 4, f'stroke="{col}" stroke-width="2"') + Ci(0, 4, 6, SK) + R(-10, 16, 20, 3, '#a7adb1') + R(-10, 22, 14, 3, '#a7adb1'), f'translate({x},{y}) scale({s})')

def hardhat(cx, cy, r, col='#f3c234'):
    return Pa(f'M{cx-r*1.1},{cy-r*.15} Q{cx-r*1.0},{cy-r*1.2} {cx},{cy-r*1.2} Q{cx+r*1.0},{cy-r*1.2} {cx+r*1.1},{cy-r*.15} Z', col) + R(cx - r * 1.35, cy - r * .3, r * 2.7, r * .3, shade(col, -.15), r * .12) + R(cx - r * .12, cy - r * 1.2, r * .24, r * .9, shade(col, .2))

FIELD = '#8cc06a'
def barn_(cx, base, w, col='#c0392b'):
    h = w * .7
    return R(cx - w / 2, base - h, w, h, col) + Pa(f'M{cx-w/2-6},{base-h} L{cx},{base-h-w*.42} L{cx+w/2+6},{base-h} Z', '#7a2a20') + R(cx - w * .2, base - h * .6, w * .4, h * .6, '#ffffff') + R(cx - w * .17, base - h * .57, w * .34, h * .57, col) + L(cx - w * .17, base - h * .57, cx + w * .17, base, '#ffffff', 3) + L(cx + w * .17, base - h * .57, cx - w * .17, base, '#ffffff', 3) + R(cx - w * .1, base - h - w * .22, w * .2, w * .14, '#ffffff')

def tractor(cx, base, s=1, col='#e2463b'):
    return G(R(-50, -50, 70, 30, col, 4) + R(-10, -86, 40, 40, col, 3) + R(-4, -80, 28, 26, '#9fd0ec', 2) + R(-56, -60, 6, 26, '#5d6469') + wheel(20, -30, 30, '#2f3437', '#f3c234') + wheel(-40, -16, 16, '#2f3437', '#f3c234'), f'translate({cx},{base}) scale({s})')

def wheat_(x, y, s=1, rot=0):
    g = St('M0,60 Q2,20 0,-30', '#c8a040', 3)
    for k in range(6):
        g += E(-6, -30 + k * 9, 5, 9, '#e8c060', 'transform="rotate(-25 -6 %s)"' % (-30 + k * 9)) + E(6, -30 + k * 9, 5, 9, '#e8c060', 'transform="rotate(25 6 %s)"' % (-30 + k * 9))
    g += E(0, -40, 4, 9, '#e8c060')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def crop_rows(y0=110, col='#5aaa3a'):
    g = ''
    for r_ in range(4):
        yy = y0 + r_ * 22
        g += R(0, yy + 8, 200, 8, '#a8703e')
        for k in range(10):
            g += leaf(10 + k * 20, yy + 8, 12 + r_ * 2, 5, -60, col) + leaf(10 + k * 20, yy + 8, 12 + r_ * 2, 5, -120, col)
    return g

def hay_bale(cx, base, w):
    h = w * .7
    return R(cx - w / 2, base - h, w, h, '#e8c060', 6) + ''.join(L(cx - w / 2 + 4, base - h + k * h / 5, cx + w / 2 - 4, base - h + k * h / 5 + 3, '#c8a040', 2) for k in range(1, 5)) + R(cx - w * .3, base - h, 4, h, '#a8803a') + R(cx + w * .25, base - h, 4, h, '#a8803a')

def fruit_tree(x, base, s=1):
    return G(R(-6, -40, 12, 40, '#8a5a35') + Ci(0, -60, 34, '#4a9a3a') + Ci(-20, -44, 22, '#5aaa3a') + Ci(20, -44, 22, '#5aaa3a') + ''.join(Ci(dx, dy, 5, '#e2463b') for dx, dy in [(-14, -64), (10, -70), (18, -48), (-20, -42), (2, -50)]), f'translate({x},{base}) scale({s})')

def crane_(x, base, s=1):
    g = R(-6, -170, 12, 170, '#f3c234') + ''.join(L(-6, -170 + k * 14, 6, -156 + k * 14, '#d9a020', 2) for k in range(12))
    g += R(-60, -176, 160, 10, '#f3c234') + R(-60, -166, 30, 16, '#5d6469') + Pa('M-6,-176 L0,-196 L6,-176 Z', '#f3c234') + L(0, -196, 90, -176, '#5d6469', 1.5) + L(0, -196, -60, -176, '#5d6469', 1.5)
    g += L(80, -166, 80, -90, '#2f3437', 1.5) + R(74, -92, 12, 8, '#e2463b')
    return G(g, f'translate({x},{base}) scale({s})')

def dump_truck(cx, base, s=1, col='#f3c234'):
    return G(R(-80, -60, 100, 40, col, 3) + Pa('M-84,-64 L24,-64 L20,-54 L-80,-54 Z', shade(col, -.15)) + R(24, -60, 40, 40, '#3c7fc1', 4) + R(30, -54, 22, 16, '#9fd0ec', 2) + R(-84, -22, 152, 8, '#5d6469') + wheel(-56, -12, 14) + wheel(-24, -12, 14) + wheel(44, -12, 14), f'translate({cx},{base}) scale({s})')

def digger(cx, base, s=1):
    return G(R(-60, -24, 90, 16, '#2f3437', 8) + ''.join(Ci(-52 + k * 15, -16, 5, '#5d6469') for k in range(7)) + R(-50, -60, 70, 36, '#f3c234', 4) + R(-20, -86, 36, 30, '#f3c234', 3) + R(-14, -80, 24, 20, '#9fd0ec') + St('M16,-60 L60,-110 L96,-60', '#f3c234', 12) + Pa('M86,-62 L110,-62 L104,-36 L84,-46 Z', '#5d6469'), f'translate({cx},{base}) scale({s})')

def dozer(cx, base, s=1):
    return G(R(-60, -24, 100, 20, '#2f3437', 10) + ''.join(Ci(-52 + k * 15, -14, 5, '#5d6469') for k in range(7)) + R(-50, -60, 80, 36, '#f3c234', 4) + R(-30, -94, 40, 36, '#f3c234', 3) + R(-24, -88, 28, 24, '#9fd0ec') + St('M30,-40 L56,-30', '#5d6469', 6) + Pa('M52,-70 Q66,-40 56,-4 L70,-4 L70,-70 Z', '#8a9196'), f'translate({cx},{base}) scale({s})')

def ibeam(x, y, w, h=16, col='#8a9196'):
    return R(x, y, w, h * .25, col) + R(x, y + h * .75, w, h * .25, col) + R(x, y + h * .25, w, h * .5, shade(col, -.2))

def soldier(x, ground, s=1, arms='down', legs='stand', col='#5a6a3a', hat='mil'):
    return W(x, ground, s, col, shade(col, -.1), hat, col, arms, legs)

def tank_(cx, base, s=1, col='#5a6a3a'):
    return G(R(-80, -30, 160, 28, '#2f3437', 14) + ''.join(Ci(-66 + k * 22, -16, 9, '#5d6469') for k in range(7)) + Pa('M-76,-30 L-66,-54 L66,-54 L76,-30 Z', col) + R(-36, -78, 64, 26, shade(col, -.1), 10) + R(24, -70, 80, 8, shade(col, -.2), 3), f'translate({cx},{base}) scale({s})')

def ship_(cx, base, s=1, col='#7a8a96'):
    return G(Pa('M-90,-30 L90,-30 L70,0 L-80,0 Z', col) + R(-40, -56, 60, 26, shade(col, .1)) + R(-20, -76, 30, 20, shade(col, .1)) + L(-5, -76, -5, -100, '#5d6469', 3) + R(30, -40, 40, 8, '#5d6469') + L(70, -36, 90, -42, '#5d6469', 4) + ''.join(Ci(-30 + k * 14, -44, 3, '#2f3437') for k in range(4)), f'translate({cx},{base}) scale({s})')

def jet(cx, cy, s=1, rot=0, col='#8a9196'):
    return G(Pa('M-60,0 L50,-6 Q70,0 50,6 Z', col) + Pa('M-10,-4 L-30,-44 L-16,-44 L16,-4 Z', shade(col, -.15)) + Pa('M-10,4 L-30,44 L-16,44 L16,4 Z', shade(col, -.15)) + Pa('M-50,-2 L-64,-20 L-56,-20 L-40,-2 Z', shade(col, -.2)) + E(30, -3, 10, 4, '#3c7fc1'), f'translate({cx},{cy}) rotate({rot}) scale({s})')

def medal_(x, y, s=1, col='#d9a33a', rib='#e2463b'):
    return G(Pa('M-14,-50 L14,-50 L8,-10 L-8,-10 Z', rib) + R(-14, -50, 9, 40, '#3c7fc1') + Ci(0, 10, 22, col) + Ci(0, 10, 16, shade(col, .15)) + star(0, 10, 10, shade(col, -.15)), f'translate({x},{y}) scale({s})')

def flag_(x, y, s=1, col='#3c7fc1', col2='#ffffff'):
    return G(R(-3, 0, 6, 150, '#8a9196') + Ci(0, -2, 5, '#d9a33a') + Pa('M3,6 Q30,-4 60,8 T110,8 L110,66 Q80,56 60,66 T3,64 Z', col) + Pa('M3,24 Q30,14 60,26 T110,26 L110,42 Q80,32 60,44 T3,40 Z', col2), f'translate({x},{y}) scale({s})')


NIGHT = '#24304f'
def moon(x, y, r, col='#f6efe0'):
    return Pa(f'M{x},{y-r} A{r},{r} 0 1,0 {x+r},{y+r*.3} A{r*.8},{r*.8} 0 1,1 {x},{y-r} Z', col)
def sun(x, y, r, col='#f3c234', rays=True):
    g = Ci(x, y, r, col)
    if rays: g += ''.join(L(x + (r + 6) * math.cos(a), y + (r + 6) * math.sin(a), x + (r + 16) * math.cos(a), y + (r + 16) * math.sin(a), col, 4) for a in [k * .785 for k in range(8)])
    return g
def stars(pts, s=4):
    return ''.join(star(x, y, s, '#ffffff') for x, y in pts)
def hourglass(x, y, s=1):
    return G(Pa('M-20,-34 L20,-34 L4,0 L20,34 L-20,34 L-4,0 Z', '#dff1fb', 'stroke="#8a5a35" stroke-width="3"') + Pa('M-12,-26 L12,-26 L2,-6 L-2,-6 Z', '#e8c060') + Pa('M-14,30 L14,30 L0,16 Z', '#e8c060') + R(-24, -40, 48, 8, '#8a5a35', 3) + R(-24, 32, 48, 8, '#8a5a35', 3), f'translate({x},{y}) scale({s})')
def wedge_clock(cx, cy, r, a0, a1, col='#5aa1d4', hm=(12, 0)):
    """shade angle range in minutes (0-60)"""
    t0 = math.radians(a0 * 6 - 90); t1 = math.radians(a1 * 6 - 90)
    large = 1 if (a1 - a0) > 30 else 0
    g = Ci(cx, cy, r, '#ffffff', 'stroke="#2f3437" stroke-width="6"')
    if a1 - a0 >= 60: g += Ci(cx, cy, r - 4, col)
    else: g += Pa(f'M{cx},{cy} L{cx+(r-4)*math.cos(t0)},{cy+(r-4)*math.sin(t0)} A{r-4},{r-4} 0 {large},1 {cx+(r-4)*math.cos(t1)},{cy+(r-4)*math.sin(t1)} Z', col)
    g += ''.join(L(cx + (r - 6) * math.cos(k * math.pi / 6), cy + (r - 6) * math.sin(k * math.pi / 6), cx + (r - 14) * math.cos(k * math.pi / 6), cy + (r - 14) * math.sin(k * math.pi / 6), '#2f3437', 3) for k in range(12))
    h, m = hm
    ha = math.radians((h % 12 + m / 60) * 30 - 90); ma = math.radians(m * 6 - 90)
    g += L(cx, cy, cx + r * .45 * math.cos(ha), cy + r * .45 * math.sin(ha), '#2f3437', 6) + L(cx, cy, cx + r * .72 * math.cos(ma), cy + r * .72 * math.sin(ma), '#2f3437', 4) + Ci(cx, cy, 5, '#e2463b')
    return g
def week_strip(hl, col='#e2463b', y=70):
    days = '一二三四五六日'
    g = ''
    for k in range(7):
        x = 12 + k * 26
        on = k in (hl if isinstance(hl, (list, tuple)) else [hl])
        g += R(x, y, 24, 60, col if on else '#ffffff', 4, '' if on else 'stroke="#c4cbd0" stroke-width="2"') + T(x + 12, y + 38, days[k], 16, '#ffffff' if on else '#5d6469', 900)
    return g

def factory(x, base, w, h, col='#c0603a'):
    g = R(x, base - h, w, h, col)
    n = 3
    for k in range(n):
        g += Pa(f'M{x+k*w/n},{base-h} L{x+(k+1)*w/n},{base-h} L{x+(k+1)*w/n},{base-h-h*.4} Z', shade(col, -.1))
    g += R(x + w * .75, base - h * 1.9, w * .12, h * .9, '#8a9196') + ''.join(Ci(x + w * .81 + k * 10, base - h * 2 - k * 14, 10 + k * 3, '#c4cbd0', 'opacity=".8"') for k in range(3))
    g += ''.join(R(x + 8 + k * (w - 16) / 4, base - h * .6, (w - 16) / 4 - 8, h * .3, '#f3e070') for k in range(4))
    return g

def piggy(cx, cy, s=1, col='#ef8fa4'):
    return G(E(0, 0, 60, 46, col) + Ci(-50, -8, 16, col) + E(-62, -6, 10, 12, shade(col, -.1)) + Ci(-66, -10, 2.5, '#a8506a') + Ci(-66, -2, 2.5, '#a8506a') + Ci(-36, -18, 4, '#2f3437') + Pa('M-30,-40 L-20,-60 L-10,-40 Z', col) + R(-36, 36, 14, 22, col, 4) + R(20, 36, 14, 22, col, 4) + R(-10, -46, 30, 6, shade(col, -.3), 3) + St('M60,0 q14,-4 10,-14', col, 4), f'translate({cx},{cy}) scale({s})')

def umbrella(cx, cy, r, col='#e2463b'):
    return Pa(f'M{cx-r},{cy} Q{cx-r},{cy-r} {cx},{cy-r} Q{cx+r},{cy-r} {cx+r},{cy} Q{cx+r*.75},{cy-r*.15} {cx+r*.5},{cy} Q{cx+r*.25},{cy-r*.15} {cx},{cy} Q{cx-r*.25},{cy-r*.15} {cx-r*.5},{cy} Q{cx-r*.75},{cy-r*.15} {cx-r},{cy} Z', col) + L(cx, cy - r, cx, cy + r * .8, '#5d6469', 4) + St(f'M{cx},{cy+r*.8} q0,10 -10,10', '#5d6469', 4)

def coins(x, base, n, r=16):
    return ''.join(E(x, base - k * 7, r, r * .4, '#d9a33a') + E(x, base - k * 7 - 2, r, r * .4, '#f3c234') for k in range(n))

def table_top(cx, cy, rx, ry, col=WOOD):
    return E(cx, cy, rx, ry, col)

def podium(cx, base, w=60, col='#8a5a35'):
    return Pa(f'M{cx-w/2},{base} L{cx-w*.4},{base-w*1.1} L{cx+w*.4},{base-w*1.1} L{cx+w/2},{base} Z', col) + R(cx - w * .55, base - w * 1.2, w * 1.1, 10, shade(col, -.15), 3)

def screen_proj(x, y, w, h, inner=''):
    return R(x - 4, y - 8, w + 8, 8, '#5d6469', 3) + R(x, y, w, h, '#ffffff') + inner

def org_box(x, y, col):
    return R(x - 18, y - 12, 36, 24, col, 4) + Ci(x, y - 2, 5, '#ffffff') + Pa(f'M{x-8},{y+10} Q{x},{y} {x+8},{y+10} Z', '#ffffff')


A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)
def dump():
    import os, sys
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for k, v in A.items(): open(os.path.join(out, k + '.svg'), 'w').write(v)
    print(len(A), 'drawn')

# ---- full-figure worker with hats ----
def hat_(kind, hx, hy, r, col=None):
    if kind == 'hard': return hardhat(hx, hy, r, col or '#f3c234')
    if kind == 'cap':
        c = col or '#2f4a7a'
        return Pa(f'M{hx-r},{hy-r*.25} Q{hx-r},{hy-r*1.25} {hx},{hy-r*1.2} Q{hx+r},{hy-r*1.25} {hx+r},{hy-r*.25} Z', c) + Pa(f'M{hx+r*.2},{hy-r*.35} L{hx+r*1.7},{hy-r*.2} L{hx+r*.9},{hy-r*.05} Z', shade(c, -.2))
    if kind == 'peak':
        c = col or '#2f4a7a'
        return Pa(f'M{hx-r*1.1},{hy-r*.45} L{hx+r*1.1},{hy-r*.45} L{hx+r*1.25},{hy-r*1.25} Q{hx},{hy-r*1.55} {hx-r*1.25},{hy-r*1.25} Z', c) + R(hx - r * 1.15, hy - r * .6, r * 2.3, r * .3, '#1a2a3a', 2) + Ci(hx, hy - r * .95, r * .2, '#f3c234')
    if kind == 'mil':
        c = col or '#5a6a3a'
        return Pa(f'M{hx-r*1.2},{hy-r*.05} Q{hx-r*1.2},{hy-r*1.35} {hx},{hy-r*1.35} Q{hx+r*1.2},{hy-r*1.35} {hx+r*1.2},{hy-r*.05} Z', c) + R(hx - r * 1.3, hy - r * .2, r * 2.6, r * .25, shade(c, -.2), r * .1)
    if kind == 'straw':
        c = col or '#e8c870'
        return E(hx, hy - r * .55, r * 1.9, r * .4, c) + Pa(f'M{hx-r*.85},{hy-r*.55} Q{hx-r*.8},{hy-r*1.5} {hx},{hy-r*1.5} Q{hx+r*.8},{hy-r*1.5} {hx+r*.85},{hy-r*.55} Z', c) + R(hx - r * .85, hy - r * .8, r * 1.7, r * .25, '#e2463b')
    if kind == 'sailor':
        return E(hx, hy - r * .8, r * 1.0, r * .35, '#ffffff') + R(hx - r * .9, hy - r * .85, r * 1.8, r * .25, '#2f4a7a')
    if kind == 'beret':
        c = col or '#e2463b'
        return E(hx - r * .2, hy - r * .8, r * 1.2, r * .5, c) + Ci(hx - r * .2, hy - r * 1.3, r * .15, c)
    if kind == 'chef':
        return R(hx - r * .8, hy - r * 1.2, r * 1.6, r * .5, '#ffffff') + Ci(hx - r * .5, hy - r * 1.5, r * .5, '#ffffff') + Ci(hx + r * .5, hy - r * 1.5, r * .5, '#ffffff') + Ci(hx, hy - r * 1.8, r * .6, '#ffffff')
    return ''

def W(x, ground, s=1, shirt='#3c7fc1', pants='#3b4a5a', hat='', hatcol=None, arms='down', legs='stand', style='short', hair='#3a2a20', coat=None, mood='smile'):
    hx, hy, hr = x, ground - 153 * s, 15 * s
    return person(x, ground, shirt=shirt, pants=pants, hair=hair, style=style, arms=arms, legs=legs, s=s, coat=coat, mood=mood, extra_top=hat_(hat, hx, hy, hr, hatcol))

def hands(x, ground, s, arms):
    """returns (left_hand, right_hand) positions"""
    tw = 34 * s; sh = ground - 129 * s; hip = ground - 70 * s; hy = ground - 153 * s
    return {'down': ((x - tw/2 - 4*s, hip + 2*s), (x + tw/2 + 4*s, hip + 2*s)),
            'front': ((x - 4*s, sh + 36*s), (x + 6*s, sh + 32*s)),
            'up': ((x - tw/2 - 14*s, hy - 22*s), (x + tw/2 + 14*s, hy - 22*s)),
            'wave': ((x - tw/2 - 4*s, hip + 2*s), (x + tw/2 + 20*s, hy - 12*s)),
            'hips': ((x - tw/2 + 2*s, hip - 4*s), (x + tw/2 - 2*s, hip - 4*s))}[arms]

def vest(x, ground, s, col='#f08a24'):
    sh = ground - 129 * s; hip = ground - 70 * s; tw = 34 * s
    return Pa(f'M{x-tw/2},{sh+2*s} L{x-5*s},{sh} L{x-3*s},{hip+4*s} L{x-tw/2+2*s},{hip+4*s} Z', col) + Pa(f'M{x+tw/2},{sh+2*s} L{x+5*s},{sh} L{x+3*s},{hip+4*s} L{x+tw/2-2*s},{hip+4*s} Z', col) + R(x - tw / 2 + 1 * s, sh + 30 * s, tw - 2 * s, 4 * s, '#f3f3c0') + R(x - tw / 2 + 1 * s, sh + 44 * s, tw - 2 * s, 4 * s, '#f3f3c0')
