from kit3 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)

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

# ================= 学校 =================
S_('school', sky_ground(176, '#8cc06a') + R(20, 70, 160, 106, '#f6e2c8') + R(80, 40, 40, 40, '#f6e2c8') + Pa('M74,42 L100,20 L126,42 Z', '#c0503a') + clock(100, 58, 10) + L(100, 20, 100, 4, '#5d6469', 2) + R(100, 4, 16, 10, '#e2463b') + ''.join(R(30 + k * 26, 90, 16, 18, '#8ec3e6') for k in range(6)) + ''.join(R(30 + k * 26, 120, 16, 18, '#8ec3e6') for k in range(6) if k not in (2, 3)) + R(84, 130, 32, 46, '#5a3a24'), False)
S_('teacher', board_(100, 20, 90, 60, '#2f4a3a', T(145, 58, 'A B C', 16, '#ffffff', 800)) + person_bust(60, 96, 30, '#9a7ab8', '#3a2a20', 'bun') + Ci(49, 96, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(71, 96, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + arm([(110, 200), (120, 140), (130, 70)], '#9a7ab8', SK, 12) + L(130, 70, 150, 50, '#8a5a35', 3))
S_('student', fig(100, 190, 'boy', s=1.4) + R(70, 90, 60, 50, '#3c7fc1', 10) + St('M80,90 Q80,74 100,74 Q120,74 120,90', '#2f5a8a', 4) + book_(150, 150, .5, '#e2463b'))
S_('class', R(0, 0, 200, 200, '#f2ead8') + board_(30, 16, 140, 50) + ''.join(R(18 + (k % 3) * 60, 120 + (k // 3) * 40, 44, 10, WOOD, 2) + Ci(40 + (k % 3) * 60, 106 + (k // 3) * 40, 10, SK) + Pa(f'M{30+(k%3)*60},{104+(k//3)*40} Q{40+(k%3)*60},{92+(k//3)*40} {50+(k%3)*60},{104+(k//3)*40} Z', '#3a2a20') + R(30 + (k % 3) * 60, 114 + (k // 3) * 40, 20, 8, ['#e2463b', '#3c7fc1', '#5ba644', '#f3c234', '#ef8fa4', '#7a4fa0'][k], 3) for k in range(6)), False)
S_('book', book_(80, 100, 1.4, '#3c7fc1', -8) + book_(130, 112, 1.2, '#e2463b', 10))
S_('pen', pen_(100, 100, 1.3, -30))
S_('pencil', pencil_(100, 100, 1.3, -30) + pencil_(110, 140, .9, -10))
S_('desk', R(30, 90, 140, 12, WOOD, 3) + R(36, 102, 128, 30, shade(WOOD, -.1), 2) + R(40, 132, 8, 50, '#5d6469') + R(152, 132, 8, 50, '#5d6469') + book_(70, 80, .3, '#3c7fc1', 80) + pencil_(120, 86, .4, 0))
S_('classroom', R(0, 0, 200, 200, '#f2ead8') + board_(20, 14, 160, 50, '#2f4a3a', T(100, 46, '1+1=2', 18, '#ffffff', 800)) + ''.join(R(20 + (k % 3) * 60, 110 + (k // 3) * 44, 46, 10, WOOD, 2) + R(26 + (k % 3) * 60, 120 + (k // 3) * 44, 4, 24, '#5d6469') + R(60 + (k % 3) * 60, 120 + (k // 3) * 44, 4, 24, '#5d6469') for k in range(6)) + window_(160, 80, 0, 0) + clock(170, 90, 12), False)
S_('homework', R(30, 60, 140, 110, '#ffffff', 3) + ''.join(L(40, 80 + k * 14, 160, 80 + k * 14, '#cfe8f6', 2) for k in range(6)) + T(70, 96, '3+4=7', 14, '#3c7fc1', 800) + T(70, 124, '5×2=10', 14, '#3c7fc1', 800) + pencil_(140, 150, .6, -30) + house(160, 50, 30, 18) + Ci(40, 40, 0, '#000'))
S_('lesson', R(0, 0, 200, 200, '#f2ead8') + board_(70, 20, 120, 80, '#2f4a3a', T(130, 50, 'Lesson 3', 14, '#ffffff', 800) + L(90, 66, 170, 66, '#ffffff', 2) + L(90, 80, 150, 80, '#ffffff', 2)) + fig(40, 190, 'woman', s=.9, arms='wave') + clock(30, 30, 16, (9, 0)), False)
S_('notebook', R(50, 30, 110, 140, '#5ba644', 6) + R(60, 30, 100, 140, '#ffffff', 4) + ''.join(L(66, 56 + k * 14, 150, 56 + k * 14, '#cfe8f6', 2) for k in range(8)) + ''.join(Ci(54, 40 + k * 18, 5, '#f2ead8', 'stroke="#a7adb1" stroke-width="2"') for k in range(7)) + L(80, 34, 80, 166, '#ef8fa4', 1.5))
S_('ruler', G(R(-90, -16, 180, 32, '#f3c234', 3) + ''.join(L(-84 + k * 8, -16, -84 + k * 8, -16 + (14 if k % 5 == 0 else 8), '#2f3437', 1.5) for k in range(22)) + ''.join(T(-84 + k * 40, 12, str(k * 5), 9, '#2f3437', 700) for k in range(5)), 'translate(100,100) rotate(-15)'))
S_('eraser', G(R(-40, -20, 80, 40, '#ef8fa4', 6) + R(-40, -20, 40, 40, '#5aa1d4', 6) + R(-6, -20, 6, 40, '#5aa1d4'), 'translate(90,110) rotate(-10)') + ''.join(Ci(150 + k * 8, 130 + (k % 2) * 6, 3, '#c4cbd0') for k in range(4)) + St('M130,70 Q150,60 170,70', '#2f3437', 2) + St('M128,80 Q150,70 172,80', '#c4cbd0', 2, 'opacity=".5"'))
S_('exam', R(30, 20, 140, 160, '#ffffff', 3) + T(100, 50, '100', 28, '#e2463b', 900) + Ci(100, 42, 26, 'none', 'stroke="#e2463b" stroke-width="3"') + ''.join(R(44, 80 + k * 22, 10, 10, 'none', 1, 'stroke="#2f3437" stroke-width="2"') + St(f'M45,{84+k*22} l4,4 l6,-8', '#e2463b', 2.5) + L(62, 86 + k * 22, 150, 86 + k * 22, '#a7adb1', 3) for k in range(4)) + clock(166, 30, 16, (10, 0)))
S_('blackboard', board_(20, 30, 160, 110, '#2f4a3a', T(100, 80, 'A B C', 22, '#ffffff', 800) + T(100, 116, '1 2 3', 22, '#f3e070', 800)) + R(60, 140, 16, 6, '#ffffff', 2) + R(140, 140, 22, 8, '#c8a070', 2))

# ================= 数学 =================
def math_card(sym, col='#3c7fc1', extra=''):
    return R(30, 30, 140, 140, col, 16) + T(100, 128, sym, 90, '#ffffff', 900) + extra
S_('plus', math_card('+', '#5ba644'))
S_('minus', math_card('−', '#e2463b'))
S_('equals', math_card('=', '#3c7fc1'))
S_('half', Ci(100, 100, 70, '#e6ecef') + Pa('M100,30 A70,70 0 0,1 100,170 Z', '#f08a24') + L(100, 26, 100, 174, '#2f3437', 3) + T(150, 190, '½', 0, '#000') + T(60, 110, '½', 30, '#5d6469', 900))
S_('add', ''.join(apple(40 + k * 24, 90, .6) for k in range(2)) + T(98, 104, '+', 34, '#2f3437', 900) + ''.join(apple(130 + k * 24, 90, .6) for k in range(1)) + T(100, 160, '2 + 1 = 3', 28, '#3c7fc1', 900))
S_('answer', R(20, 60, 160, 80, '#ffffff', 8) + T(80, 112, '6×7=', 30, '#2f3437', 900) + R(130, 76, 44, 48, '#f3c234', 6) + T(152, 112, '42', 28, '#e2463b', 900) + Ci(150, 40, 16, '#5ba644') + St('M142,40 l6,6 l10,-12', '#ffffff', 4))
S_('circle', Ci(100, 100, 70, 'none', 'stroke="#3c7fc1" stroke-width="10"') + Ci(100, 100, 4, '#2f3437') + L(100, 100, 170, 100, '#e2463b', 2, ) + Ci(100, 100, 60, '#3c7fc1', 'opacity=".1"'))
S_('triangle', Pa('M100,30 L170,160 L30,160 Z', '#f3c234') + Pa('M100,30 L170,160 L30,160 Z', 'none', 'stroke="#e0a020" stroke-width="6" stroke-linejoin="round"'))
S_('square-math', R(40, 40, 120, 120, '#5ba644') + R(40, 40, 120, 120, 'none', 0, 'stroke="#3c8a3a" stroke-width="6"') + R(40, 40, 14, 14, 'none', 0, 'stroke="#ffffff" stroke-width="2"'))
S_('calculator', R(50, 20, 100, 160, '#2f3437', 12) + R(60, 30, 80, 34, '#cfe8d0', 4) + T(134, 56, '123', 18, '#2f3437', 900, 'end') + ''.join(R(60 + (k % 4) * 21, 74 + (k // 4) * 24, 17, 18, ['#a7adb1', '#a7adb1', '#a7adb1', '#f08a24'][k % 4], 4) for k in range(16)))
S_('percent', Ci(100, 100, 70, '#e6ecef') + Pa('M100,100 L100,30 A70,70 0 1,1 33,122 Z', '#3c7fc1') + T(100, 110, '75%', 28, '#ffffff', 900))
S_('multiply', math_card('×', '#7a4fa0'))
S_('divide', math_card('÷', '#f08a24'))
S_('total', R(40, 20, 120, 160, '#ffffff', 4) + ''.join(T(130, 50 + k * 26, ['12', '25', '8', '30'][k], 18, '#2f3437', 800, 'end') for k in range(4)) + L(60, 140, 140, 140, '#2f3437', 3) + T(130, 168, '75', 24, '#e2463b', 900, 'end') + T(64, 164, 'Σ', 26, '#3c7fc1', 900))
S_('average', ''.join(R(30 + k * 30, 170 - h, 22, h, ['#5aa1d4', '#5ba644', '#f3c234', '#ef8fa4', '#7a4fa0'][k], 2) for k, h in enumerate([60, 100, 80, 120, 70])) + L(20, 84, 190, 84, '#e2463b', 3) + St('M20,84 L190,84', '#e2463b', 3, 'stroke-dasharray="8 6"') + R(20, 170, 170, 4, '#2f3437'))
S_('fraction', T(100, 90, '3', 50, '#3c7fc1', 900) + L(64, 104, 136, 104, '#2f3437', 5) + T(100, 160, '4', 50, '#3c7fc1', 900) + ''.join(Pa(f'M160,60 L{160+30*math.cos(a)},{60+30*math.sin(a)} A30,30 0 0,1 {160+30*math.cos(a+1.57)},{60+30*math.sin(a+1.57)} Z', '#f08a24' if k < 3 else '#e6ecef', 'stroke="#ffffff" stroke-width="2"') for k, a in enumerate([j * 1.5708 - 1.5708 for j in range(4)])))

# ================= 物理 =================
S_('hot', thermometer_red if False else G(R(-12, -70, 24, 120, '#ffffff', 12) + R(-12, -70, 24, 120, 'none', 12, 'stroke="#c4cbd0" stroke-width="3"') + R(-5, -60, 10, 100, '#e2463b', 5) + Ci(0, 54, 18, '#e2463b'), 'translate(70,100)') + flame(140, 140, .8) + Ci(150, 40, 20, '#f3c234') + St('M120,50 l-10,0 M150,10 l0,-6', '#f3c234', 3))
S_('warm', R(0, 0, 200, 200, '#fbe8cc') + G(R(-12, -70, 24, 120, '#ffffff', 12) + R(-5, -10, 10, 50, '#f08a24', 5) + Ci(0, 54, 18, '#f08a24'), 'translate(60,100)') + cup(130, 110, 60, 50, '#ffffff', '#c98a3a') + steam(118, 96, 3, 10, '#c4cbd0', .6) + Ci(170, 40, 14, '#f3c234'), False)
S_('fast', R(0, 160, 200, 40, ROAD) + G(car_side(0, 0, '#e2463b', 1.0), 'translate(120,160) skewX(-10)') + ''.join(L(10, 110 + k * 14, 50 - k * 6, 110 + k * 14, '#a7adb1', 4) for k in range(3)) + T(40, 50, '>>>', 30, '#e2463b', 900), False)
S_('slow', R(0, 160, 200, 40, '#8cc06a') + G(E(0, 0, 40, 30, '#c8903a') + ''.join(St(f'M0,0 m{-14+k*2},0 a{14-k*3},{14-k*3} 0 1,1 {28-k*6},0', '#a8703e', 3) for k in range(3)) + E(50, 20, 24, 10, '#c8b880') + Ci(64, 6, 10, '#c8b880') + L(62, -4, 66, -16, '#c8b880', 3) + L(68, -2, 74, -14, '#c8b880', 3), 'translate(90,140)') + T(50, 50, '…', 40, '#7a8a94', 900), False)
S_('heat', flame(70, 150, 1.2) + ''.join(St(f'M{120+k*20},170 q-10,-20 0,-40 q10,-20 0,-40 q-10,-20 0,-40', '#f08a24', 4) for k in range(3)))
S_('sound', Ci(50, 100, 22, '#2f3437') + Pa('M60,80 L100,50 L100,150 L60,120 Z', '#2f3437') + ''.join(St(f'M{120+k*20},{70-k*12} Q{140+k*24},100 {120+k*20},{130+k*12}', '#3c7fc1', 5) for k in range(3)))
S_('speed', dash_icon(100, 110, 80))
S_('magnet', magnet_(100, 100, 1.4) + ''.join(R(50 + k * 22, 160, 8, 18, '#a7adb1', 1) for k in range(5)) + St('M70,140 L60,154 M130,140 L140,154', '#5d6469', 2, 'stroke-dasharray="3 3"'))
S_('gravity', R(0, 170, 200, 30, '#8cc06a') + tree(60, 120, 1.2) + apple(140, 130, .7) + arrow(140, 60, 140, 110, '#e2463b', 4) + fig(140, 196, 'man', s=.0), False)
S_('force', R(0, 186, 200, 14, WALK) + P_force if False else R(0, 186, 200, 14, WALK) + pose((60, 54), (66, 74), (76, 116), arms=[[(74, 78), (96, 92), (112, 96)]], legs=[[(74, 116), (60, 150), (44, 182)], [(80, 116), (90, 150), (100, 182)]], back_arm=[[(68, 80), (92, 98), (112, 104)]], shirt='#3c7fc1', pants='#3b4a5a', hr=14, tw=26) + box_(112, 80, 70, 100) + arrow(100, 40, 170, 40, '#e2463b', 8), False)
S_('wave', St('M10,100 Q35,40 60,100 T110,100 T160,100 T210,100', '#3c7fc1', 8) + St('M10,140 Q35,110 60,140 T110,140 T160,140 T210,140', '#9fd0ec', 4))
S_('echo', R(0, 0, 200, 200, SKY) + Pa('M120,200 L150,40 L200,20 L200,200 Z', '#8a7a6a') + fig(40, 190, 'man', s=.6, arms='front') + T(70, 80, 'Hi!', 18, '#3c7fc1', 900) + T(110, 70, 'Hi!', 14, '#3c7fc1', 900, extra='opacity=".6"') + T(70, 50, 'Hi!', 12, '#3c7fc1', 900, extra='opacity=".4"') + St('M80,90 Q110,90 130,80', '#3c7fc1', 2, 'stroke-dasharray="4 4"') + St('M130,70 Q100,50 80,60', '#3c7fc1', 2, 'stroke-dasharray="4 4"'), False)
S_('motion', Ci(150, 100, 30, '#e2463b') + hi(140, 90, 8, 6, .5) + ''.join(Ci(50 + k * 22, 100, 30 - k * 0, '#e2463b', f'opacity="{.15+k*.15}"') for k in range(4)) + R(20, 132, 170, 6, '#5d6469'))
S_('friction', R(10, 140, 180, 30, '#c8a070') + ''.join(Pa(f'M{10+k*12},140 l6,-6 l6,6', '#a8803a') for k in range(15)) + box_(60, 80, 80, 64, '#5aa1d4') + arrow(150, 100, 190, 100, '#3c7fc1', 4) + arrow(60, 132, 20, 132, '#e2463b', 4) + St('M110,148 l4,-8 M126,148 l4,-8', '#f08a24', 2))
S_('pressure', Ci(100, 110, 60, '#2f3437') + Ci(100, 110, 52, '#ffffff') + ''.join(L(100 + 40 * math.cos(a), 110 + 40 * math.sin(a), 100 + 48 * math.cos(a), 110 + 48 * math.sin(a), '#2f3437', 2) for a in [math.pi * .75 + k * math.pi * 1.5 / 10 for k in range(11)]) + L(100, 110, 136, 90, '#e2463b', 4) + Ci(100, 110, 6, '#2f3437') + R(92, 30, 16, 24, '#a7adb1') + R(80, 22, 40, 10, '#5d6469', 3))
S_('electric-current', R(30, 60, 140, 90, 'none', 4, 'stroke="#2f3437" stroke-width="5"') + R(40, 50, 30, 20, '#f3c234', 3) + T(55, 66, '+', 14, '#2f3437', 900) + bulb(130, 70, 14) + ''.join(Pa(f'M{60+k*30},150 l10,-6 l0,12 Z', '#e2463b') for k in range(3)) + bolt_icon(100, 110, .4))

# ================= 化学 =================
S_('air', R(0, 0, 200, 200, SKY) + ''.join(St(f'M{20+k*10},{40+k*40} q30,-14 60,0 t60,0', '#ffffff', 4) for k in range(4)) + leaf(150, 150, 20, 8, -30, '#7cc05a') + leaf(40, 60, 16, 6, 30, '#7cc05a') + ''.join(Ci(30 + k * 40, 180, 3, '#ffffff') for k in range(5)), False)
S_('liquid', glass(60, 50, 80, 120, '#5aa1d4', .6) + drop(150, 60, 14, '#5aa1d4') + St('M150,90 q4,10 0,20', '#5aa1d4', 0))
S_('solid', R(30, 110, 70, 60, '#c8903a', 3) + ''.join(L(34, 120 + k * 14, 96, 120 + k * 14, '#a8703e', 2) for k in range(4)) + Pa('M110,170 L120,120 L150,100 L180,120 L186,170 Z', '#8a9196') + Pa('M120,120 L150,100 L160,130 Z', '#a7adb1') + R(60, 50, 50, 50, '#dff1fb', 6) + R(60, 50, 50, 50, 'none', 6, 'stroke="#9fd0ec" stroke-width="3"') + hi(72, 60, 10, 4, .8))
S_('melt', Ci(165, 35, 20, '#f3c234') + ''.join(L(165 + 26 * math.cos(a), 35 + 26 * math.sin(a), 165 + 34 * math.cos(a), 35 + 34 * math.sin(a), '#f3c234', 3) for a in [k * .785 for k in range(8)]) + E(100, 165, 74, 16, '#9fd0ec') + Pa('M60,70 Q60,60 70,60 L130,60 Q140,60 140,70 L140,130 Q140,150 120,150 Q110,165 100,150 Q90,160 80,150 Q60,150 60,130 Z', '#dff1fb') + Pa('M60,70 Q60,60 70,60 L130,60 Q140,60 140,70 L140,130 Q140,150 120,150 Q110,165 100,150 Q90,160 80,150 Q60,150 60,130 Z', 'none', 'stroke="#9fd0ec" stroke-width="3"') + hi(76, 74, 14, 5, .8) + drop(50, 120, 7, '#9fd0ec') + drop(150, 110, 6, '#9fd0ec'))
S_('freeze', E(70, 150, 50, 14, '#9fd0ec') + R(100, 60, 70, 70, '#dff1fb', 8) + R(100, 60, 70, 70, 'none', 8, 'stroke="#9fd0ec" stroke-width="3"') + T(135, 108, '❄', 30, '#5aa1d4') + arrow(70, 130, 110, 100, '#3c7fc1', 4) + T(40, 50, '0°C', 22, '#3c7fc1', 900))
S_('experiment', flask(70, 170, 70, '#7cc05a') + flask(130, 170, 50, '#ef8fa4', 'round') + ''.join(Ci(68 + k * 6, 120 - k * 12, 4 - k * .5, '#7cc05a', 'opacity=".7"') for k in range(4)) + R(20, 170, 160, 8, '#a7adb1', 3))
S_('lab', R(0, 0, 200, 200, '#e6f0f4') + R(0, 130, 200, 70, '#c4cbd0') + R(0, 124, 200, 10, '#5d6469') + flask(40, 124, 40, '#7cc05a') + flask(90, 124, 34, '#5aa1d4', 'round') + ''.join(tube(130 + k * 16, 100, .5, 0, ['#e2463b', '#f3c234', '#5ba644'][k]) for k in range(3)) + micro(170, 70, .4) + R(10, 20, 70, 50, '#ffffff', 3) + atom_(45, 45, 18), False)
S_('test-tube', ''.join(tube(60 + k * 40, 100, 1.0, -10 + k * 10, ['#e2463b', '#5aa1d4', '#7cc05a'][k]) for k in range(3)) + R(40, 150, 120, 10, WOOD, 2))
S_('chemical', bottle_shape(60, 40, 80, 140, '#8a5a35', .35) + R(80, 26, 40, 16, '#2f3437', 3) + Pa('M100,90 L130,140 L70,140 Z', '#f3c234') + Pa('M100,90 L130,140 L70,140 Z', 'none', 'stroke="#2f3437" stroke-width="3"') + T(100, 134, '!', 26, '#2f3437', 900))
S_('oxygen', ''.join(G(Ci(-14, 0, 22, '#e2463b') + Ci(14, 0, 22, '#e2463b') + T(-14, 6, 'O', 16, '#ffffff', 900) + T(14, 6, 'O', 16, '#ffffff', 900), f'translate({x},{y})') for x, y in [(60, 70), (140, 110), (80, 150)]) + T(150, 50, 'O₂', 28, '#3c7fc1', 900))
S_('acid', flask(90, 180, 80, '#c8e040') + ''.join(Ci(80 + k * 10, 130 - k * 14, 5, '#c8e040', 'opacity=".7"') for k in range(3)) + G(R(-14, 0, 28, 20, '#e2463b', 2) + T(0, 15, 'pH 2', 9, '#ffffff', 900), 'translate(150,60)') + Pa('M150,110 L170,150 L130,150 Z', '#f3c234') + T(150, 146, '!', 18, '#2f3437', 900))
S_('safety-goggles', G(R(-70, -26, 140, 52, '#9fd0ec', 24, 'opacity=".8"') + R(-70, -26, 140, 52, 'none', 24, 'stroke="#2f3437" stroke-width="7"') + L(0, -26, 0, 26, '#2f3437', 5) + St('M-70,0 L-96,-6 M70,0 L96,-6', '#5aa1d4', 8), 'translate(100,100)'))
S_('reaction', flask(60, 170, 60, '#5aa1d4') + flask(140, 170, 60, '#f3c234') + St('M76,80 Q100,50 124,80', '#e2463b', 4) + Pa('M118,72 L128,84 L114,86 Z', '#e2463b') + star(100, 40, 14, '#f08a24') + ''.join(Ci(140 + k * 6, 110 - k * 10, 4, '#f3c234', 'opacity=".7"') for k in range(3)))
S_('mixture', bowl(100, 100, 140, fill='#e6dcc4', pattern=None) + ''.join(Ci(50 + (k * 37) % 100, 96 + (k % 3) * 4, 6, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644'][k % 4]) for k in range(16)) + G(R(-4, -60, 8, 60, WOOD, 4), 'translate(140,90) rotate(30)'))
S_('formula', board_(20, 30, 160, 110, '#2f4a3a', T(100, 86, 'H₂O', 34, '#ffffff', 900) + T(100, 122, 'E = mc²', 20, '#f3e070', 800)))
S_('molecule', ''.join(L(100, 100, 100 + 50 * math.cos(a), 100 + 50 * math.sin(a), '#a7adb1', 6) for a in [k * 2.094 - 1.57 for k in range(3)]) + ''.join(Ci(100 + 50 * math.cos(a), 100 + 50 * math.sin(a), 18, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') for a in [k * 2.094 - 1.57 for k in range(3)]) + Ci(100, 100, 28, '#2f3437') + hi(92, 92, 6, 4, .4))

# ================= 生物 =================
S_('animal', badge(60, 70, 'cow', 30) + badge(140, 70, 'pig', 30) + badge(60, 150, 'sheep', 30) + badge(140, 150, 'duck', 30))
S_('human', fig(70, 190, 'man') + fig(130, 190, 'woman'))
S_('alive', potted(100, 180, 60, 40) + St('M100,140 L100,70', '#4a9a3a', 5) + ''.join(leaf(100, 130 - k * 18, 30, 10, -30 if k % 2 else -150, '#5aaa3a') for k in range(4)) + flower(100, 60, 1.6, '#f3c234') + heart(160, 40, 10))
S_('dead', potted(100, 180, 60, 40) + St('M100,140 Q100,100 120,80 Q130,90 140,120', '#8a6a3a', 5) + ''.join(leaf(100 + k * 8, 130 - k * 8, 22, 8, 40 + k * 30, '#a8905a') for k in range(3)) + ''.join(leaf(50 + k * 30, 176, 16, 6, 0, '#a8905a') for k in range(3)))
S_('cell', E(100, 100, 80, 64, '#bfe6c0') + E(100, 100, 80, 64, 'none', 'stroke="#5aaa3a" stroke-width="4"') + Ci(90, 96, 22, '#7a6ab8') + Ci(90, 96, 8, '#5a4a98') + ''.join(E(130 + k * 8, 80 + k * 18, 10, 5, '#f08a24') for k in range(3)) + ''.join(Ci(60 + k * 14, 140 - k * 4, 3, '#3c7fc1') for k in range(4)))
S_('microscope', micro(100, 100, 1.3))
S_('virus', virus_(100, 100, 46))
S_('bacteria', ''.join(G(R(-26, -10, 52, 20, '#7cc05a', 10) + St('M26,0 q10,-6 18,4', '#7cc05a', 2) + Ci(-10, 0, 3, '#3c8a3a') + Ci(8, 0, 3, '#3c8a3a'), f'translate({x},{y}) rotate({r_})') for x, y, r_ in [(60, 70, 20), (130, 80, -30), (90, 140, 60), (150, 150, 10), (50, 150, -20)]) + Ci(100, 100, 90, 'none', 'stroke="#a7adb1" stroke-width="4"'))
S_('species', ''.join(G(E(0, 0, 18, 10, c) + Ci(14, -6, 7, c) + Pa('M20,-6 l6,2 l-6,2 Z', '#f3c234') + Ci(16, -8, 1.5, '#2f3437'), f'translate({x},{y})') for x, y, c in [(50, 60, '#e2463b'), (100, 60, '#3c7fc1'), (150, 60, '#f3c234'), (50, 120, '#5ba644'), (100, 120, '#7a4fa0'), (150, 120, '#f08a24')]) + ''.join(leaf(40 + k * 50, 170, 20, 8, -60, '#5aaa3a') for k in range(3)))
S_('habitat', R(0, 0, 200, 200, SKY) + R(0, 130, 200, 70, '#8cc06a') + E(130, 160, 40, 14, '#5aa1d4') + tree(50, 130, 1.0) + G(E(0, 0, 18, 10, '#8a5a35') + Ci(14, -6, 7, '#8a5a35') + Pa('M20,-6 l6,2 l-6,2 Z', '#f3c234'), 'translate(60,70)') + Ci(170, 30, 14, '#f3c234') + G(E(0, 0, 12, 8, '#c8903a') + Ci(10, -4, 5, '#c8903a'), 'translate(110,150)'), False)
S_('food-chain', leaf(30, 150, 30, 12, -40, '#5aaa3a') + arrow(56, 140, 74, 120, '#2f3437', 3) + G(E(0, 0, 14, 8, '#7cc05a') + Ci(12, -2, 5, '#7cc05a'), 'translate(90,110)') + arrow(110, 100, 126, 84, '#2f3437', 3) + G(E(0, 0, 16, 10, '#8a5a35') + Ci(14, -6, 7, '#8a5a35') + Pa('M20,-6 l6,2 l-6,2 Z', '#f3c234'), 'translate(146,70)') + arrow(160, 60, 170, 40, '#2f3437', 3) + G(Pa('M-20,0 L0,-10 L20,0 L0,6 Z', '#5d6469') + Ci(14, -8, 5, '#5d6469'), 'translate(176,26)'))
S_('life-cycle', ''.join(St(f'M{100+60*math.cos(a)},{100+60*math.sin(a)} A60,60 0 0,1 {100+60*math.cos(a+1.3)},{100+60*math.sin(a+1.3)}', '#5ba644', 4) + Pa(f'M{100+60*math.cos(a+1.4)},{100+60*math.sin(a+1.4)} l-6,-8 l10,0 Z', '#5ba644') for a in [k * 1.5708 - 1.5708 for k in range(4)]) + E(100, 40, 8, 6, '#f6efe0') + G(E(0, 0, 16, 6, '#7cc05a'), 'translate(160,100)') + E(100, 160, 10, 16, '#c8a070') + G(Pa('M0,0 Q-20,-20 -16,0 Q-20,20 0,0 Q20,-20 16,0 Q20,20 0,0 Z', '#f08a24'), 'translate(40,100) scale(1.2)'))
S_('gene', ''.join(Ci(80 + 30 * math.sin(k / 3), 20 + k * 9, 6, '#e2463b') + Ci(120 - 30 * math.sin(k / 3), 20 + k * 9, 6, '#3c7fc1') + L(80 + 30 * math.sin(k / 3), 20 + k * 9, 120 - 30 * math.sin(k / 3), 20 + k * 9, '#a7adb1', 2) for k in range(18)))
S_('dna', ''.join(L(70 + 40 * math.sin(k / 2.5), 20 + k * 9, 130 - 40 * math.sin(k / 2.5), 20 + k * 9, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644'][k % 4], 4) for k in range(18)) + St('M' + ' L'.join(f'{70+40*math.sin(k/2.5):.1f},{20+k*9}' for k in range(18)), '#2f3437', 4) + St('M' + ' L'.join(f'{130-40*math.sin(k/2.5):.1f},{20+k*9}' for k in range(18)), '#2f3437', 4))
S_('evolution', R(0, 186, 200, 14, WALK) + pose((30, 120), (36, 132), (50, 156), arms=[[(40, 136), (44, 172)]], legs=[[(48, 158), (44, 184)]], shirt='#8a5a35', pants='#8a5a35', hair='#5a3a24', hr=10, tw=20, lw=9, aw=7) + pose((90, 90), (92, 108), (98, 140), arms=[[(98, 112), (104, 150)]], legs=[[(96, 140), (92, 184)], [(102, 140), (106, 184)]], shirt='#a8703e', pants='#a8703e', hair='#5a3a24', hr=11, tw=22, lw=10, aw=8) + fig(155, 190, 'man', s=.8), False)
S_('organism', Ci(100, 100, 80, '#dff1fb') + Ci(100, 100, 80, 'none', 'stroke="#a7adb1" stroke-width="5"') + E(80, 90, 30, 20, '#bfe6c0') + Ci(76, 88, 8, '#7a6ab8') + virus_(140, 70, 10) + G(R(-14, -6, 28, 12, '#7cc05a', 6), 'translate(120,140) rotate(30)') + leaf(60, 140, 20, 8, -20, '#5aaa3a'))

# ================= 元素周期表 =================
def ingots(c, sym, num):
    bar = lambda x, y: Pa(f'M{x-30},{y+14} L{x-20},{y-10} L{x+20},{y-10} L{x+30},{y+14} Z', c) + Pa(f'M{x-20},{y-10} L{x+20},{y-10} L{x+16},{y-4} L{x-16},{y-4} Z', shade(c, .25)) + hi(x - 10, y, 10, 3, .5)
    return bar(70, 160) + bar(130, 160) + bar(100, 134) + R(130, 24, 50, 50, '#ffffff', 6, f'stroke="{shade(c,-.2)}" stroke-width="4"') + T(155, 60, sym, 24, '#2f3437', 900) + T(136, 38, str(num), 10, '#5d6469', 700, 'start')

S_('gold', ingots('#f3c234', 'Au', 79))
S_('silver', ingots('#c4cbd0', 'Ag', 47))
S_('iron-periodic', Pa('M30,110 L150,110 Q140,130 120,134 L110,150 L130,170 L50,170 L70,150 L60,134 Q40,130 30,110 Z', '#5d6469') + Pa('M150,110 L180,110 Q170,120 150,124 Z', '#5d6469') + R(30,104,120,8,'#8a9196',2) + R(130, 24, 50, 50, '#ffffff', 6, 'stroke="#6a3a2a" stroke-width="4"') + T(155, 60, 'Fe', 24, '#2f3437', 900) + T(136, 38, '26', 10, '#5d6469', 700, 'start'))
S_('copper', ''.join(E(80, 120 - k * 6, 50, 18, 'none', f'stroke="{["#c8703a","#e08a4a"][k%2]}" stroke-width="6"') for k in range(8)) + St('M130,90 Q160,80 170,140', '#c8703a', 6) + R(130, 24, 50, 50, '#ffffff', 6, 'stroke="#a8582a" stroke-width="4"') + T(155, 60, 'Cu', 24, '#2f3437', 900) + T(136, 38, '29', 10, '#5d6469', 700, 'start'))
S_('metal', ''.join(G(Pa('M-30,10 L-20,-10 L20,-10 L30,10 Z', c) + hi(-6, -4, 10, 3, .5), f'translate({x},{y}) scale(1.4)') for x, y, c in [(60, 70, '#f3c234'), (140, 70, '#c4cbd0'), (60, 140, '#c8703a'), (140, 140, '#8a9196')]))
S_('element', ''.join(R(20 + (k % 6) * 28, 40 + (k // 6) * 28, 24, 24, ['#ef8fa4', '#f3c234', '#9fd0ec', '#7cc05a', '#c4cbd0'][(k * 7) % 5], 2) for k in range(24) if not (k // 6 == 0 and 1 <= k % 6 <= 4)) + R(48, 96, 52, 52, '#ffffff', 4, 'stroke="#e2463b" stroke-width="3"') + T(74, 132, 'C', 26, '#2f3437', 900))
S_('symbol', T(70, 110, 'H', 60, '#3c7fc1', 900) + T(140, 110, 'O', 60, '#e2463b', 900) + T(70, 170, 'Fe', 40, '#8a5a4a', 900) + T(140, 170, 'Au', 40, '#d9a33a', 900))
S_('atom', atom_(100, 100, 70))
S_('hydrogen', element_tile('H', 1, '#9fd0ec', '氢'))
S_('carbon', element_tile('C', 6, '#5d6469', '碳') + G(Pa('M0,-12 L12,0 L0,12 L-12,0 Z', '#dff1fb'), 'translate(150,170)'))
S_('nitrogen', element_tile('N', 7, '#7a8ac8', '氮'))
S_('aluminum', R(50, 50, 70, 120, '#c4cbd0', 10) + R(50, 60, 70, 100, '#dfe4e7', 4) + R(60, 44, 50, 10, '#a7adb1', 4) + hi(62, 70, 6, 40, .7) + Pa('M130,150 L170,140 L180,170 L140,180 Z', '#dfe4e7') + R(130, 24, 50, 50, '#ffffff', 6, 'stroke="#a7adb1" stroke-width="4"') + T(155, 60, 'Al', 24, '#2f3437', 900) + T(136, 38, '13', 10, '#5d6469', 700, 'start'))
S_('tin', R(40, 70, 90, 110, '#b8bfc4', 6) + ''.join(L(40, 90 + k * 20, 130, 90 + k * 20, '#9aa1a6', 3) for k in range(4)) + E(85, 70, 45, 10, '#d4d9dc') + R(130, 24, 50, 50, '#ffffff', 6, 'stroke="#8a837c" stroke-width="4"') + T(155, 60, 'Sn', 24, '#2f3437', 900) + T(136, 38, '50', 10, '#5d6469', 700, 'start'))
S_('lead', element_tile('Pb', 82, '#5d6469', '铅'))
S_('zinc', element_tile('Zn', 30, '#9ab0b8', '锌'))
S_('helium', element_tile('He', 2, '#f6c8dc', '氦') + balloon(166, 40, 14, '#ef8fa4'))

# ================= 历史 =================
S_('past', R(0, 0, 200, 200, '#e8d8b8') + Pa('M30,60 L170,60 L170,170 L30,170 Z', '#d0b890') + Pa('M40,70 L160,70 L160,160 L40,160 Z', '#c8a878') + ''.join(R(60 + k * 30, 110 - k * 6, 20, 50 + k * 6, '#8a6a4a') for k in range(3)) + clock(160, 40, 20, (9, 0)) + St('M150,40 a10,10 0 1,0 10,-10', '#e2463b', 3) + arrow(140, 30, 130, 44, '#e2463b', 3), False)
S_('history', open_book(100, 120, 1.2, '#8a5a35') + crown(100, 40, .6) + G(Pa('M-20,0 L20,0 L14,-30 L-14,-30 Z', '#c4bcae') + R(-24, 0, 48, 6, '#a7a09a'), 'translate(40,60)'))
S_('king', crown(100, 40, .7) + big_face(100, 104, 48, hair='#5a3a24', style='none', m='smile') + Pa('M60,150 Q100,170 140,150 L160,200 L40,200 Z', '#c0283a') + Pa('M60,150 L60,200 M140,150 L140,200', 'none', 'stroke="#ffffff" stroke-width="10"') + Pa('M70,128 Q100,160 130,128 Q120,150 100,154 Q80,150 70,128 Z', '#8a6a4a'))
S_('queen', crown(100, 34, .6) + big_face(100, 100, 46, hair='#3a2a20', style='long', m='smile', blush='#ef9a8a') + Pa('M50,200 Q60,150 100,146 Q140,150 150,200 Z', '#7a4fa0') + ''.join(Ci(80 + k * 10, 152 + abs(k - 2) * 2, 3, '#ffffff') for k in range(5)))
S_('war', R(0, 0, 200, 200, '#d8c8b0') + ''.join(Ci(30 + k * 40, 30 + (k % 2) * 16, 20, '#8a837c', 'opacity=".6"') + flame(20 + k * 40, 196, .5) for k in range(5)) + G(R(-4, -80, 8, 120, '#c4cbd0', 2) + Pa('M-4,-80 L0,-92 L4,-80 Z', '#c4cbd0') + R(-20, 40, 40, 8, '#8a5a35', 3) + R(-4, 48, 8, 26, '#5a3a24', 2) + Ci(0, 78, 6, '#d9a33a'), 'translate(100,100) rotate(-40)') + G(R(-4, -80, 8, 120, '#c4cbd0', 2) + Pa('M-4,-80 L0,-92 L4,-80 Z', '#c4cbd0') + R(-20, 40, 40, 8, '#8a5a35', 3) + R(-4, 48, 8, 26, '#5a3a24', 2) + Ci(0, 78, 6, '#d9a33a'), 'translate(100,100) rotate(40)') + Pa('M70,90 L130,90 L130,130 Q130,160 100,172 Q70,160 70,130 Z', '#c0283a') + Pa('M80,98 L120,98 L120,128 Q120,150 100,160 Q80,150 80,128 Z', '#e6c870'), False)
S_('peace', R(0, 0, 200, 200, '#dff1fb') + G(E(0, 0, 40, 22, '#ffffff') + Pa('M-10,-10 Q-40,-50 -60,-30 Q-40,-20 -10,0 Z', '#ffffff') + Pa('M10,-10 Q30,-50 60,-40 Q40,-20 10,0 Z', '#f2efe8') + Ci(34, -10, 12, '#ffffff') + Pa('M44,-10 l12,4 l-12,2 Z', '#f08a24') + Ci(36, -12, 2, '#2f3437'), 'translate(100,90)') + St('M150,90 Q170,100 180,120', '#5a8a3a', 3) + leaf(170, 108, 14, 5, 40, '#5aaa3a'), False)
S_('emperor', R(0, 0, 200, 200, '#c0302a') + R(0, 150, 200, 50, '#a8241f') + big_face(100, 96, 44, hair='#2a1a10', style='none', m='flat') + R(60, 44, 80, 12, '#2f3437') + ''.join(L(64 + k * 9, 56, 64 + k * 9, 70, '#e6c870', 2) for k in range(9)) + Pa('M50,200 Q60,140 100,136 Q140,140 150,200 Z', '#f3c234') + St('M70,160 q10,-10 20,0 q10,-10 20,0 q10,-10 20,0', '#e2463b', 3), False)
S_('century', T(100, 110, '100', 60, '#3c7fc1', 900) + T(100, 160, '1900 → 2000', 20, '#5d6469', 800) + clock(170, 40, 18, (12, 0)))
S_('dynasty', ''.join(R(20 + k * 40, 40, 34, 120, ['#e2463b', '#f3c234', '#5ba644', '#3c7fc1'][k], 4) + T(37 + k * 40, 104, ['秦', '汉', '唐', '宋'][k], 22, '#ffffff', 900) for k in range(4)) + R(20, 170, 156, 6, '#5d6469', 2) + arrow(20, 186, 180, 186, '#5d6469', 3))
S_('empire', R(0, 0, 200, 200, '#e6dcc8') + Pa('M30,60 Q60,30 100,40 Q150,30 170,70 Q180,120 140,150 Q100,170 60,150 Q20,120 30,60 Z', '#e2463b', 'opacity=".7"') + crown(100, 100, .7) + ''.join(R(36 + k * 36, 170, 2, 16, '#8a5a35') + Pa(f'M{38+k*36},170 l14,4 l-14,4 Z', '#e2463b') for k in range(4)), False)
S_('invention', bulb(70, 80, 30) + G(Ci(0, 0, 26, '#a7adb1') + Ci(0, 0, 10, '#5d6469') + ''.join(R(-5, -34, 10, 12, '#a7adb1', 2, f'transform="rotate({k*45})"') for k in range(8)), 'translate(140,130)') + St('M100,70 l14,-8 M100,90 l16,0', '#f3c234', 3))
S_('ruins', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#c8b890') + ''.join(R(30 + k * 40, 160 - h, 20, h, '#d9d0c0') + ''.join(L(32 + k * 40, 160 - h + j * 10, 48 + k * 40, 160 - h + j * 10, '#c4b8a0', 1) for j in range(int(h / 10))) for k, h in enumerate([90, 60, 110, 40])) + R(20, 60, 100, 12, '#d9d0c0', 0, 'transform="rotate(-6 70 66)"') + ''.join(Pa(f'M{40+k*30},170 l10,-12 l10,12 Z', '#b8a888') for k in range(5)), False)
S_('revolution', R(0, 0, 200, 200, '#f6efe0') + R(60, 30, 6, 160, '#5d6469') + Pa('M66,30 Q110,20 150,40 Q120,56 150,80 Q110,70 66,80 Z', '#e2463b') + ''.join(fig(30 + k * 50, 196, ['man', 'woman', 'oldman'][k], arms='up', s=.4) for k in range(3)), False)
S_('great-wall', R(0, 0, 200, 200, SKY) + Pa('M0,170 L30,140 L60,122 L90,128 L120,106 L150,86 L180,80 L200,74 L200,200 L0,200 Z', '#7a9a5a') + St('M0,160 L30,130 L60,112 L90,118 L120,96 L150,76 L180,70 L200,64', '#b8a888', 16) + ''.join(R(x - 3, y - 16, 6, 8, '#a89878') for x, y in [(10, 150), (40, 122), (70, 108), (100, 110), (130, 88), (160, 72), (190, 66)]) + R(108, 70, 28, 34, '#b8a888') + ''.join(R(108 + k * 8, 64, 5, 8, '#a89878') for k in range(4)) + R(117, 88, 10, 16, '#5a4a3a', 4), False)
S_('silk-road', R(0, 0, 200, 200, '#f0d890') + Pa('M0,140 Q50,110 100,130 Q150,150 200,120 L200,200 L0,200 Z', '#e0c070') + Ci(160, 40, 16, '#f3c234') + ''.join(G(E(0, 0, 18, 10, '#c8903a') + Ci(-6, -12, 7, '#c8903a') + Ci(8, -12, 7, '#c8903a') + St('M18,-4 Q26,-20 30,-26', '#c8903a', 6) + Ci(32, -28, 5, '#c8903a') + L(-12, 8, -12, 24, '#a8703e', 3) + L(12, 8, 12, 24, '#a8703e', 3) + R(-14, -24, 20, 8, ['#e2463b', '#3c7fc1', '#7a4fa0'][k], 2), f'translate({50+k*50},{130-k*6})') for k in range(3)), False)
S_('era', R(10, 96, 180, 8, '#5d6469', 4) + ''.join(Ci(30 + k * 46, 100, 12, ['#c8a070', '#e2463b', '#3c7fc1', '#5ba644'][k]) for k in range(4)) + G(Pa('M-20,0 L20,0 L14,-30 L-14,-30 Z', '#c4bcae'), 'translate(30,70)') + crown(76, 64, .3) + G(R(-10, -26, 20, 26, '#5d6469', 2), 'translate(122,70)') + G(R(-12, -24, 24, 24, '#2f3437', 3) + R(-10, -22, 20, 14, '#9fd0ec'), 'translate(168,72)') + arrow(10, 140, 190, 140, '#5d6469', 3))

# ================= 大学 =================
S_('university', sky_ground(176, '#8cc06a') + R(10, 80, 180, 96, '#c8b8a0') + Pa('M10,84 L100,40 L190,84 Z', '#8a5a4a') + ''.join(R(20 + k * 34, 96, 14, 80, '#e6dcc8') for k in range(6)) + R(84, 124, 32, 52, '#5a3a24') + Pa('M80,60 L100,48 L120,60 L100,66 Z', '#2f3437'), False)
S_('college', sky_ground(176, '#8cc06a') + R(30, 70, 140, 106, '#c0603a') + ''.join(R(40 + (k % 4) * 32, 84 + (k // 4) * 30, 18, 20, '#f6e2c8') for k in range(8)) + Pa('M24,74 L100,40 L176,74 Z', '#5a5a5a') + R(86, 140, 28, 36, '#5a3a24') + Pa('M86,40 L100,30 L114,40 L100,44 Z', '#2f3437'), False)
S_('campus', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#8cc06a') + Pa('M80,200 Q100,160 110,120 L120,120 Q118,160 120,200 Z', WALK) + R(20, 60, 70, 60, '#c8b8a0') + R(120, 50, 70, 70, '#c0603a') + tree(40, 150, .6) + tree(170, 150, .6) + fig(150, 196, 'youngman', s=.35) + fig(70, 196, 'youngwoman', s=.35), False)
S_('professor', board_(110, 20, 80, 60, '#2f4a3a', T(150, 56, 'E=mc²', 12, '#ffffff', 800)) + person_bust(70, 90, 30, '#5d6469', P['grey'], 'grey') + Ci(59, 90, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(81, 90, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + Pa('M50,60 L90,60 L100,52 L70,40 L40,52 Z', '#2f3437') + R(60, 120, 20, 4, '#ffffff', 0, 'opacity="0"') + Pa('M50,118 Q70,140 90,118 Q80,134 70,136 Q60,134 50,118 Z', '#c8c3bc'))
S_('lecture', R(0, 0, 200, 200, '#e6dcc8') + R(20, 10, 160, 70, '#ffffff', 3) + R(26, 16, 148, 58, '#9fd0ec') + ''.join(Ci(20 + (k % 7) * 27, 120 + (k // 7) * 36, 10, SK) + Pa(f'M{10+(k%7)*27},{118+(k//7)*36} Q{20+(k%7)*27},{106+(k//7)*36} {30+(k%7)*27},{118+(k//7)*36} Z', ['#3a2a20', '#5a3a2a', P['grey']][k % 3]) + R(8 + (k % 7) * 27, 130 + (k // 7) * 36, 24, 20, ['#3c7fc1', '#e2463b', '#5ba644', '#f3c234'][k % 4], 6) for k in range(14)), False)
S_('degree', G(R(-70, -46, 140, 92, '#fbf3e0', 4) + R(-62, -38, 124, 76, 'none', 3, 'stroke="#d9a33a" stroke-width="3"') + ''.join(L(-40, -20 + k * 12, 40, -20 + k * 12, '#a7adb1', 2) for k in range(4)) + Ci(40, 26, 12, '#e2463b') + Pa('M34,34 L30,50 L40,44 L50,50 L46,34 Z', '#e2463b'), 'translate(100,110)') + Pa('M60,40 L100,24 L140,40 L100,56 Z', '#2f3437') + R(132, 40, 2, 20, '#f3c234'))
S_('major', ''.join(R(14 + k * 46, 50, 40, 100, ['#e2463b', '#3c7fc1', '#5ba644', '#f3c234'][k], 6) for k in range(4)) + T(34, 110, '∑', 24, '#ffffff', 900) + T(80, 110, 'A', 24, '#ffffff', 900) + T(126, 110, '⚗', 0, '#fff') + atom_(126, 100, 14) + T(172, 110, '♪', 0, '#fff') + note(166, 86, .8, '#ffffff') + Pa('M80,30 L100,16 L120,30', 'none', 'stroke="#2f3437" stroke-width="0"'))
S_('dormitory', R(0, 0, 200, 200, '#f2ead8') + R(10, 20, 10, 170, '#8a9196') + R(80, 20, 10, 170, '#8a9196') + R(10, 60, 80, 20, '#5aa1d4', 4) + R(10, 140, 80, 20, '#ef8fa4', 4) + ladder_(84, 180, 84, 60, 0, '#8a9196', 0) + R(110, 100, 80, 10, WOOD, 2) + R(116, 110, 6, 70, '#5d6469') + R(178, 110, 6, 70, '#5d6469') + book_(140, 86, .3, '#3c7fc1', 0) + window_(130, 20, 50, 50), False)
S_('semester', ''.join(R(20 + (k % 3) * 56, 30 + (k // 3) * 74, 48, 62, '#ffffff', 4) + R(20 + (k % 3) * 56, 30 + (k // 3) * 74, 48, 14, '#e2463b' if k < 3 else '#3c7fc1', 4) + T(44 + (k % 3) * 56, 76 + (k // 3) * 74, str(k + 9 if k < 4 else k - 3), 18, '#2f3437', 900) for k in range(6)) + St('M14,24 L186,24', '#5ba644', 0))
S_('graduate', fig(100, 190, 'youngwoman', arms='up') + Pa('M70,30 L100,18 L130,30 L100,42 Z', '#2f3437') + R(124, 30, 2, 16, '#f3c234') + confetti(9, 16, (10, 10, 180, 60)) + G(R(-24, -6, 48, 12, '#fbf3e0', 6) + R(-4, -6, 8, 12, '#e2463b'), 'translate(150,60) rotate(-30)'))
S_('scholarship', G(R(-70, -40, 140, 80, '#fbf3e0', 6) + R(-70, -40, 140, 80, 'none', 6, 'stroke="#d9a33a" stroke-width="4"') + T(0, 8, '¥ 10,000', 22, '#2f3437', 900) + star(-50, -22, 8) + star(50, -22, 8), 'translate(100,90)') + Pa('M80,140 L100,128 L120,140 L100,152 Z', '#2f3437') + coin_(50, 170, 12) + coin_(150, 170, 12))
S_('tuition', R(30, 30, 140, 140, '#ffffff', 4) + R(30, 30, 140, 30, '#3c7fc1', 4) + Pa('M70,44 L100,34 L130,44 L100,54 Z', '#ffffff') + ''.join(L(44, 80 + k * 18, 120, 80 + k * 18, '#a7adb1', 3) for k in range(3)) + T(140, 160, '¥', 30, '#e2463b', 900) + L(44, 140, 156, 140, '#2f3437', 2))
S_('research', R(0, 0, 200, 200, '#e6f0f4') + micro(60, 110, .9) + R(110, 40, 80, 100, '#ffffff', 3) + ''.join(R(118 + k * 16, 120 - h, 10, h, '#5aa1d4') for k, h in enumerate([20, 40, 30, 60])) + St('M118,100 L134,80 L150,90 L170,50', '#e2463b', 3) + Ci(160, 160, 18, 'none', 'stroke="#5d6469" stroke-width="5"') + L(172, 172, 190, 190, '#5d6469', 6), False)
S_('student-card', G(R(-80, -50, 160, 100, '#ffffff', 8) + R(-80, -50, 160, 26, '#e2463b', 8) + R(-80, -32, 160, 8, '#e2463b') + Pa('M-20,-44 L0,-50 L20,-44 L0,-38 Z', '#ffffff') + R(-68, -16, 44, 56, '#dff1fb', 3) + Ci(-46, 4, 12, SK) + Pa('M-58,0 Q-46,-14 -34,0 Z', '#3a2a20') + Pa('M-64,38 Q-46,16 -28,38 Z', '#3c7fc1') + ''.join(L(-10, -6 + k * 12, 64 - (k % 2) * 16, -6 + k * 12, '#a7adb1', 3) for k in range(4)), 'translate(100,100) rotate(-6)'))
S_('thesis', R(50, 30, 110, 150, '#2f4a7a', 4) + R(56, 30, 104, 150, '#3c5a8a', 4) + R(76, 60, 64, 30, '#f3c234', 2) + ''.join(L(84, 70 + k * 8, 132, 70 + k * 8, '#2f3437', 2) for k in range(2)) + ''.join(R(50, 40 + k * 20, 6, 4, '#ffffff') for k in range(7)) + pen_(150, 170, .5, -40))
S_('alumni', ''.join(fig(30 + k * 35, 190, ['man', 'woman', 'oldman', 'youngwoman', 'man'][k], s=.62, arms='wave' if k == 2 else 'down') for k in range(5)) + R(40, 20, 120, 40, '#3c7fc1', 6) + Pa('M80,34 L100,26 L120,34 L100,42 Z', '#ffffff') + T(100, 54, '1980', 0, '#fff') + heart(100, 74, 0))

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
