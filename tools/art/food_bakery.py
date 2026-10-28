from flat import *
from fig import *
import os, sys, random

A = {}
SK = P['skin']
CR = '#c8803a'; CRD = '#a8642a'; IN = '#f6e2b8'

def loaf(cx, cy, w, h, col=CR):
    g = Pa(f'M{cx-w/2},{cy+h/2} L{cx-w/2},{cy} Q{cx-w/2},{cy-h/2} {cx},{cy-h/2} Q{cx+w/2},{cy-h/2} {cx+w/2},{cy} L{cx+w/2},{cy+h/2} Z', col)
    g += ''.join(St(f'M{cx-w*.3+k*w*.2},{cy-h*.4} q{w*.08},{h*.15} {w*.12},{h*.3}', shade(col, .3), 3) for k in range(4))
    g += hi(cx - w * .25, cy - h * .2, w * .12, h * .08, .3, -10)
    return g

def bread_slice(cx, cy, s, col=CR, inner=IN, rot=0):
    d = 'M-30,40 L-30,-10 Q-44,-14 -40,-30 Q-34,-46 0,-46 Q34,-46 40,-30 Q44,-14 30,-10 L30,40 Z'
    g = Pa(d, col) + G(Pa(d, inner), 'scale(.84) translate(0,2)')
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def cake_slice(x, y, s, sponge='#f6e2a8', cream='#ffffff', top='#ef8fa4', fruit='#d9453a'):
    g = Pa('M0,40 L0,0 L80,-20 L80,20 Z', sponge) + Pa('M0,14 L80,-6 L80,0 L0,20 Z', cream) + Pa('M0,0 L46,-36 L80,-20 Z', top) + Pa('M0,0 L80,-20 L80,-14 L0,6 Z', cream)
    g += Ci(46, -30, 7, fruit)
    return G(g, f'translate({x},{y}) scale({s})')

def round_cake(cx, cy, w, h, body='#fbf3e6', top='#ffffff', drip='#ef8fa4'):
    g = R(cx - w / 2, cy - h / 2, w, h, body, 6) + E(cx, cy + h / 2, w / 2, w * .12, shade(body, -.06)) + E(cx, cy - h / 2, w / 2, w * .12, top)
    g += Pa(f'M{cx-w/2},{cy-h/2} ' + ' '.join(f'q{w/16},{14 if k%2 else 6} {w/8},0' for k in range(8)) + f' L{cx+w/2},{cy-h/2} Z', drip)
    return g

def candle(x, y, h=26, col='#5aa1d4'):
    return R(x - 3, y - h, 6, h, col, 2) + ''.join(L(x - 3, y - h + 4 + k * 6, x + 3, y - h + 7 + k * 6, '#ffffff', 1.5) for k in range(h // 6)) + Pa(f'M{x},{y-h-14} Q{x+6},{y-h-6} {x},{y-h-2} Q{x-6},{y-h-6} {x},{y-h-14} Z', '#f3c234') + Pa(f'M{x},{y-h-9} Q{x+3},{y-h-5} {x},{y-h-3} Q{x-3},{y-h-5} {x},{y-h-9} Z', '#f08a24')

def plate(cx, cy, rx):
    return E(cx, cy + 4, rx, rx * .26, '#d9dcde') + E(cx, cy, rx, rx * .26, '#ffffff')

# =============== 面包店（一） ===============
A['bread'] = svg(loaf(84, 110, 120, 70) + bread_slice(150, 130, .9, rot=10))

# cake 蛋糕：奶油草莓圆蛋糕
g = plate(100, 160, 84) + round_cake(100, 120, 130, 64)
g += ''.join(Ci(56 + k * 22, 86, 8, '#d9453a') + leaf(56 + k * 22, 79, 6, 2.5, -90, '#5ba644') for k in range(5))
A['cake'] = svg(g)

# cookie 饼干：几块圆曲奇，带巧克力豆
def cookie(x, y, r):
    random.seed(int(x + y))
    return Ci(x, y, r, '#d9a050') + Ci(x, y, r * .88, '#e6b468') + ''.join(Ci(x + random.uniform(-r * .6, r * .6), y + random.uniform(-r * .6, r * .6), r * .1 + 1, '#5a3a24') for _ in range(7))
A['cookie'] = svg(cookie(70, 90, 36) + cookie(136, 110, 30) + cookie(96, 150, 28))

# toast 吐司：烤面包机弹出两片烤好的吐司
g = R(36, 100, 128, 76, '#c4cbd0', 18) + R(36, 100, 128, 20, '#e6ecef', 10) + R(150, 130, 20, 8, '#5d6469', 3) + R(44, 150, 112, 4, '#a7adb1', 2)
g += bread_slice(78, 82, .8, '#a8642a', '#d9a050') + bread_slice(124, 76, .8, '#a8642a', '#d9a050')
g += R(56, 100, 44, 10, '#5d6469', 3) + R(102, 100, 44, 10, '#5d6469', 3)
A['toast'] = svg(g)

# bun 小圆面包：几个圆面包，一个掰开有红豆馅
g = E(70, 100, 40, 30, CR) + hi(56, 86, 12, 5, .35, -10) + E(140, 90, 34, 26, CR) + ''.join(Ci(130 + k * 8, 76, 1.5, '#fbf8f0') for k in range(3))
g += E(110, 150, 44, 22, IN) + Pa('M66,150 A44,22 0 0,0 154,150 Z', CR) + E(110, 148, 24, 10, '#7a2a30')
A['bun'] = svg(g)

A['loaf'] = svg(loaf(100, 108, 150, 84))

# slice 片：一条面包切成一片一片
g = loaf(70, 110, 90, 70)
for k in range(4):
    g += bread_slice(126 + k * 12, 116, .7, rot=8)
g += G(R(0, -4, 70, 8, '#c4cbd0', 3) + R(68, -5, 30, 10, '#5a3a24', 4), 'translate(100,40) rotate(20)')
A['slice'] = svg(g)

# baker 面包师：高帽白衣，端着一盘面包
cx, cy, r = 100, 80, 30
g = body(cx, cy, r, '#ffffff', w=r * 3.6) + St(f'M{cx-r*.4},{cy+r*1.0} L{cx},{cy+r*1.5} L{cx+r*.4},{cy+r*1.0}', '#d9453a', 6)
g += ''.join(Ci(cx, cy + r * (1.9 + k * .5), 3, '#c4cbd0') for k in range(3))
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'smile', None, '#ef9a8a')
g += Pa(f'M{cx-r*.9},{cy-r*.7} L{cx+r*.9},{cy-r*.7} L{cx+r*.8},{cy-r*1.2} Q{cx+r*1.3},{cy-r*1.6} {cx+r*.8},{cy-r*2.2} Q{cx+r*.4},{cy-r*2.6} {cx},{cy-r*2.2} Q{cx-r*.4},{cy-r*2.6} {cx-r*.8},{cy-r*2.2} Q{cx-r*1.3},{cy-r*1.6} {cx-r*.8},{cy-r*1.2} Z', '#ffffff')
g += R(cx - r * .9, cy - r * .9, r * 1.8, r * .3, '#e6ecef', 3)
g += R(cx - r * 2.6, cy + r * 2.4, r * 2.2, 6, '#a7adb1', 2) + loaf(cx - r * 2.0, cy + r * 2.15, 30, 20) + loaf(cx - r * 1.1, cy + r * 2.15, 26, 18)
g += arm([(cx - r * 1.6, 200), (cx - r * 1.9, cy + r * 2.6), (cx - r * 1.5, cy + r * 2.5)], '#ffffff', SK, 15)
A['baker'] = svg(g)

# pie 派：格子面的苹果派，切掉一块
g = plate(100, 150, 84)
g += Pa('M30,134 A70,30 0 0,0 170,134 L170,124 A70,30 0 0,1 30,124 Z', CRD) + E(100, 124, 70, 30, '#d9a050')
g += ''.join(L(44 + k * 16, 104, 34 + k * 16 + 10, 148, '#f0c070', 5) for k in range(7)) + ''.join(L(34, 112 + k * 9, 166, 112 + k * 9, '#f0c070', 5) for k in range(3))
g += Pa('M100,124 L170,124 A70,30 0 0,1 150,146 Z', '#e8c070') + Pa('M100,124 L150,146 L150,154 L100,132 Z', '#c06a3a')
g = g.replace('<path d="M100,124 L170,124 A70,30 0 0,1 150,146 Z"', '<path d="M100,124 L170,124 A70,30 0 0,1 150,146 Z"')
A['pie'] = svg(g)

# muffin 松饼：纸杯里鼓起的蓝莓松饼
def muffin(x, y, s, top='#d9a050', dots='#3c4f9a'):
    g = Pa('M-28,0 L28,0 L20,44 L-20,44 Z', '#7fb7d8') + ''.join(L(-24 + k * 8, 2, -16 + k * 6, 42, '#5aa1d4', 2) for k in range(7))
    g += Pa('M-36,4 Q-40,-36 0,-40 Q40,-36 36,4 Z', top) + ''.join(Ci(-20 + k * 10, -18 + (k % 2) * 12, 4, dots) for k in range(5)) + hi(-14, -26, 8, 4, .35)
    return G(g, f'translate({x},{y}) scale({s})')
A['muffin'] = svg(muffin(100, 110, 1.9))

# doughnut 甜甜圈：粉色糖霜带彩色糖粒
def donut(x, y, r, icing='#ef8fa4'):
    random.seed(int(x))
    g = Ci(x, y, r, '#d9a050') + Pa(f'M{x-r*.95},{y} ' + ' '.join(f'q{r*.12},{r*.18*(1 if k%2 else -.4)} {r*.24},0' for k in range(8)) + f' A{r*.95},{r*.95} 0 0,0 {x-r*.95},{y} Z', icing)
    g = Ci(x, y, r, '#d9a050') + Ci(x, y - 2, r * .9, icing) + Ci(x, y, r * .32, '#f1e8d4')
    g += ''.join(R(x + rr * math.cos(a), y + rr * math.sin(a), 6, 2.5, random.choice(['#ffffff', '#f3c234', '#5aa1d4', '#5ba644']), 1, f'transform="rotate({random.uniform(0,180):.0f} {x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f})"') for a, rr in [(random.uniform(0, 6.28), random.uniform(r * .45, r * .8)) for _ in range(16)])
    return g
A['doughnut'] = svg(donut(84, 96, 50) + donut(150, 150, 30, '#7a4a2a'))

# croissant 牛角包：弯弯的金黄牛角包
g = ''
for k, (rx, ry, a) in enumerate([(22, 18, -60), (26, 22, -30), (30, 26, 0), (26, 22, 30), (22, 18, 60)]):
    x = 100 + 62 * math.sin(math.radians(a)); y = 120 - 30 * math.cos(math.radians(a)) + 20
    g += E(x, y, rx, ry, '#d9903a' if k % 2 else '#c8782a', f'transform="rotate({a} {x:.0f} {y:.0f})"')
    g += St(f'M{x-rx*.6:.0f},{y-ry*.4:.0f} q{rx*.6:.0f},{ry*.5:.0f} {rx*1.2:.0f},0', '#f0b860', 2.5)
g += Pa('M34,140 q-10,10 -4,18 Z M166,140 q10,10 4,18 Z', '#c8782a')
A['croissant'] = svg(g)

# baguette 法棍：细长的法式长棍面包，斜刀口
g = G(R(-86, -16, 172, 32, '#c8803a', 16) + ''.join(Pa(f'M{-60+k*30},-12 q12,6 22,-2', 'none', 'stroke="#f0c070" stroke-width="5" stroke-linecap="round"') for k in range(5)) + hi(-40, -8, 30, 4, .3), 'translate(100,90) rotate(-25)')
g += G(R(-60, -14, 120, 28, '#b8702a', 14) + ''.join(Pa(f'M{-40+k*28},-10 q12,6 22,-2', 'none', 'stroke="#e8b060" stroke-width="5" stroke-linecap="round"') for k in range(4)), 'translate(110,150) rotate(-5)')
A['baguette'] = svg(g)

# whole-wheat 全麦：褐色全麦面包片和麦穗
random.seed(41)
g = bread_slice(78, 110, 1.3, '#7a4a24', '#b8865a') + ''.join(E(random.uniform(52, 104), random.uniform(80, 150), 2.5, 1.5, '#6a3a1a') for _ in range(26))
def ear(x, y, s, rot):
    e = St('M0,60 L0,-30', '#c9a24a', 3) + ''.join(E(-6, -20 + i * 11, 5, 9, '#e0b85a', 'transform="rotate(-25 -6 %d)"' % (-20 + i * 11)) + E(6, -20 + i * 11, 5, 9, '#d6aa48', 'transform="rotate(25 6 %d)"' % (-20 + i * 11)) for i in range(5))
    return G(e + E(0, -34, 4, 8, '#e0b85a'), f'translate({x},{y}) rotate({rot}) scale({s})')
g += ear(150, 104, 1.1, 10) + ear(172, 112, 1.0, 22)
A['whole-wheat'] = svg(g)

# roll 面包卷：篮子里几个小餐包
g = Pa('M30,120 L170,120 L156,176 L44,176 Z', '#c58b54') + ''.join(L(34 + i * 2.4, 130 + i * 12, 166 - i * 2.4, 130 + i * 12, '#a8703e', 2.5) for i in range(4)) + Pa('M30,120 L60,100 L140,100 L170,120 Z', '#f6f1ea')
for x, y in [(64, 106), (100, 96), (136, 106), (82, 120), (120, 120)]:
    g += E(x, y, 22, 16, CR) + St(f'M{x-10},{y-6} q10,-6 20,0', '#f0c070', 3)
A['roll'] = svg(g)

# crust 面包皮：一片面包，箭头指着外圈的褐色硬皮
g = bread_slice(96, 110, 1.6, '#8a4a1a', IN)
g += St('M160,40 L136,62', '#d9453a', 4) + Pa('M130,68 L134,54 L144,62 Z', '#d9453a')
g += St('M150,170 L134,148', '#d9453a', 4) + Pa('M130,142 L140,146 L134,154 Z', '#d9453a')
A['crust'] = svg(g)

# =============== 面包店（二） ===============
# birthday-cake 生日蛋糕：两层蛋糕插着蜡烛
g = plate(100, 170, 84) + round_cake(100, 148, 130, 40, '#fbf3e6', '#ffffff', '#ef8fa4') + round_cake(100, 108, 90, 36, '#fbf3e6', '#ffffff', '#5aa1d4')
g += candle(80, 84, 26, '#ef8fa4') + candle(100, 82, 28, '#f3c234') + candle(120, 84, 26, '#5ba644')
g += ''.join(Ci(48 + k * 26, 150, 4, '#d9453a') for k in range(5))
A['birthday-cake'] = svg(g)

# cupcake 纸杯蛋糕：螺旋奶油顶，上面一颗樱桃
def cupcake(x, y, s, cream='#ef8fa4'):
    g = Pa('M-28,0 L28,0 L20,44 L-20,44 Z', '#f3c234') + ''.join(L(-24 + k * 8, 2, -16 + k * 6, 42, '#d9a020', 2) for k in range(7))
    for k, (rx, yy) in enumerate([(34, -4), (28, -18), (20, -30), (12, -40)]):
        g += E(0, yy, rx, 10, cream if k % 2 else shade(cream, .15))
    g += Ci(0, -52, 7, '#d9453a') + St('M0,-58 q4,-8 10,-10', '#5a8a3a', 2)
    return G(g, f'translate({x},{y}) scale({s})')
A['cupcake'] = svg(cupcake(76, 116, 1.5) + cupcake(146, 136, 1.0, '#9fd0ec'))

# mooncake 月饼：圆形带花纹的月饼，切开露出蛋黄
def mooncake(x, y, r, cut=False):
    g = Ci(x, y + r * .25, r, '#a8642a') + Ci(x, y, r, '#d9903a') + Ci(x, y, r * .8, '#e8a850')
    g += ''.join(Ci(x + r * .9 * math.cos(a), y + r * .9 * math.sin(a), r * .16, '#d9903a') for a in [k * math.pi / 6 for k in range(12)])
    g += Ci(x, y, r * .5, 'none', 'stroke="#c8782a" stroke-width="3"') + ''.join(L(x, y, x + r * .5 * math.cos(a), y + r * .5 * math.sin(a), '#c8782a', 2) for a in [k * math.pi / 4 for k in range(8)])
    return g
g = mooncake(78, 92, 50)
g += Pa('M110,170 L110,130 A44,44 0 0,1 180,140 L180,170 Z', '#d9903a') + Pa('M110,170 L110,140 L180,150 L180,170 Z', '#7a3a24') + Ci(148, 158, 12, '#f3a024')
A['mooncake'] = svg(g)

# steamed-bun 馒头：蒸笼里白白胖胖的馒头
g = E(100, 150, 84, 24, '#a8703e') + R(16, 120, 168, 32, '#c58b54', 4) + E(100, 120, 84, 22, '#d9a868') + ''.join(L(16, 128 + k * 8, 184, 128 + k * 8, '#a8703e', 1.5) for k in range(3))
for x, y in [(62, 104), (108, 98), (148, 106), (88, 118), (128, 120)]:
    g += E(x, y, 24, 18, '#fbf8f0') + E(x, y + 6, 22, 10, '#efe8d8') + hi(x - 8, y - 8, 6, 3, .8)
g += steam(80, 70, 3, 20, '#c4cbd0', .8)
A['steamed-bun'] = svg(g)

# dough 面团：撒了面粉的案板上一团面，旁边擀面杖
g = board(100, 150, 180, 60, '#d9b07a') + E(90, 124, 54, 34, '#f6ecd4') + E(98, 134, 44, 20, '#ecdcb8') + hi(74, 110, 12, 6, .7)
random.seed(51)
g += ''.join(Ci(random.uniform(20, 180), random.uniform(130, 170), 1.5, '#ffffff') for _ in range(30))
g += G(R(-60, -8, 120, 16, '#e0b070', 8) + R(-80, -5, 22, 10, '#c8903a', 5) + R(58, -5, 22, 10, '#c8903a', 5), 'translate(110,64) rotate(-10)')
A['dough'] = svg(g)

# egg-tart 蛋挞：酥皮小碗里黄色蛋奶，表面焦斑
def tart(x, y, s, fill='#f3c234'):
    g = Pa('M-40,-6 Q-38,30 -28,34 L28,34 Q38,30 40,-6 Z', '#d9a050') + ''.join(L(-36 + k * 9, -2, -26 + k * 7, 32, '#c08038', 2) for k in range(9))
    g += E(0, -6, 40, 12, '#e8b868') + E(0, -6, 32, 9, fill) + Ci(-8, -8, 4, '#c8782a', 'opacity=".6"') + Ci(10, -4, 3, '#c8782a', 'opacity=".6"')
    return G(g, f'translate({x},{y}) scale({s})')
A['egg-tart'] = svg(tart(72, 104, 1.3) + tart(140, 140, 1.0))

# pastry 酥皮点心：一层层的千层酥
g = plate(100, 160, 84)
for i, (x, y) in enumerate([(70, 130), (126, 128), (98, 102)]):
    g += ''.join(R(x - 30, y - k * 6, 60, 6, '#f0c070' if k % 2 else '#e0a050', 3) for k in range(5)) + R(x - 30, y - 30, 60, 4, '#fbf8f0', 2) + Ci(x, y - 34, 6, '#d9453a')
A['pastry'] = svg(g)

# cheesecake 芝士蛋糕：奶白色三角芝士蛋糕，底部饼干层
g = plate(100, 160, 84) + Pa('M30,150 L30,108 L160,84 L160,128 Z', '#f6ecd0') + Pa('M30,150 L30,138 L160,116 L160,128 Z', '#b8763a')
g += Pa('M30,108 L110,70 L160,84 Z', '#fbf4dc') + Pa('M30,108 L160,84 L160,88 L30,112 Z', '#e8d8b0') + Pa('M96,76 q10,-8 22,-4 q-6,10 -22,4 Z', '#c0283a')
A['cheesecake'] = svg(g)

# sponge-cake 海绵蛋糕：金黄松软、满是小孔的戚风蛋糕
random.seed(53)
g = plate(100, 160, 84) + Pa('M30,150 L30,90 Q100,60 170,90 L170,150 Z', '#f6dc8a') + Pa('M30,90 Q100,60 170,90 L170,100 Q100,72 30,100 Z', '#c8903a')
g += ''.join(Ci(random.uniform(40, 160), random.uniform(104, 146), random.uniform(1.5, 3), '#e8c060') for _ in range(40))
A['sponge-cake'] = svg(g)

# waffle 华夫饼：方格华夫饼，淋着蜂蜜，配草莓
g = plate(100, 160, 84) + R(40, 70, 120, 84, '#d9a050', 10)
g += ''.join(R(48 + c * 22, 78 + r_ * 18, 16, 12, '#b8803a', 3) for c in range(5) for r_ in range(4))
g += St('M60,80 Q90,100 80,130 Q100,140 130,120', '#f0b030', 6, 'opacity=".9"') + Ci(140, 84, 10, '#d9453a') + Ci(152, 100, 8, '#d9453a')
A['waffle'] = svg(g)

# tart 水果挞：酥皮底，上面摆满草莓和猕猴桃
g = plate(100, 160, 84) + Pa('M30,130 Q32,150 46,152 L154,152 Q168,150 170,130 Z', '#d9a050') + E(100, 130, 70, 22, '#e8b868') + E(100, 128, 62, 18, '#f6e2a8')
for x, y in [(70, 124), (100, 118), (130, 124), (84, 134), (116, 134)]:
    g += Pa(f'M{x-9},{y-6} Q{x},{y-14} {x+9},{y-6} Q{x+8},{y+8} {x},{y+10} Q{x-8},{y+8} {x-9},{y-6} Z', '#d9453a')
g += Ci(54, 128, 8, '#8ac04a') + Ci(146, 128, 8, '#8ac04a') + Ci(100, 136, 6, '#3c4f9a')
A['tart'] = svg(g)

# icing 糖霜：裱花袋在饼干上挤白色糖霜
g = Ci(84, 130, 46, '#d9a050') + Ci(84, 130, 40, '#ffffff') + Ci(84, 130, 40, 'none', 'stroke="#f2ece0" stroke-width="3"') + heart(84, 128, 18, '#ef8fa4') + ''.join(Ci(84 + 30 * math.cos(a), 130 + 30 * math.sin(a), 3, '#5aa1d4') for a in [k * math.pi / 5 for k in range(10)])
g += St('M118,96 q8,4 4,12', '#ffffff', 6)
g += G(Pa('M-24,-50 L24,-50 L6,30 L-6,30 Z', '#e6ecef') + R(-26, -56, 52, 10, '#5aa1d4', 4) + R(-3, 30, 6, 8, '#c4cbd0'), 'translate(140,66) rotate(35)')
A['icing'] = svg(g)

A['candle'] = svg(candle(76, 170, 100, '#ef8fa4') + candle(116, 170, 80, '#5aa1d4') + candle(152, 170, 60, '#f3c234'))

# yeast 酵母：一包酵母，倒出米色小颗粒
g = R(30, 50, 80, 110, '#f3c234', 4) + Pa('M30,50 L110,50 L106,40 L34,40 Z', '#e0a820') + R(42, 80, 56, 50, '#ffffff', 4) + Ci(62, 100, 8, '#e8d4a8') + Ci(76, 108, 6, '#e8d4a8') + Ci(70, 92, 5, '#e8d4a8')
random.seed(55)
g += Pa('M120,176 Q130,150 150,148 Q172,150 182,176 Z', '#e8d4a8') + ''.join(Ci(random.uniform(124, 178), random.uniform(152, 174), 2, '#c9b080') for _ in range(20))
A['yeast'] = svg(g)

# cream-puff 泡芙：撒糖粉的泡芙，中间夹着奶油
def puff_(x, y, s):
    g = E(0, 10, 34, 18, '#d9a050') + E(0, 0, 34, 6, '#ffffff') + E(0, -10, 30, 18, '#e0b060') + hi(-10, -18, 10, 4, .4)
    g += ''.join(Ci(-20 + k * 7, -16 + (k % 3) * 4, 1.5, '#ffffff') for k in range(7))
    return G(g, f'translate({x},{y}) scale({s})')
A['cream-puff'] = svg(plate(100, 160, 84) + puff_(70, 130, 1.1) + puff_(130, 128, 1.1) + puff_(100, 98, 1.1))

# knead 揉面：一双手按在面团上揉
g = board(100, 160, 180, 40, '#d9b07a') + E(100, 140, 66, 24, '#f6ecd4') + E(100, 148, 56, 14, '#ecdcb8')
for sx in (-1, 1):
    g += St(f'M{100+sx*90},60 L{100+sx*40},120', '#5aa1d4', 18) + G(R(-20, -14, 40, 28, SK, 12) + ''.join(R(-16 + k * 9, 8, 8, 14, SK, 4) for k in range(4)), f'translate({100+sx*36},{126}) rotate({sx*-20})')
g += St('M40,100 q-10,10 0,20 M160,100 q10,10 0,20', '#a7adb1', 3)
A['knead'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
