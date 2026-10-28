from kit4 import *

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

# ================= 农业 =================
S_('farm', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, FIELD) + barn_(60, 140, 70) + Ci(170, 30, 14, '#f3c234') + ''.join(R(110 + k * 18, 126, 4, 20, '#f6efe0') for k in range(5)) + R(106, 130, 84, 4, '#f6efe0') + crop_rows(150, '#4a9a3a'), False)
S_('farmer', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, FIELD) + W(90, 194, .95, '#3c7fc1', '#3b5f8f', 'straw') + R(66, 76, 48, 50, '#5a7ab8', 3, 'opacity="0"') + St('M140,40 L130,190', '#a8703e', 5) + St('M126,40 L130,24 M140,40 L140,22 M154,40 L150,24', '#8a9196', 4) + R(124, 38, 32, 6, '#8a9196', 2), False)
S_('field', R(0, 0, 200, 200, SKY) + Pa('M0,90 L200,80 L200,200 L0,200 Z', '#e8c060') + ''.join(St(f'M{-40+k*30},200 L{60+k*10},90', '#c8a040', 3) for k in range(10)) + Pa('M0,90 Q60,70 120,84 Q160,70 200,80 L200,90 L0,96 Z', '#7aaa5a') + Ci(160, 34, 14, '#f3c234'), False)
S_('tractor', tractor(100, 160, 1.2))
S_('crop', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 100, '#a8703e') + ''.join(G(St('M0,0 L0,-60', '#4a9a3a', 4) + leaf(0, -20, 26, 7, -30, '#5aaa3a') + leaf(0, -36, 24, 7, -150, '#5aaa3a') + E(4, -50, 5, 14, '#f3c234'), f'translate({20+(k%5)*40},{140+(k//5)*50}) scale({.8+(k//5)*.3})') for k in range(10)), False)
S_('wheat', ''.join(wheat_(60 + k * 20, 110 + (k % 2) * 6, 1.1, -12 + k * 6) for k in range(5)) + R(80, 150, 40, 10, '#e2463b', 3))
S_('barn', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, FIELD) + barn_(100, 170, 120), False)
S_('hay', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#c8b860') + hay_bale(60, 176, 70) + hay_bale(140, 176, 70) + hay_bale(100, 126, 70) + Pa('M150,40 L190,40 L194,46 L146,46 Z', '#ffffff', 'opacity="0"'), False)
S_('orchard', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, FIELD) + ''.join(fruit_tree(30 + k * 50, 130, .6) for k in range(4)) + ''.join(fruit_tree(20 + k * 54, 196, .9) for k in range(4)), False)
S_('paddy-field', R(0, 0, 200, 200, SKY) + ''.join(Pa(f'M0,{70+k*34} Q100,{60+k*34} 200,{70+k*34} L200,{104+k*34} Q100,{94+k*34} 0,{104+k*34} Z', ['#9fd0ec', '#8ac3e0', '#9fd0ec', '#8ac3e0'][k]) + Pa(f'M0,{100+k*34} Q100,{90+k*34} 200,{100+k*34} L200,{104+k*34} Q100,{94+k*34} 0,{104+k*34} Z', '#8a6a3a') + ''.join(St(f'M{10+j*16},{92+k*34-abs(j-6)*0} l-3,-12 M{10+j*16},{92+k*34} l3,-12 M{10+j*16},{92+k*34} l0,-14', '#5aaa3a', 2) for j in range(13)) for k in range(4)) + W(150, 140, .4, '#ffffff', '#3b5f8f', 'straw'), False)
S_('plow', R(0, 0, 200, 200, SKY) + R(0, 130, 200, 70, '#a8703e') + ''.join(St(f'M0,{150+k*14} Q100,{144+k*14} 200,{150+k*14}', '#8a5a35', 4) for k in range(4)) + G(St('M0,0 L80,-50', '#8a5a35', 6) + St('M60,-40 L80,-60 M70,-46 L92,-56', '#8a5a35', 4) + Pa('M-10,-4 L20,-6 L10,14 Z', '#8a9196'), 'translate(60,150)') + G(E(0, 0, 36, 20, '#8a6a4a') + Ci(36, -10, 12, '#8a6a4a') + L(-20, 16, -20, 34, '#6a4a2a', 6) + L(20, 16, 20, 34, '#6a4a2a', 6) + Pa('M30,-20 l-6,-10 M42,-20 l6,-10', '#f6efe0', 0) + St('M30,-20 q-4,-10 -10,-12 M42,-20 q4,-10 10,-12', '#f6efe0', 3), 'translate(30,116) scale(-1,1) translate(-160,0)'), False)
S_('scarecrow', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#e8c060') + R(96, 50, 8, 140, '#8a5a35') + R(40, 80, 120, 8, '#8a5a35') + Pa('M70,80 L130,80 L124,140 L76,140 Z', '#5a8ac8') + R(96, 96, 8, 8, '#e2463b') + R(110, 114, 10, 10, '#e2463b') + Ci(100, 60, 22, '#e8c870') + Ci(92, 58, 3, '#2f3437') + Ci(108, 58, 3, '#2f3437') + St('M92,68 L96,70 L100,68 L104,70 L108,68', '#2f3437', 2) + E(100, 40, 34, 8, '#c8a040') + Pa('M84,40 Q86,20 100,20 Q114,20 116,40 Z', '#c8a040') + ''.join(L(40 - k * 3, 84 + k * 4, 30, 90 + k * 5, '#e8c060', 2) + L(160 + k * 3, 84 + k * 4, 170, 90 + k * 5, '#e8c060', 2) for k in range(3)) + G(Pa('M0,0 L14,-6 L8,4 L18,6 L0,8 Z', '#2f3437'), 'translate(160,30)'), False)
S_('organic', Ci(100, 100, 70, '#5ba644') + Ci(100, 100, 60, 'none', 'stroke="#ffffff" stroke-width="3"') + leaf(100, 130, 70, 30, -90, '#ffffff') + St('M100,130 L100,70', '#5ba644', 3) + carrot(40, 170, .6, -30) + apple(160, 166, .6))
S_('irrigation', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#7aaa5a') + crop_rows(120, '#4a9a3a') + R(20, 60, 160, 8, '#8a9196', 3) + ''.join(R(36 + k * 40, 60, 6, 70, '#8a9196') for k in range(4)) + ''.join(drop(30 + k * 22, 90 + (k % 2) * 14, 5) for k in range(8)) + ''.join(St(f'M{40+k*40},68 q-10,20 -16,40 M{40+k*40},68 q10,20 16,40', '#9fd0ec', 2) for k in range(4)), False)
S_('pesticide', R(0, 0, 200, 200, '#dff1fb') + R(0, 150, 200, 50, FIELD) + W(60, 194, .9, '#e6dcc4', '#5d6469', 'straw') + R(30, 70, 26, 40, '#5ba644', 6) + St('M66,100 L120,90', '#2f3437', 3) + ''.join(Ci(130 + k * 10, 90 + (k % 3 - 1) * 8, 4 + k, '#dfeec8', 'opacity=".8"') for k in range(5)) + G(E(0, 0, 8, 6, '#2f3437') + L(-6, 0, -12, -6, '#2f3437', 2) + L(6, 0, 12, -6, '#2f3437', 2), 'translate(170,140)') + L(160, 130, 180, 150, '#e2463b', 4) + L(180, 130, 160, 150, '#e2463b', 4), False)
S_('vineyard', R(0, 0, 200, 200, SKY) + Pa('M0,110 Q100,70 200,100 L200,200 L0,200 Z', '#7aaa5a') + ''.join(St(f'M0,{120+k*30} Q100,{90+k*34} 200,{116+k*30}', '#4a8a3a', 10) for k in range(3)) + ''.join(G(''.join(Ci(dx, dy, 6, '#7a3a8a') for dx, dy in [(-6, 0), (6, 0), (0, 8), (-6, 14), (6, 14), (0, 22)]) + leaf(0, -4, 14, 7, -30, '#5aaa3a'), f'translate({30+k*46},{150+(k%2)*10})') for k in range(4)), False)

# ================= 建筑 =================
S_('worker', R(0, 0, 200, 200, '#e6dcc8') + W(100, 194, 1.0, '#3c7fc1', '#3b4a5a', 'hard') + vest(100, 194, 1.0) + hammer_(140, 120, .5, 30), False)
S_('hard-hat', hardhat(100, 140, 60))
S_('crane', R(0, 0, 200, 200, SKY) + crane_(60, 200, 1.0) + box_(124, 120, 30, 20, '#c8a070') + building(140, 140, 50, 60, cols=2, rows=3), False)
S_('truck', dump_truck(100, 160, 1.1))
S_('building-site', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#c8a070') + crane_(150, 160, .7) + ''.join(R(30, 60 + k * 30, 100, 6, '#8a9196') for k in range(4)) + ''.join(R(30 + k * 32, 60, 6, 100, '#8a9196') for k in range(4)) + R(0, 160, 200, 30, '#f3c234', 0, 'opacity="0"') + ''.join(R(k * 40, 168, 36, 22, ['#f08a24', '#ffffff'][k % 2]) for k in range(5)), False)
S_('cement', G(R(-50, -60, 100, 120, '#c4bcae', 10) + R(-40, -40, 80, 30, '#ffffff', 2) + R(-30, -32, 60, 14, '#8a9196', 2) + Pa('M-50,-60 L-40,-70 L40,-70 L50,-60 Z', '#a89f92'), 'translate(80,100)') + Pa('M120,170 Q150,120 190,170 Z', '#a7adb1') + spade_(160, 110, .5, 20))
S_('concrete', G(R(-80, -50, 60, 40, '#3c7fc1', 4) + R(-74, -44, 30, 18, '#9fd0ec') + E(20, -40, 50, 32, '#c4cbd0') + ''.join(St(f'M{-10+k*20},-66 q14,26 0,52', '#8a9196', 4) for k in range(3)) + R(-90, -12, 160, 8, '#5d6469') + wheel(-60, 0, 14) + wheel(30, 0, 14) + St('M68,-30 L96,-6', '#8a9196', 8), 'translate(90,150)') + Pa('M150,170 Q170,140 196,170 Z', '#a7adb1'))
S_('steel', ''.join(ibeam(30 + (k % 2) * 6, 140 - k * 22, 140, 20, ['#8a9196', '#a7adb1'][k % 2]) for k in range(5)) + ''.join(R(30 + k * 10, 160, 6, 20, '#5d6469') for k in range(0)))
S_('digger', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#a8703e') + digger(80, 164, 1.1) + Pa('M150,166 Q170,140 196,166 Z', '#8a5a35'), False)
S_('bulldozer', dozer(90, 166, 1.2))
S_('scaffolding', R(0, 0, 200, 200, SKY) + R(30, 40, 140, 160, '#c0603a') + ''.join(R(40 + (k % 4) * 34, 50 + (k // 4) * 40, 16, 20, '#9fd0ec') for k in range(16)) + ''.join(R(20 + k * 40, 30, 5, 170, '#8a9196') for k in range(5)) + ''.join(R(20, 60 + k * 40, 165, 6, '#c8903a') + R(20, 56 + k * 40, 165, 3, '#8a9196') for k in range(4)) + ''.join(L(20 + k * 40, 70, 60 + k * 40, 110, '#8a9196', 2) for k in range(4)) + W(130, 136, .3, '#3c7fc1', '#3b4a5a', 'hard'), False)
S_('road-works', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, ROAD) + ''.join(G(Pa('M-14,0 L-4,-50 L4,-50 L14,0 Z', '#f08a24') + R(-8, -34, 16, 6, '#ffffff') + R(-11, -16, 22, 6, '#ffffff') + R(-18, -2, 36, 6, '#f08a24', 2), f'translate({30+k*70},180)') for k in range(3)) + R(50, 110, 100, 18, '#ffffff', 2) + ''.join(Pa(f'M{50+k*20},110 l10,0 l-8,18 l-10,0 Z', '#e2463b') for k in range(5)) + R(60, 128, 5, 30, '#5d6469') + R(135, 128, 5, 30, '#5d6469') + G(Pa('M0,-40 L36,24 L-36,24 Z', '#e2463b') + Pa('M0,-28 L26,18 L-26,18 Z', '#ffffff') + W(0, 16, .22, '#2f3437', '#2f3437', 'hard', '#2f3437', legs='walk'), 'translate(100,60)'), False)
S_('beam', R(0, 0, 200, 200, SKY) + L(100, 0, 100, 60, '#2f3437', 2) + R(94, 56, 12, 10, '#e2463b') + L(100, 66, 40, 100, '#2f3437', 2) + L(100, 66, 160, 100, '#2f3437', 2) + ibeam(20, 100, 160, 30, '#e2463b') + building(20, 150, 160, 50, cols=6, rows=1, col='#c4bcae'), False)
S_('blueprint', G(R(-80, -60, 160, 120, '#2f5a9a', 3) + ''.join(L(-80, -60 + k * 15, 80, -60 + k * 15, '#3c6aaa', 1) for k in range(9)) + ''.join(L(-80 + k * 15, -60, -80 + k * 15, 60, '#3c6aaa', 1) for k in range(11)) + R(-50, -30, 100, 70, 'none', 0, 'stroke="#ffffff" stroke-width="3"') + L(-50, 0, 10, 0, '#ffffff', 2) + L(10, -30, 10, 40, '#ffffff', 2) + R(30, 36, 16, 4, '#2f5a9a') + Pa('M-55,-30 L0,-56 L55,-30', 'none', 'stroke="#ffffff" stroke-width="3"') + L(-50, 50, 50, 50, '#ffffff', 1.5), 'translate(100,100) rotate(-6)') + pencil_(150, 160, .5, -30))
S_('safety-vest', Pa('M60,30 L84,30 Q100,60 116,30 L140,30 L160,60 L150,80 L150,180 L50,180 L50,80 L40,60 Z', '#f08a24') + L(100, 60, 100, 180, '#d9701a', 3) + R(50, 110, 100, 12, '#f3f3c0') + R(50, 146, 100, 12, '#f3f3c0') + R(62, 30, 12, 80, '#f3f3c0') + R(126, 30, 12, 80, '#f3f3c0'))
S_('jackhammer', R(0, 0, 200, 200, '#e6dcc8') + R(0, 170, 200, 30, '#a7adb1') + W(80, 194, .9, '#3c7fc1', '#3b4a5a', 'hard', arms='front') + vest(80, 194, .9) + R(84, 72, 40, 8, '#2f3437', 3) + R(96, 76, 18, 60, '#e2463b', 4) + R(102, 136, 6, 34, '#8a9196') + ''.join(Pa(f'M{90+k*14},176 l4,-8 l4,8 Z', '#8a9196') for k in range(3)) + St('M120,150 l10,-6 M122,162 l12,0', '#5d6469', 2), False)

# ================= 军事 =================
S_('army', R(0, 0, 200, 200, '#dfe8d0') + ''.join(soldier(28 + k * 36, 196, .7) for k in range(5)) + ''.join(soldier(46 + k * 36, 150, .5) for k in range(4)), False)
S_('soldier', R(0, 0, 200, 200, '#dfe8d0') + soldier(100, 194, 1.0), False)
S_('navy', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#3c7fc1') + ship_(100, 150, 1.0) + St('M0,160 q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', '#9fd0ec', 3) + flag_(30, 40, .3, '#2f4a7a', '#2f4a7a'), False)
S_('air-force', R(0, 0, 200, 200, SKY) + jet(100, 60, 1.0, -10) + jet(60, 130, .7, -10) + jet(150, 140, .7, -10) + St('M160,140 L200,148', '#ffffff', 4), False)
S_('flag', flag_(50, 30, 1.0, '#e2463b', '#e2463b') + star(84, 60, 10, '#f3c234'))
S_('medal', medal_(100, 100, 1.6))
S_('tank', tank_(100, 160, 1.0))
S_('helmet', hat_('mil', 100, 150, 60) + R(70, 150, 4, 30, '#4a5a2a') + R(126, 150, 4, 30, '#4a5a2a'))
S_('sailor', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#3c7fc1') + W(100, 194, 1.0, '#ffffff', '#ffffff', 'sailor') + Pa('M84,64 L116,64 L110,80 L100,90 L90,80 Z', '#2f4a7a') + Pa('M96,82 L104,82 L100,96 Z', '#e2463b'), False)
S_('general', R(0, 0, 200, 200, '#e6dcc8') + person_bust(100, 90, 34, '#4a5a3a', P['grey'], 'grey', m='flat') + hat_('peak', 100, 90, 34, '#4a5a3a') + ''.join(star(66 + k * 8, 132, 4) for k in range(2)) + ''.join(star(126 + k * 8, 132, 4) for k in range(2)) + ''.join(R(80 + k * 8, 150, 6, 10, ['#e2463b', '#f3c234', '#3c7fc1'][k]) for k in range(3)), False)
S_('veteran', R(0, 0, 200, 200, '#e6dcc8') + person_bust(100, 84, 34, '#4a5a3a', P['grey'], 'grey') + Pa('M70,120 Q100,140 130,120 Q120,138 100,140 Q80,138 70,120 Z', '#c8c3bc') + medal_(80, 168, .4) + medal_(100, 168, .4, '#c4cbd0', '#3c7fc1') + medal_(120, 168, .4, '#c8703a', '#5ba644'), False)
S_('parade', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, WALK) + ''.join(soldier(20 + k * 32, 194, .6, legs='walk') for k in range(6)) + flag_(20, 30, .4, '#e2463b', '#e2463b') + flag_(170, 40, .35, '#3c7fc1', '#3c7fc1') + confetti(3, 14, (10, 10, 180, 40)), False)
S_('salute', R(0, 0, 200, 200, '#dfe8d0') + person_bust(100, 92, 36, '#4a5a3a', m='flat') + hat_('peak', 100, 92, 36, '#4a5a3a') + arm([(130, 140), (160, 100), (128, 74)], '#4a5a3a', SK, 14), False)
S_('march', R(0, 0, 200, 200, '#dfe8d0') + R(0, 170, 200, 30, WALK) + ''.join(soldier(40 + k * 60, 196, .78, arms='down', legs='walk') for k in range(3)), False)
S_('base', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#b8b080') + Pa('M10,150 Q50,100 90,150 Z', '#5a6a3a') + Pa('M100,140 L190,140 L190,100 Q145,70 100,100 Z', '#7a8a6a') + R(126, 110, 40, 30, '#2f3437') + flag_(60, 40, .4, '#3c7fc1', '#3c7fc1') + ''.join(R(k * 20, 170, 4, 30, '#8a9196') for k in range(10)) + L(0, 176, 200, 176, '#8a9196', 2) + L(0, 188, 200, 188, '#8a9196', 2), False)
S_('battle', R(0, 0, 200, 200, '#d8c8b0') + ''.join(Ci(30 + k * 50, 50, 26, '#8a837c', 'opacity=".6"') for k in range(4)) + tank_(60, 170, .5) + G(tank_(0, 0, .5, '#7a6a4a'), 'translate(150,170) scale(-1,1)') + burst(100, 110, 30, '#f08a24', 10) + burst(100, 110, 16, '#f3c234', 8) + jet(150, 40, .5, 10), False)

# ================= 职业 1 =================
S_('driver', R(0, 0, 200, 200, '#9fd0ec') + R(0, 0, 200, 200, '#dff1fb', 0, 'opacity=".4"') + person_bust(100, 74, 30, '#3c7fc1') + hat_('cap', 100, 74, 30, '#2f4a7a') + R(0, 130, 200, 70, '#5d6469') + steering(100, 150, 50) + Ci(44, 150, 0, '#000'), False)
S_('engineer', R(0, 0, 200, 200, '#e6dcc8') + person_bust(70, 90, 30, '#ffffff') + hardhat(70, 90, 30, '#ffffff') + G(R(-40, -30, 80, 60, '#2f5a9a', 3) + R(-26, -16, 52, 34, 'none', 0, 'stroke="#ffffff" stroke-width="2"'), 'translate(150,140) rotate(-8)') + G(Ci(0, 0, 18, '#8a9196') + Ci(0, 0, 7, '#e6dcc8') + ''.join(R(-4, -24, 8, 8, '#8a9196', 1, f'transform="rotate({k*45})"') for k in range(8)), 'translate(160,50)'), False)
S_('scientist', R(0, 0, 200, 200, '#e6f0f4') + coat_over(80, 84, 30) + face_full(80, 84, 30, P['grey'], 'grey') + R(60, 78, 40, 12, '#9fd0ec', 6, 'opacity=".7"') + flask(150, 180, 50, '#7cc05a') + ''.join(Ci(146 + k * 4, 120 - k * 10, 4, '#7cc05a', 'opacity=".7"') for k in range(3)), False)
S_('artist', R(0, 0, 200, 200, '#f6efe0') + W(60, 196, .9, '#5aa1d4', '#3b4a5a', 'beret', arms='wave') + R(110, 40, 80, 100, '#ffffff', 2, 'stroke="#c8903a" stroke-width="5"') + Pa('M116,130 L140,90 L156,110 L184,70 L184,134 L116,134 Z', '#7cc05a') + Ci(166, 60, 10, '#f3c234') + L(130, 140, 116, 196, '#c8903a', 5) + L(170, 140, 184, 196, '#c8903a', 5) + G(E(0, 0, 22, 16, '#e8c890') + Ci(-10, -4, 4, '#e2463b') + Ci(0, -8, 4, '#3c7fc1') + Ci(10, -2, 4, '#f3c234') + Ci(-2, 6, 4, '#5ba644'), 'translate(30,130)'), False)
S_('singer', R(0, 0, 200, 200, '#3a2a5a') + Pa('M60,0 L140,0 L180,200 L20,200 Z', '#f3e070', 'opacity=".25"') + W(100, 196, 1.0, '#e2463b', '#2f3437', '', arms='front', style='long', hair='#2a1a10') + mic_(110, 70, .7, 20) + note(40, 60, 1.2, '#f3c234') + note(160, 80, 1.0, '#f3c234'), False)
S_('writer', R(0, 0, 200, 200, '#f2ead8') + person_bust(90, 80, 28, '#7a8a6a', P['grey'], 'grey') + R(10, 136, 180, 12, WOOD, 3) + doc_(60, 100, 60, 40, 3, '#ffffff', False) + pen_(120, 120, .4, -30) + book_(160, 116, .3, '#e2463b', 90) + book_(160, 104, .3, '#3c7fc1', 90) + lamp_(30, 136, 70), False)
S_('pilot', R(0, 0, 200, 200, SKY) + plane_(150, 50, .5) if False else R(0, 0, 200, 200, SKY) + jet(150, 40, .5, -10, '#ffffff') + person_bust(90, 96, 34, '#ffffff') + hat_('peak', 90, 96, 34, '#1f2a45') + Pa('M70,130 L110,130 L104,170 L76,170 Z', '#1f2a45', 'opacity="0"') + R(108, 136, 20, 4, '#d9a33a') + R(108, 142, 20, 4, '#d9a33a') + R(60, 134, 10, 6, '#d9a33a', 1) + R(112, 134, 10, 6, '#d9a33a', 1), False)
S_('mechanic', R(0, 0, 200, 200, '#e6dcc8') + car_side(140, 190, '#e2463b', .8) + W(60, 196, .95, '#3c7fc1', '#3c7fc1', 'cap', '#e2463b', arms='wave') + wrench_(96, 50, .45, 30), False)
S_('cleaner', R(0, 0, 200, 200, '#e8eef2') + R(0, 170, 200, 30, '#c4cbd0') + W(80, 196, .95, '#5ba644', '#3b4a5a', 'cap', '#5ba644', arms='front') + mop_(110, 110, .8, 10) + bucket_(160, 194, 50, 40, '#3c7fc1') + bubbles(150, 160, 30, 5), False)
S_('shop-assistant', R(0, 0, 200, 200, '#f6efe0') + ''.join(R(10, 20 + k * 30, 180, 4, WOOD) + ''.join(R(16 + j * 22, 2 + k * 30, 16, 18, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644', '#ef8fa4'][(j + k) % 5], 3) for j in range(8)) for k in range(1, 3)) + person_bust(100, 104, 28, '#ffffff', '#5a3a2a', 'long') + Pa('M80,130 L120,130 L124,170 L76,170 Z', '#e2463b') + R(0, 150, 200, 50, '#c58b54') + badge_card(116, 126, .4) + R(130, 130, 50, 24, '#3a4048', 4), False)
S_('hairdresser', R(0, 0, 200, 200, '#f6e8ee') + R(10, 20, 80, 100, '#dff1fb', 40) + person_bust(60, 120, 28, '#9fd0ec', '#3a2a20') + Pa('M30,140 L90,140 L96,200 L24,200 Z', '#ffffff') + W(150, 196, .9, '#2f3437', '#2f3437', '', arms='wave', style='bun', hair='#7a3a8a') + shears_(170, 40, .4, 0, True) + R(140, 100, 20, 6, '#2f3437', 2), False)
S_('accountant', R(0, 0, 200, 200, '#e8eef2') + person_bust(100, 74, 28, '#ffffff', '#3a2a20') + Ci(90, 74, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(110, 74, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + R(10, 130, 180, 12, WOOD, 3) + G(R(-24, -34, 48, 68, '#2f3437', 6) + R(-18, -28, 36, 14, '#cfe8d0', 2) + ''.join(R(-18 + (k % 4) * 9.5, -8 + (k // 4) * 9.5, 7, 7, '#a7adb1', 2) for k in range(16)), 'translate(150,150) rotate(-10)') + G(R(-40, -24, 80, 48, '#ffffff', 2) + ''.join(L(-34, -14 + k * 8, 34, -14 + k * 8, '#a7adb1', 2) for k in range(5)) + L(10, -24, 10, 24, '#e2463b', 1.5), 'translate(70,150)'), False)
S_('secretary', R(0, 0, 200, 200, '#e8eef2') + person_bust(90, 80, 30, '#ef8fa4', '#5a3a2a', 'bun') + St('M62,70 Q90,30 118,70', '#2f3437', 4) + R(56, 66, 10, 18, '#2f3437', 4) + St('M64,84 Q70,100 84,98', '#2f3437', 2) + R(10, 136, 180, 12, WOOD, 3) + monitor(130, 80, 56, 44) + calendar_(16, 20, 40, 40, 5), False)
S_('postman', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + W(90, 196, 1.0, '#2f6a3a', '#2f3437', 'cap', '#2f6a3a', arms='wave') + St('M78,52 L106,106', '#8a5a35', 4) + R(90, 100, 40, 34, '#8a5a35', 6) + envelope_(124, 30, 40, 28) + G(R(-12, -40, 24, 50, '#2f6a3a', 3) + R(-16, -44, 32, 8, '#2f6a3a', 3) + R(-6, -34, 12, 4, '#2f3437'), 'translate(170,194)'), False)
S_('security-guard', R(0, 0, 200, 200, '#e8eef2') + W(100, 196, 1.05, '#2f3a4a', '#2f3437', 'peak', '#2f3a4a') + badge(110, 76, 'cow', 0) + Pa('M104,76 L112,72 L120,76 L118,86 L112,90 L106,86 Z', '#f3c234') + R(126, 110, 10, 22, '#2f3437', 2) + L(132, 110, 132, 98, '#2f3437', 2), False)
S_('tour-guide', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(60, 196, .9, '#f08a24', '#3b4a5a', 'cap', '#f08a24', arms='wave') + R(98, 40, 2, 24, '#5d6469') + Pa('M100,40 L126,46 L100,54 Z', '#e2463b') + ''.join(fig(120 + k * 26, 196, ['man', 'woman', 'oldman'][k], s=.5) for k in range(3)), False)

# ================= 职业 2 =================
S_('actor', R(0, 0, 200, 200, '#7a1a2a') + Pa('M0,0 L60,0 Q40,100 0,200 Z', '#c0283a') + Pa('M200,0 L140,0 Q160,100 200,200 Z', '#c0283a') + R(0, 170, 200, 30, '#8a5a35') + W(100, 186, .9, '#f3c234', '#2f3437', arms='up') + Pa('M60,10 L140,10 Q100,30 60,10 Z', '#f3c234', 'opacity=".2"'), False)
S_('musician', R(0, 0, 200, 200, '#f6efe0') + W(70, 196, .95, '#2f3437', '#2f3437', arms='front') + G(E(0, 0, 22, 30, '#c0603a') + E(0, -30, 16, 18, '#c0603a') + Ci(0, -10, 6, '#3a2a20') + R(-3, -110, 6, 80, '#3a2a20') + R(-6, -116, 12, 10, '#3a2a20', 2), 'translate(78,130) rotate(-30)') + note(150, 60, 1.4) + note(170, 110, 1.0, '#3c7fc1'), False)
S_('photographer', R(0, 0, 200, 200, '#e6dcc8') + W(100, 196, 1.0, '#5d6469', '#2f3437', 'cap', '#2f3437', arms='front') + camera_(100, 60, .45) + burst(140, 40, 12, '#f3c234', 8), False)
S_('gardener', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, FIELD) + W(70, 196, .95, '#5ba644', '#3b5f8f', 'straw') + watering_can_(130, 130, .6) + ''.join(flower(150 + k * 18, 160 - (k % 2) * 10, 1.0, ['#e2463b', '#f3c234', '#ef8fa4'][k]) + St(f'M{150+k*18},{160-(k%2)*10} L{150+k*18},180', '#4a9a3a', 2) for k in range(3)), False)
S_('fisherman', R(0, 0, 200, 200, SKY) + R(0, 130, 200, 70, '#3c7fc1') + Pa('M20,150 L130,150 L116,174 L34,174 Z', '#a8703e') + W(70, 156, .55, '#f3c234', '#3b5f8f', 'straw') + St('M80,90 Q140,20 180,40', '#5d6469', 3) + L(180, 40, 180, 140, '#5d6469', 1) + fish_shape(170, 156, 36, '#9fb4c4'), False)
S_('tailor', R(0, 0, 200, 200, '#f6efe0') + person_bust(70, 90, 30, '#7a4fa0', P['grey'], 'grey') + St('M40,120 Q70,150 100,120', '#f3c234', 6) + ''.join(L(44 + k * 8, 128 + abs(k - 3) * 2, 44 + k * 8, 134 + abs(k - 3) * 2, '#2f3437', 1.5) for k in range(7)) + R(100, 150, 90, 10, WOOD) + R(116, 100, 60, 50, '#2f3437', 8) + R(116, 100, 20, 30, '#2f3437') + R(160, 140, 4, 14, '#c4cbd0') + Ci(170, 116, 10, '#5d6469') + Pa('M60,170 L140,170 L150,200 L50,200 Z', '#3c7fc1', 'opacity="0"'), False)
S_('vet', R(0, 0, 200, 200, '#e6f0f4') + coat_over(70, 80, 30) + face_full(70, 80, 30, '#5a3a2a', 'long') + stetho(70, 80, 30) + G(E(0, 0, 34, 22, '#c8903a') + Ci(30, -20, 18, '#c8903a') + E(22, -32, 7, 12, '#8a5a35') + Ci(36, -24, 3, '#2f3437') + Ci(46, -18, 4, '#2f3437') + L(-30, 0, -44, -14, '#c8903a', 6) + R(-24, 16, 8, 20, '#c8903a', 3) + R(16, 16, 8, 20, '#c8903a', 3), 'translate(140,150)') + cross_sign(170, 40, .6), False)
S_('librarian', R(0, 0, 200, 200, '#f2ead8') + ''.join(R(0, 20 + k * 40, 200, 6, WOOD) + ''.join(R(4 + j * 14, k * 40 - 8 + 20, 11, 28, ['#8a2a2a', '#2f4a7a', '#3c6a3a', '#a8903a', '#7a4fa0'][(j * 3 + k) % 5], 2) for j in range(14)) for k in range(1, 3)) + person_bust(100, 130, 26, '#5aa1d4', P['grey'], 'bun') + Ci(91, 130, 6, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(109, 130, 6, 'none', 'stroke="#2f3437" stroke-width="2"') + book_(150, 176, .4, '#e2463b', -80) + R(0, 172, 200, 28, WOOD), False)
S_('receptionist', R(0, 0, 200, 200, '#e8eef2') + person_bust(100, 80, 28, '#2f3a4a', '#5a3a2a', 'bun') + R(10, 120, 180, 80, '#c58b54', 4) + R(10, 116, 180, 10, '#a8703e', 3) + G(E(0, 0, 14, 4, '#d9a33a') + Pa('M-10,0 Q-10,-14 0,-14 Q10,-14 10,0 Z', '#d9a33a') + Ci(0, -16, 3, '#d9a33a'), 'translate(150,112)') + R(60, 150, 80, 20, '#ffffff', 3, 'opacity=".25"'), False)
S_('manager', R(0, 0, 200, 200, '#e8eef2') + suit_bust(70, 90, 30, '#2f4a7a', '#f3c234', '#3a2a20') + R(110, 30, 80, 70, '#ffffff', 3) + ''.join(R(120 + k * 16, 90 - h, 10, h, '#5aa1d4') for k, h in enumerate([16, 30, 22, 46])) + St('M120,70 L136,54 L152,62 L176,36', '#e2463b', 3) + R(140, 100, 4, 60, '#a7adb1'), False)
S_('businessman', R(0, 0, 200, 200, SKY) + building(10, 40, 50, 160) + building(150, 20, 50, 180, '#a8b8c8') + R(0, 180, 200, 20, WALK) + W(100, 196, 1.0, '#2f3a4a', '#2f3a4a', legs='walk') + Pa('M94,60 L100,90 L106,60 Z', '#ffffff') + Pa('M98,62 L102,62 L103,84 L100,88 L97,84 Z', '#e2463b') + briefcase(130, 136, 30, '#5a3a24'), False)
S_('programmer', R(0, 0, 200, 200, '#1f2a35') + person_bust(60, 96, 28, '#5d6469', '#3a2a20') + St('M32,86 Q60,40 88,86', '#2f3437', 4) + E(32, 96, 6, 10, '#2f3437') + E(88, 96, 6, 10, '#2f3437') + monitor(100, 50, 92, 70, ''.join(R(110 + (k % 2) * 10, 62 + k * 9, 30 + (k * 17) % 40, 4, ['#7cc05a', '#f3c234', '#ef8fa4', '#9fd0ec'][k % 4], 2) for k in range(6)), '#1f2a35', '#3a4048') + R(0, 150, 200, 50, '#2f3a45'), False)
S_('designer', R(0, 0, 200, 200, '#f6efe0') + person_bust(60, 90, 28, '#2f3437', '#7a3a2a', 'bun') + R(100, 40, 90, 110, '#ffffff', 4) + Ci(130, 80, 20, '#ef8fa4') + R(140, 80, 36, 36, '#5aa1d4', 0, 'opacity=".85"') + Pa('M120,140 L140,100 L160,140 Z', '#f3c234', 'opacity=".9"') + ''.join(R(20 + k * 22, 160, 18, 30, ['#e2463b', '#f3c234', '#5ba644', '#3c7fc1', '#7a4fa0', '#ef8fa4', '#2f3437', '#f08a24'][k], 2) for k in range(8)) + pencil_(120, 150, .4, -40), False)
S_('translator', person_bust(100, 120, 30, '#5ba644', '#3a2a20') + bubble(50, 52, 80, 56, (80, 96)) + T(50, 60, 'A', 34, '#3c7fc1', 900) + bubble(150, 52, 80, 56, (120, 96)) + T(150, 60, '文', 34, '#e2463b', 900) + arrow(84, 90, 116, 90, '#5d6469', 3) + arrow(116, 90, 84, 90, '#5d6469', 3))
S_('housekeeper', R(0, 0, 200, 200, '#f2ead8') + R(0, 160, 200, 40, '#d9b07a') + W(90, 196, .95, '#3c3a5a', '#3c3a5a', '', arms='wave', style='bun', hair='#3a2a20') + Pa('M78,90 L102,90 L106,140 L74,140 Z', '#ffffff') + G(R(-3, 0, 6, 40, WOOD) + ''.join(Pa(f'M0,0 L{-14+k*7},-26 L{-10+k*7},-26 Z', ['#ef8fa4', '#9fd0ec', '#f3c234', '#7cc05a', '#ef8fa4'][k]) for k in range(5)), 'translate(130,50) rotate(170)') + sofa(160, 170, 70, '#5aa1d4', .6), False)
S_('delivery-driver', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, ROAD) + G(wheel(-50, 0, 18) + wheel(50, 0, 18) + Pa('M-50,0 L-20,-30 L40,-30 L56,0 Z', '#f3c234') + R(-70, -70, 50, 44, '#f3c234', 4) + R(-64, -64, 38, 32, '#f6d860', 3) + St('M40,-30 L50,-60', '#2f3437', 5) + L(42, -60, 60, -60, '#2f3437', 5), 'translate(100,174)') + W(110, 160, .6, '#f3c234', '#3b4a5a', 'hard', '#f3c234', arms='front'), False)

dump()
