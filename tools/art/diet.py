from flat import *
from fig import *
import os, sys

A = {}

def apple(cx, cy, s, col='#d93a33'):
    g = Pa(f'M{cx},{cy-18*s} C{cx+12*s},{cy-24*s} {cx+24*s},{cy-14*s} {cx+22*s},{cy+2*s} C{cx+20*s},{cy+18*s} {cx+10*s},{cy+24*s} {cx},{cy+20*s} C{cx-10*s},{cy+24*s} {cx-20*s},{cy+18*s} {cx-22*s},{cy+2*s} C{cx-24*s},{cy-14*s} {cx-12*s},{cy-24*s} {cx},{cy-18*s} Z', col)
    g += hi(cx - 10 * s, cy - 6 * s, 4 * s, 7 * s, .45, 20) + St(f'M{cx},{cy-16*s} l{2*s},{-9*s}', '#6b4423', 2.5 * s) + leaf(cx + 2 * s, cy - 22 * s, 13 * s, 5 * s, -20, '#5ba644')
    return g

def broccoli(cx, cy, s):
    g = Pa(f'M{cx-6*s},{cy+30*s} L{cx-4*s},{cy} L{cx+4*s},{cy} L{cx+6*s},{cy+30*s} Z', '#8cc06a')
    for dx, dy, rr in [(-14, -4, 12), (0, -12, 14), (14, -4, 12), (-6, 2, 10), (8, 2, 10)]:
        g += Ci(cx + dx * s, cy + dy * s, rr * s, '#3c8a3a')
    g += Ci(cx - 4 * s, cy - 16 * s, 5 * s, '#5aaa4a') + Ci(cx + 10 * s, cy - 8 * s, 4 * s, '#5aaa4a')
    return g

def carrot(cx, cy, s, rot=0):
    g = Pa(f'M-8,-30 Q0,-34 8,-30 Q6,10 0,34 Q-6,10 -8,-30 Z', '#f08a24') + Pa('M2,-32 Q8,-30 8,-28 Q6,10 0,34 Q4,6 2,-32 Z', '#d9741a')
    g += ''.join(L(-6, -16 + i * 12, 0, -14 + i * 12, '#d9741a', 1.5) for i in range(3))
    g += leaf(0, -32, 18, 4, -110, '#5ba644') + leaf(0, -32, 18, 4, -70, '#5ba644') + leaf(0, -32, 14, 4, -90, '#3c8a3a')
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def egg(cx, cy, s, cut=False):
    if not cut:
        return E(cx, cy, 16 * s, 21 * s, '#f6ead4') + E(cx + 5 * s, cy + 3 * s, 9 * s, 15 * s, '#e6d4b4', 'opacity=".6"') + hi(cx - 6 * s, cy - 8 * s, 3 * s, 6 * s, .7)
    return E(cx, cy, 18 * s, 22 * s, '#ffffff') + Ci(cx, cy + 2 * s, 10 * s, '#f3b82a')

def drumstick(cx, cy, s, rot=0):
    g = Pa('M-30,-14 Q-40,-32 -18,-34 Q4,-34 16,-14 Q24,0 12,10 Q-6,18 -20,6 Q-28,0 -30,-14 Z', '#c97a3a') + Pa('M-6,-30 Q8,-24 16,-14 Q24,0 12,10 Q8,-4 -6,-30 Z', '#a85f28')
    g += R(10, 4, 26, 8, '#f6efe0', 4, 'transform="rotate(35 10 4)"') + Ci(34, 24, 6, '#f6efe0') + Ci(28, 28, 6, '#f6efe0') + hi(-16, -20, 6, 3, .4, -20)
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def plate(cx, cy, r, col='#ffffff'):
    return E(cx, cy + 4, r, r * .5, '#d9dcde') + E(cx, cy, r, r * .5, col) + E(cx, cy, r * .72, r * .36, '#f4f6f7')

def glass(x, y, w, h, fill='#bfe0ef', level=.75):
    g = Pa(f'M{x},{y} L{x+w},{y} L{x+w-6},{y+h} L{x+6},{y+h} Z', '#e8f4fa', 'opacity=".9"')
    g += Pa(f'M{x+w*.02+ (1-level)*0},{y+h*(1-level)} L{x+w-(1-level)*0-1},{y+h*(1-level)} L{x+w-6},{y+h} L{x+6},{y+h} Z', fill)
    g += R(x + 6, y + 8, 6, h - 16, '#ffffff', 3, 'opacity=".55"')
    return g

def bottle_shape(x, y, w, h, col, neck=.35):
    nw = w * neck
    return Pa(f'M{x+w/2-nw/2},{y} L{x+w/2+nw/2},{y} L{x+w/2+nw/2},{y+h*.2} Q{x+w},{y+h*.3} {x+w},{y+h*.42} L{x+w},{y+h} L{x},{y+h} L{x},{y+h*.42} Q{x},{y+h*.3} {x+w/2-nw/2},{y+h*.2} Z', col)

# healthy 健康的：绿色爱心里装满苹果、西兰花和胡萝卜
g = heart(100, 100, 82, '#cfe8c2') + heart(100, 100, 82, 'none').replace('fill="none"', 'fill="none" stroke="#5ba644" stroke-width="6"')
g += apple(76, 92, 1.2) + broccoli(122, 92, 1.0) + carrot(100, 128, .8, 70)
g += St('M150,40 l8,8 l16,-18', '#5ba644', 6)
A['healthy'] = svg(g)

# water 水：一杯清水和一瓶矿泉水
g = bottle_shape(108, 30, 50, 150, '#cfe8f6') + R(122, 18, 22, 14, '#3c7fc1', 3) + R(108, 98, 50, 34, '#3c7fc1') + R(108, 104, 50, 6, '#ffffff', 0, 'opacity=".4"')
g += R(114, 70, 6, 100, '#ffffff', 3, 'opacity=".6"') + drop(133, 115, 9, '#ffffff')
g += glass(36, 80, 58, 98)
A['water'] = svg(g)

# salt 盐：玻璃盐瓶，银色带孔盖子，倒出白色盐粒
g = G(R(-28, -40, 56, 84, '#eef6fa', 10, 'opacity=".95"') + R(-28, -10, 56, 54, '#ffffff', 8) + R(-30, -58, 60, 22, '#c4cbd0', 8) + R(-30, -44, 60, 6, '#a7adb1', 2) +
      ''.join(Ci(-14 + i * 9, -50, 2, '#5d6469') for i in range(4)) + R(-20, -32, 6, 60, '#ffffff', 3, 'opacity=".8"'), 'translate(86,118) rotate(-25)')
import random; random.seed(5)
g += ''.join(R(130 + random.uniform(-14, 30), 120 + random.uniform(0, 56), 3.5, 3.5, '#ffffff', .5, 'stroke="#d9dcde" stroke-width=".8"') for _ in range(26))
A['salt'] = svg(g)

# sugar 糖：糖罐、勺子和几块方糖
g = E(80, 170, 54, 12, '#d9dcde') + Pa('M30,110 Q30,174 80,174 Q130,174 130,110 Z', '#f4f1ea') + E(80, 110, 50, 12, '#ffffff') + E(80, 110, 44, 9, '#f6f3ee')
g += R(68, 108, 14, 10, '#ffffff', 2, 'stroke="#e6e1d8"') + R(84, 104, 14, 10, '#ffffff', 2, 'stroke="#e6e1d8"')
g += St('M110,112 L150,60', '#c4cbd0', 5) + E(154, 56, 9, 6, '#c4cbd0', 'transform="rotate(-50 154 56)"')
for x, y in [(140, 150), (160, 160), (150, 132)]:
    g += R(x, y, 18, 18, '#ffffff', 2) + Pa(f'M{x},{y} L{x+5},{y-5} L{x+23},{y-5} L{x+18},{y} Z', '#f4f1ea') + Pa(f'M{x+18},{y} L{x+23},{y-5} L{x+23},{y+13} L{x+18},{y+18} Z', '#e2ddd3')
A['sugar'] = svg(g)

# oil 油：一瓶金黄的食用油，旁边一滴油
g = bottle_shape(64, 22, 64, 158, '#f0c43a', .3) + R(86, 10, 20, 14, '#2f6b3a', 3) + R(70, 96, 52, 46, '#ffffff', 4) + leaf(82, 120, 28, 9, -20, '#5ba644') + Ci(108, 116, 6, '#7a8a3a')
g += R(70, 60, 8, 110, '#f8de86', 4, 'opacity=".8"') + drop(156, 140, 20, '#f0c43a') + hi(150, 136, 3, 6, .7)
A['oil'] = svg(g)

# fat 脂肪：两片肥瘦相间的培根，旁边油滴
def bacon(y, rot):
    w = 'M0,{a} Q20,{b} 40,{a} T80,{a} T120,{a} T160,{a}'
    g = ''
    for off, th, c in [(0, 10, '#fbeee0'), (10, 9, '#c9524a'), (19, 7, '#fbeee0'), (26, 10, '#b8463e'), (36, 6, '#fbeee0')]:
        g += St(w.format(a=off + th / 2, b=off + th / 2 - 12), c, th + .8, 'stroke-linecap="butt"')
    return G(g, f'translate(18,{y}) rotate({rot} 80 20)')
g = bacon(66, -6) + bacon(118, 4)
g += drop(160, 36, 11, '#f0c43a') + drop(178, 24, 6, '#f0c43a')
A['fat'] = svg(g)

# vitamin 维生素：半个橙子和几粒维生素 C 片
g = Ci(78, 112, 52, '#f08a24') + Ci(78, 112, 46, '#fbd18a') + Ci(78, 112, 42, '#f5a43a')
g += ''.join(Pa(f'M78,112 L{78+40*math.cos(a)},{112+40*math.sin(a)} L{78+40*math.cos(a+0.6)},{112+40*math.sin(a+0.6)} Z', '#f8b85a', 'stroke="#fbd18a" stroke-width="3"') for a in [i * math.pi / 5 for i in range(10)])
g += Ci(78, 112, 5, '#fbe6c0')
for x, y in [(150, 70), (160, 130), (134, 160)]:
    g += Ci(x, y, 17, '#f3c234') + Ci(x, y, 17, 'none', 'stroke="#d9a33a" stroke-width="2"') + T(x, y + 7, 'C', 20, '#c0741a', 900)
A['vitamin'] = svg(g)

# protein 蛋白质：鸡蛋、剖开的鸡蛋和鸡腿
g = egg(56, 116, 1.6) + egg(102, 132, 1.2, True) + drumstick(146, 90, 1.25, 20)
A['protein'] = svg(g)

# calcium 钙：一杯牛奶、牛奶盒和一根骨头
g = R(108, 46, 56, 128, '#ffffff', 3) + Pa('M108,46 L136,22 L164,46 Z', '#e6ecef') + R(124, 14, 24, 10, '#3c7fc1', 2)
g += R(108, 92, 56, 40, '#3c7fc1') + E(136, 112, 16, 12, '#ffffff') + Pa('M150,46 L164,46 L164,174 L150,174 Z', '#e9eef1')
g += glass(32, 86, 56, 90, '#ffffff', .82)
g += G(R(-30, -6, 60, 12, '#f6f1e4', 4) + Ci(-30, -8, 8, '#f6f1e4') + Ci(-30, 8, 8, '#f6f1e4') + Ci(30, -8, 8, '#f6f1e4') + Ci(30, 8, 8, '#f6f1e4'), 'translate(64,48) rotate(-20) scale(.75)')
A['calcium'] = svg(g)

# fiber 纤维：全麦面包片、燕麦和麦穗
g = Pa('M30,170 L30,96 Q22,60 64,58 Q106,60 98,96 L98,170 Z', '#b5793a') + Pa('M38,164 L38,98 Q32,68 64,66 Q96,68 90,98 L90,164 Z', '#d9a865')
random.seed(7)
g += ''.join(E(42 + random.uniform(0, 44), 80 + random.uniform(0, 80), 2.2, 1.3, '#9a6430') for _ in range(24))
def ear(x, y, s, rot):
    e = St('M0,60 L0,-30', '#c9a24a', 3) + ''.join(E(-6, -20 + i * 11, 5, 9, '#e0b85a', 'transform="rotate(-25 -6 %d)"' % (-20 + i * 11)) + E(6, -20 + i * 11, 5, 9, '#d6aa48', 'transform="rotate(25 6 %d)"' % (-20 + i * 11)) for i in range(5))
    return G(e + E(0, -34, 4, 8, '#e0b85a'), f'translate({x},{y}) rotate({rot}) scale({s})')
g += ear(140, 100, 1.1, 10) + ear(166, 106, 1.0, 22)
g += E(132, 172, 34, 10, '#c58b54') + ''.join(E(110 + random.uniform(0, 44), 164 + random.uniform(-2, 4), 4, 2.5, '#f2e2c0') for _ in range(14))
A['fiber'] = svg(g)

# diet 饮食：餐盘里配好的一份健康餐，旁边软尺
g = plate(96, 112, 76)
g += Ci(72, 108, 18, '#ffffff') + ''.join(Ci(66 + i * 5, 104 + (i % 2) * 6, 4, '#f6f3ee') for i in range(3))
g += broccoli(110, 102, .55) + broccoli(126, 112, .45) + carrot(92, 122, .42, 80)
g += E(126, 92, 14, 8, '#e0915a') + E(124, 90, 10, 5, '#f0a46a')
g += G(R(0, 0, 44, 56, '#ffffff', 3) + R(0, 0, 44, 56, 'none', 3, 'stroke="#c4cbd0" stroke-width="2"') + R(14, -5, 16, 9, '#a7adb1', 3) +
       ''.join(St(f'M7,{14+i*12} l3,3 l6,-6', '#5ba644', 2.5) + L(20, 14 + i * 12, 38, 14 + i * 12, '#a7adb1', 2) for i in range(3)), 'translate(148,128) rotate(8)')
g += St('M28,58 L28,170', '#c4cbd0', 5) + ''.join(L(22 + i * 6, 58, 22 + i * 6, 80, '#c4cbd0', 2.5) for i in range(3))
A['diet'] = svg(g)

# calorie 卡路里：汉堡上方一团火，标着 kcal
g = R(52, 128, 96, 18, '#c97a3a', 8) + R(46, 116, 108, 14, '#5d3a24', 6) + R(48, 110, 104, 8, '#f3c234', 3) + R(46, 104, 108, 8, '#5ba644', 4)
g += Pa('M50,104 Q50,62 100,62 Q150,62 150,104 Z', '#e0a050') + ''.join(E(70 + i * 14, 80 + (i % 2) * 8, 3, 2, '#f6e6c0') for i in range(5))
g += Pa('M100,10 Q126,32 120,50 Q132,44 130,30 Q148,52 134,70 Q122,84 100,84 Q74,84 68,64 Q62,46 80,34 Q80,48 90,50 Q84,30 100,10 Z', '#f08a24', 'opacity=".0"')
g += Pa('M150,20 Q168,36 164,48 Q172,44 172,34 Q184,50 174,62 Q166,72 152,72 Q134,72 130,58 Q126,46 138,38 Q138,48 144,50 Q140,34 150,20 Z', '#f08a24')
g += Pa('M152,40 Q162,50 160,58 Q166,56 166,50 Q172,60 164,66 Q156,72 148,68 Q140,62 146,52 Q148,58 152,58 Q148,48 152,40 Z', '#f3c234')
g += R(30, 154, 140, 30, '#2f3437', 8) + T(100, 176, '550 kcal', 20, '#ffffff', 800)
A['calorie'] = svg(g)

# low-fat 低脂的：贴绿色标签的牛奶瓶，1% 和向下箭头
g = bottle_shape(56, 22, 70, 160, '#ffffff', .4) + R(76, 12, 30, 14, '#5ba644', 3)
g += R(56, 96, 70, 56, '#5ba644') + T(91, 134, '1%', 26, '#ffffff', 900) + R(60, 60, 8, 112, '#eef1f2', 4)
g += Pa('M150,60 L170,60 L170,120 L184,120 L160,150 L136,120 L150,120 Z', '#5ba644')
A['low-fat'] = svg(g)

# vegetarian 素食者：一盘蔬菜，旁边被划掉的鸡腿
g = plate(84, 124, 70)
g += broccoli(70, 112, .7) + carrot(102, 120, .55, 60) + Ci(58, 130, 9, '#d93a33') + Ci(118, 108, 8, '#d93a33') + leaf(90, 104, 24, 9, -10, '#7fc45a') + leaf(110, 132, 22, 8, 160, '#7fc45a')
g += drumstick(156, 52, .8, 0) + Ci(156, 52, 30, 'none', 'stroke="#d9453a" stroke-width="6"') + L(136, 72, 176, 32, '#d9453a', 6)
A['vegetarian'] = svg(g)

# balanced 均衡的：分格餐盘——蔬菜、主食、肉蛋、水果各占一格
cx, cy = 100, 104
g = Ci(cx, cy + 4, 78, '#d9dcde') + Ci(cx, cy, 78, '#ffffff')
cols = ['#8cc06a', '#f2d9a0', '#e79a7a', '#f2b0b8']
for i, c in enumerate(cols):
    a0, a1 = i * math.pi / 2 - math.pi / 2, (i + 1) * math.pi / 2 - math.pi / 2
    g += Pa(f'M{cx},{cy} L{cx+66*math.cos(a0)},{cy+66*math.sin(a0)} A66,66 0 0,1 {cx+66*math.cos(a1)},{cy+66*math.sin(a1)} Z', c)
g += L(cx, cy - 68, cx, cy + 68, '#ffffff', 5) + L(cx - 68, cy, cx + 68, cy, '#ffffff', 5)
g += broccoli(128, 70, .6) + carrot(144, 86, .38, 50)
g += ''.join(E(132 + (i % 3) * 9, 124 + (i // 3) * 8, 5, 3.5, '#ffffff') for i in range(9))
g += drumstick(70, 132, .55, -30) + egg(58, 116, .5, True)
g += apple(72, 72, .8) + Ci(56, 84, 7, '#7a4fa0') + Ci(62, 92, 7, '#7a4fa0')
A['balanced'] = svg(g, shadow=False)

# nutrition 营养：膳食金字塔
g = ''
tiers = [(150, 186, '#e0b85a'), (118, 150, '#8cc06a'), (86, 118, '#e79a7a'), (58, 86, '#9fd0ec'), (34, 58, '#f3c234')]
for i, (y0, y1, c) in enumerate(tiers):
    w0 = (y1 - 22) * .58; w1 = (y0 - 22) * .58
    g += Pa(f'M{100-w0},{y1} L{100+w0},{y1} L{100+w1},{y0+2} L{100-w1},{y0+2} Z', c)
g += Pa('M100,22 L112,34 L88,34 Z', '#f3c234')
g += ''.join(E(66 + i * 13.6, 170, 5, 3.5, '#f6e6c0') for i in range(6))
g += broccoli(76, 136, .38) + carrot(104, 136, .3, 70) + apple(128, 136, .5)
g += egg(84, 104, .45) + drumstick(116, 102, .4, 0)
g += glass(90, 64, 20, 18, '#ffffff', .8)
g += Ci(100, 47, 4, '#ffffff')
A['nutrition'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
