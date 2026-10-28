from flat import *
from fig import *
import os, sys, random

A = {}

def shrimp(x, y, s, rot=0, col='#f08a6a'):
    g = ''
    for i in range(6):
        a = math.radians(-90 + i * 34)
        rr = 26 - i * 2.4
        g += Ci(rr * math.cos(a), rr * math.sin(a), 11 - i * 1.1, col if i % 2 == 0 else shade(col, -.08))
    g += Pa('M-8,30 L-22,40 L-10,36 L-12,46 L0,34 Z', shade(col, -.15))
    g += Ci(2, -30, 2.5, '#2f3437') + St('M4,-34 Q30,-60 60,-50 M2,-34 Q24,-70 50,-70', shade(col, -.2), 1.6)
    g += ''.join(L(-6 + k * 4, -10 + k * 5, -14 + k * 4, -4 + k * 5, shade(col, -.2), 1.5) for k in range(4))
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def crab(x, y, s, col='#d9453a'):
    g = ''
    for sx in (-1, 1):
        for k in range(3):
            g += St(f'M{sx*24},{4+k*6} l{sx*18},{6+k*4} l{sx*6},{12}', shade(col, -.15), 4)
        g += St(f'M{sx*20},-8 Q{sx*34},-26 {sx*30},-36', col, 6)
        g += Pa(f'M{sx*30},-36 q{sx*-12},-10 {sx*-4},-20 q{sx*10},-4 {sx*14},8 q{sx*-2},-10 {sx*6},-12 q{sx*6},10 {sx*-2},20 Z', col)
    g += E(0, 6, 34, 22, col) + E(0, 2, 26, 14, shade(col, .15)) + Ci(-8, -16, 4, '#ffffff') + Ci(8, -16, 4, '#ffffff') + Ci(-8, -16, 2, '#2f3437') + Ci(8, -16, 2, '#2f3437')
    return G(g, f'translate({x},{y}) scale({s})')

def shell_fan(x, y, s, col='#f0a07a', rot=0):
    g = Pa('M0,30 L-40,-6 Q-30,-40 0,-44 Q30,-40 40,-6 Z', col)
    g += ''.join(St(f'M0,30 L{-36+k*9},{-8-abs(k-4)*-0-26+abs(k-4)*4}', shade(col, -.15), 2) for k in range(9))
    g += R(-14, 24, 28, 12, shade(col, -.1), 4)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def ice(x0, y0, w, n=10, seed=1):
    random.seed(seed)
    return ''.join(R(x0 + random.uniform(0, w), y0 + random.uniform(-6, 10), 14, 12, '#e8f6fc', 3, f'transform="rotate({random.uniform(-30,30):.0f} {x0} {y0})" stroke="#bfe0ef" stroke-width="1"') for _ in range(n))

# fish 鱼：一条完整的鱼
A['fish'] = svg(fish_shape(112, 104, 128, '#7ea2bc', '#e6ecef'))

# seafood 海鲜：冰上摆着虾、螃蟹、扇贝、生蚝
g = E(100, 150, 90, 28, '#a7c8d8') + ice(16, 150, 160, 18)
g += crab(62, 110, .8) + shrimp(134, 100, .7, 30) + shell_fan(150, 144, .5, '#f0a07a', 10) + E(64, 156, 24, 12, '#8a9a94') + E(64, 154, 16, 7, '#e6e1d0')
A['seafood'] = svg(g)

# shrimp 虾：两只粉红的大虾
A['shrimp'] = svg(shrimp(80, 110, 1.2, 0) + shrimp(138, 120, .85, 40, '#f29a7a'))

# crab 螃蟹：一只红色螃蟹
A['crab'] = svg(crab(100, 112, 1.5))

# fresh 新鲜的：冰上的鱼，眼睛亮、鱼身带水珠，旁边绿色对勾
g = E(100, 146, 84, 24, '#a7c8d8') + ice(20, 144, 150, 16, 3) + fish_shape(110, 112, 124, '#6f9cbc', '#eef4f6')
g += drop(70, 84, 5, '#ffffff') + drop(116, 82, 4, '#ffffff') + drop(90, 128, 4, '#ffffff') + star(150, 70, 6, '#ffffff')
g += Ci(166, 40, 16, '#5ba644') + St('M158,40 l6,6 l10,-12', '#ffffff', 4)
A['fresh'] = svg(g)

# salmon 三文鱼：橙色三文鱼排，白色纹路
g = board(100, 140, 170, 60)
g += Pa('M30,120 Q30,80 80,78 L160,84 Q176,90 172,112 L166,140 Q100,150 40,140 Q30,134 30,120 Z', '#f58a5a')
g += ''.join(St(f'M{50+i*20},84 Q{40+i*20},110 {54+i*20},142', '#fbd0b8', 3) for i in range(6))
g += Pa('M30,120 Q30,134 40,140 Q100,150 166,140 L168,132 Q100,140 40,132 Z', '#9aa4aa')
A['salmon'] = svg(g)

# tuna 金枪鱼：蓝背银肚的大金枪鱼
g = fish_shape(112, 104, 136, '#2f5a8a', '#d9e2e8')
g += ''.join(Pa(f'M{62+i*8},{88} l3,-5 l3,5 Z', '#f3c234') for i in range(4)) + ''.join(Pa(f'M{62+i*8},{118} l3,5 l3,-5 Z', '#f3c234') for i in range(4))
A['tuna'] = svg(g)

# squid 鱿鱼：长身体、三角鳍、一把触须
g = G(Pa('M0,-70 Q22,-40 20,10 L-20,10 Q-22,-40 0,-70 Z', '#f2c0b0') + Pa('M0,-70 L-30,-50 L-14,-36 Z M0,-70 L30,-50 L14,-36 Z', '#e9a898') +
      ''.join(Ci(-10 + (k % 3) * 10, -40 + k * 7, 2.5, '#d98a7a') for k in range(7)) + Ci(-8, 4, 4, '#2f3437') + Ci(8, 4, 4, '#2f3437') +
      ''.join(St(f'M{-16+k*6.4},10 q{(k-2.5)*4},30 {(k-2.5)*8},{50+(k%2)*10}', '#f2c0b0', 5) for k in range(6)), 'translate(100,94) rotate(-20)')
A['squid'] = svg(g)

# lobster 龙虾：红色大龙虾，两只大钳子
g = ''
for sx in (-1, 1):
    g += St(f'M{100+sx*12},70 Q{100+sx*30},50 {100+sx*36},34', '#c0302a', 7)
    g += Pa(f'M{100+sx*36},34 q{sx*-16},-8 {sx*-6},-24 q{sx*14},-4 {sx*18},14 q{sx*2},-12 {sx*10},-12 q{sx*6},14 {sx*-4},22 Z', '#d9453a')
    g += ''.join(St(f'M{100+sx*14},{90+k*10} l{sx*20},{6}', '#a8302a', 3) for k in range(3))
    g += St(f'M{100+sx*6},60 Q{100+sx*40},20 {100+sx*70},16', '#c0302a', 2)
g += E(100, 80, 16, 24, '#d9453a') + Ci(94, 62, 3, '#2f3437') + Ci(106, 62, 3, '#2f3437')
g += ''.join(E(100, 108 + k * 13, 15 - k, 8, '#d9453a' if k % 2 else '#c0302a') for k in range(5)) + Pa('M100,172 L84,186 L116,186 Z', '#c0302a')
A['lobster'] = svg(g)

# oyster 生蚝：张开的生蚝壳里有乳白色蚝肉，配柠檬
g = Pa('M30,120 Q24,80 70,70 Q130,58 170,90 Q186,120 150,150 Q100,174 50,154 Q30,142 30,120 Z', '#8a9a94')
g += Pa('M44,118 Q42,90 76,84 Q126,74 156,98 Q166,120 140,138 Q100,156 60,144 Q44,136 44,118 Z', '#ece6d6')
g += Pa('M66,116 Q70,96 100,96 Q134,98 138,116 Q130,134 100,136 Q70,134 66,116 Z', '#d9cfb8') + E(100, 112, 24, 10, '#c9bfa6') + hi(86, 104, 12, 4, .6)
g += G(Pa('M0,0 L30,0 A30,30 0 0,1 0,30 Z', '#f3d034') + Pa('M3,3 L26,3 A24,24 0 0,1 3,26 Z', '#fbe98a'), 'translate(144,140) rotate(20)')
A['oyster'] = svg(g)

# cod 鳕鱼：带斑点、下巴有须的鳕鱼
g = fish_shape(112, 104, 134, '#9a8a64', '#efe9d8', spots='#6a5a3a') + St('M164,110 q4,10 -2,16', '#6a5a3a', 2)
A['cod'] = svg(g)

# mussel 青口贝：几只黑蓝色贝壳，一只张开露出橙色贝肉
def mussel(x, y, rot, open_=False):
    g = Pa('M0,-30 Q18,-26 20,0 Q18,30 0,34 Q-12,20 -14,0 Q-12,-24 0,-30 Z', '#2f3a52') + Pa('M0,-30 Q18,-26 20,0 Q18,30 0,34 Q10,0 0,-30 Z', '#4a5878')
    if open_: g += E(-2, 2, 9, 22, '#f08a4a') + E(-2, 2, 5, 14, '#f6b07a')
    return G(g, f'translate({x},{y}) rotate({rot}) scale(1.3)')
g = mussel(60, 110, -30) + mussel(100, 120, 10, True) + mussel(146, 104, 40)
A['mussel'] = svg(g)

# scallop 扇贝：扇形贝壳，里面白色贝柱
g = shell_fan(100, 100, 1.9, '#f0a07a')
g += Ci(100, 98, 22, '#f8f2e4') + Ci(100, 96, 14, '#fffaf0') + Pa('M80,110 q20,16 40,0', 'none', 'stroke="#f2b07a" stroke-width="5"')
A['scallop'] = svg(g)

# seaweed 海带/紫菜：一卷卷墨绿色海带和一张紫菜片
g = R(98, 40, 80, 100, '#1f3a2a', 4) + ''.join(L(102, 50 + i * 12, 174, 50 + i * 12, '#2f5a3a', 1.5) for i in range(8))
for i, x in enumerate((36, 62, 88)):
    g += St(f'M{x},180 Q{x-16},140 {x+6},110 Q{x+24},80 {x+4},40', '#3c6a3a', 14) + St(f'M{x},180 Q{x-16},140 {x+6},110 Q{x+24},80 {x+4},40', '#5a8a4a', 4)
A['seaweed'] = svg(g)

# fillet 鱼片：去骨的白色鱼片放在砧板上
g = board(100, 140, 170, 60)
g += Pa('M24,124 Q40,90 100,86 Q150,84 176,104 Q170,124 140,132 Q90,142 24,124 Z', '#f6efe6')
g += ''.join(St(f'M{50+i*22},{92} Q{44+i*22},112 {54+i*22},130', '#e6d8c8', 2.5) for i in range(5)) + Pa('M24,124 Q90,142 140,132 Q170,124 176,104 L178,110 Q172,132 140,138 Q90,148 24,128 Z', '#c9c2b8')
g += Ci(160, 40, 16, '#5ba644') + St('M152,40 l6,6 l10,-12', '#ffffff', 4)
A['fillet'] = svg(g)

# fish-bone 鱼刺：一副完整的鱼骨头
g = ''
g += Pa('M150,104 Q170,80 186,96 Q190,108 186,116 Q170,128 150,104 Z', '#e6ecef') + Ci(172, 100, 4, '#5d6469')
g += L(30, 104, 152, 104, '#e6ecef', 6)
for i in range(8):
    x = 44 + i * 14
    g += St(f'M{x},104 Q{x+6},84 {x+2},{70+abs(i-3.5)*4}', '#e6ecef', 3) + St(f'M{x},104 Q{x+6},124 {x+2},{138-abs(i-3.5)*4}', '#e6ecef', 3)
g += Pa('M32,104 L10,80 Q18,104 10,128 Z', '#e6ecef')
g = G(g, 'translate(0,0)') + E(100, 160, 70, 6, '#000', 'opacity=".0"')
A['fish-bone'] = svg(g.replace('#e6ecef', '#c9d2d8'))

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
