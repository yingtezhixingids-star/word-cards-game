from kit6 import *

def branch_bg(sky='#dff1fb'):
    return R(0, 0, 200, 200, sky) + St('M0,150 Q100,140 200,156', '#8a5a35', 8) + leaf(30, 146, 14, 6, -40, '#5aaa3a') + leaf(170, 150, 14, 6, -140, '#5aaa3a')
def perch(x, y, s=1, **kw):
    return bird(x, y, s, **kw)
def owl_(x, y, s=1):
    return G(E(0, 10, 34, 42, '#8a6a4a') + E(0, 20, 22, 28, '#d8c0a0') + ''.join(St(f'M{-12+j*8},{14+(j%2)*10} q4,4 8,0', '#a8805a', 2) for j in range(4)) + Ci(-14, -18, 13, '#f6efe0') + Ci(14, -18, 13, '#f6efe0') + Ci(-14, -18, 7, '#f3c234') + Ci(14, -18, 7, '#f3c234') + Ci(-14, -18, 3.5, '#2f3437') + Ci(14, -18, 3.5, '#2f3437') + Pa('M-4,-8 L4,-8 L0,2 Z', '#e0a040') + Pa('M-30,-30 L-26,-46 L-14,-32 Z', '#8a6a4a') + Pa('M30,-30 L26,-46 L14,-32 Z', '#8a6a4a') + L(-8, 50, -8, 56, '#e0a040', 3) + L(8, 50, 8, 56, '#e0a040', 3), f'translate({x},{y}) scale({s})')
def penguin_(x, y, s=1):
    return G(E(0, 0, 28, 44, '#2f3437') + E(0, 8, 20, 34, '#ffffff') + Ci(0, -36, 18, '#2f3437') + E(0, -30, 11, 9, '#ffffff') + Ci(-5, -38, 2.5, '#2f3437') + Ci(5, -38, 2.5, '#2f3437') + Pa('M-5,-32 L5,-32 L0,-24 Z', '#f08a24') + E(-26, 4, 8, 22, '#2f3437', 'transform="rotate(20 -26 4)"') + E(26, 4, 8, 22, '#2f3437', 'transform="rotate(-20 26 4)"') + E(-10, 44, 10, 4, '#f08a24') + E(10, 44, 10, 4, '#f08a24') + E(0, -22, 12, 6, '#f3c234', 'opacity=".6"'), f'translate({x},{y}) scale({s})')
def peacock_(x, y, s=1):
    g = ''.join(E(70 * math.cos(a), 70 * math.sin(a), 18, 26, '#2a8a6a', f'transform="rotate({math.degrees(a)+90} {70*math.cos(a)} {70*math.sin(a)})"') + Ci(70 * math.cos(a), 70 * math.sin(a), 9, '#3c7fc1') + Ci(70 * math.cos(a), 70 * math.sin(a), 4, '#1f2a5a') for a in [math.radians(d) for d in range(-170, -9, 20)])
    g += E(0, 0, 18, 30, '#1f5aa8') + Ci(0, -36, 10, '#1f5aa8') + Pa('M8,-38 l10,3 l-10,3 Z', '#5d6469') + Ci(3, -38, 2, '#2f3437') + ''.join(L(-4 + j * 4, -46, -6 + j * 6, -58, '#1f5aa8', 1.5) + Ci(-6 + j * 6, -58, 2.5, '#1f5aa8') for j in range(3)) + L(-4, 28, -4, 50, '#8a9196', 2) + L(4, 28, 4, 50, '#8a9196', 2)
    return G(g, f'translate({x},{y}) scale({s})')
def eagle_(x, y, s=1):
    return G(Pa('M0,0 Q-50,-40 -100,-30 Q-70,-10 -60,10 Q-40,0 -20,14 Z', '#6a4a2a') + Pa('M0,0 Q50,-40 100,-30 Q70,-10 60,10 Q40,0 20,14 Z', '#6a4a2a') + E(0, 10, 18, 26, '#6a4a2a') + Pa('M-12,32 L0,52 L12,32 Z', '#ffffff') + Ci(0, -16, 14, '#ffffff') + Pa('M8,-18 L22,-14 L14,-6 L8,-10 Z', '#f3c234') + Ci(4, -20, 2.5, '#2f3437'), f'translate({x},{y}) scale({s})')
def swan_(x, y, s=1, col='#ffffff'):
    return G(Pa('M-50,0 Q-40,30 20,30 Q50,30 50,0 Q30,-10 10,0 Q-20,-30 -50,0 Z', col, 'stroke="#d9dcde" stroke-width="1.5"') + St('M30,4 Q40,-30 26,-50 Q20,-60 30,-64', col, 10) + Ci(32, -64, 8, col) + Pa('M38,-66 L52,-60 L38,-58 Z', '#f08a24') + Ci(32, -66, 2, '#2f3437'), f'translate({x},{y}) scale({s})')
def flamingo_(x, y, s=1):
    return G(L(0, 20, 0, 90, '#ef8fa4', 3) + St('M0,50 L14,40 L4,30', '#ef8fa4', 3) + E(0, 0, 30, 20, '#ef8fa4') + E(-6, -2, 20, 12, '#f6b8c4') + St('M24,-6 Q40,-40 20,-60 Q10,-74 24,-80', '#ef8fa4', 7) + Ci(26, -80, 7, '#ef8fa4') + Pa('M30,-82 L42,-76 L36,-66 Z', '#2f3437') + Ci(26, -82, 1.5, '#2f3437'), f'translate({x},{y}) scale({s})')
def hummer(x, y, s=1):
    return G(E(-10, -14, 24, 6, '#9fd0ec', 'opacity=".7" transform="rotate(-40 -10 -14)"') + E(0, 0, 16, 9, '#2fa59b') + E(2, 4, 10, 5, '#ffffff') + Ci(14, -4, 7, '#2fa59b') + Pa('M18,-5 L44,-2 L18,-2 Z', '#2f3437') + Ci(16, -6, 1.5, '#2f3437') + Pa('M-14,0 L-28,6 L-26,-4 Z', '#1f7a6a') + E(6, 2, 4, 3, '#e2463b'), f'translate({x},{y}) scale({s})')
def pelican_(x, y, s=1):
    return G(E(0, 0, 34, 22, '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"') + E(-6, -4, 22, 12, '#e6ecef') + St('M26,-4 Q34,-30 30,-44', '#ffffff', 10) + Ci(32, -46, 10, '#ffffff') + Pa('M38,-48 L90,-40 L88,-36 Q60,-20 40,-36 Z', '#f3c234') + Ci(34, -48, 2, '#2f3437') + L(-6, 20, -6, 40, '#f08a24', 3) + L(6, 20, 6, 40, '#f08a24', 3), f'translate({x},{y}) scale({s})')
def ostrich_(x, base, s=1):
    return G(L(-6, -70, -14, 0, '#d8a080', 5) + L(8, -70, 14, 0, '#d8a080', 5) + E(0, -90, 40, 28, '#2f3437') + Pa('M-40,-96 Q-60,-110 -50,-80 Z', '#ffffff') + St('M26,-104 Q34,-150 30,-170', '#e8b8a0', 7) + Ci(32, -172, 9, '#e8b8a0') + Pa('M38,-174 L52,-170 L38,-166 Z', '#e0a040') + Ci(34, -174, 2, '#2f3437'), f'translate({x},{base}) scale({s})')
def crane_bird(x, y, s=1):
    return G(L(-4, 20, -6, 90, '#2f3437', 3) + L(4, 20, 6, 90, '#2f3437', 3) + E(0, 0, 30, 18, '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"') + Pa('M-28,-2 Q-46,10 -44,24 Q-30,12 -20,10 Z', '#2f3437') + St('M24,-6 Q34,-40 28,-70', '#2f3437', 6) + Ci(28, -74, 7, '#ffffff') + Ci(28, -80, 4, '#e2463b') + Pa('M34,-74 L54,-70 L34,-68 Z', '#5d6469'), f'translate({x},{y}) scale({s})')
def heron_(x, y, s=1):
    return G(L(-2, 20, -4, 90, '#5d6469', 3) + L(4, 20, 6, 90, '#5d6469', 3) + E(0, 0, 28, 16, '#9aa6ae') + St('M22,-4 Q34,-24 24,-40 Q16,-52 26,-60', '#9aa6ae', 6) + Ci(28, -62, 7, '#ffffff') + L(26, -66, 10, -70, '#2f3437', 2) + Pa('M34,-62 L58,-58 L34,-58 Z', '#f3c234'), f'translate({x},{y}) scale({s})')
def stork_(x, y, s=1):
    return G(L(-4, 20, -6, 90, '#e2463b', 3) + L(4, 20, 6, 90, '#e2463b', 3) + E(0, 0, 30, 18, '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"') + Pa('M-28,-4 Q-10,14 20,12 Q-6,24 -30,10 Z', '#2f3437') + St('M24,-6 Q30,-30 26,-50', '#ffffff', 8) + Ci(28, -54, 8, '#ffffff', 'stroke="#d9dcde" stroke-width="1"') + Pa('M34,-56 L64,-46 L34,-50 Z', '#e2463b'), f'translate({x},{y}) scale({s})')
def vulture_(x, y, s=1):
    return G(E(0, 0, 30, 30, '#4a3a3a') + Pa('M-30,0 Q-50,30 -40,50 L-20,20 Z', '#3a2a2a') + E(12, -30, 20, 8, '#f6efe0') + St('M16,-30 Q20,-50 16,-60', '#e8b8a0', 7) + Ci(16, -62, 9, '#e8b8a0') + Pa('M22,-64 L34,-58 L22,-54 Z', '#5d6469') + Ci(18, -64, 2, '#2f3437') + L(-6, 28, -6, 44, '#a8a090', 3) + L(6, 28, 6, 44, '#a8a090', 3), f'translate({x},{y}) scale({s})')
def nest_(x, y, s=1, eggs=3):
    return G(E(0, 6, 50, 20, '#8a5a35') + ''.join(St(f'M{-48+j*8},{-2+(j%3)*6} q16,10 30,-2', '#6a4a2a', 2) for j in range(10)) + ''.join(E(-16 + j * 16, -4, 9, 12, '#cfe8f6') for j in range(eggs)) + E(0, 10, 44, 12, '#a8703e'), f'translate({x},{y}) scale({s})')
def feather_(x, y, s=1, col='#3c7fc1', rot=30):
    return G(Pa('M0,60 Q-26,0 0,-70 Q26,0 0,60 Z', col) + L(0, 70, 0, -66, '#ffffff', 2) + ''.join(L(0, -50 + j * 14, -14, -40 + j * 14, '#ffffff', 1, ) + L(0, -50 + j * 14, 14, -40 + j * 14, '#ffffff', 1) for j in range(7)), f'translate({x},{y}) rotate({rot}) scale({s})')
def butterfly_(x, y, s=1, col='#f08a24', col2='#2f3437'):
    return G(E(-22, -14, 22, 20, col, 'transform="rotate(-20 -22 -14)"') + E(22, -14, 22, 20, col, 'transform="rotate(20 22 -14)"') + E(-16, 14, 14, 14, col) + E(16, 14, 14, 14, col) + Ci(-24, -16, 6, col2) + Ci(24, -16, 6, col2) + Ci(-16, 14, 4, '#ffffff') + Ci(16, 14, 4, '#ffffff') + E(0, 0, 4, 22, '#2f3437') + St('M-2,-20 Q-10,-34 -14,-36 M2,-20 Q10,-34 14,-36', '#2f3437', 1.5), f'translate({x},{y}) scale({s})')
def bee_(x, y, s=1):
    return G(E(-6, -16, 12, 8, '#dff1fb', 'opacity=".9" transform="rotate(-30 -6 -16)"') + E(8, -16, 12, 8, '#dff1fb', 'opacity=".9" transform="rotate(30 8 -16)"') + E(0, 0, 22, 15, '#f3c234') + R(-8, -14, 6, 28, '#2f3437') + R(6, -14, 6, 28, '#2f3437') + Ci(22, -2, 9, '#2f3437') + Ci(24, -4, 2, '#ffffff') + Pa('M-22,0 L-30,0 L-22,4 Z', '#2f3437'), f'translate({x},{y}) scale({s})')
def ant_(x, y, s=1, col='#2f3437'):
    return G(E(-18, 0, 12, 9, col) + E(0, 0, 7, 6, col) + Ci(14, -2, 8, col) + ''.join(L(-4 + j * 6, 4, -12 + j * 10, 18, col, 2) for j in range(3)) + L(18, -8, 26, -18, col, 1.5) + L(14, -8, 18, -20, col, 1.5), f'translate({x},{y}) scale({s})')
def spider_(x, y, s=1):
    return G(''.join(St(f'M0,0 Q{d*24},{-14+j*8} {d*36},{6+j*8}', '#2f3437', 3) for j in range(4) for d in (-1, 1)) + E(0, 6, 14, 16, '#2f3437') + Ci(0, -10, 9, '#2f3437') + Ci(-3, -12, 2, '#ffffff') + Ci(3, -12, 2, '#ffffff'), f'translate({x},{y}) scale({s})')
def mosquito_(x, y, s=1):
    return G(E(-4, -12, 16, 6, '#dff1fb', 'opacity=".9" transform="rotate(-20 -4 -12)"') + E(8, -12, 16, 6, '#dff1fb', 'opacity=".9" transform="rotate(20 8 -12)"') + E(-10, 0, 18, 5, '#5d6469') + Ci(10, -2, 6, '#5d6469') + L(14, 0, 30, 8, '#2f3437', 1.5) + ''.join(L(-4 + j * 6, 2, -14 + j * 10, 24, '#5d6469', 1) for j in range(3)), f'translate({x},{y}) scale({s})')
def fly_(x, y, s=1):
    return G(E(-8, -12, 14, 9, '#dff1fb', 'opacity=".8" transform="rotate(-30 -8 -12)"') + E(8, -12, 14, 9, '#dff1fb', 'opacity=".8" transform="rotate(30 8 -12)"') + E(0, 2, 12, 14, '#3a4a3a') + Ci(0, -14, 8, '#3a4a3a') + Ci(-5, -16, 4, '#a8302a') + Ci(5, -16, 4, '#a8302a') + ''.join(L(-6, 0 + j * 6, -16, 4 + j * 8, '#2f3437', 1.5) + L(6, 0 + j * 6, 16, 4 + j * 8, '#2f3437', 1.5) for j in range(3)), f'translate({x},{y}) scale({s})')
def ladybug_(x, y, s=1):
    return G(Ci(0, 0, 28, '#e2463b') + Ci(0, -26, 12, '#2f3437') + L(0, -18, 0, 28, '#2f3437', 2) + ''.join(Ci(dx, dy, 5, '#2f3437') for dx, dy in [(-12, -6), (12, -6), (-14, 12), (14, 12), (-6, 22), (6, 22)]) + Ci(-4, -30, 2.5, '#ffffff') + Ci(4, -30, 2.5, '#ffffff'), f'translate({x},{y}) scale({s})')
def dragonfly_(x, y, s=1):
    return G(E(-16, -10, 28, 7, '#ffffff', 'stroke="#5aa1d4" stroke-width="2" opacity=".9" transform="rotate(-15 -16 -10)"') + E(16, -10, 28, 7, '#ffffff', 'stroke="#5aa1d4" stroke-width="2" opacity=".9" transform="rotate(15 16 -10)"') + E(-14, 6, 24, 6, '#ffffff', 'stroke="#5aa1d4" stroke-width="2" opacity=".9" transform="rotate(15 -14 6)"') + E(14, 6, 24, 6, '#ffffff', 'stroke="#5aa1d4" stroke-width="2" opacity=".9" transform="rotate(-15 14 6)"') + R(-3, -6, 6, 60, '#2fa59b', 3) + Ci(0, -12, 8, '#2fa59b') + Ci(-4, -14, 4, '#1f5a5a') + Ci(4, -14, 4, '#1f5a5a'), f'translate({x},{y}) scale({s})')
def caterpillar_(x, y, s=1):
    return G(''.join(Ci(-40 + j * 14, -abs(math.sin(j * .7)) * 10, 10, '#7cc05a' if j % 2 else '#5aaa3a') for j in range(6)) + Ci(40, -6, 12, '#5aaa3a') + Ci(44, -8, 2.5, '#2f3437') + L(38, -16, 34, -26, '#2f3437', 1.5) + L(44, -16, 48, -26, '#2f3437', 1.5), f'translate({x},{y}) scale({s})')
def worm_(x, y, s=1):
    return G(St('M-50,0 q12,-16 24,0 t24,0 t24,0 t24,0', '#e08a8a', 12) + Ci(46, 0, 7, '#e08a8a') + Ci(48, -2, 1.5, '#2f3437'), f'translate({x},{y}) scale({s})')
def snail_(x, y, s=1):
    return G(E(0, 14, 44, 10, '#c8b880') + Ci(36, 0, 9, '#c8b880') + L(34, -8, 36, -22, '#c8b880', 3) + L(40, -8, 46, -20, '#c8b880', 3) + Ci(36, -22, 2.5, '#2f3437') + Ci(46, -20, 2.5, '#2f3437') + Ci(0, -2, 24, '#c8903a') + St('M0,-2 m-14,0 a14,14 0 1,1 28,0 a9,9 0 1,1 -18,0 a4,4 0 1,1 8,0', '#a8703e', 3), f'translate({x},{y}) scale({s})')
def beetle_(x, y, s=1, col='#2f6a4a'):
    return G(''.join(L(-10, -8 + j * 10, -26, -14 + j * 14, '#2f3437', 2) + L(10, -8 + j * 10, 26, -14 + j * 14, '#2f3437', 2) for j in range(3)) + E(0, 6, 20, 26, col) + L(0, -18, 0, 32, shade(col, -.3), 2) + Ci(0, -22, 10, '#2f3437') + hi(-8, -2, 4, 8, .5) + L(-4, -30, -12, -40, '#2f3437', 1.5) + L(4, -30, 12, -40, '#2f3437', 1.5), f'translate({x},{y}) scale({s})')
def moth_(x, y, s=1):
    return G(Pa('M0,-6 Q-40,-36 -50,-4 Q-40,20 0,6 Z', '#c8b8a0') + Pa('M0,-6 Q40,-36 50,-4 Q40,20 0,6 Z', '#c8b8a0') + Ci(-26, -8, 6, '#8a7a6a') + Ci(26, -8, 6, '#8a7a6a') + E(0, 0, 5, 18, '#8a7a6a') + St('M-2,-16 Q-12,-30 -20,-28 M2,-16 Q12,-30 20,-28', '#8a7a6a', 2), f'translate({x},{y}) scale({s})')
def grasshopper_(x, y, s=1):
    return G(E(0, 0, 30, 10, '#7cc05a') + Pa('M-20,-6 L20,-12 L26,-4 L-20,4 Z', '#5aaa3a') + Ci(30, -4, 9, '#7cc05a') + Ci(33, -6, 2.5, '#2f3437') + St('M-10,6 L-30,-20 L-40,16', '#5aaa3a', 4) + L(10, 8, 14, 20, '#5aaa3a', 2) + L(20, 6, 26, 18, '#5aaa3a', 2) + St('M32,-12 Q50,-40 70,-36', '#5aaa3a', 1.5), f'translate({x},{y}) scale({s})')
def flower_bg():
    return R(0, 0, 200, 200, '#e6f4e0') + R(0, 160, 200, 40, '#9ac070') + ''.join(St(f'M{20+k*40},200 L{20+k*40},160', '#4a9a3a', 3) + flower(20 + k * 40, 158, 1.2, ['#ef8fa4', '#f3c234', '#ffffff', '#e2463b', '#7a4fa0'][k]) for k in range(5))

# ================= 鸟 1 =================
S_('bird', branch_bg() + bird(100, 120, 1.6, '#3c7fc1', '#f6efe0', '#f3c234', legs=True), False)
S_('nest', R(0, 0, 200, 200, '#dff1fb') + St('M0,140 Q100,120 200,150', '#8a5a35', 10) + nest_(100, 120, 1.4), False)
S_('feather', feather_(100, 100, 1.2, '#3c7fc1', 30))
S_('beak', R(0, 0, 200, 200, '#dff1fb') + Ci(60, 100, 60, '#3c7fc1') + Ci(70, 80, 8, '#ffffff') + Ci(72, 80, 4, '#2f3437') + Pa('M110,80 L190,100 L110,120 Z', '#f3c234') + L(110, 100, 180, 100, '#d9a020', 2) + Ci(100, 100, 66, 'none', 'stroke="#e2463b" stroke-width="0"'), False)
S_('sparrow', branch_bg() + bird(100, 120, 1.5, '#8a6a4a', '#e6dcc8', '#5d6469', '#6a4a2a', beak_len=7), False)
S_('pigeon', R(0, 0, 200, 200, '#e8eef2') + R(0, 160, 200, 40, WALK) + bird(100, 130, 1.6, '#9aa6ae', '#c4cbd0', '#5d6469', '#7a8690', eye_ring='#e2463b', beak_len=7) + E(122, 120, 8, 6, '#5a8a7a', 'opacity=".7"'), False)
S_('eagle', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,150 L60,110 L120,150 L200,120 L200,200 Z', '#7a8a9a') + eagle_(100, 80, .9), False)
S_('owl', R(0, 0, 200, 200, '#24304f') + moon(160, 40, 14) + St('M0,170 Q100,150 200,176', '#6a4a2a', 10) + owl_(100, 110, 1.3), False)
S_('parrot', R(0, 0, 200, 200, '#dff1d8') + St('M0,160 Q100,150 200,166', '#8a5a35', 8) + G(E(0, 0, 22, 34, '#e2463b') + E(-10, 4, 14, 26, '#3c7fc1') + Pa('M-6,30 L-18,80 L0,40 L6,82 L8,32 Z', '#3c7fc1') + Ci(4, -34, 18, '#e2463b') + Ci(10, -38, 7, '#ffffff') + Ci(11, -38, 3, '#2f3437') + Pa('M18,-34 Q34,-34 30,-16 Q24,-22 18,-24 Z', '#f6efe0') + E(-4, -4, 10, 18, '#f3c234'), 'translate(100,110)'), False)
S_('crow', R(0, 0, 200, 200, '#e8eef2') + St('M0,160 Q100,150 200,166', '#5a4a3a', 8) + bird(100, 124, 1.6, '#2f3437', '#3a4048', '#2f3437', '#1f2328', leg_col='#2f3437', beak_len=12), False)
S_('swan', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#5aa1d4') + swan_(100, 130, 1.3) + St('M30,170 q20,-6 40,0 t40,0 t40,0', '#9fd0ec', 3), False)
S_('magpie', branch_bg() + bird(100, 120, 1.5, '#2f3437', '#ffffff', '#2f3437', '#1f3a5a', 46, leg_col='#2f3437') + E(92, 120, 10, 6, '#ffffff'), False)
S_('seagull', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#3c9ad4') + bird(100, 120, 1.5, '#ffffff', '#ffffff', '#f3c234', '#a7adb1', leg_col='#f3c234') + flying_bird(160, 50, .5, '#5d6469'), False)
S_('penguin', R(0, 0, 200, 200, '#cfe2f0') + R(0, 150, 200, 50, '#ffffff') + penguin_(100, 110, 1.4), False)
S_('peacock', R(0, 0, 200, 200, '#e6f0d8') + peacock_(100, 130, 1.0), False)
S_('woodpecker', R(0, 0, 200, 200, '#dff1d8') + R(120, 0, 40, 200, '#8a5a35') + ''.join(L(124, k * 20, 156, k * 20 + 4, '#6a4a2a', 1) for k in range(10)) + G(bird(0, 0, 1.3, '#2f3437', '#ffffff', '#5d6469', '#2f3437', 20, False, '#e2463b', beak_len=14), 'translate(90,100) rotate(-70)') + ''.join(Ci(122, 70 + k * 10, 2, '#d9a868') for k in range(3)), False)

# ================= 鸟 2 =================
S_('robin', branch_bg() + bird(100, 120, 1.5, '#8a6a4a', '#f08a24', '#f3c234', beak_len=7), False)
S_('swallow-birds2', R(0, 0, 200, 200, SKY) + G(Pa('M0,0 Q-40,-30 -80,-20 Q-50,-6 -20,8 Z', '#1f2a5a') + Pa('M0,0 Q40,-30 80,-20 Q50,-6 20,8 Z', '#1f2a5a') + E(0, 4, 12, 18, '#1f2a5a') + E(0, 10, 7, 10, '#ffffff') + Ci(0, -14, 8, '#1f2a5a') + E(0, -8, 5, 3, '#c0583a') + Pa('M-4,20 L-14,50 L0,26 L14,50 L4,20 Z', '#1f2a5a'), 'translate(100,90) scale(1.1)'), False)
S_('crane-birds2', R(0, 0, 200, 200, '#e6f0f4') + R(0, 170, 200, 30, '#9ac070') + crane_bird(100, 102, .95), False)
S_('ostrich', savanna_ if False else R(0, 0, 200, 200, '#f6e8c8') + R(0, 170, 200, 30, '#d8c070') + ostrich_(100, 190, 1.0), False)
S_('flamingo', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#5aa1d4') + flamingo_(96, 100, .95), False)
S_('hummingbird', R(0, 0, 200, 200, '#e6f4e0') + G(Pa('M0,0 Q-20,-30 0,-50 Q20,-30 0,0 Z', '#e2463b') + St('M0,0 L0,60', '#4a9a3a', 3), 'translate(150,110) rotate(-30)') + hummer(80, 90, 1.6), False)
S_('pelican', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#3c9ad4') + pelican_(80, 110, 1.2), False)
S_('kingfisher', R(0, 0, 200, 200, '#dff1d8') + R(0, 150, 200, 50, '#5aa1d4') + St('M0,120 L120,110', '#8a5a35', 6) + bird(70, 90, 1.4, '#2f8ac8', '#f08a24', '#2f3437', '#1f6aa8', 12, beak_len=18) + fish_shape(150, 170, 26, '#a7adb1'), False)
S_('canary', R(0, 0, 200, 200, '#fef3e2') + ''.join(L(40 + k * 15, 30, 40 + k * 15, 170, '#c4cbd0', 2) for k in range(9)) + E(100, 30, 64, 14, '#c4cbd0') + R(30, 166, 140, 10, '#c4cbd0', 3) + L(50, 130, 150, 130, '#8a5a35', 4) + bird(100, 104, 1.3, '#f3c234', '#f6e070', '#f08a24', '#e0b020', leg_col='#f08a24', beak_len=6), False)
S_('cuckoo', R(0, 0, 200, 200, '#fef3e2') + G(R(-50, -40, 100, 110, '#8a5a35', 4) + Pa('M-60,-40 L0,-80 L60,-40 Z', '#6a3a20') + Ci(0, 20, 30, '#f6efe0') + clock(0, 20, 28, (3, 0)) + R(-14, -34, 28, 22, '#2f3437', 3) + bird(4, -24, .5, '#8a9196', '#e6dcc8', '#f3c234', legs=False) + L(-14, 70, -14, 100, '#d9a33a', 2) + L(14, 70, 14, 110, '#d9a33a', 2), 'translate(100,90)'), False)
S_('hawk', R(0, 0, 200, 200, SKY) + G(Pa('M0,0 Q-50,-30 -90,-10 Q-60,0 -50,16 Q-30,6 -16,14 Z', '#8a5a35') + Pa('M0,0 Q50,-30 90,-10 Q60,0 50,16 Q30,6 16,14 Z', '#8a5a35') + E(0, 10, 16, 24, '#a8703e') + E(0, 14, 10, 16, '#f6e8d0') + Ci(0, -14, 12, '#a8703e') + Pa('M6,-14 L16,-8 L6,-6 Z', '#f3c234') + Ci(3, -16, 2.5, '#2f3437') + Pa('M-10,30 L0,48 L10,30 Z', '#a8703e'), 'translate(100,90) scale(1.0)'), False)
S_('falcon', R(0, 0, 200, 200, '#cfe8f6') + G(bird(0, 0, 1.4, '#5d6469', '#f6efe0', '#f3c234', '#3a4048', 26, leg_col='#f3c234', beak_len=8) + Pa('M18,-12 L22,0 L16,-2 Z', '#2f3437'), 'translate(100,100) rotate(-10)') + R(60, 140, 80, 10, '#8a5a35', 4), False)
S_('vulture', R(0, 0, 200, 200, '#f6e8c8') + R(0, 160, 200, 40, '#d8c070') + R(40, 140, 100, 10, '#8a6a4a', 4) + vulture_(100, 100, 1.3), False)
S_('heron', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#5aa1d4') + heron_(100, 80, 1.1), False)
S_('stork', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#9ac070') + stork_(90, 90, 1.1), False)
S_('migrate', R(0, 0, 200, 200, '#fbe0c0') + ''.join(flying_bird(40 + k * 22, 80 + abs(k - 3) * 14, .5, '#2f3437') for k in range(7)) + arrow(30, 150, 170, 150, '#e2463b', 4) + earth_(20, 180, 0), False)

# ================= 昆虫 =================
S_('insect', R(0, 0, 200, 200, '#e6f4e0') + beetle_(100, 100, 1.6, '#3c7fc1'), False)
S_('bug', R(0, 0, 200, 200, '#e6f4e0') + leaf_shape(100, 110, 1.6, '#7cc05a', 30) + ladybug_(110, 90, .7) + ant_(60, 150, .8), False)
S_('butterfly', flower_bg() + butterfly_(100, 80, 1.5), False)
S_('bee', flower_bg() + bee_(100, 80, 1.6), False)
S_('ant', R(0, 0, 200, 200, '#e6dcc0') + ant_(70, 110, 1.6) + ant_(150, 150, 1.0) + G(Ci(0, 0, 6, '#ffffff'), 'translate(100,96)'), False)
S_('spider', R(0, 0, 200, 200, '#e8eef2') + ''.join(L(100, 60, 100 + 100 * math.cos(a), 60 + 100 * math.sin(a), '#c4cbd0', 1) for a in [k * math.pi / 6 for k in range(12)]) + ''.join(Ci(100, 60, r_, 'none', 'stroke="#c4cbd0" stroke-width="1"') for r_ in (20, 40, 60, 80)) + L(100, 0, 100, 100, '#5d6469', 1) + spider_(100, 120, 1.4), False)
S_('mosquito', R(0, 0, 200, 200, '#e8eef2') + mosquito_(100, 90, 2.0) + G(R(-12, -12, 24, 24, '#ef8fa4', 12), 'translate(140,160)'), False)
S_('fly-insects', R(0, 0, 200, 200, '#e8eef2') + fly_(100, 100, 2.4), False)
S_('ladybug', R(0, 0, 200, 200, '#e6f4e0') + leaf_shape(100, 110, 1.8, '#7cc05a', -20) + ladybug_(100, 100, 1.3), False)
S_('dragonfly', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#5aa1d4') + ''.join(St(f'M{30+k*30},200 L{30+k*30},140', '#5a8a3a', 3) for k in range(5)) + dragonfly_(100, 70, 1.4), False)
S_('caterpillar', R(0, 0, 200, 200, '#e6f4e0') + leaf_shape(100, 130, 1.8, '#5aaa3a', 90) + caterpillar_(100, 120, 1.3), False)
S_('worm', R(0, 0, 200, 200, '#a8805a') + R(0, 0, 200, 60, '#9ac070') + worm_(100, 120, 1.5) + ''.join(Ci((k * 37) % 200, 80 + (k * 29) % 120, 3, '#8a6a4a') for k in range(12)), False)
S_('snail', R(0, 0, 200, 200, '#e6f4e0') + R(0, 150, 200, 50, '#9ac070') + snail_(100, 136, 1.6), False)
S_('beetle', R(0, 0, 200, 200, '#e6dcc0') + beetle_(100, 100, 2.0, '#2f6a4a'), False)
S_('moth', R(0, 0, 200, 200, '#24304f') + bulb(100, 40, 14) + moth_(100, 120, 1.4), False)
S_('grasshopper', R(0, 0, 200, 200, '#e6f4e0') + R(0, 150, 200, 50, '#9ac070') + grasshopper_(90, 120, 1.6), False)

dump()
