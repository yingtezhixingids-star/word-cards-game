from kit6 import *

SAV = '#f0d890'
def savanna(y=140):
    return R(0, 0, 200, 200, '#cfe8f6') + R(0, y, 200, 200 - y, '#d8c070') + ''.join(St(f'M{(k*23)%200},{200-(k%4)*12} l-2,-10 M{(k*23)%200},{200-(k%4)*12} l2,-10', '#b8a050', 2) for k in range(24))
def meadow(y=150, sky=SKY):
    return R(0, 0, 200, 200, sky) + R(0, y, 200, 200 - y, '#9ac070')
def forest_bg(y=150):
    return R(0, 0, 200, 200, '#dff1d8') + pine(20, y, .6) + pine(180, y, .7) + R(0, y, 200, 200 - y, '#7aa050')
def snow_land(y=150):
    return R(0, 0, 200, 200, '#cfe2f0') + R(0, y, 200, 200 - y, '#ffffff')

def lion(x, base, s=1):
    k = s
    g = quad(x, base, s, '#d8a050', '#e8c080', 42, 56, 28, (54, -78), 20, '#f0d8a8', 'round', '#c08840', 'tuft', '#d8a050')
    g += G(Ci(54, -78, 34, '#a8602a') + ''.join(Ci(54 + 32 * math.cos(a), -78 + 32 * math.sin(a), 10, '#a8602a') for a in [j * .52 for j in range(12)]) + Ci(54, -78, 20, '#d8a050') + Ci(48, -96, 6, '#c08840') + Ci(66, -96, 6, '#c08840') + E(62, -72, 10, 8, '#f0d8a8') + Pa('M60,-76 L68,-76 L64,-70 Z', '#5a3a2a') + Ci(50, -84, 2.5, '#2f3437') + Ci(62, -84, 2.5, '#2f3437'), f'translate({x},{base}) scale({k})')
    return g
def tiger(x, base, s=1):
    k = s
    g = quad(x, base, s, '#f08a24', '#fbe8cc', 40, 58, 28, (56, -74), 20, '#fbe8cc', 'round', '#d9701a', 'thin', '#f08a24')
    g += G(''.join(Pa(f'M{-40+j*14},-98 L{-36+j*14},-78 L{-32+j*14},-98 Z', '#2f3437') for j in range(6)) + Pa('M46,-92 L50,-84 L54,-92 Z', '#2f3437') + Pa('M60,-90 L62,-82 L66,-90 Z', '#2f3437') + St('M-70,-60 l-6,6 M-74,-46 l-6,4', '#2f3437', 3), f'translate({x},{base}) scale({k})')
    return g
def elephant(x, base, s=1):
    k = s
    g = G(R(-50, -60, 22, 60, '#8a959c', 6) + R(30, -60, 22, 60, '#8a959c', 6) + E(0, -74, 64, 44, '#9aa6ae') + R(-36, -50, 22, 50, '#9aa6ae', 6) + R(16, -50, 22, 50, '#9aa6ae', 6) + Ci(58, -90, 30, '#9aa6ae') + E(40, -88, 20, 28, '#8a959c') + St('M80,-82 Q96,-50 84,-18 Q80,-10 74,-16', '#9aa6ae', 14) + Pa('M70,-70 Q84,-60 88,-74', 'none', 'stroke="#f6efe0" stroke-width="5" stroke-linecap="round"') + Ci(66, -98, 3, '#2f3437') + St('M-62,-80 q-12,10 -8,26', '#9aa6ae', 3), f'translate({x},{base}) scale({k})')
    return g
def monkey(x, y, s=1):
    return G(St('M20,30 Q60,40 50,-10 Q46,-30 60,-30', '#8a5a35', 6) + E(0, 20, 26, 30, '#8a5a35') + E(0, 26, 16, 20, '#d8b890') + Ci(0, -24, 24, '#8a5a35') + Ci(-24, -24, 9, '#8a5a35') + Ci(24, -24, 9, '#8a5a35') + Ci(-24, -24, 5, '#d8b890') + Ci(24, -24, 5, '#d8b890') + E(0, -18, 16, 14, '#d8b890') + Ci(-7, -26, 3, '#2f3437') + Ci(7, -26, 3, '#2f3437') + St('M-6,-10 Q0,-6 6,-10', '#5a3a24', 2) + arm([(-20, 10), (-36, -10), (-40, -40)], '#8a5a35', '#d8b890', 9) + arm([(20, 10), (30, 30), (24, 46)], '#8a5a35', '#d8b890', 9), f'translate({x},{y}) scale({s})')
def panda(x, y, s=1):
    return G(E(0, 30, 40, 36, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + E(-26, 54, 14, 12, '#2f3437') + E(26, 54, 14, 12, '#2f3437') + E(-34, 16, 12, 22, '#2f3437') + E(34, 16, 12, 22, '#2f3437') + Ci(0, -24, 32, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + Ci(-24, -48, 11, '#2f3437') + Ci(24, -48, 11, '#2f3437') + E(-12, -24, 8, 11, '#2f3437', 'transform="rotate(-25 -12 -24)"') + E(12, -24, 8, 11, '#2f3437', 'transform="rotate(25 12 -24)"') + Ci(-11, -25, 2.5, '#ffffff') + Ci(11, -25, 2.5, '#ffffff') + E(0, -10, 5, 4, '#2f3437') + St('M-5,-4 Q0,0 5,-4', '#2f3437', 2), f'translate({x},{y}) scale({s})')
def bear(x, base, s=1, col='#7a4a2a', snout='#c8a080'):
    return quad(x, base, s, col, None, 30, 60, 36, (54, -70), 24, snout, 'round', shade(col, -.1), 'short', col)
def giraffe(x, base, s=1):
    k = s
    g = G(R(-40, -70, 12, 70, '#e0b050', 4) + R(24, -70, 12, 70, '#e0b050', 4) + E(0, -84, 48, 22, '#f0c060') + R(-30, -70, 12, 70, '#f0c060', 4) + R(34, -70, 12, 70, '#f0c060', 4) + Pa('M30,-96 L56,-170 L72,-166 L48,-84 Z', '#f0c060') + E(70, -172, 18, 11, '#f0c060', 'transform="rotate(20 70 -172)"') + R(56, -192, 4, 14, '#a8703e') + R(64, -194, 4, 14, '#a8703e') + Ci(58, -192, 3, '#a8703e') + Ci(66, -194, 3, '#a8703e') + Ci(72, -176, 2.5, '#2f3437') + ''.join(R(dx, dy, 10, 9, '#a8602a', 3) for dx, dy in [(-30, -96), (-12, -98), (6, -92), (-22, -82), (2, -80), (20, -84), (40, -110), (46, -130), (52, -150), (36, -96)]) + St('M-48,-90 q-8,10 -6,24', '#e0b050', 3), f'translate({x},{base}) scale({k})')
    return g
def zebra(x, base, s=1):
    k = s
    g = quad(x, base, s, '#ffffff', None, 44, 54, 26, (60, -96), 16, '#2f3437', 'point', '#ffffff', 'tuft', '#ffffff', True, True, None, '#2f3437')
    g += G(''.join(Pa(f'M{-44+j*12},-96 Q{-40+j*12},-80 {-44+j*12},-64 L{-38+j*12},-64 Q{-34+j*12},-80 {-38+j*12},-96 Z', '#2f3437') for j in range(8)) + ''.join(L(40 + j * 5, -84 - j * 4, 56 + j * 4, -78 - j * 4, '#2f3437', 3) for j in range(3)) + Pa('M44,-92 L56,-110 L62,-104 L50,-88 Z', '#2f3437'), f'translate({x},{base}) scale({k})')
    return g
def kangaroo(x, base, s=1):
    return G(St('M-30,-30 Q-70,-10 -80,0', '#c8885a', 12) + E(0, -50, 30, 44, '#c8885a') + E(6, -40, 16, 26, '#e8c8a0') + E(-6, -6, 30, 10, '#b8784a') + E(30, -6, 20, 6, '#b8784a') + Ci(14, -100, 16, '#c8885a') + E(28, -96, 12, 8, '#c8885a') + E(6, -122, 5, 14, '#b8784a') + E(16, -124, 5, 14, '#b8784a') + Ci(18, -104, 2.5, '#2f3437') + Ci(38, -96, 2.5, '#2f3437') + arm([(18, -70), (30, -60), (34, -52)], '#c8885a', '#c8885a', 7), f'translate({x},{base}) scale({s})')
def wolf(x, base, s=1):
    return quad(x, base, s, '#8a9196', '#d9dcde', 40, 52, 22, (54, -74), 16, '#a7adb1', 'point', '#6a7076', 'bushy', '#8a9196')
def fox(x, base, s=1):
    return quad(x, base, s, '#e07a2a', '#ffffff', 30, 46, 20, (46, -58), 15, '#ffffff', 'point', '#2f3437', 'bushy', '#e07a2a') + G(Ci(-70, -40, 8, '#ffffff'), f'translate({x},{base}) scale({s})')
def deer(x, base, s=1):
    k = s
    return quad(x, base, s, '#b8783a', '#e8c8a0', 50, 46, 22, (54, -100), 14, '#c8885a', 'point', '#a8683a', 'short', '#ffffff', True, True) + G(St('M48,-112 L40,-140 M44,-128 L32,-134 M60,-112 L68,-140 M64,-128 L76,-134', '#8a5a35', 4) + ''.join(Ci(dx, dy, 3, '#f6efe0') for dx, dy in [(-20, -86), (-4, -90), (12, -84), (-10, -78)]), f'translate({x},{base}) scale({k})')
def camel(x, base, s=1):
    k = s
    return G(R(-38, -60, 12, 60, '#c8a060', 4) + R(30, -60, 12, 60, '#c8a060', 4) + E(0, -70, 50, 24, '#d8b070') + Ci(-14, -90, 20, '#d8b070') + Ci(16, -90, 20, '#d8b070') + R(-28, -60, 12, 60, '#d8b070', 4) + R(20, -60, 12, 60, '#d8b070', 4) + Pa('M40,-80 Q60,-80 64,-110 L80,-110 Q78,-70 50,-60 Z', '#d8b070') + E(80, -112, 16, 10, '#d8b070') + Ci(80, -116, 2.5, '#2f3437') + St('M-50,-74 q-8,6 -6,20', '#c8a060', 3), f'translate({x},{base}) scale({k})')
def hippo(x, base, s=1):
    k = s
    return G(R(-40, -30, 18, 30, '#8a7a8a', 6) + R(20, -30, 18, 30, '#8a7a8a', 6) + E(0, -50, 56, 32, '#9a8a9a') + R(-30, -30, 18, 30, '#9a8a9a', 6) + R(30, -30, 18, 30, '#9a8a9a', 6) + E(60, -56, 26, 22, '#9a8a9a') + E(76, -48, 18, 16, '#a898a8') + Ci(54, -76, 6, '#8a7a8a') + Ci(66, -78, 6, '#8a7a8a') + Ci(62, -66, 3, '#2f3437') + Ci(84, -52, 2, '#5a4a5a') + Ci(90, -48, 2, '#5a4a5a'), f'translate({x},{base}) scale({k})')
def rhino(x, base, s=1):
    k = s
    return G(R(-40, -30, 18, 30, '#8a9196', 6) + R(24, -30, 18, 30, '#8a9196', 6) + E(0, -52, 56, 32, '#9aa1a6') + R(-30, -30, 18, 30, '#9aa1a6', 6) + R(32, -30, 18, 30, '#9aa1a6', 6) + Pa('M40,-70 Q70,-80 90,-56 Q86,-36 60,-40 Z', '#9aa1a6') + Pa('M80,-66 L92,-96 L94,-62 Z', '#e6dcc8') + Pa('M68,-72 L72,-86 L78,-70 Z', '#e6dcc8') + Pa('M46,-76 L50,-92 L56,-74 Z', '#8a9196') + Ci(70, -60, 2.5, '#2f3437'), f'translate({x},{base}) scale({k})')
def gorilla(x, y, s=1, col='#3a3a3a', face_c='#5a5a5a'):
    return G(E(0, 20, 40, 44, col) + Ci(-26, -36, 9, face_c) + Ci(26, -36, 9, face_c) + Ci(0, -36, 26, col) + E(0, -30, 16, 14, face_c) + Ci(-7, -38, 3, '#ffffff') + Ci(7, -38, 3, '#ffffff') + Ci(-7, -38, 1.5, '#2f3437') + Ci(7, -38, 1.5, '#2f3437') + E(0, -24, 8, 4, '#2a2a2a') + E(0, 24, 22, 26, face_c) + arm([(-34, 0), (-50, 40), (-46, 66)], col, shade(col, -.2), 18) + arm([(34, 0), (50, 40), (46, 66)], col, shade(col, -.2), 18), f'translate({x},{y}) scale({s})')
def squirrel(x, base, s=1):
    return G(Pa('M-20,-10 Q-60,-20 -50,-70 Q-40,-90 -20,-80 Q-36,-50 -10,-30 Z', '#c8783a') + E(0, -24, 20, 24, '#c8783a') + E(4, -18, 10, 14, '#f0d8b0') + Ci(10, -54, 14, '#c8783a') + Pa('M2,-66 L4,-78 L10,-66 Z', '#c8783a') + Ci(16, -56, 2.5, '#2f3437') + E(18, -30, 7, 6, '#8a5a35') + E(-6, 0, 12, 4, '#a8683a'), f'translate({x},{base}) scale({s})')
def mouse_(x, base, s=1, col='#a7adb1'):
    return G(St('M-24,-10 Q-50,-10 -60,-24', '#ef8fa4', 3) + E(0, -14, 26, 16, col) + Ci(18, -28, 10, col) + Ci(14, -38, 8, '#ef8fa4') + Ci(26, -18, 4, '#ef8fa4') + Ci(22, -24, 2, '#2f3437') + L(26, -18, 40, -22, '#5d6469', 1) + L(26, -18, 40, -14, '#5d6469', 1), f'translate({x},{base}) scale({s})')
def bat_(x, y, s=1):
    return G(Pa('M0,0 Q-20,-30 -60,-20 Q-50,-10 -52,4 Q-40,-4 -34,8 Q-24,0 -16,10 Q-8,4 0,10 Q8,4 16,10 Q24,0 34,8 Q40,-4 52,4 Q50,-10 60,-20 Q20,-30 0,0 Z', '#3a3040') + E(0, 0, 10, 14, '#4a3a50') + Pa('M-8,-10 L-6,-22 L0,-12 L6,-22 L8,-10 Z', '#4a3a50') + Ci(-4, -6, 2, '#f3c234') + Ci(4, -6, 2, '#f3c234'), f'translate({x},{y}) scale({s})')
def koala(x, y, s=1):
    return G(E(0, 30, 30, 34, '#9aa1a6') + Ci(0, -16, 28, '#9aa1a6') + Ci(-28, -30, 16, '#9aa1a6') + Ci(28, -30, 16, '#9aa1a6') + Ci(-28, -30, 9, '#e6e2dc') + Ci(28, -30, 9, '#e6e2dc') + E(0, -8, 9, 12, '#2f3437') + Ci(-12, -20, 3, '#2f3437') + Ci(12, -20, 3, '#2f3437') + E(0, 30, 16, 20, '#e6e2dc'), f'translate({x},{y}) scale({s})')
def hedgehog(x, base, s=1):
    return G(Pa('M-50,-10 ' + ' '.join(f'L{-50+j*8},{-20-12*math.sin(j*math.pi/12)-(j%2)*10}' for j in range(13)) + ' L46,-10 Z', '#6a4a3a') + E(30, -14, 22, 14, '#d8b890') + Ci(52, -14, 4, '#2f3437') + Ci(36, -20, 2.5, '#2f3437') + E(0, -8, 40, 10, '#a8805a'), f'translate({x},{base}) scale({s})')
def raccoon(x, base, s=1):
    k = s
    return quad(x, base, s, '#8a9196', '#c4cbd0', 24, 44, 22, (44, -56), 16, '#e6ecef', 'point', '#5d6469', 'bushy', '#8a9196') + G(R(28, -62, 32, 10, '#2f3437', 5) + Ci(48, -58, 2.5, '#ffffff') + ''.join(R(-80 + j * 10, -48, 6, 22, '#2f3437', 2, 'transform="rotate(-20 -70 -40)"') for j in range(3)), f'translate({x},{base}) scale({k})')
def otter(x, y, s=1):
    return G(E(0, 0, 50, 18, '#8a5a35') + E(4, 6, 36, 10, '#c8a080') + Ci(46, -8, 16, '#8a5a35') + E(54, -2, 10, 7, '#d8b890') + Ci(50, -14, 2.5, '#2f3437') + Ci(40, -20, 4, '#7a4a2a') + St('M-48,0 Q-70,0 -80,10', '#8a5a35', 8) + E(20, -14, 8, 6, '#8a5a35'), f'translate({x},{y}) scale({s})')
def leopard(x, base, s=1, col='#e8b040', spots='#5a3a1a'):
    k = s
    return quad(x, base, s, col, '#fbe8c0', 40, 58, 24, (56, -72), 17, '#fbe8c0', 'round', shade(col, -.15), 'thin', col) + G(''.join(Ci(dx, dy, 4, 'none', f'stroke="{spots}" stroke-width="2.5"') for dx, dy in [(-40, -70), (-24, -78), (-8, -70), (8, -78), (24, -70), (-30, -58), (-14, -56), (2, -60), (18, -58), (34, -76)]), f'translate({x},{base}) scale({k})')
def cheetah(x, base, s=1):
    k = s
    return quad(x, base, s, '#f0c060', '#fbe8c0', 46, 58, 20, (58, -76), 15, '#fbe8c0', 'round', '#d8a040', 'thin', '#f0c060') + G(''.join(Ci(dx, dy, 3, '#2f3437') for dx, dy in [(-40, -72), (-28, -78), (-14, -72), (0, -80), (14, -72), (28, -78), (-34, -62), (-20, -64), (-6, -60), (8, -64), (22, -62)]) + St('M62,-72 Q60,-60 66,-58', '#2f3437', 2), f'translate({x},{base}) scale({k})')
def polar(x, base, s=1):
    return bear(x, base, s, '#f6f4ee', '#e6e2dc') + G(Ci(78, -66, 3, '#2f3437'), f'translate({x},{base}) scale({s})')
def beaver(x, base, s=1):
    return G(E(-50, -6, 28, 10, '#5a4a3a', 'transform="rotate(-10 -50 -6)"') + ''.join(L(-70 + j * 8, -12, -64 + j * 8, 2, '#3a2a20', 1) for j in range(5)) + E(0, -24, 34, 24, '#8a5a35') + Ci(32, -36, 16, '#8a5a35') + Ci(26, -50, 5, '#7a4a2a') + E(44, -30, 8, 6, '#a8703e') + R(42, -26, 8, 8, '#ffffff', 1) + Ci(36, -40, 2.5, '#2f3437'), f'translate({x},{base}) scale({s})')
def moose(x, base, s=1):
    k = s
    return quad(x, base, s, '#6a4a2a', None, 54, 54, 26, (60, -96), 18, '#7a5a3a', 'point', '#5a3a1a', 'short', '#6a4a2a', True, True) + G(Pa('M40,-112 Q20,-130 22,-150 L30,-140 L32,-154 L40,-142 L46,-150 L50,-118 Z', '#c8a878') + Pa('M70,-112 Q90,-130 90,-150 L82,-140 L80,-154 L72,-142 L66,-150 L62,-118 Z', '#c8a878') + E(80, -76, 6, 12, '#5a3a1a'), f'translate({x},{base}) scale({k})')
def badger(x, base, s=1):
    k = s
    return quad(x, base, s, '#5d6469', '#3a4048', 18, 52, 22, (52, -44), 16, '#ffffff', 'round', '#3a4048', 'short', '#5d6469') + G(Pa('M40,-60 L70,-46 L68,-40 L40,-50 Z', '#ffffff') + R(46, -56, 26, 5, '#2f3437', 2), f'translate({x},{base}) scale({k})')
def mole(x, base, s=1):
    return G(Pa('M-90,0 Q0,-60 90,0 Z', '#8a6a4a') + E(0, -20, 40, 26, '#3a3a3a') + E(40, -18, 12, 8, '#ef8fa4') + Ci(26, -28, 2, '#ffffff') + E(26, -4, 14, 8, '#ef8fa4') + E(-20, -4, 14, 8, '#ef8fa4') + ''.join(L(20 + j * 5, -4, 22 + j * 5, 6, '#ffffff', 1.5) for j in range(4)), f'translate({x},{base}) scale({s})')
def sloth(x, y, s=1):
    return G(R(-100, -50, 200, 10, '#8a5a35', 5) + E(0, 0, 30, 36, '#a8906a') + Ci(0, -40, 20, '#a8906a') + E(0, -38, 15, 12, '#e6dcc0') + E(-7, -40, 6, 4, '#5a4a3a', 'transform="rotate(20 -7 -40)"') + E(7, -40, 6, 4, '#5a4a3a', 'transform="rotate(-20 7 -40)"') + Ci(-7, -40, 1.5, '#ffffff') + Ci(7, -40, 1.5, '#ffffff') + St('M-4,-32 Q0,-28 4,-32', '#5a4a3a', 1.5) + arm([(-20, -16), (-30, -40), (-26, -46)], '#a8906a', '#5a4a3a', 9) + arm([(20, -16), (30, -40), (26, -46)], '#a8906a', '#5a4a3a', 9) + arm([(-14, 26), (-26, -10), (-20, -46)], '#a8906a', '#5a4a3a', 9), f'translate({x},{y}) scale({s})')
def red_panda(x, base, s=1):
    k = s
    return quad(x, base, s, '#c8502a', '#3a2a20', 26, 46, 22, (46, -62), 18, '#ffffff', 'point', '#ffffff', 'bushy', '#c8502a', legcol='#3a2a20') + G(''.join(R(-82 + j * 10, -56, 6, 30, '#f0d8b8', 2, 'transform="rotate(-30 -70 -40)"') for j in range(3)) + E(40, -66, 4, 6, '#ffffff') + E(56, -66, 4, 6, '#ffffff'), f'translate({x},{base}) scale({k})')
def mammoth(x, base, s=1):
    k = s
    return G(R(-46, -60, 24, 60, '#6a4a3a', 8) + R(28, -60, 24, 60, '#6a4a3a', 8) + Pa('M-70,-60 Q-70,-140 0,-140 Q60,-140 70,-90 Q70,-60 50,-50 L-60,-40 Z', '#7a5a42') + R(-36, -56, 24, 56, '#7a5a42', 8) + R(18, -56, 24, 56, '#7a5a42', 8) + ''.join(L(-60 + j * 12, -60, -64 + j * 12, -30, '#6a4a3a', 3) for j in range(10)) + Ci(54, -100, 34, '#7a5a42') + St('M76,-90 Q100,-40 76,-10', '#7a5a42', 16) + St('M66,-80 Q110,-60 100,-20', '#f6efe0', 8) + Ci(60, -112, 3.5, '#2f3437'), f'translate({x},{base}) scale({k})')
def trex(x, base, s=1, col='#5a8a3a'):
    k = s
    return G(Pa('M-90,-60 Q-40,-80 0,-90 L0,-60 Q-40,-60 -90,-60 Z', col) + E(0, -84, 40, 30, col) + R(-14, -64, 16, 64, shade(col, -.1), 6) + R(10, -64, 18, 64, col, 6) + R(-20, -6, 24, 8, shade(col, -.2), 3) + R(6, -6, 28, 8, shade(col, -.2), 3) + Pa('M20,-110 L50,-150 L100,-140 L104,-120 L70,-116 L96,-104 L60,-96 Z', col) + ''.join(Pa(f'M{70+j*8},-116 l4,8 l4,-8 Z', '#ffffff') for j in range(3)) + Ci(80, -136, 4, '#ffffff') + Ci(81, -136, 2, '#2f3437') + arm([(30, -90), (44, -80), (48, -72)], col, col, 6), f'translate({x},{base}) scale({k})')
def dino_long(x, base, s=1, col='#7aa050'):
    k = s
    return G(R(-40, -50, 16, 50, shade(col, -.1), 6) + R(24, -50, 16, 50, shade(col, -.1), 6) + E(0, -60, 50, 30, col) + R(-28, -50, 16, 50, col, 6) + R(36, -50, 16, 50, col, 6) + St('M-46,-60 Q-90,-50 -100,-20', col, 14) + St('M36,-76 Q70,-110 76,-160', col, 16) + E(84, -164, 18, 10, col) + Ci(88, -168, 2.5, '#2f3437') + ''.join(Ci(-20 + j * 14, -70, 4, shade(col, .15)) for j in range(4)), f'translate({x},{base}) scale({k})')
def caveman(x, ground, s=1):
    return pose((x, ground - 150 * s), (x, ground - 126 * s), (x, ground - 74 * s), arms=[[(x + 10 * s, ground - 122 * s), (x + 26 * s, ground - 100 * s), (x + 30 * s, ground - 130 * s)]], legs=[[(x - 6 * s, ground - 74 * s), (x - 10 * s, ground)], [(x + 6 * s, ground - 74 * s), (x + 10 * s, ground)]], back_arm=[[(x - 10 * s, ground - 122 * s), (x - 22 * s, ground - 96 * s)]], shirt='#a8703e', pants=SK, hair='#3a2a20', style='long', hr=16 * s, tw=32 * s, shoes=SK) + Pa(f'M{x-18*s},{ground-128*s} L{x+18*s},{ground-128*s} L{x+20*s},{ground-70*s} L{x+8*s},{ground-78*s} L{x-4*s},{ground-68*s} L{x-20*s},{ground-74*s} Z', '#a8703e') + G(R(-4, -50, 8, 50, '#8a5a35', 3) + E(0, -54, 9, 12, '#8a5a35'), f'translate({x+30*s},{ground-110*s}) rotate(20)')
def sabre(x, base, s=1):
    k = s
    return quad(x, base, s, '#c8a060', '#e8d8b0', 40, 58, 28, (56, -74), 20, '#e8d8b0', 'round', '#a8803a', 'short', '#c8a060') + G(Pa('M62,-64 L64,-36 L68,-64 Z', '#ffffff') + Pa('M70,-64 L72,-38 L76,-64 Z', '#ffffff'), f'translate({x},{base}) scale({k})')

# ================= 自然史 =================
S_('nature', R(0, 0, 200, 200, SKY) + Pa('M0,120 L60,70 L110,110 L160,60 L200,100 L200,200 L0,200 Z', '#7a9a8a') + R(0, 140, 200, 60, '#9ac070') + tree(40, 150, .8) + E(130, 170, 40, 10, '#5aa1d4') + flower(80, 180, 1.4) + flying_bird(150, 50, .4) + sun(40, 40, 14), False)
S_('wildlife', savanna() + giraffe(60, 186, .6) + zebra(130, 186, .55) + flying_bird(160, 40, .4) + flying_bird(130, 30, .3), False)
S_('dinosaur', R(0, 0, 200, 200, '#e6f0d8') + R(0, 170, 200, 30, '#b8a070') + dino_long(90, 180, .9) + volcano_(180, 120, .3, False), False)
S_('extinct', R(0, 0, 200, 200, '#e8e0d0') + G(dino_long(0, 0, .8, '#a7adb1'), 'translate(90,160)') + Ci(100, 100, 80, 'none', 'stroke="#e2463b" stroke-width="10"') + L(44, 44, 156, 156, '#e2463b', 10), False)
S_('footprint', R(0, 0, 200, 200, '#d8c8a0') + ''.join(G(Pa('M0,20 Q-20,10 -16,-10 L-26,-30 L-10,-20 L0,-40 L10,-20 L26,-30 L16,-10 Q20,10 0,20 Z', '#a89070'), f'translate({x},{y}) rotate({r_}) scale(.9)') for x, y, r_ in [(50, 160, -10), (100, 110, 10), (150, 60, -10)]), False)
S_('claw', G(Pa('M-60,40 Q-60,-20 0,-30 Q60,-20 60,40 Z', '#8a6a4a') + ''.join(Pa(f'M{dx},-20 Q{dx+6},-60 {dx+20},-70 Q{dx+12},-50 {dx+14},-20 Z', '#e6dcc8') for dx in (-44, -14, 16)), 'translate(100,120)'))
S_('tail', G(quad(0, 0, 1, '#e07a2a', '#ffffff', 30, 46, 20, (46, -58), 15, '#ffffff', 'point', '#2f3437', 'bushy', '#e07a2a'), 'translate(150,180) scale(-1.2,1.2)') + Ci(56, 120, 40, 'none', 'stroke="#e2463b" stroke-width="3" stroke-dasharray="6 4"'))
S_('prehistoric', R(0, 0, 200, 200, '#f0d8b0') + volcano_(150, 150, .5) + R(0, 150, 200, 50, '#a89070') + trex(70, 170, .7) + G(Pa('M-30,0 Q0,-10 30,0 L20,6 L-20,6 Z', '#5a5a5a'), 'translate(160,40)') + St('M140,40 Q160,30 180,40', '#5a5a5a', 0), False)
S_('mammoth', snow_land(160) + mammoth(90, 180, .9), False)
S_('t-rex', R(0, 0, 200, 200, '#e6f0d8') + R(0, 176, 200, 24, '#a89070') + trex(80, 186, 1.0), False)
S_('ice-age', R(0, 0, 200, 200, '#cfe2f0') + Pa('M0,100 L50,60 L100,90 L160,40 L200,80 L200,200 L0,200 Z', '#ffffff') + mammoth(80, 190, .55) + ''.join(Ci((k * 41) % 200, (k * 29) % 100, 3, '#ffffff') for k in range(12)), False)
S_('caveman', R(0, 0, 200, 200, '#d8c0a0') + cave_(100, 200, 1.1) + caveman(100, 196, .95) + campfire(160, 190, .4), False)
S_('ancestor', R(0, 0, 200, 200, '#f6efe0') + ''.join(G(R(-26, -32, 52, 64, '#c8a070', 4) + R(-20, -26, 40, 52, '#e6dcc8') + Ci(0, -6, 10, SK) + Pa('M-14,22 Q0,6 14,22 Z', c) + Pa('M-10,-10 Q0,-22 10,-10 Z', P['grey']), f'translate({50+k*50},{60 if k != 1 else 50})') for k, c in enumerate(['#5d6469', '#7a4fa0', '#3c7fc1'])) + St('M50,96 L100,140 L150,96 M100,86 L100,140', '#8a5a35', 2) + Ci(100, 160, 18, SK) + Pa('M86,196 Q100,170 114,196 Z', '#5ba644'), False)
S_('ape', R(0, 0, 200, 200, '#e6f0d8') + gorilla(100, 110, .9, '#6a4a32', '#d8b890'), False)
S_('sabre-toothed-tiger', snow_land(170) + sabre(90, 186, 1.0), False)
S_('meteorite', R(0, 0, 200, 200, '#f6efe0') + rock_(100, 120, 1.1, '#5d5850') + ''.join(Ci(70 + k * 15, 110 + (k % 2) * 10, 3, '#8a7a6a') for k in range(5)) + G(Pa('M0,-6 L-60,-2 L-60,2 L0,6 Z', '#f08a24', 'opacity=".6"'), 'translate(60,70) rotate(40)') + E(100, 170, 70, 10, '#c8b8a0'))

# ================= 哺乳 1 =================
S_('lion', savanna() + lion(90, 186, .95), False)
S_('tiger', forest_bg() + tiger(90, 186, .95), False)
S_('elephant', savanna() + elephant(90, 190, .95), False)
S_('monkey', R(0, 0, 200, 200, '#dff1d8') + R(0, 30, 200, 10, '#8a5a35', 5) + monkey(100, 100, 1.4), False)
S_('panda', R(0, 0, 200, 200, '#e6f4e0') + ''.join(R(10 + k * 30, 0, 8, 200, '#7ab050', 3) for k in range(0)) + ''.join(G(R(-4, -160, 8, 160, '#8ac060', 3) + leaf(6, -120, 20, 6, -30, '#5aaa3a'), f'translate({20+k*160},200)') for k in range(2)) + panda(100, 110, 1.2), False)
S_('bear', forest_bg() + bear(90, 186, 1.0), False)
S_('giraffe', savanna(170) + giraffe(70, 196, .9) + tree(170, 170, .5), False)
S_('zebra', savanna() + zebra(90, 186, 1.0), False)
S_('kangaroo', R(0, 0, 200, 200, '#f6d8a8') + R(0, 170, 200, 30, '#c87a3a') + kangaroo(100, 180, 1.1), False)
S_('wolf', snow_land() + wolf(90, 180, 1.1) + moon(160, 40, 14), False)
S_('fox', forest_bg(160) + fox(100, 186, 1.3), False)
S_('deer', forest_bg(160) + deer(90, 192, .95), False)
S_('camel', R(0, 0, 200, 200, '#fbe0a0') + R(0, 160, 200, 40, '#f0c870') + camel(80, 186, .95), False)
S_('hippo', R(0, 0, 200, 200, SKY) + R(0, 130, 200, 70, '#5aa1d4') + hippo(80, 170, 1.0) + R(0, 150, 200, 50, '#5aa1d4', 0, 'opacity=".7"'), False)
S_('rhino', savanna() + rhino(80, 186, 1.0), False)
S_('gorilla', R(0, 0, 200, 200, '#dff1d8') + gorilla(100, 120, 1.1), False)

# ================= 哺乳 2 =================
S_('squirrel', forest_bg(170) + squirrel(110, 186, 1.6) + G(Ci(0, 0, 8, '#a8703e') + E(0, -8, 9, 4, '#6a4a2a'), 'translate(140,152)'), False)
S_('mouse-mammals2', mouse_(110, 160, 2.0) + G(Pa('M0,0 L30,-10 L30,10 Z', '#f3c234') + Ci(16, -2, 3, '#e0b030'), 'translate(30,150)'))
S_('bat-mammals2', R(0, 0, 200, 200, '#24304f') + moon(150, 50, 24) + bat_(100, 110, 1.4), False)
S_('koala', R(0, 0, 200, 200, '#e6f0d8') + R(140, 0, 24, 200, '#a8906a') + koala(110, 100, 1.3) + leaf(40, 60, 24, 8, -30, '#7aa070'), False)
S_('hedgehog', R(0, 0, 200, 200, '#e6f0d8') + R(0, 150, 200, 50, '#9ac070') + hedgehog(100, 160, 1.4) + apple(160, 150, .4), False)
S_('raccoon', forest_bg(170) + raccoon(84, 190, 1.15), False)
S_('otter', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#5aa1d4') + otter(100, 120, 1.2) + St('M20,150 q20,-6 40,0 t40,0 t40,0 t40,0', '#9fd0ec', 3), False)
S_('leopard', savanna() + leopard(90, 186, 1.0), False)
S_('cheetah', savanna() + cheetah(90, 186, 1.0) + ''.join(L(10, 110 + k * 14, 30, 110 + k * 14, '#ffffff', 3) for k in range(3)), False)
S_('polar-bear', snow_land(150) + polar(90, 180, 1.0), False)
S_('beaver', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#5aa1d4') + ''.join(R(120 + k * 6, 100 + k * 4, 70, 10, '#8a5a35', 5, 'transform="rotate(-10)"') for k in range(4)) + beaver(80, 160, 1.4), False)
S_('moose', forest_bg(170) + moose(90, 196, .8), False)
S_('badger', R(0, 0, 200, 200, '#e6f0d8') + R(0, 150, 200, 50, '#8a6a4a') + badger(80, 170, 1.2), False)
S_('mole', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#8a6a4a') + mole(100, 150, 1.2) + ''.join(Ci((k * 37) % 200, 170 + (k * 13) % 30, 3, '#6a4a2a') for k in range(10)), False)
S_('sloth', R(0, 0, 200, 200, '#dff1d8') + sloth(100, 110, 1.3), False)
S_('red-panda', R(0, 0, 200, 200, '#e6f0d8') + R(0, 150, 200, 14, '#8a5a35', 7) + red_panda(90, 152, 1.3), False)

dump()
