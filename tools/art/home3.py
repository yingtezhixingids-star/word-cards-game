from homekit import *
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

A = {}
GRASS = '#8cc06a'; SOIL = '#7a5236'; SOILL = '#9a6a46'

def paint_can(cx, base, w, h, col, open_=True):
    g = R(cx - w / 2, base - h, w, h, '#c4cbd0', 4) + R(cx - w / 2, base - h * .7, w, h * .45, '#ffffff', 2) + R(cx - w / 2 + 8, base - h * .62, w - 16, h * .3, col, 2)
    if open_: g += E(cx, base - h, w / 2, 8, '#a7adb1') + E(cx, base - h, w / 2 - 4, 6, col) + Pa(f'M{cx-w/2+6},{base-h} q4,20 8,0 q4,14 8,0', col)
    g += St(f'M{cx-w/2},{base-h+6} Q{cx},{base-h-36} {cx+w/2},{base-h+6}', '#5d6469', 3)
    return g

def paint_brush(x, y, s=1, rot=0, col='#3c7fc1'):
    return G(R(-5, 0, 10, 70, WOOD, 5) + R(-12, -16, 24, 20, '#c4cbd0', 2) + Pa('M-12,-16 L12,-16 L14,-50 Q0,-56 -14,-50 Z', '#e0c090') + Pa('M-14,-50 Q0,-56 14,-50 L13,-40 L-13,-40 Z', col), f'translate({x},{y}) rotate({rot}) scale({s})')

def roller_(x, y, s=1, rot=0, col='#5aa1d4'):
    return G(R(-40, -16, 80, 32, col, 14) + R(-40, -16, 80, 10, shade(col, .25), 8) + St('M40,0 L56,0 L56,40 L6,40 L6,60', '#a7adb1', 4) + R(0, 60, 12, 50, '#e2463b', 5), f'translate({x},{y}) rotate({rot}) scale({s})')

def potted(cx, base, w=40, h=34, col='#c0603a'):
    return Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w*.38},{base} L{cx-w*.38},{base} Z', col) + R(cx - w / 2 - 3, base - h - 6, w + 6, 10, shade(col, -.1), 2)

def soil_ground(y=150, h=50):
    return R(0, y, 200, h, SOIL) + ''.join(Ci(10 + k * 23, y + 10 + (k % 3) * 12, 3, SOILL) for k in range(9))

def tulip_(x, y, s=1, col='#e2463b'):
    return St(f'M{x},{y} L{x},{y+60*s}', '#4a9a3a', 4 * s) + leaf(x, y + 50 * s, 30 * s, 8 * s, -70, '#5aaa3a') + Pa(f'M{x-14*s},{y-20*s} L{x-14*s},{y} Q{x},{y+10*s} {x+14*s},{y} L{x+14*s},{y-20*s} L{x+7*s},{y-10*s} L{x},{y-22*s} L{x-7*s},{y-10*s} Z', col)

def rose_(x, y, s=1, col='#d9283a'):
    g = St(f'M{x},{y} L{x},{y+70*s}', '#3c7a2c', 4 * s) + leaf(x, y + 30 * s, 22 * s, 9 * s, -20, '#4a8a3a') + leaf(x, y + 46 * s, 22 * s, 9 * s, -160, '#4a8a3a')
    g += Ci(x, y - 6 * s, 20 * s, col) + Pa(f'M{x-12*s},{y-10*s} Q{x},{y-26*s} {x+12*s},{y-10*s} Q{x},{y-2*s} {x-12*s},{y-10*s} Z', shade(col, -.2)) + St(f'M{x-6*s},{y-8*s} q6,-8 12,0', shade(col, .2), 2)
    g += Pa(f'M{x-18*s},{y} Q{x},{y+16*s} {x+18*s},{y} Q{x},{y+6*s} {x-18*s},{y} Z', shade(col, -.1))
    return g

def daisy(x, y, r, petal='#ffffff', center='#f3c234', n=10):
    return ''.join(E(x + r * .6 * math.cos(a), y + r * .6 * math.sin(a), r * .45, r * .18, petal, f'transform="rotate({math.degrees(a):.0f} {x+r*.6*math.cos(a):.1f} {y+r*.6*math.sin(a):.1f})"') for a in [k * 2 * math.pi / n for k in range(n)]) + Ci(x, y, r * .3, center)

def watering_can_(x, y, s=1, rot=0, col='#5ba644'):
    return G(Pa('M-30,-30 L30,-30 L34,30 L-34,30 Z', col) + St('M-26,-30 Q0,-60 26,-30', shade(col, -.2), 6) + Pa('M30,10 L70,-30 L76,-24 L36,20 Z', col) + E(76, -28, 10, 6, shade(col, -.2), 'transform="rotate(45 76 -28)"'), f'translate({x},{y}) rotate({rot}) scale({s})')

def spade_(x, y, s=1, rot=0):
    return G(R(-4, -100, 8, 100, WOOD, 3) + Pa('M-14,-112 L14,-112 L14,-100 L-14,-100 Z', '#2f3437') + St('M-14,-110 L14,-110', '#2f3437', 4) + Pa('M-22,0 L22,0 L20,50 Q0,62 -20,50 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')

def rake_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 120, WOOD, 3) + R(-36, 8, 72, 8, '#5d6469', 2) + ''.join(R(-34 + k * 8, 14, 4, 18, '#5d6469', 1) for k in range(9)), f'translate({x},{y}) rotate({rot}) scale({s})')

def hoe_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 120, WOOD, 3) + Pa('M-2,6 L36,6 L40,30 L4,30 Z', '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')

def trowel_(x, y, s=1, rot=0):
    return G(R(-6, 0, 12, 44, '#5ba644', 5) + R(-2, -10, 4, 12, '#a7adb1') + Pa('M-16,-10 L16,-10 Q14,-50 0,-60 Q-14,-50 -16,-10 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')

def shears_(x, y, s=1, rot=0, short=False):
    bl = 40 if short else 80
    return G(Pa(f'M0,0 L-8,{-bl} L4,{-bl+6} L6,0 Z', '#c4cbd0') + Pa(f'M0,0 L8,{-bl} L-4,{-bl+6} L-6,0 Z', '#a7adb1') + Ci(0, 0, 5, '#5d6469') + St('M-3,4 Q-20,30 -26,70', '#e2463b', 10) + St('M3,4 Q20,30 26,70', '#e2463b', 10), f'translate({x},{y}) rotate({rot}) scale({s})')

def mower(x, y, s=1):
    return G(R(-50, -30, 90, 40, '#e2463b', 10) + R(-40, -44, 50, 20, '#2f3437', 6) + wheel(-40, 12, 12) + wheel(30, 12, 12) + St('M30,-24 L80,-90 L100,-90', '#2f3437', 5) + R(-36, -36, 14, 6, '#ffffff', 2), f'translate({x},{y}) scale({s})')

def gglove(x, y, rot, col='#5ba644'):
    g = R(-22, 0, 44, 50, col, 8) + R(-24, 40, 48, 24, '#f3c234', 6) + ''.join(R(-22 + k * 11, -36 + abs(k - 1.5) * 6, 10, 40, col, 5) for k in range(4)) + G(R(-6, -14, 12, 34, col, 6), 'translate(-24,14) rotate(-40)') + ''.join(Ci(-12 + k * 8, 20, 2, shade(col, -.25)) for k in range(4))
    return G(g, f'translate({x},{y}) rotate({rot})')

def bench_(cx, base, w=120, col=WOOD):
    return ''.join(R(cx - w / 2, base - 44 + k * 10, w, 7, col, 2) for k in range(2)) + ''.join(R(cx - w / 2, base - 84 + k * 12, w, 8, col, 2) for k in range(3)) + R(cx - w / 2 + 8, base - 84, 6, 84, '#2f3437') + R(cx + w / 2 - 14, base - 84, 6, 84, '#2f3437')

def tree_(x, y, s=1):
    return tree(x, y, s)

# ================= 装饰 =================
A['paint'] = svg(paint_can(90, 176, 90, 90, '#e2463b') + paint_brush(150, 110, .9, 20, '#e2463b') + drop(140, 170, 6, '#e2463b'))
A['brush'] = svg(paint_brush(100, 110, 1.4, 25))
# color 颜色：调色板上一格格不同颜色的色卡
g = ''.join(R(30 + (k % 4) * 36, 40 + (k // 4) * 44, 30, 38, c, 4) for k, c in enumerate(['#e2463b', '#f08a24', '#f3c234', '#5ba644', '#3c7fc1', '#7a4fa0', '#ef8fa4', '#8a5a35', '#2f3437', '#ffffff', '#9fd0ec', '#a8d878']))
A['color'] = svg(g)
# bright 明亮的：阳光照进来的明亮房间
g = room_bg('#fbf3d8', '#e8c890') + window_(60, 30, 80, 70, '#bfe6fa') + Ci(100, 20, 0, '#000') + Pa('M60,100 L140,100 L180,170 L20,170 Z', '#fff6c8', 'opacity=".7"') + Ci(170, 30, 14, '#f3c234') + ''.join(L(170 + 18 * math.cos(a), 30 + 18 * math.sin(a), 170 + 26 * math.cos(a), 30 + 26 * math.sin(a), '#f3c234', 3) for a in [k * math.pi / 4 for k in range(8)])
A['bright'] = svg(g, shadow=False)
# dark 深色的/暗的：一排由浅到深的色卡，箭头指着最深的那块
g = ''.join(R(20 + k * 32, 60, 28, 90, shade('#3c7fc1', .7 - k * .3), 3) for k in range(5)) + arrow(164, 30, 164, 56, '#e2463b', 4) + St('M150,156 L178,156', '#e2463b', 4)
A['dark'] = svg(g)
A['light-blue'] = svg(paint_can(80, 176, 90, 90, '#9fd0ec') + R(140, 60, 40, 100, '#9fd0ec', 4) + R(140, 60, 40, 100, 'none', 4, 'stroke="#ffffff" stroke-width="3"') + paint_brush(150, 40, .6, -30, '#9fd0ec'))
# decorate 装饰：门上挂红灯笼，贴着窗花和福字式红纸
def lantern(x, y, s=1):
    return G(L(0, -40, 0, -26, '#d9a33a', 2) + R(-14, -28, 28, 6, '#d9a33a', 2) + E(0, 0, 26, 24, '#e2302a') + ''.join(St(f'M{k*9},-22 Q{k*14},0 {k*9},22', '#c0201a', 1.5) for k in (-2, -1, 0, 1, 2)) + R(-14, 22, 28, 6, '#d9a33a', 2) + ''.join(L(-8 + j * 4, 28, -8 + j * 4, 44, '#d9a33a', 1.5) for j in range(5)), f'translate({x},{y}) scale({s})')
g = R(0, 0, 200, 200, '#f2e2c8') + door_(60, 60, 80, 140, '#8a3a2a') + lantern(40, 60, 1.0) + lantern(160, 60, 1.0) + Pa('M100,70 L118,88 L100,106 L82,88 Z', '#e2302a') + R(42, 104, 14, 70, '#e2302a', 1) + R(144, 104, 14, 70, '#e2302a', 1) + R(60, 40, 80, 14, '#e2302a', 1)
A['decorate'] = svg(g, shadow=False)
# hook 挂钩：墙上的挂钩挂着一件外套
g = R(0, 0, 200, 200, '#f2ead8') + R(84, 30, 32, 14, WOOD, 3) + St('M100,44 L100,60 Q100,74 112,70', '#5d6469', 5)
g += Pa('M100,64 L70,80 L56,180 L144,180 L130,80 Z', '#5a7a9a') + Pa('M100,64 L92,110 L100,180 L108,110 Z', '#4a6a8a') + ''.join(Ci(100, 120 + k * 18, 3, '#2f3437') for k in range(3))
A['hook'] = svg(g, shadow=False)
# photo-frame 相框：桌上立着的相框，里面是全家福
g = R(40, 30, 120, 120, '#c8903a', 6) + R(50, 40, 100, 100, '#a9d8f2') + R(50, 110, 100, 30, GRASS)
for k, (x, c, hr) in enumerate([(70, '#e2463b', P['grey']), (100, '#3c7fc1', '#3a2a20'), (130, '#5ba644', P['grey'])]):
    g += Ci(x, 84, 9, SK) + Pa(f'M{x-9},82 Q{x},72 {x+9},82 Z', hr) + R(x - 10, 94, 20, 30, c, 6)
g += Pa('M100,150 L120,180 L130,178 Z', '#a8703e')
A['photo-frame'] = svg(g)
# pattern 图案：一块印满花朵图案的布料
g = Pa('M30,40 L170,40 L170,160 Q150,176 130,160 Q110,176 90,160 Q70,176 50,160 Q30,176 30,160 Z', '#f6e2c8') + ''.join(flower(48 + (k % 4) * 36, 62 + (k // 4) * 34, .9, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644'][(k + k // 4) % 4], '#ffffff') for k in range(12)) + ''.join(leaf(60 + (k % 4) * 36, 74 + (k // 4) * 34, 10, 4, 30, '#5aaa3a') for k in range(12))
A['pattern'] = svg(g)
# stripe 条纹：蓝白条纹的衬衫
g = Pa('M70,40 L130,40 L170,64 L160,96 L144,90 L144,180 L56,180 L56,90 L40,96 L30,64 Z', '#ffffff') + f'<clipPath id="sc"><path d="M70,40 L130,40 L170,64 L160,96 L144,90 L144,180 L56,180 L56,90 L40,96 L30,64 Z"/></clipPath>' + '<g clip-path="url(#sc)">' + ''.join(R(20 + k * 16, 30, 8, 160, '#3c7fc1') for k in range(10)) + '</g>'
g += Pa('M80,40 L100,60 L120,40 Z', '#ffffff') + ''.join(Ci(100, 80 + k * 22, 3, '#2f3437') for k in range(4))
A['stripe'] = svg(g)
A['roller'] = svg(R(0, 0, 200, 200, '#f2ead8') + R(0, 0, 100, 200, '#9fd0ec') + roller_(100, 70, 1.0) + Pa('M88,48 L112,48 L112,200 L88,200 Z', '#9fd0ec', 'opacity=".5"'), shadow=False)
# wallpaper 壁纸：一卷花纹壁纸，墙上已经贴了一半
g = R(0, 0, 200, 200, '#f2ead8') + R(0, 0, 110, 200, '#e8d8f0') + ''.join(flower(14 + (k % 4) * 30, 20 + (k // 4) * 36, .7, '#9a7ab8', '#ffffff') for k in range(24))
g += R(120, 140, 70, 40, '#e8d8f0', 4) + E(190, 160, 8, 20, '#d6c4e2') + E(120, 160, 8, 20, '#c4b0d4') + ''.join(flower(134 + k * 16, 156, .5, '#9a7ab8', '#ffffff') for k in range(3))
A['wallpaper'] = svg(g, shadow=False)
# masking-tape 美纹纸胶带：一卷米色纸胶带，贴在窗框边上
g = R(0, 0, 200, 200, '#f2ead8') + window_(30, 30, 90, 90) + R(22, 22, 106, 6, '#f0e2b0') + R(22, 22, 6, 106, '#f0e2b0')
g += Ci(150, 150, 34, '#f0e2b0') + Ci(150, 150, 20, '#f2ead8') + Ci(150, 150, 20, 'none', 'stroke="#c4b48a" stroke-width="3"') + R(128, 120, 24, 8, '#f0e2b0', 0, 'transform="rotate(-30 140 124)"')
A['masking-tape'] = svg(g, shadow=False)
# dust-sheet 防尘布：沙发上盖着一大块白色防尘布，旁边油漆桶
g = Pa('M20,170 L24,100 Q40,80 70,90 Q100,70 130,90 Q160,80 176,100 L180,170 Z', '#f6f6f2') + ''.join(St(f'M{40+k*30},96 Q{36+k*30},130 {44+k*30},168', '#e6e6e0', 3) for k in range(5))
g += paint_can(170, 186, 30, 30, '#5aa1d4', False)
A['dust-sheet'] = svg(g)
# matching 相配的：窗帘和靠垫是同样的花纹，中间等号
pat = lambda x, y: flower(x, y, .6, '#ef8fa4', '#ffffff')
g = Pa('M20,30 L80,30 Q70,110 76,170 L20,170 Z', '#5aa1d4') + ''.join(pat(32 + (k % 2) * 24, 50 + (k // 2) * 26) for k in range(10))
g += Pa('M120,90 Q150,80 180,90 Q186,120 180,150 Q150,160 120,150 Q114,120 120,90 Z', '#5aa1d4') + ''.join(pat(134 + (k % 2) * 26, 104 + (k // 2) * 24) for k in range(4)) + R(88, 96, 24, 6, '#5ba644', 2) + R(88, 110, 24, 6, '#5ba644', 2)
A['matching'] = svg(g)

# ================= 花草 =================
A['flower'] = svg(St('M100,100 L100,180', '#4a9a3a', 5) + leaf(100, 150, 36, 12, -40, '#5aaa3a') + leaf(100, 160, 36, 12, -140, '#5aaa3a') + daisy(100, 80, 54, '#ef8fa4', '#f3c234', 10))
A['rose'] = svg(rose_(100, 70, 1.6))
# plant 植物：花盆里的一株绿叶盆栽
g = potted(100, 180, 70, 56) + ''.join(leaf(100, 124, 60 - abs(a) * .3, 18, a, ['#3c8a3a', '#4a9a3a', '#5aaa3a'][k % 3]) for k, a in enumerate((-160, -130, -100, -80, -50, -20)))
A['plant'] = svg(g)
A['leaf'] = svg(leaf(40, 150, 150, 56, -40, '#5aaa3a') + St('M70,124 L96,110 M90,108 L118,92 M110,90 L136,72 M70,124 L80,98 M90,108 L100,84 M110,90 L118,66', '#3c8a3a', 2))
A['grass'] = svg(R(0, 150, 200, 50, '#6aaa4a') + ''.join(Pa(f'M{x},160 Q{x-4},{120-(k%3)*12} {x+(k%2)*8-4},{90+(k%4)*10} Q{x+4},{124} {x+6},160 Z', ['#4a9a3a', '#5aaa3a', '#7cc05a'][k % 3]) for k, x in enumerate(range(6, 200, 9))), shadow=False)
A['flowerpot'] = svg(potted(100, 176, 110, 100) + E(100, 70, 52, 8, '#8a4a2a'))
# seed 种子：手心里捧着几粒种子，旁边种子袋
g = hand_(80, 140, 1.2, 0, '#5aa1d4') + ''.join(E(70 + k * 8, 116 + (k % 2) * 4, 4, 3, '#5a3a24') for k in range(4))
g += R(130, 40, 54, 80, '#f6efe0', 2) + R(136, 48, 42, 42, '#a9d8f2') + flower(157, 70, 1.2, '#f3c234', '#8a5a35') + St('M157,80 L157,90', '#4a9a3a', 2) + ''.join(E(140 + k * 10, 104, 3, 2, '#5a3a24') for k in range(4))
A['seed'] = svg(g)
A['sunflower'] = svg(St('M100,100 L100,190', '#4a9a3a', 6) + leaf(100, 150, 44, 16, -30, '#5aaa3a') + leaf(100, 166, 44, 16, -150, '#5aaa3a') + daisy(100, 70, 74, '#f3c234', '#6a3a1a', 16) + ''.join(Ci(100 + 10 * math.cos(k), 70 + 10 * math.sin(k), 2, '#3a2010') for k in range(8)))
A['tulip'] = svg(tulip_(70, 80, 1.4, '#e2463b') + tulip_(130, 70, 1.5, '#f3c234') + tulip_(100, 100, 1.2, '#ef8fa4'))
# lily 百合：白色大喇叭形百合花，橙色花蕊
def lily(x, y, s):
    g = ''.join(G(Pa('M0,0 Q-14,-20 -6,-56 Q0,-62 6,-56 Q14,-20 0,0 Z', '#ffffff') + St('M0,-4 L0,-50', '#f2d0d8', 2), f'rotate({a})') for a in (-70, -35, 0, 35, 70, 180))
    g += ''.join(St(f'M0,0 L{14*math.cos(math.radians(-90+a))},{14*math.sin(math.radians(-90+a))-10}', '#5aaa3a', 1.5) + E(14 * math.cos(math.radians(-90 + a)), 14 * math.sin(math.radians(-90 + a)) - 12, 3, 5, '#d9641a') for a in (-30, 0, 30))
    return G(g, f'translate({x},{y}) scale({s})')
A['lily'] = svg(St('M100,100 L100,190', '#4a9a3a', 5) + leaf(100, 160, 40, 8, -40, '#5aaa3a') + leaf(100, 140, 40, 8, -140, '#5aaa3a') + lily(100, 96, 1.3))
# cactus 仙人掌：花盆里带刺的仙人掌，顶上开小花
g = potted(100, 186, 70, 44) + R(84, 50, 32, 96, '#5a9a4a', 16) + St('M84,110 L64,110 L64,80', '#5a9a4a', 20) + St('M116,96 L136,96 L136,70', '#5a9a4a', 20)
g += ''.join(L(84 + (k % 3) * 16, 60 + (k // 3) * 14, 80 + (k % 3) * 16 + (-4 if k % 2 else 4), 56 + (k // 3) * 14, '#f6f1e4', 1.5) for k in range(18)) + flower(100, 48, .9, '#ef8fa4')
A['cactus'] = svg(g)
# bamboo 竹子：几根带竹节的绿竹，竹叶
g = ''
for k, x in enumerate((60, 100, 140)):
    g += R(x - 8, 10, 16, 180, '#6aaa4a' if k % 2 else '#5a9a3a', 6) + ''.join(R(x - 9, 30 + j * 40 + k * 8, 18, 5, '#3c7a2c', 2) for j in range(4))
    g += leaf(x + 8, 40 + k * 20, 40, 8, -20, '#4a9a3a') + leaf(x - 8, 60 + k * 16, 40, 8, -160, '#5aaa3a')
A['bamboo'] = svg(g)
# orchid 兰花：一枝弯弯的花茎上开着几朵蝴蝶兰
def orchid_f(x, y, s, col='#c86ab8'):
    return G(E(-14, -8, 14, 10, col) + E(14, -8, 14, 10, col) + E(-12, 10, 11, 9, col) + E(12, 10, 11, 9, col) + E(0, 2, 7, 9, '#f3c234') + Ci(0, 0, 3, '#d9453a'), f'translate({x},{y}) scale({s})')
g = potted(70, 186, 60, 40, '#ffffff') + leaf(70, 146, 50, 14, -160, '#3c7a2c') + leaf(70, 146, 50, 14, -20, '#3c7a2c') + St('M70,146 Q70,60 140,50 Q170,52 176,80', '#5a7a3a', 3)
g += orchid_f(100, 76, 1.1) + orchid_f(136, 56, 1.1) + orchid_f(170, 86, 1.0)
A['orchid'] = svg(g)
# chrysanthemum 菊花：细长花瓣层层叠叠的黄菊花
def chrys(x, y, r, col='#f3c234'):
    g = ''
    for ring, rr in enumerate((r, r * .75, r * .5)):
        n = 20 - ring * 4
        g += ''.join(E(x + rr * .5 * math.cos(a), y + rr * .5 * math.sin(a), rr * .5, rr * .09 + 1, shade(col, -.08 * ring), f'transform="rotate({math.degrees(a):.0f} {x+rr*.5*math.cos(a):.1f} {y+rr*.5*math.sin(a):.1f})"') for a in [k * 2 * math.pi / n + ring * .2 for k in range(n)])
    return g + Ci(x, y, r * .14, shade(col, -.25))
A['chrysanthemum'] = svg(St('M100,110 L100,190', '#4a8a3a', 5) + leaf(100, 160, 34, 14, -30, '#4a8a3a') + leaf(100, 150, 34, 14, -150, '#4a8a3a') + chrys(100, 84, 80))
# peony 牡丹：层层叠叠的大朵粉色牡丹
g = leaf(100, 130, 60, 18, -20, '#4a8a3a') + leaf(100, 130, 60, 18, -160, '#4a8a3a')
for k, (rr, c) in enumerate([(64, '#f2a0b8'), (52, '#ef8fa4'), (40, '#f6b8cc'), (26, '#e2708a')]):
    g += ''.join(Ci(100 + rr * .45 * math.cos(a), 96 + rr * .4 * math.sin(a), rr * .45, c) for a in [j * 2 * math.pi / 7 + k for j in range(7)])
g += Ci(100, 94, 10, '#f3c234')
A['peony'] = svg(g)
# bush 灌木：修剪成圆团的绿色灌木丛
random.seed(111)
g = ''.join(Ci(100 + random.uniform(-60, 60), 120 + random.uniform(-40, 30), random.uniform(22, 32), random.choice(['#3c8a3a', '#4a9a3a', '#5aaa3a'])) for _ in range(22)) + R(0, 168, 200, 32, GRASS)
A['bush'] = svg(g, shadow=False)

# ================= 园艺 =================
# grow 种植/生长：从种子到幼苗到大株的三个阶段，箭头
g = soil_ground(150) + E(36, 148, 6, 4, '#5a3a24') + St('M100,150 L100,124', '#4a9a3a', 3) + leaf(100, 126, 16, 6, -30, '#5aaa3a') + leaf(100, 126, 16, 6, -150, '#5aaa3a')
g += St('M164,150 L164,70', '#4a9a3a', 4) + ''.join(leaf(164, 140 - k * 18, 28, 9, -30 if k % 2 else -150, '#5aaa3a') for k in range(4)) + daisy(164, 60, 30, '#f3c234', '#8a5a35') + arrow(48, 130, 84, 120, '#5ba644', 3) + arrow(116, 110, 146, 96, '#5ba644', 3)
A['grow'] = svg(g, shadow=False)
# dig 挖：铁锹插进土里，挖出一个坑
g = R(0, 0, 200, 120, '#e6f0d8') + soil_ground(120, 80) + E(100, 140, 40, 12, '#4a3020') + Pa('M140,130 Q150,110 170,116 Q186,126 180,140 Z', SOILL) + spade_(120, 120, .9, 20) + St('M88,40 L120,30', 'none', 0)
g += pose((60, 40), (62, 60), (66, 104), arms=[[(70, 64), (96, 60), (112, 54)], [(60, 66), (90, 80), (110, 70)]], legs=[[(62, 104), (54, 150)], [(70, 104), (84, 150)]], shirt='#5aa1d4', pants='#5d6469', style='grey', hr=13, tw=24, lw=11, aw=9)
A['dig'] = svg(g, shadow=False)
# pick 摘：手从植株上摘下一颗红草莓，放进小篮
g = R(0, 150, 200, 50, '#8cc06a') + ''.join(leaf(60 + k * 30, 150, 30, 12, -60 - k * 20, '#3c8a3a') for k in range(4))
g += Pa('M90,120 Q100,140 110,120 Q114,104 100,104 Q86,104 90,120 Z', '#d9302c') + ''.join(Ci(94 + k * 6, 112 + (k % 2) * 6, 1.2, '#f3d058') for k in range(3)) + hand_(108, 90, .7, 180, '#5aa1d4')
g += Pa('M130,160 L186,160 L178,190 L138,190 Z', '#c58b54') + ''.join(Ci(142 + k * 12, 156, 8, '#d9302c') for k in range(4)) + St('M134,160 Q158,130 182,160', '#a8703e', 3)
A['pick'] = svg(g, shadow=False)
# soil 土壤：一堆深褐色的泥土，旁边小铲
random.seed(112)
g = Pa('M20,170 Q40,100 100,90 Q160,100 180,170 Z', SOIL) + ''.join(Ci(random.uniform(40, 160), random.uniform(110, 166), random.uniform(2, 5), random.choice([SOILL, '#5a3a24'])) for _ in range(40)) + trowel_(160, 100, .8, 40)
A['soil'] = svg(g)
# weed 杂草：手把杂草连根拔出来
g = soil_ground(140, 60) + St('M100,100 L100,146', '#4a9a3a', 3) + ''.join(leaf(100, 110 - k * 4, 26, 6, -30 - k * 40, '#7a9a3a') for k in range(4)) + ''.join(St(f'M100,146 q{(k-2)*6},10 {(k-2)*10},26', '#c8b080', 2) for k in range(5))
g += hand_(100, 84, .8, 180, '#5aa1d4') + arrow(130, 140, 130, 90, '#5ba644', 3) + E(100, 146, 20, 5, '#4a3020')
A['weed'] = svg(g, shadow=False)
# water-the-plants 浇花：洒水壶往花上浇水
g = soil_ground(160, 40) + ''.join(St(f'M{60+k*40},160 L{60+k*40},120', '#4a9a3a', 3) + flower(60 + k * 40, 114, 1.0, ['#e2463b', '#f3c234', '#ef8fa4'][k]) for k in range(3)) + watering_can_(70, 50, .9, 20) + ''.join(L(132 + k * 6, 48, 120 + k * 8, 100, '#9fd0ec', 2) for k in range(5))
A['water-the-plants'] = svg(g, shadow=False)
# sunlight 阳光：太阳光照在一盆植物上
g = Ci(50, 50, 30, '#f3c234') + ''.join(L(50 + 36 * math.cos(a), 50 + 36 * math.sin(a), 50 + 48 * math.cos(a), 50 + 48 * math.sin(a), '#f3c234', 4) for a in [k * math.pi / 6 for k in range(12)]) + Pa('M70,70 L180,140 L130,180 Z', '#fff3a0', 'opacity=".5"')
g += potted(140, 186, 50, 36) + ''.join(leaf(140, 150, 36, 12, a, '#5aaa3a') for a in (-150, -110, -70, -30))
A['sunlight'] = svg(g)
# shade 阴凉处：大树下一片阴影，阴影里放着一盆蕨类
g = R(0, 0, 200, 200, '#e6f0d8') + R(0, 150, 200, 50, GRASS) + E(110, 160, 80, 14, '#5a8a4a', 'opacity=".5"') + tree(70, 110, 1.6) + Ci(180, 26, 14, '#f3c234')
g += potted(130, 172, 34, 24) + ''.join(leaf(130, 148, 30, 6, a, '#2f7a3a') for a in (-160, -120, -90, -60, -20))
A['shade'] = svg(g, shadow=False)
# fertilizer 肥料：一袋肥料倒出颗粒在植物根部
random.seed(113)
g = Pa('M30,180 L34,60 L106,60 L110,180 Z', '#5ba644') + Pa('M34,60 L44,46 L96,46 L106,60 Z', '#4a9a3a') + R(46, 90, 48, 50, '#ffffff', 4) + leaf(70, 128, 22, 8, -60, '#5ba644') + leaf(70, 128, 22, 8, -120, '#5ba644')
g += soil_ground(170, 30) + St('M150,170 L150,120', '#4a9a3a', 4) + leaf(150, 140, 26, 9, -30, '#5aaa3a') + leaf(150, 130, 26, 9, -150, '#5aaa3a') + ''.join(Ci(random.uniform(120, 180), random.uniform(160, 172), 2.5, '#f6efe0') for _ in range(16))
A['fertilizer'] = svg(g, shadow=False)
# harvest 收获：竹筐里装满刚收的蔬菜
g = Pa('M30,110 L170,110 L156,180 L44,180 Z', '#c58b54') + ''.join(L(34 + i * 2.4, 120 + i * 12, 166 - i * 2.4, 120 + i * 12, '#a8703e', 2.5) for i in range(5))
g += tomato_ if False else ''
g += Ci(60, 100, 18, '#e0392f') + leaf(60, 84, 10, 4, -90, '#3c8a3a') + broccoli(98, 90, .8) + carrot(136, 80, .8, 30) + E(152, 104, 18, 14, '#7a4fa0') + Ci(80, 108, 12, '#f08a24') + Ci(120, 108, 12, '#f3c234')
A['harvest'] = svg(g)
# seedling 幼苗：土里冒出一株两片叶的小苗
A['seedling'] = svg(soil_ground(140, 60) + St('M100,140 Q96,110 100,90', '#5aaa3a', 5) + leaf(100, 94, 50, 20, -20, '#7cc05a') + leaf(100, 94, 50, 20, -160, '#6ab04a') + E(100, 140, 20, 4, '#4a3020'), shadow=False)
# prune 修剪：修枝剪剪掉玫瑰的枯枝
g = rose_(70, 70, 1.3) + St('M70,140 L130,100 L150,90', '#3c7a2c', 3) + shears_(140, 100, .7, -60, True) + St('M150,90 L170,80', '#8a6a3a', 3) + St('M150,80 l6,-6 M164,96 l8,4', '#e2463b', 2)
A['prune'] = svg(g)
# compost 堆肥：绿色堆肥箱，里面菜叶果皮，冒出热气
g = R(30, 70, 140, 110, '#3c7a3a', 6) + ''.join(L(30, 80 + k * 20, 170, 80 + k * 20, '#2f6a2f', 3) for k in range(5)) + Pa('M30,70 L170,70 L160,50 L40,50 Z', '#2f6a2f')
g += Pa('M40,70 Q60,40 80,60 Q100,30 120,60 Q140,40 160,70 Z', SOIL) + leaf(60, 56, 20, 7, -40, '#8cc06a') + E(100, 52, 10, 4, '#f3c234') + Ci(130, 58, 6, '#d93a33') + steam(70, 40, 3, 26, '#c4cbd0', .6)
A['compost'] = svg(g)
# sow 播种：手往一行行的沟里撒种子
g = soil_ground(110, 90) + ''.join(R(0, 128 + k * 22, 200, 6, '#5a3a24') for k in range(3)) + hand_(110, 60, .8, 160, '#5aa1d4') + ''.join(E(96 + k * 4, 96 + k * 10, 3, 2, '#e8d4a8') for k in range(4)) + ''.join(E(30 + k * 24, 130, 3, 2, '#e8d4a8') for k in range(7))
A['sow'] = svg(g, shadow=False)
# mow-the-lawn 割草：推着割草机割草，后面草变短
g = R(0, 0, 200, 140, '#e6f0d8') + R(0, 140, 200, 60, '#6aaa4a') + R(0, 140, 110, 60, '#8cc06a') + ''.join(Pa(f'M{x},150 l3,-14 l3,14 Z', '#4a9a3a') for x in range(116, 200, 8))
g += mower(90, 160, .8) + pose((150, 60), (150, 82), (148, 128), arms=[[(142, 86), (132, 100), (156, 96)]], legs=[[(144, 128), (136, 176)], [(152, 128), (164, 176)]], shirt='#f08a24', pants='#3b4a5a', style='short', hr=13, tw=24, lw=11, aw=9)
A['mow-the-lawn'] = svg(g, shadow=False)
# transplant 移栽：把植物从小盆移到大盆，箭头
g = potted(50, 180, 40, 32) + Pa('M150,40 Q130,40 120,60', 'none', 'stroke="none"') + potted(140, 182, 80, 60) + E(140, 116, 36, 6, SOIL)
g += G(St('M0,0 L0,-40', '#4a9a3a', 4) + leaf(0, -30, 24, 9, -40, '#5aaa3a') + leaf(0, -36, 24, 9, -140, '#5aaa3a') + E(0, 6, 16, 12, SOIL) + ''.join(St(f'M0,10 q{(k-1)*6},8 {(k-1)*10},16', '#c8b080', 2) for k in range(3)), 'translate(96,84)') + arrow(56, 130, 84, 100, '#5ba644', 3) + arrow(110, 100, 130, 116, '#5ba644', 3)
A['transplant'] = svg(g)

# ================= 园艺工具 =================
A['spade'] = svg(spade_(100, 128, 1.0, 15))
A['rake'] = svg(rake_(100, 136, 1.05, 15))
# hose 水管：一卷绿色水管，喷头喷水
g = ''.join(E(80, 120, 60 - k * 8, 40 - k * 6, 'none', 'stroke="#5ba644" stroke-width="9"') for k in range(4)) + St('M140,120 Q160,90 150,60', '#5ba644', 9) + R(140, 40, 20, 24, '#f3c234', 4) + ''.join(L(150, 40, 130 + k * 10, 10, '#9fd0ec', 2) for k in range(5))
A['hose'] = svg(g)
A['watering-can'] = svg(watering_can_(90, 110, 1.4))
# wheelbarrow 手推车：独轮手推车装着泥土
g = Pa('M30,90 L150,90 L130,140 L50,140 Z', '#e2463b') + Pa('M34,90 Q90,60 146,90 Z', SOIL) + wheel(60, 160, 20) + L(50, 140, 60, 160, '#2f3437', 5) + St('M130,140 L186,150 M120,140 L120,180 M150,90 L190,120', '#2f3437', 5)
A['wheelbarrow'] = svg(g)
A['hoe'] = svg(hoe_(90, 146, 1.1, 15))
A['trowel'] = svg(trowel_(100, 120, 1.6, 30))
A['shears'] = svg(shears_(100, 100, 1.1, 0))
A['lawn-mower'] = svg(mower(90, 150, 1.4))
# sprinkler 洒水器：草坪上的洒水器转着喷出弧形水柱
g = R(0, 150, 200, 50, GRASS) + R(92, 130, 16, 24, '#5d6469', 3) + E(100, 128, 20, 6, '#a7adb1') + ''.join(St(f'M100,126 Q{100+k*18},{60-abs(k)*4} {100+k*34},{130}', '#9fd0ec', 3) for k in (-3, -2, -1, 1, 2, 3)) + ''.join(drop(100 + k * 34, 136, 4, '#9fd0ec') for k in (-3, 3))
A['sprinkler'] = svg(g, shadow=False)
# garden-fork 园艺叉：四齿的园艺叉插在土里
A['garden-fork'] = svg(soil_ground(150) + G(R(-4, -120, 8, 120, WOOD, 3) + Pa('M-16,-132 L16,-132 L16,-120 L-16,-120 Z', '#2f3437') + R(-28, 0, 56, 8, '#5d6469', 2) + ''.join(R(-28 + k * 17, 6, 5, 50, '#5d6469', 2) for k in range(4)), 'translate(100,128) rotate(10) scale(.9)'), shadow=False)
A['gardening-gloves'] = svg(gglove(70, 100, -15) + gglove(130, 106, 15, '#4a9a3a'))
A['pruning-shears'] = svg(shears_(100, 90, 1.3, 20, True))
# knee-pad 护膝：跪在地上干活用的软垫
g = R(40, 100, 120, 60, '#3c7fc1', 20) + R(50, 108, 100, 44, '#5aa1d4', 14) + R(80, 80, 40, 20, '#3c7fc1', 8) + ''.join(L(60 + k * 20, 112, 60 + k * 20, 148, '#3c7fc1', 2) for k in range(5))
A['knee-pad'] = svg(g)
# seed-tray 育苗盘：一格格的黑色育苗盘，每格冒出小苗
g = Pa('M20,120 L180,120 L170,170 L30,170 Z', '#2f3437') + Pa('M20,120 L40,90 L160,90 L180,120 Z', '#3a3f44')
for r_ in range(2):
    for c in range(5):
        x = 50 + c * 25 - r_ * 6; y = 102 + r_ * 16
        g += E(x, y, 9, 4, SOIL) + St(f'M{x},{y} L{x},{y-10}', '#5aaa3a', 2) + leaf(x, y - 8, 8, 3, -30, '#7cc05a') + leaf(x, y - 8, 8, 3, -150, '#7cc05a')
A['seed-tray'] = svg(g)
# leaf-blower 吹叶机：吹叶机把落叶吹走
g = G(R(-40, -20, 60, 40, '#f08a24', 12) + R(-30, -40, 30, 24, '#2f3437', 6) + R(20, -8, 90, 16, '#f08a24', 8), 'translate(70,90) rotate(15)')
g += ''.join(St(f'M{170+k*4},{130+k*10} q6,-6 12,0', '#c4cbd0', 2) for k in range(3)) + ''.join(leaf(150 + k * 14, 150 + (k % 2) * 16, 14, 6, k * 70, ['#e0a020', '#d9641a', '#c0403a'][k % 3]) for k in range(4))
A['leaf-blower'] = svg(g)

# ================= 花园景观 =================
# garden 花园：草坪、花坛、小树和栅栏组成的花园
g = R(0, 0, 200, 110, '#bfe6fa') + R(0, 110, 200, 90, GRASS) + ''.join(Pa(f'M{8+k*20},120 L{8+k*20},80 L{14+k*20},72 L{20+k*20},80 L{20+k*20},120 Z', '#ffffff') for k in range(10)) + R(0, 92, 200, 6, '#f2efe8')
g += tree(40, 110, .9) + ''.join(flower(100 + k * 20, 150 + (k % 2) * 8, 1.0, ['#e2463b', '#f3c234', '#ef8fa4', '#7a4fa0', '#e2463b'][k]) for k in range(5)) + Ci(170, 30, 14, '#f3c234')
A['garden'] = svg(g, shadow=False)
# lawn 草坪：修剪整齐的条纹草坪
g = R(0, 0, 200, 70, '#bfe6fa') + ''.join(Pa(f'M{-40+k*40},200 L{40+k*28},70 L{68+k*28},70 L{k*40},200 Z', '#7cc05a' if k % 2 else '#6aaa4a') for k in range(7)) + tree(170, 70, .6) + house(40, 74, 40, 20)
A['lawn'] = svg(g, shadow=False)
# path 小路：石板小路穿过草地
g = R(0, 0, 200, 200, GRASS) + ''.join(E(100 + (k % 2) * 16 - 8, 186 - k * 30, 34 - k * 3, 12 - k, '#c4bcae') for k in range(6)) + ''.join(flower(30 + (k % 2) * 140, 60 + k * 30, .8, ['#e2463b', '#f3c234'][k % 2]) for k in range(4))
A['path'] = svg(g, shadow=False)
A['bench'] = svg(R(0, 160, 200, 40, GRASS) + bench_(100, 170, 150) + tree(30, 120, .7), shadow=False)
# pond 池塘：草地上的池塘，荷叶、小鱼和石头
g = R(0, 0, 200, 200, GRASS) + E(100, 110, 84, 54, '#c4bcae') + E(100, 110, 76, 46, '#5aa1d4') + E(80, 100, 18, 8, '#3c8a3a') + E(130, 120, 14, 6, '#3c8a3a') + flower(84, 96, .7, '#ef8fa4') + G(fish_shape(0, 0, 30, '#f08a24', '#f6c070'), 'translate(110,96)')
g += Pa('M30,150 q10,-30 20,0 M170,150 q-10,-30 -20,0', '#5aaa3a') + ''.join(St(f'M{60+k*40},{126} q10,-4 20,0', '#9fd0ec', 2) for k in range(2))
A['pond'] = svg(g, shadow=False)
# fountain 喷泉：多层石喷泉往上喷水
g = E(100, 176, 80, 14, '#a7a09a') + E(100, 170, 76, 12, '#5aa1d4') + R(92, 110, 16, 60, '#c4bcae') + E(100, 112, 40, 8, '#c4bcae') + E(100, 108, 34, 6, '#5aa1d4') + R(96, 70, 8, 40, '#c4bcae') + E(100, 72, 18, 5, '#c4bcae')
g += St('M100,70 L100,30', '#9fd0ec', 5) + ''.join(St(f'M100,30 Q{100+k*20},20 {100+k*30},{70 if abs(k)==1 else 110}', '#9fd0ec', 3) for k in (-2, -1, 1, 2))
A['fountain'] = svg(g)
# swing 秋千：树枝上挂着的木秋千
g = R(0, 170, 200, 30, GRASS) + R(20, 20, 160, 14, '#8a5a35', 6) + R(20, 20, 14, 160, '#8a5a35', 4) + L(70, 30, 66, 130, '#c8a070', 3) + L(130, 30, 134, 130, '#c8a070', 3) + R(56, 128, 88, 10, WOOD, 3)
A['swing'] = svg(g, shadow=False)
# flower-bed 花坛：砖边围起来的花坛，里面开满郁金香
g = R(0, 0, 200, 200, GRASS) + R(20, 110, 160, 50, SOIL, 6) + R(16, 106, 168, 8, '#c0603a', 3) + R(16, 156, 168, 8, '#c0603a', 3)
g += ''.join(tulip_(36 + k * 22, 90 + (k % 2) * 8, .6, ['#e2463b', '#f3c234', '#ef8fa4', '#7a4fa0'][k % 4]) for k in range(7))
A['flower-bed'] = svg(g, shadow=False)
# hedge 树篱：修剪成方整长条的绿篱
random.seed(114)
g = R(0, 0, 200, 70, '#bfe6fa') + R(0, 160, 200, 40, GRASS) + R(10, 70, 180, 96, '#3c8a3a', 10) + ''.join(Ci(random.uniform(16, 184), random.uniform(78, 160), random.uniform(5, 9), random.choice(['#4a9a3a', '#2f7a2f'])) for _ in range(60))
A['hedge'] = svg(g, shadow=False)
# patio 露台：铺砖的露台，遮阳伞、桌椅和盆花
g = R(0, 0, 200, 90, '#bfe6fa') + Pa('M0,200 L40,90 L160,90 L200,200 Z', '#d9c8a8') + ''.join(L(40 - k * 8, 90 + k * 22, 160 + k * 8, 90 + k * 22, '#c4b090', 2) for k in range(5)) + ''.join(L(60 + k * 20, 90, 30 + k * 34, 200, '#c4b090', 2) for k in range(5))
g += Pa('M50,70 Q100,30 150,70 Z', '#e2463b') + L(100, 50, 100, 150, '#5d6469', 3) + E(100, 140, 36, 8, '#ffffff') + R(98, 140, 4, 30, '#a7adb1') + potted(176, 170, 26, 22) + flower(176, 140, 1.0, '#ef8fa4')
A['patio'] = svg(g, shadow=False)
# greenhouse 温室：玻璃温室，里面一排排绿苗
g = R(0, 170, 200, 30, GRASS) + Pa('M20,170 L20,90 L100,40 L180,90 L180,170 Z', '#dff1fb', 'opacity=".85"') + ''.join(L(20 + k * 32, 90 - (k if k <= 2.5 else 5 - k) * 0, 20 + k * 32, 170, '#ffffff', 3) for k in range(6)) + St('M20,90 L100,40 L180,90', '#ffffff', 4) + L(20, 130, 180, 130, '#ffffff', 2)
g += ''.join(St(f'M{36+k*20},164 L{36+k*20},146', '#4a9a3a', 3) + leaf(36 + k * 20, 150, 12, 5, -40, '#5aaa3a') + leaf(36 + k * 20, 150, 12, 5, -140, '#5aaa3a') for k in range(7))
A['greenhouse'] = svg(g, shadow=False)
# shed 小棚子：花园里的木头小工具棚
g = R(0, 170, 200, 30, GRASS) + R(40, 80, 120, 94, '#a8703e') + ''.join(L(40 + k * 12, 80, 40 + k * 12, 174, '#8a5a35', 2) for k in range(10)) + Pa('M30,84 L100,40 L170,84 Z', '#5a4a3a') + R(80, 110, 40, 64, '#8a5a35', 2) + Ci(112, 144, 3, '#d9a33a') + R(130, 100, 22, 18, '#a9d8f2', 2) + spade_(30, 170, .5, -10)
A['shed'] = svg(g, shadow=False)
# arch 拱门：爬满玫瑰的花园拱门
g = R(0, 170, 200, 30, GRASS) + St('M50,176 L50,80 Q50,30 100,30 Q150,30 150,80 L150,176', '#ffffff', 10) + St('M50,176 L50,80 Q50,30 100,30 Q150,30 150,80 L150,176', '#e6e6e0', 3)
random.seed(115)
g += ''.join(leaf(100 + 50 * math.cos(a), 80 - 50 * math.sin(a) + (40 if abs(math.cos(a)) > .9 else 0), 14, 6, random.uniform(0, 360), '#4a9a3a') for a in [k * math.pi / 12 for k in range(13)]) + ''.join(Ci(100 + 50 * math.cos(a), 80 - 50 * math.sin(a), 7, '#e2463b') for a in [k * math.pi / 6 + .2 for k in range(6)])
A['arch'] = svg(g, shadow=False)
# rock-garden 假山：叠起来的石头山，配小树和水
g = R(0, 170, 200, 30, GRASS) + E(100, 176, 90, 10, '#5aa1d4') + Pa('M40,176 Q30,120 60,110 Q50,70 90,60 Q100,30 120,50 Q150,50 146,90 Q170,110 160,176 Z', '#a7a09a')
g += Pa('M70,110 Q80,90 96,96 M110,70 Q120,60 130,72 M100,140 Q114,126 130,140', 'none', 'stroke="#7a7470" stroke-width="3"') + Ci(84, 130, 7, '#7a7470') + Ci(126, 104, 6, '#7a7470') + tree(132, 54, .4)
A['rock-garden'] = svg(g, shadow=False)
# bird-bath 鸟浴盆：石柱上的浅水盆，小鸟在戏水
g = R(0, 170, 200, 30, GRASS) + R(88, 100, 24, 74, '#c4bcae') + E(100, 176, 30, 6, '#a7a09a') + E(100, 100, 60, 12, '#c4bcae') + E(100, 96, 52, 8, '#9fd0ec')
g += G(E(0, 0, 16, 11, '#7a4a2a') + Ci(12, -8, 8, '#7a4a2a') + Pa('M18,-8 l8,2 l-8,2 Z', '#f3c234') + Ci(13, -10, 1.5, '#ffffff') + Pa('M-14,-2 L-26,-8 L-22,4 Z', '#5a3a1a') + E(-2, 2, 8, 5, '#d9a87a'), 'translate(90,84)') + drop(120, 80, 4, '#9fd0ec') + drop(130, 74, 3, '#9fd0ec')
A['bird-bath'] = svg(g, shadow=False)
# pergola 藤架：木藤架上爬满葡萄藤，挂着葡萄
g = R(0, 170, 200, 30, GRASS) + R(30, 60, 10, 116, WOOD) + R(160, 60, 10, 116, WOOD) + ''.join(R(16, 50 + k * 4, 168, 6, '#a8703e', 2) for k in range(1)) + ''.join(R(26 + k * 24, 40, 6, 24, '#a8703e', 1) for k in range(7))
random.seed(116)
g += ''.join(leaf(random.uniform(20, 180), random.uniform(40, 70), 16, 8, random.uniform(0, 360), '#4a9a3a') for _ in range(18)) + ''.join(''.join(Ci(x + (j % 3) * 6 - 6 - (j // 3) * -3, 76 + (j // 3) * 7, 4, '#6a2a6a') for j in range(8)) for x in (64, 110, 146)) + bench_(100, 176, 80)
A['pergola'] = svg(g, shadow=False)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
