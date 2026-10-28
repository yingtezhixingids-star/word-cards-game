from kit3 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)
SEA = '#5aa1d4'; SEAD = '#3c7fc1'

def road_top(lines=True):
    g = R(0, 0, 200, 200, '#8cc06a') + R(70, 0, 60, 200, ROAD)
    if lines: g += ''.join(R(98, 10 + k * 30, 4, 16, '#ffffff') for k in range(7))
    return g

def sign_round(x, y, r, ring_col='#e2463b', inner=''):
    return R(x - 3, y + r, 6, 190 - y - r, '#8a9196') + Ci(x, y, r, '#ffffff') + Ci(x, y, r, 'none', f'stroke="{ring_col}" stroke-width="{r*.22}"') + inner

def sign_blue(x, y, r, inner=''):
    return R(x - 3, y + r, 6, 190 - y - r, '#8a9196') + Ci(x, y, r, '#3c7fc1') + inner

def bus_side(cx, base, s=1, col='#3c7fc1', double=False):
    h = 90 if double else 56
    g = R(-80, -h - 10, 160, h, col, 8) + ''.join(R(-70 + k * 28, -h - 2, 22, 22, '#cfe8f6', 3) for k in range(5)) + R(64, -h - 2, 12, 40, '#cfe8f6', 2)
    if double: g += ''.join(R(-70 + k * 28, -h + 32, 22, 20, '#cfe8f6', 3) for k in range(5)) + R(-80, -h + 26, 160, 4, '#ffffff')
    g += R(-80, -24, 160, 6, '#ffffff') + wheel(-50, -6, 13) + wheel(50, -6, 13) + R(70, -26, 10, 6, '#f3d058', 2)
    return G(g, f'translate({cx},{base}) scale({s})')

def taxi_(cx, base, s=1):
    return G(car_side(0, 0, '#f3c234', 1) + R(-14, -70, 30, 12, '#2f3437', 3) + T(1, -61, 'TAXI', 8, '#f3c234', 900) + ''.join(R(-58 + k * 12, -18, 6, 6, '#2f3437') for k in range(10)), f'translate({cx},{base}) scale({s})')

def train_side(cx, base, s=1, col='#e2463b', nose=True):
    g = R(-90, -50, 170, 44, col, 6) + R(-90, -40, 170, 10, '#ffffff') + ''.join(R(-80 + k * 30, -38, 22, 8, '#5aa1d4', 2) for k in range(5))
    if nose: g += Pa('M80,-50 Q110,-40 116,-6 L80,-6 Z', col) + Pa('M84,-44 Q102,-38 106,-26 L84,-26 Z', '#5aa1d4')
    g += wheel(-60, -2, 7) + wheel(-40, -2, 7) + wheel(40, -2, 7) + wheel(60, -2, 7)
    return G(g, f'translate({cx},{base}) scale({s})')

def plane_(cx, cy, s=1, rot=0, col='#ffffff'):
    g = Pa('M-80,0 Q-80,-12 -60,-12 L60,-12 Q90,-10 96,0 Q90,10 60,12 L-60,12 Q-80,12 -80,0 Z', col) + Pa('M-10,-8 L20,-60 L36,-60 L26,-8 Z', '#c4cbd0') + Pa('M-10,8 L20,60 L36,60 L26,8 Z', '#a7adb1') + Pa('M-70,-8 L-80,-34 L-66,-34 L-56,-8 Z', '#e2463b') + ''.join(Ci(-40 + k * 14, -2, 3, '#5aa1d4') for k in range(7)) + Pa('M80,-6 Q90,-4 92,0 L80,0 Z', '#5aa1d4')
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def heli(cx, cy, s=1):
    g = E(0, 0, 40, 26, '#e2463b') + E(14, -4, 18, 14, '#cfe8f6') + R(-90, -6, 60, 10, '#e2463b', 4) + Pa('M-92,-20 L-86,-20 L-80,10 L-86,10 Z', '#e2463b') + R(-4, -34, 8, 10, '#5d6469') + R(-80, -38, 160, 4, '#5d6469', 2) + L(-20, 26, -26, 40, '#5d6469', 3) + L(20, 26, 26, 40, '#5d6469', 3) + R(-40, 38, 80, 4, '#5d6469', 2)
    return G(g, f'translate({cx},{cy}) scale({s})')

def boat_hull(cx, base, w, h, col='#ffffff', bottom='#e2463b'):
    return Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w/2-h*.6},{base} L{cx-w/2+h*.4},{base} Z', col) + Pa(f'M{cx-w/2+h*.25},{base-h*.4} L{cx+w/2-h*.35},{base-h*.4} L{cx+w/2-h*.6},{base} L{cx-w/2+h*.4},{base} Z', bottom)

def sea(y=140):
    return R(0, 0, 200, y, SKY) + R(0, y, 200, 200 - y, SEA) + ''.join(St(f'M{10+k*44},{y+20+(k%2)*20} q10,-5 20,0', '#9fd0ec', 2) for k in range(5))

def bike_(cx, base, s=1, col='#e2463b'):
    g = wheel(-40, -26, 26, '#2f3437', '#f2ead8') + wheel(40, -26, 26, '#2f3437', '#f2ead8') + Ci(-40, -26, 20, 'none', 'stroke="#c4cbd0" stroke-width="1.5"') + Ci(40, -26, 20, 'none', 'stroke="#c4cbd0" stroke-width="1.5"')
    g += St('M-40,-26 L-10,-26 L20,-60 L-20,-60 L-10,-26 M20,-60 L40,-26 M-20,-60 L-24,-70 M20,-60 L18,-74', col, 5) + R(-34, -74, 22, 6, '#2f3437', 3) + St('M12,-74 L28,-78', '#2f3437', 4) + Ci(-10, -26, 6, '#5d6469')
    return G(g, f'translate({cx},{base}) scale({s})')

def moto(cx, base, s=1, col='#e2463b'):
    g = wheel(-46, -24, 24) + wheel(50, -24, 24) + Pa('M-40,-30 L-20,-56 L30,-56 L50,-30 Z', col) + R(-20, -66, 40, 12, '#2f3437', 5) + St('M30,-56 L44,-80 L56,-80', '#5d6469', 5) + R(-30, -36, 30, 14, '#a7adb1', 4) + St('M-50,-36 L-80,-30', '#a7adb1', 6)
    return G(g, f'translate({cx},{base}) scale({s})')

def helmet(cx, cy, s=1, col='#e2463b'):
    return G(Pa('M-40,10 Q-44,-40 0,-44 Q44,-40 40,10 L30,20 L-30,20 Z', col) + Pa('M-6,-20 Q30,-24 38,0 L38,10 L-6,10 Z', '#2f3437') + hi(-20, -26, 10, 6, .4, -20), f'translate({cx},{cy}) scale({s})')

def ticket_(x, y, s=1, rot=0, col='#f3c234', txt=''):
    return G(R(-50, -26, 100, 52, col, 4) + Ci(-50, 0, 8, '#f2ead8') + Ci(50, 0, 8, '#f2ead8') + L(20, -24, 20, 24, shade(col, -.2), 2) + T(-14, 6, txt, 16, '#2f3437', 900) + ''.join(L(28, -14 + k * 8, 42, -14 + k * 8, shade(col, -.3), 1.5) for k in range(4)), f'translate({x},{y}) rotate({rot}) scale({s})')

def suitcase(cx, base, w=60, h=80, col='#3c7fc1'):
    return R(cx - w / 2, base - h, w, h, col, 8) + R(cx - 12, base - h - 14, 24, 16, 'none', 4, 'stroke="#2f3437" stroke-width="4"') + ''.join(L(cx - w / 2 + 12 + k * (w - 24) / 2, base - h + 6, cx - w / 2 + 12 + k * (w - 24) / 2, base - 6, shade(col, -.2), 2) for k in range(3)) + wheel(cx - w / 2 + 8, base + 4, 4) + wheel(cx + w / 2 - 8, base + 4, 4)

def passport_(x, y, s=1, rot=0):
    return G(R(-34, -46, 68, 92, '#7a1a24', 4) + Ci(0, -6, 16, 'none', 'stroke="#d9a33a" stroke-width="2.5"') + L(-16, -6, 16, -6, '#d9a33a', 1.5) + St('M0,-22 Q8,-6 0,10 Q-8,-6 0,-22', '#d9a33a', 1.5) + R(-20, 24, 40, 4, '#d9a33a', 1) + R(-14, 32, 28, 3, '#d9a33a', 1), f'translate({x},{y}) rotate({rot}) scale({s})')

def anchor_(x, y, s=1, col='#5d6469'):
    return G(Ci(0, -50, 10, 'none', f'stroke="{col}" stroke-width="6"') + R(-4, -40, 8, 80, col) + R(-24, -26, 48, 8, col, 3) + St('M-40,20 Q-30,50 0,50 Q30,50 40,20', col, 8) + Pa('M-46,26 L-40,10 L-30,24 Z M46,26 L40,10 L30,24 Z', col), f'translate({x},{y}) scale({s})')

def lighthouse(cx, base, s=1):
    g = Pa('M-20,0 L-12,-110 L12,-110 L20,0 Z', '#ffffff') + ''.join(Pa(f'M{-20+k*3.2*0},{-k*30} L{20},{-k*30} L{19},{-k*30-14} L{-19},{-k*30-14} Z', '#e2463b') for k in range(0)) + ''.join(R(-18 + k * 2, -24 - k * 30, 36 - k * 4, 14, '#e2463b') for k in range(3))
    g += R(-16, -130, 32, 20, '#fff3a0') + Pa('M-20,-130 L0,-148 L20,-130 Z', '#2f3437') + R(-18, -112, 36, 4, '#2f3437') + Pa('M16,-124 L90,-150 L90,-100 Z', '#fff3a0', 'opacity=".5"')
    return G(g, f'translate({cx},{base}) scale({s})')

def container_(x, y, w, h, col):
    return R(x, y, w, h, col, 1) + ''.join(L(x + 6 + k * 8, y + 3, x + 6 + k * 8, y + h - 3, shade(col, -.2), 2) for k in range(int((w - 8) / 8)))

def dash_icon(x, y, r):
    return Ci(x, y, r, '#2f3437') + Ci(x, y, r * .8, '#1f2a35') + ''.join(L(x + r * .65 * math.cos(a), y + r * .65 * math.sin(a), x + r * .78 * math.cos(a), y + r * .78 * math.sin(a), '#ffffff', 1.5) for a in [math.pi + k * math.pi / 8 for k in range(9)]) + L(x, y, x + r * .6 * math.cos(-.6), y + r * .6 * math.sin(-.6), '#e2463b', 2.5) + Ci(x, y, 3, '#e2463b')

def steering(x, y, r):
    return Ci(x, y, r, 'none', 'stroke="#2f3437" stroke-width="10"') + Ci(x, y, r * .3, '#2f3437') + L(x - r, y, x + r, y, '#2f3437', 8) + L(x, y, x, y + r, '#2f3437', 8)

# ================= 道路 =================
S_('road', R(0, 0, 200, 200, SKY) + Pa('M0,110 Q100,90 200,110 L200,200 L0,200 Z', '#8cc06a') + Pa('M90,100 L110,100 L170,200 L30,200 Z', ROAD) + ''.join(Pa(f'M{98+k*1},{110+k*24} L{102+k*1},{110+k*24} L{104+k*2},{124+k*26} L{96+k*0},{124+k*26} Z', '#ffffff') for k in range(4)) + tree(30, 110, .5) + tree(170, 104, .6), False)
S_('traffic', R(0, 0, 200, 200, ROAD) + ''.join(R(0, 66 + k * 66, 200, 3, '#ffffff', 0, 'stroke-dasharray="1"') for k in range(2)) + car_side(50, 56, '#e2463b', .55) + car_side(150, 56, '#3c7fc1', .55) + taxi_(80, 122, .55) + bus_side(150, 124, .45) + car_side(40, 188, '#5ba644', .55) + car_side(140, 188, '#f08a24', .55), False)
S_('turn-left', road_top() + St('M110,190 L110,110 Q110,80 80,80 L40,80', '#f3c234', 10) + Pa('M24,80 L46,62 L46,98 Z', '#f3c234'), False)
S_('turn-right', road_top() + St('M90,190 L90,110 Q90,80 120,80 L160,80', '#f3c234', 10) + Pa('M176,80 L154,62 L154,98 Z', '#f3c234'), False)
S_('go-straight', road_top() + St('M100,190 L100,50', '#f3c234', 10) + Pa('M100,24 L80,52 L120,52 Z', '#f3c234'), False)
S_('traffic-jam', R(0, 0, 200, 200, ROAD) + ''.join(car_side(30 + (k % 3) * 70, 50 + (k // 3) * 60, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644', '#ffffff', '#f08a24', '#7a4fa0', '#e2463b', '#3c7fc1'][k], .45) for k in range(9)) + ''.join(R(24 + (k % 3) * 70, 34 + (k // 3) * 60, 6, 4, '#ff4a3a', 1) for k in range(9)), False)
S_('highway', R(0, 0, 200, 200, SKY) + Pa('M0,120 L200,120 L200,200 L0,200 Z', '#8cc06a') + Pa('M70,90 L130,90 L200,200 L0,200 Z', ROAD) + Pa('M96,90 L104,90 L110,200 L90,200 Z', '#c4cbd0') + ''.join(R(80 - k * 8, 110 + k * 24, 3, 14, '#ffffff') for k in range(4)) + ''.join(R(118 + k * 8, 110 + k * 24, 3, 14, '#ffffff') for k in range(4)) + R(20, 40, 160, 34, '#3c8a3a', 3) + R(26, 46, 50, 22, '#ffffff', 2) + T(51, 63, 'G15', 14, '#3c8a3a', 900) + arrow(120, 57, 170, 57, '#ffffff', 4) + R(30, 74, 6, 46, '#8a9196') + R(164, 74, 6, 46, '#8a9196'), False)
S_('road-sign', R(97, 60, 6, 130, '#8a9196') + Pa('M60,30 L150,30 L166,48 L150,66 L60,66 Z', '#3c7fc1') + Pa('M140,76 L50,76 L34,94 L50,112 L140,112 Z', '#3c8a3a') + R(74, 42, 50, 6, '#ffffff', 2) + R(58, 88, 50, 6, '#ffffff', 2))
S_('speed-limit', sign_round(100, 90, 64, '#e2463b', T(100, 110, '60', 50, '#2f3437', 900)))
S_('roundabout', R(0, 0, 200, 200, '#8cc06a') + R(70, 0, 60, 200, ROAD) + R(0, 70, 200, 60, ROAD) + Ci(100, 100, 56, ROAD) + Ci(100, 100, 26, '#8cc06a') + flower(100, 100, 1.2, '#ef8fa4') + ''.join(Pa(f'M{100+42*math.cos(a)},{100+42*math.sin(a)} l{12*math.cos(a+1.8)},{12*math.sin(a+1.8)} l{12*math.cos(a+1.2)},{12*math.sin(a+1.2)} Z', '#ffffff') for a in [k * math.pi / 2 + .5 for k in range(4)]), False)
S_('one-way-street', R(0, 0, 200, 200, '#e6dcc8') + R(0, 130, 200, 70, ROAD) + R(30, 40, 140, 50, '#3c7fc1', 4) + Pa('M44,56 L130,56 L130,46 L156,65 L130,84 L130,74 L44,74 Z', '#ffffff') + R(97, 90, 6, 40, '#8a9196') + arrow(40, 170, 160, 170, '#ffffff', 5), False)
S_('tunnel', R(0, 0, 200, 200, '#7a9a5a') + Pa('M0,60 Q100,10 200,60 L200,200 L0,200 Z', '#8a7a6a') + Pa('M40,200 L40,120 Q40,60 100,60 Q160,60 160,120 L160,200 Z', '#c4bcae') + Pa('M54,200 L54,124 Q54,76 100,76 Q146,76 146,124 L146,200 Z', '#2f3437') + Pa('M80,200 L92,110 L108,110 L120,200 Z', '#5d6469') + ''.join(Ci(70 + k * 20, 100, 3, '#f3d058') for k in range(4)), False)
S_('lane', R(0, 0, 200, 200, ROAD) + ''.join(R(64 + k * 70 * 0, 0, 0, 0, '#fff') for k in range(1)) + ''.join(R(64, 10 + k * 34, 4, 20, '#ffffff') + R(132, 10 + k * 34, 4, 20, '#ffffff') for k in range(6)) + R(4, 0, 4, 200, '#f3c234') + R(192, 0, 4, 200, '#f3c234') + R(70, 0, 60, 200, '#f3c234', 0, 'opacity=".2"') + G(car_side(0, 0, '#e2463b', .5), 'translate(100,120) rotate(-90)'), False)
S_('toll', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, ROAD) + R(10, 40, 180, 20, '#3c7fc1') + R(20, 60, 30, 90, '#e6ecef') + R(150, 60, 30, 90, '#e6ecef') + R(50, 120, 60, 6, '#e2463b', 2) + ''.join(R(54 + k * 14, 120, 7, 6, '#ffffff') for k in range(4)) + car_side(130, 178, '#5ba644', .45) + coin_(100, 90, 12), False)
S_('intersection', R(0, 0, 200, 200, '#8cc06a') + R(70, 0, 60, 200, ROAD) + R(0, 70, 200, 60, ROAD) + ''.join(R(72 + k * 10, 60, 6, 10, '#ffffff') + R(72 + k * 10, 130, 6, 10, '#ffffff') + R(60, 72 + k * 10, 10, 6, '#ffffff') + R(130, 72 + k * 10, 10, 6, '#ffffff') for k in range(6)) + G(R(-4, -26, 8, 20, '#2f3437', 2) + Ci(0, -21, 2.5, '#ff4a3a') + Ci(0, -11, 2.5, '#2f7a3a'), 'translate(150,60)'), False)
S_('u-turn', road_top() + St('M120,190 L120,80 Q120,50 100,50 Q80,50 80,80 L80,140', '#f3c234', 10) + Pa('M80,164 L62,138 L98,138 Z', '#f3c234'), False)

# ================= 汽车（一） =================
S_('car', R(0, 160, 200, 40, ROAD) + car_side(100, 160, '#e2463b', 1.3), False)
S_('drive', R(0, 0, 200, 200, '#cfe8f6') + Pa('M0,120 L200,120 L200,200 L0,200 Z', '#2f3437') + steering(100, 150, 46) + G(R(-12, -10, 24, 26, SK, 8), 'translate(56,140) rotate(-20)') + G(R(-12, -10, 24, 26, SK, 8), 'translate(144,140) rotate(20)') + Pa('M60,0 L90,120 L110,120 L140,0 Z', ROAD) + ''.join(R(98, 10 + k * 34, 4, 18, '#ffffff') for k in range(3)), False)
S_('wheel', wheel(100, 100, 70, '#2f3437', '#c4cbd0') + ''.join(L(100, 100, 100 + 34 * math.cos(a), 100 + 34 * math.sin(a), '#8a9196', 6) for a in [k * math.pi * 2 / 5 for k in range(5)]) + Ci(100, 100, 10, '#5d6469'))
S_('tire', Ci(100, 100, 70, '#2f3437') + Ci(100, 100, 40, '#f2ead8') + ''.join(R(100 + 60 * math.cos(a) - 4, 100 + 60 * math.sin(a) - 8, 8, 16, '#1a1a1a', 1, f'transform="rotate({math.degrees(a):.0f} {100+60*math.cos(a):.0f} {100+60*math.sin(a):.0f})"') for a in [k * math.pi / 8 for k in range(16)]))
S_('seat-belt', R(40, 30, 120, 170, '#5d6469', 20) + R(60, 10, 80, 40, '#5d6469', 16) + St('M150,20 L60,180', '#2f3437', 14) + St('M40,150 L160,150', '#2f3437', 14) + R(130, 140, 26, 20, '#c4cbd0', 3) + R(136, 146, 14, 8, '#e2463b', 2))
S_('horn', steering(100, 110, 64) + Ci(100, 110, 20, '#5d6469') + T(100, 116, '♪', 0, '#000') + St('M150,40 q10,10 0,20 M162,30 q16,20 0,40 M50,40 q-10,10 0,20 M38,30 q-16,20 0,40', '#e2463b', 3) + hand_(100, 100, .5, 0, '#3c7fc1'))
S_('brake', R(0, 0, 200, 200, '#2f3437') + R(40, 90, 50, 70, '#5d6469', 6) + ''.join(L(46, 100 + k * 10, 84, 100 + k * 10, '#2f3437', 3) for k in range(6)) + R(120, 110, 30, 50, '#5d6469', 4) + G(Pa('M-20,0 L-20,-20 Q-18,-28 -8,-26 L6,-16 Q24,-12 38,-8 Q46,-4 44,4 L-20,4 Z', '#2f5a8a'), 'translate(64,86) rotate(30)') + arrow(30, 40, 50, 80, '#e2463b', 4), False)
S_('engine', R(30, 70, 140, 90, '#8a9196', 8) + ''.join(R(44 + k * 30, 50, 20, 26, '#5d6469', 4) for k in range(4)) + R(40, 100, 120, 10, '#5d6469') + Ci(70, 140, 14, '#2f3437') + Ci(130, 140, 14, '#2f3437') + St('M70,126 L130,126 L130,154 L70,154 Z', 'none', 0) + St('M40,80 Q20,90 26,120', '#2f3437', 5) + R(150, 60, 24, 14, '#e2463b', 3))
S_('trunk', R(0, 160, 200, 40, ROAD) + G(car_side(0, 0, '#3c7fc1', 1.3) + Pa('M-60,-22 L-64,-50 L-26,-52', 'none', 'stroke="none"'), 'translate(110,160)') + Pa('M24,130 L10,84 L50,76 L42,128 Z', '#3c7fc1') + R(28, 116, 40, 18, '#2f3437') + suitcase(46, 132, 22, 22, '#e2463b'), False)
S_('headlight', R(0, 0, 200, 200, '#2f3445') + R(0, 160, 200, 40, ROAD) + G(car_side(0, 0, '#e6ecef', 1.2), 'translate(70,160)') + Pa('M150,130 L200,100 L200,170 Z', '#fff3a0', 'opacity=".6"') + Ci(146, 134, 6, '#fff3a0'), False)
S_('steering-wheel', steering(100, 100, 66) + R(90, 160, 20, 40, '#2f3437'))
S_('driver-s-license', G(R(-80, -50, 160, 100, '#e6f0f4', 8) + R(-80, -50, 160, 22, '#3c7fc1', 8) + R(-80, -36, 160, 8, '#3c7fc1') + R(-68, -18, 44, 56, '#ffffff', 3) + Ci(-46, 2, 12, SK) + Pa('M-58,-2 Q-46,-16 -34,-2 Z', '#3a2a20') + Pa('M-64,38 Q-46,16 -28,38 Z', '#5aa1d4') + ''.join(L(-10, -10 + k * 12, 64 - (k % 2) * 20, -10 + k * 12, '#a7adb1', 3) for k in range(4)) + car_side(50, 40, '#e2463b', .2), 'translate(100,100) rotate(-6)'))
S_('windshield', R(0, 0, 200, 200, '#e6ecef') + Pa('M20,150 L50,40 Q100,24 150,40 L180,150 Z', '#2f3437') + Pa('M30,144 L56,48 Q100,34 144,48 L170,144 Z', '#a9d8f2') + Pa('M60,130 L90,60 L106,60 L76,130 Z', '#ffffff', 'opacity=".4"') + St('M60,140 Q90,100 110,110', '#5d6469', 4) + St('M110,140 Q140,100 160,110', '#5d6469', 4), False)
S_('rear-view-mirror', R(0, 0, 200, 200, '#a9d8f2') + R(96, 0, 8, 40, '#2f3437') + R(30, 40, 140, 56, '#2f3437', 20) + R(38, 48, 124, 40, '#cfe8f6', 14) + car_side(100, 84, '#e2463b', .3) + R(0, 140, 200, 60, '#2f3437'), False)
S_('gear', R(60, 140, 80, 40, '#2f3437', 10) + R(94, 60, 12, 90, '#5d6469', 4) + Ci(100, 54, 22, '#2f3437') + G(T(0, 6, 'P R N D', 12, '#ffffff', 900), 'translate(100,168)') + Ci(100, 54, 22, 'none', 'stroke="#5d6469" stroke-width="2"'))
S_('dashboard', R(0, 0, 200, 200, '#2f3437') + R(10, 50, 180, 100, '#3a3f44', 20) + dash_icon(64, 104, 40) + dash_icon(140, 104, 34) + R(90, 130, 24, 10, '#7fe08a', 2) + Ci(100, 70, 5, '#f3c234') + steering(100, 200, 70), False)

# ================= 汽车（二） =================
S_('fuel', R(50, 50, 80, 130, '#e2463b', 8) + R(60, 60, 60, 40, '#ffffff', 4) + St('M130,80 L160,80 L160,150 Q160,166 146,166', '#2f3437', 6) + R(140, 60, 30, 16, '#2f3437', 4) + R(64, 70, 30, 6, '#7fe08a', 1) + drop(80, 140, 14, '#f3c234') + R(40, 176, 100, 8, '#5d6469', 3))
S_('fill-up', R(0, 160, 200, 40, ROAD) + R(20, 60, 50, 100, '#e2463b', 6) + R(28, 70, 34, 24, '#ffffff', 3) + St('M70,100 Q100,96 120,120', '#2f3437', 5) + G(car_side(0, 0, '#3c7fc1', .9), 'translate(130,160)') + G(R(0, 0, 40, 16, '#e6ecef', 3) + R(4, 4, 30, 8, '#5ba644', 1), 'translate(20,30)') + T(56, 26, 'FULL', 0, '#000'), False)
S_('car-wash', R(0, 0, 200, 200, '#e6f0f4') + R(0, 160, 200, 40, '#a7b0b8') + car_side(100, 160, '#e2463b', 1.0) + ''.join(Ci(30 + k * 26, 80 - (k % 2) * 14, 12, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(7)) + ''.join(drop(20 + k * 30, 30 + (k % 2) * 10, 6, '#9fd0ec') for k in range(6)) + R(0, 0, 14, 160, '#5aa1d4', 6) + R(186, 0, 14, 160, '#5aa1d4', 6), False)
S_('flat-tire', R(0, 160, 200, 40, ROAD) + G(car_side(0, 0, '#5ba644', 1.2), 'translate(100,152) rotate(4)') + E(146, 158, 20, 8, '#2f3437') + Pa('M140,150 l6,-6 l4,6 l6,-8', 'none', 'stroke="#f3c234" stroke-width="3"') + T(150, 120, '!', 0, '#000'), False)
S_('breakdown', R(0, 160, 200, 40, ROAD) + car_side(90, 160, '#3c7fc1', 1.1) + ''.join(Ci(150 + k * 8, 80 - k * 16, 10 + k * 4, '#a7adb1', 'opacity=".8"') for k in range(3)) + Pa('M30,180 L44,156 L58,180 Z', '#e2463b') + Pa('M36,176 L44,162 L52,176 Z', '#f2ead8'), False)
S_('spare-tire', R(0, 160, 200, 40, ROAD) + Ci(100, 100, 60, '#2f3437') + Ci(100, 100, 32, '#c4cbd0') + Ci(100, 100, 10, '#5d6469') + R(150, 60, 36, 20, '#3c7fc1', 3, 'opacity="0"') + R(140, 30, 40, 26, '#e2463b', 3) + T(160, 49, '+1', 16, '#ffffff', 900), False)
S_('tow-truck', R(0, 160, 200, 40, ROAD) + G(R(-90, -50, 70, 44, '#f3c234', 4) + R(-80, -44, 30, 18, '#cfe8f6', 2) + R(-20, -20, 80, 14, '#5d6469') + St('M0,-20 L40,-70 L60,-40', '#5d6469', 6) + wheel(-70, -2, 12) + wheel(20, -2, 12) + R(-56, -60, 14, 10, '#f08a24', 2), 'translate(100,164)') + G(car_side(0, 0, '#3c7fc1', .55), 'translate(170,150) rotate(-15)'), False)
S_('gps', R(40, 40, 120, 100, '#2f3437', 10) + R(48, 48, 104, 84, '#e6f0d8', 4) + St('M60,120 L80,90 L110,100 L140,60', '#3c7fc1', 5) + Pa('M140,46 Q128,46 128,58 Q128,66 140,78 Q152,66 152,58 Q152,46 140,46 Z', '#e2463b') + Ci(140, 58, 4, '#ffffff') + Ci(60, 120, 6, '#5ba644') + R(90, 140, 20, 30, '#5d6469') + R(70, 166, 60, 10, '#5d6469', 3))
S_('airbag', R(0, 0, 200, 200, '#2f3437') + E(100, 90, 70, 60, '#ffffff') + E(90, 80, 40, 30, '#f2efe8') + steering(100, 170, 50) + St('M30,40 l-10,-10 M170,40 l10,-10', '#f3c234', 3), False)
S_('electric-car', R(0, 160, 200, 40, ROAD) + car_side(80, 160, '#5ba644', 1.0) + R(160, 70, 30, 90, '#e6ecef', 6) + R(166, 80, 18, 14, '#7fe08a', 2) + St('M160,120 Q140,120 140,130', '#2f3437', 4) + bolt_icon(80, 110, .4, '#ffffff'), False)
S_('speed-up', R(0, 160, 200, 40, ROAD) + car_side(110, 160, '#e2463b', 1.1) + ''.join(L(10, 110 + k * 14, 40 - k * 6, 110 + k * 14, '#a7adb1', 4) for k in range(3)) + arrow(120, 40, 190, 40, '#5ba644', 6) + arrow(120, 40, 170, 40, '#5ba644', 6), False)
S_('slow-down', R(0, 160, 200, 40, ROAD) + car_side(100, 160, '#3c7fc1', 1.1) + Pa('M150,30 L190,30 L190,70 L150,70 Z', '#f3c234', 'transform="rotate(45 170 50)"') + T(170, 58, '!', 24, '#2f3437', 900) + T(40, 50, '▼', 0, '#000') + arrow(60, 40, 20, 40, '#e2463b', 5), False)
S_('reverse', R(0, 160, 200, 40, ROAD) + car_side(110, 160, '#f08a24', 1.0) + arrow(60, 120, 10, 120, '#e2463b', 6) + R(140, 30, 40, 40, '#2f3437', 6) + T(160, 60, 'R', 26, '#ffffff', 900), False)
S_('warning-light', R(0, 0, 200, 200, '#2f3437') + Pa('M100,40 L170,160 L30,160 Z', '#f3c234') + Pa('M100,60 L150,148 L50,148 Z', '#e2463b') + R(94, 84, 12, 40, '#ffffff', 4) + Ci(100, 136, 7, '#ffffff'), False)
S_('service', R(0, 0, 200, 200, '#e6ecef') + R(0, 160, 200, 40, '#a7b0b8') + G(car_side(0, 0, '#3c7fc1', 1.0), 'translate(110,130)') + R(40, 130, 140, 10, '#e2463b') + R(50, 140, 10, 40, '#e2463b') + R(160, 140, 10, 40, '#e2463b') + G(R(-8, -10, 16, 100, '#a7adb1', 7) + Pa('M-22,-30 Q-28,-10 -8,-4 L8,-4 Q28,-10 22,-30 L12,-30 L12,-14 L-12,-14 L-12,-30 Z', '#a7adb1'), 'translate(30,60) rotate(-30) scale(.6)'), False)
S_('jack', R(0, 160, 200, 40, ROAD) + G(car_side(0, 0, '#5ba644', 1.0), 'translate(110,130) rotate(-6)') + Pa('M60,160 L70,130 L90,130 L100,160 Z', '#e2463b') + R(74, 110, 12, 24, '#a7adb1') + R(66, 106, 28, 6, '#5d6469') + St('M100,150 L140,150', '#5d6469', 4), False)

# ================= 汽车和公交 =================
S_('bus', R(0, 160, 200, 40, ROAD) + bus_side(100, 164, 1.1, '#3c7fc1'), False)
S_('taxi', R(0, 160, 200, 40, ROAD) + taxi_(100, 160, 1.3), False)
S_('van', R(0, 160, 200, 40, ROAD) + G(R(-80, -80, 130, 70, '#ffffff', 6) + Pa('M50,-80 L66,-80 Q80,-76 84,-50 L86,-10 L50,-10 Z', '#ffffff') + Pa('M54,-74 L64,-74 Q74,-70 76,-50 L54,-50 Z', '#cfe8f6') + R(-80, -30, 166, 6, '#5aa1d4') + wheel(-50, -6, 13) + wheel(56, -6, 13) + L(-20, -78, -20, -12, '#d9dcde', 2), 'translate(96,170) scale(1.1)'), False)
S_('get-on', R(0, 160, 200, 40, WALK) + G(R(-60, -110, 140, 104, '#3c7fc1', 6) + R(-40, -96, 40, 90, '#2f3437') + R(-36, -92, 32, 84, '#cfe8f6'), 'translate(100,166)') + fig(52, 180, 'oldwoman', s=.8) + arrow(70, 120, 90, 120, '#5ba644', 4), False)
S_('get-off', R(0, 160, 200, 40, WALK) + G(R(-60, -110, 140, 104, '#3c7fc1', 6) + R(-40, -96, 40, 90, '#2f3437') + R(-36, -92, 32, 84, '#cfe8f6'), 'translate(130,166)') + fig(60, 180, 'oldman', s=.8) + arrow(90, 120, 70, 120, '#e2463b', 4), False)
S_('fare', R(40, 60, 100, 120, '#f3c234', 8) + R(54, 74, 72, 30, '#2f3437', 4) + T(90, 96, '¥2', 18, '#7fe08a', 900) + R(80, 116, 20, 6, '#2f3437', 2) + coin_(150, 60, 16) + coin_(160, 100, 14))
S_('next-stop', R(0, 0, 200, 200, '#e6ecef') + R(20, 40, 160, 60, '#2f3437', 6) + T(100, 78, '▶ 人民公园', 18, '#f3c234', 800) + R(20, 120, 160, 12, '#5d6469', 4) + ''.join(Ci(40 + k * 40, 126, 8, '#e2463b' if k == 2 else '#ffffff') for k in range(4)) + R(170, 150, 20, 30, '#e2463b', 4) + T(180, 170, '●', 0, '#000'), False)
S_('bus-driver', R(0, 0, 200, 200, '#cfe8f6') + person_bust(80, 80, 30, '#3c7fc1', '#3a2a20', 'short') + Pa('M50,60 L110,60 L104,40 Q80,30 56,40 Z', '#2f4a7a') + R(46, 58, 70, 6, '#1f3a5a', 2) + steering(150, 170, 40), False)
S_('minibus', R(0, 160, 200, 40, ROAD) + G(R(-70, -70, 140, 60, '#f3c234', 10) + ''.join(R(-60 + k * 26, -62, 20, 20, '#cfe8f6', 3) for k in range(5)) + wheel(-40, -6, 12) + wheel(44, -6, 12), 'translate(100,166) scale(1.1)'), False)
S_('coach', R(0, 160, 200, 40, ROAD) + G(R(-90, -80, 180, 70, '#ffffff', 10) + R(-90, -54, 180, 8, '#e2463b') + ''.join(R(-80 + k * 30, -74, 24, 18, '#2f4a7a', 2) for k in range(6)) + R(-90, -30, 180, 10, '#5aa1d4') + wheel(-56, -6, 13) + wheel(56, -6, 13), 'translate(100,166) scale(1.05)'), False)
S_('bus-route', R(20, 20, 160, 160, '#ffffff', 6) + R(20, 20, 160, 30, '#3c7fc1', 6) + T(100, 42, '23', 18, '#ffffff', 900) + L(40, 100, 160, 100, '#3c7fc1', 6) + ''.join(Ci(40 + k * 30, 100, 8, '#ffffff', 'stroke="#3c7fc1" stroke-width="4"') + L(40 + k * 30, 116, 40 + k * 30, 150, '#a7adb1', 2) for k in range(5)))
S_('transfer', bus_side(60, 90, .5, '#3c7fc1') + train_side(130, 170, .5, '#e2463b') + St('M100,80 Q170,90 150,130', '#5ba644', 5) + Pa('M140,124 L152,140 L160,122 Z', '#5ba644') + fig(40, 190, 'man', s=.45))
S_('double-decker', R(0, 160, 200, 40, ROAD) + bus_side(100, 166, 1.0, '#e2463b', True), False)
S_('senior-card', G(R(-70, -44, 140, 88, '#e2463b', 8) + R(-56, -24, 40, 50, '#ffffff', 3) + Ci(-36, -6, 10, SK) + Pa('M-46,-8 Q-36,-20 -26,-8 Z', P['grey']) + Pa('M-50,22 Q-36,6 -22,22 Z', '#5aa1d4') + ''.join(L(0, -14 + k * 12, 56, -14 + k * 12, '#ffffff', 3) for k in range(3)) + heart(48, -28, 8, '#ffffff'), 'translate(100,100) rotate(-6)'))
S_('priority-seat', R(0, 0, 200, 200, '#e6ecef') + R(40, 90, 100, 20, '#e2463b', 6) + R(40, 40, 20, 60, '#e2463b', 6) + R(50, 110, 10, 60, '#5d6469') + R(120, 110, 10, 60, '#5d6469') + R(140, 20, 50, 50, '#3c7fc1', 6) + Ci(160, 34, 5, '#ffffff') + St('M160,40 L156,56 L166,60 M158,46 L150,52', '#ffffff', 3) + St('M168,48 L172,62', '#ffffff', 2) + heart(100, 60, 0), False)
S_('bus-lane', R(0, 0, 200, 200, ROAD) + R(60, 0, 80, 200, '#c0403a') + ''.join(R(56, 10 + k * 40, 4, 24, '#ffffff') + R(140, 10 + k * 40, 4, 24, '#ffffff') for k in range(5)) + T(100, 150, 'BUS', 24, '#ffffff', 900) + G(bus_side(0, 0, .35, '#3c7fc1'), 'translate(100,60) rotate(-90)'), False)

# ================= 摩托车 =================
S_('motorcycle', R(0, 160, 200, 40, ROAD) + moto(96, 164, 1.2), False)
S_('scooter', R(0, 160, 200, 40, ROAD) + G(wheel(-50, -18, 18) + wheel(54, -18, 18) + Pa('M-60,-30 L20,-30 L34,-60 L50,-80 L60,-80 L40,-50 L60,-24 L54,-14 L-60,-14 Z', '#5aa1d4') + R(-40, -50, 46, 10, '#2f3437', 5) + R(52, -84, 22, 6, '#2f3437', 3), 'translate(96,166) scale(1.15)'), False)
S_('rider', R(0, 160, 200, 40, ROAD) + moto(96, 164, 1.0) + P_rider if False else R(0, 160, 200, 40, ROAD) + moto(96, 164, 1.0) + pose((96, 60), (92, 80), (80, 112), arms=[[(98, 84), (120, 92), (138, 86)]], legs=[[(84, 114), (110, 120), (110, 150)]], shirt='#2f3437', pants='#3b4a5a', hr=14, tw=26) + helmet(96, 58, .4), False)
S_('passenger', R(0, 160, 200, 40, ROAD) + moto(110, 164, 1.0) + pose((112, 60), (108, 80), (96, 112), arms=[[(112, 84), (136, 92), (150, 86)]], legs=[[(100, 114), (126, 120), (126, 150)]], shirt='#3c7fc1', pants='#3b4a5a', hr=14, tw=26) + helmet(112, 58, .4, '#3c7fc1') + halo(72, 150, 110, 24) + pose((74, 64), (72, 84), (66, 114), arms=[[(78, 88), (96, 96)]], legs=[[(70, 116), (92, 120), (90, 150)]], shirt='#ef8fa4', pants='#3b4a5a', hr=13, tw=24) + helmet(74, 62, .38, '#ef8fa4'), False) if False else svg(R(0, 160, 200, 40, ROAD) + moto(110, 164, 1.0) + E(72, 100, 26, 56, '#f3c234', 'opacity=".25"') + pose((112, 60), (108, 80), (96, 112), arms=[[(112, 84), (136, 92), (150, 86)]], legs=[[(100, 114), (126, 120), (126, 150)]], shirt='#3c7fc1', pants='#3b4a5a', hr=14, tw=26) + helmet(112, 58, .4, '#3c7fc1') + pose((74, 64), (72, 84), (66, 114), arms=[[(78, 88), (96, 96)]], legs=[[(70, 116), (92, 120), (90, 150)]], shirt='#ef8fa4', pants='#3b4a5a', hr=13, tw=24) + helmet(74, 62, .38, '#ef8fa4'), False)
A['passenger'] = svg(R(0, 160, 200, 40, ROAD) + moto(110, 164, 1.0) + E(72, 100, 26, 56, '#f3c234', 'opacity=".25"') + pose((112, 60), (108, 80), (96, 112), arms=[[(112, 84), (136, 92), (150, 86)]], legs=[[(100, 114), (126, 120), (126, 150)]], shirt='#3c7fc1', pants='#3b4a5a', hr=14, tw=26) + helmet(112, 58, .4, '#3c7fc1') + pose((74, 64), (72, 84), (66, 114), arms=[[(78, 88), (96, 96)]], legs=[[(70, 116), (92, 120), (90, 150)]], shirt='#ef8fa4', pants='#3b4a5a', hr=13, tw=24) + helmet(74, 62, .38, '#ef8fa4'), False)
S_('crash-helmet', helmet(100, 110, 1.6))
S_('moped', R(0, 160, 200, 40, ROAD) + G(wheel(-46, -18, 18) + wheel(50, -18, 18) + St('M-46,-18 L-10,-40 L30,-40 L50,-18 M30,-40 L40,-76 L56,-76', '#e2463b', 6) + R(-30, -54, 36, 10, '#2f3437', 5) + Ci(10, -30, 10, '#5d6469') + R(-14, -30, 8, 10, '#a7adb1'), 'translate(96,166) scale(1.2)'), False)
S_('tricycle', R(0, 160, 200, 40, ROAD) + G(wheel(-60, -20, 18) + wheel(50, -20, 18) + St('M50,-20 L30,-50 L20,-80 L34,-80 M30,-50 L-20,-40', '#3c7fc1', 5) + R(-90, -60, 70, 40, '#c58b54', 3) + ''.join(L(-86 + k * 12, -60, -86 + k * 12, -20, '#a8703e', 2) for k in range(6)) + R(-4, -54, 26, 8, '#2f3437', 4), 'translate(110,166) scale(1.0)'), False)
S_('handlebars', R(0, 0, 200, 200, '#e6ecef') + St('M20,80 Q60,70 100,90 Q140,70 180,80', '#2f3437', 10) + R(10, 70, 30, 20, '#5d6469', 8) + R(160, 70, 30, 20, '#5d6469', 8) + R(94, 90, 12, 110, '#5d6469') + dash_icon(100, 130, 26) + R(36, 60, 20, 8, '#a7adb1', 3), False)
S_('license-plate', R(10, 60, 180, 80, '#3c7fc1', 8) + R(18, 68, 164, 64, 'none', 6, 'stroke="#ffffff" stroke-width="3"') + T(100, 116, '京A·88888', 30, '#ffffff', 900))
S_('leather-jacket', G(Pa('M-22,-34 L22,-34 L46,-18 L48,30 L34,32 L30,0 L28,36 L-28,36 L-30,0 L-34,32 L-48,30 L-46,-18 Z', '#2f2a27') + Pa('M-10,-34 L-20,-14 L-4,-8 Z M10,-34 L20,-14 L4,-8 Z', '#4a4440') + L(4, -30, -2, 36, '#a7adb1', 2) + R(-26, 14, 16, 3, '#a7adb1') + hi(-20, -10, 6, 14, .2), 'translate(100,104) scale(1.9)'))
S_('speedometer', Ci(100, 110, 80, '#2f3437') + Ci(100, 110, 70, '#1f2a35') + ''.join(L(100 + 56 * math.cos(a), 110 + 56 * math.sin(a), 100 + 66 * math.cos(a), 110 + 66 * math.sin(a), '#ffffff', 2.5) for a in [math.pi * .8 + k * math.pi * 1.4 / 10 for k in range(11)]) + ''.join(T(100 + 44 * math.cos(a), 114 + 44 * math.sin(a), str(k * 40), 9, '#ffffff', 700) for k, a in enumerate([math.pi * .8 + j * math.pi * 1.4 / 5 for j in range(6)])) + L(100, 110, 100 + 50 * math.cos(-.3), 110 + 50 * math.sin(-.3), '#e2463b', 4) + Ci(100, 110, 6, '#e2463b'))
S_('exhaust-pipe', R(0, 160, 200, 40, ROAD) + wheel(60, 140, 30) + G(R(-60, -10, 110, 20, '#c4cbd0', 10) + R(40, -12, 20, 24, '#a7adb1', 6), 'translate(110,140) rotate(-8)') + ''.join(Ci(176 + k * 6, 120 - k * 12, 8 + k * 4, '#a7adb1', 'opacity=".7"') for k in range(3)), False)
S_('sidecar', R(0, 160, 200, 40, ROAD) + moto(70, 164, .9) + G(Pa('M0,-20 Q0,-50 40,-50 Q70,-50 70,-20 Z', '#5ba644') + R(0, -24, 70, 14, '#4a9a3a', 6) + wheel(36, -6, 12), 'translate(116,166)'), False)
S_('visor', helmet(100, 110, 1.6, '#3c7fc1') + ring(130, 104, 40))
S_('kickstand', R(0, 160, 200, 40, ROAD) + G(moto(0, 0, 1.0), 'translate(96,160) rotate(-8)') + St('M80,140 L64,164', '#5d6469', 5) + ring(70, 154, 18), False)
S_('throttle', R(0, 0, 200, 200, '#e6ecef') + R(30, 80, 120, 20, '#2f3437', 10) + R(120, 74, 60, 32, '#5d6469', 12) + ''.join(L(126 + k * 8, 76, 126 + k * 8, 104, '#2f3437', 2) for k in range(6)) + G(R(-24, -16, 48, 34, SK, 12) + ''.join(R(-22 + k * 12, -30, 10, 20, SK, 5) for k in range(4)), 'translate(150,88)') + St('M150,140 a30,16 0 1,0 30,-20', '#5ba644', 4) + Pa('M176,114 L186,124 L174,128 Z', '#5ba644'), False)

# ================= 骑自行车 =================
S_('bicycle', R(0, 166, 200, 34, WALK) + bike_(100, 166, 1.15), False)
S_('ride', R(0, 166, 200, 34, WALK) + bike_(100, 166, 1.0) + pose((92, 50), (92, 70), (86, 104), arms=[[(98, 74), (110, 90), (118, 90)]], legs=[[(88, 106), (100, 124), (96, 140)]], back_leg=[[(84, 106), (80, 130), (88, 146)]], shirt='#e2463b', pants='#3b4a5a', hr=14, tw=24), False)
S_('bell', G(Ci(0, 0, 40, '#c4cbd0') + Ci(0, 0, 32, '#e6ecef') + Ci(0, 0, 10, '#a7adb1') + hi(-14, -14, 10, 6, .7, -30) + R(-6, 36, 12, 20, '#5d6469') + R(30, -6, 30, 12, '#5d6469', 4), 'translate(90,100) scale(1.3)') + St('M160,50 q10,10 0,20 M172,40 q16,20 0,40', '#e2463b', 3))
S_('cyclist', R(0, 166, 200, 34, WALK) + bike_(100, 166, 1.0, '#3c7fc1') + pose((112, 50), (102, 66), (82, 96), arms=[[(104, 70), (118, 86), (118, 92)]], legs=[[(84, 98), (100, 120), (96, 140)]], back_leg=[[(80, 98), (78, 124), (88, 146)]], shirt='#f3c234', pants='#2f3437', hr=13, tw=22) + Pa('M98,42 Q112,26 126,42 L126,48 L98,48 Z', '#e2463b'), False)
S_('bike-lane', R(0, 0, 200, 200, ROAD) + R(110, 0, 90, 200, '#3c8a3a') + ''.join(R(106, 10 + k * 34, 4, 20, '#ffffff') for k in range(6)) + G(bike_(0, 0, .6, '#ffffff'), 'translate(155,140)').replace('#2f3437', '#ffffff').replace('#f2ead8', '#3c8a3a') + car_side(50, 120, '#e2463b', .4), False)
S_('pedal', R(0, 0, 200, 200, '#e6ecef') + Ci(80, 110, 30, '#5d6469') + Ci(80, 110, 10, '#a7adb1') + St('M80,110 L140,150', '#5d6469', 10) + R(124, 140, 50, 20, '#2f3437', 4) + ''.join(R(128 + k * 10, 142, 6, 16, '#5d6469', 1) for k in range(4)) + G(Pa('M-30,0 L-30,-20 Q-28,-28 -18,-26 L-4,-16 Q14,-12 28,-8 Q36,-4 34,4 L-30,4 Z', '#3c7fc1'), 'translate(150,134)') + ring(150, 150, 34), False)
S_('chain', ''.join(G(R(-12, -6, 24, 12, 'none', 6, 'stroke="#5d6469" stroke-width="5"'), f'translate({30+k*18},{100+10*math.sin(k/1.5)}) rotate({math.degrees(math.atan(10/18/1.5*math.cos(k/1.5)))})') for k in range(9)) + Ci(30, 100, 20, 'none', 'stroke="#8a9196" stroke-width="3"') + Ci(170, 100, 14, 'none', 'stroke="#8a9196" stroke-width="3"'))
S_('saddle', G(Pa('M-60,-10 Q-60,-30 -20,-30 L50,-14 Q70,-10 70,0 Q60,10 30,10 L-40,14 Q-60,14 -60,-10 Z', '#2f3437') + hi(-20, -18, 20, 4, .3) + R(-6, 12, 12, 60, '#a7adb1'), 'translate(100,90) scale(1.3)'))
S_('lock', St('M70,90 L70,60 A30,30 0 0,1 130,60 L130,90', '#a7adb1', 12) + R(56, 86, 88, 80, '#e2463b', 10) + Ci(100, 120, 10, '#2f3437') + R(96, 120, 8, 22, '#2f3437', 3))
S_('pump', R(80, 40, 30, 130, '#e2463b', 8) + R(90, 20, 10, 24, '#a7adb1') + R(60, 14, 70, 12, '#2f3437', 6) + R(60, 166, 70, 12, '#2f3437', 4) + St('M110,150 Q150,160 160,120 Q166,100 150,90', '#2f3437', 5) + G(R(-14, -10, 28, 26, SK, 8), 'translate(96,30)'))
S_('puncture', Ci(100, 110, 70, '#2f3437') + Ci(100, 110, 44, '#f2ead8') + G(R(-3, -24, 6, 30, '#a7adb1') + R(-8, -28, 16, 6, '#8a9196', 2), 'translate(150,70) rotate(40)') + ''.join(Ci(154 + k * 6, 60 - k * 6, 3, '#c4cbd0') for k in range(3)) + St('M138,60 l-10,-10', '#f3c234', 3))
S_('electric-bike', R(0, 166, 200, 34, WALK) + bike_(100, 166, 1.15, '#5ba644') + R(70, 104, 40, 18, '#2f3437', 4) + bolt_icon(90, 113, .2, '#f3c234'), False)
S_('shared-bike', R(0, 166, 200, 34, WALK) + ''.join(bike_(40 + k * 60, 166 - (k % 2) * 4, .6, '#f3c234') for k in range(3)) + R(140, 30, 50, 50, '#ffffff', 4) + ''.join(R(146 + (k % 5) * 8, 36 + (k // 5) * 8, 6, 6, '#2f3437' if (k * 7) % 3 else '#ffffff') for k in range(25)), False)
S_('reflector', wheel(100, 100, 70, '#2f3437', '#f2ead8') + ''.join(L(100, 100, 100 + 58 * math.cos(a), 100 + 58 * math.sin(a), '#c4cbd0', 1.5) for a in [k * math.pi / 8 for k in range(16)]) + R(130, 70, 24, 12, '#f08a24', 4) + R(46, 120, 24, 12, '#f08a24', 4) + St('M160,60 l10,-8 M164,74 l12,0', '#f3c234', 3))
S_('mountain-bike', R(0, 0, 200, 200, SKY) + Pa('M0,170 L60,90 L100,130 L150,70 L200,140 L200,200 L0,200 Z', '#7a9a5a') + Pa('M60,90 L72,106 L48,106 Z M150,70 L162,86 L138,86 Z', '#ffffff') + bike_(100, 186, .9, '#2f5a8a'), False)
S_('tandem', R(0, 166, 200, 34, WALK) + G(wheel(-70, -26, 24, '#2f3437', '#f2ead8') + wheel(70, -26, 24, '#2f3437', '#f2ead8') + St('M-70,-26 L-40,-60 L40,-60 L70,-26 M-40,-60 L-30,-26 L30,-26 L40,-60 M-30,-26 L-44,-70 M30,-26 L18,-70', '#e2463b', 5) + R(-56, -76, 22, 6, '#2f3437', 3) + R(6, -76, 22, 6, '#2f3437', 3), 'translate(100,166)'), False)

# ================= 火车 =================
S_('train', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8a837c') + ''.join(R(k * 20, 172, 12, 4, '#5a3a24') for k in range(10)) + L(0, 168, 200, 168, '#5d6469', 3) + train_side(90, 166, 1.0, '#3c8a3a', False) + R(150, 96, 40, 64, '#3c8a3a', 4) + R(160, 70, 14, 30, '#2f3437') + ''.join(Ci(170 + k * 8, 60 - k * 14, 8 + k * 3, '#c4cbd0', 'opacity=".8"') for k in range(3)), False)
S_('subway', R(0, 0, 200, 200, '#e6ecef') + Pa('M0,40 Q100,0 200,40 L200,200 L0,200 Z', '#c4cbd0') + R(10, 70, 180, 90, '#e6ecef', 20) + R(10, 100, 180, 14, '#3c7fc1') + ''.join(R(20 + k * 44, 76, 34, 22, '#2f3437', 3) for k in range(4)) + R(80, 116, 40, 44, '#cfe8f6', 2) + L(100, 116, 100, 160, '#a7adb1', 2) + R(0, 160, 200, 40, WALK) + Ci(30, 30, 16, '#3c7fc1') + T(30, 36, 'M', 16, '#ffffff', 900), False)
S_('platform', R(0, 0, 200, 200, '#e6ecef') + R(0, 30, 200, 10, '#5d6469') + R(0, 120, 200, 80, WALK) + R(0, 120, 200, 8, '#f3c234') + train_side(110, 116, .9, '#e2463b') + fig(40, 196, 'oldman', s=.5) + suitcase(64, 190, 20, 26, '#3c7fc1') + R(150, 40, 40, 30, '#2f3437', 3) + T(170, 60, '3', 18, '#f3c234', 900), False)
S_('arrive', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, WALK) + train_side(70, 146, .8, '#e2463b') + St('M140,60 l20,0', '#a7adb1', 0) + R(140, 60, 50, 50, '#ffffff', 4) + Pa('M150,90 L170,70 L170,80 L180,80 L180,100 L170,100 L170,110 Z', '#5ba644', 'transform="rotate(90 165 90)"') + fig(170, 196, 'woman', arms='wave', s=.45) + flag if False else R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, WALK) + train_side(70, 146, .8, '#e2463b') + R(140, 40, 50, 50, '#3c8a3a', 4) + arrow(165, 50, 165, 80, '#ffffff', 5) + R(150, 82, 30, 4, '#ffffff') + fig(170, 196, 'woman', arms='wave', s=.45), False)
S_('leave', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, WALK) + train_side(120, 146, .8, '#e2463b') + ''.join(L(10, 110 + k * 12, 30 - k * 4, 110 + k * 12, '#a7adb1', 3) for k in range(3)) + fig(30, 196, 'oldwoman', arms='wave', s=.45) + arrow(140, 40, 190, 40, '#e2463b', 5), False)
S_('ticket-office', R(0, 0, 200, 200, '#e6dcc8') + R(20, 30, 160, 30, '#3c7fc1', 3) + ticket_(100, 45, .4, 0, '#f3c234') + ''.join(R(30 + k * 60, 70, 50, 60, '#cfe8f6', 2) + R(30 + k * 60, 126, 50, 10, '#a7adb1') for k in range(3)) + R(0, 136, 200, 64, '#c8a070') + fig(100, 196, 'man', s=.4) + fig(130, 196, 'woman', s=.38), False)
S_('high-speed-train', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#8a837c') + G(Pa('M-100,-40 L60,-40 Q110,-36 120,0 L-100,0 Z', '#ffffff') + Pa('M40,-38 Q80,-34 96,-14 L40,-14 Z', '#2f3437') + R(-100, -14, 210, 6, '#3c7fc1') + ''.join(R(-90 + k * 26, -32, 18, 10, '#2f3437', 2) for k in range(5)), 'translate(90,150)') + ''.join(L(0, 100 + k * 14, 30, 100 + k * 14, '#a7adb1', 3) for k in range(3)), False)
S_('carriage', R(0, 0, 200, 200, '#e6ecef') + Pa('M0,20 L200,20 L200,60 L0,60 Z', '#cfe8f6') + ''.join(R(20 + (k % 2) * 110, 70 + (k // 2) * 44, 50, 36, '#3c7fc1', 6) + R(20 + (k % 2) * 110, 64 + (k // 2) * 44, 50, 10, '#5aa1d4', 4) for k in range(6)) + Pa('M80,200 L90,60 L110,60 L120,200 Z', '#c4cbd0'), False)
S_('timetable', R(20, 20, 160, 160, '#2f3437', 6) + R(28, 28, 144, 22, '#3c7fc1', 2) + ''.join(T(60, 74 + k * 24, ['08:15', '09:40', '11:05', '13:30', '15:50'][k], 14, '#f3c234', 800) + T(126, 74 + k * 24, ['G1', 'D7', 'G23', 'K5', 'G9'][k], 14, '#ffffff', 700) for k in range(5)) + clock(170, 30, 14, (9, 0)))
S_('seat-number', R(40, 50, 120, 120, '#3c7fc1', 10) + R(40, 40, 120, 30, '#5aa1d4', 8) + R(70, 80, 60, 40, '#ffffff', 4) + T(100, 110, '12A', 24, '#2f3437', 900) + R(50, 160, 10, 30, '#5d6469') + R(140, 160, 10, 30, '#5d6469'))
S_('one-way-ticket', ticket_(100, 90, 1.4, -6, '#9fd0ec', '') + arrow(56, 92, 116, 86, '#2f3437', 4) + ticket_(100, 90, 0, 0))
S_('round-trip-ticket', ticket_(100, 90, 1.4, -6, '#f3c234', '') + arrow(56, 82, 116, 76, '#2f3437', 3) + arrow(116, 98, 56, 104, '#2f3437', 3))
S_('sleeper', R(0, 0, 200, 200, '#e6ecef') + R(10, 20, 10, 170, '#8a9196') + R(180, 20, 10, 170, '#8a9196') + ''.join(R(20, 50 + k * 54, 160, 30, '#5aa1d4', 4) + R(24, 44 + k * 54, 36, 14, '#ffffff', 6) + R(64, 44 + k * 54, 112, 18, '#9fd0ec', 4) for k in range(3)) + ladder_(150, 190, 150, 40, 20, '#a7adb1', 6) + zzz(80, 40, .6), False)
S_('dining-car', R(0, 0, 200, 200, '#e6dcc8') + R(0, 20, 200, 50, '#cfe8f6') + ''.join(L(k * 50, 20, k * 50, 70, '#ffffff', 4) for k in range(5)) + table_(100, 110, 100, 60, '#ffffff') + bowl(80, 100, 30) + coffee_cup_s if False else R(0, 0, 200, 200, '#e6dcc8') + R(0, 20, 200, 50, '#cfe8f6') + ''.join(L(k * 50, 20, k * 50, 70, '#ffffff', 4) for k in range(5)) + table_(100, 110, 100, 60, '#ffffff') + bowl(80, 98, 30) + E(124, 106, 16, 4, '#ffffff') + E(124, 104, 10, 3, '#e0915a') + R(20, 90, 30, 70, '#e2463b', 8) + R(150, 90, 30, 70, '#e2463b', 8), False)
S_('change-trains', train_side(70, 80, .6, '#e2463b') + train_side(130, 170, .6, '#3c7fc1') + St('M60,96 Q40,130 90,140', '#5ba644', 5) + Pa('M86,132 L100,142 L86,150 Z', '#5ba644') + fig(150, 110, 'man', s=.35))
S_('conductor', R(0, 0, 200, 200, '#e6ecef') + person_bust(100, 84, 30, '#2f4a7a', '#3a2a20', 'short') + Pa('M70,64 L130,64 L124,44 Q100,34 76,44 Z', '#2f4a7a') + R(66, 62, 68, 6, '#1f3a5a', 2) + R(94, 50, 12, 8, '#f3c234', 2) + R(120, 140, 30, 20, '#f3c234', 2) + St('M60,140 l20,10', '#f3c234', 0), False)

# ================= 飞机 =================
S_('airplane', R(0, 0, 200, 200, SKY) + E(40, 160, 30, 10, '#ffffff') + E(160, 40, 30, 10, '#ffffff') + plane_(100, 100, .95, -10), False)
S_('fly', R(0, 0, 200, 200, SKY) + plane_(120, 70, .6, -20) + St('M10,170 Q60,140 80,110', '#ffffff', 3, 'stroke-dasharray="6 6"') + E(50, 60, 26, 8, '#ffffff') + E(150, 160, 30, 10, '#ffffff'), False)
S_('flight', R(20, 30, 160, 140, '#2f3437', 6) + R(28, 38, 144, 22, '#f3c234', 2) + plane_(44, 49, .1, 0) + ''.join(T(70, 82 + k * 22, ['CA981', 'MU587', 'CZ3101', 'HU7801'][k], 12, '#ffffff', 800) + T(140, 82 + k * 22, ['10:20', '11:05', '12:40', '13:15'][k], 12, '#7fe08a', 800) for k in range(4)))
S_('wing', R(0, 0, 200, 200, SKY) + Pa('M0,120 L40,90 L200,140 L200,160 Z', '#e6ecef') + Pa('M0,120 L40,90 L60,96 L20,126 Z', '#c4cbd0') + E(90, 130, 20, 8, '#a7adb1') + R(0, 0, 50, 70, '#2f3437', 14) + R(6, 6, 38, 58, '#cfe8f6', 10) + E(130, 40, 30, 10, '#ffffff'), False)
S_('helicopter', R(0, 0, 200, 200, SKY) + heli(110, 100, 1.0), False)
S_('take-off', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, ROAD) + ''.join(R(10 + k * 40, 182, 20, 4, '#ffffff') for k in range(5)) + plane_(110, 110, .7, -25) + arrow(150, 60, 186, 30, '#5ba644', 4), False)
S_('land', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, ROAD) + ''.join(R(10 + k * 40, 182, 20, 4, '#ffffff') for k in range(5)) + plane_(100, 120, .7, 12) + arrow(40, 60, 70, 90, '#3c7fc1', 4), False)
S_('flight-attendant', R(0, 0, 200, 200, '#e6ecef') + person_bust(100, 80, 30, '#3c7fc1', '#2a1a10', 'bun', 'dot', 'smile') + Pa('M86,110 L100,128 L114,110 Z', '#ffffff') + Pa('M92,114 L100,124 L108,114 Z', '#e2463b') + Pa('M72,58 L128,58 L120,46 L80,46 Z', '#3c7fc1') + R(140, 140, 50, 50, '#c4cbd0', 4) + R(146, 146, 38, 20, '#a7adb1', 2) + plane_(40, 30, .12, 0), False)
S_('window-seat', R(0, 0, 200, 200, '#e6ecef') + R(110, 30, 70, 90, '#c4cbd0', 34) + R(118, 38, 54, 74, '#a9d8f2', 28) + E(140, 80, 20, 6, '#ffffff') + R(30, 70, 70, 110, '#3c7fc1', 14) + R(36, 60, 58, 40, '#5aa1d4', 12) + ring(146, 76, 44), False)
S_('aisle-seat', R(0, 0, 200, 200, '#e6ecef') + ''.join(R(10 + k * 48, 80, 40, 90, '#3c7fc1', 10) for k in range(2)) + ''.join(R(140 + k * 48, 80, 40, 90, '#3c7fc1', 10) for k in range(2)) + Pa('M100,200 L106,60 L134,60 L140,200 Z', '#c4cbd0') + halo(76, 170, 100, 26), False)
S_('cabin', R(0, 0, 200, 200, '#e6ecef') + Pa('M0,0 L200,0 L160,50 L40,50 Z', '#f6f8fa') + ''.join(R(20 + (k % 2) * 110, 60 + (k // 2) * 46, 50, 38, '#3c7fc1', 8) for k in range(6)) + Pa('M80,200 L90,50 L110,50 L120,200 Z', '#c4cbd0') + ''.join(R(4 + k * 160, 50, 30, 18, '#d9dcde', 4) for k in range(2)), False)
S_('cockpit', R(0, 0, 200, 200, '#2f3437') + Pa('M10,90 L40,20 L160,20 L190,90 Z', '#a9d8f2') + L(100, 20, 100, 90, '#2f3437', 6) + R(10, 100, 180, 60, '#3a3f44', 6) + ''.join(dash_icon(36 + k * 32, 126, 13) for k in range(5)) + St('M70,200 L70,170 L130,170 L130,200', '#5d6469', 8), False)
S_('jet-lag', big_face(80, 110, 50, eyes='closed', m='o', brows='sad') + clock(156, 50, 26, (3, 0)) + Pa('M150,110 A14,14 0 1,0 166,130 A11,11 0 1,1 150,110 Z', '#7a6ab8') + Ci(150, 160, 12, '#f3c234') + zzz(110, 50, .7) + plane_(40, 30, .15, 0))
S_('turbulence', R(0, 0, 200, 200, '#8a9aa8') + ''.join(E(30 + k * 50, 160 - (k % 2) * 100, 30, 12, '#c4cbd0') for k in range(4)) + G(plane_(0, 0, .6, 0), 'translate(100,100) rotate(-10)') + St('M40,100 l-14,-8 M40,110 l-14,8 M160,90 l14,-8 M160,100 l14,8', '#f3c234', 3) + Pa('M150,30 L140,50 L150,50 L142,70 L164,44 L152,44 L160,30 Z', '#f3c234'), False)
S_('life-jacket', G(Pa('M-40,-50 L-16,-50 Q-10,-30 0,-30 Q10,-30 16,-50 L40,-50 L46,50 L-46,50 Z', '#f08a24') + L(0, -30, 0, 50, '#d9741a', 3) + R(-40, 0, 80, 8, '#2f3437') + R(-6, -2, 12, 12, '#a7adb1', 2) + ''.join(R(-36, -30 + k * 30, 6, 16, '#ffffff', 2, 'opacity=".5"') for k in range(3)), 'translate(100,110) scale(1.4)'))
S_('overhead-locker', R(0, 0, 200, 200, '#e6ecef') + Pa('M10,20 L190,20 L190,80 Q100,96 10,80 Z', '#f6f8fa') + Pa('M10,80 Q100,96 190,80 L190,90 Q100,106 10,90 Z', '#c4cbd0') + Pa('M110,30 L180,30 L190,10 L120,0 Z', '#ffffff') + suitcase(140, 74, 40, 40, '#e2463b') + R(40, 50, 50, 26, '#3c7fc1', 6) + arrow(150, 150, 150, 100, '#5ba644', 4) + ''.join(R(20 + k * 48, 130, 40, 70, '#3c7fc1', 8) for k in range(2)), False)

# ================= 机场 =================
S_('passport', passport_(100, 100, 1.5, -8))
S_('ticket', ticket_(100, 100, 1.5, -8, '#f3c234', '¥'))
S_('suitcase', suitcase(100, 170, 100, 120, '#e2463b') + R(66, 70, 30, 30, '#f3c234', 4, 'opacity=".0"'))
S_('gate-airport', R(0, 0, 200, 200, '#e6ecef') + R(0, 130, 200, 70, '#c4cbd0') + R(20, 20, 70, 40, '#f3c234', 4) + T(55, 50, 'A12', 22, '#2f3437', 900) + plane_(150, 100, .4, 0) + R(110, 70, 90, 60, '#a9d8f2', 2, 'opacity=".5"') + R(30, 70, 60, 60, '#2f3437', 3) + R(36, 76, 48, 54, '#5d6469') + fig(60, 196, 'man', s=.45), False)
S_('check-in', R(0, 0, 200, 200, '#e6ecef') + R(0, 110, 200, 90, '#c4cbd0') + R(10, 80, 120, 30, '#5d6469', 4) + R(20, 40, 50, 30, '#2f3437', 3) + T(45, 60, '✓', 16, '#7fe08a', 900) + person_bust(100, 60, 18, '#3c7fc1', '#3a2a20', 'bun') + suitcase(160, 150, 40, 54, '#5ba644') + passport_(70, 100, .3, 0), False)
S_('delay', R(20, 30, 160, 140, '#2f3437', 6) + ''.join(T(60, 70 + k * 26, ['CA981', 'MU587', 'CZ310', 'HU780'][k], 12, '#ffffff', 800) + T(140, 70 + k * 26, ['已延误' if k == 1 else '准点'][0], 12, '#ff4a3a' if k == 1 else '#7fe08a', 800) for k in range(4)) + R(28, 78, 144, 22, '#ff4a3a', 2, 'opacity=".2"') + clock(170, 170, 20, (5, 0)))
S_('departure', R(0, 0, 200, 200, '#e6ecef') + R(30, 30, 140, 70, '#3c7fc1', 6) + plane_(100, 64, .4, -25) + R(97, 100, 6, 90, '#8a9196') + arrow(60, 140, 140, 140, '#5ba644', 0), False)
S_('arrival', R(0, 0, 200, 200, '#e6ecef') + R(30, 30, 140, 70, '#5ba644', 6) + plane_(100, 64, .4, 20) + R(97, 100, 6, 90, '#8a9196'), False)
S_('boarding-pass', G(R(-90, -44, 180, 88, '#ffffff', 6) + R(-90, -44, 180, 22, '#3c7fc1', 6) + R(-90, -30, 180, 8, '#3c7fc1') + plane_(-70, -33, .1, 0) + ''.join(L(-80, -6 + k * 12, 10, -6 + k * 12, '#a7adb1', 3) for k in range(4)) + L(30, -22, 30, 44, '#d9dcde', 2) + ''.join(R(40 + k * 4, 0, 2 + (k % 2), 30, '#2f3437') for k in range(10)), 'translate(100,100) rotate(-6)'))
S_('security-check', R(0, 0, 200, 200, '#e6ecef') + R(0, 140, 200, 60, '#c4cbd0') + R(60, 30, 80, 140, 'none', 6, 'stroke="#8a9196" stroke-width="10"') + fig(100, 166, 'man', s=.7, arms='up') + R(150, 90, 40, 60, '#5d6469', 4) + R(156, 96, 28, 20, '#7fe08a', 2), False)
S_('customs', R(0, 0, 200, 200, '#e6ecef') + R(0, 120, 200, 80, '#c4cbd0') + officer(70, 70, 22) + R(20, 116, 110, 12, '#5d6469') + passport_(130, 110, .35, 0) + suitcase(170, 170, 40, 50, '#3c7fc1') + R(140, 30, 50, 30, '#2f3437', 3), False)
S_('visa', passport_(70, 100, 1.0, -6) + G(R(-46, -60, 92, 120, '#ffffff', 4) + R(-38, -40, 30, 36, '#a9d8f2') + ''.join(L(0, -36 + k * 12, 36, -36 + k * 12, '#a7adb1', 2) for k in range(4)) + R(-38, 10, 76, 30, '#7a4fa0', 2, 'opacity=".2"') + Ci(20, 24, 14, 'none', 'stroke="#e2463b" stroke-width="3"'), 'translate(130,100) rotate(8)'))
S_('baggage-claim', R(0, 0, 200, 200, '#e6ecef') + E(100, 150, 90, 30, '#5d6469') + E(100, 146, 78, 22, '#8a9196') + suitcase(60, 150, 30, 36, '#e2463b') + suitcase(110, 156, 34, 30, '#5ba644') + suitcase(150, 146, 28, 34, '#f3c234') + R(20, 20, 160, 40, '#f3c234', 4) + suitcase(60, 52, 20, 20, '#2f3437') + arrow(90, 40, 150, 40, '#2f3437', 3), False)
S_('duty-free', R(0, 180, 200, 20, '#c4cbd0') + storefront(20, 40, 160, 140, '#f6efe0', '#7a4fa0', sign='#7a4fa0', door=False) + T(100, 58, '%', 18, '#ffffff', 900) + R(40, 110, 20, 40, '#f6c8dc', 4) + R(70, 120, 20, 30, '#c8782a', 3) + R(100, 104, 24, 46, '#5ba644', 4) + R(132, 116, 26, 34, '#e2463b', 4), False)
S_('trolley', G(Pa('M-40,0 L40,0 L40,10 L-40,10 Z', '#5d6469') + St('M30,0 L50,-110 L60,-110', '#5d6469', 6) + suitcase(0, 0, 60, 60, '#e2463b') + suitcase(4, -60, 40, 34, '#3c7fc1') + wheel(-30, 18, 8) + wheel(30, 18, 8), 'translate(90,160)'))
S_('connecting-flight', R(0, 0, 200, 200, SKY) + Ci(100, 120, 12, '#e2463b') + St('M20,170 Q60,100 100,120', '#ffffff', 3, 'stroke-dasharray="6 5"') + St('M100,120 Q140,60 180,40', '#ffffff', 3, 'stroke-dasharray="6 5"') + plane_(40, 150, .2, -40) + plane_(170, 46, .2, -30) + T(100, 150, '✈', 0, '#000'), False)

# ================= 船 =================
S_('boat', sea(130) + boat_hull(100, 150, 120, 30, '#c8903a', '#8a5a35') + L(100, 120, 100, 60, '#5d6469', 0), False)
S_('ship', sea(130) + boat_hull(100, 156, 170, 40, '#ffffff', '#2f3437') + R(50, 90, 90, 26, '#ffffff') + R(60, 70, 50, 22, '#ffffff') + ''.join(R(56 + k * 16, 98, 10, 8, '#2f4a7a') for k in range(5)) + R(110, 50, 18, 30, '#e2463b') + R(110, 50, 18, 6, '#2f3437'), False)
S_('ferry', sea(130) + boat_hull(100, 156, 170, 30, '#ffffff', '#3c7fc1') + R(30, 100, 140, 30, '#ffffff') + R(30, 120, 140, 6, '#3c7fc1') + ''.join(R(36 + k * 20, 106, 14, 10, '#2f4a7a') for k in range(7)) + car_side(70, 96, '#e2463b', .25) + car_side(130, 96, '#f3c234', .25), False)
S_('captain', R(0, 0, 200, 200, SKY) + person_bust(100, 84, 30, '#ffffff', P['grey'], 'grey') + Pa('M70,62 L130,62 L124,40 Q100,30 76,40 Z', '#ffffff') + R(66, 60, 68, 8, '#1f3a5a', 2) + anchor_(100, 50, .12, '#d9a33a') + R(70, 140, 20, 6, '#d9a33a') + R(110, 140, 20, 6, '#d9a33a') + Pa('M70,180 Q74,164 82,178', 'none', 'stroke="none"') + Ci(120, 170, 0, '#000'), False)
S_('cruise-ship', sea(140) + boat_hull(100, 166, 190, 40, '#ffffff', '#2f4a7a') + ''.join(R(14 + k * 4, 126 - k * 16, 172 - k * 12, 16, '#ffffff') + ''.join(Ci(26 + k * 4 + j * 14, 134 - k * 16, 3, '#2f4a7a') for j in range(int((172 - k * 12) / 14))) for k in range(4)) + R(120, 50, 20, 26, '#e2463b'), False)
S_('sailboat', sea(140) + boat_hull(100, 160, 110, 26, '#ffffff', '#3c7fc1') + L(100, 134, 100, 30, '#5d6469', 4) + Pa('M104,34 L104,124 L160,124 Z', '#ffffff') + Pa('M96,40 L96,124 L50,124 Z', '#f3c234'), False)
S_('deck', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 30, SEA) + Pa('M0,130 L200,130 L200,200 L0,200 Z', '#c8a070') + ''.join(L(0, 140 + k * 14, 200, 140 + k * 14, '#a8803a', 2) for k in range(5)) + R(0, 110, 200, 6, '#ffffff') + ''.join(R(10 + k * 30, 110, 4, 22, '#ffffff') for k in range(7)) + chair_side(140, 186, '#5aa1d4', .6) + fig(60, 196, 'oldwoman', s=.5), False)
S_('anchor', anchor_(100, 100, 1.5))
S_('lifeboat', sea(150) + boat_hull(100, 170, 120, 30, '#f08a24', '#e2463b') + Pa('M50,140 Q100,110 150,140 Z', '#f08a24') + Ci(70, 154, 8, 'none', 'stroke="#ffffff" stroke-width="4"') + St('M60,40 L60,140 M140,40 L140,140', '#5d6469', 3) + R(40, 34, 120, 8, '#5d6469', 3), False)
S_('seasick', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, SEA) + big_face(100, 90, 50, eyes='shut', m='wavy', brows='sad') + E(100, 96, 40, 30, '#9bc77a', 'opacity=".45"') + G(boat_hull(0, 0, 140, 30, '#ffffff', '#3c7fc1'), 'translate(100,190) rotate(-8)') + St('M30,40 q10,-6 20,0 t20,0 M140,40 q10,-6 20,0 t20,0', '#7fae5a', 3), False)
S_('yacht', sea(140) + Pa('M20,130 L180,130 Q170,160 140,166 L40,166 Z', '#ffffff') + Pa('M50,130 L70,106 L150,106 L170,130 Z', '#ffffff') + R(76, 110, 60, 10, '#2f3437', 3) + Pa('M80,106 L96,86 L130,86 L140,106 Z', '#e6ecef') + L(20, 150, 180, 150, '#3c7fc1', 3), False)
S_('canoe', sea(120) + Pa('M20,140 Q100,170 180,140 Q100,154 20,140 Z', '#c8603a') + Pa('M20,140 Q100,154 180,140 L176,136 Q100,146 24,136 Z', '#e0905a') + fig(100, 150, 'man', s=.35) + St('M60,90 L140,170', '#8a5a35', 4) + E(140, 172, 8, 14, '#8a5a35', 'transform="rotate(-45 140 172)"'), False)
S_('rowing-boat', sea(120) + boat_hull(100, 160, 120, 30, '#c8903a', '#8a5a35') + St('M20,120 L180,170', '#8a5a35', 4) + St('M20,170 L180,120', '#8a5a35', 4) + E(20, 120, 10, 5, '#8a5a35') + E(180, 120, 10, 5, '#8a5a35'), False)
S_('raft', sea(130) + ''.join(R(30, 130 + k * 0, 140, 0, '#000') for k in range(0)) + ''.join(R(30 + k * 18, 120, 16, 50, '#c8903a', 6) for k in range(8)) + L(30, 132, 174, 132, '#8a5a35', 4) + L(30, 158, 174, 158, '#8a5a35', 4) + L(100, 120, 100, 50, '#8a5a35', 4) + Pa('M104,54 L150,70 L104,96 Z', '#f6efe0'), False)
S_('submarine', R(0, 0, 200, 200, '#2f5a8a') + ''.join(Ci(30 + k * 40, 40 + (k % 2) * 30, 4, '#9fd0ec', 'opacity=".6"') for k in range(5)) + E(100, 120, 80, 30, '#f3c234') + R(80, 74, 36, 30, '#f3c234', 6) + R(94, 50, 6, 26, '#5d6469') + R(94, 50, 20, 6, '#5d6469') + ''.join(Ci(60 + k * 26, 120, 8, '#9fd0ec') for k in range(4)) + Pa('M180,120 L196,100 L196,140 Z', '#e0a820'), False)
S_('speedboat', sea(130) + Pa('M20,130 L170,130 Q190,136 186,150 L40,150 Z', '#e2463b') + Pa('M70,130 L100,110 L130,110 L140,130 Z', '#cfe8f6') + Pa('M20,136 L186,140', 'none', 'stroke="#ffffff" stroke-width="4"') + St('M10,150 q-10,10 -10,20 M20,154 q-10,14 -16,20', '#ffffff', 3) + ''.join(L(0, 120 + k * 8, 14, 120 + k * 8, '#ffffff', 2) for k in range(3)), False)

# ================= 港口 =================
S_('port', sea(120) + R(0, 100, 200, 20, '#a7a09a') + ''.join(container_(10 + (k % 4) * 30, 70 + (k // 4) * 16, 28, 14, ['#e2463b', '#3c7fc1', '#5ba644', '#f08a24'][(k + k // 4) % 4]) for k in range(8)) + St('M150,100 L150,20 L190,20 M150,30 L130,30', '#f3c234', 5) + L(180, 20, 180, 60, '#5d6469', 2) + boat_hull(100, 170, 150, 30, '#2f4a7a', '#e2463b') + ''.join(container_(50 + k * 22, 126, 20, 14, ['#e2463b', '#f3c234', '#3c7fc1', '#5ba644'][k]) for k in range(4)), False)
S_('harbor', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, SEA) + Pa('M0,100 Q60,90 80,120 L0,140 Z', '#c4bcae') + Pa('M200,90 Q140,90 120,120 L200,140 Z', '#c4bcae') + boat_hull(100, 156, 50, 14, '#ffffff', '#e2463b') + L(100, 142, 100, 116, '#5d6469', 2) + Pa('M102,118 L120,138 L102,138 Z', '#ffffff') + lighthouse(180, 100, .4) + house(30, 100, 30, 16), False)
S_('pier', sea(110) + Pa('M0,120 L130,120 L130,132 L0,132 Z', '#a8703e') + ''.join(R(10 + k * 24, 132, 6, 60, '#7a5030') for k in range(6)) + ''.join(L(k * 14, 120, k * 14, 132, '#8a5a35', 1.5) for k in range(10)) + fig(110, 120, 'oldman', s=.4) + St('M120,90 Q160,90 170,150', '#5d6469', 1.5), False)
S_('dock', sea(130) + R(0, 110, 200, 20, '#a7a09a') + ''.join(R(20 + k * 60, 96, 14, 16, '#2f3437', 3) for k in range(3)) + boat_hull(100, 170, 160, 36, '#2f4a7a', '#e2463b') + St('M34,104 L60,140 M154,104 L140,140', '#c8a070', 3), False)
S_('lighthouse', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, SEA) + Pa('M60,170 Q90,140 140,150 L150,180 L50,180 Z', '#8a837c') + lighthouse(100, 160, 1.0), False)
S_('container', container_(20, 90, 160, 80, '#e2463b') + Pa('M20,90 L50,60 L200,60 L180,90 Z', '#c0302a') + Pa('M180,90 L200,60 L200,140 L180,170 Z', '#a8241f'))
S_('cargo', box_(20, 110, 70, 70) + box_(90, 120, 60, 60, '#c8a070') + box_(50, 50, 60, 60, '#d9b880') + St('M150,40 L150,10 M150,40 L120,60', '#5d6469', 3) + R(140, 120, 50, 60, '#a7a09a', 3, 'opacity=".0"') + G(R(-20, -10, 40, 30, '#5d6469', 2), 'translate(160,170)'))
S_('fishing-boat', sea(130) + boat_hull(100, 166, 140, 34, '#3c7fc1', '#e2463b') + R(100, 100, 40, 32, '#ffffff') + St('M60,132 L40,40 L170,90', '#5d6469', 3) + ''.join(L(60 + k * 12, 60 + k * 3, 60 + k * 12, 140, '#c4cbd0', 1) for k in range(0)) + Pa('M40,40 L80,60 L60,130 Z', 'none', 'stroke="#a7adb1" stroke-width="1.5"') + fish_shape(160, 186, 20, '#9fb4c4', '#e6ecef'), False)
S_('board', sea(140) + boat_hull(130, 176, 140, 40, '#ffffff', '#2f4a7a') + R(70, 100, 120, 36, '#ffffff') + Pa('M10,120 L80,140 L80,146 L10,126 Z', '#a7adb1') + fig(56, 132, 'oldwoman', s=.4) + arrow(70, 90, 100, 100, '#5ba644', 3), False)
S_('ferry-terminal', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, SEA) + R(10, 60, 120, 80, '#e6dcc8') + Pa('M4,64 L70,30 L136,64 Z', '#3c7fc1') + ''.join(R(20 + k * 26, 80, 18, 24, '#8ec3e6') for k in range(4)) + R(54, 110, 30, 30, '#5a3a24') + boat_hull(160, 170, 70, 20, '#ffffff', '#3c7fc1') + R(140, 140, 40, 14, '#ffffff'), False)
S_('marina', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, SEA) + R(0, 150, 200, 8, '#a8703e') + ''.join(R(10 + k * 50, 110, 6, 40, '#a8703e') for k in range(4)) + ''.join(boat_hull(36 + k * 50, 146, 36, 12, '#ffffff', '#3c7fc1') + L(36 + k * 50, 134, 36 + k * 50, 70, '#5d6469', 2) for k in range(4)), False)
S_('warehouse', R(0, 0, 200, 200, SKY) + R(0, 176, 200, 24, '#a7a09a') + R(20, 80, 160, 96, '#c4cbd0') + Pa('M10,84 Q100,30 190,84 Z', '#8a9196') + R(60, 110, 80, 66, '#5d6469') + ''.join(L(60, 116 + k * 10, 140, 116 + k * 10, '#8a9196', 2) for k in range(6)) + box_(150, 150, 30, 26), False)
S_('coast-guard', sea(130) + Pa('M20,130 L170,130 Q186,136 182,156 L40,156 Z', '#ffffff') + Pa('M40,136 L60,156 L76,156 L56,136 Z', '#e2463b') + Pa('M60,130 L80,100 L140,100 L150,130 Z', '#ffffff') + R(90, 104, 40, 12, '#2f4a7a', 2) + R(104, 84, 6, 18, '#5d6469') + R(102, 80, 10, 6, '#3c7fc1', 2), False)
S_('buoy', sea(110) + Pa('M80,140 L120,140 L114,80 L86,80 Z', '#e2463b') + R(86, 100, 28, 12, '#ffffff') + R(96, 56, 8, 26, '#5d6469') + Ci(100, 52, 8, '#f3d058') + E(100, 142, 30, 8, '#c0302a') + St('M60,150 q10,-6 20,0 M120,150 q10,-6 20,0', '#9fd0ec', 2), False)
S_('quay', sea(130) + R(0, 80, 200, 50, '#a7a09a') + ''.join(R(k * 40, 80, 38, 50, 'none', 0, 'stroke="#8a837c" stroke-width="2"') for k in range(5)) + R(30, 66, 12, 16, '#2f3437', 3) + R(150, 66, 12, 16, '#2f3437', 3) + St('M36,74 Q60,110 90,140', '#c8a070', 3) + boat_hull(120, 170, 120, 30, '#c8903a', '#8a5a35') + fig(100, 82, 'man', s=.35), False)
S_('tide', R(0, 0, 200, 200, SKY) + Pa('M0,160 L200,120 L200,200 L0,200 Z', '#f0d890') + R(0, 100, 200, 30, SEA, 0, 'opacity=".5"') + R(0, 130, 200, 70, SEA, 0, 'opacity=".9"') + St('M0,100 L200,100', '#3c7fc1', 2, 'stroke-dasharray="6 4"') + St('M0,130 L200,130', '#3c7fc1', 2, 'stroke-dasharray="6 4"') + arrow(170, 140, 170, 104, '#e2463b', 3) + Pa('M150,30 A12,12 0 1,0 164,48 A10,10 0 1,1 150,30 Z', '#f3c234'), False)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
