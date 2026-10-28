from flat import *
from fig import *
import os, sys, random

A = {}

def peanut(x, y, s, rot):
    return G(E(-9, 0, 11, 9, '#d9b07a') + E(9, 0, 11, 9, '#d9b07a') + E(0, 0, 6, 6, '#d9b07a') +
             ''.join(Ci(-12 + i * 6, -3 + (i % 2) * 5, 1.2, '#b88c55') for i in range(5)), f'translate({x},{y}) rotate({rot}) scale({s})')

def kernel(x, y, s, rot, col='#e8b896'):
    return G(E(0, 0, 7, 10, col) + E(2, 2, 4, 7, shade(col, -.1)), f'translate({x},{y}) rotate({rot}) scale({s})')

def walnut(x, y, s, half=False):
    if half:
        g = Ci(0, 0, 26, '#b88a52') + Ci(0, 0, 22, '#d9b07a') + Pa('M0,-20 Q-16,-12 -8,0 Q-18,12 0,20 Q-4,0 0,-20 Z M0,-20 Q16,-12 8,0 Q18,12 0,20 Q4,0 0,-20 Z', '#a8743a')
    else:
        g = E(0, 0, 26, 28, '#c9985a') + St('M0,-28 Q-6,0 0,28', '#a8743a', 2.5) + ''.join(St(f'M{-20+k*8},{-16+(k%2)*10} q4,6 8,0', '#a8743a', 2) for k in range(6)) + hi(-10, -10, 5, 8, .3)
    return G(g, f'translate({x},{y}) scale({s})')

def almond(x, y, s, rot):
    return G(Pa('M0,-20 Q14,-6 10,10 Q4,22 0,22 Q-4,22 -10,10 Q-14,-6 0,-20 Z', '#b8743a') + St('M-2,-12 q-2,14 0,28', '#9a5a2a', 1.5) + St('M4,-8 q2,12 0,22', '#9a5a2a', 1.2), f'translate({x},{y}) rotate({rot}) scale({s})')

def cashew(x, y, s, rot):
    g = St('M-14,-14 Q-22,6 -6,16 Q10,22 16,8', '#e8cc94', 15) + St('M-14,-14 Q-22,6 -6,16 Q10,22 16,8', '#f4e2b8', 8) + hi(-14, 0, 2, 6, .5)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def berry(x, y, r, col='#3c4f9a'):
    return Ci(x, y, r, col) + Ci(x - r * .3, y - r * .3, r * .25, '#ffffff', 'opacity=".35"') + Pa(f'M{x-r*.3},{y-r*.85} l{r*.3},{r*.3} l{r*.3},{-r*.3}', 'none', f'stroke="{shade(col,-.3)}" stroke-width="1.5"')

# nut 坚果：一碗什锦坚果
random.seed(1)
g = bowl(100, 110, 140, pattern='#c58b54')
g += Pa('M32,110 Q50,80 100,78 Q150,80 168,110 Z', '#a8703e')
for k in range(14):
    x, y = random.uniform(48, 152), random.uniform(80, 104)
    g += random.choice([lambda: almond(x, y, .9, random.uniform(-60, 60)), lambda: cashew(x, y, .8, random.uniform(0, 360)), lambda: walnut(x, y, .5, True), lambda: peanut(x, y, .9, random.uniform(0, 180))])()
A['nut'] = svg(g)

# peanut 花生：带壳花生和花生米
g = peanut(70, 90, 2.2, -20) + peanut(130, 80, 1.8, 30)
g += ''.join(kernel(80 + k * 18, 150 + (k % 2) * 8, 1.2, k * 40) for k in range(4))
A['peanut'] = svg(g)

A['walnut'] = svg(walnut(76, 100, 1.6) + walnut(140, 140, 1.2, True))

# coconut 椰子：棕色毛椰子和一半白色椰肉
g = Ci(76, 104, 52, '#7a5030') + ''.join(St(f'M{40+k*10},{70+(k%3)*12} l8,6', '#5a3a20', 2) for k in range(8)) + Ci(60, 88, 5, '#4a2a18') + Ci(76, 80, 5, '#4a2a18') + Ci(68, 100, 5, '#4a2a18')
g += Pa('M110,130 A42,42 0 0,0 194,130 Z', '#7a5030') + Pa('M116,130 A36,36 0 0,0 188,130 Z', '#fbf8f0') + E(152, 130, 36, 6, '#f2ece0')
g += St('M66,60 L90,10', '#e2463b', 5) + St('M90,10 l10,6', '#e2463b', 5)
A['coconut'] = svg(g)

# chestnut 栗子：深棕发亮的栗子，底部浅色
def chestnut(x, y, s, rot):
    return G(Pa('M0,-30 Q24,-20 28,6 Q26,26 0,28 Q-26,26 -28,6 Q-24,-20 0,-30 Z', '#7a3a1a') + Pa('M-26,10 Q0,18 26,10 Q24,26 0,28 Q-24,26 -26,10 Z', '#d9b07a') + Pa('M0,-30 l-3,-6 l6,0 Z', '#d9b07a') + hi(-10, -12, 6, 10, .4, 20), f'translate({x},{y}) rotate({rot}) scale({s})')
A['chestnut'] = svg(chestnut(70, 96, 1.5, -10) + chestnut(134, 100, 1.3, 15) + chestnut(104, 146, 1.2, 5))

A['almond'] = svg(''.join(almond(60 + (k % 3) * 40, 70 + (k // 3) * 56, 1.8, -30 + k * 20) for k in range(6)))

# raisin 葡萄干：小碗里的皱皱的葡萄干
random.seed(3)
g = bowl(100, 104, 130, pattern='#7a4fa0')
g += Pa('M38,104 Q56,72 100,70 Q144,72 162,104 Z', '#6a3a3a')
g += ''.join(E(random.uniform(48, 152), random.uniform(78, 102), 7, 5, random.choice(['#5a2a30', '#7a3a3a', '#8a4a3a']), f'transform="rotate({random.uniform(0,180):.0f} 100 100)"') for _ in range(0))
g += ''.join(E(x, y, 7, 5, random.choice(['#4a2028', '#7a3a3a', '#8a4a3a'])) + St(f'M{x-4},{y} q4,-3 8,0', '#3a1a20', 1) for x, y in [(random.uniform(50, 150), random.uniform(78, 100)) for _ in range(22)])
A['raisin'] = svg(g)

# blueberry 蓝莓：一堆深蓝色小浆果
random.seed(5)
g = ''.join(berry(x, y, random.uniform(14, 18), random.choice(['#3c4f9a', '#33447f', '#4a5aa8'])) for x, y in [(70, 120), (104, 116), (138, 122), (86, 92), (122, 92), (104, 146), (70, 150), (140, 152), (104, 70)])
g += leaf(150, 70, 30, 10, -40, '#5ba644')
A['blueberry'] = svg(g)

# grapefruit 西柚：一个整的，一个切开是粉红色瓣
g = Ci(70, 96, 42, '#f2a050') + hi(56, 80, 8, 12, .35, 30)
g += Ci(136, 136, 40, '#f2a050') + Ci(136, 136, 36, '#fbe0c8') + Ci(136, 136, 32, '#ef7a7a')
g += ''.join(L(136, 136, 136 + 32 * math.cos(a), 136 + 32 * math.sin(a), '#fbe0c8', 2.5) for a in [k * math.pi / 5 for k in range(10)]) + Ci(136, 136, 4, '#fbe0c8')
A['grapefruit'] = svg(g)

# lychee 荔枝：红色带疙瘩外壳，剥开是白色果肉
def lychee(x, y, r):
    g = Ci(x, y, r, '#d9354a') + ''.join(Ci(x + r * .6 * math.cos(a), y + r * .6 * math.sin(a), 3, '#b02438') for a in [k * math.pi / 4 for k in range(8)]) + Ci(x, y, 3, '#b02438') + hi(x - r * .4, y - r * .4, 5, 4, .35)
    return g
g = St('M60,30 Q80,40 76,64 M80,40 Q110,40 118,70', '#6a4a2a', 3) + leaf(70, 36, 24, 8, -150, '#5ba644') + lychee(76, 86, 24) + lychee(120, 92, 24)
g += Pa('M100,150 Q100,124 124,120 Q150,122 150,150 Q140,176 124,176 Q104,174 100,150 Z', '#f6f1ea') + Pa('M98,152 Q96,136 104,130 L102,170 Q96,164 98,152 Z', '#d9354a') + hi(116, 136, 8, 4, .7)
A['lychee'] = svg(g)

# persimmon 柿子：扁圆橙红色柿子，顶上四片绿叶蒂
def persimmon(x, y, s):
    g = E(0, 0, 44, 36, '#f07a24') + Pa('M-40,-6 Q-30,24 0,30 Q-30,10 -40,-6 Z', '#d9641a') + hi(-18, -10, 10, 6, .35, -20)
    g += ''.join(G(Pa('M0,0 Q12,-6 22,0 Q12,6 0,0 Z', '#4a7a30'), f'rotate({a})') for a in (0, 90, 180, 270)) + R(-3, -14, 6, 12, '#5a4a2a', 2)
    return G(g, f'translate({x},{y-34}) scale({s})'.replace(f'{y-34}', f'{y}'))
A['persimmon'] = svg(persimmon(80, 100, 1.4) + persimmon(146, 146, .9))

# pomegranate 石榴：红石榴带顶冠，切开一半满是红籽
g = Ci(70, 100, 44, '#c0283a') + Pa('M58,58 L62,46 L68,56 L72,44 L78,56 L82,46 L84,60 Z', '#a01e30') + hi(54, 86, 8, 14, .3, 20)
g += Ci(140, 140, 38, '#c0283a') + Ci(140, 140, 33, '#f6e2c8')
random.seed(6)
g += ''.join(Ci(140 + rr * math.cos(a), 140 + rr * math.sin(a), 4.2, random.choice(['#e0304a', '#c8203a', '#f04a5a'])) for a, rr in [(random.uniform(0, 6.28), random.uniform(0, 28)) for _ in range(46)])
A['pomegranate'] = svg(g)

# red-date 红枣：一把暗红发皱的干枣
def date(x, y, s, rot):
    return G(E(0, 0, 22, 15, '#9a1f24') + ''.join(St(f'M{-14+k*7},{-10} q-3,10 2,20', '#6a1418', 1.5) for k in range(4)) + hi(-8, -6, 6, 3, .35) + Ci(22, 0, 2.5, '#6a4a2a'), f'translate({x},{y}) rotate({rot}) scale({s})')
A['red-date'] = svg(date(70, 80, 1.6, -20) + date(130, 90, 1.5, 25) + date(80, 140, 1.4, 10) + date(140, 146, 1.5, -30))

# longan 龙眼：一串黄褐色小圆果，剥开是半透明果肉
g = St('M100,24 Q100,50 80,70 M100,40 Q120,60 130,80 M100,50 Q100,70 104,90', '#6a4a2a', 3)
for x, y in [(70, 84), (98, 98), (130, 90), (82, 118), (114, 124)]:
    g += Ci(x, y, 17, '#c9a060') + hi(x - 6, y - 6, 4, 3, .4)
g += Ci(140, 156, 18, '#f2ecdc', 'opacity=".95"') + Ci(140, 156, 8, '#3a2018') + hi(134, 150, 3, 2, .9) + Pa('M118,162 q8,14 22,14 q-14,-6 -22,-14 Z', '#c9a060')
A['longan'] = svg(g)

A['cashew'] = svg(''.join(cashew(50 + (k % 3) * 50, 76 + (k // 3) * 62, 1.25, k * 60) for k in range(6)))

# pistachio 开心果：外壳裂开，露出绿色果仁
def pist(x, y, s, rot):
    g = Pa('M-16,4 Q-18,-20 -2,-24 L-2,24 Q-14,22 -16,4 Z', '#d6bf8a') + Pa('M16,4 Q18,-20 2,-24 L6,24 Q14,22 16,4 Z', '#c9ae78')
    g += Pa('M-3,-22 Q0,-28 4,-22 L6,-4 Q0,0 -4,-4 Z', '#8aba4a') + Pa('M-2,-20 L3,-20 L4,-8 L-2,-8 Z', '#a8d060')
    g += St('M-12,0 q-1,10 4,18', '#b89a68', 1.5)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
A['pistachio'] = svg(''.join(pist(50 + (k % 3) * 50, 76 + (k // 3) * 62, 1.3, -30 + k * 25) for k in range(6)))

# ============ 香草和香料 ============
# garlic 大蒜：白色蒜头和几瓣蒜
def garlic(x, y, s):
    g = ''
    for dx, c in [(-18, '#efe6d6'), (18, '#efe6d6'), (-8, '#f6f0e4'), (8, '#f6f0e4'), (0, '#fbf8f0')]:
        g += Pa(f'M{dx},-34 Q{dx+18},-10 {dx+14},18 Q{dx},30 {dx-14},18 Q{dx-18},-10 {dx},-34 Z', c)
    g += St('M0,-34 Q0,-50 6,-58', '#d9cfb8', 4) + ''.join(St(f'M{-10+k*5},28 l{-2+k},8', '#c9b89a', 1.5) for k in range(5))
    return G(g, f'translate({x},{y}) scale({s})')
g = garlic(84, 100, 1.6) + G(Pa('M0,-18 Q12,-4 8,14 Q0,18 -8,14 Q-12,-4 0,-18 Z', '#f6f0e4') + St('M0,-18 l2,-6', '#d9cfb8', 2), 'translate(150,150) rotate(30) scale(1.2)')
A['garlic'] = svg(g)

# ginger 姜：疙疙瘩瘩的姜块，一片切面淡黄
g = Pa('M30,120 Q30,96 60,98 Q66,70 90,76 Q100,52 120,64 Q140,60 140,84 Q168,90 162,116 Q156,140 120,136 Q100,152 72,142 Q40,146 30,120 Z', '#d9b07a')
g += ''.join(St(f'M{50+k*20},{108+(k%2)*10} q6,-4 12,0', '#b88a52', 2) for k in range(5)) + hi(70, 104, 10, 4, .3)
g += Ci(150, 160, 16, '#d9b07a') + Ci(150, 160, 13, '#f6e6a0')
A['ginger'] = svg(g)

# chili 辣椒：一把红辣椒和一根青辣椒
def chili(x, y, s, rot, col='#d9302c'):
    return G(Pa('M0,0 Q30,-6 44,14 Q50,30 40,40 Q36,20 6,14 Q-6,10 0,0 Z', col) + Pa('M0,2 q-6,-10 -2,-16 q4,-2 6,6', '#3c8a3a') + hi(22, 4, 10, 3, .4, 20), f'translate({x},{y}) rotate({rot}) scale({s})')
A['chili'] = svg(chili(40, 60, 2.0, 10) + chili(60, 100, 1.8, 0) + chili(90, 130, 1.6, -20, '#3c9a3a'))

# pepper 胡椒：胡椒研磨瓶和黑胡椒粒
g = R(70, 50, 40, 110, '#5a3a24', 12) + R(74, 54, 10, 100, '#7a5236', 5) + E(90, 50, 20, 8, '#4a2a18') + R(84, 26, 12, 24, '#c4cbd0', 4) + E(90, 162, 22, 6, '#3a2418')
random.seed(8)
g += ''.join(Ci(random.uniform(120, 170), random.uniform(146, 170), 4, '#2f2a27') + Ci(0, 0, 0, '#000') for _ in range(18))
A['pepper'] = svg(g)

# green-onion 葱：一把白根绿叶的小葱
g = ''
for i in range(5):
    x = 80 + i * 10
    g += G(R(-5, 0, 10, 50, '#f6f4e6', 5) + R(-5, -100, 10, 104, '#4aa040' if i % 2 else '#3c9036', 5) + ''.join(L(-2 + k * 2, 50, -4 + k * 4, 58, '#c9b89a', 1.2) for k in range(3)), f'translate({x},{110}) rotate({(i-2)*6})')
A['green-onion'] = svg(g)

# mint 薄荷：一枝锯齿边的嫩绿叶子
def mleaf(x, y, l, w, ang, col):
    pts = []
    for k in range(9):
        t = k / 8
        pts.append((l * t, -w * math.sin(math.pi * t) - (2 if k % 2 else 0)))
    d = 'M0,0 ' + ' '.join(f'L{px:.1f},{py:.1f}' for px, py in pts) + ' ' + ' '.join(f'L{l*(1-k/8):.1f},{w*math.sin(math.pi*(1-k/8))+(2 if k%2 else 0):.1f}' for k in range(9)) + ' Z'
    return G(Pa(d, col) + St(f'M2,0 L{l*.9},0', shade(col, -.2), 1.5), f'translate({x},{y}) rotate({ang})')
g = St('M100,180 L100,40', '#5a9a3a', 4)
for k in range(4):
    y = 150 - k * 30
    g += mleaf(100, y, 44 - k * 6, 18 - k * 2, -150 + k * 8, '#5ec060') + mleaf(100, y - 8, 44 - k * 6, 18 - k * 2, -30 - k * 8, '#4ab04e')
A['mint'] = svg(g)

# cinnamon 肉桂：一捆卷起来的肉桂棒
g = ''
for i, (x, y, rot) in enumerate([(84, 96, -20), (110, 104, -12), (96, 124, -16)]):
    g += G(R(-60, -10, 120, 20, '#a8582a', 8) + R(-60, -10, 120, 6, '#c06a3a', 4) + Ci(60, 0, 10, '#8a4220') + St('M60,-6 a6,6 0 1,1 -4,8', '#c87a4a', 2), f'translate({x},{y}) rotate({rot})')
g += R(84, 88, 10, 48, '#d9453a', 3, 'transform="rotate(-16 89 112)"')
A['cinnamon'] = svg(g)

# sesame 芝麻：木勺里的白芝麻和一小堆黑芝麻
random.seed(12)
g = E(80, 110, 46, 30, '#c58b54') + E(80, 106, 40, 24, '#a8703e') + R(120, 102, 70, 12, '#c58b54', 6, 'transform="rotate(-10 120 108)"')
g += ''.join(E(random.uniform(50, 110), random.uniform(92, 120), 3.2, 1.8, '#f6ead0', f'transform="rotate({random.uniform(0,180):.0f} 80 106)"') for _ in range(50))
g += ''.join(E(random.uniform(120, 170), random.uniform(150, 170), 3, 1.7, '#2f2a27') for _ in range(40))
A['sesame'] = svg(g)

# curry 咖喱：一盘咖喱饭，黄色咖喱配土豆胡萝卜
g = E(100, 136, 84, 30, '#d9dcde') + E(100, 132, 84, 30, '#ffffff')
g += Pa('M30,130 Q40,100 90,100 L100,130 Q60,150 30,130 Z', '#fbf8f0') + ''.join(E(40 + k * 9, 116 + (k % 3) * 6, 4, 2.5, '#f2ece0') for k in range(6))
g += Pa('M90,100 Q150,96 170,124 Q150,152 100,148 Q90,130 90,100 Z', '#e0a020')
g += R(110, 112, 14, 12, '#f0d080', 3) + R(140, 120, 12, 10, '#f08a24', 2) + R(124, 132, 12, 12, '#f0d080', 3) + R(150, 108, 10, 10, '#c06a3a', 2)
g += steam(110, 92, 3, 16, '#c4cbd0', .6)
A['curry'] = svg(g)

# basil 罗勒：大片光亮的绿叶
g = St('M100,180 L100,60', '#4a8a3a', 4)
for k in range(3):
    y = 150 - k * 34
    g += leaf(100, y, 56 - k * 8, 24 - k * 3, -160 + k * 10, '#3c9a3a') + leaf(100, y - 6, 56 - k * 8, 24 - k * 3, -20 - k * 10, '#4aaa44')
g += leaf(100, 58, 30, 14, -90, '#5aba50')
A['basil'] = svg(g)

# coriander 香菜：一把细茎、锯齿圆叶的香菜
g = ''
for i in range(5):
    a = -30 + i * 15
    br = St('M0,0 Q4,-60 0,-110', '#7ab05a', 2.5)
    for k in range(3):
        y = -50 - k * 22
        br += ''.join(Ci((-1) ** j * (10 + j * 4), y - j * 4, 8, '#4aa040' if (k + j) % 2 else '#5ab04a') for j in range(2))
    g += G(br, f'translate(100,176) rotate({a})')
A['coriander'] = svg(g)

# star-anise 八角：八个角的星形棕色香料
def anise(x, y, s, rot):
    g = ''
    for k in range(8):
        g += G(Pa('M0,0 Q-8,-14 0,-34 Q8,-14 0,0 Z', '#7a3a1a') + E(0, -16, 3, 6, '#c08a4a'), f'rotate({k*45})')
    return G(g + Ci(0, 0, 5, '#5a2a10'), f'translate({x},{y}) rotate({rot}) scale({s})')
A['star-anise'] = svg(anise(80, 96, 1.6, 0) + anise(144, 146, 1.0, 20))

# mustard 芥末：黄色芥末挤瓶和一小碟芥末
g = Pa('M70,170 L70,80 Q70,64 90,64 Q110,64 110,80 L110,170 Z', '#f3c234') + Pa('M84,64 L96,64 L94,30 L86,30 Z', '#e0a820') + Pa('M88,30 L92,30 L90,18 Z', '#e0a820')
g += R(74, 100, 32, 30, '#ffffff', 3) + Ci(90, 115, 8, '#f3c234') + hi(78, 120, 3, 20, .4)
g += E(150, 160, 30, 10, '#d9dcde') + E(150, 156, 30, 10, '#ffffff') + E(150, 154, 16, 5, '#d9b830') + St('M138,150 q12,-10 24,0', '#e0c040', 4)
A['mustard'] = svg(g)

# parsley 欧芹：卷曲的深绿叶子
random.seed(14)
g = ''.join(St(f'M100,180 Q{100+k*6},120 {100+k*14},{70+abs(k)*8}', '#5a9a3a', 3) for k in range(-2, 3))
g += ''.join(Ci(100 + k * 14 + random.uniform(-14, 14), 70 + abs(k) * 8 + random.uniform(-16, 10), random.uniform(8, 13), random.choice(['#2f7a2a', '#3c8a34', '#4a9a3a'])) for k in range(-2, 3) for _ in range(5))
A['parsley'] = svg(g)

# rosemary 迷迭香：细长枝条上排满针状叶
g = ''
for i, (x, rot) in enumerate([(80, -15), (104, 0), (128, 15)]):
    br = St('M0,60 L0,-80', '#6a5a3a', 3) + ''.join(L(0, -70 + k * 9, (-1) ** k * 16, -78 + k * 9, '#4a7a4a' if k % 2 else '#5a8a5a', 3.5) for k in range(14))
    g += G(br, f'translate({x},110) rotate({rot})')
A['rosemary'] = svg(g)

# sichuan-pepper 花椒：一簇簇红褐色、裂开的小粒
random.seed(15)
g = ''
for cx, cy in [(70, 90), (130, 96), (100, 140)]:
    g += St(f'M{cx},{cy-30} L{cx},{cy}', '#6a4a2a', 2)
    for _ in range(7):
        x, y = cx + random.uniform(-22, 22), cy + random.uniform(-18, 18)
        g += Ci(x, y, 8, '#a8302a') + ''.join(Ci(x + 4 * math.cos(a), y + 4 * math.sin(a), 1.2, '#7a1a18') for a in (0, 2, 4)) + Pa(f'M{x-3},{y-7} q3,-4 6,0', 'none', 'stroke="#2f2a27" stroke-width="2"')
g += leaf(150, 50, 30, 9, -30, '#4a8a3a')
A['sichuan-pepper'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
