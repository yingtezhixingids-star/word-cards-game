from flat import *
from fig import *
import os, sys, random

A = {}
SK = P['skin']

def chunk(cx, cy, w, h, meat='#c9524a', fat='#fbeee0', rot=0, marble=True, seed=1):
    random.seed(seed)
    g = Pa(f'M{-w/2},{-h*.3} Q{-w*.45},{-h/2} {-w*.1},{-h/2} L{w*.35},{-h*.45} Q{w/2},{-h*.4} {w/2},{-h*.1} L{w*.45},{h*.35} Q{w*.4},{h/2} {w*.1},{h/2} L{-w*.35},{h*.45} Q{-w/2},{h*.4} {-w/2},{h*.1} Z', fat)
    g += Pa(f'M{-w*.44},{-h*.24} Q{-w*.4},{-h*.4} {-w*.1},{-h*.4} L{w*.32},{-h*.36} Q{w*.42},{-h*.32} {w*.42},{-h*.08} L{w*.38},{h*.3} Q{w*.34},{h*.4} {w*.1},{h*.4} L{-w*.32},{h*.36} Q{-w*.42},{h*.32} {-w*.42},{h*.08} Z', meat)
    if marble:
        g += ''.join(St(f'M{random.uniform(-w*.35,w*.2):.0f},{random.uniform(-h*.3,h*.3):.0f} q{random.uniform(4,10):.0f},{random.uniform(-4,4):.0f} {random.uniform(10,20):.0f},0', shade(fat, -.02), 2) for _ in range(5))
    g += hi(-w * .2, -h * .2, w * .12, h * .06, .3, -10)
    return G(g, f'translate({cx},{cy}) rotate({rot})')

def bone_end(x, y, s=1):
    return Ci(x - 4 * s, y, 6 * s, '#f6efe0') + Ci(x + 4 * s, y, 6 * s, '#f6efe0')

def drumstick(cx, cy, s, rot=0, col='#c97a3a'):
    g = Pa('M-30,-14 Q-40,-32 -18,-34 Q4,-34 16,-14 Q24,0 12,10 Q-6,18 -20,6 Q-28,0 -30,-14 Z', col) + Pa('M-6,-30 Q8,-24 16,-14 Q24,0 12,10 Q8,-4 -6,-30 Z', shade(col, -.15))
    g += R(10, 4, 26, 8, '#f6efe0', 4, 'transform="rotate(35 10 4)"') + Ci(34, 24, 6, '#f6efe0') + Ci(28, 28, 6, '#f6efe0') + hi(-16, -20, 6, 3, .4, -20)
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

# meat 肉：砧板上牛排、鸡腿、排骨放在一起
g = board(100, 130, 170, 90) + chunk(72, 118, 74, 52, seed=2) + drumstick(140, 120, .9, -20, '#f2c9a8') + chunk(110, 150, 50, 30, '#e88a8a', seed=3)
A['meat'] = svg(g)

# chicken 鸡肉：一整只生鸡（白条鸡）+ 鸡头像标记
g = board(100, 150, 170, 50)
g += E(96, 118, 58, 40, '#f6d8b0') + E(110, 108, 30, 20, '#fbe6c8') + E(84, 132, 40, 16, '#eac49a')
g += drumstick(52, 140, .75, 160, '#f2cfa0') + drumstick(142, 140, .75, 20, '#f2cfa0')
g += E(140, 98, 16, 12, '#f2cfa0')
g += badge(160, 40, 'chicken')
A['chicken'] = svg(g)

# beef 牛肉：一大块深红色牛肉 + 牛头标记
g = board(96, 140, 160, 70) + chunk(92, 126, 112, 72, '#a8342e', '#f3e2d0', seed=4) + badge(160, 40, 'cow')
A['beef'] = svg(g)

# pork 猪肉：一块粉红色带皮猪肉 + 猪头标记
g = board(96, 140, 160, 70) + chunk(92, 126, 112, 72, '#e98a86', '#fbeee0', seed=5) + badge(160, 40, 'pig')
A['pork'] = svg(g)

# lamb 羊肉：带骨羊排 + 羊头标记
g = board(96, 140, 160, 70)
for i in range(4):
    x = 52 + i * 26
    g += R(x + 6, 76, 8, 46, '#f6efe0', 4) + Ci(x + 10, 76, 6, '#f6efe0')
    g += Pa(f'M{x-6},116 Q{x-8},150 {x+10},156 Q{x+30},152 {x+26},116 Z', '#c9625a') + Pa(f'M{x-6},116 Q{x},110 {x+10},112 Q{x+22},110 {x+26},116 Q{x+10},124 {x-6},116 Z', '#fbeee0')
g += badge(160, 40, 'sheep')
A['lamb'] = svg(g)

# duck 鸭肉：一只烤鸭腿和一盘鸭肉片 + 鸭子标记
g = E(96, 146, 76, 22, '#d9dcde') + E(96, 142, 76, 22, '#ffffff')
for i in range(6):
    g += G(Pa('M-14,-6 Q0,-12 14,-6 L12,6 Q0,10 -12,6 Z', '#fbeee0') + Pa('M-14,-6 Q0,-12 14,-6 L13,-1 Q0,-5 -13,-1 Z', '#b0582a'), f'translate({56+i*15},{140-(i%2)*4}) rotate({-10+i*4})')
g += drumstick(110, 96, 1.0, -30, '#b0582a') + badge(160, 40, 'duck')
A['duck'] = svg(g)

# sausage 香肠：一串连在一起的香肠
g = ''
pts = [(40, 70), (80, 92), (120, 104), (156, 130)]
for i, (x, y) in enumerate(pts):
    g += G(R(-24, -12, 48, 24, '#b8463e', 12) + R(-20, -9, 40, 7, '#d9645a', 4) + ''.join(Ci(-12 + k * 8, 4, 1.4, '#8a2a24') for k in range(4)), f'translate({x},{y}) rotate({20+i*6})')
    if i < 3: g += L(x + 22, y + 9, pts[i + 1][0] - 22, pts[i + 1][1] - 9, '#8a2a24', 3)
g += G(R(-24, -12, 48, 24, '#b8463e', 12) + R(-20, -9, 40, 7, '#d9645a', 4), 'translate(70,150) rotate(-10)')
A['sausage'] = svg(g)

# ham 火腿：一整只带骨火腿，切开露出粉色
g = Pa('M30,120 Q24,70 70,58 Q120,46 150,84 Q170,110 150,140 Q120,170 70,164 Q36,160 30,120 Z', '#b0582a')
g += Pa('M150,84 Q170,110 150,140 Q140,150 128,152 Q150,120 136,82 Z', '#8a4020')
g += E(150, 112, 18, 30, '#ef9a96') + E(150, 112, 10, 18, '#f6b8b0') + Ci(150, 112, 5, '#f6efe0')
g += R(18, 104, 30, 14, '#f6efe0', 6, 'transform="rotate(-20 33 111)"') + bone_end(16, 116, 1.1)
g += ''.join(L(56 + i * 18, 70, 46 + i * 18, 150, '#c96a3a', 2) for i in range(5))
A['ham'] = svg(g)

# bacon 培根：平底锅里煎着两片培根
g = G(Ci(0, 0, 70, '#3a3f44') + Ci(0, 0, 60, '#50565c') + R(66, -8, 70, 16, '#2f3437', 8), 'translate(84,110) scale(1,.7)')
def strip(y, rot):
    w = 'M0,{a} Q15,{b} 30,{a} T60,{a} T90,{a}'
    g = ''
    for off, th, c in [(0, 6, '#fbeee0'), (6, 6, '#c9524a'), (12, 4, '#fbeee0'), (16, 6, '#a8342e')]:
        g += St(w.format(a=off + th / 2, b=off + th / 2 - 8), c, th + .8, 'stroke-linecap="butt"')
    return G(g, f'translate(40,{y}) rotate({rot} 45 10)')
g += strip(84, -4) + strip(108, 4)
g += steam(70, 70, 3, 16, '#c4cbd0', .8)
A['bacon'] = svg(g)

# steak 牛排：铁板上带烤纹的T骨牛排
g = E(100, 140, 84, 28, '#2f3437') + E(100, 134, 84, 28, '#4a5157')
g += Pa('M40,120 Q36,94 70,86 Q120,76 150,96 Q170,112 156,134 Q130,152 80,150 Q44,146 40,120 Z', '#7a3a24')
g += ''.join(L(56 + i * 20, 92, 76 + i * 20, 146, '#3a1a10', 4) for i in range(5))
g += Pa('M94,86 L104,148', 'none', 'stroke="#f6efe0" stroke-width="6" stroke-linecap="round"') + Pa('M94,90 L120,92', 'none', 'stroke="#f6efe0" stroke-width="5" stroke-linecap="round"')
g += Ci(150, 116, 6, '#5ba644') + Ci(140, 140, 7, '#f08a24') + steam(80, 70, 3, 18, '#c4cbd0', .8)
A['steak'] = svg(g)

# ribs 排骨：一扇烤排骨，一根根骨头露出来
g = board(100, 140, 170, 60)
g += Pa('M30,96 Q100,74 170,96 L170,142 Q100,124 30,142 Z', '#a8502a') + Pa('M30,96 Q100,74 170,96 L170,106 Q100,86 30,106 Z', '#c06a3a')
for i in range(6):
    x = 42 + i * 24
    g += R(x - 4, 80 - abs(i - 2.5) * 3, 8, 70, '#f6efe0', 4) + L(x + 12, 96, x + 12, 136, '#7a3a20', 2)
g += hi(80, 100, 20, 4, .3)
A['ribs'] = svg(g)

# chicken-wings 鸡翅：盘子里几只金黄的炸鸡翅
g = E(100, 140, 82, 26, '#d9dcde') + E(100, 136, 82, 26, '#ffffff')
def wing(x, y, rot):
    w = Pa('M-26,0 Q-28,-16 -10,-16 L8,-10 Q20,-22 30,-12 Q34,0 22,8 Q6,14 -12,12 Q-26,10 -26,0 Z', '#d98a3a') + Pa('M8,-10 Q20,-22 30,-12 Q34,0 22,8 Q24,-4 8,-10 Z', '#b86a28')
    w += ''.join(Ci(-18 + k * 8, -4 + (k % 2) * 6, 2, '#f0b060') for k in range(5))
    return G(w, f'translate({x},{y}) rotate({rot})')
g += wing(68, 126, -10) + wing(126, 124, 15) + wing(98, 108, -5) + wing(96, 140, 5)
A['chicken-wings'] = svg(g)

# minced-meat 肉馅：碗里一堆细碎的粉红肉馅，旁边菜刀
random.seed(9)
g = bowl(84, 112, 120, fill='#e98a86', pattern=None)
g += Pa('M36,112 Q50,74 84,76 Q118,74 132,112 Z', '#e98a86')
g += ''.join(Ci(random.uniform(46, 122), random.uniform(84, 110), random.uniform(2, 4), random.choice(['#f6b8b0', '#c9625a', '#fbeee0'])) for _ in range(60))
g += G(R(0, 0, 50, 34, '#cfd5d9', 3) + R(50, 8, 36, 16, '#5a3a24', 6), 'translate(140,140) rotate(-60) scale(.8)')
A['minced-meat'] = svg(g)

# turkey 火鸡：大盘子上一整只烤火鸡，腿上套着纸花
g = E(100, 156, 90, 26, '#d9dcde') + E(100, 152, 90, 26, '#ffffff')
g += E(100, 120, 62, 42, '#c0702e') + E(90, 106, 36, 20, '#d98a40') + hi(84, 100, 14, 6, .35, -10)
for sx in (-1, 1):
    g += G(E(0, 0, 22, 16, '#b0602a') + R(14, -5, 22, 10, '#f6efe0', 5) + Pa('M34,-10 L44,-14 L42,-6 L48,0 L42,6 L44,14 L34,10 Z', '#ffffff'), f'translate({100+sx*44},{100}) rotate({-30 if sx>0 else 210})')
g += Ci(52, 156, 7, '#5ba644') + Ci(150, 158, 7, '#d9453a') + Ci(160, 150, 6, '#f08a24')
A['turkey'] = svg(g)

# butcher 肉铺：系围裙、拿砍刀的屠夫，身后挂着肉
cx, cy, r = 100, 80, 30
g = R(0, 0, 200, 8, '#a7adb1') + ''.join(St(f'M{x},8 L{x},26', '#5d6469', 2) + chunk(x, 50, 26, 44, '#c9524a', '#fbeee0', seed=x) for x in (24, 176))
g += body(cx, cy, r, '#3c7fc1', w=r * 3.6) + Pa(f'M{cx-r*1.2},{cy+r*1.1} L{cx+r*1.2},{cy+r*1.1} L{cx+r*1.4},200 L{cx-r*1.4},200 Z', '#ffffff') + L(cx - r * .6, cy + r * 1.1, cx - r * .4, cy + r * .9, '#e6ecef', 3)
g += Pa(f'M{cx-r*.2},{cy+r*2.6} q10,-4 18,6 q-6,8 -18,2', '#e2a0a0', 'opacity=".5"')
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'smile', None)
g += St(f'M{cx-r*.45},{cy+r*.32} q{r*.45},{-r*.15} {r*.9},0', '#3a2a20', 4)
g += R(cx - r * .95, cy - r * 1.25, r * 1.9, r * .5, '#ffffff', 6)
g += arm([(cx + r * 1.7, 200), (cx + r * 2.2, cy + r * 1.6), (cx + r * 2.0, cy + r * .6)], '#3c7fc1', SK, 15)
g += G(R(-2, -40, 34, 26, '#cfd5d9', 3) + R(-4, -14, 10, 24, '#5a3a24', 4), f'translate({cx+r*1.9},{cy+r*.5})')
A['butcher'] = svg(g, shadow=False)

# lean 瘦的：瘦肉（打勾）和肥肉（打叉）对比
g = chunk(58, 104, 76, 60, '#c9524a', '#c9524a', marble=False, seed=1) + Ci(58, 160, 14, '#5ba644') + St('M50,160 l6,6 l10,-12', '#ffffff', 4)
g += chunk(146, 104, 76, 60, '#e98a86', '#fbeee0', seed=2) + R(118, 84, 56, 14, '#fbeee0', 6) + R(118, 110, 56, 10, '#fbeee0', 5)
g += Ci(146, 160, 14, '#d9453a') + St('M140,154 l12,12 M152,154 l-12,12', '#ffffff', 4)
A['lean'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
