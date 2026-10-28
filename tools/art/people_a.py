from kit3 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)
BONE = '#dccfae'; BONED = '#bfae88'

FACE = lambda **kw: big_face(100, 104, 62, **kw)
BODY = body_front(100, 192, '#7fc4c0', '#3b5f8f', 1.0)
# 身体关键点（person 100,192,s=1）
HY = 192 - 168 + 15

# ================= 身体部位 =================
S_('head', BODY + ring(100, HY, 22))
S_('eye', FACE(hair='#3a2a20') + ring(100 - 62 * .34, 104, 16))
S_('ear', FACE(hair='#3a2a20') + ring(100 + 62 * .95, 110, 18))
S_('nose', FACE(hair='#3a2a20') + ring(100, 116, 16))
S_('mouth', FACE(hair='#3a2a20', m='grin') + ring(100, 136, 22))
S_('hair', FACE(hair='#5a3a2a', style='long') + ring(100, 46, 26))
S_('face', FACE(hair='#3a2a20') + E(100, 108, 64, 72, 'none', f'stroke="{HL}" stroke-width="4" stroke-dasharray="8 6"'))
S_('neck', BODY + ring(100, HY + 19, 12))
S_('arm', BODY + E(80, 94, 12, 32, 'none', f'stroke="{HL}" stroke-width="4"'))
S_('leg', BODY + E(91, 158, 12, 36, 'none', f'stroke="{HL}" stroke-width="4"'))
# back 背：人物背影，背部画圈
g = person(100, 192, shirt='#7fc4c0', pants='#3b5f8f', arms='down', style='short') + Ci(100, HY, 15, '#3a2a20') + E(100, HY + 6, 14, 10, '#3a2a20') + ring(100, 88, 20)
S_('back', g)
S_('shoulder', BODY + ring(116, 64, 12))
S_('knee', BODY + ring(91, 156, 11))
S_('chest', BODY + ring(100, 80, 16))
S_('waist', BODY + E(100, 114, 24, 10, 'none', f'stroke="{HL}" stroke-width="4"'))
S_('belly', BODY + ring(100, 102, 14))

# ================= 手和脚 =================
def palm_hand(x, y, s=1, rot=0, lines=True):
    g = R(-26, -50, 52, 60, SK, 18) + ''.join(R(-24 + k * 12.5, -100 + abs(k - 1.5) * 8, 11, 56 - abs(k - 1.5) * 6, SK, 5.5) for k in range(4)) + G(R(-7, -36, 14, 40, SK, 7), 'translate(-28,-14) rotate(-35)')
    if lines: g += St('M-18,-32 Q0,-26 20,-36', SKD, 1.8) + St('M-20,-22 Q-4,-14 14,-10', SKD, 1.8) + St('M-14,-40 Q-20,-12 -6,6', SKD, 1.8)
    g += R(-22, 6, 44, 30, SK, 6)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def foot_side(x, y, s=1):
    g = Pa('M-50,0 Q-56,-14 -44,-20 L-40,-60 L-16,-60 L-12,-26 Q10,-20 40,-14 Q56,-10 56,0 Z', SK) + Pa('M-50,0 L56,0 Q56,-6 52,-8 L-52,-6 Z', SKD) + ''.join(E(48 - k * 2, -6 - k * 3, 0, 0, SK) for k in range(0))
    return G(g, f'translate({x},{y}) scale({s})')

def foot_top(x, y, s=1):
    g = Pa('M-30,60 Q-40,0 -34,-30 Q-30,-50 -6,-50 Q24,-50 30,-30 Q36,0 26,60 Z', SK)
    for k, (dx, dy, r) in enumerate([(-24, -56, 10), (-6, -62, 8), (8, -60, 7), (20, -56, 6), (30, -48, 5.5)]):
        g += Ci(dx, dy, r, SK) + E(dx, dy - r * .4, r * .5, r * .35, shade(SK, .25))
    return G(g, f'translate({x},{y}) scale({s})')

def fist_(x, y, s=1, rot=0):
    g = R(-30, -30, 60, 56, SK, 16) + ''.join(R(-28 + k * 14, -40, 14, 26, SK, 7) + L(-14 + k * 14, -34, -14 + k * 14, -18, SKD, 1.5) for k in range(4)) + G(R(-8, -22, 16, 36, SK, 8), 'translate(-30,0) rotate(-70)') + R(-24, 24, 48, 24, SK, 6)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

S_('hand', palm_hand(100, 140, 1.0, 0) + St('M70,186 L130,186', '#5aa1d4', 0))
S_('foot', foot_side(100, 150, 1.4))
S_('finger', palm_hand(100, 150, 1.0) + ring(100 - 24 + 12.5 + 5.5, 72, 14))
S_('thumb', thumbs_up(100, 120, 2.4) + ring(100, 50, 20))
S_('toe', foot_top(100, 120, 1.2) + ring(100 - 24 * 1.2, 120 - 56 * 1.2, 16))
S_('nail', palm_hand(90, 150, 1.0, 0) + ''.join(E(90 - 24 + k * 12.5 + 5.5, 150 - 96 + abs(k - 1.5) * 8, 4, 5, '#f6dcd0') for k in range(4)) + ring(90 - 24 + 12.5 + 5.5, 150 - 96 + 4, 10))
S_('wrist', palm_hand(100, 120, 1.0) + R(76, 150, 48, 60, SK) + E(100, 158, 30, 12, 'none', f'stroke="{HL}" stroke-width="4"'))
S_('palm', palm_hand(100, 150, 1.0) + ring(100, 120, 24))
S_('fist', fist_(100, 110, 1.6))
S_('heel', foot_side(100, 150, 1.4) + ring(100 - 48 * 1.4, 140, 16))
S_('ankle', foot_side(100, 150, 1.4) + ring(100 - 28 * 1.4, 150 - 46 * 1.4, 16))
# sole 脚底：抬起的脚，露出脚底板
S_('sole', G(Pa('M-30,60 Q-40,0 -34,-30 Q-30,-50 -6,-50 Q24,-50 30,-30 Q36,0 26,60 Z', '#f2c8a8') + ''.join(Ci(dx, dy, r, '#f2c8a8') for dx, dy, r in [(-24, -56, 10), (-6, -62, 8), (8, -60, 7), (20, -56, 6), (30, -48, 5.5)]) + E(0, 30, 22, 26, '#e8b898') + E(-4, -24, 26, 20, '#e8b898'), 'translate(100,110) scale(1.2)') + ring(100, 120, 40))
S_('knuckle', fist_(100, 120, 1.6) + E(100, 120 - 40 * 1.6 + 14, 50, 14, 'none', f'stroke="{HL}" stroke-width="4"'))
S_('little-finger', palm_hand(100, 150, 1.0) + ring(100 - 24 + 3 * 12.5 + 5.5, 150 - 100 + 12 + 10, 14))
S_('index-finger', G(R(-30, -30, 60, 56, SK, 16) + ''.join(R(-14 + k * 14, -40, 14, 26, SK, 7) for k in range(3)) + R(-30, -110, 15, 84, SK, 7.5) + G(R(-8, -22, 16, 36, SK, 8), 'translate(-30,0) rotate(-70)') + R(-24, 24, 48, 30, SK, 6), 'translate(100,130) scale(1.2)') + ring(78, 18, 16))
S_('big-toe', foot_top(100, 120, 1.2) + ring(100 - 24 * 1.2, 120 - 56 * 1.2, 16) + St('M30,20 L60,40', HL, 0))

# ================= 肌肉和骨骼 =================
def bone_(x, y, s=1, rot=0, l=60):
    return G(R(-l / 2, -7, l, 14, BONE, 4) + Ci(-l / 2, -9, 10, BONE) + Ci(-l / 2, 9, 10, BONE) + Ci(l / 2, -9, 10, BONE) + Ci(l / 2, 9, 10, BONE), f'translate({x},{y}) rotate({rot}) scale({s})')

def skull_(x, y, s=1):
    g = E(0, -10, 44, 46, BONE) + R(-24, 20, 48, 26, BONE, 8) + E(-17, -2, 12, 14, '#5d5048') + E(17, -2, 12, 14, '#5d5048') + Pa('M0,12 L-6,24 L6,24 Z', '#5d5048') + ''.join(R(-18 + k * 7, 36, 5, 10, '#ffffff', 1) for k in range(6))
    return G(g, f'translate({x},{y}) scale({s})')

def ribcage(x, y, s=1):
    g = ''.join(R(-5, -60 + k * 14, 10, 12, BONE, 3) for k in range(10))
    for k in range(6):
        yy = -50 + k * 15
        w = 40 + k * 4 - (k > 4) * 8
        g += St(f'M-5,{yy} Q{-w},{yy-6} {-w+6},{yy+16}', BONE, 6) + St(f'M5,{yy} Q{w},{yy-6} {w-6},{yy+16}', BONE, 6)
    g += R(-6, -64, 12, 50, BONED, 3)
    return G(g, f'translate({x},{y}) scale({s})')

def pelvis_(x, y, s=1):
    g = Pa('M-60,-20 Q-70,-50 -40,-50 Q-20,-30 -10,-10 L10,-10 Q20,-30 40,-50 Q70,-50 60,-20 Q50,10 24,22 L14,30 L-14,30 L-24,22 Q-50,10 -60,-20 Z', BONE) + E(-26, 6, 10, 12, '#e6dcc8') + E(26, 6, 10, 12, '#e6dcc8') + E(0, -6, 14, 10, '#e6dcc8')
    return G(g, f'translate({x},{y}) scale({s})')

def skeleton_(x, y, s=1):
    g = skull_(0, -150, .45) + R(-3, -128, 6, 120, BONE, 2) + G(ribcage(0, 0, .55), 'translate(0,-90)') + pelvis_(0, -14, .55)
    for sx in (-1, 1):
        g += St(f'M{sx*8},-118 L{sx*30},-114', BONE, 5) + St(f'M{sx*30},-114 L{sx*36},-70 L{sx*38},-28', BONE, 5) + Ci(sx * 38, -24, 5, BONE)
        g += St(f'M{sx*14},0 L{sx*16},50 L{sx*16},100', BONE, 6) + Ci(sx * 16, 50, 5, BONE) + E(sx * 22, 104, 10, 4, BONE)
    return G(g, f'translate({x},{y}) scale({s})')

def arm_bent(x, y, s=1, muscle=False):
    g = St('M0,0 L50,0', SK, 24) + St('M50,0 L54,-56', SK, 20) + Ci(56, -66, 14, SK)
    if muscle: g += E(28, -10, 22, 14, shade(SK, .05)) + St('M14,-16 Q28,-26 42,-16', SKD, 2)
    g += R(-40, -14, 40, 28, '#3c7fc1', 8)
    return G(g, f'translate({x},{y}) scale({s})')

S_('bone', bone_(100, 100, 1.6, -30))
S_('muscle', arm_bent(40, 140, 1.5, True) + ring(84, 124, 26))
S_('skull', skull_(100, 100, 1.4))
# spine 脊柱：一节节椎骨叠成的脊柱，S 形
g = ''.join(G(R(-14, -6, 28, 12, BONE, 4) + R(-6, -10, 12, 4, BONED, 1) + R(14, -3, 10, 6, BONE, 2) + R(-24, -3, 10, 6, BONE, 2), f'translate({100+12*math.sin(k/3)},{24+k*14})') for k in range(12))
S_('spine', g)
S_('rib', ribcage(100, 110, 1.3) + ring(60, 110, 16))
# joint 关节：膝关节示意，两根骨头相接，关节处画圈
g = bone_(100, 60, 1.0, 90, 70) + bone_(100, 150, 1.0, 90, 70) + E(100, 106, 22, 10, '#9fd0ec', 'opacity=".8"') + ring(100, 106, 30)
S_('joint', g)
S_('hip', BODY + ring(110, 122, 14))
S_('elbow', arm_bent(40, 140, 1.5) + ring(40 + 50 * 1.5, 140, 18))
S_('jaw', big_face(100, 96, 60, hair='#3a2a20') + St(f'M{100-56},{120} Q{100},{190} {100+56},{120}', HL, 5))
# x-ray X光片：灯箱上一张黑底X光片，显示胸腔骨骼
S_('x-ray', R(30, 20, 140, 160, '#c4cbd0', 6) + R(38, 28, 124, 144, '#1f2a35', 3) + G(ribcage(0, 0, .8), 'translate(100,96)').replace(BONE, '#dfe8ee').replace(BONED, '#b8c8d0'))
S_('skeleton', skeleton_(100, 140, .85))
S_('pelvis', pelvis_(100, 100, 1.4))
# kneecap 膝盖骨：腿骨相接处一块圆形小骨头被圈出
S_('kneecap', bone_(100, 50, 1.0, 90, 70) + bone_(100, 160, 1.0, 90, 70) + E(100, 104, 18, 22, BONE) + E(100, 104, 18, 22, 'none', f'stroke="{BONED}" stroke-width="2"') + ring(100, 104, 28))
# collarbone 锁骨：上半身骨骼，肩下横着的两根锁骨高亮
S_('collarbone', skull_(100, 46, .55) + R(97, 70, 6, 30, BONE) + G(ribcage(0, 0, .7), 'translate(100,140)') + St('M100,96 Q70,88 44,96', HL, 7) + St('M100,96 Q130,88 156,96', HL, 7))
# tendon 肌腱：脚后跟上方连着小腿的那条腱高亮
S_('tendon', foot_side(100, 170, 1.4) + R(100 - 40 * 1.4, 10, 34, 80, SK) + St(f'M{100-46*1.4},{30} L{100-46*1.4},{150}', HL, 6))
# cartilage 软骨：关节处骨头末端覆盖蓝色软骨
S_('cartilage', bone_(100, 56, 1.0, 90, 70) + bone_(100, 150, 1.0, 90, 70) + E(100, 92, 22, 7, '#7fc4e8') + E(100, 116, 22, 7, '#7fc4e8') + ring(100, 104, 30, '#3c7fc1'))

# ================= 内脏 =================
def heart_organ(x, y, s=1):
    g = Pa('M0,50 Q-50,20 -46,-14 Q-40,-44 -10,-36 Q0,-34 4,-26 Q16,-46 38,-36 Q56,-20 44,10 Q30,40 0,50 Z', '#c0283a') + Pa('M4,-26 Q16,-46 38,-36 Q56,-20 44,10 Q30,40 0,50 Q30,10 4,-26 Z', '#a01e30')
    g += R(-12, -60, 12, 28, '#d94a5a', 5) + R(4, -58, 12, 26, '#5a7ac8', 5) + St('M-2,-60 Q-2,-76 20,-76', '#d94a5a', 10) + hi(-24, -10, 8, 14, .3, 20)
    return G(g, f'translate({x},{y}) scale({s})')
S_('heart', heart_organ(100, 110, 1.5))
S_('lung', R(96, 30, 8, 50, '#e6b0b8', 4) + St('M100,76 L76,92 M100,76 L124,92', '#e6b0b8', 6) + Pa('M88,80 Q60,60 44,100 Q34,150 50,170 Q80,176 90,150 Z', '#ef8fa4') + Pa('M112,80 Q140,60 156,100 Q166,150 150,170 Q120,176 110,150 Z', '#ef8fa4') + St('M76,92 L66,120 M76,92 L80,130', '#e07a90', 2) + St('M124,92 L134,120 M124,92 L120,130', '#e07a90', 2))
S_('brain', Pa('M100,64 Q70,46 52,64 Q30,66 34,92 Q20,110 38,128 Q40,152 66,150 Q82,166 100,152 Q118,166 134,150 Q160,152 162,128 Q180,110 166,92 Q170,66 148,64 Q130,46 100,64 Z', '#f2a6b4') + L(100, 64, 100, 152, '#d9809a', 3) + St('M58,84 q12,-6 20,4 t18,0 M56,112 q14,-8 24,4 t16,-4 M66,134 q10,4 22,-4', '#d9809a', 3) + St('M142,84 q-12,-6 -20,4 t-18,0 M144,112 q-14,-8 -24,4 t-16,-4 M134,134 q-10,4 -22,-4', '#d9809a', 3))
S_('blood', drop(84, 110, 50, '#c0283a') + hi(70, 104, 8, 14, .35, 20) + ''.join(E(140 + k * 12, 70 + k * 30, 14, 10, '#e2463b') + E(140 + k * 12, 70 + k * 30, 6, 4, '#c0283a') for k in range(3)))
# skin 皮肤：放大镜下的皮肤剖面：表皮、真皮和毛发
S_('skin', R(30, 70, 140, 20, '#f2c8a8') + R(30, 90, 140, 40, '#e8a890') + R(30, 130, 140, 40, '#f6e0b8') + ''.join(St(f'M{50+k*40},70 L{56+k*40},40', '#5a3a2a', 2) + E(50 + k * 40, 104, 4, 10, '#c88878') for k in range(4)) + ''.join(St(f'M{40+k*26},110 q8,6 16,0', '#c0283a', 2) for k in range(5)) + Ci(150, 50, 26, 'none', 'stroke="#5d6469" stroke-width="5"') + L(168, 68, 188, 88, '#5d6469', 7))
S_('throat', big_face(100, 64, 44, hair='#3a2a20', m='sad', brows='sad') + R(84, 102, 32, 50, SK) + Pa('M40,200 L40,170 Q40,150 70,148 L130,148 Q160,150 160,170 L160,200 Z', '#7fc4c0') + ring(100, 124, 20) + St('M126,118 l8,-4 M128,128 l10,0', HL, 3))
S_('liver', Pa('M30,100 Q30,60 90,60 Q160,58 176,80 Q180,100 150,120 Q110,150 70,140 Q30,130 30,100 Z', '#8a2a2a') + Pa('M110,62 Q150,70 150,100 Q130,130 90,140 Q120,110 110,62 Z', '#6a1a1a') + hi(64, 84, 16, 8, .2, -10) + St('M110,140 L114,170', '#5a9a3a', 6))
S_('kidney', ''.join(G(Pa('M0,-50 Q36,-50 36,-10 Q36,40 0,50 Q-24,50 -26,30 Q-10,10 -12,0 Q-10,-10 -26,-30 Q-24,-50 0,-50 Z', '#a8343a') + St('M-14,0 L-40,0 L-40,80', '#d9a33a', 4) + hi(10, -20, 6, 14, .25), f'translate({100+sx*38},{90}) scale({-sx},1)') for sx in (-1, 1)))
S_('pulse', palm_hand(70, 170, .8, 30) + R(64, 130, 40, 70, SK, 0, 'transform="rotate(30 84 165)"') + St('M100,80 L120,80 L128,60 L138,104 L146,70 L152,80 L190,80', '#e2463b', 4) + heart(120, 40, 14))
S_('vein', G(St('M0,0 L150,0', SK, 50) + ''.join(St(f'M{20+k*30},{-6+(k%2)*10} Q{36+k*30},{(k%2)*-10} {50+k*30},{4}', '#5a7ac8', 3) for k in range(4)) + St('M10,6 Q80,-4 150,8', '#5a7ac8', 4), 'translate(30,110) rotate(-10)') + ring(110, 100, 22, '#3c7fc1'))
S_('intestine', E(100, 110, 70, 64, '#f2b8a0') + ''.join(St(f'M{56+k*14},{80+(k%2)*6} q8,20 0,40 q-8,20 0,30', '#e09a80', 6) for k in range(7)) + St('M30,110 Q30,46 100,46 Q170,46 170,110 Q170,170 120,172', '#e8a080', 14))
S_('bladder', Pa('M100,40 Q150,40 156,100 Q156,150 112,160 L106,186 L94,186 L88,160 Q44,150 44,100 Q50,40 100,40 Z', '#f2c060') + hi(80, 70, 10, 18, .35, 20) + St('M60,30 Q70,50 80,46 M140,30 Q130,50 120,46', '#e0a040', 5))
# nerve 神经：黄色的神经细胞，向四周伸出很多分支
S_('nerve', Ci(80, 90, 22, '#f3d058') + Ci(80, 90, 9, '#e0a820') + ''.join(St(f'M{80+22*math.cos(a)},{90+22*math.sin(a)} q{20*math.cos(a+.4)},{20*math.sin(a+.4)} {40*math.cos(a)},{40*math.sin(a)}', '#f3d058', 5) for a in [k * math.pi / 3 + .3 for k in range(6) if k != 0]) + St('M102,90 Q140,100 180,150', '#f3d058', 6) + ''.join(E(120 + k * 18, 96 + k * 16, 7, 4, '#f6e8a0') for k in range(3)))
S_('blood-vessel', St('M20,180 Q60,120 100,100 Q140,80 180,20', '#c0283a', 14) + St('M60,190 Q90,130 120,120 Q150,110 190,60', '#5a7ac8', 12) + St('M100,100 Q90,60 70,30 M120,120 Q150,160 170,170', '#c0283a', 7) + St('M140,110 Q160,80 186,90', '#5a7ac8', 6))
S_('gland', big_face(100, 60, 40, hair='#3a2a20') + R(84, 94, 32, 60, SK) + Pa('M40,200 L40,170 Q40,150 70,150 L130,150 Q160,150 160,170 L160,200 Z', '#7fc4c0') + Pa('M100,124 Q86,110 82,120 Q78,136 92,138 Q98,134 100,128 Q102,134 108,138 Q122,136 118,120 Q114,110 100,124 Z', '#c84a6a') + ring(100, 126, 26))
# digestion 消化：从嘴到胃到肠的消化路线，食物沿箭头往下走
S_('digestion', big_face(60, 40, 26, hair='#3a2a20') + St('M60,66 L60,90 Q60,100 74,100', '#e8a080', 8) + Pa('M70,96 Q120,80 130,110 Q136,140 100,140 Q74,136 70,110 Z', '#e8a080') + ''.join(St(f'M{80+k*12},150 q6,10 0,20', '#e8a080', 6) for k in range(4)) + arrow(150, 60, 150, 170, '#5ba644', 4) + Ci(96, 116, 5, '#f08a24') + Ci(110, 120, 4, '#5ba644'))

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
