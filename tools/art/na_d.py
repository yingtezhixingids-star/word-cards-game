from kit6 import *

def pine_tree(x, base, s=1, col='#2f6a4a'):
    return G(R(-6, -20, 12, 22, '#6a4a2a') + Pa('M0,-130 L30,-80 L16,-80 L40,-46 L22,-46 L50,-16 L-50,-16 L-22,-46 L-40,-46 L-16,-80 L-30,-80 Z', col), f'translate({x},{base}) scale({s})')
def willow(x, base, s=1):
    return G(R(-8, -90, 16, 90, '#6a4a2a', 4) + Ci(0, -100, 40, '#8ac060') + ''.join(St(f'M{-40+j*10},{-110+abs(j-4)*4} Q{-44+j*10},{-60} {-42+j*10},{-20}', '#7ab050', 4) for j in range(9)), f'translate({x},{base}) scale({s})')
def oak(x, base, s=1):
    return G(R(-12, -70, 24, 70, '#6a4a2a', 4) + ''.join(Ci(dx, dy, r_, c) for dx, dy, r_, c in [(-40, -90, 30, '#3c7a2c'), (40, -90, 30, '#3c7a2c'), (0, -120, 40, '#4a8a3a'), (-24, -70, 24, '#4a8a3a'), (24, -70, 24, '#5a9a3a')]) + ''.join(E(dx, dy, 4, 5, '#a8703e') for dx, dy in [(-30, -80), (20, -110), (34, -76)]), f'translate({x},{base}) scale({s})')
def maple_tree(x, base, s=1):
    return G(R(-10, -70, 20, 70, '#6a4a2a', 4) + Ci(0, -110, 50, '#d9532a') + Ci(-36, -84, 30, '#e07a2a') + Ci(36, -84, 30, '#c8402a') + ''.join(leaf_shape(dx, dy, .25, '#f3a234', r_, 'maple') for dx, dy, r_ in [(-20, -120, 10), (24, -100, -20), (0, -80, 30)]), f'translate({x},{base}) scale({s})')
def palm(x, base, s=1):
    return G(St('M0,0 Q10,-60 -6,-130', '#a8703e', 14) + ''.join(L(-6 + (j * 2), -20 - j * 20, 8 + j, -22 - j * 20, '#8a5a35', 2) for j in range(5)) + ''.join(St(f'M-6,-130 Q{60*math.cos(a)},{-130+30*math.sin(a)-30} {80*math.cos(a)},{-130+60*math.sin(a)+10}', '#3c8a3a', 10) for a in [math.radians(d) for d in (-170, -130, -90, -50, -10, 30, 150)]) + Ci(-2, -124, 6, '#8a5a35') + Ci(8, -122, 6, '#8a5a35'), f'translate({x},{base}) scale({s})')
def ginkgo_tree(x, base, s=1):
    return G(R(-8, -80, 16, 80, '#6a4a2a', 4) + Pa('M0,-170 Q50,-120 50,-80 Q0,-60 -50,-80 Q-50,-120 0,-170 Z', '#f3c234'), f'translate({x},{base}) scale({s})')
def xmas_tree(x, base, s=1):
    return G(R(-8, -20, 16, 22, '#6a4a2a') + Pa('M0,-150 L40,-96 L24,-96 L54,-56 L32,-56 L64,-16 L-64,-16 L-32,-56 L-54,-56 L-24,-96 L-40,-96 Z', '#2f8a4a') + star(0, -150, 12, '#f3c234') + ''.join(Ci(dx, dy, 5, c) for dx, dy, c in [(-14, -100, '#e2463b'), (16, -80, '#3c7fc1'), (-26, -50, '#f3c234'), (24, -40, '#e2463b'), (0, -60, '#ef8fa4'), (-40, -24, '#3c7fc1'), (40, -24, '#f3c234')]) + R(-12, 0, 24, 16, '#e2463b', 2) + R(-2, 0, 4, 16, '#f3c234'), f'translate({x},{base}) scale({s})')
def birch(x, base, s=1):
    return G(R(-8, -140, 16, 140, '#f6f4ee') + ''.join(R(-8, -130 + j * 18, 6 + (j % 2) * 6, 3, '#2f3437') for j in range(7)) + ''.join(Ci(dx, dy, 14, '#9ac060') for dx, dy in [(-20, -130), (16, -140), (0, -160), (24, -116), (-24, -104)]), f'translate({x},{base}) scale({s})')
def poplar(x, base, s=1):
    return G(R(-6, -40, 12, 40, '#6a4a2a') + E(0, -110, 26, 80, '#5a9a3a') + St('M0,-40 L0,-160', '#4a8a2a', 2), f'translate({x},{base}) scale({s})')
def cypress(x, base, s=1):
    return G(R(-5, -20, 10, 20, '#6a4a2a') + Pa('M0,-170 Q30,-110 22,-40 Q0,-16 -22,-40 Q-30,-110 0,-170 Z', '#2f5a3a'), f'translate({x},{base}) scale({s})')
def cedar(x, base, s=1):
    return G(R(-8, -110, 16, 110, '#6a4a2a') + ''.join(E(0, -40 - j * 26, 70 - j * 14, 12, '#3a6a4a') for j in range(5)), f'translate({x},{base}) scale({s})')
def elm(x, base, s=1):
    return G(St('M0,0 L0,-60 M0,-60 L-30,-110 M0,-60 L30,-110 M0,-70 L0,-120', '#6a4a2a', 10) + Pa('M-70,-90 Q-70,-170 0,-170 Q70,-170 70,-90 Q40,-70 0,-80 Q-40,-70 -70,-90 Z', '#5a9a3a'), f'translate({x},{base}) scale({s})')
def pinecone(x, y, s=1):
    return G(''.join(Pa(f'M{-26+j*0},{-30+r_*14} ' + ' '.join(f'l6,10 l6,-10' for _ in range(int(4 - abs(r_ - 3) * .7))) + ' Z', '#a8703e') for r_ in range(0)) + E(0, 0, 30, 46, '#8a5a35') + ''.join(Pa(f'M{dx-8},{dy} L{dx},{dy+10} L{dx+8},{dy} L{dx},{dy-4} Z', '#c8903a') for dx, dy in [(x_, y_) for y_ in range(-36, 40, 12) for x_ in range(-20 + (abs(y_) // 12) * 2, 22 - (abs(y_) // 12) * 2, 12)]) + R(-4, -56, 8, 12, '#6a4a2a', 3), f'translate({x},{y}) scale({s})')
def acorn(x, y, s=1):
    return G(E(0, 14, 24, 30, '#c8903a') + Pa('M-30,0 Q-30,-26 0,-26 Q30,-26 30,0 Z', '#8a5a35') + ''.join(L(-24 + j * 8, -20, -20 + j * 8, 0, '#6a3a20', 1.5) for j in range(7)) + R(-3, -38, 6, 14, '#6a4a2a', 3) + hi(-8, 10, 5, 10, .4), f'translate({x},{y}) scale({s})')
def petal_flower(x, y, s=1, col='#ef8fa4', center='#f3c234', n=5, pl=30, pw=16):
    return G(''.join(E(0, -pl * .6, pw, pl * .6, col, f'transform="rotate({k*360/n})"') for k in range(n)) + Ci(0, 0, pw * .7, center), f'translate({x},{y}) scale({s})')
def lotus(x, y, s=1):
    return G(E(0, 20, 70, 14, '#4a9a5a') + ''.join(Pa(f'M0,10 Q{-16+j*8},-20 {(-40+j*20)*.5},-50 Q{(-20+j*20)*.6},-10 0,10 Z', ['#f6c8dc', '#ef8fa4', '#f6c8dc', '#ef8fa4', '#f6c8dc'][j]) for j in range(5)) + Pa('M0,10 Q-30,0 -46,-20 Q-20,-14 0,10 Z', '#f6c8dc') + Pa('M0,10 Q30,0 46,-20 Q20,-14 0,10 Z', '#f6c8dc'), f'translate({x},{y}) scale({s})')

# ================= 树 1 =================
S_('tree', meadow(170) + big_tree(100, 180, 1.2), False)
S_('wood', ''.join(G(R(-70, -16, 140, 32, '#c8903a', 4) + E(-70, 0, 10, 16, '#e8c890') + Ci(-70, 0, 5, '#c8a070', 'stroke="#a8703e" stroke-width="1"') + L(-50, -6, 60, -6, '#a8703e', 1.5), f'translate(100,{60+k*36})') for k in range(4)))
S_('branch', R(0, 0, 200, 200, '#dff1fb') + St('M0,140 Q60,120 120,100 Q160,86 200,60', '#8a5a35', 12) + St('M80,112 Q100,80 120,60', '#8a5a35', 6) + ''.join(leaf_shape(x, y, .4, '#5aaa3a', r_) for x, y, r_ in [(120, 60, 30), (160, 70, 60), (60, 120, -40), (190, 54, 40), (110, 76, -60)]), False)
S_('root', R(0, 0, 200, 200, SKY) + R(0, 80, 200, 120, '#8a6a4a') + R(90, 0, 20, 90, '#6a4a2a') + ''.join(St(f'M100,86 Q{100+d*30},{110+j*10} {100+d*70},{150+j*20}', '#a8805a', 6 - j) for d in (-1, 1) for j in range(3)) + St('M100,90 L100,190', '#a8805a', 5) + R(0, 70, 200, 12, '#7ab050'), False)
S_('bark', R(30, 10, 140, 180, '#8a5a35') + ''.join(St(f'M{40+k*18},10 Q{34+k*18},60 {44+k*18},110 Q{36+k*18},150 {42+k*18},190', '#6a3a20', 4) for k in range(8)) + E(110, 100, 10, 14, '#6a3a20'), False)
S_('tree-trunk', R(0, 0, 200, 200, '#dff1d8') + R(0, 170, 200, 30, '#7aa050') + Pa('M70,0 L130,0 L134,160 Q150,176 170,180 L30,180 Q50,176 66,160 Z', '#8a5a35') + ''.join(L(80 + k * 10, 10, 78 + k * 10, 160, '#6a3a20', 2) for k in range(5)), False)
S_('pine', R(0, 0, 200, 200, '#dff1fb') + R(0, 176, 200, 24, '#7aa050') + pine_tree(100, 186, 1.2), False)
S_('willow', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#5aa1d4') + willow(100, 170, 1.2), False)
S_('oak', meadow(170) + oak(100, 186, 1.0), False)
S_('maple', R(0, 0, 200, 200, '#fbe8cc') + leaf_shape(100, 100, 1.8, '#d9532a', 0, 'maple'), False)
S_('palm-tree', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#3c9ad4') + E(100, 170, 80, 16, '#f0d890') + palm(100, 170, 1.0), False)
S_('cherry-blossom', R(0, 0, 200, 200, '#dff1fb') + blossom_branch(100, 110, 1.1) + ''.join(G(Ci(0, 0, 4, '#f6c8dc'), f'translate({x},{y})') for x, y in [(40, 170), (150, 160), (90, 180)]), False)
S_('ginkgo', R(0, 0, 200, 200, '#fef3e2') + leaf_shape(80, 100, 1.4, '#f3c234', -20, 'ginkgo') + leaf_shape(140, 130, .8, '#e0b020', 30, 'ginkgo'), False)
S_('christmas-tree', R(0, 0, 200, 200, '#24304f') + ''.join(Ci((k * 37) % 200, (k * 53) % 140, 2, '#ffffff') for k in range(16)) + R(0, 176, 200, 24, '#ffffff') + xmas_tree(100, 180, 1.05), False)
S_('evergreen', snow_land(170) + pine_tree(60, 186, 1.0) + pine_tree(140, 186, .8, '#3a7a5a') + ''.join(Ci((k * 37) % 200, (k * 23) % 160, 3, '#ffffff') for k in range(12)), False)
S_('fallen-leaves', R(0, 0, 200, 200, '#e8d8b8') + ''.join(leaf_shape((k * 47) % 180 + 10, (k * 31) % 170 + 15, .45, ['#d9532a', '#f3a234', '#e07a2a', '#c8a040', '#a8502a'][k % 5], k * 47, 'maple' if k % 2 else 'oval') for k in range(16)), False)

# ================= 树 2（花草） =================
S_('bud', R(0, 0, 200, 200, '#e6f4e0') + St('M100,200 L100,90', '#4a9a3a', 6) + leaf_shape(84, 140, .5, '#5aaa3a', -50) + leaf_shape(116, 120, .5, '#5aaa3a', 50) + Pa('M100,60 Q80,80 92,100 L108,100 Q120,80 100,60 Z', '#ef8fa4') + Pa('M92,100 Q88,86 96,76 L100,100 Z', '#5aaa3a') + Pa('M108,100 Q112,86 104,76 L100,100 Z', '#5aaa3a'), False)
S_('petal', ''.join(G(E(0, -40, 20, 40, '#ef8fa4') + hi(-6, -50, 4, 12, .5), f'translate({60+k*40},{110+(k%2)*20}) rotate({-30+k*30})') for k in range(3)) + Ci(150, 50, 0, '#000'))
S_('stem', R(0, 0, 200, 200, '#e6f4e0') + St('M100,190 Q90,120 100,40', '#4a9a3a', 10) + leaf_shape(76, 120, .6, '#5aaa3a', -60) + leaf_shape(120, 90, .6, '#5aaa3a', 60) + petal_flower(100, 36, .6, '#e2463b') + St('M100,190 Q90,120 100,40', '#f3e070', 0) + R(60, 60, 0, 0, '#000') + St('M118,180 L140,150', '#e2463b', 0), False)
S_('thorn', R(0, 0, 200, 200, '#e6f4e0') + St('M60,200 Q80,100 120,20', '#4a8a3a', 12) + ''.join(Pa(f'M{x},{y} l{d*20},-8 l{-d*4},12 Z', '#7a4a2a') for x, y, d in [(74, 160, -1), (82, 130, 1), (92, 100, -1), (100, 76, 1), (110, 50, -1)]) + rose_(120, 30, 1.0), False)
S_('blossom', R(0, 0, 200, 200, '#dff1fb') + blossom_branch(100, 100, 1.2, '#ffffff', '#f3c234'), False)
S_('bloom', R(0, 0, 200, 200, '#e6f4e0') + St('M100,200 L100,110', '#4a9a3a', 6) + petal_flower(100, 90, 1.8, '#e2463b', '#f3c234', 8, 30, 14) + ''.join(L(100 + 70 * math.cos(a), 90 + 70 * math.sin(a), 100 + 82 * math.cos(a), 90 + 82 * math.sin(a), '#f3c234', 3) for a in [k * .785 for k in range(8)]), False)
S_('pollen', petal_flower(90, 110, 1.6, '#f3c234', '#f08a24', 8, 30, 14) + ''.join(Ci(90 + (k * 13) % 30 - 15, 110 + (k * 7) % 20 - 10, 3, '#e0a020') for k in range(10)) + bee_(160, 50, .7) + ''.join(Ci(120 + k * 10, 80 - k * 8, 3, '#f3c234') for k in range(3)))
S_('lotus', R(0, 0, 200, 200, '#cfe8f6') + R(0, 110, 200, 90, '#5aa1d4') + E(50, 160, 34, 10, '#4a9a5a') + lotus(110, 120, 1.3), False)
S_('vine', R(0, 0, 200, 200, '#f2ead8') + R(0, 0, 200, 200, '#d8c8b0', 0, 'opacity=".4"') + St('M20,200 Q60,140 40,100 Q20,60 80,40 Q140,20 180,60', '#4a8a3a', 5) + ''.join(leaf_shape(x, y, .35, '#5aaa3a', r_) for x, y, r_ in [(40, 160, -40), (36, 110, 60), (60, 60, -20), (110, 34, 40), (160, 46, -60)]) + ''.join(St(f'M{x},{y} q8,-8 4,-14', '#4a8a3a', 2) for x, y in [(50, 130), (90, 40), (150, 50)]), False)
S_('ivy', R(0, 0, 200, 200, '#c0603a') + ''.join(L(0, k * 20, 200, k * 20, '#a8502a', 1) for k in range(10)) + ''.join(G(Pa('M0,20 L-16,4 L-10,-6 L-16,-16 L0,-10 L16,-16 L10,-6 L16,4 Z', ['#3c7a2c', '#4a8a3a', '#2f6a2a'][k % 3]), f'translate({(k*37)%180+10},{(k*53)%180+10}) rotate({k*30})') for k in range(22)), False)
S_('moss', rock_(100, 120, 1.4, '#8a9196') + Pa('M40,110 Q60,80 100,80 Q140,80 160,110 Q120,100 100,104 Q70,100 40,110 Z', '#5a9a3a') + ''.join(Ci(50 + k * 12, 92 + (k % 3) * 4, 6, ['#6aaa4a', '#4a8a2a'][k % 2]) for k in range(9)))
S_('fern', R(0, 0, 200, 200, '#e6f4e0') + St('M100,196 Q104,110 90,24', '#4a8a3a', 4) + ''.join(G(E(d * (34 - j * 2.2), 0, 34 - j * 2.2, 7, '#5aaa3a'), f'translate({100+2-j*.6},{184-j*13}) rotate({-d*20})') for j in range(13) for d in (-1, 1)), False)
S_('reed', R(0, 0, 200, 200, '#cfe8f6') + R(0, 150, 200, 50, '#5aa1d4') + ''.join(St(f'M{30+k*24},200 Q{28+k*24},120 {34+k*24},{50+(k%3)*12}', '#8a9a5a', 3) + E(34 + k * 24, 46 + (k % 3) * 12, 4, 14, '#8a5a35') for k in range(7)), False)
S_('wildflower', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#9ac070') + ''.join(St(f'M{(k*37)%190+5},{200} L{(k*37)%190+5},{130+(k*17)%50}', '#4a9a3a', 2) + flower((k * 37) % 190 + 5, 130 + (k * 17) % 50, .9, ['#e2463b', '#f3c234', '#ffffff', '#7a4fa0', '#ef8fa4'][k % 5]) for k in range(16)), False)
S_('fruit-tree', meadow(170) + fruit_tree(100, 186, 1.6), False)
S_('algae', R(0, 0, 200, 200, '#3c8a7a') + ''.join(St(f'M{20+k*30},200 Q{10+k*30},150 {30+k*30},110 Q{40+k*30},70 {20+k*30},30', '#4aaa5a', 6) for k in range(6)) + ''.join(Ci((k * 37) % 200, (k * 53) % 200, 3, '#7ac87a', 'opacity=".6"') for k in range(14)), False)

# ================= 树 3 =================
S_('plum-blossom', R(0, 0, 200, 200, '#f2efe8') + blossom_branch(100, 110, 1.1, '#e2466a', '#f3e070') + ''.join(Ci(x, y, 3, '#ffffff') for x, y in [(40, 30), (160, 160)]), False)
S_('osmanthus', R(0, 0, 200, 200, '#fef3e2') + St('M20,180 Q100,120 180,40', '#6a4a2a', 6) + ''.join(leaf_shape(x, y, .45, '#3c7a2c', r_) for x, y, r_ in [(60, 140, -60), (110, 110, 40), (150, 70, -40), (90, 100, -120)]) + ''.join(petal_flower(x, y, .18, '#f3a234', '#e08a24', 4, 30, 16) for x, y in [(70, 150), (80, 140), (100, 120), (120, 104), (130, 96), (140, 80), (160, 60), (90, 130)]), False)
S_('jasmine', R(0, 0, 200, 200, '#e6f4e0') + ''.join(petal_flower(x, y, .7, '#ffffff', '#f3e070', 5, 30, 12) for x, y in [(70, 80), (130, 100), (90, 140)]) + leaf_shape(150, 160, .6, '#3c7a2c', 40) + leaf_shape(40, 140, .6, '#3c7a2c', -40), False)
S_('magnolia', R(0, 0, 200, 200, '#dff1fb') + St('M30,190 Q90,140 110,90', '#5a4a3a', 6) + G(Pa('M0,0 Q-30,-30 -10,-70 Q0,-30 0,0 Z', '#f6e8f0') + Pa('M0,0 Q30,-30 10,-70 Q0,-30 0,0 Z', '#f6d8e6') + Pa('M0,0 Q-16,-40 0,-80 Q16,-40 0,0 Z', '#ffffff') + Pa('M0,0 Q-40,-10 -40,-40 Q-14,-20 0,0 Z', '#e8b8d0'), 'translate(110,96) scale(1.1)'), False)
S_('azalea', R(0, 0, 200, 200, '#e6f4e0') + ''.join(leaf_shape(x, y, .35, '#3c7a2c', r_) for x, y, r_ in [(40, 160, -60), (160, 160, 60), (100, 180, 0)]) + ''.join(petal_flower(x, y, .8, '#e2466a', '#f6c8dc', 5, 30, 14) for x, y in [(60, 90), (130, 80), (100, 130), (150, 140), (50, 140)]), False)
S_('camellia', R(0, 0, 200, 200, '#e6f4e0') + leaf_shape(50, 140, .8, '#2f6a2a', -50) + leaf_shape(150, 140, .8, '#2f6a2a', 50) + ''.join(Ci(100 + 26 * math.cos(a), 100 + 26 * math.sin(a), 24, '#c8102e') for a in [k * 1.2566 for k in range(5)]) + ''.join(Ci(100 + 12 * math.cos(a), 100 + 12 * math.sin(a), 16, '#e2283e') for a in [k * 1.2566 + .6 for k in range(5)]) + Ci(100, 100, 10, '#f3c234'), False)
S_('birch', R(0, 0, 200, 200, '#dff1fb') + R(0, 176, 200, 24, '#9ac070') + birch(70, 190, 1.0) + birch(140, 190, .8), False)
S_('poplar', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#9ac070') + ''.join(poplar(40 + k * 40, 186, .9) for k in range(4)), False)
S_('cypress', R(0, 0, 200, 200, '#f6e8c8') + R(0, 176, 200, 24, '#c8b070') + cypress(70, 190, 1.0) + cypress(130, 190, .9), False)
S_('cedar', R(0, 0, 200, 200, '#dff1fb') + R(0, 176, 200, 24, '#9ac070') + cedar(100, 186, 1.2), False)
S_('elm', meadow(170) + elm(100, 186, 1.0), False)
S_('pine-cone', pinecone(100, 104, 1.6))
S_('acorn', acorn(80, 100, 1.4) + acorn(150, 140, .8) + leaf_shape(150, 60, .6, '#5a8a3a', 30, 'oak'))
S_('tree-ring', Ci(100, 100, 76, '#8a5a35') + Ci(100, 100, 70, '#e8c890') + ''.join(Ci(100 + (j % 2), 100, 66 - j * 8, 'none', 'stroke="#c8a070" stroke-width="2"') for j in range(8)) + Ci(100, 100, 4, '#a8703e'))
S_('canopy', R(0, 0, 200, 200, '#cfe8c0') + ''.join(Ci((k * 47) % 220 - 10, (k * 23) % 70, 30, ['#3c7a2c', '#4a8a3a', '#5a9a3a'][k % 3]) for k in range(14)) + ''.join(R(30 + k * 50, 60, 12, 140, '#6a4a2a') for k in range(3)) + ''.join(Pa(f'M{40+k*50},70 L{20+k*50},200 L{60+k*50},200 Z', '#f3e070', 'opacity=".12"') for k in range(3)), False)
S_('deciduous', R(0, 0, 200, 200, '#fef3e2') + G(big_tree(0, 0, .55, '#5aaa3a'), 'translate(50,190)') + arrow(86, 120, 114, 120, '#5d6469', 3) + G(R(-10, -60, 20, 60, '#6a4a2a', 3) + St('M0,-60 L-20,-90 M0,-60 L20,-96 M0,-50 L-30,-70', '#6a4a2a', 4), 'translate(150,190) scale(.9)') + ''.join(leaf_shape(140 + k * 10, 180, .15, '#e07a2a', k * 40, 'maple') for k in range(4)), False)

# ================= 菌类 =================
S_('mushroom', R(0, 0, 200, 200, '#e6f4e0') + R(0, 160, 200, 40, '#7aa050') + mushroom(100, 176, 1.6, '#c8603a', '#f6efe0', False), False)
S_('fungus', rock_(100, 150, 0) + R(0, 0, 200, 200, '#e6dcc8') + R(60, 0, 80, 200, '#8a5a35') + ''.join(G(Pa('M0,0 Q40,-10 50,10 Q20,16 0,8 Z', '#d8b880'), f'translate({140},{60+k*40})') for k in range(3)) + ''.join(L(144, 62 + k * 40, 180, 66 + k * 40, '#b8985a', 1) for k in range(3)), False)
S_('poisonous', R(0, 0, 200, 200, '#e6f4e0') + R(0, 160, 200, 40, '#7aa050') + mushroom(90, 176, 1.5, '#e2463b') + G(Pa('M0,-30 L30,22 L-30,22 Z', '#f3c234') + T(0, 16, '!', 30, '#2f3437', 900), 'translate(160,60)'), False)
S_('edible', R(0, 0, 200, 200, '#fef3e2') + plate(100, 140, 60) + mushroom(80, 150, .8, '#c8903a', '#f6efe0', False, 'flat') + mushroom(120, 150, .7, '#a8703e', '#f6efe0', False) + Ci(160, 50, 20, '#5ba644') + St('M150,50 l7,8 l13,-16', '#ffffff', 5), False)
S_('mold', R(0, 0, 200, 200, '#f6efe0') + G(R(-60, -40, 120, 80, '#e8c890', 10) + R(-60, -40, 120, 16, '#c8903a', 8), 'translate(100,110)') + ''.join(Ci(70 + (k * 23) % 60, 100 + (k * 13) % 40, 6 + k % 3 * 3, ['#7a9a7a', '#5a8a6a', '#9ab090'][k % 3], 'opacity=".9"') for k in range(10)), False)
S_('damp', R(0, 0, 200, 200, '#c8d0c8') + R(0, 0, 200, 200, '#8a9a8a', 0, 'opacity=".25"') + ''.join(Pa(f'M{x},{y} q-6,10 0,14 q6,-4 0,-14 Z', '#5aa1d4') for x, y in [(40, 60), (100, 40), (160, 70), (70, 120), (140, 140)]) + ''.join(Ci(30 + k * 40, 180, 16, '#7a8a6a', 'opacity=".4"') for k in range(5)), False)
S_('shiitake', R(0, 0, 200, 200, '#f2ead8') + mushroom(100, 170, 1.6, '#7a4a2a', '#f6efe0', False, 'flat') + ''.join(Pa(f'M{100+dx},{170-80+dy} l6,-4 l-2,6 Z', '#e6d8c0') for dx, dy in [(-30, -6), (0, -12), (24, -6), (-12, 2)]), False)
S_('wood-ear', R(0, 0, 200, 200, '#f2ead8') + R(0, 140, 200, 60, '#8a5a35') + ''.join(G(Pa('M0,0 Q-30,-40 0,-50 Q40,-50 30,-10 Q20,10 0,0 Z', '#3a2a24') + St('M4,-10 Q10,-30 20,-36', '#5a4a3a', 2), f'translate({50+k*50},{140-(k%2)*10}) rotate({-20+k*20})') for k in range(3)), False)
S_('enoki', R(0, 0, 200, 200, '#f2ead8') + ''.join(St(f'M{100+(k-6)*4},180 Q{100+(k-6)*6},120 {100+(k-6)*9},{60+abs(k-6)*4}', '#f6f2e6', 4) + Ci(100 + (k - 6) * 9, 58 + abs(k - 6) * 4, 6, '#f6efdc') for k in range(13)) + R(70, 170, 60, 20, '#5aa1d4', 4), False)
S_('button-mushroom', R(0, 0, 200, 200, '#f2ead8') + ''.join(mushroom(60 + k * 40, 170 - (k % 2) * 10, .9 - (k % 2) * .1, '#f6f2ea', '#e6e0d0', False) for k in range(3)), False)
S_('oyster-mushroom', R(0, 0, 200, 200, '#f2ead8') + ''.join(G(Pa('M0,0 Q-50,-10 -50,-40 Q-20,-60 20,-40 Q30,-20 0,0 Z', '#c8c0b0') + ''.join(L(0, 0, -40 + j * 10, -40, '#a8a090', 1) for j in range(6)), f'translate({110+k*10},{90+k*36}) rotate({k*10})') for k in range(3)), False)
S_('truffle', R(0, 0, 200, 200, '#e8d8b8') + Ci(90, 110, 46, '#3a2a24') + ''.join(Ci(90 + 40 * math.cos(a) * r_, 110 + 40 * math.sin(a) * r_, 4, '#5a4a3a') for a in [k * .9 for k in range(7)] for r_ in (.4, .8)) + G(R(-20, -4, 40, 8, '#c4cbd0', 3) + R(20, -6, 30, 12, '#8a5a35', 4), 'translate(150,170) rotate(-20)'), False)
S_('toadstool', R(0, 0, 200, 200, '#dff1d8') + R(0, 160, 200, 40, '#7aa050') + mushroom(100, 176, 1.6, '#e2463b', '#f6efe0', True) + frog_(150, 156, 0), False)
S_('spore', mushroom(70, 180, 1.3, '#c8903a', '#f6efe0', False) + ''.join(Ci(80 + (k * 23) % 100, 40 + (k * 31) % 60, 2 + k % 2, '#a8805a') for k in range(24)))
S_('lichen', rock_(100, 120, 1.4, '#8a9196') + ''.join(Ci(60 + (k * 31) % 80, 100 + (k * 17) % 40, 8 + k % 3 * 3, ['#c8d070', '#e0a040', '#a8c890'][k % 3]) for k in range(10)))
S_('forage', R(0, 0, 200, 200, '#dff1d8') + pine(30, 150, .6) + R(0, 150, 200, 50, '#7aa050') + W(80, 196, .8, '#5aa040', '#5a4a3a', 'straw', arms='front') + G(R(-24, -10, 48, 30, '#c8903a', 6) + St('M-20,-10 Q0,-30 20,-10', '#8a5a35', 3) + mushroom(-8, -6, .2, '#c8603a', '#f6efe0', False) + mushroom(8, -6, .2, '#a8703e', '#f6efe0', False), 'translate(84,130)') + mushroom(150, 186, .5, '#c8603a', '#f6efe0', False), False)

dump()
