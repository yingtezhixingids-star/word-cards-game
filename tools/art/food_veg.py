from flat import *
from fig import *
import os, sys, random

A = {}

def tomato(x, y, s=1):
    g = Ci(x, y, 30 * s, '#e0392f') + Pa(f'M{x+8*s},{y-28*s} A30,30 0 0,1 {x+28*s},{y+10*s} Q{x+14*s},{y-8*s} {x+8*s},{y-28*s} Z'.replace('A30,30', f'A{30*s},{30*s}'), '#c02a22')
    g += hi(x - 12 * s, y - 10 * s, 6 * s, 9 * s, .45, 30)
    g += ''.join(leaf(x, y - 26 * s, 14 * s, 4 * s, a, '#3c8a3a') for a in (-160, -110, -60, -20, 30)) + R(x - 2 * s, y - 36 * s, 4 * s, 10 * s, '#3c8a3a', 2)
    return g

def potato(x, y, s=1, rot=0):
    g = E(0, 0, 36, 26, '#c9a06a') + E(8, 6, 26, 16, '#b88a52') + ''.join(Ci(-14 + k * 11, -6 + (k % 2) * 12, 2, '#9a7040') for k in range(4)) + hi(-12, -10, 10, 5, .3, -10)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def onion(x, y, s=1, col='#c98a4a'):
    g = Pa('M0,-40 Q8,-30 30,-10 Q42,14 24,30 Q0,42 -24,30 Q-42,14 -30,-10 Q-8,-30 0,-40 Z', col)
    g += Pa('M0,-40 Q8,-30 30,-10 Q42,14 24,30 Q12,36 0,38 Q20,0 0,-40 Z', shade(col, -.15))
    g += ''.join(St(f'M0,-36 Q{k*8},0 {k*5},36', shade(col, -.25), 1.5) for k in (-2, -1, 1, 2))
    g += St('M0,-40 q-2,-10 4,-16', '#8a6a3a', 3) + St('M-6,36 q6,8 12,0', '#e6d4b4', 2)
    return G(g, f'translate({x},{y}) scale({s})')

def leafy(x, y, s, col, vein, n=5):
    g = ''
    for i in range(n):
        a = -90 + (i - (n - 1) / 2) * 22
        g += G(Pa('M0,0 Q-22,-30 -12,-70 Q0,-84 12,-70 Q22,-30 0,0 Z', col if i % 2 else shade(col, -.08)) + St('M0,0 L0,-72', vein, 3), f'rotate({a+90})')
    return G(g, f'translate({x},{y}) scale({s})')

def pod(x, y, s, rot, col='#7cc04a', peas=5, open_=True):
    g = Pa('M-50,0 Q-30,-20 20,-16 Q50,-12 56,0 Q40,16 0,16 Q-36,14 -50,0 Z', col) + Pa('M-50,0 Q-30,-6 20,-4 Q50,-2 56,0 Q40,16 0,16 Q-36,14 -50,0 Z', shade(col, -.12))
    if open_: g += Pa('M-44,-2 Q0,-12 50,-2 Q0,4 -44,-2 Z', '#d6eeb0') + ''.join(Ci(-32 + k * 16, -3, 7, '#8ccc4a') + hi(-34 + k * 16, -6, 2, 2, .6) for k in range(peas))
    g += St('M-50,0 q-8,-4 -10,-12', '#5a8a3a', 3)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

# ============ 蔬菜（一） ============
# vegetable 蔬菜：菜篮子里装满各种蔬菜
g = Pa('M30,110 L170,110 L156,176 L44,176 Z', '#c58b54') + ''.join(L(34 + i * 2.4, 120 + i * 12, 166 - i * 2.4, 120 + i * 12, '#a8703e', 2.5) for i in range(5))
g += broccoli(64, 92, .9) + tomato(108, 96, .75) + carrot(140, 84, .8, 30) + Ci(88, 108, 14, '#7a4fa0') + leaf(150, 108, 30, 10, -30, '#5ba644')
g += St('M40,110 Q100,30 160,110', '#a8703e', 6)
A['vegetable'] = svg(g)

A['tomato'] = svg(tomato(100, 108, 2.0))
A['potato'] = svg(potato(80, 110, 1.6, -10) + potato(140, 140, 1.0, 20))
g = carrot(76, 104, 1.6, 20) + carrot(130, 110, 1.4, -15)
A['carrot'] = svg(g)
A['onion'] = svg(onion(80, 110, 1.4) + G(Ci(0, 0, 30, '#f6efe0') + ''.join(Ci(0, 0, 30 - k * 6, 'none', 'stroke="#d9cfb8" stroke-width="2"') for k in range(5)), 'translate(150,140) scale(1,.9)'))

# cabbage 卷心菜：圆圆的绿色卷心菜
g = Ci(100, 108, 62, '#7fbf5a') + Ci(100, 112, 46, '#b8e090') + Ci(104, 116, 30, '#d4efb4')
g += ''.join(St(f'M100,{150} Q{100+k*20},{110} {100+k*30},{60}', '#9fd07a', 3) for k in (-2, -1, 1, 2))
g += Pa('M38,108 Q40,60 90,46 Q60,80 70,140 Q46,140 38,108 Z', '#6aaa4a') + Pa('M162,108 Q160,60 110,46 Q140,80 130,140 Q154,140 162,108 Z', '#6aaa4a')
A['cabbage'] = svg(g)

# cucumber 黄瓜：带小刺的长黄瓜和切片
g = G(R(-80, -16, 160, 32, '#3c8a3a', 16) + R(-76, -12, 150, 10, '#5aaa4a', 6) + ''.join(Ci(-60 + k * 16, (k % 2) * 8 - 2, 2, '#c4e8a0') for k in range(8)) + Pa('M76,-8 q14,-2 14,8 q-2,8 -14,6 Z', '#f3c234'), 'translate(96,90) rotate(-15)')
g += Ci(70, 150, 22, '#3c8a3a') + Ci(70, 150, 18, '#d6f0b8') + ''.join(Ci(70 + 8 * math.cos(a), 150 + 8 * math.sin(a), 2, '#f6f8e8') for a in [k * math.pi / 3 for k in range(6)])
g += Ci(120, 156, 20, '#3c8a3a') + Ci(120, 156, 16, '#d6f0b8')
A['cucumber'] = svg(g)

# corn 玉米：剥开叶子的黄色玉米棒
g = G(Pa('M-26,60 Q-60,20 -40,-30 Q-20,10 -6,56 Z', '#8cc06a') + Pa('M26,60 Q60,20 40,-30 Q20,10 6,56 Z', '#7cb05a') +
      E(0, -10, 26, 70, '#f3c234') + ''.join(Ci(-15 + c * 10, -70 + r_ * 11, 4.5, '#f8d860' if (r_ + c) % 2 else '#f0c030') for r_ in range(13) for c in range(4) if (abs(-15 + c * 10) < 26 * math.sqrt(max(0, 1 - ((-70 + r_ * 11 + 10) / 72) ** 2)))) +
      Pa('M-30,64 Q-46,30 -30,0 Q-14,30 0,64 Z', '#6aa04a') + Pa('M30,64 Q46,30 30,0 Q14,30 0,64 Z', '#5a9a3a'), 'translate(100,100) rotate(20)')
A['corn'] = svg(g)

# eggplant 茄子：紫色长茄子
def eggplant(x, y, s, rot):
    g = Pa('M-14,-50 Q14,-56 18,-30 Q24,20 16,50 Q4,74 -12,62 Q-30,40 -24,0 Q-26,-40 -14,-50 Z', '#5a2f7a') + Pa('M8,-48 Q22,-30 22,0 Q24,30 16,50 Q8,66 0,66 Q20,20 8,-48 Z', '#47215f')
    g += hi(-12, -10, 4, 22, .35) + Pa('M-20,-46 Q0,-66 20,-46 Q10,-40 0,-44 Q-10,-40 -20,-46 Z', '#5a8a3a') + R(-3, -66, 6, 18, '#5a8a3a', 3)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
A['eggplant'] = svg(eggplant(84, 104, 1.3, -25) + eggplant(136, 116, 1.0, 15))

# pumpkin 南瓜：橙色大南瓜
g = ''
for i, (dx, rx) in enumerate([(-36, 30), (36, 30), (-18, 32), (18, 32), (0, 30)]):
    g += E(100 + dx, 118, rx, 50, '#f08a24' if i % 2 else '#e07a1a')
g += Pa('M96,70 q-4,-20 10,-30 l6,6 q-10,8 -6,24 Z', '#6a8a3a') + leaf(110, 64, 26, 9, -30, '#5ba644') + hi(80, 100, 6, 18, .3)
A['pumpkin'] = svg(g)

A['broccoli'] = svg(broccoli(100, 96, 2.2))

# lettuce 生菜：一颗嫩绿的生菜，叶子边缘波浪
g = ''
for i, (dx, dy, s, c) in enumerate([(-34, 10, 1.2, '#9fd07a'), (34, 10, 1.2, '#9fd07a'), (-16, 0, 1.3, '#b8e090'), (16, 0, 1.3, '#b8e090'), (0, 10, 1.1, '#d4efb4')]):
    g += G(Pa('M0,40 Q-40,20 -34,-20 Q-30,-40 -16,-30 Q-10,-48 4,-36 Q16,-48 24,-30 Q40,-30 34,0 Q30,30 0,40 Z', c) + St('M0,38 L0,-26', '#e6f6d6', 3), f'translate({100+dx},{112+dy}) scale({s})')
A['lettuce'] = svg(g)

# spinach 菠菜：一把带红根的深绿菠菜
g = ''
for i in range(6):
    a = -40 + i * 16
    g += G(Pa('M0,0 L0,-50 Q-22,-70 -16,-100 Q0,-112 16,-100 Q22,-70 0,-50 Z', '#2f7a3a' if i % 2 else '#3c8a3a') + St('M0,0 L0,-96', '#7cc06a', 2.5), f'translate(100,170) rotate({a})')
g += R(92, 156, 16, 20, '#d96a8a', 6) + R(86, 140, 28, 10, '#c58b54', 3)
A['spinach'] = svg(g)

# celery 芹菜：一束浅绿色芹菜杆，顶上带叶子
g = ''
for i in range(5):
    x = 72 + i * 14
    g += R(x - 7, 60 + abs(i - 2) * 6, 14, 116, '#a8d878' if i % 2 else '#9acc6a', 7) + L(x - 2, 70, x - 2, 170, '#c8e8a0', 2)
    g += leaf(x, 60 + abs(i - 2) * 6, 26, 10, -90 + (i - 2) * 25, '#5aaa3a') + leaf(x, 70 + abs(i - 2) * 6, 20, 8, -60 + (i - 2) * 30, '#6abb4a')
A['celery'] = svg(g)

# green-pepper 青椒：一个绿色灯笼椒
g = Pa('M100,58 Q60,50 50,80 Q40,120 60,150 Q80,170 100,160 Q120,170 140,150 Q160,120 150,80 Q140,50 100,58 Z', '#3c8a3a')
g += Pa('M100,58 Q120,52 140,64 Q150,100 140,150 Q130,164 118,164 Q132,110 100,58 Z', '#2f7030') + hi(72, 96, 7, 22, .35)
g += Pa('M90,58 Q100,48 110,58 Q104,62 100,60 Q96,62 90,58 Z', '#5a8a3a') + St('M100,52 q2,-14 12,-20', '#5a8a3a', 6)
A['green-pepper'] = svg(g)

# sweet-potato 红薯：紫红皮红薯，一个掰开露出橙黄心
def sp(x, y, s, rot, cut=False):
    g = Pa('M-60,0 Q-50,-24 0,-26 Q50,-24 60,0 Q50,24 0,26 Q-50,24 -60,0 Z', '#a8445a') + Pa('M-56,6 Q0,30 56,6 Q50,24 0,26 Q-50,24 -56,6 Z', '#8a3048')
    g += St('M60,0 l12,-2', '#8a3048', 3) + St('M-60,0 l-10,4', '#8a3048', 3) + ''.join(L(-40 + k * 20, -10, -36 + k * 20, -4, '#7a2a40', 1.5) for k in range(5))
    if cut: g += E(60, 0, 10, 24, '#f5a43a') + E(60, 0, 6, 18, '#f8c060')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
A['sweet-potato'] = svg(sp(90, 90, 1.1, -15) + sp(100, 150, .9, 5, True))

# ============ 蔬菜（二） ============
A['pea'] = svg(pod(100, 104, 1.5, -15))
# bean 豆子：一把绿色长豆角
g = ''.join(G(Pa('M-70,0 Q-40,-10 0,-8 Q40,-6 70,4 Q40,12 0,10 Q-40,10 -70,0 Z', '#5aa04a' if i % 2 else '#6ab05a') + ''.join(E(-50 + k * 20, 1, 6, 4, shade('#5aa04a', .15)) for k in range(6)), f'translate(100,{70+i*22}) rotate({-15+i*8})') for i in range(5))
A['bean'] = svg(g)

# radish 萝卜：白萝卜，绿叶子
g = G(Pa('M-26,-40 Q0,-50 26,-40 Q34,20 10,70 Q2,88 -2,90 Q-6,80 -12,70 Q-34,20 -26,-40 Z', '#f6f2ea') + Pa('M10,-46 Q30,-40 28,0 Q24,40 10,70 Q2,88 -2,90 Q16,40 10,-46 Z', '#e6e0d4') +
      Pa('M-26,-40 Q0,-50 26,-40 L26,-20 Q0,-30 -26,-20 Z', '#d0e8b0') + ''.join(L(-20, -10 + k * 18, -12, -8 + k * 18, '#d9d0c0', 1.5) for k in range(4)) +
      leaf(0, -44, 50, 14, -110, '#5aaa3a') + leaf(0, -44, 50, 14, -70, '#4a9a3a') + leaf(0, -44, 44, 12, -90, '#6abb4a'), 'translate(100,100) rotate(-15)')
A['radish'] = svg(g)

# bok-choy 小白菜：白色菜帮、绿色叶子
g = ''
for i in range(5):
    a = -30 + i * 15
    g += G(Pa('M-10,0 Q-14,-40 -8,-60 L8,-60 Q14,-40 10,0 Z', '#eef6e0') + Pa('M-8,-56 Q-34,-80 -20,-124 Q0,-136 20,-124 Q34,-80 8,-56 Z', '#3c8a3a' if i % 2 else '#4a9a40') + St('M0,-56 L0,-120', '#a8d878', 2.5), f'translate(100,176) rotate({a})')
A['bok-choy'] = svg(g)

# cauliflower 菜花：白色花球，外面一圈绿叶
g = leaf(100, 140, 70, 24, -160, '#5aaa3a') + leaf(100, 140, 70, 24, -20, '#5aaa3a') + leaf(100, 150, 60, 20, -120, '#4a9a3a') + leaf(100, 150, 60, 20, -60, '#4a9a3a')
random.seed(11)
for k in range(26):
    a = random.uniform(0, 2 * math.pi); rr = random.uniform(0, 40)
    g += Ci(100 + rr * math.cos(a), 104 + rr * .8 * math.sin(a), random.uniform(10, 15), random.choice(['#f6f0dc', '#efe6c8', '#fbf6e8']))
A['cauliflower'] = svg(g)

# zucchini 西葫芦：长条深绿西葫芦和切片
g = G(R(-74, -18, 148, 36, '#3a7a2a', 18) + ''.join(L(-60, -10 + k * 7, 60, -10 + k * 7, '#5a9a3a', 2) for k in range(4)) + R(-86, -6, 16, 12, '#8a9a5a', 4), 'translate(100,90) rotate(-12)')
g += Ci(84, 150, 22, '#3a7a2a') + Ci(84, 150, 18, '#eaf4c8') + ''.join(Ci(84 + 8 * math.cos(a), 150 + 8 * math.sin(a), 1.8, '#d6e6a8') for a in [k * math.pi / 4 for k in range(8)])
A['zucchini'] = svg(g)

# leek 韭葱：粗长白杆，上面深绿扁叶
g = G(R(-14, -10, 28, 100, '#f6f4e6', 12) + R(-14, -10, 28, 30, '#d0e8a0', 6) + R(-12, 86, 24, 8, '#e6dcc4', 3) + ''.join(L(-8 + k * 4, 90, -10 + k * 6, 100, '#c9b89a', 1.5) for k in range(5)) +
      Pa('M-14,-8 L-30,-80 L-18,-82 L-2,-10 Z', '#3c7a3a') + Pa('M14,-8 L34,-76 L22,-80 L2,-10 Z', '#4a8a40') + Pa('M-4,-10 L-6,-90 L6,-90 L4,-10 Z', '#5a9a4a'), 'translate(100,96) rotate(15)')
A['leek'] = svg(g)

# bean-sprouts 豆芽：碗里一堆白色带黄头的豆芽
random.seed(4)
g = bowl(100, 120, 140, pattern='#3c7fc1', fill='#f6f6ee')
for k in range(22):
    x = random.uniform(44, 156); y = random.uniform(70, 116)
    a = random.uniform(-60, 60)
    g += G(St('M0,0 q6,14 0,28', '#f6f2e0', 3) + E(0, -2, 4, 5, '#f3d03a'), f'translate({x},{y}) rotate({a})')
A['bean-sprouts'] = svg(g)

# lotus-root 莲藕：一节节的莲藕和切面上的孔
g = G(E(-46, 0, 34, 22, '#e8d4b8') + E(10, 0, 30, 20, '#e2ccae') + E(60, 0, 26, 18, '#e8d4b8') + R(-14, -4, 6, 8, '#c9b090') + R(36, -4, 6, 8, '#c9b090'), 'translate(90,80) rotate(-10)')
g += Ci(110, 146, 32, '#e8d4b8') + Ci(110, 146, 28, '#f6ecdc') + Ci(110, 146, 6, '#c9b090') + ''.join(Ci(110 + 16 * math.cos(a), 146 + 16 * math.sin(a), 5, '#c9b090') for a in [k * math.pi / 4 for k in range(8)])
A['lotus-root'] = svg(g)

# bamboo-shoot 竹笋：一层层黄褐色笋壳包着的竹笋
g = Pa('M100,30 Q130,90 132,150 Q120,176 100,176 Q80,176 68,150 Q70,90 100,30 Z', '#e6c87a')
for k in range(5):
    y = 60 + k * 24
    g += Pa(f'M{100},{y-30} Q{124+k*2},{y} {130+k*1},{y+20} Q{110},{y+10} {100},{y+16} Z', '#b88a4a' if k % 2 else '#a07a3a')
    g += Pa(f'M{100},{y-30} Q{76-k*2},{y} {70-k*1},{y+20} Q{90},{y+10} {100},{y+16} Z', '#c89a5a' if k % 2 else '#b88a4a')
g += E(100, 174, 32, 6, '#f6ecd0')
A['bamboo-shoot'] = svg(g)

# asparagus 芦笋：一捆绿色细长芦笋，用皮筋扎着
g = ''
for i in range(7):
    x = 70 + i * 10
    g += R(x - 4, 50 + abs(i - 3) * 4, 8, 120, '#6aaa4a' if i % 2 else '#5a9a3a', 4) + Pa(f'M{x-5},{56+abs(i-3)*4} Q{x},{36+abs(i-3)*4} {x+5},{56+abs(i-3)*4} Z', '#7a6aa0')
    g += ''.join(Pa(f'M{x-4},{80+k*22} l-3,-6 l6,2 Z', '#4a8a3a') for k in range(3))
g += R(64, 130, 72, 10, '#d9453a', 3)
A['asparagus'] = svg(g)

# yam 山药：长条棕皮山药，切口白色黏滑
g = G(R(-80, -14, 160, 28, '#b8946a', 14) + ''.join(L(-70 + k * 16, -10, -66 + k * 16, 10, '#8a6a4a', 1.2) for k in range(10)) + ''.join(Ci(-70 + k * 14, -6 + (k % 3) * 5, 1.5, '#6a4a2a') for k in range(11)) +
      E(80, 0, 6, 14, '#fbf8f0'), 'translate(96,90) rotate(-20)')
g += G(R(-30, -12, 60, 24, '#b8946a', 12) + E(-30, 0, 6, 12, '#fbf8f0') + E(30, 0, 6, 12, '#fbf8f0'), 'translate(110,150) rotate(5)')
A['yam'] = svg(g)

# kale 羽衣甘蓝：深绿卷边的叶子
g = ''
for i, a in enumerate((-30, -10, 10, 30)):
    leafd = 'M0,0 ' + ' '.join(f'Q{-18-(k%2)*8},{-20-k*20} {-10},{-30-k*20}' for k in range(4)) + ' L0,-110 ' + ' '.join(f'Q{18+(k%2)*8},{-90+k*20} {10},{-80+k*20}' for k in range(4)) + ' Z'
    g += G(Pa(leafd, '#2f6a3a' if i % 2 else '#3a7a44') + St('M0,0 L0,-104', '#8ac07a', 3), f'translate(100,176) rotate({a})')
A['kale'] = svg(g)

# beetroot 甜菜根：深紫红圆根，切开有圈纹
g = Ci(80, 110, 42, '#8a1f3a') + Pa('M80,152 q4,14 -2,26', 'none', 'stroke="#8a1f3a" stroke-width="4"') + hi(66, 96, 8, 12, .3)
g += leaf(80, 70, 50, 14, -110, '#4a8a3a') + leaf(80, 70, 50, 14, -70, '#3c7a30') + St('M80,70 L72,30 M80,70 L92,32', '#b0304a', 3)
g += Ci(146, 150, 26, '#8a1f3a') + ''.join(Ci(146, 150, 22 - k * 5, '#c0305a' if k % 2 else '#a02448') for k in range(4))
A['beetroot'] = svg(g)

# okra 秋葵：绿色五棱长角，切面像星星
def okra(x, y, s, rot):
    g = Pa('M-10,-60 Q12,-62 14,-40 Q16,0 4,50 Q0,64 -2,64 Q-6,40 -14,0 Q-18,-40 -10,-60 Z', '#5aaa3a') + St('M0,-58 Q4,0 0,62', '#4a9030', 2) + St('M-8,-50 Q-8,0 -4,50', '#7cc05a', 2)
    g += Pa('M-12,-60 Q0,-72 12,-60 Q4,-64 0,-62 Q-4,-64 -12,-60 Z', '#3c7a30') + R(-3, -76, 6, 14, '#3c7a30', 3)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
g = okra(70, 96, 1.2, -20) + okra(110, 90, 1.1, 10)
g += G(Pa(''.join(('M' if k == 0 else 'L') + f'{20*math.cos(k*math.pi/5-math.pi/2):.1f},{20*math.sin(k*math.pi/5-math.pi/2)*(1 if k%2==0 else .6):.1f} ' for k in range(10)) + 'Z', '#5aaa3a') + Ci(0, 0, 11, '#d6eeb0') + ''.join(Ci(7 * math.cos(k * 1.2566), 7 * math.sin(k * 1.2566), 2.5, '#f6f6e0') for k in range(5)), 'translate(156,150)')
A['okra'] = svg(g)

# artichoke 洋蓟：一层层尖鳞片的灰绿色花苞
g = ''
for row in range(5):
    y = 150 - row * 22
    n = 5 - row // 2
    for k in range(n):
        x = 100 + (k - (n - 1) / 2) * (22 - row * 2)
        g += Pa(f'M{x-14},{y} Q{x-12},{y-26} {x},{y-34} Q{x+12},{y-26} {x+14},{y} Q{x},{y+6} {x-14},{y} Z', '#6a9a6a' if (k + row) % 2 else '#7aaa78')
        g += Pa(f'M{x-8},{y-24} Q{x},{y-36} {x+8},{y-24} Q{x},{y-30} {x-8},{y-24} Z', '#8a6a9a')
g += R(94, 152, 12, 26, '#6a9a6a', 4)
A['artichoke'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
