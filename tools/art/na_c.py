from kit6 import *

def frog_(x, y, s=1, col='#5aaa3a'):
    return G(E(0, 10, 34, 24, col) + E(0, 18, 22, 14, '#c8e0a0') + Ci(-16, -14, 12, col) + Ci(16, -14, 12, col) + Ci(-16, -16, 7, '#ffffff') + Ci(16, -16, 7, '#ffffff') + Ci(-15, -16, 4, '#2f3437') + Ci(17, -16, 4, '#2f3437') + St('M-14,2 Q0,10 14,2', '#2f6a2a', 2) + St('M-30,20 Q-50,30 -40,40 L-24,36', col, 8) + St('M30,20 Q50,30 40,40 L24,36', col, 8), f'translate({x},{y}) scale({s})')
def snake_(x, y, s=1, col='#7aa040', pat='#4a7a2a'):
    return G(St('M-70,30 Q-50,0 -20,20 T40,20 Q60,10 56,-20', col, 16) + St('M-70,30 Q-50,0 -20,20 T40,20 Q60,10 56,-20', pat, 4, 'stroke-dasharray="4 10"') + E(58, -30, 14, 10, col) + Ci(62, -34, 2.5, '#2f3437') + St('M70,-30 l10,-2 M80,-32 l4,-4 M80,-32 l4,2', '#e2463b', 2), f'translate({x},{y}) scale({s})')
def turtle_(x, y, s=1, shell='#5a8a3a', skin='#9ac070', sea=False):
    legs = (E(-30, 16, 16, 8, skin, 'transform="rotate(30 -30 16)"') + E(30, 16, 16, 8, skin, 'transform="rotate(-30 30 16)"') + E(-26, -14, 18, 8, skin, 'transform="rotate(-30 -26 -14)"') + E(26, -14, 18, 8, skin, 'transform="rotate(30 26 -14)"')) if sea else (R(-30, 6, 12, 18, skin, 4) + R(18, 6, 12, 18, skin, 4))
    return G(legs + Ci(46, -4, 13, skin) + Ci(52, -8, 2.5, '#2f3437') + Pa('M-44,10 Q-44,-36 0,-38 Q44,-36 44,10 Z', shell) + ''.join(Pa(f'M{dx-10},{dy} L{dx},{dy-8} L{dx+10},{dy} L{dx+6},{dy+8} L{dx-6},{dy+8} Z', shade(shell, -.15)) for dx, dy in [(-20, -10), (0, -20), (20, -10), (-10, 4), (10, 4)]) + R(-46, 6, 92, 6, shade(shell, .1), 3), f'translate({x},{y}) scale({s})')
def lizard_(x, y, s=1, col='#7ab050'):
    return G(St('M-30,0 Q-70,10 -90,-10', col, 8) + E(0, 0, 34, 12, col) + Ci(36, -2, 11, col) + Ci(40, -6, 2.5, '#2f3437') + St('M-16,6 L-24,22 M14,6 L22,22 M-16,-6 L-26,-20 M14,-6 L24,-20', col, 5), f'translate({x},{y}) scale({s})')
def croc_(x, y, s=1, col='#4a7a3a'):
    return G(St('M-50,0 Q-80,-4 -96,10', col, 14) + E(0, 0, 54, 16, col) + Pa('M40,-12 L100,-6 L100,4 L40,10 Z', col) + ''.join(Pa(f'M{50+j*10},4 l4,6 l4,-6 Z', '#ffffff') for j in range(5)) + Ci(46, -14, 6, col) + Ci(48, -16, 2.5, '#f3c234') + ''.join(Pa(f'M{-40+j*12},-14 l6,-8 l6,8 Z', shade(col, -.15)) for j in range(7)) + R(-36, 10, 10, 14, col, 3) + R(24, 10, 10, 14, col, 3), f'translate({x},{y}) scale({s})')
def chameleon_(x, y, s=1):
    return G(St('M-30,10 Q-60,30 -50,50 Q-36,56 -40,40', '#5aaa3a', 8) + E(0, 0, 34, 20, '#5aaa3a') + Pa('M-20,-18 Q0,-26 20,-18', 'none', 'stroke="#3c8a2a" stroke-width="3"') + Pa('M28,-16 L46,-30 L50,0 L30,8 Z', '#5aaa3a') + Ci(38, -6, 8, '#f3c234') + Ci(39, -6, 3, '#2f3437') + St('M48,-2 Q70,0 80,-10', '#ef8fa4', 3) + Ci(82, -12, 5, '#ef8fa4') + ''.join(Ci(-10 + j * 12, 2, 4, ['#f3c234', '#3c7fc1', '#e2463b'][j % 3]) for j in range(4)) + L(-14, 18, -18, 34, '#5aaa3a', 5) + L(14, 18, 18, 34, '#5aaa3a', 5), f'translate({x},{y}) scale({s})')
def dog_(x, base, s=1, col='#c8903a', ear=None):
    return quad(x, base, s, col, '#f0d8b0', 34, 46, 22, (44, -66), 18, '#f0d8b0', 'droop', ear or shade(col, -.25), 'thin', col)
def cat_(x, base, s=1, col='#f3a234'):
    k = s
    return G(St('M-40,-50 Q-80,-60 -70,-110', col, 7) + R(-30, -40, 12, 40, shade(col, -.1), 5) + R(14, -40, 12, 40, shade(col, -.1), 5) + E(0, -50, 40, 22, col) + R(-22, -40, 12, 40, col, 5) + R(22, -40, 12, 40, col, 5) + Ci(42, -76, 20, col) + Pa('M26,-88 L28,-108 L40,-94 Z', col) + Pa('M46,-94 L58,-108 L60,-88 Z', col) + Ci(36, -78, 3, '#2f3437') + Ci(50, -78, 3, '#2f3437') + Pa('M41,-70 L45,-70 L43,-67 Z', '#ef8fa4') + L(48, -68, 68, -72, '#5d6469', 1) + L(48, -66, 68, -64, '#5d6469', 1) + ''.join(L(-24 + j * 12, -68, -20 + j * 12, -56, shade(col, -.25), 3) for j in range(4)), f'translate({x},{base}) scale({k})')
def rabbit_(x, base, s=1, col='#ffffff'):
    return G(Ci(-40, -30, 10, col, 'stroke="#d9dcde" stroke-width="1"') + E(-6, -30, 36, 28, col, 'stroke="#d9dcde" stroke-width="1"') + E(20, -6, 18, 6, col, 'stroke="#d9dcde" stroke-width="1"') + Ci(30, -58, 18, col, 'stroke="#d9dcde" stroke-width="1"') + E(20, -96, 7, 24, col, 'stroke="#d9dcde" stroke-width="1"') + E(34, -98, 7, 24, col, 'stroke="#d9dcde" stroke-width="1"') + E(20, -96, 3, 16, '#f6c8d4') + E(34, -98, 3, 16, '#f6c8d4') + Ci(36, -60, 2.5, '#2f3437') + Ci(46, -54, 3, '#ef8fa4'), f'translate({x},{base}) scale({s})')
def hamster_(x, y, s=1):
    return G(E(0, 0, 40, 32, '#e8b070') + E(0, 10, 26, 18, '#ffffff') + Ci(-24, -26, 8, '#e8b070') + Ci(24, -26, 8, '#e8b070') + Ci(-24, -26, 4, '#f6c8d4') + Ci(24, -26, 4, '#f6c8d4') + Ci(-12, -8, 3.5, '#2f3437') + Ci(12, -8, 3.5, '#2f3437') + E(0, 0, 3, 2, '#ef8fa4') + E(-22, 4, 8, 6, '#f6c8d4', 'opacity=".6"') + E(22, 4, 8, 6, '#f6c8d4', 'opacity=".6"'), f'translate({x},{y}) scale({s})')
def guinea_(x, y, s=1):
    return G(E(0, 0, 46, 28, '#ffffff', 'stroke="#d9dcde" stroke-width="1"') + E(-16, -6, 26, 22, '#c8783a') + E(30, -4, 20, 20, '#2f3437') + Ci(36, -8, 3, '#ffffff') + Ci(48, 2, 3, '#ef8fa4') + E(26, -22, 8, 5, '#c8783a') + E(-30, 24, 8, 4, '#ef8fa4') + E(20, 24, 8, 4, '#ef8fa4'), f'translate({x},{y}) scale({s})')
def cow_(x, base, s=1):
    k = s
    return quad(x, base, s, '#ffffff', None, 40, 56, 30, (60, -80), 20, '#f6c8c0', 'point', '#ffffff', 'tuft', '#ffffff', hoof='#2f3437') + G(E(-20, -84, 14, 10, '#2f3437') + E(16, -72, 12, 9, '#2f3437') + E(-34, -66, 8, 6, '#2f3437') + St('M48,-96 q-6,-10 -2,-16 M70,-96 q6,-10 2,-16', '#e6dcc8', 4) + E(10, -50, 10, 6, '#f6c8c0'), f'translate({x},{base}) scale({k})')
def pig_(x, base, s=1, col='#f6b8c4'):
    k = s
    return quad(x, base, s, col, None, 24, 52, 30, (54, -60), 22, '#ef8fa4', 'point', shade(col, -.1), 'curly', shade(col, -.1)) + G(Ci(72, -54, 2, '#9a4a5a') + Ci(78, -56, 2, '#9a4a5a'), f'translate({x},{base}) scale({k})')
def sheep_(x, base, s=1):
    k = s
    return G(R(-36, -40, 10, 40, '#4a4440', 4) + R(24, -40, 10, 40, '#4a4440', 4) + ''.join(Ci(dx, dy, 16, '#f6f2ea', 'stroke="#e6e0d6" stroke-width="1"') for dx, dy in [(-30, -56), (-10, -66), (10, -66), (30, -56), (-20, -44), (0, -46), (20, -44), (-34, -40)]) + E(48, -60, 14, 18, '#4a4440') + E(40, -66, 8, 5, '#4a4440') + Ci(52, -64, 2.5, '#ffffff') + Ci(44, -76, 8, '#f6f2ea'), f'translate({x},{base}) scale({k})')
def goat_(x, base, s=1):
    k = s
    return quad(x, base, s, '#e6dcc8', None, 44, 46, 22, (50, -84), 15, '#d8c8b0', 'point', '#c8b8a0', 'short', '#e6dcc8', True, True, hoof='#5d6469') + G(St('M44,-96 Q36,-114 26,-110 M52,-98 Q48,-118 38,-116', '#8a7a6a', 4) + Pa('M56,-74 L60,-58 L64,-74 Z', '#e6dcc8'), f'translate({x},{base}) scale({k})')
def hen_(x, base, s=1, col='#c8783a', rooster=False):
    g = L(-6, -20, -8, 0, '#f3c234', 3) + L(6, -20, 8, 0, '#f3c234', 3)
    if rooster: g += Pa('M-26,-46 Q-60,-80 -50,-30 Q-40,-50 -30,-30 Q-50,-40 -26,-26 Z', '#2f6a4a') + Pa('M-30,-50 Q-60,-70 -54,-34 Z', '#e2463b')
    else: g += Pa('M-26,-44 L-46,-62 L-40,-34 Z', shade(col, -.2))
    g += E(0, -36, 30, 22, col) + E(-4, -36, 18, 12, shade(col, -.15)) + Ci(22, -58, 13, col) + Pa('M14,-70 q4,-10 8,-2 q4,-10 8,0 q4,-8 4,4 Z', '#e2463b') + (Pa('M12,-74 q6,-16 10,-4 q6,-16 10,0 q6,-10 4,6 Z', '#e2463b') if rooster else '') + Pa('M34,-60 L44,-56 L34,-52 Z', '#f3c234') + E(32, -48, 3, 5, '#e2463b') + Ci(26, -62, 2.5, '#2f3437')
    return G(g, f'translate({x},{base}) scale({s})')
def chick_(x, base, s=1):
    return G(L(-4, -10, -6, 0, '#f08a24', 2) + L(4, -10, 6, 0, '#f08a24', 2) + E(0, -24, 20, 16, '#f6d840') + Ci(12, -42, 12, '#f6d840') + Pa('M22,-44 L30,-40 L22,-38 Z', '#f08a24') + Ci(16, -45, 2, '#2f3437') + E(-4, -24, 10, 6, '#f0c830'), f'translate({x},{base}) scale({s})')
def goose_(x, base, s=1):
    return G(L(-6, -20, -8, 0, '#f08a24', 4) + L(6, -20, 8, 0, '#f08a24', 4) + E(0, -36, 34, 22, '#f6f4ee', 'stroke="#d9dcde" stroke-width="1"') + E(-6, -38, 20, 12, '#e6e2dc') + St('M24,-46 Q32,-80 26,-94', '#f6f4ee', 10) + Ci(28, -96, 9, '#f6f4ee') + Pa('M34,-98 L50,-92 L34,-88 Z', '#f08a24') + E(34, -100, 4, 3, '#f08a24') + Ci(30, -98, 2, '#2f3437'), f'translate({x},{base}) scale({s})')
def donkey_(x, base, s=1):
    k = s
    return quad(x, base, s, '#9a8a8a', '#e6dcd8', 42, 48, 24, (56, -86), 16, '#e6dcd8', 'long', '#8a7a7a', 'tuft', '#9a8a8a', True, True, hoof='#5d6469') + G(Pa('M40,-92 L52,-100 L46,-72 Z', '#5a4a4a'), f'translate({x},{base}) scale({k})')
def bull_(x, base, s=1):
    k = s
    return quad(x, base, s, '#5a3a24', None, 36, 60, 32, (62, -74), 22, '#8a5a3a', 'point', '#4a2a14', 'tuft', '#5a3a24', hoof='#2f3437') + G(Pa('M44,-94 Q30,-112 24,-100 Q34,-100 42,-86 Z', '#e6dcc8') + Pa('M78,-92 Q92,-110 98,-98 Q88,-98 80,-84 Z', '#e6dcc8') + Ci(82, -62, 5, 'none', 'stroke="#d9a33a" stroke-width="2"'), f'translate({x},{base}) scale({k})')
def whale_(x, y, s=1, col='#3c6a9a'):
    return G(Pa('M-80,0 Q-60,-50 20,-44 Q80,-40 90,0 Q70,30 0,30 Q-50,30 -80,0 Z', col) + Pa('M-20,14 Q30,30 80,8 Q60,26 0,28 Q-30,26 -20,14 Z', '#c8d8e6') + Pa('M-78,-2 L-110,-30 L-100,0 L-110,24 Z', col) + Ci(54, -8, 4, '#2f3437') + St('M60,8 Q70,12 80,6', '#2f4a6a', 2) + St('M10,-46 Q4,-70 -8,-74 M10,-46 Q16,-70 28,-74', '#9fd0ec', 4), f'translate({x},{y}) scale({s})')
def dolphin_(x, y, s=1):
    return G(Pa('M-70,10 Q-40,-40 30,-30 Q60,-26 80,-12 L96,-10 L80,-2 Q50,10 0,14 Q-40,16 -70,10 Z', '#6a9ac0') + Pa('M-10,-30 L6,-54 L20,-30 Z', '#6a9ac0') + Pa('M-70,10 L-96,-6 L-88,14 L-100,30 Z', '#6a9ac0') + Pa('M-40,10 Q0,18 60,0 Q20,14 -30,16 Z', '#dfeef6') + Ci(56, -16, 3, '#2f3437') + E(10, 10, 12, 6, '#5a8ab0', 'transform="rotate(30 10 10)"'), f'translate({x},{y}) scale({s})')
def shark_(x, y, s=1):
    return G(Pa('M-80,0 Q-40,-30 30,-26 Q70,-22 90,0 Q60,20 0,20 Q-40,18 -80,0 Z', '#7a8a9a') + Pa('M-10,-26 L6,-60 L24,-24 Z', '#7a8a9a') + Pa('M-80,0 L-104,-30 L-96,0 L-104,26 Z', '#7a8a9a') + Pa('M-40,8 Q20,22 80,4 Q30,18 -20,18 Z', '#e6ecef') + Ci(56, -6, 3.5, '#2f3437') + ''.join(Pa(f'M{60+j*6},6 l3,5 l3,-5 Z', '#ffffff') for j in range(4)) + ''.join(L(30 - j * 6, -4, 28 - j * 6, 8, '#5a6a7a', 1.5) for j in range(3)), f'translate({x},{y}) scale({s})')
def octopus_(x, y, s=1, col='#c8508a'):
    return G(''.join(St(f'M{-30+j*9},10 Q{-50+j*14},{50} {-40+j*12},{70+(j%2)*6}', col, 8) for j in range(8)) + Pa('M-36,14 Q-40,-50 0,-54 Q40,-50 36,14 Z', col) + Ci(-12, -10, 8, '#ffffff') + Ci(12, -10, 8, '#ffffff') + Ci(-11, -9, 4, '#2f3437') + Ci(13, -9, 4, '#2f3437') + St('M-6,4 Q0,8 6,4', '#8a2a5a', 2), f'translate({x},{y}) scale({s})')
def jelly_(x, y, s=1, col='#c8a0f0'):
    return G(''.join(St(f'M{-20+j*10},0 Q{-26+j*10},30 {-18+j*10},60 Q{-22+j*10},80 {-16+j*10},96', col, 3, 'opacity=".8"') for j in range(5)) + Pa('M-40,0 Q-40,-50 0,-50 Q40,-50 40,0 Q30,-6 20,0 Q10,-6 0,0 Q-10,-6 -20,0 Q-30,-6 -40,0 Z', col, 'opacity=".9"') + hi(-14, -30, 10, 5, .6), f'translate({x},{y}) scale({s})')
def starfish_(x, y, s=1, col='#f08a24'):
    pts = []
    for k in range(10):
        a = math.radians(-90 + k * 36); rr = 50 if k % 2 == 0 else 22
        pts.append(f'{rr*math.cos(a):.1f},{rr*math.sin(a):.1f}')
    return G(f'<polygon points="{" ".join(pts)}" fill="{col}" stroke="{shade(col,-.15)}" stroke-width="4" stroke-linejoin="round"/>' + ''.join(Ci(30 * math.cos(math.radians(-90 + k * 72)) * (j / 3), 30 * math.sin(math.radians(-90 + k * 72)) * (j / 3), 2.5, '#fbe0b0') for k in range(5) for j in range(1, 4)), f'translate({x},{y}) scale({s})')
def seal_(x, y, s=1, col='#8a9196'):
    return G(Pa('M-70,20 Q-60,-10 -10,-20 Q30,-30 40,-60 Q60,-70 66,-50 Q70,0 20,24 Z', col) + Pa('M-70,20 L-90,6 L-86,24 L-96,34 Z', col) + E(10, 24, 16, 6, shade(col, -.1)) + Ci(56, -56, 3, '#2f3437') + E(66, -48, 4, 3, '#2f3437') + L(64, -46, 80, -50, '#5d6469', 1) + L(64, -46, 80, -42, '#5d6469', 1), f'translate({x},{y}) scale({s})')
def seahorse_(x, y, s=1, col='#f3a234'):
    return G(Pa('M0,-60 Q24,-56 20,-36 L36,-30 L20,-26 Q14,-6 18,20 Q20,50 0,60 Q-14,64 -10,50 Q4,50 4,30 Q0,10 -10,-10 Q-20,-40 0,-60 Z', col) + ''.join(L(-14 + j * 2, -40 + j * 12, -22 + j * 2, -36 + j * 12, shade(col, -.2), 3) for j in range(6)) + Ci(8, -46, 3, '#2f3437') + E(-8, 10, 6, 12, shade(col, .2), 'transform="rotate(-20 -8 10)"'), f'translate({x},{y}) scale({s})')
def coral_(x, base, s=1, col='#ef7a6a'):
    return G(St('M0,0 L0,-50 M0,-30 L-20,-56 M0,-40 L18,-70 M-20,-56 L-30,-74 M-20,-56 L-10,-80 M18,-70 L30,-86', col, 9), f'translate({x},{base}) scale({s})')
def ocean_bg(top='#2f7ab0', bot='#1f5a8a', sand=True):
    return R(0, 0, 200, 200, top) + R(0, 100, 200, 100, bot, 0, 'opacity=".5"') + ''.join(Ci(20 + k * 40, 30 + (k % 3) * 30, 3 + k % 3, '#9fd0ec', 'opacity=".5"') for k in range(5)) + (Pa('M0,180 Q100,166 200,182 L200,200 L0,200 Z', '#d9c28a') if sand else '')

# ================= 爬行 =================
S_('frog', R(0, 0, 200, 200, '#cfe8f6') + R(0, 120, 200, 80, '#5aa1d4') + E(100, 150, 60, 16, '#5aaa3a') + frog_(100, 120, 1.4), False)
S_('snake', R(0, 0, 200, 200, '#e6dcc0') + snake_(100, 100, 1.2), False)
S_('turtle', R(0, 0, 200, 200, '#e6f4e0') + R(0, 150, 200, 50, '#9ac070') + turtle_(100, 140, 1.4), False)
S_('tortoise', R(0, 0, 200, 200, '#f6e8c8') + R(0, 150, 200, 50, '#d8c070') + turtle_(100, 136, 1.4, '#8a6a3a', '#a89070') + G(Pa('M-44,10 Q-44,-56 0,-58 Q44,-56 44,10 Z', '#8a6a3a'), 'translate(100,136) scale(1.4)') + ''.join(Pa(f'M{100+dx*1.4-12},{136+dy*1.4} l12,-10 l12,10 l-6,10 l-12,0 Z', '#6a4a2a') for dx, dy in [(-20, -20), (0, -36), (20, -20), (-10, -2), (10, -2)]), False)
S_('lizard', R(0, 0, 200, 200, '#f0d8b0') + Pa('M0,140 Q100,120 200,150 L200,200 L0,200 Z', '#c8a070') + lizard_(110, 120, 1.3), False)
S_('crocodile', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#5a8a7a') + croc_(90, 120, .95), False)
S_('toad', R(0, 0, 200, 200, '#e6dcc0') + frog_(100, 110, 1.5, '#8a7a4a') + ''.join(Ci(80 + (k * 13) % 40, 110 + (k * 7) % 20, 3, '#6a5a3a') for k in range(8)), False)
S_('tadpole', R(0, 0, 200, 200, '#5aa1d4') + ''.join(G(Ci(0, 0, 12, '#2f3437') + St('M-10,0 Q-26,-8 -40,4', '#2f3437', 4) + Ci(4, -4, 2, '#ffffff'), f'translate({x},{y}) rotate({r_})') for x, y, r_ in [(60, 70, 10), (130, 100, -20), (90, 150, 30)]) + ''.join(St(f'M{20+k*50},200 L{20+k*50},160', '#5a8a3a', 3) for k in range(4)), False)
S_('alligator', R(0, 0, 200, 200, '#dff1d8') + R(0, 120, 200, 80, '#7a9a6a') + croc_(90, 128, .95, '#3a5a2a') + Pa('M140,116 Q170,116 190,124', 'none', 'stroke="#000" stroke-width="0"'), False)
S_('chameleon', R(0, 0, 200, 200, '#e6f4e0') + St('M0,150 Q100,140 200,156', '#8a5a35', 8) + chameleon_(90, 110, 1.3), False)
S_('gecko', R(0, 0, 200, 200, '#f2ead8') + G(lizard_(0, 0, 1.3, '#c8b070') + ''.join(Ci(-20 + j * 14, 0, 4, '#e8d090') for j in range(4)), 'translate(100,100) rotate(-60)'), False)
S_('cobra', R(0, 0, 200, 200, '#f0d8b0') + Pa('M60,190 Q20,170 60,150 Q100,140 90,110 L80,60 Q100,20 120,60 L110,110 Q120,150 160,160 Q190,180 150,194 Z', '#8a6a3a') + E(100, 60, 30, 36, '#a8803a') + E(100, 66, 14, 24, '#e8d090') + Ci(92, 46, 3, '#2f3437') + Ci(108, 46, 3, '#2f3437') + St('M100,60 l0,10 M100,70 l-4,6 M100,70 l4,6', '#e2463b', 2), False)
S_('python', R(0, 0, 200, 200, '#dff1d8') + St('M0,120 L200,100', '#8a5a35', 14) + G(St('M-80,10 Q-60,-30 -20,-10 Q20,10 40,-20 Q60,-50 80,-30', '#c8a050', 22) + St('M-80,10 Q-60,-30 -20,-10 Q20,10 40,-20 Q60,-50 80,-30', '#6a4a2a', 8, 'stroke-dasharray="6 12"') + E(88, -36, 18, 12, '#c8a050') + Ci(94, -40, 3, '#2f3437') + St('M104,-36 l10,0 M114,-36 l4,-4 M114,-36 l4,4', '#e2463b', 2), 'translate(90,110)'), False)
S_('iguana', R(0, 0, 200, 200, '#f0e0c0') + lizard_(110, 120, 1.4, '#5aa060') + ''.join(Pa(f'M{110+(-24+j*8)*1.4},{120-14*1.4} l4,-10 l4,10 Z', '#3c7a3a') for j in range(7)) + E(160, 130, 8, 10, '#e8b070'), False)
S_('salamander', R(0, 0, 200, 200, '#3a3a3a') + R(0, 140, 200, 60, '#5a4a3a') + G(lizard_(0, 0, 1.3, '#2f3437') + ''.join(Ci(-30 + j * 14, (-1) ** j * 4, 5, '#f3c234') for j in range(5)), 'translate(100,120)'), False)
S_('scales', ''.join(Pa(f'M{x-14},{y} Q{x},{y+24} {x+14},{y} Q{x},{y+8} {x-14},{y} Z', '#5aaa3a', 'stroke="#3c7a2a" stroke-width="2"') for x, y in [(30 + (k % 6) * 28 + (k // 6 % 2) * 14, 30 + (k // 6) * 22) for k in range(42)]))

# ================= 宠物 =================
S_('pet', R(0, 0, 200, 200, '#fef3e2') + dog_(70, 186, .9) + cat_(140, 186, .7) + heart(100, 40, 12), False)
S_('dog', R(0, 0, 200, 200, '#e6f4e0') + R(0, 170, 200, 30, '#9ac070') + dog_(90, 186, 1.3), False)
S_('cat', R(0, 0, 200, 200, '#fef3e2') + cat_(90, 186, 1.2), False)
S_('puppy', R(0, 0, 200, 200, '#fef3e2') + dog_(100, 180, .9, '#e8c090') + G(Ci(0, 0, 8, '#e2463b'), 'translate(150,172)'), False)
S_('kitten', R(0, 0, 200, 200, '#fef3e2') + cat_(90, 180, .8, '#a7adb1') + yarn_ball(160, 166, 14, '#ef8fa4'), False)
S_('rabbit', R(0, 0, 200, 200, '#e6f4e0') + R(0, 160, 200, 40, '#9ac070') + rabbit_(100, 176, 1.3) + carrot(160, 170, .5, -30), False)
S_('goldfish', R(0, 0, 200, 200, '#fef3e2') + Pa('M40,60 Q30,180 100,180 Q170,180 160,60 Z', '#cfe8f6', 'opacity=".8"') + E(100, 60, 60, 10, '#9fd0ec') + fish2(100, 120, 1.0, '#f08a24') + ''.join(Ci(130 + k * 6, 90 - k * 12, 3, '#ffffff') for k in range(3)), False)
S_('hamster', R(0, 0, 200, 200, '#fef3e2') + R(0, 150, 200, 50, '#f0d8a8') + hamster_(100, 120, 1.4), False)
S_('feed', R(0, 0, 200, 200, '#fef3e2') + dog_(60, 186, .8) + E(130, 180, 30, 8, '#e2463b') + E(130, 176, 24, 5, '#8a5a35') + G(R(-20, -30, 40, 50, '#f3c234', 4), 'translate(160,110) rotate(40)') + ''.join(Ci(140 + k * 6, 150 + (k % 2) * 6, 3, '#8a5a35') for k in range(3)), False)
S_('walk-the-dog', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(60, 196, .8, '#3c7fc1', '#3b4a5a', legs='walk') + dog_(140, 196, .7) + St('M80,128 Q110,150 166,146', '#e2463b', 2), False)
S_('leash', St('M40,40 Q80,160 150,140', '#e2463b', 6) + R(26, 26, 30, 30, 'none', 10, 'stroke="#e2463b" stroke-width="8"') + E(150, 140, 30, 14, 'none', 'stroke="#3c7fc1" stroke-width="8"') + Ci(130, 134, 5, '#d9a33a'))
S_('cage', R(40, 40, 120, 130, '#ffffff', 0, 'opacity=".3"') + ''.join(L(40 + k * 15, 40, 40 + k * 15, 170, '#a7adb1', 3) for k in range(9)) + Pa('M40,40 Q100,0 160,40 Z', 'none', 'stroke="#a7adb1" stroke-width="3"') + R(30, 166, 140, 12, '#5d6469', 3) + bird(100, 110, 1.0, '#f3c234', '#f6e070', '#f08a24', legs=True) + Ci(100, 14, 6, 'none', 'stroke="#a7adb1" stroke-width="3"'))
S_('fish-tank', R(20, 40, 160, 120, '#9fd0ec', 4, 'opacity=".85"') + R(20, 40, 160, 10, '#5d6469') + R(20, 150, 160, 10, '#d9c28a') + fish2(70, 100, .6, '#f08a24') + fish2(130, 80, .5, '#3c7fc1') + ''.join(St(f'M{40+k*30},150 Q{36+k*30},120 {44+k*30},100', '#4a9a3a', 3) for k in range(0)) + St('M160,150 Q150,120 164,90', '#4a9a3a', 4) + ''.join(Ci(100 + k * 6, 130 - k * 16, 3, '#ffffff') for k in range(3)) + R(18, 160, 164, 10, '#5d6469'))
S_('pet-food', G(R(-40, -60, 80, 110, '#e2463b', 6) + R(-30, -40, 60, 40, '#ffffff', 4) + Pa('M-10,-30 Q0,-40 10,-30 Q14,-16 0,-12 Q-14,-16 -10,-30 Z', '#8a5a35') + Ci(-12, -34, 4, '#8a5a35') + Ci(12, -34, 4, '#8a5a35') + R(-40, -66, 80, 10, '#c0283a', 3), 'translate(80,100)') + E(150, 170, 34, 10, '#3c7fc1') + ''.join(Ci(134 + k * 8, 164, 5, '#8a5a35') for k in range(5)))
S_('guinea-pig', R(0, 0, 200, 200, '#fef3e2') + R(0, 150, 200, 50, '#e6d8a8') + guinea_(100, 130, 1.3), False)
S_('litter-box', R(30, 110, 140, 60, '#3c7fc1', 8) + R(36, 104, 128, 16, '#d9c8a0', 6) + ''.join(Ci(50 + k * 12, 110, 3, '#c8b890') for k in range(9)) + cat_(100, 100, .5, '#a7adb1') + R(140, 160, 40, 10, '#5d6469', 3, 'transform="rotate(-20 160 165)"'))

# ================= 农场动物 =================
S_('cow', meadow() + cow_(90, 186, 1.0), False)
S_('pig', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#8a6a4a') + pig_(90, 180, 1.2), False)
S_('sheep', meadow() + sheep_(90, 180, 1.4), False)
S_('goat', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,150 L80,120 L200,150 L200,200 Z', '#a8a090') + goat_(90, 180, 1.0), False)
S_('hen', R(0, 0, 200, 200, '#fef3e2') + R(0, 160, 200, 40, '#e8c880') + hen_(100, 176, 1.6) + egg(160, 172, .6), False)
S_('rooster', R(0, 0, 200, 200, '#ffe2b8') + R(0, 160, 200, 40, '#8a5a35') + hen_(100, 168, 1.6, '#c8603a', True) + sun(170, 40, 14), False)
S_('chick', R(0, 0, 200, 200, '#fef3e2') + R(0, 160, 200, 40, '#e8c880') + chick_(80, 176, 2.0) + G(Pa('M-20,0 L-14,-10 L-6,0 L2,-10 L10,0 L18,-10 L22,0 Q20,20 0,20 Q-20,20 -20,0 Z', '#f6efe0'), 'translate(150,170)'), False)
S_('goose', meadow() + goose_(100, 186, 1.4), False)
S_('donkey', meadow() + donkey_(90, 186, 1.0), False)
S_('bull', R(0, 0, 200, 200, '#f6e8c8') + R(0, 160, 200, 40, '#c8a070') + bull_(90, 186, 1.0), False)
S_('calf', meadow() + cow_(70, 186, .7) + G(cow_(0, 0, .5), 'translate(150,186)'), False)
S_('piglet', R(0, 0, 200, 200, '#fef3e2') + R(0, 160, 200, 40, '#e8c880') + pig_(90, 176, .8, '#f6c8d4'), False)
S_('duckling', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#5aa1d4') + chick_(80, 160, 1.6) + G(Pa('M22,-44 L34,-40 L22,-36 Z', '#f08a24'), 'translate(80,160) scale(1.6)') + chick_(150, 170, 1.0), False)
S_('sheepdog', meadow() + dog_(60, 186, .9, '#2f3437') + G(Pa('M40,-60 Q60,-80 70,-60 L66,-40 L44,-40 Z', '#ffffff'), 'translate(60,186) scale(.9)') + sheep_(150, 186, .7), False)
S_('mule', meadow() + donkey_(90, 186, 1.0) + G(R(-20, -84, 40, 20, '#c8903a', 4) + R(-24, -66, 10, 24, '#a8703e', 3) + R(14, -66, 10, 24, '#a8703e', 3), 'translate(90,186)'), False)
S_('shepherd', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,140 Q100,110 200,140 L200,200 Z', '#9ac070') + W(50, 196, .9, '#8a5a35', '#3b4a5a', 'straw') + St('M80,100 L80,190 M80,100 Q80,84 92,86', '#8a5a35', 3) + sheep_(130, 186, .5) + sheep_(170, 176, .4), False)

# ================= 海洋 =================
S_('whale', ocean_bg() + whale_(100, 110, 1.0), False)
S_('dolphin', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#2f7ab0') + G(dolphin_(0, 0, .9), 'translate(100,100) rotate(-20)') + St('M20,130 q20,-6 40,0 t40,0 t40,0 t40,0', '#9fd0ec', 3), False)
S_('shark', ocean_bg() + shark_(100, 100, 1.0), False)
S_('octopus', ocean_bg() + octopus_(100, 90, 1.3), False)
S_('jellyfish', ocean_bg('#1f4a7a', '#1a3a6a', False) + jelly_(100, 80, 1.2), False)
S_('starfish', R(0, 0, 200, 200, '#f0d890') + starfish_(100, 100, 1.4) + shell_(170, 170, .3), False)
S_('seal-ocean', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#3c9ad4') + rock_(100, 160, 1.4, '#8a8a8a') + seal_(100, 120, 1.0), False)
S_('sea-turtle', ocean_bg() + turtle_(100, 100, 1.3, '#4a8a6a', '#8ab890', True), False)
S_('seahorse', ocean_bg() + seahorse_(100, 100, 1.3) + coral_(40, 190, .6) + coral_(160, 190, .5, '#f3a234'), False)
S_('coral', ocean_bg() + coral_(60, 190, 1.0) + coral_(120, 190, 1.2, '#f3a234') + coral_(170, 190, .8, '#c8508a') + fish2(140, 70, .4, '#f3c234'), False)
S_('aquarium', R(0, 0, 200, 200, '#1a2a4a') + R(10, 20, 180, 140, '#2f7ab0', 6) + fish2(60, 70, .5, '#f08a24') + fish2(140, 100, .5, '#f3c234', stripes='#2f3437') + shark_(90, 130, .4) + R(10, 150, 180, 10, '#d9c28a') + ''.join(G(Ci(0, 0, 8, SK) + R(-8, 8, 16, 24, c, 4), f'translate({40+k*60},180)') for k, c in enumerate(['#e2463b', '#3c7fc1', '#5ba644'])), False)
S_('tropical-fish', ocean_bg() + fish2(80, 80, .9, '#f08a24', '#2f3437', '#ffffff') + fish2(140, 140, .7, '#f3c234', '#3c7fc1') + coral_(40, 196, .5), False)
S_('sea-lion', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#3c9ad4') + rock_(100, 170, 1.4, '#8a8a8a') + seal_(100, 134, 1.0, '#8a5a35') + G(Ci(0, 0, 10, '#e2463b') + R(-10, -2, 20, 4, '#ffffff'), 'translate(166,64)'), False)
S_('killer-whale', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#2f7ab0') + G(Pa('M-80,10 Q-50,-40 20,-36 Q70,-30 90,0 Q60,24 0,24 Q-50,22 -80,10 Z', '#1f2328') + Pa('M-10,-34 L0,-80 L16,-32 Z', '#1f2328') + Pa('M-80,8 L-104,-16 L-98,8 L-106,30 Z', '#1f2328') + Pa('M-30,14 Q20,26 80,4 Q30,20 -20,20 Z', '#ffffff') + E(50, -14, 12, 6, '#ffffff'), 'translate(100,110) rotate(-10)'), False)
S_('stingray', ocean_bg() + G(Pa('M0,-40 Q60,-20 80,10 Q40,10 0,40 Q-40,10 -80,10 Q-60,-20 0,-40 Z', '#8a8070') + St('M0,40 Q10,80 30,90', '#8a8070', 3) + Ci(-10, -16, 3, '#2f3437') + Ci(10, -16, 3, '#2f3437') + ''.join(Ci(-30 + j * 15, 0, 3, '#a89a88') for j in range(5)), 'translate(100,90)'), False)
S_('sea-urchin', ocean_bg() + ''.join(L(100, 130, 100 + 50 * math.cos(a), 130 + 50 * math.sin(a), '#3a2a5a', 3) for a in [k * math.pi / 14 for k in range(28)]) + Ci(100, 130, 26, '#4a3a6a'), False)

dump()
