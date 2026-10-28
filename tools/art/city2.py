from kit2 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)

def shelf_unit(x, y, w, h, rows=4, seed=1):
    random.seed(seed)
    g = R(x, y, w, h, '#e6ecef', 2)
    rh = h / rows
    for r_ in range(rows):
        g += R(x, y + (r_ + 1) * rh - 4, w, 4, '#a7adb1')
        xx = x + 3
        while xx < x + w - 10:
            ww = random.uniform(8, 14); hh = random.uniform(rh * .45, rh * .8)
            g += R(xx, y + (r_ + 1) * rh - 4 - hh, ww, hh, random.choice(['#e2463b', '#5ba644', '#f3c234', '#3c7fc1', '#f08a24', '#ef8fa4', '#ffffff']), 1)
            xx += ww + 2
    return g

def running_man(x, y, s=1, col='#ffffff'):
    return G(Ci(6, -30, 6, col) + St('M2,-20 L-4,0 L-16,6 M-4,0 L6,12 L4,26 M0,-16 L14,-8 L20,-14 M0,-16 L-12,-10 L-18,-2', col, 5), f'translate({x},{y}) scale({s})')

def pill_bottle(cx, base, w, h, col='#f08a24', cap='#ffffff'):
    return R(cx - w / 2, base - h, w, h, col, 6, 'opacity=".9"') + R(cx - w / 2 - 3, base - h - 14, w + 6, 16, cap, 3) + R(cx - w / 2 + 4, base - h * .7, w - 8, h * .4, '#ffffff', 2) + R(cx - w / 2 + 4, base - h + 6, 5, h - 12, '#ffffff', 2, 'opacity=".35"')

def capsule(x, y, s=1, rot=0, c1='#e2463b', c2='#ffffff'):
    return pill(x, y, 30 * s, 12 * s, c1, c2, rot)

def officer(cx, cy, r, shirt='#2f4a7a', hat='#1f3a5a', badge='#f3c234'):
    g = person_bust(cx, cy, r, shirt, '#3a2a20', 'short', 'dot', 'flat')
    g += Pa(f'M{cx-r*1.05},{cy-r*.45} L{cx+r*1.05},{cy-r*.45} L{cx+r*.9},{cy-r*1.3} Q{cx},{cy-r*1.5} {cx-r*.9},{cy-r*1.3} Z', hat) + R(cx - r * 1.2, cy - r * .55, r * 2.4, 6, '#1a2a3a', 2) + star(cx, cy - r * .95, r * .2, badge)
    g += star(cx - r * .9, cy + r * 1.7, r * .22, badge) + R(cx + r * .4, cy + r * 1.5, r * .5, r * .1, '#ffffff', 1)
    return g

def fire_truck(cx, base, s=1):
    g = R(-80, -50, 120, 44, '#d9302c', 4) + Pa('M40,-6 L40,-50 L66,-50 Q78,-48 80,-30 L80,-6 Z', '#d9302c') + R(46, -44, 22, 16, '#cfe8f6', 2) + R(-76, -60, 110, 6, '#c4cbd0') + ''.join(L(-70 + k * 12, -60, -70 + k * 12, -54, '#a7adb1', 2) for k in range(10))
    g += R(-80, -20, 160, 6, '#ffffff') + R(50, -58, 14, 8, '#3c7fc1', 2) + wheel(-50, 0, 14) + wheel(50, 0, 14) + ''.join(R(-70 + k * 20, -44, 14, 14, '#a7231f', 2) for k in range(5))
    return G(g, f'translate({cx},{base}) scale({s})')

def police_car(cx, base, s=1):
    g = car_side(0, 0, '#ffffff', 1) + R(-50, -26, 110, 10, '#2f4a7a') + R(-8, -66, 24, 8, '#e2463b', 2) + R(4, -66, 12, 8, '#3c7fc1', 2)
    return G(g, f'translate({cx},{base}) scale({s})')

def extinguisher(cx, base, s=1):
    return G(R(-18, -90, 36, 90, '#d9302c', 14) + R(-10, -104, 20, 16, '#2f3437', 3) + Pa('M10,-100 L34,-96 L34,-90 L10,-92 Z', '#2f3437') + St('M-10,-96 Q-40,-80 -34,-40', '#2f3437', 5) + R(-14, -60, 28, 26, '#ffffff', 2) + R(-14, -86, 6, 70, '#ffffff', 3, 'opacity=".25"'), f'translate({cx},{base}) scale({s})')

def turbine(cx, base, h, s=1):
    g = Pa(f'M{cx-4},{base} L{cx-2},{base-h} L{cx+2},{base-h} L{cx+4},{base} Z', '#ffffff') + Ci(cx, base - h, 5, '#e6ecef')
    for a in (-90, 30, 150):
        g += G(Pa('M0,0 L-4,-6 L0,-60 L5,-6 Z', '#ffffff', 'stroke="#d9dcde" stroke-width="1"'), f'translate({cx},{base-h}) rotate({a+90}) scale({s})')
    return g

def solar(x, y, w, h):
    return Pa(f'M{x},{y+h} L{x+w*.2},{y} L{x+w},{y} L{x+w*.8},{y+h} Z', '#2f4a7a') + ''.join(L(x + w * .2 * (1 - t) + w * .8 * 0 + (w * .8) * t * 0 + (x + w * .8 * t + w * .2 * (1 - t) - x) * 0, 0, 0, 0, '#000', 0) for t in [])+ ''.join(L(x + w * (.2 + .8 * t) - w * .2 * 0, y, x + w * .8 * t, y + h, '#7a9ac8', 1.5) for t in [k / 4 for k in range(1, 4)]) + ''.join(L(x + w * .2 * (1 - t), y + h * t, x + w * .2 * (1 - t) + w * .8, y + h * t, '#7a9ac8', 1.5) for t in [k / 3 for k in range(1, 3)])

def pylon(cx, base, h):
    return Pa(f'M{cx-20},{base} L{cx-4},{base-h} L{cx+4},{base-h} L{cx+20},{base} Z', 'none', 'stroke="#8a9196" stroke-width="3"') + L(cx - 28, base - h * .75, cx + 28, base - h * .75, '#8a9196', 3) + L(cx - 20, base - h * .5, cx + 20, base - h * .5, '#8a9196', 3) + L(cx - 15, base, cx + 10, base - h * .5, '#8a9196', 2) + L(cx + 15, base, cx - 10, base - h * .5, '#8a9196', 2)

# ================= 商场 =================
# shopping-mall 购物中心：多层玻璃大楼，许多店铺，人们拎着购物袋
g = sky_ground(176, WALK) + R(10, 40, 180, 136, '#e6ecef', 4) + R(10, 30, 180, 14, '#5aa1d4', 3) + ''.join(R(20 + (k % 4) * 44, 60 + (k // 4) * 40, 36, 30, ['#ef8fa4', '#f3c234', '#9fd0ec', '#7cc05a'][(k + k // 4) % 4], 2, 'opacity=".75"') for k in range(8)) + R(80, 140, 40, 36, '#a9d8f2', 2)
g += bag_(40, 156, 18, 20, '#e2463b') + bag_(150, 156, 18, 20, '#3c7fc1')
S_('shopping-mall', g, False)
S_('store', R(0, 180, 200, 20, WALK) + storefront(20, 40, 160, 140, '#f6efe0', '#5ba644', icon=shirt_icon if False else '') + Pa('M50,100 L66,100 L76,108 L72,114 L66,112 L66,150 L50,150 L50,112 L44,114 L40,108 Z', '#e2463b'), False)
# escalator 自动扶梯：斜着上升的扶梯，扶手和台阶
g = R(0, 0, 200, 200, '#e6ecef') + Pa('M10,180 L50,180 L160,60 L190,60 L190,80 L164,80 L60,196 L10,196 Z', '#a7adb1') + ''.join(R(40 + k * 14, 170 - k * 15, 16, 4, '#5d6469') for k in range(9)) + St('M10,160 L50,160 L156,42 L190,42', '#2f3437', 7) + person_stand(110, 120, '#e2463b', s=.4)
S_('escalator', g, False)
# restroom 洗手间：墙上的男女洗手间标志牌，箭头
S_('restroom', R(0, 0, 200, 200, '#e6ecef') + R(30, 50, 140, 90, '#3c7fc1', 8) + Ci(70, 74, 8, '#ffffff') + R(62, 86, 16, 34, '#ffffff', 4) + Ci(130, 74, 8, '#ffffff') + Pa('M118,120 L142,120 L136,86 L124,86 Z', '#ffffff') + L(100, 60, 100, 130, '#ffffff', 3) + arrow(80, 170, 130, 170, '#3c7fc1', 5), False)
# exit 出口：门框上方绿色指示牌，人走向门外，箭头向外
S_('exit', R(0, 0, 200, 200, '#e6ecef') + R(50, 70, 100, 130, '#ffffff') + R(56, 76, 88, 124, '#bfe6fa') + R(60, 24, 80, 34, '#2f9a5a', 4) + arrow(70, 41, 126, 41, '#ffffff', 5) + person_stand(100, 196, '#5aa1d4', s=.55), False)
# department-store 百货商店：多层大楼，每层不同商品区
g = sky_ground(184, WALK) + R(20, 20, 160, 164, '#f2ead8', 4) + R(14, 14, 172, 10, '#c0302a', 2)
for k, icon_c in enumerate(['#ef8fa4', '#3c7fc1', '#f3c234', '#7cc05a']):
    y = 30 + k * 36
    g += R(28, y, 144, 30, '#bfe6fa', 2) + ''.join(R(36 + j * 28, y + 8, 18, 18, icon_c, 3) for j in range(5))
S_('department-store', g, False)
# food-court 美食广场：一圈小吃档口，中间桌椅，人们吃饭
g = R(0, 0, 200, 200, '#f2ead8') + ''.join(R(4 + k * 50, 20, 44, 50, ['#e2463b', '#f3c234', '#5ba644', '#3c7fc1'][k], 3) + R(10 + k * 50, 30, 32, 20, '#ffffff', 2) + Ci(26 + k * 50, 40, 6, ['#e0915a', '#f3d58a', '#d9302c', '#c8903a'][k]) for k in range(4))
g += ''.join(E(50 + k * 100, 140, 30, 8, '#c58b54') + R(48 + k * 100, 140, 4, 34, '#8a5a35') + bowl(40 + k * 100, 130, 18, pattern=None) + bowl(60 + k * 100, 130, 18, pattern=None) for k in range(2))
S_('food-court', g, False)
# toy-store 玩具店：橱窗里摆着泰迪熊、小汽车和气球
def teddy(x, y, s):
    return G(Ci(-14, -30, 8, '#c8903a') + Ci(14, -30, 8, '#c8903a') + Ci(0, -18, 18, '#c8903a') + E(0, 12, 20, 22, '#c8903a') + E(0, -12, 8, 6, '#e8c8a0') + Ci(-6, -22, 2.5, '#2f3437') + Ci(6, -22, 2.5, '#2f3437') + E(0, 16, 10, 12, '#e8c8a0'), f'translate({x},{y}) scale({s})')
S_('toy-store', R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#fbe8f0', '#ef8fa4', door=False) + teddy(70, 140, .9) + car_side(140, 160, '#3c7fc1', .3) + Ci(140, 100, 12, '#f3c234') + L(140, 112, 140, 140, '#5d6469', 1) + Ci(120, 90, 10, '#e2463b') + L(120, 100, 130, 140, '#5d6469', 1), False)
# bookstore 书店：橱窗里一排排书，一本打开的书标志
S_('bookstore', R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#f2ead8', '#3c7fc1', sign='#3c7fc1', door=False) + Pa('M100,42 L84,38 L84,54 L100,58 Z', '#ffffff') + Pa('M100,42 L116,38 L116,54 L100,58 Z', '#e6ecef') + shelf_unit(34, 96, 132, 74, 3, 5), False)
# shoe-store 鞋店：橱窗里几双鞋子
def shoe(x, y, s, col):
    return G(Pa('M-30,0 L-30,-20 Q-28,-28 -18,-26 L-4,-16 Q14,-12 28,-8 Q36,-4 34,4 L-30,4 Z', col) + R(-32, 2, 68, 6, '#2f3437', 3) + L(-14, -20, -8, -14, '#ffffff', 2), f'translate({x},{y}) scale({s})')
S_('shoe-store', R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#f2ead8', '#8a5a35', door=False) + R(34, 120, 132, 6, '#c4cbd0') + R(34, 160, 132, 6, '#c4cbd0') + shoe(70, 118, .8, '#e2463b') + shoe(130, 118, .8, '#3c7fc1') + shoe(70, 158, .8, '#2f3437') + shoe(130, 158, .8, '#f3c234'), False)
# florist 花店：门口摆满一桶桶鲜花
S_('florist', R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#f6efe0', '#ef8fa4') + ''.join(R(14 + k * 36, 150, 28, 32, '#a7adb1', 3) + ''.join(flower(20 + k * 36 + j * 8, 140 - (j % 2) * 8, .6, ['#e2463b', '#f3c234', '#ef8fa4', '#7a4fa0', '#ffffff'][(k + j) % 5]) for j in range(3)) for k in range(5)), False)
# electronics-store 电器店：橱窗里电视、手机和笔记本电脑
g = R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#e6ecef', '#3c7fc1', door=False) + R(40, 96, 60, 40, '#2f3437', 3) + R(44, 100, 52, 32, '#5aa1d4') + R(66, 136, 8, 8, '#2f3437')
g += R(110, 100, 20, 36, '#2f3437', 4) + R(112, 104, 16, 26, '#9fd0ec') + Pa('M136,120 L176,120 L180,140 L132,140 Z', '#a7adb1') + R(140, 96, 32, 24, '#2f3437', 2) + R(143, 99, 26, 18, '#9fd0ec') + R(40, 150, 120, 20, '#ffffff', 2) + bolt_icon(100, 160, .2)
S_('electronics-store', g, False)
# information-desk 服务台：柜台上方 i 标志，工作人员在后面
S_('information-desk', R(0, 0, 200, 200, '#e6ecef') + person_bust(100, 74, 24, '#3c7fc1', '#5a3a2a', 'bun') + R(20, 120, 160, 80, '#5aa1d4', 4) + R(14, 114, 172, 10, '#3c7fc1', 3) + Ci(100, 156, 18, '#ffffff') + T(100, 166, 'i', 28, '#3c7fc1', 900) + Ci(40, 30, 16, '#3c7fc1') + T(40, 38, '?', 20, '#ffffff', 900), False)
S_('shopping-bag', bag_(40, 80, 80, 96, '#e2463b') + bag_(100, 100, 66, 76, '#3c7fc1') + R(116, 120, 30, 20, '#ffffff', 3, 'opacity=".5"'))
# opening-hours 营业时间：门上挂着的营业时间牌和时钟
S_('opening-hours', R(0, 0, 200, 200, '#bfe6fa') + R(40, 30, 120, 170, '#a9d8f2') + L(100, 0, 100, 40, '#5d6469', 2) + St('M80,40 L100,20 L120,40', '#5d6469', 2) + R(50, 40, 100, 70, '#ffffff', 6) + T(100, 70, '9:00', 18, '#2f3437', 900) + T(100, 96, '21:00', 18, '#2f3437', 900) + L(70, 78, 130, 78, '#a7adb1', 1) + clock(100, 150, 30, (9, 0)), False)
# lost-and-found 失物招领：桌上一箱失物：雨伞、钱包、钥匙、帽子，问号
g = box_(50, 110, 110, 70) + St('M70,80 Q70,60 90,60 Q110,60 110,80 L110,130', '#3c7fc1', 5) + Pa('M60,80 Q90,40 120,80 Z', '#3c7fc1') + R(120, 96, 30, 22, '#8a5a35', 4) + R(64, 100, 30, 14, '#e2463b', 6) + T(160, 60, '?', 40, '#f3c234', 900)
S_('lost-and-found', g)

# ================= 超市 =================
S_('supermarket', R(0, 180, 200, 20, WALK) + storefront(10, 40, 180, 140, '#ffffff', '#5ba644', sign='#5ba644', door=True) + cart_(100, 60, .2) + shelf_unit(24, 96, 80, 70, 3, 2), False)
S_('cart', cart_(100, 130, 1.3) + ''.join(R(40 + k * 18, 52 - (k % 2) * 6, 14, 26, ['#e2463b', '#f3c234', '#5ba644', '#3c7fc1', '#f08a24'][k], 2) for k in range(5)))
# basket 购物篮：红色塑料购物篮，提手，里面装着东西
g = Pa('M30,90 L170,90 L156,176 L44,176 Z', '#e2463b') + ''.join(R(48 + (k % 6) * 18, 110 + (k // 6) * 22, 10, 14, '#c0302a', 2) for k in range(12)) + St('M50,90 Q60,40 100,40 Q140,40 150,90', '#2f3437', 6)
g += R(60, 70, 20, 30, '#ffffff', 3) + Ci(110, 80, 14, '#e0392f') + R(124, 64, 22, 34, '#f3c234', 3)
S_('basket', g)
S_('shelf-supermarket', shelf_unit(20, 20, 160, 170, 5, 3), False)
# aisle 过道：两排货架中间的通道，往远处延伸
g = R(0, 0, 200, 200, '#e6ecef') + Pa('M0,0 L80,60 L80,150 L0,200 Z', '#d9dcde') + Pa('M200,0 L120,60 L120,150 L200,200 Z', '#d9dcde') + Pa('M0,200 L80,150 L120,150 L200,200 Z', '#c4cbd0')
for side in (0, 1):
    for k in range(5):
        t = k / 5
        if side == 0: g += Pa(f'M0,{20+k*36} L80,{70+k*16} L80,{78+k*16} L0,{30+k*36} Z', '#a7adb1') + ''.join(R(6 + j * 14, 6 + k * 36 + j * 8, 8, 10, ['#e2463b', '#5ba644', '#f3c234', '#3c7fc1', '#f08a24'][j], 1) for j in range(5))
        else: g += Pa(f'M200,{20+k*36} L120,{70+k*16} L120,{78+k*16} L200,{30+k*36} Z', '#a7adb1') + ''.join(R(186 - j * 14, 6 + k * 36 + j * 8, 8, 10, ['#ef8fa4', '#7cc05a', '#f08a24', '#9fd0ec', '#e2463b'][j], 1) for j in range(5))
g += cart_(100, 176, .35)
S_('aisle', g, False)
# checkout 收银台：传送带上放着商品，收银机，扫码
g = R(0, 0, 200, 200, '#e6ecef') + R(10, 110, 140, 30, '#2f3437', 3) + R(10, 140, 140, 60, '#c4cbd0') + R(150, 70, 44, 130, '#c4cbd0') + R(154, 60, 36, 26, '#2f3437', 3) + R(158, 64, 28, 12, '#7fe08a', 1)
g += R(30, 90, 20, 22, '#e2463b', 2) + Ci(72, 100, 11, '#f08a24') + R(90, 86, 24, 26, '#f3c234', 2) + R(120, 96, 18, 16, '#3c7fc1', 2) + St('M140,104 L160,96', '#e2463b', 2, 'opacity=".8"')
S_('checkout', g, False)
# snacks 零食：薯片袋、饼干、糖果放在一起
S_('snacks', Pa('M30,60 Q40,50 50,60 L80,60 Q90,50 100,60 L96,170 L34,170 Z', '#f3c234') + E(66, 110, 20, 14, '#e2463b') + R(110, 100, 60, 70, '#3c7fc1', 4) + ''.join(Ci(124 + (k % 3) * 16, 120 + (k // 3) * 20, 6, '#d9a050') for k in range(6)) + G(Pa('M-22,0 L-36,-12 L-34,0 L-36,12 Z', '#e2463b') + Pa('M22,0 L36,-12 L34,0 L36,12 Z', '#e2463b') + E(0, 0, 24, 16, '#e2463b'), 'translate(140,60)'))
S_('drinks', R(24, 70, 40, 110, '#d9302c', 6) + E(44, 70, 20, 6, '#c4cbd0') + bottle_shape(76, 40, 44, 140, '#9fd0ec', .32) + R(90, 28, 16, 14, '#3c7fc1', 3) + R(76, 100, 44, 30, '#3c7fc1') + R(130, 90, 46, 90, '#ffffff', 2) + R(130, 120, 46, 40, '#f5a43a') + Pa('M130,90 L153,70 L176,90 Z', '#e6ecef'))
S_('plastic-bag', Pa('M50,70 L150,70 L160,180 L40,180 Z', '#f6f6f2', 'opacity=".95"') + Pa('M50,70 L56,30 L76,30 L80,70 Z M150,70 L144,30 L124,30 L120,70 Z', '#f6f6f2') + ''.join(St(f'M{60+k*20},90 Q{56+k*20},130 {64+k*20},170', '#e6e6e0', 2) for k in range(5)) + Ci(80, 80, 14, '#e0392f', 'opacity=".5"') + R(110, 60, 20, 30, '#f3c234', 2, 'opacity=".5"'))
# frozen-food 冷冻食品：冷柜里结霜的冷冻水饺、冰淇淋盒，雪花
g = R(20, 70, 160, 110, '#e6ecef', 6) + R(28, 60, 144, 50, '#dff1fb', 4, 'opacity=".9"') + R(36, 84, 40, 24, '#3c7fc1', 2) + R(82, 84, 40, 24, '#ef8fa4', 2) + R(128, 84, 36, 24, '#7cc05a', 2) + ''.join(T(50 + k * 50, 50, '❄', 20, '#5aa1d4') for k in range(3)) + ''.join(Ci(40 + k * 22, 64, 2, '#ffffff') for k in range(6))
S_('frozen-food', g)
# special-offer 特价：货架上的醒目黄色爆炸贴“买一送一”样式（图形）
g = shelf_unit(20, 40, 160, 150, 3, 7) + G(''.join(Pa(f'M0,0 L{50*math.cos(a)},{50*math.sin(a)} L{50*math.cos(a+.2)},{50*math.sin(a+.2)} Z', '#000') for a in []) + Pa(' '.join(('M' if k == 0 else 'L') + f'{(48 if k%2==0 else 34)*math.cos(k*math.pi/10):.1f},{(48 if k%2==0 else 34)*math.sin(k*math.pi/10):.1f}' for k in range(20)) + ' Z', '#f3c234') + T(0, 6, '1+1', 22, '#e2463b', 900), 'translate(130,80)')
S_('special-offer', g, False)
# weigh 称重：电子秤上放着一袋苹果，屏幕显示重量
g = R(30, 130, 140, 40, '#e6ecef', 6) + R(40, 120, 120, 12, '#c4cbd0', 3) + R(70, 146, 60, 16, '#2f3437', 2) + T(100, 159, '0.85kg', 12, '#7fe08a', 800) + Pa('M60,120 L140,120 L132,70 L68,70 Z', '#f6f6f2', 'opacity=".9"') + ''.join(Ci(80 + (k % 3) * 20, 106 - (k // 3) * 18, 10, '#e0392f') for k in range(5))
S_('weigh', g)
# label 标签：商品上贴着的白色标签，写着信息
S_('label', R(40, 50, 120, 110, '#e98a86', 10) + R(50, 70, 100, 60, '#ffffff', 4) + ''.join(L(60, 84 + k * 12, 140 - k * 20, 84 + k * 12, '#5d6469', 3) for k in range(3)) + arrow(170, 30, 140, 66, '#3c7fc1', 4))
S_('barcode', R(30, 50, 140, 100, '#ffffff', 4) + ''.join(R(42 + x, 62, w, 70, '#2f3437') for x, w in [(0, 3), (5, 2), (9, 4), (15, 2), (19, 3), (24, 5), (31, 2), (35, 3), (40, 2), (44, 4), (50, 3), (55, 2), (59, 5), (66, 2), (70, 3), (75, 4), (81, 2), (85, 3), (90, 2), (94, 4), (100, 2), (104, 3), (109, 5), (116, 2)]) + T(100, 146, '6 901234 567892', 10, '#2f3437', 700) + St('M20,96 L180,96', '#e2463b', 2, 'opacity=".8"'))
# best-before 保质期至：牛奶盒上印着日期，旁边日历
g = R(30, 66, 80, 112, '#ffffff', 2) + Pa('M30,66 L70,30 L110,66 Z', '#e6ecef') + R(30, 96, 80, 30, '#3c7fc1') + R(40, 140, 60, 22, '#f3c234', 2) + T(70, 156, '25.10', 13, '#2f3437', 900)
g += R(124, 70, 60, 60, '#ffffff', 4) + R(124, 70, 60, 16, '#e2463b', 4) + T(154, 120, '25', 22, '#2f3437', 900) + arrow(110, 150, 130, 130, '#e2463b', 3)
S_('best-before', g)
# loyalty-card 会员卡：印着星星的会员卡，攒积分印章
S_('loyalty-card', G(R(-70, -44, 140, 88, '#f3c234', 8) + ''.join(Ci(-46 + (k % 5) * 23, -10 + (k // 5) * 30, 9, '#ffffff') + (star(-46 + (k % 5) * 23, -10 + (k // 5) * 30, 7, '#e2463b') if k < 7 else '') for k in range(10)) + R(-60, -36, 50, 10, '#e0a820', 2), 'translate(100,104) rotate(-8)'))

# ================= 药店 =================
S_('pharmacy', R(0, 180, 200, 20, WALK) + storefront(20, 40, 160, 140, '#ffffff', '#5ba644') + R(150, 20, 40, 40, '#5ba644', 4) + cross_sign(170, 40, .9, '#ffffff'), False)
S_('pill', capsule(70, 90, 2.2, -30) + capsule(130, 130, 1.8, 20, '#3c7fc1', '#ffffff') + Ci(140, 70, 14, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + L(130, 70, 150, 70, '#d9dcde', 2) + Ci(60, 150, 12, '#f3c234'))
# pharmacist 药剂师：穿白大褂的药剂师，身后药柜，拿着药瓶
cx, cy, r = 90, 80, 28
g = R(0, 0, 200, 200, '#e6f4ec') + shelf_unit(0, 10, 200, 90, 3, 9) + body(cx, cy, r, '#7fc4c0', w=r * 3.6) + coat_over(cx, cy, r, w=r * 3.6) + face_full(cx, cy, r, '#3a2a20', 'bun', 'dot', 'smile') + Ci(cx - r * .34, cy, 6, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(cx + r * .34, cy, 6, 'none', 'stroke="#2f3437" stroke-width="2"')
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 1.6), (cx + r * 2.1, cy + r * 1.0)], '#ffffff', SK, 13) + pill_bottle(cx + r * 2.2, cy + r * .9, 22, 30)
S_('pharmacist', g, False)
# painkiller 止痛药：药盒和药片，旁边一道红色闪电被划掉
S_('painkiller', R(30, 80, 90, 70, '#ffffff', 4) + R(30, 80, 90, 20, '#e2463b', 4) + cross_sign(75, 125, .8, '#e2463b') + Ci(150, 60, 12, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + Ci(160, 140, 30, 'none', 'stroke="#5ba644" stroke-width="4"') + Pa('M164,118 L150,140 L160,140 L152,162 L172,134 L162,134 L170,118 Z', '#e2463b') + L(140, 160, 180, 120, '#5ba644', 4))
S_('band-aid', bandage(100, 100, 150, 46, -20) + bandage(140, 160, 70, 22, 20))
# mask 口罩：蓝色医用口罩，耳挂带子
S_('mask', R(40, 70, 120, 70, '#9fd0ec', 12) + ''.join(L(44, 86 + k * 16, 156, 86 + k * 16, '#7fb7d8', 2) for k in range(3)) + St('M40,80 Q10,100 40,130', '#ffffff', 4) + St('M160,80 Q190,100 160,130', '#ffffff', 4) + L(80, 72, 120, 72, '#c4cbd0', 3))
# cough-syrup 止咳糖浆：棕色药瓶和量杯里的红色糖浆
S_('cough-syrup', bottle_shape(40, 40, 70, 140, '#8a4a1a', .38) + R(62, 28, 26, 16, '#ffffff', 3) + R(46, 100, 58, 44, '#ffffff', 3) + cross_sign(75, 122, .6, '#e2463b') + Pa('M126,120 L170,120 L164,176 L132,176 Z', '#eef6fa', 'opacity=".9"') + Pa('M128,140 L168,140 L164,176 L132,176 Z', '#c0283a') + ''.join(L(126, 130 + k * 10, 134, 130 + k * 10, '#a7adb1', 1.5) for k in range(4)))
# cold-medicine 感冒药：药盒上画着打喷嚏的鼻子/温度计图案，冲剂袋
S_('cold-medicine', R(30, 60, 100, 110, '#ffffff', 4) + R(30, 60, 100, 30, '#3c7fc1', 4) + Ci(80, 130, 22, '#dff1fb') + Pa('M70,124 Q80,116 90,124 L90,134 L70,134 Z', '#f1c7a3') + drop(96, 140, 4, '#9fd0ec') + R(140, 90, 40, 70, '#f3c234', 4) + L(140, 104, 180, 104, '#e0a820', 2) + cross_sign(160, 132, .5, '#e2463b'))
S_('eye-drops', G(R(-14, -10, 28, 70, '#ffffff', 8) + Pa('M-10,-10 L10,-10 L4,-50 L-4,-50 Z', '#ffffff') + R(-14, 10, 28, 30, '#5aa1d4', 2), 'translate(70,110) rotate(-20)') + drop(110, 110, 8, '#9fd0ec') + E(150, 100, 30, 18, '#ffffff') + Ci(150, 100, 12, '#5a3a2a') + Ci(150, 100, 6, '#2f3437') + St('M120,90 Q150,70 180,90', '#3a2a20', 3))
S_('thermometer', G(R(-14, -70, 28, 120, '#ffffff', 14) + R(-14, -70, 28, 120, 'none', 14, 'stroke="#d9dcde" stroke-width="3"') + R(-10, -48, 20, 50, '#cfe8d0', 3) + T(0, -14, '36.5', 10, '#2f3437', 800, extra='transform="rotate(90 0 -22)"') + R(-4, 50, 8, 26, '#c4cbd0', 3), 'translate(100,96) rotate(-30)'))
# dose 剂量：药盒格子上标着早中晚各吃几片
g = R(20, 70, 160, 80, '#e6ecef', 6) + ''.join(R(28 + k * 50, 78, 44, 64, ['#f3d058', '#9fd0ec', '#9a8ac8'][k], 4) + ''.join(Ci(42 + k * 50 + j * 16, 120, 6, '#ffffff', 'stroke="#d9dcde" stroke-width="1"') for j in range(2 if k != 1 else 1)) for k in range(3))
g += Ci(50, 50, 12, '#f3c234') + Pa('M140,40 A12,12 0 1,0 152,58 A10,10 0 1,1 140,40 Z', '#7a6ab8') + ''.join(L(100 + 14 * math.cos(a), 50 + 14 * math.sin(a), 100 + 18 * math.cos(a), 50 + 18 * math.sin(a), '#f08a24', 2) for a in [k * math.pi / 4 for k in range(8)]) + Ci(100, 50, 10, '#f08a24')
S_('dose', g)
S_('ointment', G(Pa('M-60,-20 L30,-16 L30,16 L-60,20 Z', '#ffffff') + Pa('M-60,-20 L-66,-20 L-66,20 L-60,20 Z', '#d9dcde') + R(-44, -16, 60, 32, '#5ba644') + cross_sign(-14, 0, .5, '#ffffff') + R(30, -8, 12, 16, '#e6ecef', 2) + R(42, -10, 16, 20, '#2f3437', 3), 'translate(90,90) rotate(-15)') + St('M150,130 q14,-6 20,-18', '#f6f6f2', 8) + E(100, 160, 0, 0, '#000'))
S_('cotton-swab', ''.join(G(R(-3, -50, 6, 100, '#f6f1e4' if False else '#ffffff', 3) + E(0, -54, 7, 12, '#ffffff', 'stroke="#e6e6e0" stroke-width="1"') + E(0, 54, 7, 12, '#ffffff', 'stroke="#e6e6e0" stroke-width="1"') + R(-3, -44, 6, 88, '#9fd0ec', 3), f'translate({70+k*30},{100}) rotate({-20+k*15})') for k in range(3)) + R(40, 160, 120, 20, '#e6ecef', 4))
S_('antibiotics', R(40, 50, 120, 110, '#ffffff', 4) + R(40, 50, 120, 24, '#7a4fa0', 4) + capsule(80, 110, 1.6, -20, '#7a4fa0', '#ffffff') + capsule(120, 130, 1.6, 30, '#7a4fa0', '#ffffff') + R(56, 140, 88, 8, '#e6ecef', 2) + Pa('M120,90 L134,90 L134,82 L146,94 L134,106 L134,98 L120,98 Z', '#5ba644', 'opacity="0"') + G(Ci(0, 0, 10, '#7cc05a') + ''.join(Ci(10 * math.cos(a), 10 * math.sin(a), 4, '#7cc05a') for a in [k * math.pi / 3 for k in range(6)]) + Ci(-3, -2, 1.5, '#2f3437') + Ci(3, -2, 1.5, '#2f3437'), 'translate(150,170)') + no_sign(150, 170, 18) if False else R(40, 50, 120, 110, '#ffffff', 4) + R(40, 50, 120, 24, '#7a4fa0', 4) + capsule(80, 110, 1.6, -20, '#7a4fa0', '#ffffff') + capsule(120, 130, 1.6, 30, '#7a4fa0', '#ffffff'))
# sleeping-pill 安眠药：药瓶旁边月亮和 Zzz
S_('sleeping-pill', pill_bottle(70, 170, 60, 80, '#5a5a9a') + Ci(130, 150, 12, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + L(120, 150, 140, 150, '#d9dcde', 2) + Pa('M140,30 A24,24 0 1,0 166,66 A20,20 0 1,1 140,30 Z', '#f3c234') + zzz(110, 100, .8))
# hot-water-bottle 热水袋：橡胶热水袋，套着毛绒套，冒热气
S_('hot-water-bottle', Pa('M60,60 L140,60 Q160,60 160,80 L160,160 Q160,180 140,180 L60,180 Q40,180 40,160 L40,80 Q40,60 60,60 Z', '#e2463b') + R(84, 36, 32, 28, '#c0302a', 4) + R(80, 26, 40, 14, '#2f3437', 4) + ''.join(L(52, 90 + k * 14, 148, 90 + k * 14, '#c0302a', 3) for k in range(6)) + heart(100, 130, 18, '#ffffff') + steam(80, 24, 3, 18, '#c4cbd0', .7))

# ================= 紧急服务 =================
# help 救命：人挥手大喊，对话框里感叹号
S_('help', person(70, 190, shirt='#f3c234', pants='#3b4a5a', arms='up', mood='o') + bubble(150, 60, 70, 56, (110, 80)) + T(150, 76, 'SOS', 20, '#e2463b', 900))
S_('police', officer(100, 84, 32), False if False else True)
# fire 火：熊熊燃烧的大火
S_('fire', flame(100, 150, 2.0) + flame(60, 160, 1.0) + flame(146, 162, .9) + R(30, 160, 140, 14, '#5a3a24', 4))
# danger 危险：黄色三角警示牌，感叹号
S_('danger', Pa('M100,30 L176,166 L24,166 Z', '#f3c234') + Pa('M100,30 L176,166 L24,166 Z', 'none', 'stroke="#2f3437" stroke-width="8" stroke-linejoin="round"') + R(92, 72, 16, 54, '#2f3437', 6) + Ci(100, 144, 9, '#2f3437'))
# lost 迷路：老人站在岔路口，四个方向路牌，头上问号
g = R(0, 0, 200, 200, '#e6f0d8') + Pa('M80,200 L90,110 L110,110 L120,200 Z M0,150 L90,120 L90,130 L0,170 Z M200,140 L110,120 L110,130 L200,160 Z', WALK) + R(150, 40, 6, 100, '#8a5a35') + Pa('M120,50 L180,50 L188,58 L180,66 L120,66 Z', '#3c7fc1') + Pa('M186,76 L126,76 L118,84 L126,92 L186,92 Z', '#5ba644')
g += person(60, 186, shirt='#ef8fa4', pants='#5d6469', style='grey', hair=P['grey'], arms='down', s=.7, mood='o') + T(60, 50, '?', 30, '#e2463b', 900) + T(84, 64, '?', 20, '#e2463b', 900)
S_('lost', g, False)
S_('police-officer', officer(100, 76, 30) + R(150, 150, 20, 40, '#2f3437', 3))
S_('police-car', sky_ground(170, ROAD) + police_car(100, 168, 1.2) + St('M90,80 l-8,-8 M110,78 l0,-10 M126,80 l8,-8', '#e2463b', 3), False)
# firefighter 消防员：戴头盔、穿反光消防服的消防员，拿水管
cx, cy, r = 90, 80, 28
g = person_bust(cx, cy, r, '#2f2f2f', '#3a2a20', 'short', 'dot', 'flat') + R(cx - r * 1.7, cy + r * 1.8, r * 3.4, 8, '#f3f3a0') + R(cx - r * 1.7, cy + r * 2.5, r * 3.4, 8, '#f3f3a0')
g += Pa(f'M{cx-r*1.3},{cy-r*.3} Q{cx-r*1.1},{cy-r*1.6} {cx},{cy-r*1.6} Q{cx+r*1.1},{cy-r*1.6} {cx+r*1.3},{cy-r*.3} L{cx+r*1.5},{cy-r*.2} L{cx-r*1.5},{cy-r*.2} Z', '#d9302c') + R(cx - 8, cy - r * 1.4, 16, 14, '#f3c234', 2)
g += St('M150,200 Q160,140 180,120', '#c0a060', 10) + R(170, 106, 20, 20, '#a7adb1', 4) + ''.join(L(190, 116, 200, 100 + k * 8, '#9fd0ec', 3) for k in range(3))
S_('firefighter', g)
S_('fire-engine', sky_ground(170, ROAD) + fire_truck(100, 168, 1.0), False)
# accident 事故：两辆车撞在一起，冒烟，三角警示牌
g = sky_ground(160, ROAD) + G(car_side(0, 0, '#3c7fc1', .7), 'translate(64,166) rotate(-8)') + G(car_side(0, 0, '#e2463b', .7), 'translate(146,170) rotate(10) scale(-1,1)') + star(104, 120, 14, '#f3c234') + ''.join(Ci(100 + k * 8, 90 - k * 12, 8 + k * 2, '#a7adb1', 'opacity=".7"') for k in range(3))
g += Pa('M30,150 L44,126 L58,150 Z', '#e2463b') + Pa('M36,146 L44,132 L52,146 Z', '#f6f1e4')
S_('accident', g, False)
# thief 小偷：戴眼罩的小偷背着鼓鼓的袋子踮脚溜走
g = pose((90, 60), (92, 82), (100, 124), arms=[[(98, 86), (120, 74), (124, 56)]], legs=[[(96, 124), (80, 150), (70, 176)], [(104, 124), (124, 146), (134, 168)]], back_arm=[[(86, 86), (70, 100), (60, 96)]], shirt='#2f2f2f', pants='#3a3a4a', hr=15, tw=30)
g += R(76, 54, 28, 8, '#2f3437', 3) + Ci(84, 58, 3, '#ffffff') + Ci(96, 58, 3, '#ffffff') + Pa('M110,30 Q150,10 160,50 Q164,80 130,80 Q110,70 110,30 Z', '#c8a070') + T(138, 60, '¥', 20, '#8a6a3a', 900)
S_('thief', g)
S_('emergency-exit', R(0, 0, 200, 200, '#e6ecef') + R(30, 50, 140, 90, '#2f9a5a', 8) + running_man(80, 104, 1.3) + R(120, 62, 36, 66, '#ffffff', 2) + R(124, 66, 28, 58, '#2f9a5a') + arrow(70, 160, 140, 160, '#2f9a5a', 6), False)
# fire-alarm 火警警报：墙上红色的火警报警器，响铃
S_('fire-alarm', R(0, 0, 200, 200, '#e6ecef') + R(60, 50, 80, 100, '#d9302c', 8) + Ci(100, 90, 26, '#f6f1e4') + Ci(100, 90, 18, '#d9302c') + R(76, 126, 48, 14, '#ffffff', 3) + flame(100, 136, .15) + St('M40,70 q-10,20 0,40 M30,60 q-16,30 0,60 M160,70 q10,20 0,40 M170,60 q16,30 0,60', '#e2463b', 3), False)
# first-aid 急救：白底红十字的急救箱，打开里面有绷带
S_('first-aid', R(30, 70, 140, 100, '#ffffff', 10) + R(30, 70, 140, 100, 'none', 10, 'stroke="#d9dcde" stroke-width="3"') + cross_sign(100, 120, 1.4) + St('M80,70 Q80,44 100,44 Q120,44 120,70', '#2f3437', 6) + R(30, 96, 14, 6, '#d9dcde', 2) + R(156, 96, 14, 6, '#d9dcde', 2))
S_('fire-extinguisher', extinguisher(100, 180, 1.4))
# witness 目击者：一个人指着发生的事情，眼睛睁大，旁边警察记录
g = person(60, 186, shirt='#5aa1d4', pants='#3b4a5a', arms='wave', mood='o', s=.8) + E(54, 52, 0, 0, '#000') + officer(150, 96, 22) + R(110, 140, 24, 30, '#ffffff', 2) + ''.join(L(114, 146 + k * 6, 130, 146 + k * 6, '#a7adb1', 1.5) for k in range(3))
S_('witness', g)

# ================= 能源与供电 =================
S_('electricity', bulb(70, 80, 30) + plug_(150, 80, .8) + bolt_icon(110, 150, 1.0))
# gas 燃气：燃气灶上蓝色的火苗
S_('gas', R(30, 110, 140, 60, '#e6ecef', 6) + R(30, 104, 140, 12, '#2f3437', 3) + E(100, 104, 40, 8, '#5d6469') + ''.join(Pa(f'M{72+k*14},104 Q{66+k*14},86 {72+k*14},70 Q{78+k*14},86 {72+k*14},104 Z', '#3c7fc1') + Pa(f'M{72+k*14},104 Q{69+k*14},94 {72+k*14},86 Q{75+k*14},94 {72+k*14},104 Z', '#9fd0ec') for k in range(5)) + Ci(60, 140, 8, '#a7adb1') + Ci(140, 140, 8, '#a7adb1'))
# power 电力：高压电塔和电线，闪电
S_('power', R(0, 0, 200, 200, SKY) + pylon(60, 190, 150) + pylon(160, 190, 110) + St('M32,78 Q110,110 132,108 M88,78 Q130,104 188,108', '#2f3437', 2) + bolt_icon(110, 50, .9), False)
# energy 能源：太阳、风车、闪电合成的能量图标
S_('energy', Ci(60, 60, 26, '#f3c234') + ''.join(L(60 + 32 * math.cos(a), 60 + 32 * math.sin(a), 60 + 42 * math.cos(a), 60 + 42 * math.sin(a), '#f3c234', 4) for a in [k * math.pi / 4 for k in range(8)]) + turbine(150, 180, 100, .8) + bolt_icon(70, 150, 1.0) + St('M100,100 Q110,60 130,60', '#5d6469', 0))
# coal 煤：一堆黑亮的煤块，旁边铲子
random.seed(121)
S_('coal', ''.join(Pa(f'M{x-18},{y} L{x-10},{y-16} L{x+10},{y-18} L{x+20},{y-2} L{x+10},{y+14} L{x-12},{y+12} Z', random.choice(['#2f2f2f', '#3a3a3a', '#262626'])) + hi(x - 4, y - 8, 6, 3, .3) for x, y in [(60, 160), (100, 164), (140, 160), (80, 136), (120, 136), (100, 112)]) + spade_(170, 150, .6, 30))
# charge 充电：手机插着充电线，屏幕上电池在充电
S_('charge', R(60, 30, 80, 140, '#2f3437', 12) + R(66, 44, 68, 110, '#9fd0ec', 4) + R(84, 70, 32, 56, '#ffffff', 4) + R(92, 64, 16, 8, '#ffffff', 2) + R(88, 96, 24, 26, '#5ba644', 2) + bolt_icon(100, 98, .3, '#ffffff') + St('M100,170 L100,190', '#ffffff', 6) + plug_(100, 196, .4, 180, False))
S_('solar-panel', R(0, 0, 200, 200, SKY) + Ci(40, 40, 20, '#f3c234') + solar(40, 80, 140, 70) + L(110, 150, 110, 190, '#5d6469', 6) + R(0, 186, 200, 14, '#8cc06a'), False)
S_('wind-turbine', R(0, 0, 200, 200, SKY) + R(0, 180, 200, 20, '#8cc06a') + turbine(80, 186, 130, 1.1) + turbine(160, 186, 90, .7), False)
# power-station 发电站：大冷却塔冒着白汽，厂房和电线
g = R(0, 0, 200, 200, SKY) + R(0, 180, 200, 20, '#a7a09a') + Pa('M40,180 Q50,120 44,70 L96,70 Q90,120 100,180 Z', '#c4cbd0') + Pa('M110,180 Q118,130 114,90 L156,90 Q150,130 160,180 Z', '#b0b8c0')
g += ''.join(Ci(70 + k * 10, 60 - k * 14, 14 + k * 4, '#ffffff', 'opacity=".9"') for k in range(3)) + ''.join(Ci(136 + k * 8, 80 - k * 12, 10 + k * 3, '#ffffff', 'opacity=".9"') for k in range(3)) + pylon(186, 186, 80)
S_('power-station', g, False)
# electricity-bill 电费单：一张电费账单，上面闪电标志和金额
S_('electricity-bill', Pa('M40,20 L160,20 L160,180 L40,180 Z', '#ffffff') + R(40, 20, 120, 34, '#f3c234') + bolt_icon(62, 37, .35, '#ffffff') + ''.join(L(52, 74 + k * 16, 148, 74 + k * 16, '#a7adb1', 3) for k in range(5)) + R(90, 150, 60, 20, '#e2463b', 3) + T(120, 165, '¥168', 14, '#ffffff', 900))
# meter 电表/水表：墙上的电表，数字转盘
S_('meter', R(0, 0, 200, 200, '#e6dcc8') + R(50, 30, 100, 140, '#e6ecef', 6) + R(60, 50, 80, 30, '#2f3437', 3) + ''.join(R(64 + k * 15, 54, 12, 22, '#ffffff', 1) + T(70 + k * 15, 71, str([0, 3, 5, 8, 2][k]), 14, '#2f3437', 800) for k in range(5)) + Ci(100, 120, 22, '#ffffff') + L(100, 120, 112, 108, '#e2463b', 3) + bolt_icon(100, 158, .25), False)
# save-energy 节能：灯泡里一片绿叶，开关关掉
S_('save-energy', bulb(80, 80, 40, False) + leaf(66, 96, 30, 12, -60, '#5ba644') + R(140, 100, 40, 60, '#ffffff', 6) + R(140, 100, 40, 60, 'none', 6, 'stroke="#d9dcde" stroke-width="2"') + R(150, 128, 20, 24, '#5ba644', 4) + T(160, 90, 'OFF', 10, '#5ba644', 900))
# nuclear-power 核能：核电站圆顶和黄色辐射标志
S_('nuclear-power', R(0, 0, 200, 200, SKY) + R(0, 180, 200, 20, '#a7a09a') + Pa('M30,180 L30,120 Q30,80 70,80 Q110,80 110,120 L110,180 Z', '#e6ecef') + Pa('M120,180 Q128,130 124,90 L166,90 Q160,130 170,180 Z', '#c4cbd0') + Ci(70, 140, 22, '#f3c234') + Ci(70, 140, 5, '#2f3437') + ''.join(Pa(f'M70,140 L{70+18*math.cos(a)},{140+18*math.sin(a)} A18,18 0 0,1 {70+18*math.cos(a+1.05)},{140+18*math.sin(a+1.05)} Z', '#2f3437') for a in [k * 2.094 - 1.57 - .52 for k in range(3)]), False)
S_('power-line', R(0, 0, 200, 200, SKY) + R(0, 180, 200, 20, '#8cc06a') + pylon(40, 190, 140) + pylon(160, 190, 140) + ''.join(St(f'M{12+0},{85+k*0} Q100,{110+k*12} 188,{85}', '#2f3437', 2) for k in range(2)) + St('M20,120 Q100,150 180,120', '#2f3437', 2) + ''.join(E(80 + k * 30, 128 + abs(k - 1) * -4, 6, 4, '#5a4a3a') for k in range(0)), False)
# generator 发电机：带轮子的黄色小发电机，插着电线，灯泡亮
S_('generator', R(30, 90, 110, 70, '#f3c234', 8) + R(40, 100, 50, 40, '#2f3437', 4) + ''.join(L(44, 106 + k * 8, 86, 106 + k * 8, '#5d6469', 2) for k in range(4)) + R(100, 100, 30, 20, '#e0a820', 3) + St('M20,90 L20,70 L150,70 L150,90', '#2f3437', 5) + wheel(50, 166, 10) + wheel(120, 166, 10) + St('M140,130 Q170,130 170,100', '#2f3437', 3) + bulb(170, 64, 14))
# renewable 可再生的：绿色循环箭头，中间太阳和风车
S_('renewable', ''.join(St(f'M{100+60*math.cos(a)},{100+60*math.sin(a)} A60,60 0 0,1 {100+60*math.cos(a+1.6)},{100+60*math.sin(a+1.6)}', '#5ba644', 10) + Pa(f'M{100+60*math.cos(a+1.75)},{100+60*math.sin(a+1.75)} L{100+48*math.cos(a+1.5)},{100+48*math.sin(a+1.5)} L{100+72*math.cos(a+1.5)},{100+72*math.sin(a+1.5)} Z', '#5ba644') for a in [k * 2.094 for k in range(3)]) + Ci(84, 92, 14, '#f3c234') + turbine(116, 130, 36, .4) + leaf(90, 120, 20, 8, -40, '#7cc05a'))

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
