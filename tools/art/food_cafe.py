from flat import *
from fig import *
import os, sys, random

A = {}
SK = P['skin']

def plate(cx, cy, rx):
    return E(cx, cy + 4, rx, rx * .26, '#d9dcde') + E(cx, cy, rx, rx * .26, '#ffffff')

def coffee_cup(cx, cy, w, liquid='#6a3a1a', col='#ffffff', saucer=True, foam=None):
    g = ''
    if saucer: g += E(cx, cy + w * .62, w * .9, w * .18, '#d9dcde') + E(cx, cy + w * .58, w * .9, w * .18, col)
    g += St(f'M{cx+w/2-3},{cy+w*.1} q{w*.32},0 {w*.3},{w*.22} q-2,{w*.2} {-w*.32},{w*.18}', col, w * .1)
    g += Pa(f'M{cx-w/2},{cy} L{cx+w/2},{cy} Q{cx+w/2},{cy+w*.62} {cx},{cy+w*.62} Q{cx-w/2},{cy+w*.62} {cx-w/2},{cy} Z', col)
    g += Pa(f'M{cx+w*.2},{cy+w*.04} Q{cx+w*.45},{cy+w*.1} {cx+w*.3},{cy+w*.5} Q{cx+w*.15},{cy+w*.6} {cx},{cy+w*.62} Q{cx+w*.4},{cy+w*.4} {cx+w*.2},{cy+w*.04} Z', '#e6ecef')
    g += E(cx, cy, w / 2, w * .13, liquid)
    if foam: g += E(cx, cy, w * .42, w * .1, foam)
    return g

def tall_glass(x, y, w, h, fill, level=.85, layers=None):
    g = Pa(f'M{x},{y} L{x+w},{y} L{x+w-4},{y+h} L{x+4},{y+h} Z', '#eef6fa', 'opacity=".9"')
    top = y + h * (1 - level)
    if layers:
        yy = y + h
        for c, frac in layers:
            hh = h * level * frac
            g += Pa(f'M{x+2},{yy-hh} L{x+w-2},{yy-hh} L{x+w-4},{yy} L{x+4},{yy} Z', c); yy -= hh
    else:
        g += Pa(f'M{x+1},{top} L{x+w-1},{top} L{x+w-4},{y+h} L{x+4},{y+h} Z', fill)
    g += R(x + 5, y + 6, 5, h - 12, '#ffffff', 2, 'opacity=".45"')
    return g

def ice_cube(x, y, s, rot=0):
    return G(R(-s / 2, -s / 2, s, s, '#e8f6fc', 3, 'opacity=".85"') + R(-s / 2, -s / 2, s, s, 'none', 3, 'stroke="#bfe0ef" stroke-width="1.5"') + R(-s / 3, -s / 3, s / 3, s / 5, '#ffffff', 1), f'translate({x},{y}) rotate({rot})')

def straw(x1, y1, x2, y2, col='#e2463b'):
    return L(x1, y1, x2, y2, col, 6) + L(x1, y1, x2, y2, '#ffffff', 1.5)

def takeaway(cx, base, w, h, col='#ffffff', sleeve='#c58b54', lid='#f4f1ea'):
    g = Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w*.38},{base} L{cx-w*.38},{base} Z', col)
    g += Pa(f'M{cx-w*.46},{base-h*.65} L{cx+w*.46},{base-h*.65} L{cx+w*.42},{base-h*.3} L{cx-w*.42},{base-h*.3} Z', sleeve)
    g += R(cx - w / 2 - 4, base - h - 10, w + 8, 12, lid, 4) + R(cx - w / 2 + 4, base - h - 16, w - 8, 8, lid, 3)
    return g

def bean(x, y, s, rot=0):
    return G(E(0, 0, 9, 12, '#5a3a24') + St('M0,-10 q-4,10 0,20', '#3a2214', 2), f'translate({x},{y}) rotate({rot}) scale({s})')

def no_sign(x, y, r):
    return Ci(x, y, r, 'none', 'stroke="#d9453a" stroke-width="5"') + L(x - r * .7, y + r * .7, x + r * .7, y - r * .7, '#d9453a', 5)

def sugar_cube(x, y, s):
    return Pa(f'M{x},{y} L{x+s},{y-s*.4} L{x+s*2},{y} L{x+s},{y+s*.4} Z', '#ffffff') + Pa(f'M{x},{y} L{x+s},{y+s*.4} L{x+s},{y+s*1.4} L{x},{y+s} Z', '#f2efe8') + Pa(f'M{x+s},{y+s*.4} L{x+s*2},{y} L{x+s*2},{y+s} L{x+s},{y+s*1.4} Z', '#e2ddd3')

def chair(x, y, col='#8a5a35', flip=1):
    return R(x - 14, y, 28, 6, col, 2) + R(x + flip * 10, y - 36, 5, 40, col, 2) + R(x - 12, y + 6, 4, 30, col) + R(x + 8, y + 6, 4, 30, col)

def sandwich(x, y, s):
    g = Pa('M-50,20 L50,20 L0,-40 Z', '#e8c890') + Pa('M-46,16 L46,16 L0,-34 Z', '#fbf3e0')
    g += Pa('M-54,30 L54,30 L50,20 L-50,20 Z', '#5ba644') + Pa('M-54,38 L54,38 L54,30 L-54,30 Z', '#e98a86') + Pa('M-54,44 L54,44 L54,38 L-54,38 Z', '#f3c234')
    g += Pa('M-54,44 L54,44 L50,56 L-50,56 Z', '#e8c890')
    return G(g, f'translate({x},{y}) scale({s})')

# ================= 熟食店 =================
# salad 沙拉：一大碗生菜番茄黄瓜沙拉
random.seed(61)
g = bowl(100, 110, 150, pattern='#5ba644')
g += Pa('M28,110 Q40,66 100,62 Q160,66 172,110 Z', '#8cc06a')
g += ''.join(leaf(random.uniform(40, 160), random.uniform(74, 104), 26, 10, random.uniform(-180, 0), random.choice(['#5aaa3a', '#7cc05a', '#a8d878'])) for _ in range(10))
g += Ci(70, 88, 9, '#e0392f') + Ci(122, 80, 9, '#e0392f') + Ci(100, 96, 9, '#d6f0b8') + Ci(100, 96, 9, 'none', 'stroke="#3c8a3a" stroke-width="2"') + Ci(140, 96, 6, '#f3c234')
A['salad'] = svg(g)

# olive 橄榄：小碟里的绿橄榄，旁边一枝橄榄叶
g = E(96, 150, 60, 16, '#d9dcde') + E(96, 146, 60, 16, '#ffffff')
for x, y in [(70, 130), (96, 126), (122, 130), (84, 112), (110, 110)]:
    g += E(x, y, 14, 18, '#8aa83a') + Ci(x - 2, y - 2, 5, '#d9453a') + hi(x - 6, y - 8, 3, 4, .5)
g += St('M130,60 Q150,40 180,36', '#6a5a3a', 3) + leaf(146, 50, 26, 6, -30, '#7a9a6a') + leaf(160, 42, 24, 6, 20, '#8aaa7a') + E(150, 64, 8, 10, '#5a6a2a')
A['olive'] = svg(g)

# pickles 腌菜：玻璃罐里泡着黄瓜条和辣椒，小碟腌菜
g = R(30, 46, 84, 126, '#e8f4e0', 12, 'opacity=".9"') + R(26, 34, 92, 18, '#c4cbd0', 5)
g += Pa('M32,80 L112,80 L112,166 Q112,172 104,172 L40,172 Q32,172 32,166 Z', '#cfe2a8', 'opacity=".8"')
g += ''.join(R(40 + k * 16, 90 + (k % 2) * 10, 12, 70, '#6a9a3a', 5) for k in range(4)) + Pa('M60,100 q16,4 10,40 q-8,-4 -10,-40 Z', '#d9302c') + Ci(90, 130, 5, '#f3c234')
g += E(152, 160, 32, 9, '#d9dcde') + E(152, 156, 32, 9, '#ffffff') + ''.join(R(134 + k * 8, 146 + (k % 2) * 4, 6, 10, '#9aba5a', 2) for k in range(5))
A['pickles'] = svg(g)

# sliced 切片的：一片片火腿整齐摊开，旁边刀
g = plate(100, 140, 84)
for k in range(6):
    g += G(E(0, 0, 30, 20, '#ef9a96') + E(0, 0, 30, 20, 'none', 'stroke="#fbeee0" stroke-width="3"'), f'translate({50+k*20},{128-k*4}) rotate({-20+k*4})')
g += G(R(0, -4, 70, 8, '#c4cbd0', 3) + R(68, -5, 30, 10, '#2f3437', 4), 'translate(60,60) rotate(-10)')
A['sliced'] = svg(g)

# cooked 熟的：锅里煎熟的金黄鸡块冒着热气，绿色对勾
g = G(Ci(0, 0, 70, '#3a3f44') + Ci(0, 0, 60, '#50565c') + R(66, -8, 70, 16, '#2f3437', 8), 'translate(84,120) scale(1,.6)')
for x, y in [(60, 110), (90, 104), (112, 118), (76, 126)]:
    g += E(x, y, 16, 11, '#c87a2a') + E(x - 3, y - 3, 10, 6, '#e0a050')
g += steam(66, 90, 3, 18, '#c4cbd0', .8) + Ci(164, 42, 16, '#5ba644') + St('M156,42 l6,6 l10,-12', '#ffffff', 4)
A['cooked'] = svg(g)

# roast-duck 烤鸭：挂在钩子上油亮的整只烤鸭
g = L(100, 6, 100, 36, '#a7adb1', 3) + St('M100,36 q8,6 0,14', '#a7adb1', 3)
g += Pa('M100,46 Q92,60 96,74 Q60,90 58,130 Q60,170 100,176 Q140,170 142,130 Q140,90 104,74 Q108,60 100,46 Z', '#a8441a')
g += Pa('M104,74 Q140,90 142,130 Q140,170 100,176 Q128,140 104,74 Z', '#8a3412') + hi(80, 110, 10, 22, .35, 10)
g += E(100, 60, 8, 12, '#b8501f')
A['roast-duck'] = svg(g, shadow=False)

# spring-roll 春卷：金黄酥脆的春卷，一个切开
g = plate(100, 150, 84)
for k, (x, y, r_) in enumerate([(70, 124, -10), (110, 116, -6), (130, 138, 4)]):
    g += G(R(-36, -12, 72, 24, '#d9903a', 12) + ''.join(St(f'M{-26+j*12},-10 l4,20', '#b8702a', 1.5) for j in range(5)) + hi(-16, -6, 14, 3, .4), f'translate({x},{y}) rotate({r_})')
g += Ci(166, 138, 12, '#d9903a') + Ci(166, 138, 9, '#8cc06a') + Ci(166, 138, 4, '#f08a24')
A['spring-roll'] = svg(g)

# salami 萨拉米：一根萨拉米香肠和切片，红色里有白点
random.seed(62)
g = G(R(-70, -22, 140, 44, '#8a2a24', 22) + R(-80, -4, 12, 8, '#e6dcc4', 2) + St('M-70,-10 q70,-14 140,0', '#a8443a', 3), 'translate(86,86) rotate(-12)')
for x, y in [(110, 150), (150, 140), (70, 156)]:
    g += Ci(x, y, 22, '#8a2a24') + Ci(x, y, 19, '#c0403a') + ''.join(Ci(x + random.uniform(-13, 13), y + random.uniform(-13, 13), 2.2, '#fbeee0') for _ in range(10))
A['salami'] = svg(g)

# smoked-salmon 烟熏三文鱼：面包上卷着橙色三文鱼片和莳萝
g = plate(100, 150, 84) + R(40, 112, 120, 30, '#d9a050', 8) + R(44, 108, 112, 26, '#f6e2b8', 6)
for k in range(3):
    g += Pa(f'M{56+k*32},{116} Q{64+k*32},{90} {80+k*32},{98} Q{92+k*32},{110} {84+k*32},{124} Q{70+k*32},{130} {56+k*32},{116} Z', '#f58a5a') + St(f'M{62+k*32},{110} q8,-6 16,0', '#fbd0b8', 2)
g += ''.join(St(f'M{70+k*30},{100} l4,-10 M{72+k*30},{98} l-6,-8', '#3c8a3a', 2) for k in range(3))
A['smoked-salmon'] = svg(g)

# cold-cuts 冷切肉：木板上摆着几种切片肉
g = board(100, 120, 176, 110)
for k in range(5): g += G(E(0, 0, 18, 14, '#ef9a96') + E(0, 0, 18, 14, 'none', 'stroke="#fbeee0" stroke-width="2"'), f'translate({40+k*14},{96+k*4})')
random.seed(63)
for k in range(4): g += Ci(126 + k * 12, 92 + (k % 2) * 8, 13, '#b8403a') + ''.join(Ci(126 + k * 12 + random.uniform(-7, 7), 92 + (k % 2) * 8 + random.uniform(-7, 7), 1.5, '#fbeee0') for _ in range(5))
for k in range(3): g += Pa(f'M{60+k*30},{150} q14,-12 28,0 q-14,8 -28,0 Z', '#c97a6a')
g += E(160, 150, 10, 12, '#8aa83a') + E(170, 140, 8, 10, '#8aa83a')
A['cold-cuts'] = svg(g)

# deli-counter 熟食柜台：玻璃柜里一排排熟食
g = R(10, 70, 180, 100, '#d9dcde', 6) + R(16, 76, 168, 60, '#e8f4fa', 4, 'opacity=".9"') + Pa('M10,70 L30,40 L170,40 L190,70 Z', '#cfe8f6', 'opacity=".8"')
for k, c in enumerate(['#e98a86', '#f3c234', '#8cc06a', '#c87a2a', '#f6e2b8']):
    g += R(22 + k * 33, 108, 28, 22, '#ffffff', 3) + E(36 + k * 33, 110, 12, 6, c)
g += R(10, 140, 180, 30, '#8a5a35', 4) + R(10, 34, 180, 8, '#5d6469', 3)
A['deli-counter'] = svg(g, shadow=False)

# marinated 腌制的：碗里的肉泡在酱汁里，蒜、葱、八角
g = bowl(96, 100, 140, fill='#7a3a1a', pattern='#c58b54')
g += E(70, 94, 22, 10, '#c9625a') + E(110, 92, 24, 11, '#c9625a') + E(92, 100, 20, 8, '#b8503a')
g += Ci(140, 94, 6, '#fbf8f0') + R(54, 94, 14, 3, '#4aa040', 1) + R(126, 90, 14, 3, '#4aa040', 1)
g += G(St('M0,0 L0,-40', '#c58b54', 6) + R(-8, -6, 16, 16, '#e8c070', 3), 'translate(160,70) rotate(30)')
A['marinated'] = svg(g)

# cured-ham 腌火腿：架子上夹着的一整条带蹄子的风干火腿
g = R(20, 160, 160, 12, '#8a5a35', 4) + R(36, 120, 10, 40, '#8a5a35') + R(150, 100, 10, 60, '#8a5a35') + St('M41,120 L155,100', '#5d6469', 4)
g += Pa('M40,110 Q40,70 80,60 Q130,50 156,80 Q170,100 150,120 Q120,140 80,136 Q40,134 40,110 Z', '#8a3a1a') + Pa('M60,80 Q90,64 130,72 Q110,90 60,80 Z', '#c8603a')
g += St('M150,90 L176,40', '#6a2a14', 14) + Pa('M168,34 l14,-6 l4,10 l-12,6 Z', '#2f2a27')
A['cured-ham'] = svg(g)

# quiche 法式咸派：带褶边的咸派，里面有菠菜和蛋奶，一块切出来
g = plate(100, 150, 84) + Pa('M30,136 Q32,150 46,152 L154,152 Q168,150 170,136 Z', '#d9a050') + E(100, 134, 70, 22, '#e8b868') + E(100, 132, 62, 18, '#f6dc8a')
g += ''.join(leaf(70 + k * 18, 128 + (k % 2) * 6, 14, 5, k * 50, '#3c8a3a') for k in range(4)) + Ci(116, 126, 4, '#d9453a')
g += Pa('M100,132 L162,132 L150,146 Z', '#e8b868')
A['quiche'] = svg(g)

# hummus 鹰嘴豆泥：一碗米色豆泥，中间淋橄榄油、撒几颗鹰嘴豆，配皮塔饼
g = E(96, 130, 64, 22, '#d9dcde') + E(96, 126, 64, 22, '#ffffff') + E(96, 124, 52, 16, '#e8d4a8')
g += St('M64,122 Q96,110 128,122', '#d6bc88', 4) + E(96, 122, 12, 5, '#c8a830') + ''.join(Ci(80 + k * 10, 120 + (k % 2) * 4, 4, '#e0c070') for k in range(4)) + Ci(110, 118, 2, '#d9453a')
g += G(Pa('M0,0 L40,-10 L30,30 Z', '#e8c890') + Pa('M0,0 L40,-10 L36,4 Z', '#d6a868'), 'translate(140,70)') + G(Pa('M0,0 L40,-10 L30,30 Z', '#e8c890'), 'translate(150,90) rotate(20)')
A['hummus'] = svg(g)

# sun-dried-tomato 番茄干：罐子里泡在油里的深红色番茄干
g = R(50, 46, 100, 130, '#f0dc90', 12, 'opacity=".9"') + R(46, 34, 108, 18, '#c4cbd0', 5)
random.seed(64)
g += ''.join(Pa(f'M{x-14},{y} Q{x-12},{y-12} {x},{y-10} Q{x+14},{y-8} {x+12},{y+4} Q{x},{y+12} {x-14},{y} Z', random.choice(['#a8302a', '#8a2420', '#c0403a'])) for x, y in [(random.uniform(70, 130), random.uniform(70, 160)) for _ in range(12)])
g += ''.join(leaf(70 + k * 30, 80 + k * 30, 14, 5, k * 60, '#3c8a3a') for k in range(3)) + R(56, 52, 8, 116, '#ffffff', 4, 'opacity=".35"')
A['sun-dried-tomato'] = svg(g)

# ================= 咖啡馆（一） =================
A['coffee'] = svg(coffee_cup(96, 96, 90) + steam(80, 80, 3, 16, '#c4cbd0', .9))

# green-tea 绿茶：玻璃杯里泡着嫩绿茶叶
g = tall_glass(56, 50, 84, 120, '#c8e098', .85) + ''.join(leaf(70 + k * 14, 80 + (k * 23) % 70, 14, 5, k * 47, '#5aa03a') for k in range(6)) + steam(74, 44, 3, 16, '#c4cbd0', .6)
A['green-tea'] = svg(g)

# black-tea 红茶：白瓷杯里红亮的茶，配小奶壶
g = coffee_cup(88, 100, 82, '#a8401a') + steam(74, 84, 3, 14, '#c4cbd0', .8)
g += Pa('M150,120 L176,120 L172,160 L154,160 Z', '#ffffff') + Pa('M150,120 L144,112 L156,120 Z', '#ffffff') + St('M176,128 q10,4 0,20', '#ffffff', 4)
A['black-tea'] = svg(g)

# milk-tea 奶茶：塑料杯里的珍珠奶茶，粗吸管
random.seed(65)
g = Pa('M50,50 L150,50 L136,180 L64,180 Z', '#eef6fa', 'opacity=".9"') + Pa('M52,66 L148,66 L136,180 L64,180 Z', '#d9b48a')
g += ''.join(Ci(random.uniform(72, 128), random.uniform(150, 172), 7, '#3a2418') for _ in range(14))
g += E(100, 50, 52, 8, '#e6ecef') + straw(118, 10, 108, 170, '#ef8fa4') + R(60, 96, 80, 30, '#ffffff', 4, 'opacity=".5"')
A['milk-tea'] = svg(g)

# hot-chocolate 热巧克力：马克杯里的热可可，上面漂着棉花糖
g = R(44, 70, 100, 100, '#d9453a', 14) + St('M144,92 q30,0 30,26 q0,26 -30,26', '#d9453a', 12) + E(94, 70, 50, 12, '#6a3a1a')
g += ''.join(R(66 + k * 16, 60 + (k % 2) * 6, 14, 12, '#ffffff', 3) for k in range(4)) + R(50, 120, 88, 12, '#ffffff', 0, 'opacity=".25"') + steam(80, 50, 3, 16, '#c4cbd0', .7)
A['hot-chocolate'] = svg(g)

# lemonade 柠檬水：玻璃壶装着淡黄柠檬水、柠檬片和冰块
g = Pa('M50,50 L130,50 L140,176 L40,176 Z', '#eef6fa', 'opacity=".9"') + Pa('M46,76 L134,76 L140,176 L40,176 Z', '#f6ec98', 'opacity=".9"') + Pa('M50,50 L36,56 L50,66 Z', '#eef6fa') + St('M130,70 q30,10 22,60 q-6,20 -18,24', '#dfeef6', 8)
g += ''.join(Ci(70 + k * 22, 110 + (k % 2) * 30, 14, '#f3d034') + Ci(70 + k * 22, 110 + (k % 2) * 30, 11, '#fbe98a') for k in range(3)) + ice_cube(80, 90, 18, 15) + ice_cube(116, 94, 16, -10)
A['lemonade'] = svg(g)

# latte 拿铁：高玻璃杯里分层的牛奶咖啡，表面拉花
g = tall_glass(60, 40, 80, 136, '', .92, [('#8a5a3a', .35), ('#c8a07a', .35), ('#f6efe2', .3)])
g += E(100, 52, 36, 8, '#f6efe2') + heart(100, 52, 8, '#c8a07a')
g += E(100, 182, 60, 10, '#d9dcde')
A['latte'] = svg(g)

# cappuccino 卡布奇诺：杯口厚厚一层奶泡，上面撒可可粉
g = coffee_cup(96, 100, 92, '#8a5a3a', foam='#f6efe2') + Pa('M50,100 Q60,76 96,74 Q132,76 142,100 Z', '#f6efe2')
random.seed(66)
g += ''.join(Ci(random.uniform(66, 126), random.uniform(80, 96), 1.4, '#7a4a2a') for _ in range(30))
A['cappuccino'] = svg(g)

# espresso 浓缩咖啡：小小一杯，表面一层金色油脂，咖啡豆
g = coffee_cup(96, 110, 60, '#a8703a') + E(96, 110, 22, 5, '#c8904a')
g += bean(150, 150, 1.2, 20) + bean(166, 140, 1.0, -30) + bean(40, 150, 1.1, 60)
A['espresso'] = svg(g)

# iced-coffee 冰咖啡：玻璃杯里加冰块的咖啡，吸管
g = tall_glass(56, 40, 88, 136, '', .85, [('#5a3218', .6), ('#c8a07a', .4)]) + ice_cube(80, 70, 22, 15) + ice_cube(116, 78, 20, -12) + ice_cube(96, 100, 18, 30)
g += straw(124, 10, 108, 160, '#3a8a3a')
A['iced-coffee'] = svg(g)

# decaf 无咖啡因：咖啡杯，旁边咖啡豆被划掉，月亮
g = coffee_cup(86, 110, 80) + bean(156, 70, 1.8) + no_sign(156, 70, 26)
g += Pa('M150,140 A18,18 0 1,0 170,170 A14,14 0 1,1 150,140 Z', '#f3c234')
A['decaf'] = svg(g)

# to-go 带走：纸杯咖啡套着杯套，装进外卖纸袋
g = Pa('M100,90 L176,90 L170,176 L106,176 Z', '#c8a070') + Pa('M100,90 L176,90 L172,100 L104,100 Z', '#b8905a') + St('M122,90 q16,-24 32,0', '#a87a4a', 4)
g += takeaway(66, 176, 64, 116)
A['to-go'] = svg(g)

# refill 续杯：咖啡壶往杯里倒咖啡，循环箭头
g = coffee_cup(70, 120, 80)
g += G(Pa('M0,0 L50,0 Q60,40 46,70 L4,70 Q-10,40 0,0 Z', '#eef6fa', 'opacity=".9"') + Pa('M-4,30 L54,30 Q58,50 46,70 L4,70 Q-6,50 -4,30 Z', '#6a3a1a') + R(-6, -10, 62, 12, '#2f3437', 4) + St('M50,10 q24,8 10,40', '#2f3437', 6) + Pa('M0,6 L-14,0 L0,-2 Z', '#2f3437'), 'translate(110,30) rotate(-35)')
g += St('M70,110 Q72,80 92,62', '#6a3a1a', 5)
g += St('M150,140 A22,22 0 1,1 172,162', '#5ba644', 5) + Pa('M166,166 L178,160 L176,172 Z', '#5ba644')
A['refill'] = svg(g)

# straw 吸管：几根彩色可弯折吸管
g = ''
for k, c in enumerate(['#e2463b', '#5aa1d4', '#f3c234', '#5ba644']):
    x = 56 + k * 28
    g += St(f'M{x},176 L{x},60 Q{x},44 {x+14},34 L{x+30},24', c, 9) + St(f'M{x-2},176 L{x-2},60', '#ffffff', 2) + ''.join(L(x - 4, 66 + j * 3, x + 4, 66 + j * 3, shade(c, -.2), 1) for j in range(4))
A['straw'] = svg(g)

# smoothie 果昔：粉色果昔，杯口插着草莓和香蕉片
g = tall_glass(56, 50, 88, 126, '#ef8fa4', .9) + Pa('M60,60 Q100,44 140,60 L140,70 L60,70 Z', '#f6b0c0')
g += straw(122, 14, 108, 150, '#ffffff') + Pa('M50,52 Q50,36 64,38 Q72,46 64,56 Z', '#d9453a') + Ci(144, 50, 12, '#f8e8a8') + Ci(144, 50, 4, '#e0c870')
A['smoothie'] = svg(g)

# sugar-free 无糖：咖啡杯，旁边方糖被划掉
g = coffee_cup(86, 110, 80) + sugar_cube(140, 64, 18) + no_sign(158, 72, 28)
A['sugar-free'] = svg(g)

# ================= 咖啡馆（二） =================
# order 点单：一只手指着菜单上的一项
g = R(36, 20, 110, 150, '#2f3437', 6) + R(44, 28, 94, 134, '#3a3f44', 4)
for k in range(5):
    y = 50 + k * 24
    g += Ci(58, y, 6, '#f3c234' if k == 2 else '#c4cbd0') + L(70, y, 120, y, '#e6ecef' if k == 2 else '#a7adb1', 4) + L(70, y + 8, 100, y + 8, '#7a8288', 2)
g += R(48, 92, 90, 20, '#f3c234', 4, 'opacity=".25"')
g += G(R(-14, -10, 28, 30, SK, 8) + R(-34, -6, 26, 12, SK, 6) + R(14, -6, 40, 26, '#3c7fc1', 6), 'translate(150,104)')
A['order'] = svg(g)

# counter 柜台：咖啡馆收银柜台，上面有收银机和点心柜
g = R(10, 110, 180, 70, '#8a5a35', 4) + R(6, 104, 188, 10, '#5a3a24', 3)
g += R(30, 70, 56, 36, '#3a3f44', 4) + R(36, 76, 44, 16, '#7fe08a', 2) + Pa('M24,104 L92,104 L86,96 L30,96 Z', '#5d6469')
g += R(110, 60, 72, 46, '#eef6fa', 4, 'opacity=".9"') + Ci(130, 92, 9, '#d9903a') + Ci(152, 92, 9, '#ef8fa4') + Ci(140, 76, 8, '#f6e2a8')
g += R(10, 10, 180, 30, '#2f3437', 4) + ''.join(L(24 + k * 40, 22, 54 + k * 40, 22, '#e6ecef', 3) for k in range(4))
A['counter'] = svg(g, shadow=False)

# waiter 服务员：系领结的服务员，托着托盘
cx, cy, r = 92, 76, 30
g = body(cx, cy, r, '#ffffff', w=r * 3.6) + Pa(f'M{cx-r*1.4},{cy+r*1.3} L{cx-r*.3},{cy+r*1.3} L{cx-r*.1},200 L{cx-r*1.6},200 Z', '#2f3437') + Pa(f'M{cx+r*1.4},{cy+r*1.3} L{cx+r*.3},{cy+r*1.3} L{cx+r*.1},200 L{cx+r*1.6},200 Z', '#2f3437')
g += Pa(f'M{cx-12},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx-12},{cy+r*1.32} Z M{cx+12},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx+12},{cy+r*1.32} Z', '#d9453a')
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'smile', None)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 1.6), (cx + r * 2.3, cy + r * .9)], '#ffffff', SK, 15)
g += E(cx + r * 2.3, cy + r * .75, 34, 7, '#c4cbd0') + coffee_cup(cx + r * 2.0, cy + r * .2, 22, saucer=False) + tall_glass(cx + r * 2.5, cy - r * .6, 16, 28, '#f3c234')
g += R(cx - r * 2.2, cy + r * 2.0, 18, 30, '#ffffff', 3)
A['waiter'] = svg(g)

A['sandwich'] = svg(plate(100, 156, 84) + sandwich(84, 104, 1.1) + G(sandwich(0, 0, .7), 'translate(150,124) rotate(20)'))

# biscuit 饼干：一摞长方形带小孔的茶点饼干和一杯茶
def bisc(x, y, rot):
    return G(R(-30, -20, 60, 40, '#e0b060', 6) + R(-26, -16, 52, 32, '#ecc880', 4) + ''.join(Ci(-16 + c * 16, -8 + r_ * 16, 2, '#c08a3a') for c in range(3) for r_ in range(2)), f'translate({x},{y}) rotate({rot})')
g = bisc(64, 140, -10) + bisc(70, 120, 5) + bisc(60, 98, -5) + coffee_cup(144, 106, 64, '#c98a3a')
A['biscuit'] = svg(g)

# bagel 贝果：带芝麻的圆圈面包
random.seed(67)
g = Ci(100, 108, 62, '#b8702a') + Ci(100, 104, 58, '#d9903a') + Ci(100, 106, 20, '#f1e8d4') + hi(76, 80, 16, 6, .3, -20)
g += ''.join(E(100 + rr * math.cos(a), 104 + rr * math.sin(a), 3, 1.6, '#fbf3dc', f'transform="rotate({random.uniform(0,180):.0f} {100+rr*math.cos(a):.0f} {104+rr*math.sin(a):.0f})"') for a, rr in [(random.uniform(0, 6.28), random.uniform(28, 52)) for _ in range(40)])
A['bagel'] = svg(g)

# wi-fi 无线网：门牌上的无线信号图标
g = R(40, 40, 120, 120, '#3c7fc1', 16) + Ci(100, 136, 8, '#ffffff')
for k in range(3):
    rr = 22 + k * 20
    g += St(f'M{100-rr*.75},{136-rr*.75} A{rr},{rr} 0 0,1 {100+rr*.75},{136-rr*.75}', '#ffffff', 9)
A['wi-fi'] = svg(g)

# password 密码：锁头和一排星号的输入框
g = R(30, 120, 140, 40, '#ffffff', 8) + R(30, 120, 140, 40, 'none', 8, 'stroke="#c4cbd0" stroke-width="3"') + ''.join(T(52 + k * 20, 152, '*', 30, '#2f3437', 900) for k in range(6))
g += St('M80,70 L80,54 A20,20 0 0,1 120,54 L120,70', '#a7adb1', 8) + R(70, 68, 60, 44, '#f3c234', 8) + Ci(100, 86, 6, '#8a6a1a') + R(97, 86, 6, 14, '#8a6a1a', 2)
A['password'] = svg(g)

# table-for-two 两人桌：小圆桌，两把椅子面对面，桌上两杯咖啡
g = E(100, 110, 50, 12, '#c58b54') + R(96, 116, 8, 54, '#8a5a35') + E(100, 172, 26, 6, '#5a3a24')
g += chair(36, 130, '#8a5a35', -1) + chair(164, 130, '#8a5a35', 1)
g += coffee_cup(84, 92, 22, saucer=False) + coffee_cup(118, 92, 22, saucer=False) + Ci(100, 96, 3, '#d9453a') + St('M100,96 l0,-12', '#5ba644', 2)
A['table-for-two'] = svg(g)

# outside 外面：露天座位，遮阳伞，阳光和树
g = Ci(36, 34, 16, '#f3c234') + tree(166, 120, .9) + R(0, 170, 200, 30, '#d6d0c2')
g += Pa('M30,70 Q90,20 150,70 Z', '#d9453a') + Pa('M60,70 Q90,20 120,70 Z', '#ffffff') + L(90, 40, 90, 170, '#5d6469', 4)
g += E(90, 128, 44, 9, '#ffffff') + R(88, 130, 4, 40, '#a7adb1') + chair(36, 140, '#5aa1d4', -1) + chair(144, 140, '#5aa1d4', 1)
A['outside'] = svg(g, shadow=False)

# queue 排队：一排人在柜台前排队
g = R(160, 90, 36, 90, '#8a5a35', 3)
for k in range(4):
    x = 140 - k * 34
    g += pose((x, 70 + (k % 2) * 4), (x, 92 + (k % 2) * 4), (x, 130), arms=[[(x - 8, 96), (x - 10, 126)], [(x + 8, 96), (x + 10, 126)]], legs=[[(x - 5, 130), (x - 6, 172)], [(x + 5, 130), (x + 6, 172)]],
              shirt=['#d9453a', '#3c7fc1', '#5ba644', '#f3c234'][k], pants='#3b4a5a', style=['short', 'long', 'grey', 'bun'][k], hair=['#3a2a20', '#5a3a2a', '#c8c3bc', '#3a2a20'][k], hr=12, tw=22, lw=10, aw=8)
A['queue'] = svg(g)

# self-service 自助：托盘上自己拿食物，自助取餐台
g = R(10, 70, 180, 30, '#c4cbd0', 4) + R(16, 58, 50, 16, '#f3c234', 3) + R(76, 58, 50, 16, '#8cc06a', 3) + R(136, 58, 50, 16, '#e98a86', 3)
g += R(30, 120, 140, 50, '#d9453a', 8) + R(36, 126, 128, 38, '#e2564b', 6) + plate(76, 144, 26) + coffee_cup(130, 136, 24, saucer=False)
g += G(R(-6, -40, 12, 50, '#c4cbd0', 3) + E(0, 12, 10, 14, '#c4cbd0'), 'translate(100,60) rotate(20)') + G(R(-14, -10, 28, 30, SK, 8) + R(-6, -30, 12, 24, SK, 6), 'translate(110,30)')
A['self-service'] = svg(g)

# scone 司康饼：切开的司康饼夹着果酱和奶油
g = plate(100, 156, 84) + R(46, 110, 70, 40, '#d9a050', 14) + R(46, 104, 70, 12, '#c0403a', 5) + R(46, 96, 70, 12, '#fbf8f0', 6) + Pa('M46,96 Q46,64 81,62 Q116,64 116,96 Z', '#e0b060') + hi(66, 74, 10, 4, .35)
g += E(150, 140, 20, 8, '#ffffff') + E(150, 136, 14, 6, '#c0403a')
A['scone'] = svg(g)

# saucer 茶碟：茶杯下面的小碟子，箭头指着碟子
g = coffee_cup(96, 92, 90) + St('M170,170 L148,150', '#d9453a', 4) + Pa('M142,144 L156,146 L148,156 Z', '#d9453a')
g = g.replace(f'<ellipse cx="96" cy="{92+90*.58}"', f'<ellipse cx="96" cy="{92+90*.58}"')
g += E(96, 92 + 90 * .58, 81, 16, 'none', 'stroke="#f3c234" stroke-width="4"')
A['saucer'] = svg(g)

# teaspoon 茶匙：小勺子舀着一勺白糖
g = G(R(-4, -70, 8, 90, '#c4cbd0', 4) + E(0, 34, 20, 28, '#c4cbd0') + E(0, 32, 16, 22, '#e6ecef') + E(0, 30, 13, 16, '#ffffff') + hi(-6, 24, 3, 8, .8), 'translate(100,90) rotate(-30)')
random.seed(68)
g += ''.join(R(random.uniform(110, 140), random.uniform(120, 160), 2.5, 2.5, '#ffffff', .5, 'stroke="#d9dcde" stroke-width=".6"') for _ in range(12))
A['teaspoon'] = svg(g)

# sugar-bowl 糖罐：带盖的瓷糖罐，旁边方糖
g = E(90, 170, 54, 10, '#d9dcde') + Pa('M40,100 Q40,170 90,170 Q140,170 140,100 Z', '#ffffff') + E(90, 100, 50, 10, '#f2efe8') + St('M40,116 q-16,6 -2,24 M140,116 q16,6 2,24', '#ffffff', 6)
g += Pa('M44,96 Q90,62 136,96 Z', '#ffffff') + Ci(90, 70, 8, '#ffffff') + St('M50,140 Q90,150 130,140', '#5aa1d4', 3)
g += sugar_cube(140, 150, 14) + sugar_cube(160, 160, 12)
A['sugar-bowl'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
