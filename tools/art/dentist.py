from flat import *
from fig import *
import os, sys

A = {}
SK = P['skin']; SKD = shade(SK, -.12)

def tooth(x, y, s, col='#ffffff', side='#dfe6ea'):
    return G(Pa('M-20,-18 Q-22,-30 -10,-30 Q0,-26 0,-26 Q0,-26 10,-30 Q22,-30 20,-18 Q18,0 14,12 Q10,26 6,26 Q2,20 0,6 Q-2,20 -6,26 Q-10,26 -14,12 Q-18,0 -20,-18 Z', col) +
             Pa('M8,-29 Q22,-30 20,-18 Q18,0 14,12 Q10,26 6,26 Q12,0 8,-29 Z', side) + hi(-10, -16, 4, 8, .7, 10), f'translate({x},{y}) scale({s})')

def glasses(cx, cy, s=1, col='#2f3437', lens='#cfe8f6', shape='round', w=4):
    g = ''
    for sx in (-1, 1):
        x = cx + sx * 26 * s
        if shape == 'round':
            g += Ci(x, cy, 20 * s, lens, 'opacity=".7"') + Ci(x, cy, 20 * s, 'none', f'stroke="{col}" stroke-width="{w}"')
        else:
            g += R(x - 22 * s, cy - 14 * s, 44 * s, 28 * s, lens, 10 * s, 'opacity=".7"') + R(x - 22 * s, cy - 14 * s, 44 * s, 28 * s, 'none', 10 * s, f'stroke="{col}" stroke-width="{w}"')
    g += St(f'M{cx-8*s},{cy-4*s} Q{cx},{cy-10*s} {cx+8*s},{cy-4*s}', col, w)
    return g

# tooth 牙齿：一颗白色大臼齿
A['tooth'] = svg(tooth(100, 98, 2.6))

# dentist 牙医：白大褂、口罩拉到下巴，手拿口腔镜，头顶牙科灯
cx, cy, r = 90, 76, 32
g = body(cx, cy, r, '#7fc4c0', w=r * 3.6) + coat_over(cx, cy, r, w=r * 3.6)
g += face_full(cx, cy, r, '#3a2a20', 'bun', 'dot', 'smile', None)
g += R(cx - r * .6, cy + r * .78, r * 1.2, r * .4, '#bfe3f0', 6)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 1.7), (cx + r * 1.9, cy + r * .6)], '#ffffff', SK, 15)
g += L(cx + r * 1.9, cy + r * .5, cx + r * 2.05, cy - r * .7, '#a7adb1', 3) + E(cx + r * 2.08, cy - r * .9, 7, 9, '#dfe9ef') + E(cx + r * 2.08, cy - r * .9, 7, 9, 'none', 'stroke="#8a9196" stroke-width="2"')
g += tooth(cx - r * 1.1, cy + r * 2.2, .45)
A['dentist'] = svg(g)

# toothbrush 牙刷：蓝色牙刷，白蓝刷毛
g = G(R(-70, -9, 120, 18, '#3c7fc1', 9) + R(-70, -9, 120, 7, '#5aa1d4', 5) + R(30, -6, 60, 12, '#3c7fc1', 6) + E(-40, 0, 14, 5, '#8ec3e6') +
      ''.join(R(46 + i * 7, -32, 5, 26, '#ffffff' if i % 2 else '#bfe0ef', 2) for i in range(6)), 'translate(96,108) rotate(-25)')
A['toothbrush'] = svg(g)

# toothpaste 牙膏：挤出一截牙膏的软管
g = G(Pa('M-60,-24 L40,-20 L40,20 L-60,24 Z', '#ffffff') + Pa('M-60,-24 L-66,-24 L-66,24 L-60,24 Z', '#d9dcde') +
      Pa('M-46,-23 L20,-21 L20,21 L-46,23 Z', '#d9453a') + Pa('M-46,-6 L20,-6 L20,6 L-46,6 Z', '#ffffff') + R(-40, -2, 54, 4, '#3c7fc1', 2) +
      R(40, -12, 10, 24, '#e6ecef', 2) + R(50, -14, 18, 28, '#3c7fc1', 4), 'translate(84,118) rotate(-15)')
g += St('M154,98 q14,-6 20,-18 q4,-10 -6,-12 q-10,0 -8,10', '#ffffff', 11) + St('M154,98 q14,-6 20,-18 q4,-10 -6,-12', '#7fc4ea', 3, 'opacity=".6"')
A['toothpaste'] = svg(g)

# optician 眼镜店：店面招牌上挂着一副大眼镜
g = R(18, 64, 164, 116, '#f4f1ea', 4) + R(12, 54, 176, 20, '#2f5a8a', 3)
g += ''.join(Pa(f'M{18+i*20},74 L{38+i*20},74 L{36+i*20},92 Q{28+i*20},98 {20+i*20},92 Z', '#3c7fc1' if i % 2 else '#ffffff') for i in range(8))
g += glasses(100, 32, 1.05, '#2f3437', '#bfe0ef', 'round', 5)
g += R(30, 104, 74, 60, '#8ec3e6', 3) + R(116, 104, 50, 76, '#5d6469', 3) + Ci(158, 144, 2.5, '#d9a33a')
for i in range(3):
    g += glasses(67, 118 + i * 16, .38, '#2f3437', '#ffffff', 'rect', 2)
A['optician'] = svg(g, shadow=False)

# eye-test 视力检查：E 字视力表，指示棒
def E_(x, y, s, rot):
    return G(R(-s / 2, -s / 2, s, s * .2, '#2f3437') + R(-s / 2, -s * .1, s, s * .2, '#2f3437') + R(-s / 2, s * .3, s, s * .2, '#2f3437') + R(-s / 2, -s / 2, s * .2, s, '#2f3437'), f'translate({x},{y}) rotate({rot})')
g = R(48, 14, 104, 166, '#ffffff', 4) + R(48, 14, 104, 166, 'none', 4, 'stroke="#c4cbd0" stroke-width="3"')
rows = [(1, 34, 0), (2, 22, 1), (3, 15, 2), (4, 11, 3), (5, 8, 4), (6, 6, 5)]
y = 44
import itertools
rots = itertools.cycle([0, 90, 180, 270, 90, 0, 270, 180])
for n, s, _ in rows:
    for k in range(n):
        g += E_(100 - (n - 1) * s * .8 + k * s * 1.6, y, s, next(rots))
    y += s + 10
g += St('M178,186 L118,96', '#c58b54', 4) + Ci(118, 96, 3, '#d9453a')
A['eye-test'] = svg(g)

# filling 补牙：一颗牙上面补了银灰色的填充物，旁边牙钻
g = tooth(84, 104, 2.2) + Pa('M60,50 Q72,40 88,48 Q98,56 92,66 Q80,72 66,66 Q56,60 60,50 Z', '#a7b2ba') + hi(70, 54, 6, 3, .7)
g += G(R(-6, -70, 12, 74, '#e6ecef', 5) + R(-8, -70, 16, 20, '#c4cbd0', 4) + R(-3, 4, 6, 14, '#a7adb1', 2) + R(-1.2, 18, 2.4, 10, '#5d6469'), 'translate(150,70) rotate(35)')
A['filling'] = svg(g)

# gum 牙龈：张开的嘴，上下粉红色牙龈和一排牙
g = E(100, 100, 80, 60, '#d9645a') + E(100, 100, 66, 46, '#5a1e1e')
g += Pa('M36,82 Q100,40 164,82 Q100,66 36,82 Z', '#ef8fa4') + Pa('M36,118 Q100,160 164,118 Q100,136 36,118 Z', '#ef8fa4')
g += ''.join(R(48 + i * 13, 74 - (abs(i - 3.5) < 2) * 2, 12, 16, '#ffffff', 4) for i in range(8))
g += ''.join(R(52 + i * 12.5, 112, 11, 14, '#ffffff', 4) for i in range(8))
g += E(100, 120, 26, 10, '#c84a5a') + Pa('M36,82 Q100,40 164,82 L164,80 Q100,34 36,80 Z', '#e2645a')
g += Pa('M150,74 L172,58', 'none', 'stroke="#2f3437" stroke-width="3"') + Pa('M144,78 L156,66 L160,76 Z', '#2f3437')
A['gum'] = svg(g)

# dentures 假牙：泡在水杯里的一副假牙
g = R(46, 52, 108, 128, '#dff1fb', 10, 'opacity=".9"') + R(46, 90, 108, 90, '#bfe0ef', 10, 'opacity=".9"') + R(54, 60, 12, 110, '#ffffff', 6, 'opacity=".5"')
g += E(100, 134, 40, 22, '#ef8fa4') + E(100, 128, 30, 14, '#e47a8e')
g += ''.join(R(66 + i * 8.6, 116 + abs(i - 3.5) * 1.6, 8, 12, '#ffffff', 3) for i in range(8))
g += Ci(80, 80, 3, '#ffffff') + Ci(118, 100, 2.5, '#ffffff') + Ci(130, 70, 3.5, '#ffffff') + E(100, 90, 54, 4, '#ffffff', 'opacity=".5"')
A['dentures'] = svg(g)

# reading-glasses 老花镜：放在打开的书上的老花镜
g = Pa('M14,150 L100,136 L186,150 L186,164 L100,152 L14,164 Z', '#c58b54')
g += Pa('M20,80 Q60,70 100,86 L100,150 Q60,134 20,144 Z', '#ffffff') + Pa('M180,80 Q140,70 100,86 L100,150 Q140,134 180,144 Z', '#f4f1ea')
g += ''.join(L(30, 92 + i * 10, 90, 98 + i * 10 - i * .3, '#c4cbd0', 2) for i in range(5)) + ''.join(L(110, 98 + i * 10, 170, 92 + i * 10, '#c4cbd0', 2) for i in range(5))
g += G(glasses(0, 0, 1.0, '#8a5a35', '#e6f3fa', 'rect', 4.5) + St('M-48,-4 L-70,-14', '#8a5a35', 4) + St('M48,-4 L70,-14', '#8a5a35', 4), 'translate(100,96) rotate(-6)')
A['reading-glasses'] = svg(g, shadow=False)

# floss 牙线：圆盒子拉出一段白色细线
g = Ci(84, 118, 44, '#7fc4c0') + Ci(84, 112, 44, '#9edad6') + Ci(84, 112, 30, '#bfe8e5') + R(118, 98, 14, 10, '#d9dcde', 2)
g += St('M130,102 Q160,90 168,60 Q172,40 160,30', '#ffffff', 3) + St('M130,102 Q160,90 168,60', '#d9dcde', 1)
g += hi(66, 96, 12, 6, .6, -20)
A['floss'] = svg(g)

# frame 镜框：一副没有镜片的黑框眼镜架在展示台上
g = R(40, 150, 120, 14, '#c58b54', 4) + R(50, 140, 100, 12, '#d6a06a', 4)
g += glasses(100, 100, 1.5, '#4a2f20', 'none', 'rect', 7) + St('M34,94 L22,84', '#4a2f20', 6) + St('M166,94 L178,84', '#4a2f20', 6)
A['frame'] = svg(g)

# lens 镜片：单独一块透明镜片，边上有反光
g = E(100, 100, 60, 46, '#cfe8f6', 'opacity=".95"') + E(100, 100, 60, 46, 'none', 'stroke="#9fc9e3" stroke-width="5"')
g += Pa('M62,84 Q74,64 100,60', 'none', 'stroke="#ffffff" stroke-width="7" stroke-linecap="round"') + Ci(132, 120, 5, '#ffffff', 'opacity=".8"')
g += St('M110,82 L140,106', '#9fc9e3', 2)
g += R(20, 160, 70, 18, '#ef8fa4', 4) + L(30, 166, 80, 166, '#e47a8e', 2) + L(30, 172, 80, 172, '#e47a8e', 2)
A['lens'] = svg(g)

# contact-lenses 隐形眼镜：指尖上一片透明薄镜片，旁边双联盒（L R）
g = Pa('M30,200 L30,140 Q30,106 60,104 Q88,104 88,136 L88,200 Z', SK) + E(59, 112, 14, 10, shade(SK, .25))
g += Pa('M40,112 Q59,86 78,112 Q59,104 40,112 Z', '#9fd0ec', 'opacity=".85"') + Pa('M46,104 Q56,96 64,98', 'none', 'stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"')
g += R(108, 120, 82, 40, '#e6ecef', 18)
g += Ci(128, 140, 16, '#3c7fc1') + Ci(170, 140, 16, '#5ba644') + T(128, 147, 'L', 18, '#ffffff', 800) + T(170, 147, 'R', 18, '#ffffff', 800)
A['contact-lenses'] = svg(g)

# short-sighted 近视：眯着眼看远处模糊的字
cx, cy, r = 62, 90, 30
g = '<defs><filter id="bl"><feGaussianBlur stdDeviation="2.6"/></filter></defs>'
g += R(118, 30, 70, 90, '#ffffff', 4) + R(118, 30, 70, 90, 'none', 4, 'stroke="#c4cbd0" stroke-width="2"')
g += f'<g filter="url(#bl)">' + E_(153, 52, 20, 0) + E_(140, 82, 12, 90) + E_(166, 82, 12, 180) + E_(134, 104, 8, 270) + E_(153, 104, 8, 0) + E_(172, 104, 8, 90) + '</g>'
g += body(cx, cy, r, '#d98a4a')
g += bare_head(cx, cy, r, '#3a2a20', 'short')
g += L(cx - r * .34 - 6, cy, cx - r * .34 + 6, cy, '#2b211b', 3) + L(cx + r * .34 - 6, cy, cx + r * .34 + 6, cy, '#2b211b', 3)
g += brows_sad(cx, cy, r) + nose_line(cx, cy, r) + mouth(cx, cy, r, 'flat')
g += T(104, 60, '?', 26, '#3c7fc1', 800)
A['short-sighted'] = svg(g)

# crown 牙冠：一颗牙戴着金色的牙冠
g = tooth(100, 112, 2.3)
g += Pa('M54,70 Q50,42 76,42 Q90,44 100,52 Q110,44 124,42 Q150,42 146,70 Q140,88 100,86 Q60,88 54,70 Z', '#e0b040')
g += Pa('M118,44 Q150,42 146,70 Q140,88 110,86 Q134,70 118,44 Z', '#c89a2a') + hi(72, 56, 8, 4, .7, -10)
g += star(150, 36, 6, '#f3d26a') + star(56, 34, 4, '#f3d26a')
A['crown'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
