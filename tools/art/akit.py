# 进阶词插图：人体解剖小工具（骨骼 / 肌肉 / 牙齿 / 眼睛 / 器官），被高亮的部分画成红色
from kit6 import *
import math, os, sys, re

BONE = '#dccfae'; BONED = '#bfae88'; HLB = '#e2463b'
SK = P['skin']; SKD = shade(SK, -.12)
MUS = '#c8574e'; MUSD = '#a8433c'; MUSH = '#f08a24'

def bc(name, hl):  # 骨头颜色
    return HLB if hl and name in hl else BONE

def bone_seg(x1, y1, x2, y2, w, col, knob=True):
    g = St(f'M{x1},{y1} L{x2},{y2}', col, w)
    if knob:
        g += Ci(x1, y1, w * .75, col) + Ci(x2, y2, w * .75, col)
    return g

# ---------- 全身骨骼（正面，铺满画布） ----------
def skel(hl=(), x=100, s=1.0):
    hl = set(hl)
    g = ''
    # 肩胛骨（在肋骨后面）
    for sx in (-1, 1):
        g += Pa(f'M{sx*10},-150 L{sx*26},-150 L{sx*18},-124 Z', bc('scapula', hl), 'opacity=".9"')
    # 脊柱
    for k in range(5): g += R(-3.5, -172 + k * 4.4, 7, 3.6, bc('cervical', hl), 1)
    for k in range(9): g += R(-3.5, -150 + k * 4.4, 7, 3.6, bc('thoracic', hl), 1)
    for k in range(5): g += R(-4.5, -110 + k * 5, 9, 4.2, bc('lumbar', hl), 1.5)
    # 肋骨
    for k in range(7):
        yy = -150 + k * 5.6; w = 16 + min(k, 4) * 2.2
        c = bc('ribs', hl)
        g += St(f'M-2,{yy} Q{-w-6},{yy-3} {-w+1},{yy+9}', c, 2.4) + St(f'M2,{yy} Q{w+6},{yy-3} {w-1},{yy+9}', c, 2.4)
    g += R(-3, -152, 6, 32, bc('sternum', hl), 2)
    # 锁骨
    for sx in (-1, 1): g += St(f'M{sx*3},-154 Q{sx*14},-158 {sx*26},-155', bc('clavicle', hl), 3.2)
    # 骨盆 + 尾骨
    g += Pa('M-30,-86 Q-36,-104 -20,-104 Q-10,-94 -4,-84 L4,-84 Q10,-94 20,-104 Q36,-104 30,-86 Q26,-72 12,-66 L-12,-66 Q-26,-72 -30,-86 Z', bc('pelvis', hl)) + E(-14, -76, 5, 6, '#efe6d0') + E(14, -76, 5, 6, '#efe6d0')
    g += Pa('M-4,-70 L4,-70 L0,-60 Z', bc('coccyx', hl))
    # 手臂
    for sx in (-1, 1):
        g += bone_seg(sx * 26, -154, sx * 31, -118, 4.2, bc('humerus', hl))
        g += bone_seg(sx * 30, -118, sx * 34, -86, 2.4, bc('ulna', hl), False) + bone_seg(sx * 33, -117, sx * 38, -86, 2.4, bc('radius', hl), False)
        g += ''.join(St(f'M{sx*(33+k*1.6)},-84 L{sx*(32+k*2.4)},-76', bc('metacarpals', hl), 1.6) for k in range(4))
        g += ''.join(St(f'M{sx*(32+k*2.4)},-75 L{sx*(31.5+k*2.6)},-68', BONE, 1.3) for k in range(4))
    # 腿
    for sx in (-1, 1):
        g += bone_seg(sx * 20, -78, sx * 16, -38, 5.2, bc('femur', hl))
        g += E(sx * 16, -37, 3.6, 3.6, bc('patella', hl))
        g += bone_seg(sx * 15, -34, sx * 14, 0, 4.4, bc('tibia', hl), False) + bone_seg(sx * 20, -32, sx * 19, -2, 2.2, bc('fibula', hl), False)
        g += ''.join(St(f'M{sx*(12+k*2.2)},3 L{sx*(10+k*3)},10', bc('metatarsals', hl), 1.8) for k in range(5))
        g += E(sx * 15, 2, 5, 2.6, BONE)
    # 头骨
    g += E(0, -190, 13, 15, bc('skull', hl)) + R(-8, -182, 16, 9, bc('skull', hl), 3)
    if 'frontal' in hl: g += Pa('M-12,-194 Q-12,-206 0,-206 Q12,-206 12,-194 Q0,-190 -12,-194 Z', HLB)
    g += E(-5, -189, 3.6, 4, '#5d5048') + E(5, -189, 3.6, 4, '#5d5048') + Pa('M0,-185 L-2,-181 L2,-181 Z', '#5d5048')
    return G(g, f'translate({x},{184}) scale({.86*s})')

# ---------- 局部骨骼 ----------
def leg_bones(hl=()):
    hl = set(hl)
    g = bone_seg(96, 14, 92, 96, 14, bc('femur', hl)) + Ci(112, 14, 10, bc('femur', hl)) + St('M98,16 L110,14', bc('femur', hl), 8)
    g += E(100, 104, 11, 12, bc('patella', hl)) + E(100, 104, 11, 12, 'none', f'stroke="{BONED}" stroke-width="2"')
    g += bone_seg(92, 112, 90, 182, 12, bc('tibia', hl)) + bone_seg(110, 116, 108, 182, 6, bc('fibula', hl))
    return g

def knee_joint(hl=()):
    hl = set(hl)
    g = R(80, 0, 34, 70, bc('femur', hl), 6) + E(84, 82, 18, 14, bc('femur', hl)) + E(112, 82, 16, 13, bc('femur', hl)) + R(74, 64, 46, 22, bc('femur', hl), 8)
    g += R(70, 104, 56, 16, bc('tibia', hl), 6) + R(82, 112, 32, 88, bc('tibia', hl), 5)
    g += R(122, 116, 12, 84, bc('fibula', hl), 4) + Ci(128, 118, 8, bc('fibula', hl))
    if 'cartilage' in hl: g += E(98, 98, 30, 5, '#7fc4e8')
    lc = HLB if 'ligament' in hl else '#e6c8a8'
    g += St('M70,80 L72,118', lc, 7) + St('M126,80 L126,122', lc, 7) + St('M90,88 L108,110', lc, 5) + St('M108,88 L90,110', lc, 5)
    g += E(98, 90, 13, 15, bc('patella', hl), 'opacity=".8"')
    return g

def arm_bones(hl=()):
    hl = set(hl)
    g = Ci(40, 40, 16, bc('humerus', hl)) + bone_seg(46, 50, 96, 100, 13, bc('humerus', hl))
    g += bone_seg(100, 106, 154, 120, 7, bc('ulna', hl)) + bone_seg(98, 94, 154, 104, 7, bc('radius', hl))
    g += Pa('M154,96 L176,94 L178,128 L156,128 Z', bc('carpals', hl))
    g += ''.join(St(f'M178,{96+k*9} L194,{94+k*10}', bc('metacarpals', hl), 4) for k in range(4))
    return g

def hand_bones(hl=()):
    hl = set(hl)
    g = ''.join(R(66 + k * 10, 150, 9, 9, bc('carpals', hl), 2) for k in range(4)) + ''.join(R(70 + k * 10, 140, 9, 9, bc('carpals', hl), 2) for k in range(3))
    for k in range(4):
        x = 70 + k * 15
        g += bone_seg(x + 4, 132, x + 2, 92, 7, bc('metacarpals', hl))
        top = 40 + abs(k - 1.5) * 8
        g += bone_seg(x + 2, 86, x + 1, 66 - abs(k - 1.5) * 4, 6, bc('phalanges', hl)) + bone_seg(x + 1, 60 - abs(k - 1.5) * 4, x, top, 5, bc('phalanges', hl))
    g += bone_seg(62, 140, 44, 112, 7, bc('metacarpals', hl)) + bone_seg(41, 106, 30, 82, 6, bc('phalanges', hl))
    g += R(64, 162, 60, 26, bc('radius', hl), 6)
    return g

def foot_bones(hl=()):
    hl = set(hl)
    g = Pa('M60,170 Q50,140 66,130 L96,128 Q112,134 104,170 Z', bc('tarsals', hl)) + E(80, 176, 20, 12, bc('tarsals', hl))
    for k in range(5):
        x = 64 + k * 9
        g += bone_seg(x + 4, 122, x - 6 + k * 2, 70, 6, bc('metatarsals', hl))
        g += bone_seg(x - 8 + k * 2, 62, x - 10 + k * 2.4, 40 + k * 4, 5, bc('toes', hl))
    return g

def spine_side(hl=()):
    hl = set(hl)
    g = ''
    for k in range(24):
        y = 16 + k * 6.6
        x = 100 + 14 * math.sin((k - 2) / 5.2) - 4
        part = 'cervical' if k < 7 else 'thoracic' if k < 19 else 'lumbar'
        w = 10 + k * .5
        g += R(x - w / 2, y, w, 5.4, bc(part, hl), 2) + R(x + w / 2 - 1, y + 1.4, 8, 2.6, bc(part, hl), 1)
    g += Pa('M92,176 L112,176 L104,192 Z', bc('sacrum', hl)) + Pa('M101,192 L107,192 L104,198 Z', bc('coccyx', hl))
    return g

def chest_bones(hl=()):
    hl = set(hl)
    g = ''
    for sx in (-1, 1):
        g += Pa(f'M{100+sx*36},62 L{100+sx*70},60 L{100+sx*56},118 Z', bc('scapula', hl), 'opacity=".95"')
    for k in range(8):
        yy = 66 + k * 14; w = 36 + min(k, 4) * 8
        c = bc('ribs', hl)
        g += St(f'M96,{yy} Q{100-w-14},{yy-8} {100-w+2},{yy+26}', c, 6) + St(f'M104,{yy} Q{100+w+14},{yy-8} {100+w-2},{yy+26}', c, 6)
    g += R(92, 62, 16, 84, bc('sternum', hl), 6)
    for sx in (-1, 1): g += St(f'M{100+sx*8},56 Q{100+sx*40},46 {100+sx*72},54', bc('clavicle', hl), 9)
    if 'intercostal' in hl:
        for k in range(6):
            yy = 74 + k * 14; w = 40 + min(k, 4) * 8
            g += St(f'M{100-w+6},{yy+8} Q{100-w/2},{yy-2} 92,{yy+4}', HLB, 5, 'opacity=".85"') + St(f'M{100+w-6},{yy+8} Q{100+w/2},{yy-2} 108,{yy+4}', HLB, 5, 'opacity=".85"')
    return g

def skull_big(hl=()):
    hl = set(hl)
    g = E(100, 86, 62, 66, bc('skull', hl)) + R(66, 120, 68, 48, bc('jaw', hl), 14)
    if 'frontal' in hl: g += Pa('M44,82 Q44,22 100,20 Q156,22 156,82 Q100,66 44,82 Z', HLB)
    g += E(76, 100, 16, 18, '#5d5048') + E(124, 100, 16, 18, '#5d5048') + Pa('M100,116 L92,134 L108,134 Z', '#5d5048')
    g += ''.join(R(74 + k * 9, 146, 7, 14, '#ffffff', 2) for k in range(6))
    return g

# ---------- 肌肉人（正面 / 背面） ----------
def muscle_man(hl=(), back=False):
    hl = set(hl)
    def mc(n): return MUSH if n in hl else MUS
    g = ''
    # 腿、手臂底色
    for sx in (-1, 1):
        g += St(f'M{100+sx*14},112 L{100+sx*16},150 L{100+sx*15},186', MUSD, 20)
        g += St(f'M{100+sx*30},50 L{100+sx*40},86 L{100+sx*44},116', MUSD, 13) + Ci(100 + sx * 45, 120, 6, SK)
    g += Pa('M72,46 Q100,38 128,46 L124,112 L76,112 Z', MUSD)
    # 头
    g += Ci(100, 22, 15, SK) + R(94, 34, 12, 10, SKD, 3)
    if not back:
        g += Ci(95, 20, 1.6, '#2b211b') + Ci(105, 20, 1.6, '#2b211b')
        for sx in (-1, 1):
            g += Pa(f'M100,50 Q{100+sx*24},44 {100+sx*28},54 Q{100+sx*26},70 100,70 Z', mc('pectoral'))
            g += E(100 + sx * 32, 52, 8, 10, mc('deltoid'))
            g += E(100 + sx * 37, 72, 6, 12, mc('biceps'), f'transform="rotate({sx*-14} {100+sx*37} 72)"')
            g += Pa(f'M{100+sx*24},72 Q{100+sx*28},92 {100+sx*24},110 L{100+sx*14},110 L{100+sx*14},74 Z', mc('obliques'))
            g += E(100 + sx * 15, 136, 8, 20, mc('quadriceps'))
        for r in range(3):
            for sx in (-1, 1): g += R(100 + (sx - 1) * 6 + 1, 74 + r * 12, 10, 10, mc('abdominals'), 3)
    else:
        g += Ci(100, 22, 15, '#3a2a20') + E(100, 30, 13, 8, '#3a2a20')
        g += Pa('M100,40 L76,52 L86,74 L100,80 L114,74 L124,52 Z', mc('trapezius'))
        for sx in (-1, 1):
            g += E(100 + sx * 32, 52, 8, 10, mc('deltoid'))
            g += Pa(f'M{100+sx*6},78 Q{100+sx*26},66 {100+sx*26},90 Q{100+sx*20},106 {100+sx*6},106 Z', mc('latissimus-dorsi'))
            g += E(100 + sx * 12, 118, 12, 10, mc('gluteus'))
            g += E(100 + sx * 15, 144, 7, 18, mc('hamstrings'))
            g += E(100 + sx * 15, 170, 6, 10, MUS)
            g += E(100 + sx * 37, 74, 6, 11, MUS, f'transform="rotate({sx*-14} {100+sx*37} 74)"')
    return g

# ---------- 牙齿 ----------
def tooth_section(hl=()):
    hl = set(hl)
    out_ = 'M60,30 Q100,14 140,30 Q150,70 136,100 Q130,140 124,184 Q114,190 108,160 L104,120 L96,120 L92,160 Q86,190 76,184 Q70,140 64,100 Q50,70 60,30 Z'
    g = Pa(out_, '#f6e8c8' if 'dentin' not in hl else HLB)
    g += Pa('M60,30 Q100,14 140,30 Q150,70 138,92 L62,92 Q50,70 60,30 Z', HLB if 'enamel' in hl else '#ffffff')
    g += Pa('M66,36 Q100,24 134,36 Q140,64 132,84 L68,84 Q60,64 66,36 Z', '#f6e8c8' if 'dentin' not in hl else HLB)
    g += Pa('M86,52 Q100,44 114,52 Q116,80 110,110 L108,170 L104,170 L102,124 L98,124 L96,170 L92,170 L90,110 Q84,80 86,52 Z', HLB if 'pulp' in hl else '#ef8fa4')
    g += R(40, 96, 120, 6, '#f2a6a6', 3, 'opacity=".5"')
    return g

def tooth_shape(kind, col='#ffffff'):
    if kind == 'incisor': return Pa('M-8,-20 L8,-20 L7,0 Q5,22 0,26 Q-5,22 -7,0 Z', col)
    if kind == 'canine': return Pa('M-8,-14 L0,-24 L8,-14 L7,2 Q4,26 0,30 Q-4,26 -7,2 Z', col)
    if kind == 'bicuspid': return Pa('M-10,-18 L-4,-22 L0,-16 L4,-22 L10,-18 L9,0 Q6,22 0,24 Q-6,22 -9,0 Z', col)
    return Pa('M-14,-16 L-8,-22 L-3,-16 L3,-22 L8,-16 L14,-22 L14,0 Q12,20 6,22 L4,8 L-4,8 L-6,22 Q-12,20 -14,0 Z', col)

def teeth_row(hl=None):
    """一排牙（门牙→臼齿），被选中的类别画成黄色"""
    kinds = ['molar', 'molar', 'bicuspid', 'bicuspid', 'canine', 'incisor', 'incisor', 'incisor', 'incisor', 'canine', 'bicuspid', 'bicuspid', 'molar', 'molar']
    xs = [18 + i * 12.6 for i in range(len(kinds))]
    g = Pa('M6,100 Q100,60 194,100 L194,124 Q100,90 6,124 Z', '#e88a90')
    for x, k in zip(xs, kinds):
        c = '#f3c234' if hl and (k == hl or (hl == 'molars' and k == 'molar')) else '#ffffff'
        g += G(tooth_shape(k, c), f'translate({x},{112 - 18 * math.cos((x - 100) / 70)}) scale(.62)')
    return g

def teeth_arch(hl=None, n=16):
    """牙弓俯视图：成人 32 颗牙（上下各一排）"""
    g = Pa('M30,180 Q20,40 100,30 Q180,40 170,180 L140,180 Q148,70 100,62 Q52,70 60,180 Z', '#e88a90')
    for i in range(n):
        t = math.pi * (i + .5) / n
        x = 100 - 56 * math.cos(t); y = 160 - 112 * math.sin(t)
        kind = 'incisor' if 6 <= i <= 9 else 'canine' if i in (5, 10) else 'bicuspid' if i in (3, 4, 11, 12) else 'molar'
        r = {'incisor': 7, 'canine': 8, 'bicuspid': 9, 'molar': 11}[kind]
        c = '#f3c234' if hl == kind else '#ffffff'
        g += Ci(x, y, r, c) + Ci(x - r * .3, y - r * .3, r * .3, '#ffffff', 'opacity=".6"')
    return g

# ---------- 眼睛特写 ----------
def eye_close(iris='#6a8a5a', hl=None, lashes=False, closed=False, tear=False):
    g = E(100, 100, 82, 46, SK) + Pa('M24,100 Q100,30 176,100 Q100,160 24,100 Z', '#ffffff' if not closed else SK)
    if not closed:
        g += Ci(100, 98, 30, iris) + Ci(100, 98, 30, 'none', f'stroke="{shade(iris,-.3)}" stroke-width="3"')
        g += ''.join(L(100 + 14 * math.cos(a), 98 + 14 * math.sin(a), 100 + 28 * math.cos(a), 98 + 28 * math.sin(a), shade(iris, .25), 1.5) for a in [k * math.pi / 9 for k in range(18)])
        g += Ci(100, 98, 13, '#14100c') + Ci(108, 90, 5, '#ffffff', 'opacity=".9"')
        g += Pa('M24,100 Q100,30 176,100 Q100,46 24,100 Z', SKD)
    else:
        g += St('M26,100 Q100,140 174,100', '#3a2a20', 5) + Pa('M24,100 Q100,30 176,100 Q100,140 24,100 Z', SKD, 'opacity=".5"')
    g += St('M30,62 Q100,22 170,60', '#3a2a20', 9)
    if lashes or closed:
        base = [(100 + 72 * math.cos(math.pi * (.15 + .7 * k / 10)), 100 - 44 * math.sin(math.pi * (.15 + .7 * k / 10))) for k in range(11)] if not closed else [(30 + k * 14, 100 + 40 * math.sin(math.pi * k / 10) * .55) for k in range(11)]
        for x, y in base:
            dx = (x - 100) / 6
            g += St(f'M{x},{y} q{dx*.4},{-8 if not closed else 8} {dx},{-14 if not closed else 16}', '#2b211b', 3)
    if tear:
        g += drop(30, 128, 12, '#7fc4e8')
    return g

def load(name):
    """取用某个旧插图脚本里定义的函数（不执行它的输出部分）"""
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.py'), encoding='utf-8').read().split('\nout = sys.argv[1]')[0].split('\nsave(A)')[0].split('\ndump()')[0]
    ns = {'__name__': 'lib', '__file__': os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.py')}
    cwd = os.getcwd(); os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try: exec(src, ns)
    finally: os.chdir(cwd)
    return ns

def save(A):
    out = sys.argv[1] if len(sys.argv) > 1 else 'out'
    os.makedirs(out, exist_ok=True)
    for k, v in A.items():
        open(os.path.join(out, k + '.svg'), 'w', encoding='utf-8').write(v)
    print(len(A), 'drawn')

def bare_torso(x=100, y=0, s=1.0, navel=True, nipples=True):
    """光膀子的上身（男性，无头）：用于肚脐、腹部等"""
    g = Pa('M40,40 Q100,24 160,40 L170,60 Q162,120 150,190 L50,190 Q38,120 30,60 Z', SK)
    g += St('M60,60 Q100,74 140,60', SKD, 2) + St('M100,100 L100,150', SKD, 1.5, 'opacity=".6"')
    if nipples: g += Ci(74, 86, 3.5, '#c98d70') + Ci(126, 86, 3.5, '#c98d70')
    if navel: g += E(100, 150, 4, 6, '#c98d70')
    return G(g, f'translate({x - 100 * s},{y}) scale({s})')

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
def reuse(id_, x=100, y=100, s=1.0, shadow=False, bg=False):
    """把基础词已经画好的插图（art/out/<id>.svg）缩放后放进新图里"""
    t = open(os.path.join(_OUT, id_ + '.svg'), encoding='utf-8').read()
    t = re.sub(r'^<svg[^>]*>', '', t).replace('</svg>', '')
    if not bg: t = re.sub(r'<rect x="0" y="[\d.]+" width="200" height="[\d.]+"[^>]*/>', '', t)
    if not shadow: t = t.replace('<ellipse cx="100" cy="186" rx="64" ry="8" fill="#000" opacity=".12"/>', '', 1)
    return G(t, f'translate({x - 100 * s},{y - 100 * s}) scale({s})')

def rc(id_, mp=None, x=100, y=100, s=1.0, bg=False):
    """复用基础插图并换颜色：mp = {'旧色': '新色'}"""
    g = reuse(id_, x, y, s, bg=bg)
    for a, b in (mp or {}).items(): g = g.replace(a, b)
    return g

def braid(x1, y1, x2, y2, col, w=12):
    n = 6; g = ''
    for k in range(n):
        t = (k + .5) / n
        x = x1 + (x2 - x1) * t; y = y1 + (y2 - y1) * t
        g += E(x, y, w * .6, (abs(y2 - y1) + 1) / n * .62, col, f'transform="rotate({(-1)**k*20} {x} {y})"')
    return g

def hairdo(style='short', col='#3a2a20', cx=100, cy=104, r=56, m='smile', eyes='dot', skin=None, brows=None, blush=None):
    """各种发型的大头像"""
    back = ''; front = ''; bf_style = 'none'
    if style in ('short', 'long', 'bun'):
        bf_style = style
    elif style == 'bob':
        back = Pa(f'M{cx-r*1.08},{cy+r*.55} Q{cx-r*1.25},{cy-r*1.2} {cx},{cy-r*1.14} Q{cx+r*1.25},{cy-r*1.2} {cx+r*1.08},{cy+r*.55} Z', col)
        front = Pa(f'M{cx-r*.95},{cy-r*.05} Q{cx-r},{cy-r*1.15} {cx},{cy-r*1.08} Q{cx+r},{cy-r*1.15} {cx+r*.95},{cy-r*.05} L{cx+r*.9},{cy-r*.5} L{cx-r*.9},{cy-r*.5} Z', col)
    elif style == 'shoulder':
        back = Pa(f'M{cx-r*1.08},{cy+r*1.05} Q{cx-r*1.3},{cy-r*1.2} {cx},{cy-r*1.14} Q{cx+r*1.3},{cy-r*1.2} {cx+r*1.08},{cy+r*1.05} Z', col); bf_style = 'short'
    elif style == 'wavy':
        back = Pa(f'M{cx-r*1.05},{cy+r*1.2} q{-r*.2},{-r*.3} 0,{-r*.6} q{-r*.25},{-r*.3} {-r*.05},{-r*.6} Q{cx-r*1.2},{cy-r*1.2} {cx},{cy-r*1.14} Q{cx+r*1.2},{cy-r*1.2} {cx+r*1.1},{cy-r*.0} q{r*.2},{r*.3} {-r*.05},{r*.6} q{r*.25},{r*.3} 0,{r*.6} Z', col); bf_style = 'short'
    elif style == 'curly':
        front = ''.join(Ci(cx + r * .95 * math.cos(a), cy - r * .2 + r * .95 * math.sin(a) * .9, r * .28, col) for a in [math.pi + k * math.pi / 9 for k in range(10)])
    elif style == 'afro':
        back = Ci(cx, cy - r * .35, r * 1.45, col) + ''.join(Ci(cx + r * 1.4 * math.cos(a), cy - r * .35 + r * 1.4 * math.sin(a), r * .2, col) for a in [k * math.pi / 8 for k in range(16)])
    elif style == 'frizzy':
        back = Pa(' '.join([f'M{cx-r*1.3},{cy+r*.6}'] + [f'L{cx + r*(1.35 + .2*(k%2))*math.cos(math.pi*(1 - k/18) + math.pi)} ,{cy - r*.2 + r*(1.35 + .2*(k%2))*math.sin(math.pi*(1 - k/18) + math.pi)}' for k in range(19)]) + f' L{cx+r*1.3},{cy+r*.6} Z', col)
    elif style == 'crew':
        front = Pa(f'M{cx-r*.9},{cy-r*.35} Q{cx-r*.92},{cy-r*1.05} {cx},{cy-r*1.04} Q{cx+r*.92},{cy-r*1.05} {cx+r*.9},{cy-r*.35} Q{cx},{cy-r*.62} {cx-r*.9},{cy-r*.35} Z', col)
    elif style == 'shaved':
        front = Pa(f'M{cx-r*.9},{cy-r*.35} Q{cx-r*.92},{cy-r*1.05} {cx},{cy-r*1.04} Q{cx+r*.92},{cy-r*1.05} {cx+r*.9},{cy-r*.35} Q{cx},{cy-r*.62} {cx-r*.9},{cy-r*.35} Z', col, 'opacity=".25"')
    elif style in ('braids', 'pigtails'):
        bf_style = 'short'
        if style == 'pigtails':
            back = Ci(cx - r * 1.05, cy - r * .5, r * .3, col) + Ci(cx + r * 1.05, cy - r * .5, r * .3, col) + braid(cx - r * 1.1, cy - r * .4, cx - r * 1.2, cy + r * .9, col, r * .3) + braid(cx + r * 1.1, cy - r * .4, cx + r * 1.2, cy + r * .9, col, r * .3)
        else:
            back = ''.join(braid(cx + dx * r, cy - r * .2, cx + dx * r * 1.05, cy + r * 1.3, col, r * .16) for dx in (-1.0, -.85, .85, 1.0))
    elif style == 'plait':
        bf_style = 'short'; back = braid(cx + r * .9, cy - r * .2, cx + r * 1.2, cy + r * 1.4, col, r * .32)
    elif style == 'cornrows':
        front = Pa(f'M{cx-r*.9},{cy-r*.3} Q{cx-r*.92},{cy-r*1.05} {cx},{cy-r*1.04} Q{cx+r*.92},{cy-r*1.05} {cx+r*.9},{cy-r*.3} Q{cx},{cy-r*.55} {cx-r*.9},{cy-r*.3} Z', col) + ''.join(St(f'M{cx+k*r*.22},{cy-r*.45} Q{cx+k*r*.24},{cy-r*.8} {cx+k*r*.18},{cy-r*1.0}', shade(col, .3), 2.5, 'stroke-dasharray="4 3"') for k in range(-3, 4))
    g = back + big_face(cx, cy, r, hair=col, style=bf_style, eyes=eyes, m=m, skin=skin, brows=brows, blush=blush) + front
    return g

def side_part(cx=100, cy=104, r=56, center=False, col='#3a2a20'):
    x = cx if center else cx - r * .35
    return St(f'M{x},{cy-r*1.08} L{x+(0 if center else r*.05)},{cy-r*.55}', shade(SK, .2), 3)

def use(ns, g):
    """把旧脚本里的画图函数放进当前脚本的全局变量（不覆盖已有的）"""
    for k, v in ns.items():
        if callable(v) and not k.startswith('_') and k not in ('S_', 'save', 'load') and k not in g:
            g[k] = v
