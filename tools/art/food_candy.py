from flat import *
from fig import *
import os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from food_cafe import coffee_cup, tall_glass, ice_cube, straw, no_sign, plate, sandwich, chair  # noqa

A = {}
SK = P['skin']

def wrapped(x, y, s, col, rot=0, stripe='#ffffff'):
    g = Pa('M-22,0 L-38,-14 L-36,0 L-38,14 Z', col) + Pa('M22,0 L38,-14 L36,0 L38,14 Z', col) + E(0, 0, 24, 18, col) + St('M-12,-14 Q0,0 -12,14 M4,-16 Q16,0 4,16', stripe, 3, 'opacity=".7"') + hi(-8, -8, 6, 3, .5)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def choc_bar(x, y, s, rot=0, bite=False):
    g = R(-40, -60, 80, 120, '#5a3018', 6)
    g += ''.join(R(-34 + c * 36, -54 + r_ * 28, 32, 24, '#6a3a1e', 3) + R(-32 + c * 36, -52 + r_ * 28, 28, 6, '#7a4a2a', 2) for c in range(2) for r_ in range(4))
    g += Pa('M-44,10 L44,10 L44,66 L-44,66 Z', '#d9453a') + R(-44, 10, 88, 8, '#f3c234')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def lolly(x, y, s, cols=('#ef8fa4', '#ffffff')):
    g = L(0, 0, 0, 90, '#ffffff', 5) + Ci(0, 0, 40, cols[0])
    for k in range(4):
        g += St(f'M0,0 m{-30+k*6},0 a{30-k*6},{30-k*6} 0 1,1 {60-k*12},0', cols[1], 5)
    return G(g, f'translate({x},{y}) scale({s})')

def glass_stem(cx, base, bowl_w, bowl_h, wine, kind='wine'):
    if kind == 'flute':
        g = Pa(f'M{cx-bowl_w/2},{base-110} L{cx+bowl_w/2},{base-110} L{cx+bowl_w/2-4},{base-50} Q{cx},{base-40} {cx-bowl_w/2+4},{base-50} Z', '#eef6fa', 'opacity=".9"')
        g += Pa(f'M{cx-bowl_w/2+1},{base-96} L{cx+bowl_w/2-1},{base-96} L{cx+bowl_w/2-4},{base-50} Q{cx},{base-42} {cx-bowl_w/2+4},{base-50} Z', wine)
    elif kind == 'martini':
        g = Pa(f'M{cx-bowl_w/2},{base-100} L{cx+bowl_w/2},{base-100} L{cx},{base-50} Z', '#eef6fa', 'opacity=".9"') + Pa(f'M{cx-bowl_w/2+8},{base-92} L{cx+bowl_w/2-8},{base-92} L{cx},{base-52} Z', wine)
    else:
        g = Pa(f'M{cx-bowl_w/2},{base-110} L{cx+bowl_w/2},{base-110} Q{cx+bowl_w/2+4},{base-60} {cx},{base-50} Q{cx-bowl_w/2-4},{base-60} {cx-bowl_w/2},{base-110} Z', '#eef6fa', 'opacity=".9"')
        g += Pa(f'M{cx-bowl_w/2-1},{base-84} L{cx+bowl_w/2+1},{base-84} Q{cx+bowl_w/2+2},{base-58} {cx},{base-52} Q{cx-bowl_w/2-2},{base-58} {cx-bowl_w/2-1},{base-84} Z', wine)
    g += R(cx - 2.5, base - 52, 5, 48, '#e6f2f8') + E(cx, base - 2, bowl_w * .4, 5, '#dfeef6')
    return g

def wine_bottle(cx, base, col='#5a1a24', label='#f6ecd8', h=150):
    return bottle_shape(cx - 22, base - h, 44, h, col, .32) + R(cx - 7, base - h - 16, 14, 18, '#8a1a24', 2) + R(cx - 18, base - h * .5, 36, h * .3, label, 3) + R(cx - 16, base - h * .7, 5, h * .6, '#ffffff', 2, 'opacity=".2"')

def beer_mug(cx, base, w=70, h=90):
    g = St(f'M{cx+w/2},{base-h*.75} q{w*.4},0 {w*.4},{h*.3} q0,{h*.3} {-w*.4},{h*.3}', '#e6f2f8', 10)
    g += R(cx - w / 2, base - h, w, h, '#f3b42a', 6) + R(cx - w / 2, base - h, w, h, 'none', 6, 'stroke="#e6f2f8" stroke-width="5"') + ''.join(L(cx - w / 2 + 14 + k * 14, base - h + 10, cx - w / 2 + 14 + k * 14, base - 8, '#f8d060', 3) for k in range(3))
    g += Pa(f'M{cx-w/2-4},{base-h} Q{cx-w/2},{base-h-20} {cx-w/4},{base-h-16} Q{cx},{base-h-28} {cx+w/4},{base-h-16} Q{cx+w/2+2},{base-h-22} {cx+w/2+4},{base-h} Z', '#ffffff')
    return g

def tumbler(cx, base, w, h, liquid, level=.5):
    return (Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w/2-3},{base} L{cx-w/2+3},{base} Z', '#eef6fa', 'opacity=".9"') + Pa(f'M{cx-w/2+1},{base-h*level} L{cx+w/2-1},{base-h*level} L{cx+w/2-3},{base} L{cx-w/2+3},{base} Z', liquid) + R(cx - w / 2 + 2, base - 8, w - 4, 8, '#dfeef6', 2))

def burger(x, y, s):
    g = Pa('M-50,0 Q-50,-44 0,-44 Q50,-44 50,0 Z', '#d9903a') + ''.join(E(-28 + k * 14, -28 + (k % 2) * 8, 3, 2, '#fbf3dc') for k in range(5))
    g += Pa('M-54,0 q9,8 18,0 q9,8 18,0 q9,8 18,0 q9,8 18,0 q9,8 18,0 q9,8 18,0 L54,4 L-54,4 Z', '#5ba644') + R(-52, 2, 104, 8, '#f3c234', 2) + R(-50, 10, 100, 14, '#6a3a1e', 6) + R(-52, 24, 104, 16, '#d9903a', 8)
    return G(g, f'translate({x},{y}) scale({s})')

def fries(x, y, s):
    g = ''.join(R(-26 + k * 9, -50 + (k % 3) * 8, 8, 56, '#f3c234', 2, f'transform="rotate({(k-3)*4} {-22+k*9} 0)"') for k in range(7))
    g += Pa('M-34,-10 L34,-10 L26,40 L-26,40 Z', '#d9453a') + Pa('M-34,-10 Q0,6 34,-10 L32,0 Q0,14 -32,0 Z', '#c0302a') + Ci(0, 18, 8, '#f3c234')
    return G(g, f'translate({x},{y}) scale({s})')

def cola_cup(x, y, s, col='#d9453a'):
    g = Pa('M-26,-40 L26,-40 L20,40 L-20,40 Z', col) + R(-30, -48, 60, 10, '#ffffff', 4) + R(-12, -10, 24, 24, '#ffffff', 12, 'opacity=".8"') + straw(8, -80, 4, -40, '#ffffff')
    return G(g, f'translate({x},{y}) scale({s})')

def steak_plate(x, y, s, inside='#8a5a3a', band=None):
    g = E(0, 24, 84, 22, '#d9dcde') + E(0, 20, 84, 22, '#ffffff')
    g += Pa('M-66,10 Q-68,-22 -30,-24 Q0,-26 6,-10 Q10,10 -4,18 Q-40,26 -66,10 Z', '#6a3018') + ''.join(L(-54 + k * 14, -18, -48 + k * 14, 18, '#3a1a10', 3) for k in range(4))
    for k in range(3):
        sx = 18 + k * 20
        sl = R(0, 0, 18, 44, '#4a2010', 4) + R(3, 3, 12, 38, band or inside, 3)
        if band: sl += R(5, 8, 8, 28, inside, 3)
        g += G(sl, f'translate({sx},{-24+k*2}) rotate({8+k*6})')
    g += Ci(-40, 30, 6, '#5ba644') + Ci(-24, 34, 5, '#5ba644') + Ci(64, 30, 6, '#f08a24')
    return G(g, f'translate({x},{y}) scale({s})')

# ================= 糖果 =================
A['candy'] = svg(wrapped(70, 80, 1.3, '#e2463b') + wrapped(132, 100, 1.2, '#5aa1d4', 30) + wrapped(90, 146, 1.2, '#f3c234', -20) + wrapped(150, 154, .9, '#5ba644', 10))
A['chocolate'] = svg(choc_bar(84, 100, 1.1, -12) + G(R(0, 0, 32, 24, '#6a3a1e', 3) + R(2, 2, 28, 6, '#7a4a2a', 2), 'translate(140,140) rotate(20)') + G(R(0, 0, 32, 24, '#6a3a1e', 3), 'translate(150,100) rotate(-10)'))
A['lollipop'] = svg(lolly(100, 80, 1.3))
# chewing-gum 口香糖：一包口香糖片，吹出粉色泡泡
g = R(30, 100, 90, 60, '#5aa1d4', 6) + ''.join(R(36 + k * 16, 70 + (k % 2) * 6, 14, 50, '#ffffff', 2) + R(36 + k * 16, 70 + (k % 2) * 6, 14, 14, '#c4e4f2', 2) for k in range(5)) + R(30, 120, 90, 40, '#3c7fc1', 6)
g += Ci(150, 70, 32, '#f6a0b8') + Ci(150, 70, 32, 'none', 'stroke="#ef8fa4" stroke-width="2"') + hi(138, 58, 8, 5, .7)
A['chewing-gum'] = svg(g)
# popsicle 冰棍：木棍上的双色冰棍，咬了一口
g = R(92, 130, 16, 50, '#e0c090', 6) + Pa('M66,40 Q66,20 100,20 Q134,20 134,40 L134,140 L66,140 Z', '#ef8fa4') + Pa('M66,90 L134,90 L134,140 L66,140 Z', '#f3c234') + Ci(132, 32, 12, '#f1e8d4') + hi(80, 50, 5, 20, .4) + drop(120, 156, 6, '#ef8fa4')
A['popsicle'] = svg(g)
# marshmallow 棉花糖：粉白相间的圆柱软糖
def mm(x, y, col):
    return E(x, y + 14, 20, 8, shade(col, -.08)) + R(x - 20, y - 14, 40, 28, col) + E(x, y - 14, 20, 8, shade(col, .2))
A['marshmallow'] = svg(mm(70, 100, '#ffffff') + mm(120, 92, '#f6c0cc') + mm(96, 140, '#f6c0cc') + mm(146, 140, '#ffffff') + mm(52, 150, '#e0f0f8'))
# toffee 太妃糖：金棕色方块糖，用透明纸包着
def tof(x, y, rot):
    return G(Pa('M-30,-18 L-44,-26 L-40,0 L-44,26 L-30,18 Z M30,-18 L44,-26 L40,0 L44,26 L30,18 Z', '#f0e8d8', 'opacity=".9"') + R(-30, -20, 60, 40, '#c8803a', 6) + R(-26, -16, 52, 10, '#d9963e', 4), f'translate({x},{y}) rotate({rot})')
A['toffee'] = svg(tof(76, 90, -10) + tof(130, 120, 15) + tof(80, 150, 5))
# caramel 焦糖：勺子上滴下金黄浓稠的焦糖，小锅
g = bowl(80, 120, 110, '#5d6469', fill='#c8782a', pattern=None) + R(130, 116, 50, 10, '#2f3437', 5)
g += G(R(-4, -60, 8, 70, '#c4cbd0', 4) + E(0, 18, 14, 20, '#c4cbd0') + E(0, 18, 10, 14, '#c8782a'), 'translate(80,56) rotate(-10)') + St('M84,92 Q86,104 82,116', '#c8782a', 5) + drop(82, 116, 5, '#c8782a')
A['caramel'] = svg(g)
# jelly-beans 软糖豆：一堆五颜六色的豆形软糖
random.seed(71)
g = ''.join(G(Pa('M-12,-6 Q-12,-14 0,-12 Q10,-12 12,-4 Q14,8 2,8 Q-4,4 -8,8 Q-14,6 -12,-6 Z', c) + hi(-4, -8, 4, 2, .6), f'translate({x:.0f},{y:.0f}) rotate({r_:.0f}) scale(1.4)') for x, y, r_, c in [(random.uniform(40, 160), random.uniform(70, 160), random.uniform(0, 360), random.choice(['#e2463b', '#f3c234', '#5ba644', '#5aa1d4', '#ef8fa4', '#f08a24', '#7a4fa0', '#ffffff'])) for _ in range(22)])
A['jelly-beans'] = svg(g)
# cotton-candy 棉花糖：木棍上一大团粉色蓬松的云
g = L(100, 110, 100, 186, '#e0c090', 5)
random.seed(72)
g += ''.join(Ci(100 + random.uniform(-40, 40), 70 + random.uniform(-36, 36), random.uniform(18, 26), random.choice(['#f6b8cc', '#f8c8d8', '#f2a8c0'])) for _ in range(20))
A['cotton-candy'] = svg(g)
# hard-candy 硬糖：玻璃罐里透亮的彩色圆糖
g = R(40, 60, 120, 116, '#eef6fa', 18, 'opacity=".85"') + R(56, 40, 88, 22, '#c4cbd0', 6)
random.seed(73)
g += ''.join(Ci(x, y, 12, c) + hi(x - 4, y - 4, 4, 3, .7) for x, y, c in [(random.uniform(56, 144), random.uniform(80, 162), random.choice(['#e2463b', '#f3c234', '#5ba644', '#5aa1d4', '#f08a24'])) for _ in range(18)]) + R(48, 70, 8, 96, '#ffffff', 4, 'opacity=".5"')
A['hard-candy'] = svg(g)
# fudge 乳脂软糖：一摞厚厚的方块软糖
def cube(x, y, s, top, side1, side2):
    return Pa(f'M{x},{y} L{x+s},{y-s*.4} L{x+s*2},{y} L{x+s},{y+s*.4} Z', top) + Pa(f'M{x},{y} L{x+s},{y+s*.4} L{x+s},{y+s*1.2} L{x},{y+s*.8} Z', side1) + Pa(f'M{x+s},{y+s*.4} L{x+s*2},{y} L{x+s*2},{y+s*.8} L{x+s},{y+s*1.2} Z', side2)
g = plate(100, 160, 84) + cube(36, 120, 30, '#8a5030', '#6a3a1e', '#5a3018') + cube(96, 122, 30, '#e8c890', '#d6b070', '#c8a060') + cube(66, 92, 30, '#8a5030', '#6a3a1e', '#5a3018')
A['fudge'] = svg(g)
# licorice 甘草糖：黑色扭绳状长条糖
g = ''.join(G(R(-70, -9, 140, 18, '#2f2a27', 9) + ''.join(L(-60 + k * 12, -9, -54 + k * 12, 9, '#4a4440', 2.5) for k in range(11)), f'translate(100,{70+i*30}) rotate({-10+i*7})') for i in range(4))
A['licorice'] = svg(g)
# candy-bar 巧克力棒：包装纸撕开、咬了一口的巧克力棒
g = G(R(-80, -22, 160, 44, '#d9453a', 6) + R(-80, -6, 160, 12, '#f3c234') + Pa('M-80,-22 L-90,-14 L-80,-6 L-90,2 L-80,10 L-90,18 L-80,22 Z', '#c0302a') +
      R(40, -18, 50, 36, '#6a3a1e', 4) + Ci(90, -2, 14, '#f1e8d4') + Pa('M40,-22 L52,-28 L48,-18 L58,-26 L56,22 L40,22 Z', '#c0302a'), 'translate(96,104) rotate(-15)')
A['candy-bar'] = svg(g)
# sweet-tooth 爱吃甜食：眼睛冒爱心，看着一桌蛋糕和糖果
cx, cy, r = 76, 80, 30
g = diner(cx, cy, r, '#ef8fa4', '#3a2a20', 'long', '', 'smile', None, '#ef9a8a')
g += heart(cx - r * .34, cy, 7, '#e2463b') + heart(cx + r * .34, cy, 7, '#e2463b') + Pa(f'M{cx-r*.3},{cy+r*.42} Q{cx},{cy+r*.8} {cx+r*.3},{cy+r*.42} Z', '#9a3a30')
g += lolly(150, 50, .55) + wrapped(160, 120, .8, '#5aa1d4', 20) + G(Pa('M0,40 L0,0 L60,-14 L60,26 Z', '#f6e2a8') + Pa('M0,0 L34,-26 L60,-14 Z', '#ef8fa4') + Ci(34, -22, 6, '#d9453a'), 'translate(130,150) scale(.8)')
A['sweet-tooth'] = svg(g)
# peppermint 薄荷糖：红白螺旋的圆形薄荷糖
def mint(x, y, r):
    g = Ci(x, y, r, '#ffffff')
    for k in range(6):
        a0 = k * math.pi / 3
        g += Pa(f'M{x},{y} Q{x+r*.9*math.cos(a0+.4)},{y+r*.9*math.sin(a0+.4)} {x+r*math.cos(a0+.5)},{y+r*math.sin(a0+.5)} A{r},{r} 0 0,1 {x+r*math.cos(a0+.9)},{y+r*math.sin(a0+.9)} Q{x+r*.4*math.cos(a0+.4)},{y+r*.4*math.sin(a0+.4)} {x},{y} Z', '#e2463b')
    return g + Ci(x, y, r, 'none', 'stroke="#f0e8e8" stroke-width="2"') + hi(x - r * .4, y - r * .4, r * .2, r * .12, .7, -30)
A['peppermint'] = svg(mint(76, 90, 40) + mint(140, 136, 30))

# ================= 酒吧 =================
A['beer'] = svg(beer_mug(90, 176, 80, 110))
A['wine'] = svg(wine_bottle(60, 178) + glass_stem(110, 180, 44, 0, '#8a1a2a') + glass_stem(156, 180, 40, 0, '#f0dc90'))
# cheers 干杯：两只啤酒杯碰在一起，溅出泡沫
g = G(beer_mug(0, 0, 60, 84), 'translate(70,170) rotate(15)') + G(beer_mug(0, 0, 60, 84), 'translate(132,170) rotate(-15) scale(-1,1)')
g += Ci(100, 60, 5, '#ffffff') + Ci(90, 48, 4, '#ffffff') + Ci(112, 50, 3, '#ffffff') + St('M80,34 l-6,-10 M100,30 l0,-12 M120,34 l6,-10', '#f3c234', 3)
A['cheers'] = svg(g)
# ice 冰块：冰桶里装满冰块，冰夹
g = Pa('M40,90 L160,90 L148,176 L52,176 Z', '#c4cbd0') + Pa('M40,90 L160,90 L156,104 L44,104 Z', '#a7adb1')
g += ice_cube(64, 84, 26, 10) + ice_cube(96, 78, 28, -15) + ice_cube(130, 84, 26, 20) + ice_cube(80, 60, 24, 30) + ice_cube(116, 58, 22, -5)
g += St('M150,30 L120,70 M160,36 L128,74', '#5d6469', 4)
A['ice'] = svg(g)
A['red-wine'] = svg(glass_stem(80, 184, 60, 0, '#8a1a2a') + ''.join(Ci(140 + (k % 3) * 12 - (k // 3) * 6, 110 + (k // 3) * 12, 8, '#6a2a5a') for k in range(9)) + leaf(146, 98, 20, 8, -40, '#5ba644'))
A['white-wine'] = svg(wine_bottle(60, 178, '#c8d890', '#ffffff') + glass_stem(124, 184, 56, 0, '#f0dc90'))
# soft-drink 软饮料：易拉罐和一杯冒气泡的汽水
g = R(36, 70, 56, 106, '#5ba644', 8) + E(64, 70, 28, 7, '#c4cbd0') + E(64, 176, 28, 6, '#a7adb1') + Ci(64, 122, 14, '#ffffff') + R(40, 76, 6, 94, '#ffffff', 3, 'opacity=".3"')
g += tall_glass(110, 70, 60, 106, '#f3c234', .8) + ''.join(Ci(122 + (k * 13) % 40, 100 + (k * 17) % 60, 2.5, '#ffffff') for k in range(10)) + straw(156, 40, 146, 150, '#e2463b')
A['soft-drink'] = svg(g)
# cocktail 鸡尾酒：倒三角酒杯里的彩色鸡尾酒，插小伞和柠檬片
g = glass_stem(96, 186, 100, 0, '#ef6a7a', 'martini') + Ci(140, 88, 14, '#f3d034') + Ci(140, 88, 10, '#fbe98a')
g += L(80, 100, 64, 40, '#8a5a35', 2) + Pa('M40,44 Q64,20 88,44 Z', '#5aa1d4') + Pa('M52,44 Q64,20 76,44 Z', '#ffffff')
A['cocktail'] = svg(g)
# whisky 威士忌：方瓶琥珀色威士忌和一只矮杯
g = R(40, 60, 64, 116, '#c8782a', 6) + R(56, 36, 32, 26, '#c8782a', 3) + R(60, 24, 24, 14, '#2f2a27', 3) + R(46, 100, 52, 40, '#f6ecd8', 3) + R(44, 66, 8, 104, '#ffffff', 3, 'opacity=".25"')
g += tumbler(146, 176, 56, 60, '#c8782a', .45)
A['whisky'] = svg(g)
# champagne 香槟：瓶塞飞出、泡沫喷出，配高脚香槟杯
g = G(bottle_shape(-22, -150, 44, 150, '#2f5a3a', .32) + R(-12, -158, 24, 18, '#d9b030', 2) + R(-18, -70, 36, 40, '#f6ecd8', 3), 'translate(70,180) rotate(-20)')
g += E(30, 30, 10, 7, '#d9a868') + ''.join(Ci(36 + k * 6, 40 + (k % 2) * 8, 4, '#ffffff') for k in range(4))
g += glass_stem(150, 186, 32, 0, '#f6e2a0', 'flute') + ''.join(Ci(146 + (k % 2) * 6, 100 + k * 10, 1.8, '#ffffff') for k in range(5))
A['champagne'] = svg(g)
# liquor 白酒：白瓷酒瓶和小酒杯
g = Pa('M50,176 Q40,120 60,96 L60,60 Q60,48 76,48 Q92,48 92,60 L92,96 Q112,120 102,176 Z', '#ffffff') + Pa('M60,40 L92,40 L92,52 L60,52 Z', '#d9453a') + Pa('M60,120 L92,120 L94,150 L58,150 Z', '#d9453a') + Ci(76, 135, 8, '#f3c234')
g += Pa('M124,140 L164,140 L158,176 L130,176 Z', '#ffffff') + E(144, 140, 20, 5, '#eef6fa') + Pa('M128,146 L160,146 L158,176 L130,176 Z', '#ffffff', 'stroke="#e6ecef" stroke-width="1"')
A['liquor'] = svg(g)
# bartender 酒保：穿马甲的酒保，摇着调酒壶
cx, cy, r = 92, 80, 30
g = R(0, 170, 200, 30, '#5a3a24') + body(cx, cy, r, '#ffffff', w=r * 3.6) + Pa(f'M{cx-r*1.7},200 L{cx-r*1.7},{cy+r*1.5} L{cx-r*.3},{cy+r*1.2} L{cx-r*.1},200 Z M{cx+r*1.7},200 L{cx+r*1.7},{cy+r*1.5} L{cx+r*.3},{cy+r*1.2} L{cx+r*.1},200 Z', '#2f3437')
g += Pa(f'M{cx-10},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx-10},{cy+r*1.3} Z M{cx+10},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx+10},{cy+r*1.3} Z', '#2f3437')
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'smile', None) + St(f'M{cx-r*.4},{cy+r*.34} q{r*.4},{-r*.1} {r*.8},0', '#3a2a20', 3)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.4), (cx + r * 2.1, cy + r * .4)], '#ffffff', SK, 15)
g += G(Pa('M-14,-40 L14,-40 L18,30 L-18,30 Z', '#c4cbd0') + R(-12, -54, 24, 16, '#a7adb1', 4) + hi(-8, -10, 3, 14, .6), f'translate({cx+r*2.1},{cy-r*.2}) rotate(15)') + St(f'M{cx+r*2.8},{cy-r*1.0} q8,6 0,14 M{cx+r*1.4},{cy-r*1.0} q-8,6 0,14', '#a7adb1', 2.5)
A['bartender'] = svg(g, shadow=False)
# pub 酒馆：老式酒馆门面，挂着啤酒杯招牌
g = R(20, 60, 160, 120, '#3a5a3a', 4) + R(14, 50, 172, 20, '#2f4a2f', 3) + R(36, 90, 54, 60, '#f3d58a', 3) + ''.join(L(36 + k * 18, 90, 36 + k * 18, 150, '#3a5a3a', 3) for k in range(1, 3)) + L(36, 120, 90, 120, '#3a5a3a', 3)
g += R(110, 90, 46, 90, '#5a3a24', 3) + Ci(148, 136, 3, '#d9a33a') + St('M170,20 L170,40 L190,40', '#2f3437', 3) + G(beer_mug(0, 0, 26, 32), 'translate(180,80)')
A['pub'] = svg(g, shadow=False)
# non-alcoholic 无酒精：啤酒瓶贴着 0.0% 标签
g = bottle_shape(70, 40, 60, 140, '#8a5a1a', .32) + R(88, 26, 24, 16, '#f3c234', 3) + R(74, 110, 52, 40, '#ffffff', 4) + T(100, 138, '0.0%', 16, '#5ba644', 900)
g += Ci(156, 60, 16, '#5ba644') + St('M148,60 l6,6 l10,-12', '#ffffff', 4)
A['non-alcoholic'] = svg(g)
# drunk 醉的：脸红、眼睛打转、头上冒泡泡，手拿酒瓶
cx, cy, r = 86, 86, 30
g = diner(cx, cy, r, '#5aa1d4', '#3a2a20', 'short', '', 'wavy', None, '#e2463b')
for sx in (-1, 1):
    ex = cx + sx * r * .34
    g += St(f'M{ex},{cy} m-1,0 a2,2 0 1,1 3,1 a4,4 0 1,1 -6,-2 a6,6 0 1,1 9,3', '#2b211b', 1.6)
g += E(cx, cy + r * .2, r * .5, r * .25, '#e2463b', 'opacity=".35"')
g += Ci(cx + 26, cy - 46, 5, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + Ci(cx + 40, cy - 60, 7, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + Ci(cx + 56, cy - 76, 9, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"')
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.8), (cx + r * 2.2, cy + r * 1.0)], shade('#5aa1d4', -.2), SK, 15) + G(wine_bottle(0, 0, '#3a6a3a', '#f6ecd8', 90), f'translate({cx+r*2.4},{cy+r*1.4}) rotate(30) scale(.8)')
A['drunk'] = svg(g)
# on-the-rocks 加冰块：矮杯里大冰块泡着威士忌
g = tumbler(100, 176, 100, 100, '#c8782a', .55) + ice_cube(84, 112, 34, 12) + ice_cube(118, 116, 30, -10) + ice_cube(100, 90, 28, 25)
A['on-the-rocks'] = svg(g)

# ================= 餐厅 =================
# menu 菜单：打开的菜单本，两页菜名和图片
g = Pa('M100,40 L20,30 L20,170 L100,180 Z', '#8a2a24') + Pa('M100,40 L180,30 L180,170 L100,180 Z', '#7a2420') + Pa('M98,46 L28,38 L28,162 L98,172 Z', '#fbf3e0') + Pa('M102,46 L172,38 L172,162 L102,172 Z', '#f6ecd4')
for k in range(4):
    g += Ci(42, 62 + k * 26, 7, ['#e0915a', '#5ba644', '#f3c234', '#d9453a'][k]) + L(54, 60 + k * 26, 90, 62 + k * 26, '#a7adb1', 3) + L(116, 60 + k * 26, 160, 58 + k * 26, '#a7adb1', 3) + L(116, 68 + k * 26, 140, 66 + k * 26, '#c4cbd0', 2)
A['menu'] = svg(g)
# bill 账单：小托盘上放着长条小票和笔
g = R(30, 120, 140, 50, '#2f3437', 8) + G(Pa('M0,0 L60,0 L60,110 L54,104 L48,110 L42,104 L36,110 L30,104 L24,110 L18,104 L12,110 L6,104 L0,110 Z', '#ffffff') + ''.join(L(8, 16 + k * 14, 52 - (k % 2) * 14, 16 + k * 14, '#a7adb1', 2.5) for k in range(5)) + L(8, 90, 52, 90, '#2f3437', 3), 'translate(60,40) rotate(-6)')
g += G(R(0, -3, 70, 6, '#3c7fc1', 3) + Pa('M70,-3 L80,0 L70,3 Z', '#c4cbd0'), 'translate(110,150) rotate(-30)')
A['bill'] = svg(g)
# tip 小费：账单旁边压着几枚硬币和一张钞票
g = G(R(0, 0, 90, 50, '#8cc06a', 4) + Ci(45, 25, 14, '#6aaa4a') + R(6, 6, 78, 38, 'none', 3, 'stroke="#ffffff" stroke-width="2"'), 'translate(30,90) rotate(-10)')
for k, (x, y) in enumerate([(130, 120), (150, 110), (140, 140), (160, 136)]):
    g += Ci(x, y, 16, '#d9a33a') + Ci(x, y, 12, '#f3c234') + T(x, y + 5, '¥', 12, '#b8862a', 900)
g += coffee_cup(150, 50, 40)
A['tip'] = svg(g)
# chef 厨师：高高的厨师帽，白色双排扣厨师服
cx, cy, r = 100, 86, 30
g = body(cx, cy, r, '#ffffff', w=r * 3.6) + ''.join(Ci(cx + sx * 10, cy + r * (1.6 + k * .45), 3, '#a7adb1') for sx in (-1, 1) for k in range(3)) + St(f'M{cx-r*.5},{cy+r*1.0} L{cx+r*.5},{cy+r*1.0}', '#e2463b', 6)
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'smile', None, '#ef9a8a') + St(f'M{cx-r*.45},{cy+r*.32} q{r*.45},{-r*.15} {r*.9},0', '#3a2a20', 4)
g += Pa(f'M{cx-r*.9},{cy-r*.7} L{cx+r*.9},{cy-r*.7} L{cx+r*.8},{cy-r*1.2} Q{cx+r*1.3},{cy-r*1.6} {cx+r*.8},{cy-r*2.2} Q{cx+r*.4},{cy-r*2.6} {cx},{cy-r*2.2} Q{cx-r*.4},{cy-r*2.6} {cx-r*.8},{cy-r*2.2} Q{cx-r*1.3},{cy-r*1.6} {cx-r*.8},{cy-r*1.2} Z', '#ffffff') + R(cx - r * .9, cy - r * .9, r * 1.8, r * .3, '#e6ecef', 3)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.6), (cx + r * 2.2, cy + r * .6)], '#ffffff', SK, 15) + G(R(-4, -50, 8, 50, '#c4cbd0', 3) + E(0, -54, 12, 8, '#c4cbd0'), f'translate({cx+r*2.2},{cy+r*.5})')
A['chef'] = svg(g)
# dessert 甜点：盘中一块淋了酱的布丁/蛋糕，配勺子
g = plate(96, 150, 80) + Pa('M60,140 L66,90 Q96,80 126,90 L132,140 Z', '#f3c234') + Pa('M66,90 Q96,80 126,90 Q122,104 112,98 Q104,112 94,100 Q84,110 76,98 Q68,104 66,90 Z', '#7a3a1a') + Ci(96, 78, 8, '#d9453a') + leaf(102, 74, 10, 4, -40, '#5ba644')
g += G(R(-3, -40, 6, 50, '#c4cbd0', 3) + E(0, 14, 9, 12, '#c4cbd0'), 'translate(160,130) rotate(30)')
A['dessert'] = svg(g)
# waitress 女服务员：围裙，拿着小本子记菜
cx, cy, r = 90, 80, 30
g = body(cx, cy, r, '#2f3437', w=r * 3.6) + Pa(f'M{cx-r*1.1},{cy+r*1.6} L{cx+r*1.1},{cy+r*1.6} L{cx+r*1.3},200 L{cx-r*1.3},200 Z', '#ffffff') + R(cx - r * 1.2, cy + r * 1.5, r * 2.4, 8, '#ffffff', 3)
g += face_full(cx, cy, r, '#5a3a2a', 'bun', 'dot', 'smile', None, '#ef9a8a')
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 2.0), (cx + r * 1.2, cy + r * 1.6)], '#2f3437', SK, 14) + R(cx + r * .6, cy + r * 1.0, 30, 38, '#ffffff', 3) + ''.join(L(cx + r * .6 + 5, cy + r * 1.0 + 10 + k * 8, cx + r * .6 + 25, cy + r * 1.0 + 10 + k * 8, '#a7adb1', 2) for k in range(3))
g += arm([(cx - r * 1.6, 200), (cx - r * 1.8, cy + r * 2.0), (cx + r * .3, cy + r * 1.6)], '#2f3437', SK, 14) + L(cx + r * .3, cy + r * 1.6, cx + r * .8, cy + r * 1.1, '#3c7fc1', 3)
A['waitress'] = svg(g)
# reservation 预订：餐桌上立着预订牌（电话和时间），两套餐具
g = E(100, 150, 90, 20, '#ffffff') + E(100, 150, 90, 20, 'none', 'stroke="#e6ecef" stroke-width="2"')
g += Pa('M70,140 L84,80 L130,80 L144,140 Z', '#2f3437') + R(84, 84, 46, 50, '#2f3437') + Pa('M94,94 q-4,10 4,18 l6,-4 q-4,-4 -2,-10 Z', '#f3c234') + T(118, 112, '19:00', 13, '#ffffff', 800) + ''.join(L(90, 122 + k * 6, 124, 122 + k * 6, '#a7adb1', 1.5) for k in range(2))
g += E(40, 150, 16, 5, '#e6ecef') + E(160, 150, 16, 5, '#e6ecef') + L(20, 146, 20, 162, '#c4cbd0', 2) + L(180, 146, 180, 162, '#c4cbd0', 2)
A['reservation'] = svg(g)
# starter 开胃菜：小盘子里的开胃小菜（面包片配番茄）和一小碗汤
g = plate(66, 140, 54) + ''.join(R(36 + k * 20, 124 - (k % 2) * 4, 18, 14, '#d9a050', 4) + Ci(45 + k * 20, 122 - (k % 2) * 4, 5, '#e0392f') + Ci(42 + k * 20, 120 - (k % 2) * 4, 2, '#5ba644') for k in range(3))
g += bowl(146, 104, 60, fill='#e0915a') + Ci(146, 104, 4, '#5ba644') + steam(136, 92, 2, 14, '#c4cbd0', .6)
A['starter'] = svg(g)
# main-course 主菜：大盘子里的牛排、土豆和蔬菜
g = E(100, 146, 86, 26, '#d9dcde') + E(100, 140, 86, 26, '#ffffff') + Pa('M50,136 Q46,110 86,108 Q120,108 124,126 Q126,142 100,146 Q60,150 50,136 Z', '#6a3018') + ''.join(L(64 + k * 14, 112, 72 + k * 14, 142, '#3a1a10', 3) for k in range(4))
g += E(140, 128, 14, 10, '#e0c070') + E(150, 142, 12, 8, '#e0c070') + Ci(136, 146, 6, '#5ba644') + Ci(146, 116, 6, '#5ba644') + G(R(0, -4, 24, 8, '#f08a24', 3), 'translate(120,150) rotate(-20)')
g += L(20, 110, 20, 170, '#c4cbd0', 4) + L(180, 110, 180, 170, '#c4cbd0', 4)
A['main-course'] = svg(g)
# recommend 推荐：服务员竖大拇指，手指向一道菜
cx, cy, r = 70, 76, 28
g = body(cx, cy, r, '#ffffff', w=r * 3.6) + Pa(f'M{cx-10},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx-10},{cy+r*1.3} Z M{cx+10},{cy+r*1.05} L{cx},{cy+r*1.18} L{cx+10},{cy+r*1.3} Z', '#d9453a')
g += face_full(cx, cy, r, '#3a2a20', 'short', 'up', 'smile', None)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.6), (cx + r * 2.2, cy + r * .4)], '#ffffff', SK, 14, hand=False) + thumbs_up(cx + r * 2.2, cy + r * .2, .9)
g += plate(146, 162, 46) + Pa('M118,156 Q120,136 146,134 Q172,136 174,156 Z', '#e0915a') + Ci(146, 136, 5, '#5ba644') + star(176, 110, 9) + star(120, 104, 6)
A['recommend'] = svg(g)
# set-menu 套餐：托盘上一份主食、一份菜、一碗汤和一杯饮料
g = R(20, 70, 160, 110, '#c58b54', 8) + R(26, 76, 148, 98, '#d9a868', 6)
g += bowl(64, 104, 54, fill='#fbf8f0') + E(130, 108, 34, 12, '#ffffff') + E(130, 106, 24, 8, '#e0915a') + bowl(64, 150, 48, fill='#e0a050') + coffee_cup(136, 146, 32, '#c98a3a', saucer=False)
A['set-menu'] = svg(g)
# today-s-special 今日特价菜：小黑板上画着一颗星和一道菜
g = Pa('M56,190 L80,40 M144,190 L120,40', 'none', 'stroke="#8a5a35" stroke-width="6"') + R(40, 30, 120, 110, '#2f3a34', 6) + R(40, 30, 120, 110, 'none', 6, 'stroke="#8a5a35" stroke-width="8"')
g += star(100, 60, 16, '#f3c234') + St('M66,110 Q100,80 134,110', '#ffffff', 3) + L(60, 112, 140, 112, '#ffffff', 3) + Ci(100, 104, 4, '#ffffff') + ''.join(L(60, 124 + k * 6, 140 - k * 30, 124 + k * 6, '#c4cbd0', 1.5) for k in range(2))
A['today-s-special'] = svg(g)
# doggy-bag 打包袋：带提手的外卖盒，装剩菜带回家
g = Pa('M40,100 L160,100 L150,170 L50,170 Z', '#ffffff') + Pa('M40,100 L60,70 L100,86 Z', '#f2efe8') + Pa('M160,100 L140,70 L100,86 Z', '#e6e1d8') + Pa('M60,70 L140,70 L100,86 Z', '#f6f3ee')
g += St('M70,72 Q100,30 130,72', '#5d6469', 3) + R(70, 120, 60, 26, '#d9453a', 4) + heart(100, 132, 8, '#ffffff')
A['doggy-bag'] = svg(g)
# well-done 全熟：牛排切开，里面全是褐色
A['well-done'] = svg(steak_plate(100, 110, 1.1, '#8a5a3a'))
# medium-rare 五分熟：牛排切开，中间是粉红色
A['medium-rare'] = svg(steak_plate(100, 110, 1.1, '#e2564b', '#c97a6a'))
# service-charge 服务费：账单上额外加了 +10%
g = Pa('M50,20 L150,20 L150,180 L140,172 L130,180 L120,172 L110,180 L100,172 L90,180 L80,172 L70,180 L60,172 L50,180 Z', '#ffffff')
g += ''.join(L(62, 40 + k * 18, 120, 40 + k * 18, '#a7adb1', 3) + L(126, 40 + k * 18, 140, 40 + k * 18, '#a7adb1', 3) for k in range(4)) + L(60, 116, 140, 116, '#2f3437', 2)
g += R(60, 124, 80, 26, '#f3c234', 4) + T(100, 143, '+10%', 18, '#2f3437', 900)
A['service-charge'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
