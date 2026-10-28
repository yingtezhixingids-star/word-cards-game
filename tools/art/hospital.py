from flat import *
from fig import *
import os, sys

A = {}
SK = P['skin']; SKD = shade(SK, -.12)

# hospital 医院：多层白楼，楼顶红十字，玻璃大门
g = R(26, 52, 148, 128, '#f4f1ea', 4) + R(150, 52, 24, 128, '#e2ddd3')
g += R(70, 22, 60, 34, '#f4f1ea', 4) + R(76, 26, 48, 26, '#ffffff', 3) + cross(100, 39, 10)
for row in range(3):
    for col in range(5):
        if row == 2 and col in (1, 2, 3): continue
        g += R(36 + col * 26, 64 + row * 32, 18, 20, '#8ec3e6', 2) + R(36 + col * 26, 64 + row * 32, 18, 6, '#b5d9f0', 2)
g += R(70, 132, 60, 48, '#5aa1d4', 3) + L(100, 132, 100, 180, '#ffffff', 2.5) + R(64, 126, 72, 8, '#3c7fc1', 2)
g += R(18, 176, 164, 8, '#c8c3bc', 2)
g += Ci(16, 162, 14, '#5ba644') + R(14, 168, 4, 12, '#8a5a35') + Ci(186, 162, 14, '#5ba644') + R(184, 168, 4, 12, '#8a5a35')
A['hospital'] = svg(g, shadow=False)

# ambulance 救护车：白色面包车，红条纹、红十字、蓝色警灯
g = R(14, 74, 120, 84, '#ffffff', 8) + Pa('M134,92 L164,92 Q176,94 182,114 L186,140 L186,158 L134,158 Z', '#ffffff')
g += Pa('M140,98 L162,98 Q170,100 174,116 L140,116 Z', '#8ec3e6')
g += R(14, 124, 172, 12, '#d9453a') + R(14, 150, 172, 10, '#d9dcde', 4)
g += cross(70, 100, 14) + R(46, 62, 30, 14, '#3c7fc1', 4) + E(61, 62, 10, 6, '#8ec3e6')
g += R(176, 132, 10, 8, '#f3c234', 2) + R(12, 132, 6, 10, '#d9453a', 2)
g += L(134, 92, 134, 158, '#d9dcde', 2) + R(120, 112, 10, 3, '#a7adb1', 1)
g += wheel(50, 160, 17) + wheel(152, 160, 17)
g += St('M40,52 l-8,-8 M61,46 l0,-12 M82,52 l8,-8', '#3c7fc1', 3)
A['ambulance'] = svg(g)

# patient 病人：穿蓝白条纹病号服、手腕戴住院手环，背后病床床头
cx, cy, r = 100, 80, 32
g = R(40, 40, 120, 110, '#c4d6e2', 10) + R(48, 48, 104, 94, '#d9e6ee', 8)
g += stripes_body(cx, cy, r, '#ffffff', '#8ec3e6', w=r * 3.6)
g += face_full(cx, cy, r, P['grey'], 'grey', 'dot', 'flat', None)
g += arm([(cx + r * 1.6, 200), (cx + r * 1.4, cy + r * 2.2), (cx + r * .5, cy + r * 2.6)], '#ffffff', SK, 15)
g += R(cx + r * .62, cy + r * 2.4, 10, 8, '#f3c234', 2)
A['patient-hospital'] = svg(g, shadow=False)

# bed 病床：可升降病床，床头抬起、护栏、轮子
g = R(28, 70, 10, 88, '#a7adb1', 3) + R(166, 92, 10, 66, '#a7adb1', 3)
g += R(32, 120, 140, 12, '#5d6469', 4)
g += Pa('M36,120 L36,92 L80,104 L80,120 Z', '#ffffff') + R(78, 108, 92, 14, '#ffffff', 4) + R(78, 112, 92, 10, '#e2e9ee', 4)
g += Pa('M40,98 Q38,86 52,90 L72,96 Q80,100 72,106 Z', '#ffffff') + Pa('M46,96 L72,103', 'none', 'stroke="#d9dcde" stroke-width="2"')
g += R(100, 96, 70, 16, '#8ec3e6', 4)
g += R(84, 92, 50, 4, '#c4cbd0', 2) + R(88, 92, 4, 18, '#c4cbd0') + R(126, 92, 4, 18, '#c4cbd0')
g += L(40, 132, 40, 168, '#5d6469', 4) + L(164, 132, 164, 168, '#5d6469', 4) + L(100, 132, 100, 160, '#5d6469', 4)
g += wheel(40, 172, 7) + wheel(164, 172, 7) + wheel(100, 166, 6)
A['bed'] = svg(g)

# wheelchair 轮椅：侧视，大轮小轮、椅座靠背、扶手、脚踏
g = wheel(84, 140, 42, '#3a3f44', '#e6ecef')
g += Ci(84, 140, 34, 'none', 'stroke="#a7adb1" stroke-width="3"') + ''.join(L(84, 140, 84 + 34 * math.cos(a * math.pi / 4), 140 + 34 * math.sin(a * math.pi / 4), '#c4cbd0', 1.5) for a in range(8))
g += Ci(84, 140, 6, '#5d6469')
g += St('M54,50 L64,116 L130,116', '#3c7fc1', 7) + R(62, 108, 74, 12, '#2f5a8a', 4)
g += Pa('M56,52 L66,112 L60,112 L50,56 Z', '#2f5a8a')
g += St('M64,84 L120,84 L124,112', '#5d6469', 5) + St('M126,118 L148,158 L164,160', '#5d6469', 5)
g += St('M54,50 L44,44', '#5d6469', 6) + wheel(150, 170, 10, '#3a3f44', '#c4cbd0')
A['wheelchair'] = svg(g)

# emergency 急诊：急诊入口，红色灯箱和闪烁警灯（120）
g = R(20, 70, 160, 110, '#f4f1ea', 4) + R(20, 70, 160, 10, '#e2ddd3')
g += R(42, 38, 116, 34, '#d9453a', 6) + cross(66, 55, 10, '#ffffff') + T(118, 66, '120', 26, '#ffffff', 900)
g += R(60, 100, 80, 80, '#5aa1d4', 3) + L(100, 100, 100, 180, '#ffffff', 2.5) + R(54, 94, 92, 8, '#3c7fc1', 2)
g += R(70, 120, 20, 8, '#ffffff', 2, 'opacity=".5"')
for x in (30, 170):
    g += R(x - 8, 92, 16, 8, '#5d6469', 2) + Pa(f'M{x-8},92 Q{x-8},74 {x},74 Q{x+8},74 {x+8},92 Z', '#ff5a4a')
    g += St(f'M{x-14},80 l-8,-6 M{x},68 l0,-10 M{x+14},80 l8,-6', '#ff5a4a', 3)
A['emergency'] = svg(g, shadow=False)

# ward 病房：一排三张病床，隔帘，窗户
g = R(6, 30, 188, 150, '#eef3f1', 4) + R(6, 156, 188, 24, '#d6d0c2')
g += R(76, 42, 48, 36, '#8ec3e6', 3) + L(100, 42, 100, 78, '#ffffff', 3)
for i, x in enumerate((14, 74, 134)):
    g += R(x, 96, 8, 54, '#a7adb1', 2) + R(x, 124, 52, 14, '#ffffff', 3) + R(x + 18, 120, 34, 18, '#8ec3e6', 3)
    g += E(x + 14, 120, 9, 6, '#ffffff') + R(x, 138, 52, 6, '#5d6469', 2) + wheel(x + 6, 150, 4) + wheel(x + 46, 150, 4)
    if i == 1: g += Ci(x + 14, 114, 7, SK) + Pa(f'M{x+7},112 Q{x+14},104 {x+21},112 Z', P['grey'])
g += St('M64,34 L64,150', '#7fb7b0', 4) + Pa('M60,36 Q66,90 60,150 L68,150 Q72,90 68,36 Z', '#9ed0c9', 'opacity=".9"')
g += Pa('M124,36 Q130,90 124,150 L132,150 Q136,90 132,36 Z', '#9ed0c9', 'opacity=".9"') + L(6, 34, 194, 34, '#7fb7b0', 3)
A['ward'] = svg(g, shadow=False)

# operation 手术：无影灯下，两位穿绿色手术服的医生围着手术台
g = E(100, 40, 52, 16, '#d9dcde') + E(100, 44, 44, 11, '#fff6c8') + R(96, 0, 8, 26, '#a7adb1')
g += Pa('M56,48 L30,150 L170,150 L144,48 Z', '#fff6c8', 'opacity=".35"')
g += R(30, 136, 140, 14, '#5d6469', 4) + R(92, 150, 16, 30, '#7a8288') + R(70, 176, 60, 8, '#5d6469', 3)
g += R(36, 124, 128, 14, '#8fc7b8', 6) + E(48, 124, 10, 7, SK)
for x, flip in ((54, 1), (146, -1)):
    g += Pa(f'M{x-24},140 L{x-24},104 Q{x-24},90 {x-10},90 L{x+10},90 Q{x+24},90 {x+24},104 L{x+24},140 Z', '#4fa088')
    g += Ci(x, 74, 15, SK) + Pa(f'M{x-15},72 Q{x-15},56 {x},56 Q{x+15},56 {x+15},72 Z', '#3d8a74') + R(x - 13, 76, 26, 12, '#9ed6c9', 5)
    g += eyes_dot(x, 68, 15) + St(f'M{x+flip*10},100 L{x+flip*34},118', '#4fa088', 10) + Ci(x + flip * 36, 120, 5, '#c9e4f2')
A['operation'] = svg(g, shadow=False)

# surgeon 外科医生：绿色手术帽和口罩，戴手套的双手举起
cx, cy, r = 100, 76, 32
g = body(cx, cy, r, '#4fa088', w=r * 3.6)
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', '', None)
g += Pa(f'M{cx-r*.98},{cy-r*.15} Q{cx-r*1.05},{cy-r*1.25} {cx},{cy-r*1.2} Q{cx+r*1.05},{cy-r*1.25} {cx+r*.98},{cy-r*.15} Q{cx},{cy-r*.55} {cx-r*.98},{cy-r*.15} Z', '#3d8a74')
g += R(cx - r * .7, cy + r * .2, r * 1.4, r * .65, '#bfe3da', 8) + L(cx - r * .55, cy + r * .4, cx + r * .55, cy + r * .4, '#9ed0c4', 1.5) + L(cx - r * .55, cy + r * .6, cx + r * .55, cy + r * .6, '#9ed0c4', 1.5)
g += L(cx - r * .7, cy + r * .35, cx - r * .95, cy + r * .1, '#bfe3da', 2) + L(cx + r * .7, cy + r * .35, cx + r * .95, cy + r * .1, '#bfe3da', 2)
sl = shade('#4fa088', -.15)
for sx in (-1, 1):
    g += arm([(cx + sx * r * 1.5, 200), (cx + sx * r * 2.0, cy + r * 1.7), (cx + sx * r * 1.75, cy + r * .4)], sl, SK, 15, hand=False)
    g += hand(cx + sx * r * 1.75, cy + r * .55, .48, sx * 8, skin='#a9d4ee')
A['surgeon'] = svg(g)

# drip 输液：输液架挂着药水袋，管子连到手臂上的针头
g = R(58, 20, 6, 160, '#a7adb1', 2) + R(40, 20, 42, 5, '#a7adb1', 2) + St('M40,176 L82,176 M61,176 L46,188 M61,176 L76,188', '#5d6469', 4)
g += L(76, 22, 76, 34, '#a7adb1', 2) + Pa('M60,34 L92,34 Q96,34 96,40 L96,84 Q96,94 86,96 L66,96 Q56,94 56,84 L56,40 Q56,34 60,34 Z', '#dff1fb')
g += Pa('M56,58 L96,58 L96,84 Q96,94 86,96 L66,96 Q56,94 56,84 Z', '#a9d8f2') + R(64, 44, 24, 10, '#ffffff', 2)
g += R(73, 96, 6, 18, '#e6ecef', 2) + St('M76,114 Q78,150 120,150 Q150,150 150,132', '#bfe0ef', 3)
g += drop(76, 106, 3.5, '#7fc4ea')
g += R(122, 126, 80, 26, SK, 13) + R(122, 140, 80, 12, SKD, 6)
g += E(116, 138, 16, 14, SK) + ''.join(E(102 + i * 2, 128 + i * 7, 6, 4, SK) for i in range(4)) + E(108, 146, 6, 4, SKD)
g += R(140, 124, 22, 14, '#ffffff', 2, 'opacity=".95"') + R(176, 120, 26, 34, '#5aa1d4', 4)
A['drip'] = svg(g, shadow=False)

# crutches 拐杖：一对腋下拐杖
def crutch(x, rot):
    c = R(-3, 0, 6, 120, '#c4cbd0', 3) + R(-22, -6, 6, 80, '#c4cbd0', 3, 'transform="rotate(-8 -19 -6)"') + R(16, -6, 6, 80, '#c4cbd0', 3, 'transform="rotate(8 19 -6)"')
    c += R(-26, -18, 52, 14, '#5d6469', 7) + R(-14, 40, 28, 10, '#5d6469', 4) + R(-5, 118, 10, 14, '#3a3f44', 4)
    return G(c, f'translate({x},40) rotate({rot})')
g = crutch(76, -6) + crutch(126, 6)
A['crutches'] = svg(g)

# stretcher 担架：两根杆子中间是帆布，上面躺着盖着毯子的人
g = R(10, 120, 180, 8, '#a7adb1', 3) + R(10, 136, 180, 8, '#8a9196', 3)
g += R(28, 116, 144, 24, '#d9453a', 3) + R(28, 132, 144, 8, shade('#d9453a', -.2), 2)
g += Pa('M44,116 Q46,104 58,102 L60,116 Z', '#ffffff') + Ci(52, 104, 11, SK) + Pa('M41,102 Q42,90 54,92 Q62,94 62,100 Z', P['hair'])
g += Pa('M62,116 Q64,96 100,96 L164,98 Q172,100 170,116 Z', '#6aa7d8') + Pa('M62,116 Q64,104 100,104 L168,106 L170,116 Z', shade('#6aa7d8', -.1))
g += R(26, 140, 6, 16, '#5d6469', 2) + R(168, 140, 6, 16, '#5d6469', 2)
g += cross(170, 60, 12)
A['stretcher'] = svg(g)

# scan 扫描检查：CT 机大圆环，病人躺在检查床上滑进去
g = R(52, 140, 120, 12, '#c4cbd0', 3) + R(100, 152, 30, 28, '#a7adb1', 3)
g += Ci(146, 104, 52, '#e9eef1') + Ci(146, 104, 30, '#5d6469') + Ci(146, 104, 26, '#2f3437')
g += Ci(146, 104, 52, 'none', 'stroke="#c4cbd0" stroke-width="5"') + R(172, 60, 18, 8, '#3c7fc1', 2) + Ci(110, 70, 3, '#5ba644')
g += R(16, 118, 150, 16, '#ffffff', 6) + R(16, 126, 150, 8, '#e2e9ee', 4)
g += Ci(30, 108, 10, SK) + Pa('M20,106 Q22,96 32,98 Q38,100 38,104 Z', P['hair'])
g += Pa('M40,118 Q40,104 60,104 L150,106 L150,118 Z', '#8ec3e6')
A['scan'] = svg(g)

# visiting-hours 探视时间：墙上时钟，手提一束鲜花和水果篮
g = clock(70, 66, 44, (3, 0))
g += St('M40,126 l0,0', '#000', 0)
g += Pa('M130,178 L118,120 L158,120 L146,178 Z', '#d6b083') + Pa('M118,120 L158,120 L156,128 L120,128 Z', '#c09a6a')
for i, (x, y, c) in enumerate([(124, 104, '#ef8fa4'), (140, 96, '#d9453a'), (156, 104, '#f3c234'), (132, 86, '#ffffff'), (150, 84, '#ef8fa4')]):
    g += St(f'M{x},{y} L138,124', '#5ba644', 2.5)
for i, (x, y, c) in enumerate([(124, 104, '#ef8fa4'), (140, 96, '#d9453a'), (156, 104, '#f3c234'), (132, 86, '#ffffff'), (150, 84, '#ef8fa4')]):
    g += ''.join(Ci(x + 6 * math.cos(k * 1.2566), y + 6 * math.sin(k * 1.2566), 5, c) for k in range(5)) + Ci(x, y, 3.5, '#f3c234' if c != '#f3c234' else '#d98a2a')
g += leaf(124, 118, 18, 6, 200, '#5ba644') + leaf(152, 118, 18, 6, -20, '#5ba644')
g += Pa('M30,150 L96,150 L90,178 L36,178 Z', '#c58b54') + St('M36,150 Q63,118 90,150', '#8a5a35', 4)
g += Ci(48, 144, 10, '#d93a33') + Ci(66, 140, 10, '#f08a24') + Ci(82, 146, 9, '#9bc34a')
A['visiting-hours'] = svg(g)

# specialist 专科医生：戴眼镜的医生，手里拿着心脏模型讲解
cx, cy, r = 84, 72, 30
g = body(cx, cy, r, '#7fb3d8', w=r * 3.6) + coat_over(cx, cy, r, w=r * 3.6)
g += R(cx - r * .3, cy + r * .95, r * .6, r * 1.2, '#2f5a8a', 2)
g += face_full(cx, cy, r, P['grey'], 'grey', 'dot', 'smile', None)
g += Ci(cx - r * .34, cy, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + Ci(cx + r * .34, cy, 7, 'none', 'stroke="#2f3437" stroke-width="2"') + L(cx - r * .34 + 7, cy, cx + r * .34 - 7, cy, '#2f3437', 2)
g += stetho(cx, cy, r)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 2.1), (cx + r * 2.6, cy + r * 1.6)], '#ffffff', SK, 15)
g += heart(cx + r * 2.75, cy + r * 1.0, 22, '#d9453a') + St(f'M{cx+r*2.6},{cy+r*.35} q-4,-10 4,-14 M{cx+r*2.9},{cy+r*.4} q2,-10 10,-12', '#3c7fc1', 4)
g += hi(cx + r * 2.5, cy + r * .9, 5, 8, .5, -20)
g += R(cx - r * 1.4, cy + r * 1.6, 22, 8, '#3c7fc1', 2)
A['specialist'] = svg(g)

# recover 康复：笑着举起胳膊、精神好了，身边阳光
cx, cy, r = 100, 82, 32
g = Ci(40, 40, 18, '#f3c234') + ''.join(L(40 + 24 * math.cos(a * math.pi / 4), 40 + 24 * math.sin(a * math.pi / 4), 40 + 32 * math.cos(a * math.pi / 4), 40 + 32 * math.sin(a * math.pi / 4), '#f3c234', 3) for a in range(8))
g += body(cx, cy, r, '#5ba644')
g += face_full(cx, cy, r, P['grey'], 'grey', 'up', 'smile', None, '#ef9a8a')
g += E(cx, cy + r * .5, r * .22, r * .12, '#9a4a3a')
sl = shade('#5ba644', -.18)
g += arm([(cx + r * 1.55, 200), (cx + r * 2.05, cy + r * 1.1), (cx + r * 2.0, cy - r * .3)], sl, SK, 16)
g += arm([(cx - r * 1.55, 200), (cx - r * 2.05, cy + r * 1.1), (cx - r * 2.0, cy - r * .3)], sl, SK, 16)
g += star(cx + r * 2.5, cy - r * 1.2, 8) + star(cx - r * 2.3, cy - r * 1.3, 6) + star(cx + r * 1.2, cy - r * 1.6, 5)
A['recover'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
