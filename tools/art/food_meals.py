from flat import *
from fig import *
import os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from food_cafe import coffee_cup, tall_glass, ice_cube, straw, no_sign, plate, sandwich, chair  # noqa
from food_candy import burger, fries, cola_cup, glass_stem  # noqa

A = {}
SK = P['skin']

def fried_egg(x, y, s=1):
    return G(Pa('M-30,-4 Q-34,-24 -10,-24 Q6,-34 22,-20 Q38,-10 30,8 Q24,24 0,22 Q-26,24 -30,-4 Z', '#ffffff') + Ci(0, -2, 11, '#f3b82a') + hi(-3, -6, 3, 2, .7), f'translate({x},{y}) scale({s})')

def toast_slice(x, y, s, rot=0):
    d = 'M-30,40 L-30,-10 Q-44,-14 -40,-30 Q-34,-46 0,-46 Q34,-46 40,-30 Q44,-14 30,-10 L30,40 Z'
    return G(Pa(d, '#a8642a') + G(Pa(d, '#e0a860'), 'scale(.84) translate(0,2)'), f'translate({x},{y}) rotate({rot}) scale({s})')

def baozi(x, y, s):
    g = Pa('M-34,14 Q-40,-14 -10,-26 Q0,-34 10,-26 Q40,-14 34,14 Q0,24 -34,14 Z', '#fbf8f0') + ''.join(St(f'M0,-26 Q{k*10},-10 {k*16},12', '#e6dcc4', 2) for k in (-2, -1, 1, 2)) + Ci(0, -28, 4, '#efe6d0') + hi(-16, -6, 6, 3, .8)
    return G(g, f'translate({x},{y}) scale({s})')

def dumpling(x, y, s, rot=0):
    g = Pa('M-30,8 Q-32,-20 0,-22 Q32,-20 30,8 Z', '#fbf8f0') + Pa('M-30,8 Q0,16 30,8 Q0,12 -30,8 Z', '#e6dcc4') + ''.join(Pa(f'M{-20+k*10},-16 q4,-8 8,0', 'none', 'stroke="#e6dcc4" stroke-width="2"') for k in range(5))
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def table_top(y=150):
    return R(0, y, 200, 200 - y, '#c58b54') + R(0, y, 200, 6, '#a8703e')

def clock_small(x, y, r, hm):
    return clock(x, y, r, hm)

def pot(cx, cy, w, h, col='#5d6469', fill='#c06a3a'):
    g = R(cx - w / 2, cy, w, h, col, 8) + E(cx, cy, w / 2, w * .12, shade(col, -.2)) + E(cx, cy + 2, w / 2 - 6, w * .1, fill)
    g += R(cx - w / 2 - 14, cy + 10, 16, 8, '#2f3437', 4) + R(cx + w / 2 - 2, cy + 10, 16, 8, '#2f3437', 4)
    return g

# ================= 快餐 =================
A['hamburger'] = svg(burger(100, 110, 1.4))
A['fries'] = svg(fries(100, 120, 1.6))
# pizza 比萨：一整个比萨，抽出一块拉丝
g = Ci(96, 110, 70, '#d9903a') + Ci(96, 110, 62, '#e0392f') + Ci(96, 110, 60, '#f3d070', 'opacity=".85"')
random.seed(81)
g += ''.join(Ci(96 + rr * math.cos(a), 110 + rr * math.sin(a), 8, '#c0302a') + Ci(96 + rr * math.cos(a), 110 + rr * math.sin(a), 3, '#a8241f') for a, rr in [(random.uniform(0, 6.28), random.uniform(10, 50)) for _ in range(8)])
g += ''.join(leaf(96 + rr * math.cos(a), 110 + rr * math.sin(a), 10, 4, random.uniform(0, 360), '#3c8a3a') for a, rr in [(random.uniform(0, 6.28), random.uniform(10, 50)) for _ in range(5)])
g += ''.join(L(96, 110, 96 + 62 * math.cos(a), 110 + 62 * math.sin(a), '#d9903a', 2) for a in [k * math.pi / 3 for k in range(6)])
A['pizza'] = svg(g)
# hot-dog 热狗：面包夹香肠，上面挤黄芥末
g = Pa('M30,110 Q30,140 60,146 L140,146 Q170,140 170,110 Z', '#d9903a') + R(22, 96, 156, 24, '#a8341f', 12) + St('M34,104 q10,-8 20,0 t20,0 t20,0 t20,0 t20,0 t20,0', '#f3c234', 5)
g += Pa('M30,110 Q30,90 60,92 L140,92 Q170,90 170,110 Q100,104 30,110 Z', '#e0a050', 'opacity=".0"')
g += Pa('M36,118 Q36,100 60,102 L140,102 Q164,100 164,118 Z', '#e0a050', 'opacity="0"')
A['hot-dog'] = svg(g)
A['cola'] = svg(cola_cup(84, 120, 1.6) + R(130, 90, 44, 86, '#d9302c', 8) + E(152, 90, 22, 6, '#c4cbd0') + St('M136,130 q16,-12 32,0', '#ffffff', 4))
# fried-chicken 炸鸡：纸桶里装满金黄炸鸡
g = Pa('M40,90 L160,90 L148,180 L52,180 Z', '#ffffff') + ''.join(Pa(f'M{40+k*24},90 L{52+k*24},90 L{58+k*20},180 L{48+k*20},180 Z', '#d9453a') for k in range(5))
for x, y in [(60, 80), (96, 70), (134, 80), (80, 60), (118, 56)]:
    g += E(x, y, 22, 16, '#c8782a') + ''.join(Ci(x - 12 + k * 6, y - 4 + (k % 2) * 6, 2.5, '#e0a050') for k in range(5))
A['fried-chicken'] = svg(g)
# milkshake 奶昔：高杯巧克力奶昔，顶上奶油和樱桃
g = Pa('M60,70 L140,70 L126,176 L74,176 Z', '#eef6fa', 'opacity=".9"') + Pa('M62,80 L138,80 L126,176 L74,176 Z', '#8a5a3a')
g += Pa('M56,76 Q60,50 80,52 Q90,36 104,46 Q122,36 128,54 Q146,54 144,76 Z', '#ffffff') + Ci(100, 34, 9, '#d9453a') + straw(118, 0, 110, 60, '#ef8fa4')
A['milkshake'] = svg(g)
# nuggets 鸡块：盒子里几块金黄鸡块，旁边蘸酱
g = Pa('M30,110 L130,110 L122,176 L38,176 Z', '#f3c234') + Pa('M30,110 L130,110 L136,90 L24,90 Z', '#e0a820')
for x, y in [(52, 100), (82, 94), (110, 102), (66, 80), (98, 76)]:
    g += Pa(f'M{x-16},{y} Q{x-18},{y-14} {x-4},{y-14} Q{x+16},{y-16} {x+16},{y-2} Q{x+14},{y+12} {x},{y+12} Q{x-14},{y+12} {x-16},{y} Z', '#d9903a') + Ci(x - 4, y - 4, 2, '#f0c070')
g += E(160, 160, 24, 10, '#ffffff') + R(136, 140, 48, 20, '#ffffff', 4) + E(160, 142, 22, 6, '#d9302c')
A['nuggets'] = svg(g)
# for-here 在这儿吃：餐盘放在店里的桌子上，椅子，刀叉标志
g = table_top(130) + chair(30, 110, '#5aa1d4', -1) + chair(170, 110, '#5aa1d4', 1)
g += R(50, 112, 100, 22, '#d9453a', 4) + burger(80, 108, .45) + fries(116, 110, .45) + cola_cup(136, 106, .45)
g += Ci(100, 44, 24, '#5ba644') + L(92, 30, 92, 58, '#ffffff', 3) + St('M88,30 l0,10 q4,4 8,0 l0,-10', '#ffffff', 2) + L(108, 30, 108, 58, '#ffffff', 3) + Pa('M108,30 q6,8 0,16 Z', '#ffffff')
A['for-here'] = svg(g, shadow=False)
# combo-meal 套餐：托盘上汉堡、薯条、可乐一套
g = R(16, 100, 168, 80, '#d9453a', 8) + R(22, 106, 156, 68, '#e2564b', 6) + burger(66, 140, .7) + fries(118, 140, .6) + cola_cup(156, 134, .6)
A['combo-meal'] = svg(g)
# delivery 外卖：骑电动车的外卖员，后座外卖箱
g = wheel(52, 160, 20) + wheel(148, 160, 20) + Pa('M52,160 L80,130 L130,130 L148,160', 'none', 'stroke="#3c7fc1" stroke-width="10" stroke-linejoin="round"') + R(76, 124, 60, 14, '#3c7fc1', 6) + St('M140,130 L150,100 L162,96', '#2f3437', 5)
g += R(30, 86, 46, 44, '#f3c234', 4) + R(30, 96, 46, 6, '#e0a820')
g += pose((112, 54), (110, 74), (104, 116), arms=[[(116, 78), (140, 94), (160, 98)]], legs=[[(104, 116), (128, 124), (132, 146)]], shirt='#f3c234', pants='#2f3437', hair='#3a2a20', hr=13, tw=24, lw=11, aw=9)
g += Pa('M98,44 Q112,30 126,44 L126,50 L98,50 Z', '#f3c234')
A['delivery'] = svg(g)
# drive-through 免下车窗口：汽车停在快餐店小窗口前，递出纸袋
g = R(120, 30, 80, 150, '#d9453a', 4) + R(132, 70, 40, 40, '#f6efe0', 3) + R(126, 64, 52, 8, '#f3c234', 2) + Pa('M150,90 L170,90 L168,110 L152,110 Z', '#c8a070')
g += Pa('M10,150 L10,120 Q14,100 40,96 L90,96 Q110,100 120,124 L120,150 Z', '#5aa1d4') + Pa('M40,100 L86,100 Q100,104 106,120 L40,120 Z', '#cfe8f6') + wheel(36, 154, 14) + wheel(98, 154, 14)
g += G(R(-14, -10, 28, 26, SK, 8), 'translate(116,108)') + R(0, 176, 200, 24, '#8a8f94')
A['drive-through'] = svg(g, shadow=False)
# instant-noodles 方便面：泡面杯，掀开盖子冒热气，叉子
g = Pa('M50,70 L150,70 L134,176 L66,176 Z', '#ffffff') + R(52, 100, 96, 40, '#d9453a') + Ci(100, 120, 12, '#f3c234')
g += Pa('M50,70 L150,70 L160,40 L60,50 Z', '#e6ecef') + E(100, 70, 50, 9, '#f3d070') + ''.join(St(f'M{64+k*12},70 q4,-4 8,0', '#e0b040', 2) for k in range(6)) + steam(80, 50, 3, 18, '#c4cbd0', .7)
g += G(R(-3, -50, 6, 60, '#c4cbd0', 3) + ''.join(R(-6 + k * 4, -64, 2.5, 16, '#c4cbd0') for k in range(4)), 'translate(150,90) rotate(25)')
A['instant-noodles'] = svg(g)
# taco 墨西哥卷饼：弯成U形的玉米饼里夹肉、生菜、番茄
g = Pa('M30,150 Q30,60 100,60 Q170,60 170,150 Z', '#e8c060') + Pa('M44,150 Q44,76 100,76 Q156,76 156,150 Z', '#7a3a1a')
g += ''.join(Ci(60 + k * 16, 82 + (k % 2) * 6, 10, '#7cc05a') for k in range(6)) + ''.join(R(62 + k * 18, 86, 10, 8, '#e0392f', 2) for k in range(4)) + ''.join(R(54 + k * 12, 92, 6, 3, '#f3d070') for k in range(7))
g += Pa('M30,150 Q30,60 100,60 L100,72 Q42,72 40,150 Z', '#d9a840')
A['taco'] = svg(g)
# kebab 烤肉串：竹签上串着烤肉和青椒洋葱
g = ''
for i, y in enumerate((70, 120)):
    sk = L(-90, 0, 90, 0, '#c8a070', 4)
    for k in range(6):
        col = ['#8a3a1a', '#5aaa3a', '#8a3a1a', '#f6efe0', '#8a3a1a', '#e0392f'][k]
        sk += R(-66 + k * 22, -14, 18, 28, col, 5) + ('' if col != '#8a3a1a' else ''.join(Ci(-60 + k * 22, -6 + j * 8, 1.5, '#d9a050') for j in range(2)))
    g += G(sk, f'translate(100,{y}) rotate({-8+i*10})')
A['kebab'] = svg(g)
# burrito 墨西哥卷：锡纸包着的大卷饼，切开露出米饭豆子
g = G(R(-70, -30, 140, 60, '#e8c890', 30) + R(-70, -30, 70, 60, '#c4cbd0', 8) + ''.join(L(-66 + k * 10, -28, -64 + k * 10, 28, '#a7adb1', 1) for k in range(7)) + E(70, 0, 16, 30, '#f6efe0') + Ci(66, -10, 5, '#7a3a1a') + Ci(74, 6, 5, '#5aaa3a') + Ci(64, 12, 4, '#e0392f') + Ci(76, -6, 3, '#7a3a1a'), 'translate(96,104) rotate(-15)')
A['burrito'] = svg(g)

# ================= 早餐 =================
# breakfast 早餐：早晨的阳光下，餐桌上煎蛋、吐司、橙汁
g = Ci(170, 30, 18, '#f3c234') + ''.join(L(170 + 22 * math.cos(a), 30 + 22 * math.sin(a), 170 + 30 * math.cos(a), 30 + 30 * math.sin(a), '#f3c234', 3) for a in [k * math.pi / 4 for k in range(8)])
g += table_top(140) + E(80, 140, 54, 14, '#ffffff') + fried_egg(70, 132, .8) + toast_slice(110, 120, .45, 10) + tall_glass(140, 90, 30, 56, '#f5a43a') + coffee_cup(30, 120, 30, saucer=False)
A['breakfast'] = svg(g, shadow=False)
# porridge 粥：一碗白粥，配一小碟咸菜，勺子
g = bowl(84, 100, 120, fill='#f6f1e4') + E(84, 100, 50, 10, '#fbf8f0') + steam(70, 86, 3, 14, '#c4cbd0', .7) + St('M110,96 L150,60', '#ffffff', 6) + E(108, 100, 10, 6, '#ffffff')
g += E(156, 160, 26, 8, '#d9dcde') + E(156, 156, 26, 8, '#ffffff') + ''.join(R(142 + k * 7, 150 + (k % 2) * 3, 5, 6, '#8aa83a', 1) for k in range(4))
A['porridge'] = svg(g)
# boiled-egg 煮鸡蛋：蛋杯里的鸡蛋，敲开顶露出蛋黄；一个剥好的切半
g = Pa('M60,170 L60,150 Q60,130 80,126 L76,116 L104,116 L100,126 Q120,130 120,150 L120,170 Z', '#5aa1d4') + E(90, 92, 30, 38, '#f6ead4') + Pa('M60,82 L120,82 L118,72 Q90,40 62,72 Z', '#f1e8d4', 'opacity="0"')
g += E(90, 70, 26, 8, '#ffffff') + Ci(90, 70, 10, '#f3b82a') + Pa('M64,70 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6 l4,0', 'none', 'stroke="#e6d4b4" stroke-width="2"')
g += E(152, 150, 22, 28, '#ffffff') + Ci(152, 154, 12, '#f3b82a')
A['boiled-egg'] = svg(g)
# fried-egg 煎蛋：平底锅里的太阳蛋
A['fried-egg'] = svg(G(Ci(0, 0, 70, '#3a3f44') + Ci(0, 0, 60, '#50565c') + R(66, -8, 70, 16, '#2f3437', 8), 'translate(84,110) scale(1,.7)') + fried_egg(84, 108, 1.4))
# orange-juice 橙汁：一杯橙汁和半个橙子
g = tall_glass(40, 50, 76, 126, '#f5a43a', .85) + straw(100, 20, 90, 150, '#5ba644')
g += Ci(150, 150, 28, '#f08a24') + Ci(150, 150, 24, '#fbd18a') + ''.join(L(150, 150, 150 + 22 * math.cos(a), 150 + 22 * math.sin(a), '#f5a43a', 4) for a in [k * math.pi / 4 for k in range(8)])
A['orange-juice'] = svg(g)
# pancake 薄煎饼：一摞煎饼淋蜂蜜，顶上一块黄油
g = plate(100, 160, 84)
for k in range(5):
    g += E(100, 150 - k * 14, 60, 14, '#c8782a') + E(100, 146 - k * 14, 60, 12, '#e0a050')
g += Pa('M50,92 Q100,76 150,92 L150,100 Q140,120 136,100 Q120,112 114,98 Q90,116 84,98 Q70,110 60,100 Z', '#f0b030') + R(90, 76, 22, 14, '#f8e08a', 3)
A['pancake'] = svg(g)
# omelet 煎蛋卷：对折的黄色蛋卷，里面有火腿青菜
g = plate(100, 150, 84) + Pa('M30,140 Q30,90 100,84 Q170,90 170,140 Z', '#f3c840') + Pa('M30,140 Q100,124 170,140 Z', '#e0b030') + hi(70, 104, 20, 6, .35, -10)
g += Ci(60, 136, 5, '#e98a86') + Ci(140, 136, 5, '#5aaa3a') + Ci(100, 138, 4, '#e0392f')
A['omelet'] = svg(g)
# scrambled-eggs 炒鸡蛋：吐司上一堆松软的炒蛋
random.seed(83)
g = plate(100, 156, 84) + toast_slice(100, 120, 1.1)
g += ''.join(Ci(100 + random.uniform(-30, 30), 108 + random.uniform(-18, 14), random.uniform(8, 13), random.choice(['#f6d34a', '#f3c234', '#f8e070'])) for _ in range(16)) + ''.join(R(80 + k * 12, 100 + (k % 2) * 10, 4, 3, '#4aa040', 1) for k in range(4))
A['scrambled-eggs'] = svg(g)
# stuffed-bun 包子：蒸笼里带褶子的包子
g = E(100, 150, 84, 24, '#a8703e') + R(16, 120, 168, 32, '#c58b54', 4) + E(100, 120, 84, 22, '#d9a868') + baozi(64, 110, 1.0) + baozi(136, 110, 1.0) + baozi(100, 94, 1.0) + steam(80, 64, 3, 20, '#c4cbd0', .7)
A['stuffed-bun'] = svg(g)
# fried-dough-stick 油条：金黄的两根连体油条和一碗豆浆
g = G(R(-80, -12, 160, 24, '#d9903a', 12) + R(-80, 10, 160, 24, '#c8782a', 12) + ''.join(St(f'M{-70+k*20},-6 q6,4 12,0', '#f0c070', 2) for k in range(8)), 'translate(96,80) rotate(-15)')
g += bowl(130, 140, 70, fill='#f6efd8')
A['fried-dough-stick'] = svg(g)
# rice-noodles 米粉：一碗汤米粉，白色细粉，牛肉、葱花
g = bowl(100, 100, 150, fill='#e0b070', pattern='#d9453a') + ''.join(St(f'M{40+k*12},100 q6,-4 12,0 t12,0', '#f6f1e4', 2.5) for k in range(9))
g += E(80, 96, 14, 8, '#8a3a1a') + E(108, 94, 14, 8, '#8a3a1a') + ''.join(R(60 + k * 14, 96 + (k % 2) * 4, 5, 3, '#4aa040', 1) for k in range(6)) + chopsticks(160, 40, 110, 96, '#8a5a35', 6)
A['rice-noodles'] = svg(g)
# buffet 自助餐：一排保温餐盘，各种食物任你拿
g = R(0, 110, 200, 70, '#e6ecef') + R(0, 104, 200, 10, '#c4cbd0')
for k, c in enumerate(['#f3c234', '#8cc06a', '#e0915a', '#fbf8f0']):
    x = 12 + k * 46
    g += R(x, 84, 40, 24, '#a7adb1', 4) + E(x + 20, 86, 18, 5, c) + Pa(f'M{x},{84} Q{x+20},{56} {x+40},{84} Z', '#c4cbd0', 'opacity=".7"') + Ci(x + 20, 66, 3, '#5d6469')
g += plate(60, 150, 22) + plate(140, 150, 22) + R(0, 20, 200, 10, '#5d6469')
A['buffet'] = svg(g, shadow=False)
# brunch 早午餐：11点的钟，盘子里早餐和午餐合在一起
g = clock(150, 50, 30, (11, 0)) + E(86, 136, 76, 24, '#d9dcde') + E(86, 132, 76, 24, '#ffffff') + fried_egg(56, 126, .6) + toast_slice(90, 118, .35, 10) + Pa('M104,132 Q104,116 124,116 Q144,116 144,132 Z', '#8cc06a') + Ci(118, 124, 5, '#e0392f')
g += coffee_cup(170, 150, 26, saucer=False)
A['brunch'] = svg(g)
# baked-beans 焗豆：吐司上浇满番茄汁焗豆
random.seed(84)
g = plate(100, 156, 84) + toast_slice(100, 120, 1.1)
g += Pa('M66,110 Q70,86 100,86 Q130,86 134,110 Q130,134 100,136 Q70,134 66,110 Z', '#d9502a') + ''.join(E(100 + random.uniform(-26, 26), 110 + random.uniform(-18, 18), 5, 3.5, '#f08a4a', f'transform="rotate({random.uniform(0,180):.0f} 100 110)"') for _ in range(24))
A['baked-beans'] = svg(g)
# hash-browns 薯饼：几块椭圆形金黄酥脆的土豆饼
random.seed(85)
g = plate(100, 156, 84) + ''.join(G(E(0, 0, 34, 22, '#c8782a') + E(0, -2, 30, 18, '#e0a050') + ''.join(L(random.uniform(-24, 18), random.uniform(-12, 12), random.uniform(-18, 24), random.uniform(-12, 12), '#f0c070', 2) for _ in range(8)), f'translate({x},{y}) rotate({r_})') for x, y, r_ in [(70, 130, -10), (130, 134, 10), (100, 108, 0)])
A['hash-browns'] = svg(g)
# english-breakfast 英式早餐：一大盘香肠、煎蛋、培根、焗豆、番茄、蘑菇、吐司
g = E(100, 140, 92, 34, '#d9dcde') + E(100, 134, 92, 34, '#ffffff')
g += fried_egg(70, 122, .7) + G(R(-24, -7, 48, 14, '#8a2a24', 7), 'translate(130,116) rotate(-10)') + G(R(-24, -7, 48, 14, '#8a2a24', 7), 'translate(132,132) rotate(-5)')
g += Pa('M80,146 Q84,134 104,134 Q122,136 124,148 Q104,156 80,146 Z', '#d9502a') + ''.join(Ci(88 + k * 8, 144 - (k % 2) * 3, 3.5, '#f08a4a') for k in range(4))
g += Ci(160, 140, 12, '#e0392f') + Ci(160, 140, 6, '#f08a6a') + E(50, 146, 14, 8, '#8a6a4a') + E(50, 142, 14, 6, '#c8a87a') + St('M90,104 q10,-8 20,0 t20,0', '#c0403a', 6) + toast_slice(32, 110, .32, -20)
A['english-breakfast'] = svg(g)

# ================= 午餐和晚餐 =================
# lunch 午饭：中午12点的钟，桌上一个饭盒
g = Ci(36, 34, 16, '#f3c234') + clock(150, 50, 30, (12, 0)) + table_top(150)
g += R(50, 110, 100, 44, '#5aa1d4', 6) + R(54, 114, 44, 36, '#fbf8f0', 3) + R(102, 114, 44, 16, '#8cc06a', 3) + R(102, 134, 44, 16, '#e0915a', 3) + chopsticks(160, 100, 120, 150, '#8a5a35', 5)
A['lunch'] = svg(g, shadow=False)
# dinner 晚饭：晚上月亮出来，一家人的饭桌上菜肴冒热气
g = R(0, 0, 200, 110, '#2f3a5a') + Pa('M160,20 A18,18 0 1,0 180,52 A14,14 0 1,1 160,20 Z', '#f3c234') + star(40, 30, 4, '#ffffff') + star(100, 20, 3, '#ffffff')
g += table_top(110) + E(100, 140, 40, 12, '#ffffff') + E(100, 138, 30, 8, '#c06a3a') + bowl(40, 128, 34, fill='#fbf8f0') + bowl(160, 128, 34, fill='#fbf8f0') + E(70, 166, 22, 7, '#ffffff') + E(70, 164, 16, 5, '#5aaa3a') + E(130, 166, 22, 7, '#ffffff') + E(130, 164, 16, 5, '#e0915a') + steam(90, 126, 2, 18, '#c4cbd0', .6)
A['dinner'] = svg(g, shadow=False)
# dumplings 饺子：盘子里一圈白胖的饺子，旁边醋碟
g = E(96, 140, 86, 28, '#d9dcde') + E(96, 134, 86, 28, '#ffffff') + dumpling(54, 122, .7, -15) + dumpling(98, 114, .7) + dumpling(142, 122, .7, 15) + dumpling(74, 146, .7, -5) + dumpling(122, 146, .7, 5)
g += E(166, 72, 20, 7, '#ffffff') + E(166, 70, 14, 4, '#6a3a1a') + chopsticks(40, 40, 80, 100, '#8a5a35', 5)
A['dumplings'] = svg(g)
# fried-rice 炒饭：盘子里的蛋炒饭，有鸡蛋、豌豆、胡萝卜丁
random.seed(86)
g = E(100, 140, 86, 28, '#d9dcde') + E(100, 134, 86, 28, '#ffffff') + Pa('M30,132 Q40,96 100,92 Q160,96 170,132 Q100,148 30,132 Z', '#f2dc9a')
g += ''.join(Ci(random.uniform(44, 156), random.uniform(102, 134), 4, random.choice(['#f3c234', '#7cc05a', '#f08a24', '#f8e070'])) for _ in range(40)) + G(R(-3, -40, 6, 50, '#c4cbd0', 3) + E(0, 14, 10, 13, '#c4cbd0'), 'translate(160,90) rotate(30)')
A['fried-rice'] = svg(g)
# noodle-soup 汤面：一大碗牛肉汤面，牛肉片、青菜、葱
g = bowl(100, 100, 160, fill='#c8783a', pattern='#d9453a') + ''.join(St(f'M{36+k*12},100 q6,-6 12,0 t12,0', '#f3d58a', 3) for k in range(10))
g += E(76, 94, 16, 10, '#7a3a1a') + E(106, 92, 16, 10, '#7a3a1a') + leaf(130, 94, 26, 10, -20, '#3c8a3a') + ''.join(R(60 + k * 14, 98, 5, 3, '#4aa040', 1) for k in range(5)) + steam(80, 80, 3, 18, '#c4cbd0', .8)
A['noodle-soup'] = svg(g)
# hot-pot 火锅：鸳鸯锅，一边红汤一边白汤，咕嘟冒泡，旁边肉片和青菜
g = E(100, 120, 80, 30, '#c4cbd0') + R(20, 120, 160, 30, '#a7adb1', 4) + E(100, 120, 72, 24, '#e2463b') + Pa('M100,96 Q60,110 100,144 Q100,120 100,96 Z', '#f6ecd8', 'opacity="0"')
g += Pa('M28,120 A72,24 0 0,1 100,96 Q80,120 100,144 A72,24 0 0,1 28,120 Z', '#f6ecd8') + St('M100,96 Q80,120 100,144', '#a7adb1', 4)
g += ''.join(Ci(120 + k * 12, 116 + (k % 2) * 6, 4, '#f08a6a') for k in range(4)) + ''.join(Ci(50 + k * 12, 118 + (k % 2) * 6, 4, '#ffffff') for k in range(3)) + Ci(140, 112, 3, '#2f2a27') + steam(70, 90, 4, 22, '#c4cbd0', .8)
g += R(4, 170, 50, 20, '#ffffff', 4) + ''.join(E(16 + k * 12, 178, 8, 5, '#e98a86') for k in range(3)) + R(146, 170, 50, 20, '#ffffff', 4) + ''.join(leaf(156 + k * 12, 182, 14, 5, -60, '#4a9a3a') for k in range(3))
A['hot-pot'] = svg(g)
# stew 炖菜：锅里炖着大块牛肉、土豆、胡萝卜
g = pot(96, 100, 140, 70, '#8a3a2a', '#9a4a2a') + E(76, 104, 12, 8, '#7a3a1a') + E(110, 102, 14, 8, '#7a3a1a') + E(94, 108, 10, 6, '#e0c070') + Ci(130, 106, 6, '#f08a24') + Ci(60, 106, 6, '#f08a24') + steam(76, 84, 3, 18, '#c4cbd0', .8)
A['stew'] = svg(g)
# stir-fry 炒菜：炒锅里翻炒青菜、彩椒，下面火苗
g = Pa('M24,96 Q100,170 176,96 Z', '#3a3f44') + R(170, 92, 30, 10, '#5a3a24', 5)
g += ''.join(leaf(60 + k * 20, 100 + (k % 2) * 8, 20, 8, k * 50, '#4a9a3a') for k in range(5)) + R(70, 92, 14, 10, '#e0392f', 2) + R(114, 96, 14, 10, '#f3c234', 2) + E(96, 92, 10, 6, '#e0915a')
g += ''.join(Pa(f'M{70+k*20},176 Q{62+k*20},156 {70+k*20},140 Q{78+k*20},156 {70+k*20},176 Z', '#f08a24') for k in range(4)) + G(R(-3, -40, 6, 50, '#5a3a24', 3), 'translate(140,70) rotate(40)') + St('M40,70 q8,-10 16,0 M150,60 q8,-10 16,0', '#c4cbd0', 3)
A['stir-fry'] = svg(g, shadow=False)
# spaghetti 意大利面条：盘中卷曲的长面条，浇红色番茄酱
g = E(100, 140, 86, 28, '#d9dcde') + E(100, 134, 86, 28, '#ffffff')
g += ''.join(St(f'M{50+k*8},130 Q{70+k*6},{90+(k%3)*6} {100+k*4},116 T{150-k*2},128', '#f3d070', 3) for k in range(8))
g += Pa('M72,112 Q80,90 100,92 Q124,92 128,112 Q100,122 72,112 Z', '#d9302c') + Ci(90, 102, 7, '#7a3a1a') + Ci(112, 100, 7, '#7a3a1a') + leaf(100, 92, 12, 5, -60, '#3c8a3a')
g += G(R(-3, -40, 6, 50, '#c4cbd0', 3) + ''.join(R(-6 + k * 4, -54, 2.5, 16, '#c4cbd0') for k in range(4)), 'translate(160,80) rotate(30)')
A['spaghetti'] = svg(g)
# barbecue 烧烤：烤架上烤着肉串和玉米，冒烟，下面炭火
g = Pa('M30,110 Q100,170 170,110 Z', '#2f3437') + L(60, 150, 50, 186, '#2f3437', 5) + L(140, 150, 150, 186, '#2f3437', 5) + ''.join(L(30 + k * 20, 110, 30 + k * 20, 112, '#5d6469', 2) for k in range(8))
g += L(26, 108, 174, 108, '#a7adb1', 3) + ''.join(Ci(50 + k * 18, 118, 6, '#f08a24') for k in range(6))
for k in range(3):
    g += L(40 + k * 40, 104, 70 + k * 40, 90, '#c8a070', 3) + ''.join(R(44 + k * 40 + j * 9, 88 - j * 4, 8, 12, '#8a3a1a', 3) for j in range(3))
g += steam(70, 76, 3, 24, '#c4cbd0', 1.2)
A['barbecue'] = svg(g, shadow=False)
# roast-chicken 烤鸡：盘子里一整只金黄的烤鸡
g = E(100, 156, 90, 26, '#d9dcde') + E(100, 152, 90, 26, '#ffffff') + E(100, 120, 60, 40, '#d9903a') + E(110, 106, 30, 18, '#e8a850') + hi(84, 104, 12, 6, .35, -10)
for sx in (-1, 1):
    g += G(E(0, 0, 20, 14, '#c8782a') + R(14, -4, 18, 8, '#f6efe0', 4) + Ci(32, -4, 5, '#f6efe0') + Ci(32, 4, 5, '#f6efe0'), f'translate({100+sx*44},{108}) rotate({-30 if sx>0 else 210})')
g += Ci(50, 152, 7, '#5ba644') + Ci(150, 156, 7, '#e0392f') + leaf(160, 148, 16, 5, -40, '#3c8a3a')
A['roast-chicken'] = svg(g)
# side-dish 配菜：一大盘主菜旁边几小碟配菜
g = E(84, 120, 64, 22, '#d9dcde') + E(84, 116, 64, 22, '#ffffff') + Pa('M40,114 Q44,96 84,94 Q124,96 128,114 Q84,126 40,114 Z', '#7a3a1a')
for k, (x, y, c) in enumerate([(160, 70, '#8cc06a'), (164, 120, '#fbf8f0'), (150, 170, '#e0c070')]):
    g += E(x, y + 3, 26, 9, '#d9dcde') + E(x, y, 26, 9, '#ffffff') + E(x, y - 1, 18, 6, c)
g += St('M136,70 L120,90 M140,120 L132,118 M126,168 L120,140', '#d9453a', 3)
A['side-dish'] = svg(g)
# leftovers 剩饭菜：冰箱里盖着保鲜膜的半碗剩菜
g = R(20, 20, 160, 170, '#e6ecef', 8) + R(28, 28, 144, 154, '#f6f8fa', 4) + L(28, 110, 172, 110, '#c4cbd0', 3) + R(150, 60, 6, 40, '#a7adb1', 3)
g += bowl(76, 82, 70, fill='#e0915a') + E(76, 82, 35, 8, '#dff1fb', 'opacity=".7"') + St('M41,82 q35,-8 70,0', '#ffffff', 2)
g += R(100, 76, 50, 30, '#ffffff', 4) + R(100, 76, 50, 8, '#5aa1d4', 3) + E(80, 156, 34, 10, '#ffffff') + Pa('M50,156 Q60,140 80,140 Q90,148 96,156 Z', '#8cc06a') + E(80, 156, 34, 10, '#dff1fb', 'opacity=".6"')
A['leftovers'] = svg(g, shadow=False)
# home-cooked 家常的：奶奶在灶台边做饭，锅里冒着热气，一颗爱心
cx, cy, r = 70, 70, 28
g = diner(cx, cy, r, '#d9453a', P['grey'], 'bun', 'up', 'smile', None, '#ef9a8a') + Pa(f'M{cx-r*1.1},{cy+r*1.4} L{cx+r*1.1},{cy+r*1.4} L{cx+r*1.3},200 L{cx-r*1.3},200 Z', '#f6efe0')
g += R(100, 150, 100, 50, '#a7adb1') + R(96, 144, 108, 10, '#5d6469', 2) + pot(150, 112, 70, 34, '#3c7fc1', '#e0915a') + steam(136, 100, 3, 14, '#c4cbd0', .8)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.8), (cx + r * 2.6, cy + r * 1.3)], '#d9453a', SK, 14) + St(f'M{cx+r*2.6},{cy+r*1.3} L{150},{110}', '#8a5a35', 4)
g += heart(150, 50, 14, '#e2463b')
A['home-cooked'] = svg(g)
# seconds 再来一份：双手递出空碗，勺子再盛一勺
g = bowl(84, 120, 90, fill='#f6f1e4') + E(84, 120, 40, 8, '#fbf8f0')
g += G(R(-4, -70, 8, 80, '#8a5a35', 3) + E(0, 14, 20, 12, '#c4cbd0') + E(0, 12, 16, 8, '#e0915a'), 'translate(130,74) rotate(30)')
g += G(R(-14, -10, 28, 26, SK, 8), 'translate(40,150)') + G(R(-14, -10, 28, 26, SK, 8), 'translate(128,150)') + St('M20,190 L36,156 M148,190 L132,156', '#5aa1d4', 14)
g += T(160, 40, '+1', 24, '#5ba644', 900)
A['seconds'] = svg(g)
# set-the-table 摆餐具：餐垫上摆好盘子、刀叉、杯子、餐巾
g = R(16, 60, 168, 120, '#e6dcc4', 8) + E(100, 124, 44, 30, '#d9dcde') + E(100, 120, 44, 30, '#ffffff') + E(100, 120, 30, 20, '#f4f6f7')
g += R(40, 90, 4, 64, '#c4cbd0', 2) + ''.join(R(34 + k * 4, 84, 2.5, 18, '#c4cbd0') for k in range(4)) + R(156, 90, 5, 64, '#c4cbd0', 2) + Pa('M156,90 q10,10 0,28 Z', '#c4cbd0')
g += R(22, 100, 12, 50, '#5aa1d4', 2) + tall_glass(124, 60, 24, 30, '#dff1fb', .6)
A['set-the-table'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
