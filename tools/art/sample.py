from flat import *

A = {}

# ================= 水果 =================
def apple(cx=100, cy=112, s=1.0, col='#d93a33'):
    g = Pa(f'M{cx},{cy-48*s} C{cx+30*s},{cy-62*s} {cx+62*s},{cy-40*s} {cx+58*s},{cy+2*s} C{cx+54*s},{cy+44*s} {cx+28*s},{cy+64*s} {cx+8*s},{cy+56*s} Q{cx},{cy+52*s} {cx-8*s},{cy+56*s} C{cx-28*s},{cy+64*s} {cx-54*s},{cy+44*s} {cx-58*s},{cy+2*s} C{cx-62*s},{cy-40*s} {cx-30*s},{cy-62*s} {cx},{cy-48*s} Z', col)
    g += Pa(f'M{cx+20*s},{cy-50*s} C{cx+50*s},{cy-50*s} {cx+62*s},{cy-20*s} {cx+56*s},{cy+12*s} C{cx+50*s},{cy+44*s} {cx+28*s},{cy+62*s} {cx+8*s},{cy+56*s} C{cx+34*s},{cy+30*s} {cx+40*s},{cy-10*s} {cx+20*s},{cy-50*s} Z', shade(col, -.2))
    g += hi(cx - 30 * s, cy - 18 * s, 9 * s, 18 * s, .4, 20)
    g += St(f'M{cx},{cy-44*s} Q{cx+2*s},{cy-62*s} {cx+8*s},{cy-72*s}', '#6b4423', 5 * s)
    g += leaf(cx + 6 * s, cy - 62 * s, 34 * s, 12 * s, -20, '#5ba644')
    return g
A['apple'] = svg(apple())

def banana(x, y, rot, s=1, col='#f3c534'):
    d = 'M0,0 C10,40 50,62 96,52 C100,51 102,56 98,58 C50,76 4,52 -6,6 Z'
    return G(Pa(d, col) + Pa('M-6,6 C4,52 50,76 98,58 C60,64 18,48 -6,6 Z', shade(col, -.18)) +
             Pa('M-6,6 L-9,-6 L0,-6 L0,0 Z', '#7a5a2a') + Ci(98, 55, 3.5, '#4a3a20'), f'translate({x},{y}) rotate({rot}) scale({s})')
A['banana'] = svg(banana(40, 40, 10, 1.15) + banana(48, 50, 25, 1.1) + banana(58, 58, 40, 1.05))

def orange_fruit(cx, cy, r):
    g = Ci(cx, cy, r, '#f08a1c') + Pa(f'M{cx+r*.2},{cy-r*.98} A{r},{r} 0 0,1 {cx+r*.2},{cy+r*.98} A{r*.8},{r} 0 0,0 {cx+r*.2},{cy-r*.98} Z', '#d9700f')
    g += ''.join(Ci(cx + r * .6 * math.cos(a), cy + r * .6 * math.sin(a), 1.4, '#e07a10') for a in [i * .7 for i in range(9)])
    g += hi(cx - r * .4, cy - r * .35, r * .18, r * .28, .45, 30) + Ci(cx, cy - r * .92, 4, '#6b8a2a')
    return g
def orange_half(cx, cy, r):
    g = Ci(cx, cy, r, '#f08a1c') + Ci(cx, cy, r * .86, '#fff1d6') + Ci(cx, cy, r * .78, '#f7a43a')
    for i in range(10):
        a = i * math.pi / 5
        g += L(cx, cy, cx + r * .78 * math.cos(a), cy + r * .78 * math.sin(a), '#fff1d6', 2.5)
    return g + Ci(cx, cy, 4, '#fff1d6')
A['orange'] = svg(orange_fruit(84, 108, 52) + leaf(84, 58, 30, 10, -40, '#4e9a3a') + orange_half(146, 142, 34))

def grapes(cx=100, cy=70, col='#6b3a8a'):
    pos = [(0, 0), (-22, 4), (22, 4), (-33, 26), (-11, 26), (11, 26), (33, 26), (-22, 48), (0, 48), (22, 48), (-11, 70), (11, 70), (0, 92)]
    g = St(f'M{cx},{cy-6} Q{cx+4},{cy-30} {cx+16},{cy-40}', '#6b4423', 5) + leaf(cx + 8, cy - 26, 44, 18, -30, '#5ba644')
    for x, y in pos:
        g += Ci(cx + x, cy + y + 10, 13, col) + Ci(cx + x + 3, cy + y + 13, 10, shade(col, -.15)) + hi(cx + x - 4, cy + y + 5, 3, 5, .5, 30)
    return g
A['grape'] = svg(grapes())

def pear(cx=100, cy=110, col='#b7c93a'):
    d = f'M{cx},{cy-62} C{cx+14},{cy-62} {cx+18},{cy-40} {cx+24},{cy-16} C{cx+52},{cy+8} {cx+52},{cy+66} {cx},{cy+68} C{cx-52},{cy+66} {cx-52},{cy+8} {cx-24},{cy-16} C{cx-18},{cy-40} {cx-14},{cy-62} {cx},{cy-62} Z'
    g = Pa(d, col) + Pa(f'M{cx+10},{cy-58} C{cx+20},{cy-40} {cx+22},{cy-18} {cx+30},{cy-10} C{cx+52},{cy+14} {cx+48},{cy+62} {cx},{cy+68} C{cx+30},{cy+40} {cx+30},{cy} {cx+10},{cy-58} Z', shade(col, -.15))
    g += hi(cx - 20, cy + 20, 8, 18, .35, 10) + St(f'M{cx},{cy-58} Q{cx+4},{cy-74} {cx+10},{cy-80}', '#6b4423', 5) + leaf(cx + 6, cy - 70, 30, 10, -10, '#5ba644')
    return g
A['pear'] = svg(pear())

def peach(cx=100, cy=112, r=56):
    g = Ci(cx, cy, r, '#f7b47a') + Pa(f'M{cx-r*.2},{cy-r} A{r},{r} 0 0,1 {cx+r*.85},{cy+r*.5} A{r*.9},{r*.9} 0 0,0 {cx-r*.2},{cy-r} Z', '#ef7a6a')
    g += Pa(f'M{cx-r*.1},{cy+r*.1} A{r},{r} 0 0,0 {cx-r*.6},{cy+r*.8} A{r},{r} 0 0,1 {cx-r*.1},{cy+r*.1}', 'none') + St(f'M{cx},{cy-r*.92} Q{cx-r*.35},{cy} {cx-r*.05},{cy+r*.95}', '#e06a5a', 3)
    g += hi(cx - r * .45, cy - r * .3, r * .14, r * .26, .4, 25) + leaf(cx + 4, cy - r * .95, 36, 13, -30, '#5ba644')
    return g
A['peach'] = svg(peach())

def watermelon():
    g = Pa('M20,86 A80,80 0 0,0 180,86 Z', '#3f8f34') + Pa('M28,86 A72,72 0 0,0 172,86 Z', '#e9f2c8') + Pa('M34,86 A66,66 0 0,0 166,86 Z', '#e8433f')
    g += Pa('M20,86 L180,86', 'none')
    for x, y in [(60, 104), (82, 116), (104, 120), (126, 114), (146, 102), (90, 98), (118, 98), (72, 130), (102, 138), (130, 130)]:
        g += E(x, y, 3, 5, '#2a1a12')
    g += hi(60, 92, 20, 4, .3)
    g += Pa('M30,86 Q100,70 170,86', 'none')
    return G(g, 'translate(0,20)')
A['watermelon'] = svg(watermelon())

def strawberry(cx=100, cy=112, s=1.0):
    d = f'M{cx},{cy+62*s} C{cx-40*s},{cy+40*s} {cx-56*s},{cy-10*s} {cx-44*s},{cy-36*s} C{cx-30*s},{cy-60*s} {cx+30*s},{cy-60*s} {cx+44*s},{cy-36*s} C{cx+56*s},{cy-10*s} {cx+40*s},{cy+40*s} {cx},{cy+62*s} Z'
    g = Pa(d, '#e0302e') + Pa(f'M{cx+30*s},{cy-50*s} C{cx+56*s},{cy-30*s} {cx+50*s},{cy+30*s} {cx},{cy+62*s} C{cx+30*s},{cy+30*s} {cx+40*s},{cy-10*s} {cx+30*s},{cy-50*s} Z', '#bf2422')
    for i, (x, y) in enumerate([(-28, -24), (-8, -30), (14, -28), (32, -18), (-36, 0), (-16, -6), (6, -8), (26, 2), (-22, 22), (0, 18), (20, 24), (-8, 40), (10, 42)]):
        g += E(cx + x * s, cy + y * s, 2 * s, 3 * s, '#f6d47a')
    for a in [-70, -35, 0, 35, 70, 110, 145]:
        g += leaf(cx, cy - 46 * s, 26 * s, 8 * s, a - 90, '#4e9a3a')
    g += St(f'M{cx},{cy-50*s} L{cx+4*s},{cy-66*s}', '#4e8a2a', 4 * s) + hi(cx - 24 * s, cy - 14 * s, 6 * s, 12 * s, .35, 20)
    return g
A['strawberry'] = svg(strawberry())

def lemon(cx, cy, s=1):
    d = f'M{cx-62*s},{cy} Q{cx-54*s},{cy-40*s} {cx},{cy-42*s} Q{cx+54*s},{cy-40*s} {cx+62*s},{cy} Q{cx+54*s},{cy+40*s} {cx},{cy+42*s} Q{cx-54*s},{cy+40*s} {cx-62*s},{cy} Z'
    g = Pa(d, '#f5d33a') + Pa(f'M{cx-62*s},{cy} Q{cx-50*s},{cy+38*s} {cx},{cy+42*s} Q{cx+54*s},{cy+40*s} {cx+62*s},{cy} Q{cx+40*s},{cy+26*s} {cx},{cy+26*s} Q{cx-40*s},{cy+24*s} {cx-62*s},{cy} Z', '#e3b81e')
    return g + hi(cx - 18 * s, cy - 20 * s, 18 * s, 6 * s, .45, -8)
def lemon_slice(cx, cy, r):
    g = Ci(cx, cy, r, '#f5d33a') + Ci(cx, cy, r * .86, '#fffbe0') + Ci(cx, cy, r * .76, '#fbe470')
    for i in range(8):
        a = i * math.pi / 4
        g += L(cx, cy, cx + r * .76 * math.cos(a), cy + r * .76 * math.sin(a), '#fffbe0', 2.5)
    return g
A['lemon'] = svg(lemon(90, 104) + lemon_slice(150, 148, 30))

def cherry():
    g = St('M70,128 Q80,70 118,40', '#6b4423', 4) + St('M130,132 Q126,80 118,40', '#6b4423', 4) + leaf(118, 40, 46, 16, -10, '#5ba644')
    for cx, cy in [(68, 140), (132, 142)]:
        g += Ci(cx, cy, 26, '#c8202a') + Ci(cx + 6, cy + 4, 20, '#a3141e') + hi(cx - 9, cy - 9, 5, 8, .5, 30)
    return g
A['cherry'] = svg(cherry())

def mango(cx=100, cy=112):
    d = f'M{cx-56},{cy+10} C{cx-60},{cy-40} {cx-10},{cy-62} {cx+30},{cy-48} C{cx+66},{cy-34} {cx+64},{cy+30} {cx+30},{cy+52} C{cx},{cy+70} {cx-52},{cy+56} {cx-56},{cy+10} Z'
    g = Pa(d, '#f6b52e') + Pa(f'M{cx+30},{cy-48} C{cx+66},{cy-34} {cx+64},{cy+30} {cx+30},{cy+52} C{cx+44},{cy+10} {cx+40},{cy-20} {cx+30},{cy-48} Z', '#e8901c')
    g += Pa(f'M{cx-56},{cy+10} C{cx-60},{cy-40} {cx-10},{cy-62} {cx+30},{cy-48} C{cx-4},{cy-40} {cx-34},{cy-20} {cx-56},{cy+10} Z', '#ef5a3a', 'opacity=".75"')
    g += hi(cx - 14, cy - 24, 16, 7, .4, -25) + St(f'M{cx+28},{cy-48} Q{cx+34},{cy-62} {cx+44},{cy-68}', '#6b4423', 5) + leaf(cx + 40, cy - 64, 36, 12, 10, '#4e9a3a')
    return g
A['mango'] = svg(mango())

def pineapple(cx=100, cy=126):
    g = ''
    for a, l in [(-60, 46), (-35, 56), (-12, 64), (12, 64), (35, 56), (60, 46), (-22, 50), (22, 50)]:
        g += G(Pa(f'M-7,0 Q0,{-l} 7,0 Z', '#3f8f34' if a % 2 else '#5ba644'), f'translate({cx},{cy-46}) rotate({a})')
    g += E(cx, cy, 42, 54, '#f0a92a') + Pa(f'M{cx+10},{cy-53} A42,54 0 0,1 {cx+10},{cy+53} A30,54 0 0,0 {cx+10},{cy-53} Z', '#d98a16')
    for i in range(-5, 6):
        g += L(cx - 42, cy + i * 14 - 30, cx + 42, cy + i * 14 + 30, '#b8701a', 2) + L(cx + 42, cy + i * 14 - 30, cx - 42, cy + i * 14 + 30, '#b8701a', 2)
    g = g.replace('</g>', '</g>', 1)
    clip = '<clipPath id="pc"><ellipse cx="%s" cy="%s" rx="42" ry="54"/></clipPath>' % (cx, cy)
    body = E(cx, cy, 42, 54, '#f0a92a') + Pa(f'M{cx+10},{cy-53} A42,54 0 0,1 {cx+10},{cy+53} A30,54 0 0,0 {cx+10},{cy-53} Z', '#d98a16')
    hatch = ''.join(L(cx - 60, cy + i * 14 - 40, cx + 60, cy + i * 14 + 40, '#b8701a', 2) + L(cx + 60, cy + i * 14 - 40, cx - 60, cy + i * 14 + 40, '#b8701a', 2) for i in range(-7, 8))
    crown = ''.join(G(Pa(f'M-7,0 Q0,{-l} 7,0 Z', c), f'translate({cx},{cy-46}) rotate({a})') for a, l, c in [(-60, 46, '#3f8f34'), (-35, 58, '#5ba644'), (-12, 66, '#3f8f34'), (12, 66, '#5ba644'), (35, 58, '#3f8f34'), (60, 46, '#5ba644'), (0, 72, '#3f8f34')])
    return crown + clip + body + f'<g clip-path="url(#pc)">{hatch}</g>' + hi(cx - 18, cy - 10, 6, 20, .25, 10)
A['pineapple'] = svg(pineapple())

def kiwi():
    g = E(70, 110, 46, 54, '#8a6232') + E(78, 112, 38, 52, '#7a5428')
    g += ''.join(L(50 + (i * 7) % 50, 70 + (i * 13) % 80, 52 + (i * 7) % 50, 74 + (i * 13) % 80, '#a07a48', 1.5) for i in range(30))
    g += E(132, 128, 46, 42, '#8a6232') + E(132, 128, 40, 36, '#7fb83a') + E(132, 128, 30, 26, '#a6d45a') + E(132, 128, 12, 10, '#f3f6dc')
    for i in range(16):
        a = i * math.pi / 8
        g += E(132 + 19 * math.cos(a), 128 + 16 * math.sin(a), 1.6, 3, '#2a2a1a', f'transform="rotate({a*57.3+90} {132+19*math.cos(a)} {128+16*math.sin(a)})"')
    return g
A['kiwi'] = svg(kiwi())

def plum(cx, cy, r):
    g = Ci(cx, cy, r, '#6b2a5a') + Pa(f'M{cx+r*.2},{cy-r*.98} A{r},{r} 0 0,1 {cx+r*.2},{cy+r*.98} A{r*.8},{r} 0 0,0 {cx+r*.2},{cy-r*.98} Z', '#521c45')
    g += St(f'M{cx-r*.1},{cy-r*.9} Q{cx-r*.35},{cy} {cx},{cy+r*.95}', '#4a1640', 2.5) + hi(cx - r * .45, cy - r * .3, r * .14, r * .26, .3, 25)
    return g + St(f'M{cx},{cy-r*.95} L{cx+4},{cy-r*1.25}', '#6b4423', 4)
A['plum'] = svg(plum(78, 118, 44) + plum(134, 128, 38) + leaf(84, 72, 34, 12, -40, '#5ba644'))

def melon():
    body = E(84, 108, 58, 50, '#e8c66a') + Pa('M110,62 A58,50 0 0,1 110,154 A44,50 0 0,0 110,62 Z', '#d4ac4c')
    net = ''.join(St(f'M{20+i*12},40 Q{40+i*12},108 {16+i*12},176', '#f6e9c0', 2.2) for i in range(12))
    net += ''.join(St(f'M10,{50+i*12} Q84,{40+i*12} 160,{58+i*12}', '#f6e9c0', 2.2) for i in range(11))
    g = '<clipPath id="mc"><ellipse cx="84" cy="108" rx="58" ry="50"/></clipPath>' + body + f'<g clip-path="url(#mc)">{net}</g>' + hi(60, 86, 14, 7, .35, -20)
    g += Pa('M112,172 Q146,96 184,118 Q178,168 112,172 Z', '#f0a24a') + Pa('M112,172 Q178,168 184,118 L190,121 Q186,178 112,178 Z', '#8fb04a') + Pa('M124,164 Q150,116 174,128 Q164,154 124,164 Z', '#f6c27a', 'opacity=".7"')
    return g
A['melon'] = svg(melon())

def ripe():
    g = G(banana(0, 0, 30, .75, '#9cc23a'), 'translate(18,58)')
    g += St('M86,104 L114,104', '#7a7f82', 6) + Pa('M110,94 L124,104 L110,114 Z', '#7a7f82')
    g += G(banana(0, 0, 30, .75, '#f3c534'), 'translate(118,58)')
    g += Ci(160, 150, 18, '#5ba644') + St('M151,150 L158,157 L170,143', '#fff', 5)
    return g
A['ripe'] = svg(ripe())

# ================= 看医生 =================
def stetho_neck(cx, sh_y, s=1):
    return (St(f'M{cx-12*s},{sh_y-2*s} Q{cx-14*s},{sh_y+28*s} {cx-2*s},{sh_y+38*s}', '#4a5157', 3.5 * s) +
            St(f'M{cx+12*s},{sh_y-2*s} Q{cx+10*s},{sh_y+18*s} {cx+4*s},{sh_y+30*s}', '#4a5157', 3.5 * s) + Ci(cx - 2 * s, sh_y + 40 * s, 5 * s, '#a7adb1'))

A['doctor'] = svg(person(100, 182, shirt='#7fb3d8', pants='#3b4a5a', coat='#ffffff', style='grey', arms='front', s=1.0,
                          extra_top='') + stetho_neck(100, 56) + R(110, 66, 12, 7, '#3c7fc1', 2) +
                  R(76, 76, 30, 38, '#c58b54', 3) + R(80, 82, 22, 28, '#ffffff', 1) + L(84, 90, 98, 90, '#a7adb1', 2) + L(84, 96, 98, 96, '#a7adb1', 2) + L(84, 102, 94, 102, '#a7adb1', 2))
nurse_cap = R(86, 18, 28, 12, '#ffffff', 3) + R(97, 20, 6, 8, '#d9453a') + R(96, 21, 8, 6, '#d9453a')
A['nurse'] = svg(person(100, 182, shirt='#4bb3a8', pants='#4bb3a8', style='bun', hair='#5a3a2a', arms='front', mood='smile') +
                 R(86, 13, 28, 11, '#ffffff', 3) + R(97.5, 14.5, 5, 8, '#d9453a') + R(96, 16, 8, 5, '#d9453a') +
                 R(90, 84, 22, 4, '#2f3437', 2) + R(92, 70, 10, 8, '#ffffff', 1))

def bottle(cx, base, w=56, h=86, glass='#a8541c', label='#ffffff', cap='#ffffff'):
    g = R(cx - w / 2, base - h, w, h, glass, 10) + R(cx - w / 2 + w * .62, base - h + 6, w * .3, h - 12, shade(glass, -.2), 6)
    g += R(cx - w * .32, base - h - 12, w * .64, 16, shade(glass, -.1), 3) + R(cx - w * .38, base - h - 30, w * .76, 22, cap, 4) + R(cx - w * .38, base - h - 14, w * .76, 4, shade(cap, -.12), 1)
    g += R(cx - w / 2 + 4, base - h * .66, w - 8, h * .44, label, 3)
    return g
A['medicine'] = svg(bottle(84, 172) + G(R(-9, -9, 18, 18, '#d9453a', 1) , 'translate(84,135)') + R(78, 126, 12, 18, '#ffffff') + R(75, 129, 18, 12, '#ffffff') + R(81, 129, 6, 12, '#d9453a') + R(78, 132, 12, 6, '#d9453a') +
                    pill(146, 160, 40, 16, '#3c7fc1', '#ffffff', -25) + Ci(140, 128, 10, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + L(134, 128, 146, 128, '#d9dcde', 2))

def calendar(x, y, w, h, mark=True):
    g = R(x, y, w, h, '#ffffff', 8) + R(x, y, w, h * .24, '#d9453a', 8) + R(x, y + h * .14, w, h * .1, '#d9453a')
    g += ''.join(R(x + w * (.2 + i * .2) - 3, y - 8, 6, 18, '#5d6469', 3) for i in range(4))
    for r_ in range(4):
        for c in range(5):
            g += R(x + 12 + c * (w - 24) / 5, y + h * .32 + r_ * (h * .66) / 4.2, (w - 24) / 5 - 6, h * .1, '#e3e6e8', 2)
    if mark:
        cx_, cy_ = x + 12 + 2 * (w - 24) / 5 + (w - 24) / 10 - 3, y + h * .32 + 2 * (h * .66) / 4.2 + h * .05
        g += Ci(cx_, cy_, 13, 'none', 'stroke="#d9453a" stroke-width="4"')
    return g
def clock(cx, cy, r, hm=(10, 2)):
    g = Ci(cx, cy, r, '#2f3437') + Ci(cx, cy, r * .86, '#ffffff')
    for i in range(12):
        a = i * math.pi / 6
        g += L(cx + r * .72 * math.cos(a), cy + r * .72 * math.sin(a), cx + r * .8 * math.cos(a), cy + r * .8 * math.sin(a), '#2f3437', 2)
    h, m = hm
    g += L(cx, cy, cx + r * .4 * math.sin(h / 6 * math.pi), cy - r * .4 * math.cos(h / 6 * math.pi), '#2f3437', 4)
    g += L(cx, cy, cx + r * .6 * math.sin(m / 6 * math.pi), cy - r * .6 * math.cos(m / 6 * math.pi), '#2f3437', 3) + Ci(cx, cy, 3, '#d9453a')
    return g
A['appointment'] = svg(calendar(26, 40, 120, 120) + clock(146, 140, 34))

def chair(x, y, col):
    return R(x, y, 34, 40, col, 5) + R(x, y + 36, 34, 10, shade(col, -.15), 3) + R(x + 3, y + 46, 4, 22, '#5d6469') + R(x + 27, y + 46, 4, 22, '#5d6469')
A['waiting-room'] = svg(R(14, 40, 172, 140, '#eef1ea', 4) + R(14, 168, 172, 12, '#d6d0c2') + clock(100, 66, 18) +
                        chair(22, 104, '#3c7fc1') + chair(60, 104, '#3c7fc1') + chair(124, 104, '#3c7fc1') +
                        G(person(0, 0, shirt='#ef8fa4', pants='#3b5f8f', style='long', hair='#3a2a20', arms='down', s=.62), 'translate(141,166)') +
                        R(160, 76, 18, 98, '#c58b54', 2) + Ci(173, 124, 2, '#5d6469') + R(150, 54, 34, 14, '#ffffff', 2) + T(167, 65, 'DR', 10, '#3c7fc1'), shadow=False)

def thermometer_digital(cx, cy, rot=-30, text_='37.5'):
    g = R(-18, -70, 36, 120, '#ffffff', 18) + R(-18, -70, 36, 120, 'none', 18, 'stroke="#d9dcde" stroke-width="3"') + R(-13, 50, 26, 30, '#a7adb1', 8) + R(-4, 78, 8, 22, '#c9cfd2', 4)
    g += R(-12, -48, 24, 54, '#cfe8d0', 4) + T(0, -6, text_, 13, '#2f3437', 800, extra='transform="rotate(90 0 -20)"')
    g += Ci(0, 26, 8, '#3c7fc1')
    return G(g, f'translate({cx},{cy}) rotate({rot})')
A['temperature'] = svg(thermometer_digital(100, 92, -35) + T(150, 170, '°C', 30, '#d9453a'))

def blister(x, y, w=110, h=72, rot=-12):
    g = R(0, 0, w, h, '#d9dcde', 8) + R(4, 4, w - 8, h - 8, '#eceff0', 6)
    for r_ in range(2):
        for c in range(4):
            cx_, cy_ = 18 + c * (w - 36) / 3, 20 + r_ * (h - 40)
            g += Ci(cx_, cy_, 11, '#ffffff', 'stroke="#c4c9cc" stroke-width="2"') + hi(cx_ - 3, cy_ - 4, 4, 2, .8)
    return G(g, f'translate({x},{y}) rotate({rot})')
A['tablet'] = svg(blister(30, 66) + Ci(150, 150, 14, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + L(141, 150, 159, 150, '#d9dcde', 2.5) + Ci(120, 164, 12, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + L(112, 164, 128, 164, '#d9dcde', 2.5))

def drop(cx, cy, s, color='#9fd0ec'):
    return Pa(f'M{cx},{cy-s} Q{cx+s*.75},{cy} {cx},{cy+s*.55} Q{cx-s*.75},{cy} {cx},{cy-s} Z', color)
A['symptom'] = svg(bust(92, 84, 34, shirt='#7a9fc7', mood='sad', style='long', hair='#3a2a20') +
                   E(76, 94, 7, 4, '#ef7a7a', 'opacity=".8"') + E(108, 94, 7, 4, '#ef7a7a', 'opacity=".8"') +
                   G(R(0, -3.5, 44, 7, '#ffffff', 3.5) + Ci(2, 0, 4.5, '#d9453a') + R(14, -1.5, 20, 3, '#d9453a', 1.5), 'translate(90,101) rotate(-14)') +
                   arm([(178, 200), (170, 120), (124, 58)], '#7a9fc7', '#f1c7a3', 15) +
                   drop(66, 56, 8) + T(160, 60, '?', 34, '#d9453a'))
def drop(cx, cy, s, color='#9fd0ec'):
    return Pa(f'M{cx},{cy-s} Q{cx+s*.75},{cy} {cx},{cy+s*.55} Q{cx-s*.75},{cy} {cx},{cy-s} Z', color)

def bp_monitor(cx, cy, reading=('120', '80'), alert=False):
    g = R(cx - 46, cy - 34, 92, 68, '#f4f1ea', 12) + R(cx - 38, cy - 26, 56, 40, '#cfe8d0' if not alert else '#f6d0c8', 4)
    g += T(cx - 10, cy - 6, reading[0], 17, '#d9453a' if alert else '#2f3437', 800) + T(cx - 10, cy + 12, reading[1], 14, '#2f3437', 700)
    g += Ci(cx + 30, cy - 10, 6, '#3c7fc1') + Ci(cx + 30, cy + 10, 6, '#d9453a') + heart_s(cx + 30, cy + 26, 5)
    return g
def heart_s(cx, cy, s, col='#d9453a'):
    return Pa(f'M{cx},{cy+s*.85} C{cx-s*1.3},{cy-s*.05} {cx-s*.75},{cy-s*1.05} {cx},{cy-s*.4} C{cx+s*.75},{cy-s*1.05} {cx+s*1.3},{cy-s*.05} {cx},{cy+s*.85} Z', col)
A['blood-pressure'] = svg(R(14, 96, 86, 46, '#f1c7a3', 22) + R(30, 90, 50, 58, '#2f5a8a', 6) + R(36, 96, 38, 46, '#3c6ea0', 4) +
                          St('M80,118 Q120,150 130,120', '#4a5157', 5) + bp_monitor(140, 100))

def clipboard(x, y, w, h):
    g = R(x, y, w, h, '#c58b54', 8) + R(x + 8, y + 12, w - 16, h - 20, '#ffffff', 3) + R(x + w / 2 - 20, y - 6, 40, 18, '#a7adb1', 5)
    return g
def check(x, y, s=1, col='#5ba644'):
    return St(f'M{x},{y} L{x+6*s},{y+6*s} L{x+16*s},{y-6*s}', col, 4 * s)
A['check-up'] = svg(clipboard(46, 28, 108, 146) + ''.join(check(62, 62 + i * 26) + L(86, 60 + i * 26, 138, 60 + i * 26, '#a7adb1', 4) for i in range(4)) +
                    heart_s(138, 160, 14) + St('M30,120 Q24,170 60,176 Q80,176 84,160', '#4a5157', 5) + Ci(86, 156, 9, '#a7adb1'))

A['prescription'] = svg(G(R(0, 0, 112, 150, '#ffffff', 4) + R(0, 0, 112, 26, '#cfe3f3', 4) + R(0, 18, 112, 8, '#cfe3f3') + T(30, 66, 'Rx', 34, '#3c7fc1', 800) +
                          ''.join(L(16, 84 + i * 14, 96 - (i % 2) * 20, 84 + i * 14, '#c4c9cc', 3) for i in range(3)) + St('M54,136 q8,-12 14,0 t14,0 t12,-4', '#2f3437', 2.5), 'translate(36,24) rotate(-6)') +
                        G(R(-4, -60, 8, 92, '#2f3437', 3) + Pa('M-4,32 L0,44 L4,32 Z', '#d9a33a') + R(-4, -60, 8, 14, '#d9453a', 3), 'translate(152,118) rotate(30)'))

def syringe(cx, cy, rot, s=1, liquid='#7fc4ea'):
    g = R(-14, -50, 28, 92, '#eef6fa', 5) + R(-14, -50, 28, 92, 'none', 5, 'stroke="#a7adb1" stroke-width="3"') + R(-11, -6, 22, 45, liquid, 3)
    g += ''.join(L(-14, -40 + i * 10, -6, -40 + i * 10, '#a7adb1', 2) for i in range(8))
    g += R(-4, -84, 8, 36, '#a7adb1', 2) + R(-16, -90, 32, 8, '#5d6469', 3) + R(-20, -54, 40, 7, '#a7adb1', 3)
    g += R(-5, 42, 10, 10, '#a7adb1', 2) + L(0, 52, 0, 92, '#8a9196', 2.5)
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')
A['injection'] = svg(syringe(100, 92, 40, 1.1) + Pa('M48,154 q6,10 0,14 q-6,-4 0,-14 Z', '#7fc4ea'))

def vial(cx, base, col='#3c7fc1'):
    return (R(cx - 18, base - 64, 36, 64, '#e8f3f8', 6) + R(cx - 18, base - 40, 36, 40, '#bfe0ef', 6) + R(cx - 12, base - 74, 24, 12, '#d9dcde', 2) +
            R(cx - 16, base - 86, 32, 14, col, 4) + R(cx - 18, base - 52, 36, 18, '#ffffff', 2) + R(cx - 8, base - 48, 16, 4, col, 1) + hi(cx - 10, base - 30, 3, 12, .6))
A['vaccine'] = svg(vial(64, 172) + vial(104, 172, '#d9453a') + syringe(150, 96, 25, .9))

def stethoscope(tr='', s=1):
    g = St('M60,40 Q48,110 100,122 Q152,110 140,40', '#4a5157', 7) + Ci(60, 38, 7, '#2f3437') + Ci(140, 38, 7, '#2f3437')
    g += St('M100,122 Q100,150 118,160 Q140,170 146,148', '#4a5157', 7) + Ci(150, 140, 18, '#a7adb1') + Ci(150, 140, 12, '#d9dcde') + Ci(150, 140, 5, '#a7adb1')
    return G(g, tr) if tr else g
A['stethoscope'] = svg(stethoscope())

def xray(x, y, w, h):
    g = R(x, y, w, h, '#1f2a33', 6) + R(x + 6, y + 6, w - 12, h - 12, '#2c3e4c', 4)
    cx = x + w / 2
    g += R(cx - 3, y + 14, 6, h - 30, '#cfd8de', 3)
    for i in range(5):
        yy = y + 26 + i * 16
        g += St(f'M{cx-4},{yy} Q{cx-36},{yy-6} {cx-42},{yy+14}', '#cfd8de', 4) + St(f'M{cx+4},{yy} Q{cx+36},{yy-6} {cx+42},{yy+14}', '#cfd8de', 4)
    g += St(f'M{cx-44},{y+20} Q{cx},{y+10} {cx+44},{y+20}', '#cfd8de', 4)
    return g
A['diagnosis'] = svg(R(18, 30, 132, 128, '#e9eef1', 6) + xray(26, 38, 116, 112) + G(Ci(0, 0, 26, 'none', 'stroke="#5d6469" stroke-width="8"') + Ci(0, 0, 22, '#dff1fb', 'opacity=".55"') + R(14, 18, 12, 42, '#5d6469', 5, 'transform="rotate(-40 20 38)"'), 'translate(132,118)'))

def warn(cx, cy, s):
    return Pa(f'M{cx},{cy-s} L{cx+s*1.1},{cy+s*.85} L{cx-s*1.1},{cy+s*.85} Z', '#f3c234') + R(cx - 3, cy - s * .45, 6, s * .75, '#2f3437', 3) + Ci(cx, cy + s * .55, 3.5, '#2f3437')
A['side-effect'] = svg(bottle(62, 172, 48, 70, '#e8eef1', '#cfe3f3', '#3c7fc1') + pill(64, 130, 30, 12, '#d9453a', '#ffffff', 20) +
                       bust(138, 70, 24, shirt='#8aa86a', mood='sad', style='short', hair='#3a2a20', w=70)[0:0] +
                       headshape(140, 76, 26, mood='o', style='short') + St('M110,50 q-6,-10 4,-14 q10,4 4,14', '#7a7f82', 2.5) + St('M170,50 q6,-10 -4,-14 q-10,4 -4,14', '#7a7f82', 2.5) + warn(144, 150, 26))

import os, sys
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
