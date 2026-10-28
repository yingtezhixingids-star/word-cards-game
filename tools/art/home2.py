from homekit import *
import os, sys

A = {}
TILE = '#e6f0f4'

def tiles(x0=0, y0=0, w=200, h=200, s=28, col=TILE):
    return R(x0, y0, w, h, col) + ''.join(L(x0, y0 + k * s, x0 + w, y0 + k * s, '#d0dfe6', 1.5) for k in range(1, int(h / s) + 1)) + ''.join(L(x0 + k * s, y0, x0 + k * s, y0 + h, '#d0dfe6', 1.5) for k in range(1, int(w / s) + 1))

def toilet(cx, base, s=1):
    g = R(cx + 6 * s, base - 120 * s, 50 * s, 60 * s, '#ffffff', 6) + R(cx + 6 * s, base - 124 * s, 50 * s, 10 * s, '#f2efe8', 4) + R(cx + 40 * s, base - 112 * s, 10 * s, 5 * s, '#a7adb1', 2)
    g += Pa(f'M{cx-50*s},{base-60*s} L{cx+20*s},{base-60*s} Q{cx+20*s},{base-24*s} {cx-6*s},{base-20*s} L{cx-6*s},{base} L{cx-30*s},{base} L{cx-30*s},{base-22*s} Q{cx-50*s},{base-30*s} {cx-50*s},{base-60*s} Z', '#ffffff')
    g += E(cx - 15 * s, base - 62 * s, 36 * s, 8 * s, '#e6ecef') + E(cx - 15 * s, base - 64 * s, 30 * s, 5 * s, '#dff1fb')
    return g

def tap_(x, y, s=1, water=False):
    g = St(f'M{x},{y} L{x},{y-30*s} Q{x},{y-44*s} {x+18*s},{y-44*s} L{x+30*s},{y-44*s} L{x+30*s},{y-34*s}', '#a7adb1', 8 * s) + R(x - 12 * s, y - 56 * s, 24 * s, 8 * s, '#5d6469', 3) + R(x - 3 * s, y - 64 * s, 6 * s, 10 * s, '#5d6469', 2)
    if water: g += St(f'M{x+30*s},{y-30*s} L{x+30*s},{y+30*s}', '#9fd0ec', 5 * s)
    return g

def towel(x, y, w, h, col):
    return R(x, y, w, h, col, 4) + R(x, y + h - 14, w, 6, '#ffffff', 0, 'opacity=".6"') + R(x, y + h - 26, w, 4, '#ffffff', 0, 'opacity=".4"')

def bulb(cx, cy, r, on=True):
    g = Ci(cx, cy, r, '#fff3a0' if on else '#e6ecef') + Pa(f'M{cx-r*.5},{cy+r*.8} L{cx+r*.5},{cy+r*.8} L{cx+r*.4},{cy+r*1.2} L{cx-r*.4},{cy+r*1.2} Z', '#fff3a0' if on else '#e6ecef')
    g += R(cx - r * .45, cy + r * 1.2, r * .9, r * .5, '#a7adb1', 2) + ''.join(L(cx - r * .45, cy + r * 1.3 + k * 4, cx + r * .45, cy + r * 1.3 + k * 4, '#8a9196', 1.5) for k in range(2))
    g += St(f'M{cx-r*.3},{cy+r*.6} L{cx-r*.2},{cy} L{cx},{cy+r*.3} L{cx+r*.2},{cy} L{cx+r*.3},{cy+r*.6}', '#d9a020', 2)
    if on: g += ''.join(L(cx + r * 1.3 * math.cos(a), cy + r * 1.3 * math.sin(a), cx + r * 1.7 * math.cos(a), cy + r * 1.7 * math.sin(a), '#f3c234', 3) for a in [math.pi + k * math.pi / 5 for k in range(6)])
    return g

def plug_(x, y, s=1, rot=0, cable=True):
    g = R(-18, -16, 36, 40, '#ffffff', 6) + R(-12, -32, 6, 18, '#c4cbd0', 2) + R(6, -32, 6, 18, '#c4cbd0', 2)
    if cable: g += St('M0,24 Q0,60 40,70', '#2f3437', 5)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def socket_(x, y, s=1):
    return G(R(-30, -30, 60, 60, '#ffffff', 8) + R(-30, -30, 60, 60, 'none', 8, 'stroke="#d9dcde" stroke-width="2"') + Ci(0, 0, 20, '#f2efe8') + R(-10, -6, 5, 14, '#5d6469', 1) + R(5, -6, 5, 14, '#5d6469', 1), f'translate({x},{y}) scale({s})')

def battery_(x, y, s=1, level=1.0, col='#5ba644'):
    g = R(-20, -44, 40, 88, '#2f3437', 6) + R(-8, -52, 16, 10, '#a7adb1', 2) + R(-14, 38 - 76 * level, 28, 76 * level, col, 3)
    return G(g, f'translate({x},{y}) scale({s})')

def broom_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 110, WOOD, 3) + Pa('M-24,0 L24,0 L34,50 L-34,50 Z', '#e0b050') + ''.join(L(-30 + k * 6, 10, -34 + k * 7, 50, '#c8963a', 1.5) for k in range(11)) + R(-26, -4, 52, 10, '#d9453a', 3), f'translate({x},{y}) rotate({rot}) scale({s})')

def mop_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 112, '#5aa1d4', 3) + R(-20, 0, 40, 10, '#5d6469', 3) + ''.join(St(f'M{-18+k*5},10 q{(k-3.5)*2},20 {(k-3.5)*4},36', '#f2efe8', 5) for k in range(8)), f'translate({x},{y}) rotate({rot}) scale({s})')

def bucket_(cx, base, w=70, h=60, col='#5aa1d4', water=True):
    g = Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w*.4},{base} L{cx-w*.4},{base} Z', col) + E(cx, base - h, w / 2, 8, shade(col, -.2))
    if water: g += E(cx, base - h + 2, w / 2 - 4, 5, '#9fd0ec')
    g += St(f'M{cx-w/2},{base-h} Q{cx},{base-h-40} {cx+w/2},{base-h}', '#5d6469', 3)
    return g

def washer(x, y, w=120, h=140, door_fill='#9fd0ec'):
    g = R(x, y, w, h, '#f2efe8', 8) + R(x, y, w, 26, '#e6e1d8', 6) + ''.join(Ci(x + w - 18 - k * 14, y + 13, 5, '#a7adb1') for k in range(2)) + R(x + 10, y + 8, 40, 10, '#7fe08a', 2)
    g += Ci(x + w / 2, y + 26 + (h - 26) / 2, w * .34, '#a7adb1') + Ci(x + w / 2, y + 26 + (h - 26) / 2, w * .28, door_fill) + Pa(f'M{x+w*.3},{y+90} Q{x+w*.5},{y+76} {x+w*.7},{y+90}', 'none', 'stroke="#ffffff" stroke-width="3" opacity=".7"')
    return g

def hammer_(x, y, s=1, rot=0):
    return G(R(-5, -10, 10, 100, WOOD, 4) + Pa('M-34,-26 L20,-26 L28,-18 L28,-4 L-34,-4 Q-40,-10 -38,-20 Z', '#5d6469') + Pa('M20,-26 L34,-34 L40,-28 L28,-18 Z', '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')

def screwdriver_(x, y, s=1, rot=0, col='#e2463b'):
    return G(R(-12, 0, 24, 56, col, 10) + ''.join(L(-6 + k * 4, 8, -6 + k * 4, 48, shade(col, -.2), 1.5) for k in range(4)) + R(-3, -60, 6, 62, '#c4cbd0', 2) + Pa('M-3,-60 L3,-60 L1,-68 L-1,-68 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')

def saw_(x, y, s=1, rot=0):
    return G(Pa('M0,0 L130,-16 L130,16 L0,30 Z', '#c4cbd0') + ''.join(Pa(f'M{k*10},{30-k*1.1} l5,6 l5,-7', '#c4cbd0') for k in range(13)) + R(-40, -4, 46, 36, '#c8903a', 10) + R(-30, 4, 26, 16, '#f1e8d4', 6), f'translate({x},{y}) rotate({rot}) scale({s})')

def ladder_(x1, y1, x2, y2, w=40, col='#c8903a', rungs=6):
    g = L(x1, y1, x2, y2, col, 7) + L(x1 + w, y1, x2 + w, y2, col, 7)
    return g + ''.join(L(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, x1 + (x2 - x1) * t + w, y1 + (y2 - y1) * t, col, 5) for t in [(k + .5) / rungs for k in range(rungs)])

def drill_(x, y, s=1):
    return G(R(-50, -20, 80, 36, '#f3c234', 10) + R(30, -10, 16, 16, '#2f3437', 3) + R(46, -4, 40, 4, '#a7adb1') + Pa('M-30,16 L-6,16 L-10,70 L-36,70 Z', '#2f3437') + R(-40, 64, 40, 18, '#2f3437', 4) + R(-6, 20, 10, 14, '#e2463b', 3), f'translate({x},{y}) scale({s})')

def pliers_(x, y, s=1, rot=0):
    return G(Pa('M0,0 L-14,-60 Q-4,-70 6,-60 Z', '#5d6469') + Pa('M0,0 L14,-60 Q4,-70 -6,-60 Z', '#a7adb1') + St('M-4,4 Q-26,50 -30,90', '#e2463b', 14) + St('M4,4 Q26,50 30,90', '#e2463b', 14) + Ci(0, 0, 7, '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')

def wrench_(x, y, s=1, rot=0):
    return G(R(-8, -10, 16, 120, '#a7adb1', 7) + Pa('M-22,-30 Q-28,-10 -8,-4 L8,-4 Q28,-10 22,-30 L12,-30 L12,-14 L-12,-14 L-12,-30 Z', '#a7adb1') + Ci(0, 104, 8, '#f1e8d4'), f'translate({x},{y}) rotate({rot}) scale({s})')

# ================= 浴室 =================
A['toilet'] = svg(tiles(0, 0, 200, 150) + R(0, 150, 200, 50, '#d0dfe6') + toilet(90, 182, 1.2), shadow=False)
A['towel'] = svg(R(30, 40, 140, 8, '#a7adb1', 4) + Ci(30, 44, 6, '#5d6469') + Ci(170, 44, 6, '#5d6469') + towel(44, 40, 60, 110, '#5aa1d4') + towel(96, 40, 60, 90, '#ef8fa4'))
# bath 浴缸：装满泡泡水的浴缸，小黄鸭
g = tiles(0, 0, 200, 120) + Pa('M14,110 L186,110 L178,160 Q170,176 150,176 L50,176 Q30,176 22,160 Z', '#ffffff') + R(10, 104, 180, 10, '#f2efe8', 5) + L(40, 176, 36, 190, '#a7adb1', 5) + L(160, 176, 164, 190, '#a7adb1', 5)
g += ''.join(Ci(40 + k * 16, 100 - (k % 3) * 6, 10 + (k % 2) * 4, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(9)) + tap_(170, 104, .8)
g += E(80, 92, 12, 9, '#f3c234') + Ci(88, 82, 7, '#f3c234') + Pa('M94,82 l6,2 l-6,2 Z', '#f08a24')
A['bath'] = svg(g, shadow=False)
# shower 淋浴：花洒喷出水柱，下面瓷砖墙
g = tiles() + St('M150,200 L150,40 Q150,24 130,24 L100,24 L100,40', '#a7adb1', 7) + Pa('M76,40 L124,40 L114,54 L86,54 Z', '#c4cbd0') + ''.join(L(84 + k * 6, 58, 70 + k * 10, 170, '#9fd0ec', 2.5) for k in range(6)) + R(140, 120, 20, 10, '#5d6469', 3)
A['shower'] = svg(g, shadow=False)
# tap 水龙头：水龙头哗哗流水
A['tap'] = svg(tiles(0, 0, 200, 140) + R(20, 140, 160, 20, '#ffffff', 4) + tap_(80, 140, 2.0, True) + E(140, 168, 30, 6, '#9fd0ec'), shadow=False)
# toilet-paper 卫生纸：一卷挂在架子上的卫生纸
g = R(30, 60, 140, 10, '#a7adb1', 4) + R(30, 56, 10, 20, '#5d6469', 3) + R(160, 56, 10, 20, '#5d6469', 3) + R(50, 50, 100, 60, '#ffffff', 10) + E(150, 80, 12, 30, '#f2efe8') + E(150, 80, 6, 14, '#c8a070')
g += Pa('M50,100 L50,170 L70,180 L90,170 L110,180 L120,174 L120,100 Z', '#ffffff') + ''.join(L(52, 120 + k * 20, 118, 120 + k * 20, '#e6ecef', 1.5, ) for k in range(3))
A['toilet-paper'] = svg(g)
# washbasin 洗脸盆：洗手台上的白色脸盆，镜子，肥皂
g = tiles(0, 0, 200, 120) + E(100, 60, 44, 40, '#dff1fb') + E(100, 60, 44, 40, 'none', 'stroke="#a7adb1" stroke-width="5"') + R(20, 116, 160, 14, '#f2efe8', 4)
g += Pa('M50,128 L150,128 Q148,170 100,174 Q52,170 50,128 Z', '#ffffff') + E(100, 130, 46, 8, '#e6ecef') + tap_(100, 118, .7) + R(140, 106, 20, 10, '#ef8fa4', 5) + R(70, 174, 60, 20, '#a7adb1')
A['washbasin'] = svg(g, shadow=False)
# sponge 海绵：黄绿双层海绵，起泡泡
random.seed(101)
g = R(40, 80, 120, 60, '#f3d034', 10) + R(40, 130, 120, 24, '#5ba644', 6) + ''.join(Ci(random.uniform(50, 150), random.uniform(88, 126), random.uniform(2, 4), '#e0b820') for _ in range(20))
g += ''.join(Ci(60 + k * 22, 74 - (k % 2) * 12, 9, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(5))
A['sponge'] = svg(g)
# flush 冲水：手按下马桶冲水按钮，水打旋
g = tiles(0, 0, 200, 150) + R(0, 150, 200, 50, '#d0dfe6') + toilet(90, 182, 1.2) + Ci(144, 37, 7, '#a7adb1') + hand_(148, 30, .5, 180, '#5aa1d4') + St('M60,106 a12,4 0 1,1 12,4 a20,6 0 1,1 -26,-6', '#5aa1d4', 2.5)
A['flush'] = svg(g, shadow=False)
# bathrobe 浴袍：挂在钩子上的毛巾浴袍，系着腰带
g = Ci(100, 20, 6, '#5d6469') + Pa('M70,30 L130,30 L160,70 L150,180 L50,180 L40,70 Z', '#ffffff') + Pa('M70,30 L100,90 L130,30', 'none', 'stroke="#e6ecef" stroke-width="10"')
g += Pa('M40,70 L20,140 L36,146 L56,90 Z M160,70 L180,140 L164,146 L144,90 Z', '#f2efe8') + R(48, 110, 104, 12, '#5aa1d4', 4) + St('M100,116 L90,150 M100,116 L112,148', '#5aa1d4', 6) + R(56, 130, 26, 22, '#f2efe8', 3)
A['bathrobe'] = svg(g)
# shower-gel 沐浴露：按压瓶沐浴露，旁边泡沫
g = R(70, 70, 60, 110, '#7fc4c0', 14) + R(84, 50, 32, 22, '#ffffff', 4) + R(96, 30, 8, 22, '#ffffff') + R(96, 30, 34, 8, '#ffffff', 3) + R(78, 100, 44, 50, '#ffffff', 4) + leaf(100, 126, 16, 6, -60, '#5ba644') + R(74, 76, 6, 96, '#ffffff', 3, 'opacity=".4"')
g += ''.join(Ci(148 + k * 12, 160 - (k % 2) * 10, 10, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(3))
A['shower-gel'] = svg(g)
# bath-mat 浴室垫：浴缸前的一块软软的地垫
g = tiles(0, 0, 200, 110) + R(0, 110, 200, 90, '#d0dfe6') + Pa('M10,80 L190,80 L184,110 L16,110 Z', '#ffffff') + Pa('M30,140 L170,140 L186,186 L14,186 Z', '#5aa1d4', 'transform="rotate(0)"') + ''.join(L(30 + k * 12, 144, 20 + k * 14, 182, '#7fb7d8', 3) for k in range(12))
A['bath-mat'] = svg(g, shadow=False)
# mouthwash 漱口水：一瓶蓝色漱口水和小量杯
g = Pa('M60,180 L60,70 Q60,54 80,54 L110,54 Q130,54 130,70 L130,180 Z', '#5ab0e0', 'opacity=".95"') + R(76, 30, 38, 26, '#ffffff', 4) + R(66, 100, 58, 44, '#ffffff', 4) + tooth_like if False else Pa('M60,180 L60,70 Q60,54 80,54 L110,54 Q130,54 130,70 L130,180 Z', '#5ab0e0', 'opacity=".95"')
g += R(76, 30, 38, 26, '#ffffff', 4) + R(66, 100, 58, 44, '#ffffff', 4) + Pa('M86,110 Q84,104 90,104 Q95,106 95,106 Q100,104 104,104 Q110,104 108,112 Q106,124 102,134 Q98,126 95,118 Q92,126 88,134 Q84,124 86,110 Z', '#5ab0e0') + R(64, 60, 6, 110, '#ffffff', 3, 'opacity=".35"')
g += Pa('M144,150 L172,150 L168,180 L148,180 Z', '#dff1fb') + Pa('M145,160 L171,160 L168,180 L148,180 Z', '#5ab0e0')
A['mouthwash'] = svg(g)
# non-slip-mat 防滑垫：淋浴间里带小吸盘的防滑垫，鞋底示意不打滑
g = tiles(0, 0, 200, 200) + R(30, 70, 140, 110, '#7fc4c0', 10) + ''.join(Ci(46 + (k % 7) * 18, 86 + (k // 7) * 18, 5, '#5aa8a0') for k in range(35))
g += Pa('M60,40 Q60,20 80,20 L110,20 Q130,20 130,40 L130,56 L60,56 Z', '#5d6469') + Ci(150, 40, 14, '#5ba644') + St('M144,40 l5,5 l9,-10', '#ffffff', 3)
A['non-slip-mat'] = svg(g, shadow=False)
# grab-bar 扶手：浴室墙上的不锈钢扶手，一只手握着
g = tiles() + R(30, 90, 140, 16, '#c4cbd0', 8) + R(26, 80, 16, 36, '#a7adb1', 4) + R(158, 80, 16, 36, '#a7adb1', 4) + hi(80, 94, 30, 3, .6)
g += G(St('M0,80 L0,40', '#ef8fa4', 18) + R(-16, 20, 32, 26, SK, 8) + R(-16, 6, 32, 16, SK, 6), 'translate(110,74)')
A['grab-bar'] = svg(g, shadow=False)
# shaving-foam 剃须泡沫：剃须泡沫罐，一团白泡沫和剃须刀
g = R(40, 70, 60, 110, '#3c7fc1', 8) + Pa('M48,70 Q70,50 92,70 Z', '#c4cbd0') + R(64, 40, 12, 20, '#ffffff', 3) + R(46, 100, 48, 40, '#ffffff', 4) + R(44, 76, 6, 100, '#ffffff', 3, 'opacity=".3"')
g += ''.join(Ci(124 + k * 10, 92 - (k % 2) * 8, 12, '#ffffff', 'stroke="#e6ecef" stroke-width="1.5"') for k in range(4)) + G(R(-4, 0, 8, 70, '#5d6469', 4) + R(-20, -10, 40, 12, '#a7adb1', 3), 'translate(150,120) rotate(15)')
A['shaving-foam'] = svg(g)

# ================= 房屋 =================
# roof 屋顶：房子上红色瓦片屋顶，箭头指着
g = house(100, 180, 130, 60, roof='#c0503a', chimney=True) + ''.join(L(36 + k * 16, 120 - (k if k < 4 else 8 - k) * 13 + 0, 36 + k * 16, 120, '#a8402a', 1.5) for k in range(9)) + arrow(176, 30, 150, 60)
A['roof'] = svg(g)
# wall 墙：砖墙，墙上挂一幅画
g = ''.join(R((k % 2) * -20 + j * 40, 10 + k * 20, 38, 18, '#c0603a' if (k + j) % 3 else '#b0502a', 2) for k in range(9) for j in range(6)) + R(60, 60, 80, 60, '#c8903a', 3) + R(66, 66, 68, 48, '#a9d8f2') + Pa('M66,114 L90,86 L110,106 L134,90 L134,114 Z', '#5ba644')
A['wall'] = svg(g, shadow=False)
# gate 大门：院子的铁栅栏大门
g = R(20, 60, 20, 130, '#a7a09a', 2) + R(160, 60, 20, 130, '#a7a09a', 2) + R(16, 50, 28, 14, '#8a837c') + R(156, 50, 28, 14, '#8a837c')
for sx, x0 in ((1, 42), (-1, 158)):
    g += ''.join(L(x0 + sx * k * 12, 190, x0 + sx * k * 12, 80 - (k * 4 if sx > 0 else k * 4), '#2f3437', 4) for k in range(5)) + L(x0, 100, x0 + sx * 56, 100, '#2f3437', 4) + L(x0, 170, x0 + sx * 56, 170, '#2f3437', 4)
g += St('M42,80 Q70,60 98,70 M158,80 Q130,60 102,70', '#2f3437', 4) + R(94, 120, 12, 20, '#d9a33a', 2)
A['gate'] = svg(g, shadow=False)
# fence 栅栏：白色木栅栏，后面草地
g = R(0, 150, 200, 50, '#8cc06a') + ''.join(Pa(f'M{10+k*24},170 L{10+k*24},70 L{20+k*24},56 L{30+k*24},70 L{30+k*24},170 Z', '#ffffff') + R(26 + k * 24, 70, 4, 100, '#e6ecef') for k in range(8)) + R(0, 90, 200, 10, '#f2efe8') + R(0, 140, 200, 10, '#f2efe8')
A['fence'] = svg(g, shadow=False)
# doorbell 门铃：门边的门铃按钮，手指按下，响铃符号
g = R(0, 0, 200, 200, '#e6dcc8') + door_(20, 30, 70, 170) + R(120, 70, 40, 60, '#ffffff', 8) + Ci(140, 100, 14, '#f3c234') + Ci(140, 100, 9, '#e0a820') + hand_(168, 130, .5, -40, '#5aa1d4')
g += St('M120,52 q10,-12 20,0 M112,40 q18,-20 36,0', '#5d6469', 3) + Pa('M170,40 Q170,28 180,28 Q190,28 190,40 L192,52 L168,52 Z', '#f3c234') + Ci(180, 56, 3, '#f3c234')
A['doorbell'] = svg(g, shadow=False)
# mailbox 信箱：立在柱子上的信箱，里面露出信，红旗竖起
g = R(92, 110, 16, 80, '#8a5a35') + Pa('M40,110 L40,70 Q40,40 80,40 L120,40 Q160,40 160,70 L160,110 Z', '#3c7fc1') + E(40, 76, 6, 36, '#2f5a8a')
g += R(156, 50, 6, 50, '#5d6469') + R(160, 50, 26, 18, '#e2463b', 2) + G(R(0, 0, 50, 34, '#ffffff', 2) + Pa('M0,0 L25,18 L50,0', 'none', 'stroke="#d9dcde" stroke-width="2"'), 'translate(10,60) rotate(-20)')
A['mailbox'] = svg(g)
# front-door 前门：房子正面的大门，门前台阶和地垫
g = R(0, 0, 200, 170, '#e6dcc8') + door_(60, 30, 80, 140, '#c0403a') + R(40, 170, 120, 12, '#a7a09a') + R(30, 182, 140, 12, '#8a837c') + R(70, 164, 60, 8, '#8a5a35', 2) + lamp_(30, 60, 0) + R(20, 60, 18, 24, '#f3d058', 3) + R(162, 60, 18, 24, '#f3d058', 3)
A['front-door'] = svg(g, shadow=False)
# upstairs 楼上：两层楼剖面，箭头指向上面那层
g = R(20, 30, 160, 150, '#f2ead8') + L(20, 105, 180, 105, '#8a5a35', 6) + ladder_(130, 180, 100, 105, 24, '#c8903a', 5) + bed_(70, 104, 80, '#7fb7d8', 1, .9) + sofa(70, 178, 80, '#5aa1d4', .9)
g += Pa('M10,30 L100,0 L190,30 Z', '#c0503a') + R(150, 50, 24, 24, '#f3c234', 4, 'opacity=".0"') + arrow(170, 140, 170, 60, '#5ba644', 6)
A['upstairs'] = svg(g, shadow=False)
# downstairs 楼下：两层楼剖面，箭头指向下面那层
g = R(20, 30, 160, 150, '#f2ead8') + L(20, 105, 180, 105, '#8a5a35', 6) + ladder_(130, 180, 100, 105, 24, '#c8903a', 5) + bed_(70, 104, 80, '#7fb7d8', 1, .9) + sofa(70, 178, 80, '#5aa1d4', .9)
g += Pa('M10,30 L100,0 L190,30 Z', '#c0503a') + arrow(170, 60, 170, 150, '#e2463b', 6)
A['downstairs'] = svg(g, shadow=False)
# hallway 走廊：长长的走廊，两边门，地上一排鞋
g = Pa('M0,0 L70,60 L70,140 L0,200 Z', '#e6dcc8') + Pa('M200,0 L130,60 L130,140 L200,200 Z', '#ddd2bc') + R(70, 60, 60, 80, '#f2ead8') + Pa('M0,200 L70,140 L130,140 L200,200 Z', '#c8a070') + Pa('M0,0 L70,60 L130,60 L200,0 Z', '#f6f1e6')
g += Pa('M18,60 L46,78 L46,150 L18,170 Z', WOOD) + Pa('M182,60 L154,78 L154,150 L182,170 Z', '#5aa1d4') + R(90, 76, 20, 50, '#c8903a', 2)
g += ''.join(E(70 + k * 20, 182, 9, 5, ['#2f3437', '#e2463b', '#5aa1d4', '#8a5a35'][k]) for k in range(4))
A['hallway'] = svg(g, shadow=False)
# ceiling 天花板：仰视房间，天花板上吊灯，箭头指向上方
g = Pa('M0,0 L200,0 L160,60 L40,60 Z', '#f6f1e6') + Pa('M0,0 L40,60 L40,200 L0,200 Z', '#e6dcc8') + Pa('M200,0 L160,60 L160,200 L200,200 Z', '#ddd2bc') + R(40, 60, 120, 140, '#f2ead8')
g += L(100, 24, 100, 70, '#5d6469', 2) + Pa('M80,70 L120,70 L110,88 L90,88 Z', '#f3d58a') + arrow(100, 150, 100, 100, '#e2463b', 5) + Ci(100, 30, 6, '#5d6469')
A['ceiling'] = svg(g, shadow=False)
# guest-room 客房：整洁的小客房，床上叠好毛巾，旁边行李箱
g = room_bg('#e6f0e8') + window_(120, 30, 56, 48, curtain='#7fc4c0') + bed_(70, 172, 110, '#f3c234') + R(70, 112, 30, 10, '#ffffff', 3) + R(70, 104, 30, 10, '#5aa1d4', 3)
g += R(144, 110, 40, 60, '#d9453a', 6) + R(156, 100, 16, 12, 'none', 3, 'stroke="#2f3437" stroke-width="3"') + Ci(150, 172, 4, '#2f3437') + Ci(178, 172, 4, '#2f3437')
A['guest-room'] = svg(g, shadow=False)
# attic 阁楼：尖屋顶下的小阁楼，斜窗，堆着箱子
g = Pa('M100,10 L200,120 L200,200 L0,200 L0,120 Z', '#c8a070') + Pa('M100,30 L184,124 L184,190 L16,190 L16,124 Z', '#e6d4b0') + Pa('M84,60 L116,60 L124,90 L76,90 Z', '#a9d8f2')
g += R(30, 140, 50, 40, '#c8903a', 2) + R(40, 112, 34, 28, '#d9a868', 2) + L(30, 160, 80, 160, '#a8703e', 2) + R(110, 150, 60, 30, '#8a5a35', 2) + Pa('M110,150 L170,150 L164,136 L116,136 Z', '#a8703e') + St('M140,40 L140,60 M140,60 q-8,6 0,10 q8,4 0,10', '#a7adb1', 1.5)
A['attic'] = svg(g, shadow=False)
# basement 地下室：地面以下的房间，楼梯往下，放着工具和杂物
g = R(0, 0, 200, 50, '#a9d8f2') + R(0, 44, 200, 10, '#8cc06a') + R(0, 54, 200, 146, '#8a7a6a') + R(10, 64, 180, 126, '#a8988a') + house(100, 50, 70, 30) if False else R(0, 0, 200, 50, '#a9d8f2')
g += house(150, 48, 50, 26) + R(0, 46, 200, 10, '#8cc06a') + R(0, 56, 200, 144, '#7a6a5a') + R(10, 66, 180, 124, '#a8988a')
g += ladder_(20, 70, 60, 190, 26, '#8a5a35', 6) + R(110, 150, 70, 40, WOOD, 2) + hammer_(126, 140, .4, -30) + R(150, 130, 24, 20, '#5aa1d4', 2) + bulb(140, 80, 8)
A['basement'] = svg(g, shadow=False)
# chimney 烟囱：屋顶上的砖烟囱冒着烟
g = house(100, 190, 140, 60) + R(124, 40, 30, 70, '#b0502a') + ''.join(L(124, 50 + k * 12, 154, 50 + k * 12, '#90401f', 1.5) for k in range(5)) + R(120, 34, 38, 10, '#90401f')
g += ''.join(Ci(140 + k * 8, 26 - k * 8, 8 + k * 2, '#c4cbd0', 'opacity=".8"') for k in range(3))
A['chimney'] = svg(g)
# porch 门廊：房门前有顶棚的门廊，两把摇椅
g = R(0, 0, 200, 200, '#e6dcc8') + door_(80, 60, 50, 110) + Pa('M0,40 L200,40 L200,60 L0,60 Z', '#8a5a35') + R(14, 60, 10, 116, '#ffffff') + R(176, 60, 10, 116, '#ffffff') + R(0, 172, 200, 28, '#c8a070')
g += chair_side(26, 176, '#5aa1d4', .6) + G(chair_side(0, 0, '#5aa1d4', .6), 'translate(172,176) scale(-1,1)') + R(140, 100, 22, 22, '#f3c234', 2, 'opacity=".0"')
A['porch'] = svg(g, shadow=False)

# ================= 水电 =================
A['light'] = svg(L(100, 0, 100, 50, '#5d6469', 3) + Pa('M60,90 L140,90 L120,50 L80,50 Z', '#f3c234') + Ci(100, 96, 14, '#fff3a0') + Pa('M50,96 L150,96 L190,190 L10,190 Z', '#fff6c8', 'opacity=".45"'), shadow=False)
A['switch'] = svg(R(60, 40, 80, 120, '#ffffff', 10) + R(60, 40, 80, 120, 'none', 10, 'stroke="#d9dcde" stroke-width="3"') + R(84, 66, 32, 68, '#f2efe8', 6) + R(86, 68, 28, 30, '#ffffff', 4, 'stroke="#c4cbd0" stroke-width="1"') + hand_(150, 120, .5, -30, '#5aa1d4'))
A['plug'] = svg(plug_(100, 90, 1.6))
A['socket'] = svg(R(0, 0, 200, 200, '#f2ead8') + socket_(100, 100, 1.7), shadow=False)
A['battery'] = svg(battery_(70, 100, 1.1) + battery_(130, 110, .9, .2, '#e2463b') + T(70, 104, '+', 26, '#ffffff', 900))
A['light-bulb'] = svg(bulb(100, 80, 40))
# heater 暖气/取暖器：电暖器发出暖红光和热浪
g = R(40, 60, 120, 110, '#e6ecef', 10) + R(52, 74, 96, 70, '#2f3437', 4) + ''.join(R(58, 80 + k * 14, 84, 6, '#f08a24', 3) for k in range(4)) + R(60, 150, 30, 10, '#a7adb1', 3) + Ci(130, 155, 6, '#e2463b') + R(46, 170, 14, 10, '#5d6469') + R(140, 170, 14, 10, '#5d6469')
g += St('M70,50 q-6,-10 0,-20 q6,-10 0,-20 M100,50 q-6,-10 0,-20 q6,-10 0,-20 M130,50 q-6,-10 0,-20 q6,-10 0,-20', '#f08a24', 3)
A['heater'] = svg(g)
# air-conditioner 空调：墙上的挂式空调吹出冷风和雪花
g = R(0, 0, 200, 200, '#f2ead8') + R(20, 40, 160, 56, '#ffffff', 14) + R(20, 80, 160, 16, '#e6ecef', 6) + R(140, 52, 24, 10, '#7fe0f0', 3) + ''.join(L(30, 86 + k * 4, 170, 86 + k * 4, '#c4cbd0', 1.5) for k in range(2))
g += ''.join(St(f'M{50+k*30},106 q-6,20 4,40 q8,16 -2,30', '#9fd0ec', 3) for k in range(4)) + T(64, 170, '❄', 18, '#5aa1d4') + T(140, 160, '❄', 22, '#5aa1d4')
A['air-conditioner'] = svg(g, shadow=False)
# pipe 管子：一段弯弯的水管和接头
g = St('M10,60 L100,60 Q130,60 130,90 L130,190', '#a7adb1', 22) + St('M10,60 L100,60 Q130,60 130,90 L130,190', '#c4cbd0', 10) + R(60, 46, 16, 28, '#8a9196', 3) + R(116, 120, 28, 16, '#8a9196', 3) + R(150, 140, 30, 10, '#e2463b', 4) + R(160, 128, 10, 14, '#5d6469')
A['pipe'] = svg(g)
# leak 漏水：水槽下的水管接头滴水，地上一摊水
g = R(0, 0, 200, 200, '#f2ead8') + R(0, 0, 200, 50, WOOD) + St('M60,50 L60,100 Q60,120 80,120 L150,120 L150,200', '#a7adb1', 16) + R(140, 112, 22, 24, '#8a9196', 3)
g += drop(156, 148, 7) + drop(164, 166, 5) + E(150, 190, 40, 8, '#9fd0ec') + St('M128,108 l-8,-8 M170,108 l8,-8', '#5aa1d4', 3)
A['leak'] = svg(g, shadow=False)
# wire 电线：几根剥开铜芯的彩色电线，闪电标志
g = ''.join(St(f'M10,{60+k*30} Q100,{40+k*30} 150,{80+k*20}', c, 10) + St(f'M150,{80+k*20} l18,{-4+k*2}', '#d9903a', 4) for k, c in enumerate(['#e2463b', '#3c7fc1', '#2f3437']))
g += Pa('M150,20 L130,60 L146,60 L134,96 L170,48 L152,48 L164,20 Z', '#f3c234')
A['wire'] = svg(g)
# power-cut 停电：漆黑的房间，灯灭了，点着蜡烛
g = R(0, 0, 200, 200, '#2f3445') + window_(120, 30, 56, 48, '#1f2435') + Pa('M150,40 A10,10 0 1,0 160,56 A8,8 0 1,1 150,40 Z', '#f3c234') + L(70, 0, 70, 30, '#5d6469', 2) + Pa('M52,50 L88,50 L80,30 L60,30 Z', '#5d6469') + bulb(70, 70, 0, False) if False else R(0, 0, 200, 200, '#2f3445')
g += window_(120, 30, 56, 48, '#1f2435') + Pa('M140,40 A10,10 0 1,0 152,56 A8,8 0 1,1 140,40 Z', '#f3c234') + L(70, 0, 70, 30, '#5d6469', 2) + Pa('M52,50 L88,50 L80,30 L60,30 Z', '#5d6469') + L(56, 64, 84, 64, '#e2463b', 3) + L(56, 64, 84, 64, '#e2463b', 0)
g += R(90, 150, 20, 40, '#f6efe0', 2) + Pa('M100,124 Q110,138 100,148 Q90,138 100,124 Z', '#f3c234') + Ci(100, 140, 40, '#f3c234', 'opacity=".12"') + R(80, 186, 40, 6, '#a7adb1', 2)
A['power-cut'] = svg(g, shadow=False)
# extension-cord 插线板：多孔插线板，插着插头，带开关
g = G(R(-80, -22, 160, 44, '#ffffff', 10) + R(-80, -22, 160, 44, 'none', 10, 'stroke="#d9dcde" stroke-width="2"') + ''.join(R(-60 + k * 30, -8, 6, 14, '#5d6469', 1) + R(-50 + k * 30, -8, 6, 14, '#5d6469', 1) for k in range(4)) + R(62, -10, 12, 20, '#e2463b', 3), 'translate(96,120) rotate(-8)')
g += St('M20,130 Q0,160 30,190', '#ffffff', 6) + plug_(60, 70, .7, 0, False) + St('M60,46 Q60,20 30,14', '#2f3437', 5)
A['extension-cord'] = svg(g)
# water-heater 热水器：挂墙的电热水器，红色温度表，出热水
g = R(0, 0, 200, 200, '#e6f0f4') + R(50, 20, 100, 130, '#ffffff', 40) + R(50, 20, 100, 130, 'none', 40, 'stroke="#d9dcde" stroke-width="2"') + Ci(100, 70, 18, '#e6ecef') + Pa('M100,70 L110,58', 'none', 'stroke="#e2463b" stroke-width="3"') + Ci(100, 70, 3, '#2f3437')
g += R(80, 110, 40, 12, '#7fe08a', 3) + L(80, 150, 80, 180, '#a7adb1', 6) + L(120, 150, 120, 170, '#a7adb1', 6) + St('M120,170 q10,10 30,10', '#e2463b', 6) + steam(150, 176, 2, 12, '#c4cbd0', .6)
A['water-heater'] = svg(g, shadow=False)
# fuse 保险丝：电闸箱里的一排开关，其中一个跳闸了
g = R(30, 30, 140, 140, '#c4cbd0', 6) + R(40, 50, 120, 100, '#e6ecef', 4)
for k in range(5):
    x = 52 + k * 22
    g += R(x, 70, 16, 60, '#ffffff', 2) + R(x + 3, 80 if k != 2 else 104, 10, 16, '#2f3437' if k != 2 else '#e2463b', 2)
g += Pa('M130,10 L118,34 L128,34 L120,52 L144,26 L132,26 L140,10 Z', '#f3c234')
A['fuse'] = svg(g)
# radiator 暖气片：白色一排排的暖气片，散发热气
g = R(0, 0, 200, 200, '#f2ead8') + ''.join(R(30 + k * 18, 70, 14, 100, '#ffffff', 6) + R(30 + k * 18, 70, 14, 100, 'none', 6, 'stroke="#d9dcde" stroke-width="1.5"') for k in range(8)) + R(26, 84, 152, 8, '#f2efe8') + R(26, 150, 152, 8, '#f2efe8') + Ci(30, 166, 6, '#e2463b')
g += St('M60,60 q-6,-10 0,-20 q6,-10 0,-20 M100,60 q-6,-10 0,-20 q6,-10 0,-20 M140,60 q-6,-10 0,-20 q6,-10 0,-20', '#f08a24', 3)
A['radiator'] = svg(g, shadow=False)

# ================= 家务 =================
# clean 打扫：戴手套拿抹布擦桌子，闪闪发亮
g = table_(100, 120, 160, 60) + hand_(90, 104, .7, 70, '#f3c234') + R(100, 104, 40, 16, '#5aa1d4', 4) + star(150, 100, 7, '#ffffff') + star(40, 106, 6, '#ffffff') + star(160, 80, 5, '#f3c234') + St('M120,96 q10,-6 20,0', '#9fd0ec', 3)
A['clean'] = svg(g)
# sweep 扫地：扫帚扫起一小堆灰尘到簸箕
g = broom_(90, 130, 1.0, 20) + Pa('M120,150 L180,150 L186,180 L114,180 Z', '#e2463b') + R(150, 120, 6, 32, '#e2463b', 2) + ''.join(Ci(100 + k * 6, 172 - (k % 2) * 3, 3, '#8a7a6a') for k in range(5))
A['sweep'] = svg(g)
A['mop'] = svg(mop_(100, 140, 1.1, 15) + bucket_(160, 180, 50, 44) + St('M40,180 q30,-6 60,0', '#9fd0ec', 4) + star(56, 170, 5, '#ffffff'))
# dust 擦灰：鸡毛掸子掸书架上的灰
g = R(20, 70, 160, 10, WOOD, 2) + R(20, 140, 160, 10, WOOD, 2) + ''.join(R(30 + k * 12, 40 + (k % 3) * 4, 10, 30 - (k % 3) * 4, ['#d9453a', '#3c7fc1', '#5ba644'][k % 3]) for k in range(6)) + R(120, 112, 30, 28, '#5aa1d4', 3)
g += G(R(-3, 0, 6, 70, WOOD, 3) + ''.join(E(0, -10 - k * 4, 16 - k, 8, ['#d9453a', '#f3c234', '#5ba644', '#3c7fc1'][k % 4]) for k in range(6)), 'translate(130,100) rotate(-40)') + ''.join(Ci(80 + k * 8, 66 - k * 6, 3, '#c4b8a0', 'opacity=".8"') for k in range(5))
A['dust'] = svg(g)
# tidy-up 收拾：把散落的玩具和书放回箱子里，前后对比
g = R(0, 0, 98, 200, '#f6e8e0') + R(102, 0, 98, 200, '#e8f4e8') + R(0, 150, 98, 50, '#d9b07a') + R(102, 150, 98, 50, '#d9b07a')
g += G(R(-14, -10, 28, 20, '#3c7fc1', 2), 'translate(30,160) rotate(30)') + G(R(-10, -14, 20, 28, '#e2463b', 2), 'translate(66,150) rotate(-40)') + Ci(50, 176, 8, '#f3c234') + G(R(-14, -4, 28, 8, '#5ba644', 2), 'translate(70,184) rotate(10)')
g += R(118, 120, 66, 46, '#c8903a', 3) + R(122, 108, 18, 14, '#3c7fc1') + R(144, 104, 14, 18, '#e2463b') + Ci(168, 112, 8, '#f3c234') + arrow(86, 60, 120, 60, '#5ba644', 5) + star(170, 40, 7)
A['tidy-up'] = svg(g, shadow=False)
# wash-the-dishes 洗碗：水槽里满是泡沫，手拿海绵洗盘子
g = R(10, 110, 180, 70, WOOD) + R(10, 104, 180, 10, '#e6ecef') + R(40, 110, 120, 46, '#a7adb1', 8) + ''.join(Ci(56 + k * 12, 108 - (k % 3) * 5, 8, '#ffffff', 'stroke="#d9e8f0" stroke-width="1"') for k in range(9))
g += E(90, 80, 30, 30, '#ffffff', 'stroke="#d9dcde" stroke-width="2"') + R(104, 66, 26, 18, '#f3d034', 4) + hand_(124, 100, .6, 0, '#ef8fa4') + tap_(160, 104, .6)
A['wash-the-dishes'] = svg(g, shadow=False)
# take-out-the-trash 倒垃圾：提着系好的垃圾袋走向垃圾桶
g = R(120, 90, 60, 90, '#5ba644', 6) + R(114, 80, 72, 14, '#3c8a3a', 4) + T(150, 140, '♻', 30, '#ffffff', 700)
g += pose((60, 50), (60, 72), (60, 116), arms=[[(70, 76), (82, 100), (90, 120)]], legs=[[(56, 116), (46, 176)], [(64, 116), (76, 176)]], back_arm=[[(50, 76), (44, 104)]], shirt='#5aa1d4', pants='#3b4a5a', style='grey', hr=13, tw=24, lw=11, aw=9)
g += Pa('M80,124 Q74,150 90,166 Q108,170 112,150 Q110,126 96,122 Z', '#2f3437') + Pa('M90,124 l-4,-8 l8,0 l-4,8', '#2f3437')
A['take-out-the-trash'] = svg(g)
# do-the-laundry 洗衣服：往洗衣机里放脏衣服，洗衣篮
g = washer(70, 40) + R(10, 130, 50, 50, '#c8a070', 6) + ''.join(L(14 + k * 8, 134, 14 + k * 8, 176, '#a8803a', 2) for k in range(6)) + Pa('M14,130 Q26,110 40,120 Q50,108 58,130 Z', '#5aa1d4') + Pa('M24,124 Q36,112 46,126 Z', '#ef8fa4')
A['do-the-laundry'] = svg(g)
# iron 熨衣服：熨斗在熨衬衫，冒蒸汽
g = Pa('M10,150 L190,150 L180,170 L20,170 Z', '#5aa1d4') + Pa('M30,150 L60,110 L140,110 L170,150 Z', '#ffffff') + Pa('M60,110 L100,130 L140,110', 'none', 'stroke="#e6ecef" stroke-width="3"')
g += G(Pa('M-50,20 L40,20 Q60,20 60,0 Q50,-26 -10,-26 Q-46,-20 -50,20 Z', '#e2463b') + St('M-20,-26 Q-10,-50 30,-40 L40,-20', '#2f3437', 8) + R(-50, 16, 110, 8, '#c4cbd0', 3), 'translate(110,110)') + steam(60, 116, 3, 14, '#c4cbd0', .7)
A['iron'] = svg(g)
# vacuum 吸尘：吸尘器吸地毯
g = Pa('M10,170 L130,170 L150,190 L0,190 Z', '#c0503a') + R(20, 120, 70, 50, '#5ba644', 20) + wheel(34, 170, 8) + wheel(78, 170, 8) + R(30, 130, 40, 14, '#ffffff', 4, 'opacity=".4"')
g += St('M80,130 Q120,110 140,60 L160,40', '#2f3437', 6) + St('M160,40 L160,170', '#a7adb1', 6) + R(140, 168, 50, 14, '#2f3437', 4) + ''.join(Ci(150 + k * 10, 186, 2, '#c4b8a0') for k in range(3))
A['vacuum'] = svg(g)
A['broom'] = svg(broom_(100, 120, 1.3, 10))
A['bucket'] = svg(bucket_(100, 170, 110, 100))
A['washing-machine'] = svg(washer(40, 30, 120, 150))
# detergent 洗衣液：一大瓶带把手的蓝色洗衣液，泡泡
g = Pa('M40,180 L40,70 Q40,50 60,50 L130,50 Q150,50 150,70 L150,180 Z', '#3c7fc1') + R(60, 30, 34, 22, '#f3c234', 4) + St('M110,50 Q150,40 140,90', '#3c7fc1', 14) + R(56, 90, 76, 60, '#ffffff', 6) + Ci(94, 120, 18, '#5aa1d4') + Ci(86, 112, 6, '#ffffff') + Ci(102, 126, 4, '#ffffff')
g += ''.join(Ci(160 + k * 10, 140 - k * 16, 8 - k, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(3))
A['detergent'] = svg(g)
# hang-out-the-washing 晾衣服：阳光下晾衣绳上挂着衣服
g = Ci(170, 30, 16, '#f3c234') + L(10, 60, 190, 70, '#5d6469', 2) + L(14, 60, 14, 190, '#8a5a35', 5) + L(186, 70, 186, 190, '#8a5a35', 5)
g += Pa('M30,62 L70,64 L80,80 L70,86 L68,130 L32,128 L32,84 L20,78 Z', '#e2463b') + Pa('M90,66 L130,68 L128,140 L116,140 L110,96 L104,140 L92,140 Z', '#3c7fc1') + R(140, 68, 30, 50, '#f3c234', 3)
g += ''.join(R(x, 58 + (x - 10) / 18, 5, 10, '#5ba644', 1) for x in (36, 64, 94, 124, 144, 164)) + R(0, 186, 200, 14, '#8cc06a')
A['hang-out-the-washing'] = svg(g, shadow=False)
# rubber-gloves 橡胶手套：一双黄色橡胶手套
def glove(x, y, rot, col='#f3c234'):
    g = R(-22, 0, 44, 50, col, 8) + R(-24, 40, 48, 30, shade(col, -.1), 6) + ''.join(R(-22 + k * 11, -36 + abs(k - 1.5) * 6, 10, 40, col, 5) for k in range(4)) + G(R(-6, -14, 12, 34, col, 6), 'translate(-24,14) rotate(-40)')
    return G(g, f'translate({x},{y}) rotate({rot})')
A['rubber-gloves'] = svg(glove(70, 100, -15) + glove(130, 106, 15, '#f0b020'))

# ================= 房屋修缮 =================
# fix 修理：扳手拧紧滴水的水龙头
A['fix'] = svg(tiles(0, 0, 200, 140) + R(20, 140, 160, 20, '#ffffff', 4) + tap_(70, 140, 1.6) + wrench_(140, 60, .8, 50) + drop(118, 160, 5))
# repair 维修：螺丝刀在修一把坏椅子
A['repair'] = svg(chair_side(40, 180, WOOD, 1.2) + R(80, 150, 6, 30, WOOD) + screwdriver_(140, 120, 1.1, -40) + G(R(-6, -6, 12, 12, '#5d6469', 2), 'translate(96,118)') + St('M90,104 l-6,-8 M104,104 l6,-8', '#d9453a', 3))
# new 新的：亮闪闪、带价签的新椅子
A['new'] = svg(sofa(100, 170, 130, '#e2463b', 1.4) + G(Pa('M0,0 L40,0 L50,16 L40,32 L0,32 Z', '#f3c234') + Ci(42, 16, 3, '#ffffff'), 'translate(130,40)') + St('M130,56 L110,100', '#5d6469', 2) + star(40, 50, 9, '#f3c234') + star(70, 30, 6, '#f3c234') + star(170, 110, 6, '#f3c234'))
# shelf 架子：墙上的一块木搁板，放着花盆和书
A['shelf'] = svg(R(0, 0, 200, 200, '#f2ead8') + R(20, 110, 160, 12, WOOD, 3) + Pa('M40,122 L40,150 L60,122 Z', '#5d6469') + Pa('M160,122 L160,150 L140,122 Z', '#5d6469') + R(40, 70, 12, 40, '#3c7fc1') + R(54, 76, 10, 34, '#e2463b') + R(66, 72, 12, 38, '#5ba644') + R(120, 88, 30, 22, '#c0603a', 3) + leaf(135, 88, 22, 8, -120, '#5ba644') + leaf(135, 88, 22, 8, -60, '#5ba644'), shadow=False)
# cabinet 柜子：两门木柜，一扇门松了歪着
A['cabinet'] = svg(R(30, 50, 140, 130, WOODL, 4) + R(36, 56, 62, 118, shade(WOODL, -.06), 2) + G(R(0, 0, 62, 118, shade(WOODL, -.06), 2) + R(6, 50, 4, 18, '#5d6469', 2), 'translate(102,56) rotate(6)') + R(88, 106, 4, 18, '#5d6469', 2) + St('M170,60 l10,-6 M172,74 l10,0', '#d9453a', 3))
# install 安装：工人用电钻把新窗户装到墙上
A['install'] = svg(R(0, 0, 200, 200, '#e6dcc8') + window_(30, 40, 90, 90) + drill_(150, 90, .8) + St('M124,88 L118,88', '#a7adb1', 3) + ladder_(130, 190, 140, 120, 30, '#c8903a', 4), shadow=False)
# measure 测量：卷尺量窗户的宽度
A['measure'] = svg(R(0, 0, 200, 200, '#e6dcc8') + window_(40, 70, 120, 90) + R(30, 40, 140, 12, '#f3c234', 2) + ''.join(L(34 + k * 8, 40, 34 + k * 8, 44 + (k % 2) * 4, '#2f3437', 1.5) for k in range(17)) + R(14, 32, 30, 28, '#e2463b', 8) + arrow(40, 30, 160, 30, '#2f3437', 2) + arrow(160, 30, 40, 30, '#2f3437', 2), shadow=False)
# tile 瓷砖：一摞方形瓷砖，其中一块有裂纹
g = ''.join(Pa(f'M{30+k*4},{140-k*10} L{100+k*4},{110-k*10} L{170+k*4},{140-k*10} L{100+k*4},{170-k*10} Z', '#ffffff' if k % 2 else '#dff1fb', 'stroke="#c4cbd0" stroke-width="1.5"') for k in range(4))
g += St('M110,80 L120,96 L112,108 L126,124', '#5d6469', 2.5)
A['tile'] = svg(g)
# plumber 水管工：戴帽子的水管工，手拿管钳，身旁水管
cx, cy, r = 80, 80, 28
g = person_bust(cx, cy, r, '#3c7fc1', '#3a2a20', 'short', 'dot', 'smile') + Pa(f'M{cx-r*1.2},{cy+r*1.3} L{cx+r*1.2},{cy+r*1.3} L{cx+r*1.2},200 L{cx-r*1.2},200 Z', '#2f5a8a') + R(cx - r * .9, cy + r * 1.3, 10, 50, '#2f5a8a')
g += Pa(f'M{cx-r},{cy-r*.4} Q{cx-r},{cy-r*1.3} {cx},{cy-r*1.3} Q{cx+r},{cy-r*1.3} {cx+r},{cy-r*.4} Z', '#e2463b') + R(cx - r * 1.2, cy - r * .5, r * 2.0, 8, '#c0302a', 3)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.6), (cx + r * 2.3, cy + r * .8)], '#3c7fc1', SK, 14) + wrench_(cx + r * 2.4, cy + r * .4, .55, 20) + St('M170,200 L170,140 Q170,120 190,120', '#a7adb1', 12)
A['plumber'] = svg(g)
# electrician 电工：戴安全帽的电工，手拿电线和电笔，闪电标志
cx, cy, r = 80, 84, 28
g = person_bust(cx, cy, r, '#f08a24', '#3a2a20', 'short', 'dot', 'smile') + Pa(f'M{cx-r*1.05},{cy-r*.3} Q{cx-r*1.05},{cy-r*1.4} {cx},{cy-r*1.4} Q{cx+r*1.05},{cy-r*1.4} {cx+r*1.05},{cy-r*.3} Z', '#f3c234') + R(cx - r * 1.3, cy - r * .4, r * 2.6, 8, '#e0a820', 3)
g += R(cx - r * 1.6, cy + r * 1.5, r * 3.2, 8, '#ffffff', 0, 'opacity=".7"') + arm([(cx + r * 1.6, 200), (cx + r * 2.2, cy + r * 1.6), (cx + r * 2.3, cy + r * .8)], '#f08a24', SK, 14) + screwdriver_(cx + r * 2.4, cy + r * .4, .6, 20, '#f3c234')
g += Pa('M160,20 L146,48 L158,48 L148,76 L176,40 L164,40 L174,20 Z', '#f3c234')
A['electrician'] = svg(g)
# carpenter 木匠：木匠拿锯子锯木板，耳朵夹着铅笔
cx, cy, r = 70, 70, 26
g = person_bust(cx, cy, r, '#8a5a35', P['grey'], 'grey', 'dot', 'smile') + Pa(f'M{cx-r*1.1},{cy+r*1.4} L{cx+r*1.1},{cy+r*1.4} L{cx+r*1.2},200 L{cx-r*1.2},200 Z', '#c8a070') + R(cx - r * 1.4, cy - r * .3, 20, 4, '#f3c234', 2, f'transform="rotate(-30 {cx-r} {cy})"')
g += R(80, 150, 120, 20, '#d9a868', 2) + R(80, 170, 120, 30, '#8a5a35') + saw_(118, 124, .6, 30) + arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 1.6), (cx + r * 2.0, cy + r * 1.8)], '#8a5a35', SK, 13)
A['carpenter'] = svg(g)
# builder 建筑工人：戴黄色安全帽、穿反光背心，后面砖墙
cx, cy, r = 100, 84, 30
g = ''.join(R((k % 2) * -20 + j * 40, 120 + k * 20, 38, 18, '#c0603a', 2) for k in range(4) for j in range(6))
g += person_bust(cx, cy, r, '#f08a24', '#3a2a20', 'short', 'dot', 'smile') + R(cx - r * 1.7, cy + r * 1.6, r * 3.4, 8, '#f3f3a0') + R(cx - r * 1.7, cy + r * 2.2, r * 3.4, 8, '#f3f3a0')
g += Pa(f'M{cx-r*1.05},{cy-r*.3} Q{cx-r*1.05},{cy-r*1.4} {cx},{cy-r*1.4} Q{cx+r*1.05},{cy-r*1.4} {cx+r*1.05},{cy-r*.3} Z', '#f3c234') + R(cx - r * 1.3, cy - r * .4, r * 2.6, 8, '#e0a820', 3)
A['builder'] = svg(g, shadow=False)
# quote 报价：师傅递来一张报价单，上面列着价格和总价 ¥
g = Pa('M40,20 L160,20 L160,180 L40,180 Z', '#ffffff') + R(40, 20, 120, 26, '#3c7fc1') + ''.join(L(52, 64 + k * 20, 110, 64 + k * 20, '#a7adb1', 3) + T(140, 68 + k * 20, '¥', 12, '#5d6469', 700) for k in range(4)) + L(52, 146, 150, 146, '#2f3437', 2)
g += T(100, 168, '¥ 3,800', 18, '#e2463b', 900) + hand_(168, 150, .6, -60, '#3c7fc1')
A['quote'] = svg(g)
# renovate 翻新：厨房一半旧一半新，箭头从旧到新
g = R(0, 0, 100, 200, '#c8b8a0') + R(100, 0, 100, 200, '#f6f1e6') + R(0, 110, 100, 90, '#8a7a6a') + R(100, 110, 100, 90, '#ffffff')
g += R(10, 60, 80, 40, '#a8988a') + St('M20,70 l20,10 M50,64 l10,20', '#6a5a4a', 2) + R(110, 60, 80, 40, '#7fc4c0', 4) + R(110, 120, 80, 60, '#7fc4c0', 4) + R(146, 120, 4, 60, '#ffffff') + star(170, 40, 8)
g += R(10, 120, 80, 60, '#a8988a') + St('M20,130 l30,30', '#6a5a4a', 2) + arrow(70, 30, 130, 30, '#5ba644', 5)
A['renovate'] = svg(g, shadow=False)
# floorboard 地板条：一条条木地板，其中一条翘起来
g = ''.join(R(0, 60 + k * 26, 200, 24, [WOODL, WOOD, '#d0985a'][k % 3]) + L((k * 70) % 200, 60 + k * 26, (k * 70) % 200, 84 + k * 26, WOODD, 2) for k in range(5))
g += G(R(0, 0, 110, 24, WOOD) + R(0, 0, 110, 4, shade(WOOD, .2)), 'translate(60,112) rotate(-8)') + St('M170,90 q6,-8 12,0 M176,80 q8,-10 16,0', '#5d6469', 2)
A['floorboard'] = svg(g, shadow=False)
# insulation 隔热层：墙体剖面里塞满粉黄色的保温棉
g = R(20, 30, 40, 160, '#c0603a') + R(140, 30, 40, 160, '#e6dcc8')
random.seed(102)
g += R(60, 30, 80, 160, '#f6c8a0') + ''.join(St(f'M60,{40+k*20} q20,-10 40,0 t40,0', '#f0b080', 3) for k in range(8)) + ''.join(L(20, 40 + k * 20, 60, 40 + k * 20, '#a8402a', 2) for k in range(8))
g += Pa('M150,90 l14,0 l0,-8 l14,14 l-14,14 l0,-8 l-14,0 Z', '#e2463b') + T(170, 140, '❄', 18, '#5aa1d4') + St('M10,100 q-6,-8 0,-16', '#f08a24', 3)
A['insulation'] = svg(g, shadow=False)

# ================= 工具 =================
A['hammer'] = svg(hammer_(100, 80, 1.3, 30))
# nail 钉子：几根铁钉，一根钉进木板
g = R(20, 130, 160, 40, WOOD, 3) + R(96, 90, 8, 44, '#a7adb1', 1) + R(84, 86, 32, 6, '#8a9196', 2) + ''.join(G(R(-3, -30, 6, 50, '#a7adb1', 1) + R(-10, -34, 20, 6, '#8a9196', 2) + Pa('M-3,20 L3,20 L0,28 Z', '#a7adb1'), f'translate({140+k*14},{70+k*6}) rotate({60+k*10})') for k in range(3))
A['nail-tools'] = svg(g)
# screw 螺丝：大大的十字螺丝，螺纹清楚
A['screw'] = svg(G(Ci(0, -60, 26, '#c4cbd0') + R(-16, -63, 32, 6, '#5d6469', 2) + R(-3, -76, 6, 32, '#5d6469', 2) + Pa('M-12,-38 L12,-38 L10,50 L0,70 L-10,50 Z', '#a7adb1') + ''.join(L(-12 + k * .4, -26 + k * 12, 12 - k * .4, -32 + k * 12, '#8a9196', 3) for k in range(7)), 'translate(100,100) rotate(20)'))
A['screwdriver'] = svg(screwdriver_(100, 110, 1.3, 30))
A['saw'] = svg(saw_(64, 96, .95, 10))
A['ladder'] = svg(ladder_(60, 186, 80, 14, 60, '#c8903a', 7))
A['drill'] = svg(drill_(100, 90, 1.3))
# glue 胶水：一管胶水挤出一滴，粘住两块木片
g = G(R(-20, -50, 40, 100, '#ffffff', 8) + R(-20, -10, 40, 40, '#f3c234', 2) + R(-8, -66, 16, 18, '#e2463b', 3) + Pa('M-6,-66 L6,-66 L2,-82 L-2,-82 Z', '#ffffff'), 'translate(70,100) rotate(-20)')
g += drop(54, 30, 7, '#f6f1e4') + R(110, 120, 70, 20, WOOD, 2) + R(110, 140, 70, 20, WOODL, 2) + St('M110,140 L180,140', '#f6f1e4', 3)
A['glue'] = svg(g)
A['pliers'] = svg(pliers_(100, 70, 1.2, 15))
A['wrench'] = svg(wrench_(100, 40, 1.1, 30))
# flashlight 手电筒：打开的手电筒射出一道光
g = G(R(-60, -14, 80, 28, '#2f3437', 8) + Pa('M20,-14 L44,-26 L44,26 L20,14 Z', '#5d6469') + E(44, 0, 6, 26, '#fff3a0') + R(-40, -18, 14, 6, '#e2463b', 2), 'translate(70,120) rotate(-20)')
g += Pa('M112,92 L196,30 L196,140 L118,118 Z', '#fff6c8', 'opacity=".7"')
A['flashlight'] = svg(g)
# toolbox 工具箱：红色工具箱，打开露出工具
g = R(30, 100, 140, 76, '#e2463b', 6) + Pa('M30,100 L170,100 L160,80 L40,80 Z', '#c0302a') + St('M70,80 Q100,50 130,80', '#2f3437', 6) + R(90, 120, 20, 10, '#c4cbd0', 2)
g += hammer_(70, 70, .4, -20) + screwdriver_(120, 66, .4, 20, '#3c7fc1') + wrench_(146, 50, .3, 10)
A['toolbox'] = svg(g)
# tape-measure 卷尺：黄色卷尺，尺子拉出来带刻度
g = R(30, 90, 70, 70, '#f3c234', 18) + Ci(65, 125, 16, '#e0a820') + R(30, 150, 70, 10, '#2f3437', 3) + R(96, 140, 90, 14, '#f8e070', 2) + ''.join(L(100 + k * 8, 140, 100 + k * 8, 144 + (k % 2) * 5, '#2f3437', 1.5) for k in range(11)) + R(182, 136, 6, 22, '#a7adb1', 1)
A['tape-measure'] = svg(g)
# rope 绳子：一卷盘起来的麻绳
g = ''.join(E(100, 140 - k * 10, 70 - k * 2, 22, 'none', f'stroke="{["#c8a070","#b8905a"][k%2]}" stroke-width="10"') for k in range(6)) + St('M160,90 Q190,60 170,30', '#c8a070', 10)
A['rope'] = svg(g)
# bolt 螺栓：六角螺栓和螺母
g = G(Pa('M-26,-14 L-14,-26 L14,-26 L26,-14 L26,6 L-26,6 Z', '#8a9196') + R(-10, 6, 20, 90, '#a7adb1') + ''.join(L(-10, 20 + k * 10, 10, 16 + k * 10, '#8a9196', 2.5) for k in range(7)), 'translate(80,60) rotate(-20)')
g += G(Pa(' '.join(('M' if k == 0 else 'L') + f'{24*math.cos(k*math.pi/3):.1f},{24*math.sin(k*math.pi/3):.1f}' for k in range(6)) + ' Z', '#a7adb1') + Ci(0, 0, 10, '#f1e8d4'), 'translate(150,140)')
A['bolt'] = svg(g)
# sandpaper 砂纸：一张粗糙的砂纸，打磨木块，木屑
random.seed(103)
g = R(30, 40, 110, 90, '#d9b070', 3) + ''.join(Ci(random.uniform(34, 136), random.uniform(44, 126), 1.2, '#a8803a') for _ in range(80)) + R(30, 40, 110, 10, '#ffffff', 2, 'opacity=".4"')
g += R(90, 130, 90, 40, WOOD, 3) + R(100, 120, 50, 20, '#d9b070', 3) + ''.join(Ci(80 + k * 10, 178, 2, '#e0b070') for k in range(6))
A['sandpaper'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
