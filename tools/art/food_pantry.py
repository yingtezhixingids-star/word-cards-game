from flat import *
from fig import *
import os, sys, random

A = {}

def grains(x0, y0, w, h, n, col='#fbf8f0', seed=1, rx=3.2, ry=1.8):
    random.seed(seed)
    return ''.join(E(random.uniform(x0, x0 + w), random.uniform(y0, y0 + h), rx, ry, col, f'transform="rotate({random.uniform(0,180):.0f} {x0+w/2} {y0+h/2})"') for _ in range(n))

def jar(cx, base, w, h, fill, lid='#d9453a', label=None):
    g = R(cx - w / 2, base - h, w, h, fill, 10) + R(cx - w / 2 + 6, base - h + 8, 8, h - 16, '#ffffff', 4, 'opacity=".35"')
    g += R(cx - w / 2 - 3, base - h - 16, w + 6, 18, lid, 4)
    if label: g += R(cx - w / 2 + 6, base - h * .6, w - 12, h * .36, label, 3)
    return g

def bottle2(cx, base, w, h, col, cap, label='#ffffff', neck=.32):
    g = bottle_shape(cx - w / 2, base - h, w, h, col, neck) + R(cx - w * neck / 2 - 2, base - h - 12, w * neck + 4, 14, cap, 3)
    g += R(cx - w / 2 + 4, base - h * .55, w - 8, h * .32, label, 3) + R(cx - w / 2 + 5, base - h * .7, 5, h * .6, '#ffffff', 3, 'opacity=".25"')
    return g

def can(cx, base, w, h, col, label):
    return (R(cx - w / 2, base - h, w, h, '#c4cbd0', 4) + R(cx - w / 2, base - h * .82, w, h * .64, label, 0) + E(cx, base - h, w / 2, 5, '#d9dcde') + E(cx, base - h, w / 2 - 4, 3, '#b5bcc1') +
            ''.join(L(cx - w / 2, base - h + 4 + k * 3, cx + w / 2, base - h + 4 + k * 3, '#a7adb1', .8) for k in range(2)) + R(cx - w / 2 + 4, base - h * .8, 4, h * .6, '#ffffff', 2, 'opacity=".3"'))

def goat_badge(x, y, r=18):
    s = r / 18
    g = Ci(x, y, r + 3, '#ffffff') + Ci(x, y, r + 3, 'none', 'stroke="#d9dcde" stroke-width="2"')
    g += St(f'M{x-6*s},{y-10*s} q-6,-10 -2,-16 M{x+6*s},{y-10*s} q6,-10 2,-16', '#8a7a6a', 3 * s)
    g += E(x - 12 * s, y - 4 * s, 7 * s, 3 * s, '#e6e0d6') + E(x + 12 * s, y - 4 * s, 7 * s, 3 * s, '#e6e0d6')
    g += E(x, y, 9 * s, 13 * s, '#f0ece4', 'stroke="#c9c2b6" stroke-width="1"') + Ci(x - 4 * s, y - 3 * s, 1.6 * s, '#2f3437') + Ci(x + 4 * s, y - 3 * s, 1.6 * s, '#2f3437') + Pa(f'M{x-3*s},{y+12*s} L{x},{y+20*s} L{x+3*s},{y+12*s} Z', '#c9c2b6')
    return g

# ================= 食品柜 =================
# rice 大米/米饭：米袋里倒出白米，旁边一碗米饭
g = Pa('M20,170 L26,70 Q30,56 46,60 L96,60 Q110,56 112,70 L118,170 Z', '#f0e2c0') + Pa('M26,70 Q60,50 112,70 L110,84 Q60,68 28,84 Z', '#e0cfa8') + R(38, 100, 64, 40, '#d9453a', 4) + E(70, 120, 14, 10, '#ffffff')
g += grains(112, 150, 60, 20, 30, seed=2) + bowl(150, 116, 64, fill='#fbf8f0') + Pa('M118,116 Q130,90 150,90 Q170,90 182,116 Z', '#fbf8f0') + grains(124, 94, 52, 18, 18, '#f2ece0', 3, 2.5, 1.5)
A['rice'] = svg(g)

# flour 面粉：牛皮纸面粉袋印着麦穗，旁边一堆白面粉
g = Pa('M40,170 L44,60 L132,60 L136,170 Z', '#e8d4a8') + Pa('M44,60 L52,48 L124,48 L132,60 Z', '#d6c090') + R(56, 90, 64, 56, '#ffffff', 4)
g += St('M88,140 L88,96', '#c9a24a', 2.5) + ''.join(E(84, 104 + k * 8, 4, 6, '#e0b85a', 'transform="rotate(-25 84 %d)"' % (104 + k * 8)) + E(92, 104 + k * 8, 4, 6, '#d6aa48', 'transform="rotate(25 92 %d)"' % (104 + k * 8)) for k in range(4))
g += Pa('M128,176 Q140,140 160,140 Q182,144 190,176 Z', '#fbf8f0') + Pa('M150,142 Q160,138 168,146 Q160,150 150,142 Z', '#ffffff')
A['flour'] = svg(g)

# noodles 面条：一碗面，筷子夹起一缕面条
g = bowl(100, 116, 140, fill='#f3d58a')
g += ''.join(St(f'M{50+k*10},114 q5,-4 10,0', '#f6e2a8', 2) for k in range(10))
g += chopsticks(150, 30, 110, 90, '#8a5a35', 7)
g += ''.join(St(f'M{108+k*4},86 Q{104+k*4},104 {110+k*4},118', '#f3d58a', 3) for k in range(4))
g += Ci(72, 112, 8, '#5ba644') + E(132, 112, 12, 6, '#e0915a')
A['noodles'] = svg(g)

# honey 蜂蜜：蜂蜜罐和蜂蜜棒
g = jar(84, 172, 80, 90, '#f0b030', '#c58b54', '#ffffff') + Ci(84, 132, 10, '#f0b030') + ''.join(Pa(f'M{84+6*math.cos(k*1.047)},{132+6*math.sin(k*1.047)} L{84+10*math.cos(k*1.047)},{132+10*math.sin(k*1.047)}', 'none', 'stroke="#c58b54" stroke-width="2"') for k in range(6))
g += St('M120,90 L160,40', '#c58b54', 5) + G(''.join(E(0, -8 + k * 6, 10, 3, '#a8703e') for k in range(4)), 'translate(160,40) rotate(40)') + drop(150, 66, 7, '#f0b030')
A['honey'] = svg(g)

# jam 果酱：格子布盖的果酱瓶，吐司上抹着红果酱
g = jar(68, 170, 70, 80, '#c0283a', '#ffffff', '#fbf8f0') + Pa('M30,82 L106,82 L114,96 L22,96 Z', '#e2463b') + ''.join(R(28 + k * 12, 84, 6, 10, '#ffffff', 0, 'opacity=".6"') for k in range(7)) + heart(68, 130, 10, '#e2463b')
g += Pa('M120,176 L120,120 Q114,98 140,96 Q168,98 162,120 L162,176 Z', '#d9a865') + Pa('M126,170 L126,122 Q122,104 140,102 Q158,104 156,122 L156,170 Z', '#f6e2b8') + Pa('M128,130 Q140,118 154,130 L154,160 Q140,168 128,160 Z', '#c0283a')
A['jam'] = svg(g)

# pasta 意大利面：意面卷、蝴蝶面和通心粉
g = ''.join(St(f'M{30+k*4},150 L{60+k*4},40', '#f0d080', 3) for k in range(8)) + R(40, 92, 40, 10, '#3c7fc1', 3, 'transform="rotate(-70 60 97)"')
for x, y in [(120, 70), (160, 90)]:
    g += Pa(f'M{x-20},{y-14} L{x},{y} L{x-20},{y+14} Z M{x+20},{y-14} L{x},{y} L{x+20},{y+14} Z', '#f0c860') + Ci(x, y, 5, '#e0b040')
for x, y, r_ in [(110, 140, 20), (150, 150, -10), (128, 116, 40)]:
    g += G(R(-16, -7, 32, 14, '#f0c860', 2) + ''.join(L(-12 + k * 6, -7, -14 + k * 6, 7, '#d9a840', 1.5) for k in range(5)) + E(16, 0, 3, 7, '#c8902a'), f'translate({x},{y}) rotate({r_})')
A['pasta'] = svg(g)

# tofu 豆腐：盘子里白嫩的方块豆腐
g = E(100, 148, 84, 24, '#d9dcde') + E(100, 144, 84, 24, '#ffffff')
def cube(x, y, s):
    return Pa(f'M{x},{y} L{x+s},{y-s*.4} L{x+s*2},{y} L{x+s},{y+s*.4} Z', '#fbf8ee') + Pa(f'M{x},{y} L{x+s},{y+s*.4} L{x+s},{y+s*1.4} L{x},{y+s} Z', '#efe8d4') + Pa(f'M{x+s},{y+s*.4} L{x+s*2},{y} L{x+s*2},{y+s} L{x+s},{y+s*1.4} Z', '#e2d8c0')
g += cube(36, 102, 30) + cube(96, 100, 30) + cube(70, 70, 30)
g += Ci(60, 150, 4, '#5ba644') + Ci(140, 140, 4, '#5ba644')
A['tofu'] = svg(g)

# soy-sauce 酱油：深色玻璃瓶红盖子，小碟里黑色酱油
g = bottle2(80, 176, 56, 140, '#3a2418', '#d9453a', '#f6e8c8')
g += R(62, 112, 36, 18, '#d9453a', 2)
g += E(150, 162, 32, 10, '#d9dcde') + E(150, 158, 32, 10, '#ffffff') + E(150, 156, 22, 6, '#3a2418')
A['soy-sauce'] = svg(g)

# vinegar 醋：棕色醋瓶，饺子蘸醋
g = bottle2(70, 176, 50, 130, '#5a3a24', '#2f3437', '#fbf8f0') + R(54, 116, 32, 8, '#3c7fc1', 2) + R(54, 128, 32, 4, '#3c7fc1', 2)
g += E(146, 164, 36, 10, '#d9dcde') + E(146, 160, 36, 10, '#ffffff') + E(146, 158, 26, 7, '#6a3a1a')
g += G(Pa('M-24,8 Q-26,-18 0,-20 Q26,-18 24,8 Z', '#fbf8f0') + ''.join(Pa(f'M{-18+k*9},-14 q4,-6 8,0', 'none', 'stroke="#e6dcc4" stroke-width="2"') for k in range(4)), 'translate(146,128) rotate(-10)')
g += chopsticks(186, 90, 150, 124, '#8a5a35', 5)
A['vinegar'] = svg(g)

# cooking-oil 食用油：带提手的大桶金黄色食用油
g = Pa('M50,176 L50,70 Q50,54 66,54 L134,54 Q150,54 150,70 L150,176 Z', '#f0c43a', 'opacity=".95"') + R(90, 36, 22, 18, '#d9453a', 3)
g += St('M126,54 Q150,30 150,70', '#e0b020', 8) + R(60, 92, 80, 54, '#ffffff', 4) + ''.join(Ci(80 + k * 20, 118, 8, '#f3d034') for k in range(3)) + leaf(100, 108, 18, 6, -40, '#5ba644')
g += R(56, 64, 8, 104, '#ffffff', 4, 'opacity=".35"')
A['cooking-oil'] = svg(g)

# cereal 麦片：一碗加了牛奶的谷物麦片和麦片盒
g = R(24, 40, 70, 120, '#f3c234', 4) + R(30, 50, 58, 50, '#ffffff', 3) + E(59, 74, 20, 12, '#e0a050') + R(24, 40, 70, 120, 'none', 4, 'stroke="#d9a020" stroke-width="2"')
g += bowl(136, 128, 92, fill='#fbf8f0', pattern='#3c7fc1')
random.seed(21)
g += ''.join(E(random.uniform(100, 172), random.uniform(118, 130), 7, 5, random.choice(['#e0a050', '#d08a3a', '#f0c060'])) for _ in range(14))
g += St('M150,124 L182,80', '#c4cbd0', 5)
A['cereal'] = svg(g)

# oatmeal 燕麦粥：一碗燕麦粥，上面有蓝莓和香蕉片，旁边燕麦片
g = bowl(96, 104, 130, fill='#e8d8b8', pattern='#c58b54')
random.seed(22)
g += grains(48, 96, 96, 14, 22, '#d6c090', 22, 4, 2.5)
g += ''.join(Ci(70 + k * 12, 100 + (k % 2) * 4, 5, '#3c4f9a') for k in range(3)) + ''.join(Ci(110 + k * 12, 100, 6, '#f8e8a8') + Ci(110 + k * 12, 100, 2, '#e0c870') for k in range(3))
g += grains(130, 160, 50, 14, 16, '#e0cfa0', 23, 5, 3)
A['oatmeal'] = svg(g)

# ketchup 番茄酱：红色番茄酱挤瓶，挤出一团在薯条旁
g = Pa('M50,176 L50,70 Q50,54 74,54 Q98,54 98,70 L98,176 Z', '#d9302c') + Pa('M66,54 L82,54 L80,30 L68,30 Z', '#ffffff') + R(56, 100, 36, 40, '#ffffff', 4) + tomato_icon if False else Pa('M50,176 L50,70 Q50,54 74,54 Q98,54 98,70 L98,176 Z', '#d9302c')
g += Pa('M66,54 L82,54 L80,30 L68,30 Z', '#ffffff') + Pa('M70,30 L78,30 L74,20 Z', '#ffffff') + R(56, 100, 36, 40, '#ffffff', 4) + Ci(74, 120, 10, '#d9302c') + leaf(74, 110, 8, 3, -90, '#5ba644') + R(56, 64, 6, 100, '#ffffff', 3, 'opacity=".3"')
g += E(150, 164, 36, 10, '#d9dcde') + E(150, 160, 36, 10, '#ffffff') + Pa('M134,158 Q136,140 150,142 Q164,140 166,158 Z', '#d9302c')
g += ''.join(R(118 + k * 14, 120 - (k % 2) * 8, 9, 40, '#f3c234', 2, f'transform="rotate({-15+k*8} {122+k*14} 140)"') for k in range(4))
A['ketchup'] = svg(g)

# canned-food 罐头：几个叠在一起的罐头
g = can(64, 178, 56, 64, '#d9453a', '#d9453a') + can(124, 178, 56, 64, '#5ba644', '#5ba644') + can(94, 112, 56, 64, '#f3c234', '#f3c234')
g += Ci(64, 146, 10, '#ffffff') + Ci(124, 146, 10, '#ffffff') + Ci(94, 80, 10, '#ffffff') + Ci(64, 146, 6, '#d9302c') + leaf(120, 146, 12, 5, 0, '#3c8a3a') + E(94, 80, 6, 4, '#f08a24')
A['canned-food'] = svg(g)

# tea-bag 茶包：茶杯里泡着茶包，线和标签挂在杯外
g = cup(90, 100, 100, 70, '#ffffff', '#c98a3a')
g += St('M90,100 Q118,60 144,70', '#a7adb1', 2) + R(140, 66, 22, 26, '#5ba644', 3) + leaf(151, 80, 10, 4, -60, '#ffffff')
g += Pa('M70,96 L96,96 L96,120 L70,120 Z', '#e8d4a8', 'opacity=".9"') + steam(70, 86, 3, 14, '#c4cbd0', .7)
A['tea-bag'] = svg(g)

# vermicelli 粉丝：一捆透明细丝的粉丝
g = ''.join(St(f'M{56+k*5},40 Q{50+k*5+(k%3)*4},100 {60+k*5},170', '#e8eef0' if k % 2 else '#dfe8ec', 3) for k in range(18))
g += R(46, 96, 108, 14, '#d9453a', 4) + R(46, 100, 108, 4, '#ffffff', 2, 'opacity=".4"')
A['vermicelli'] = svg(g)

# ================= 乳制品和蛋 =================
A['milk'] = svg(bottle2(70, 176, 60, 140, '#fbfbf8', '#3c7fc1', '#3c7fc1', .45) + glass(112, 90, 56, 86, '#ffffff', .85))

# egg 鸡蛋：几个鸡蛋，一个打开露出蛋黄
g = egg(60, 96, 2.0) + E(116, 90, 26, 34, '#f0d8b8') + hi(106, 76, 5, 10, .6)
g += E(130, 150, 46, 20, '#ffffff') + Ci(130, 148, 14, '#f3b82a') + hi(126, 144, 4, 3, .6)
A['egg'] = svg(g)

# cheese 奶酪：一块带孔的黄色奶酪三角
g = Pa('M30,140 L170,100 L170,150 L30,176 Z', '#f0c040') + Pa('M30,140 L120,60 L170,100 Z', '#f8d860') + Pa('M120,60 L170,100 L170,150 L120,110 Z', '#000', 'opacity="0"')
g += Ci(80, 150, 9, '#d9a020') + Ci(130, 136, 7, '#d9a020') + Ci(150, 156, 5, '#d9a020') + Ci(60, 160, 5, '#d9a020') + E(110, 100, 8, 4, '#e0b030') + E(140, 96, 6, 3, '#e0b030')
A['cheese'] = svg(g)

# butter 黄油：碟子上一块淡黄色黄油，黄油刀
g = E(100, 150, 84, 22, '#d9dcde') + E(100, 146, 84, 22, '#ffffff')
g += Pa('M40,130 L120,130 L120,96 L40,96 Z', '#f8e08a') + Pa('M40,96 L60,80 L140,80 L120,96 Z', '#fbeca8') + Pa('M120,96 L140,80 L140,114 L120,130 Z', '#ecd070')
g += Pa('M58,96 q8,-8 16,-4 q-6,6 -16,4 Z', '#e6c860') + G(R(0, -4, 60, 8, '#c4cbd0', 4) + R(56, -5, 36, 10, '#5a3a24', 4), 'translate(110,150) rotate(-15)')
A['butter'] = svg(g)

# yogurt 酸奶：酸奶杯，勺子挖起白色酸奶，上面有草莓
g = Pa('M50,70 L150,70 L140,176 L60,176 Z', '#ffffff') + Pa('M50,70 L150,70 L148,90 L52,90 Z', '#ef8fa4') + R(60, 110, 80, 40, '#ef8fa4', 4, 'opacity=".25"')
g += E(100, 70, 50, 10, '#fbf8f4') + Pa('M80,70 Q90,52 104,62 Q118,52 124,70 Z', '#fbf8f4') + Ci(110, 58, 8, '#d9453a')
g += St('M130,66 L170,26', '#c4cbd0', 5) + E(126, 70, 10, 6, '#c4cbd0', 'transform="rotate(-45 126 70)"')
A['yogurt'] = svg(g)

# ice-cream 冰淇淋：脆筒上叠两个球
g = Pa('M70,100 L130,100 L100,184 Z', '#d9a050') + ''.join(L(76 + k * 12, 100, 100 + (k - 2) * 2, 180, '#b8803a', 1.5) for k in range(5)) + ''.join(L(76, 112 + k * 16, 124, 104 + k * 16, '#b8803a', 1.5) for k in range(4))
g += Ci(100, 90, 34, '#f6c0cc') + Ci(100, 52, 30, '#f8f0dc') + Pa('M70,96 q10,14 20,0 q10,14 20,0 q10,14 20,0 L130,90 L70,90 Z', '#f6c0cc')
g += Ci(100, 22, 8, '#d9453a') + St('M100,14 q4,-8 10,-10', '#5a8a3a', 2) + hi(88, 44, 6, 8, .5)
A['ice-cream'] = svg(g)

# soy-milk 豆浆：一杯豆浆和一小把黄豆
g = glass(46, 50, 70, 126, '#f6efd8', .85) + steam(64, 44, 2, 16, '#c4cbd0', .6)
random.seed(31)
g += ''.join(Ci(x, y, 8, '#e8c870') + hi(x - 2, y - 2, 2.5, 2, .6) for x, y in [(140, 160), (156, 150), (160, 168), (130, 172), (148, 176), (172, 160)])
g += E(150, 120, 24, 16, '#7cc06a') + ''.join(Ci(138 + k * 12, 120, 6, '#a8d878') for k in range(3))
A['soy-milk'] = svg(g)

# milk-powder 奶粉：奶粉罐，量勺里装着白色奶粉
g = R(36, 50, 90, 126, '#e6ecef', 6) + E(81, 50, 45, 10, '#c4cbd0') + R(36, 80, 90, 64, '#5aa1d4') + E(81, 112, 22, 16, '#ffffff') + Ci(81, 112, 6, '#f3c234') + R(42, 56, 8, 112, '#ffffff', 4, 'opacity=".4"')
g += St('M128,160 L170,140', '#ffffff', 6) + E(124, 162, 16, 10, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + E(124, 158, 12, 6, '#fbf8f0')
g += Pa('M140,180 Q150,166 162,166 Q174,168 180,180 Z', '#fbf8f0')
A['milk-powder'] = svg(g)

# carton 纸盒：一盒尖顶纸盒装牛奶
g = R(60, 66, 80, 112, '#ffffff', 2) + Pa('M60,66 L100,30 L140,66 Z', '#e6ecef') + R(90, 22, 20, 12, '#3c7fc1', 2) + Pa('M120,66 L140,66 L140,178 L120,178 Z', '#e2e8eb')
g += R(60, 100, 80, 46, '#3c7fc1') + E(100, 124, 18, 12, '#ffffff') + Ci(92, 122, 3, '#2f3437') + Ci(104, 126, 3, '#2f3437')
A['carton'] = svg(g)

# skim-milk 脱脂牛奶：蓝色标签的奶瓶，标着 0%
g = bottle2(100, 180, 70, 150, '#ffffff', '#3c7fc1', '#9fd0ec', .42) + T(100, 128, '0%', 28, '#ffffff', 900)
A['skim-milk'] = svg(g)

# whipped-cream 奶油：奶油喷罐和一大团裱花奶油
g = R(36, 60, 50, 116, '#e6ecef', 8) + R(36, 90, 50, 50, '#ef8fa4') + Pa('M46,60 Q61,40 76,60 Z', '#c4cbd0') + R(56, 26, 10, 20, '#ffffff', 3) + R(40, 66, 6, 104, '#ffffff', 3, 'opacity=".4"')
for k, (rx, y) in enumerate([(46, 156), (38, 134), (28, 114), (16, 96)]):
    g += E(136, y, rx, 14, '#fbf8f0' if k % 2 else '#ffffff') + St(f'M{136-rx+6},{y} q{rx-6},8 {2*rx-12},0', '#efe6d6', 2)
g += Pa('M130,90 Q136,70 140,90 Z', '#ffffff')
A['whipped-cream'] = svg(g)

# cream-cheese 奶油奶酪：一盒奶油奶酪，涂在百吉饼上
g = R(24, 110, 70, 50, '#ffffff', 8) + R(24, 104, 70, 14, '#5aa1d4', 6) + R(34, 128, 50, 20, '#e6f2fa', 3)
g += Ci(140, 120, 46, '#c88a4a') + Ci(140, 120, 40, '#e0b070') + Ci(140, 120, 14, '#f1e8d4')
g += Pa('M106,110 Q120,86 146,88 Q170,92 176,114 Q168,108 156,112 Q140,104 126,114 Q114,108 106,110 Z', '#fbf8f0')
g += G(R(0, -3, 40, 6, '#c4cbd0', 3) + R(38, -4, 26, 8, '#5a3a24', 4), 'translate(90,70) rotate(20)')
A['cream-cheese'] = svg(g)

# sour-cream 酸奶油：烤土豆上一大勺白色酸奶油和葱花
g = E(100, 156, 84, 22, '#d9dcde') + E(100, 152, 84, 22, '#ffffff')
g += E(100, 120, 60, 36, '#a87a4a') + E(100, 112, 46, 22, '#f2d890') + Pa('M74,110 Q80,84 100,86 Q122,84 126,110 Q100,118 74,110 Z', '#fbf8f0')
g += ''.join(R(80 + k * 8, 98 + (k % 2) * 6, 5, 3, '#4aa040', 1) for k in range(6))
A['sour-cream'] = svg(g)

# goat-s-milk 羊奶：一瓶羊奶 + 山羊头标记
g = bottle2(84, 180, 64, 140, '#fbfbf8', '#8a7a6a', '#e8dcc4', .44) + glass(118, 108, 44, 70, '#ffffff', .8) + goat_badge(160, 46, 20)
A['goat-s-milk'] = svg(g)

# dairy 乳制品：牛奶、奶酪、黄油、酸奶放在一起
g = bottle2(52, 170, 44, 110, '#fbfbf8', '#3c7fc1', '#3c7fc1', .45)
g += Pa('M90,170 L176,150 L176,176 L90,190 Z', '#f0c040') + Pa('M90,170 L150,120 L176,150 Z', '#f8d860') + Ci(130, 168, 5, '#d9a020') + Ci(156, 160, 4, '#d9a020')
g += Pa('M100,80 L156,80 L150,140 L106,140 Z', '#ffffff') + Pa('M100,80 L156,80 L155,92 L101,92 Z', '#ef8fa4') + E(128, 80, 28, 6, '#fbf8f4')
g += badge(160, 34, 'cow', 16)
A['dairy'] = svg(g)

# lactose-free 无乳糖：牛奶盒上画着被划掉的乳糖符号
g = R(50, 66, 80, 112, '#ffffff', 2) + Pa('M50,66 L90,30 L130,66 Z', '#e6ecef') + R(80, 22, 20, 12, '#5ba644', 2) + Pa('M110,66 L130,66 L130,178 L110,178 Z', '#e2e8eb')
g += R(50, 98, 80, 50, '#5ba644') + E(90, 124, 18, 12, '#ffffff')
hx, hy = 152, 128
g += Ci(hx, hy, 28, '#ffffff') + Pa(' '.join(('M' if k == 0 else 'L') + f'{hx+14*math.cos(k*math.pi/3):.1f},{hy+14*math.sin(k*math.pi/3):.1f}' for k in range(6)) + ' Z', 'none', 'stroke="#5d6469" stroke-width="3"')
g += Ci(hx, hy, 24, 'none', 'stroke="#d9453a" stroke-width="5"') + L(hx - 17, hy + 17, hx + 17, hy - 17, '#d9453a', 5)
A['lactose-free'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
