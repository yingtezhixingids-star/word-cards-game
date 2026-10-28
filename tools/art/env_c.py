from kit5 import *

def rain_drops(n=14, col='#5aa1d4', y0=90):
    return ''.join(L((k * 37) % 190 + 6, y0 + (k * 23) % 90, (k * 37) % 190, y0 + (k * 23) % 90 + 14, col, 3) for k in range(n))
def snowflakes(n=14, y0=80, col='#ffffff'):
    return ''.join(G(''.join(L(0, 0, 7 * math.cos(a), 7 * math.sin(a), col, 2) for a in [j * math.pi / 3 for j in range(6)]), f'translate({(k*41)%190+6},{y0+(k*29)%100})') for k in range(n))
def dark_cloud(x, y, s=1):
    return cloud_(x, y, s, '#8a96a6')
def bolt(x, y, s=1, col='#f3c234'):
    return G(Pa('M0,0 L-14,30 L-2,30 L-10,60 L16,22 L4,22 L12,0 Z', col), f'translate({x},{y}) scale({s})')
def bin_(x, base, w, h, col, sym=''):
    return R(x - w / 2 - 4, base - h - 8, w + 8, 10, shade(col, -.2), 3) + Pa(f'M{x-w/2},{base-h} L{x+w/2},{base-h} L{x+w/2-6},{base} L{x-w/2+6},{base} Z', col) + sym
def recycle_sym(x, y, r, col='#ffffff'):
    if r <= 0: return ''
    g = ''
    rr = r * .55
    for k in range(3):
        a0 = math.radians(-80 + k * 120); a1 = math.radians(-80 + k * 120 + 85)
        g += St(f'M{x+rr*math.cos(a0)},{y+rr*math.sin(a0)} A{rr},{rr} 0 0,1 {x+rr*math.cos(a1)},{y+rr*math.sin(a1)}', col, r * .14)
        tx, ty = x + rr * math.cos(a1 + .25), y + rr * math.sin(a1 + .25)
        ang = a1 + math.pi / 2
        g += Pa(f'M{tx+r*.16*math.cos(ang)},{ty+r*.16*math.sin(ang)} L{tx+r*.16*math.cos(ang+2.4)},{ty+r*.16*math.sin(ang+2.4)} L{tx+r*.16*math.cos(ang-2.4)},{ty+r*.16*math.sin(ang-2.4)} Z', col)
    return g
def gem_(x, y, s=1, col='#e2463b'):
    return G(Pa('M-30,-10 L-18,-28 L18,-28 L30,-10 L0,30 Z', col) + Pa('M-30,-10 L30,-10 L0,30 Z', shade(col, -.15)) + Pa('M-18,-28 L-8,-10 L8,-10 L18,-28 Z', shade(col, .2)) + L(-8, -10, 0, 30, shade(col, -.25), 1) + L(8, -10, 0, 30, shade(col, -.25), 1) + hi(-12, -20, 5, 3, .7), f'translate({x},{y}) scale({s})')
def oval_gem(x, y, s=1, col='#2f9a5a'):
    return G(E(0, 0, 34, 24, shade(col, -.2)) + E(0, 0, 28, 19, col) + Pa('M-28,0 L0,-19 L28,0 L0,19 Z', shade(col, .12)) + hi(-10, -8, 8, 4, .6), f'translate({x},{y}) scale({s})')
def rock_(x, y, s=1, col='#8a9196'):
    return G(Pa('M-50,30 L-56,-4 L-30,-34 L10,-40 L46,-20 L56,20 L30,36 Z', col) + Pa('M-30,-34 L10,-40 L0,-6 L-40,0 Z', shade(col, .15)) + Pa('M10,-40 L46,-20 L20,4 L0,-6 Z', shade(col, .05)), f'translate({x},{y}) scale({s})')
def specks(x, y, w, h, cols, n=40):
    return ''.join(Ci(x + (k * 37) % w, y + (k * 53) % h, 2 + k % 3, cols[k % len(cols)]) for k in range(n))
def crystal_cluster(x, base, s=1, col='#c8a0f0'):
    return G(''.join(Pa(f'M{dx-w},0 L{dx-w},{-h} L{dx},{-h-14} L{dx+w},{-h} L{dx+w},0 Z', shade(col, sh)) + Pa(f'M{dx},{-h-14} L{dx+w},{-h} L{dx+w},0 L{dx},0 Z', shade(col, sh - .12)) for dx, w, h, sh in [(-30, 12, 50, .1), (0, 16, 90, .2), (30, 12, 60, 0), (14, 9, 40, .25), (-14, 9, 36, .3)]), f'translate({x},{base}) scale({s})')

# ================= 天气 =================
S_('sunny', R(0, 0, 200, 200, '#9fd8f6') + sun(100, 90, 40), False)
S_('rainy', R(0, 0, 200, 200, '#a8b8c8') + dark_cloud(100, 60, 1.3) + rain_drops(16) + umbrella(100, 170, 0), False)
S_('cloudy', R(0, 0, 200, 200, '#b8d8ec') + cloud_(70, 70, 1.0, '#ffffff') + cloud_(130, 110, 1.1, '#e6ecef') + sun(150, 50, 0), False)
S_('windy', R(0, 0, 200, 200, '#cfe8f6') + ''.join(St(f'M10,{50+k*36} Q80,{36+k*36} 140,{50+k*36} Q170,{56+k*36} 160,{36+k*36}', '#7a9aaa', 4) for k in range(4)) + ''.join(leaf(60 + k * 40, 70 + k * 30, 14, 6, 30 + k * 40, '#5aaa3a') for k in range(3)), False)
S_('snowy', R(0, 0, 200, 200, '#cfe2f0') + cloud_(100, 50, 1.2, '#e6ecef') + snowflakes(14, 90) + R(0, 170, 200, 30, '#ffffff'), False)
S_('rain', R(0, 0, 200, 200, '#e8eef2') + ''.join(drop(30 + (k * 37) % 150, 40 + (k * 43) % 130, 12) for k in range(10)), False)
S_('snow', R(0, 0, 200, 200, '#cfe2f0') + G(''.join(St(f'M0,0 L{60*math.cos(a)},{60*math.sin(a)}', '#ffffff', 8) + St(f'M{36*math.cos(a)},{36*math.sin(a)} l{14*math.cos(a+.8)},{14*math.sin(a+.8)} M{36*math.cos(a)},{36*math.sin(a)} l{14*math.cos(a-.8)},{14*math.sin(a-.8)}', '#ffffff', 6) for a in [k * math.pi / 3 for k in range(6)]), 'translate(100,100)'), False)
S_('cool', R(0, 0, 200, 200, '#dff1fb') + G(R(-12, -70, 24, 120, '#ffffff', 12, 'stroke="#c4cbd0" stroke-width="3"') + R(-5, -20, 10, 60, '#5aa1d4', 5) + Ci(0, 54, 18, '#5aa1d4'), 'translate(60,100)') + ''.join(leaf(130 + k * 14, 80 + k * 26, 16, 8, 30 + k * 30, ['#e08a24', '#d9532a', '#f3a234'][k]) for k in range(3)) + St('M110,60 Q140,50 170,60', '#7a9aaa', 3), False)
S_('foggy', R(0, 0, 200, 200, '#c8d0d6') + building(30, 60, 40, 140, '#a7adb1') + building(120, 80, 50, 120, '#a7adb1') + ''.join(R(0, 50 + k * 30, 200, 18, '#e6ecef', 9, 'opacity=".75"') for k in range(5)), False)
S_('storm', R(0, 0, 200, 200, '#4a5468') + dark_cloud(100, 50, 1.4) + bolt(90, 70, 1.0) + rain_drops(14, '#9fd0ec', 100) + G(tree(0, 0, .5), 'translate(160,190) rotate(20)'), False)
S_('thunder', R(0, 0, 200, 200, '#4a5468') + dark_cloud(100, 60, 1.4) + ''.join(St(f'M{60-k*12},{110+k*10} q-10,10 0,20', '#f3e070', 3) + St(f'M{140+k*12},{110+k*10} q10,10 0,20', '#f3e070', 3) for k in range(3)) + T(100, 160, '!', 0, '#000') + G(Ci(0, 0, 12, SK) + hand(-14, 0, .3) + hand(14, 0, .3), 'translate(100,170)'), False)
S_('lightning', R(0, 0, 200, 200, '#2f3a4f') + dark_cloud(100, 40, 1.2) + bolt(90, 60, 2.0), False)
S_('rainbow', R(0, 0, 200, 200, '#cfe8f6') + ''.join(Pa(f'M{10+k*8},160 A{90-k*8},{90-k*8} 0 0,1 {190-k*8},160', 'none', f'stroke="{c}" stroke-width="8"') for k, c in enumerate(['#e2463b', '#f08a24', '#f3c234', '#5ba644', '#3c7fc1', '#2f4a8a', '#7a4fa0'])) + cloud_(30, 160, .6) + cloud_(170, 160, .6), False)
S_('typhoon', R(0, 0, 200, 200, '#6a7a8a') + ''.join(St(f'M100,100 ' + ' '.join(f'L{100+(4+t*2.4)*math.cos(t*.35+arm*2.094)},{100+(4+t*2.4)*math.sin(t*.35+arm*2.094)}' for t in range(34)), '#e6ecef', 10, 'opacity=".8"') for arm in range(3)) + Ci(100, 100, 10, '#4a5468') + G(tree(0, 0, .4), 'translate(30,196) rotate(-30)'), False)
S_('humid', R(0, 0, 200, 200, '#e0eef0') + person_bust(100, 120, 34, '#f3c234', m='o') + ''.join(drop(x, y, 6) for x, y in [(60, 90), (140, 100), (130, 140)]) + ''.join(Ci(30 + k * 30, 40 + (k % 2) * 10, 6, '#9fd0ec', 'opacity=".5"') for k in range(6)) + T(170, 40, '90%', 20, '#3c7fc1', 900), False)
S_('freezing', R(0, 0, 200, 200, '#cfe2f0') + person_bust(100, 110, 34, '#3c7fc1', m='o') + R(66, 132, 68, 14, '#e2463b', 6) + G(R(-12, -70, 24, 120, '#ffffff', 12, 'stroke="#c4cbd0" stroke-width="3"') + R(-5, 20, 10, 20, '#3c7fc1', 5) + Ci(0, 54, 18, '#3c7fc1'), 'translate(170,80) scale(.6)') + snowflakes(6, 20) + ''.join(L(64 + k * 4, 100, 60 + k * 4, 110, '#9fd0ec', 2) for k in range(0)) + St('M60,90 l-6,4 l6,4 l-6,4', '#5aa1d4', 2) + St('M140,90 l6,4 l-6,4 l6,4', '#5aa1d4', 2), False)

# ================= 气候/环保 =================
S_('recycle', Ci(100, 100, 74, '#5ba644') + recycle_sym(100, 104, 80))
S_('garbage', bin_(80, 186, 80, 100, '#5d6469') + Pa('M50,86 Q60,60 80,70 Q96,50 110,74 L114,86 Z', '#8a9196') + G(R(-10, -14, 20, 28, '#c8a070', 2), 'translate(150,170) rotate(20)') + apple(170, 180, .3, '#8a6a3a') + bottle_shape(120, 140, 16, 40, '#9fd0ec'))
S_('plastic', bottle_shape(40, 40, 40, 120, '#9fd0ec', .3) + G(Pa('M-30,-40 L30,-40 L40,40 L-40,40 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2" opacity=".9"') + Pa('M-16,-40 Q-16,-60 0,-60 Q16,-60 16,-40', 'none', 'stroke="#c4cbd0" stroke-width="3"'), 'translate(130,120)') + G(R(-24, -6, 48, 12, '#f3c234', 4), 'translate(80,176)'))
S_('pollution', R(0, 0, 200, 200, '#b8b0a0') + factory(10, 170, 100, 60, '#8a6a5a') + ''.join(Ci(90 + k * 20, 60 - k * 8, 18 + k * 4, '#5d5850', 'opacity=".7"') for k in range(4)) + R(0, 170, 200, 30, '#6a6a5a') + G(fish_shape(0, 0, 26, '#8a9196'), 'translate(160,186) rotate(180)'), False)
S_('smog', R(0, 0, 200, 200, '#c8b890') + ''.join(building(10 + k * 46, 70 + (k % 2) * 30, 40, 130, '#8a8070', '#a89a80', 2, 5) for k in range(4)) + R(0, 0, 200, 200, '#b8a880', 0, 'opacity=".55"') + Ci(150, 40, 16, '#d8c8a0', 'opacity=".8"') + G(person_bust(0, 0, 18, '#5d6469') + R(-12, 2, 24, 12, '#ffffff', 4), 'translate(100,170)'), False)
S_('protect', G(hand(0, 0, 1.2, 0), 'translate(60,150) rotate(-30)') + G(hand(0, 0, 1.2, 0), 'translate(140,150) rotate(30) scale(-1,1)') + earth_(100, 90, 40) + heart(100, 30, 10))
S_('environment', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#9ac070') + tree(50, 140, 1.0) + tree(150, 150, .7) + E(110, 170, 30, 10, '#5aa1d4') + sun(160, 40, 16) + G(E(0, 0, 10, 6, '#e2463b') + Ci(8, -4, 4, '#e2463b'), 'translate(90,60)') + flower(80, 170, 1.2), False)
S_('climate', earth_(100, 110, 50) + sun(40, 40, 16) + cloud_(160, 40, .5) + snowflakes(0) + G(R(-8, -40, 16, 66, '#ffffff', 8, 'stroke="#c4cbd0" stroke-width="2"') + R(-3, -10, 6, 34, '#e2463b', 3) + Ci(0, 28, 10, '#e2463b'), 'translate(170,140)'))
S_('flood', R(0, 0, 200, 200, '#a8b8c8') + dark_cloud(100, 30, 1.0) + house(60, 150, 70, 54) + R(0, 120, 200, 80, '#7a9ab0', 0, 'opacity=".9"') + ''.join(St(f'M{-10+(k%2)*20},{130+k*16} q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', '#9fc0d6', 3) for k in range(4)) + tree(160, 140, .5), False)
S_('drought', R(0, 0, 200, 200, '#f6d890') + sun(150, 40, 24, '#f3a234') + R(0, 110, 200, 90, '#d8a860') + ''.join(St(f'M{20+k*36},{120+(k%3)*24} l10,10 l-6,10 l12,8', '#a87838', 2) for k in range(6)) + G(St('M0,0 Q0,-30 10,-40', '#a8905a', 3) + leaf(6, -30, 14, 5, 40, '#c8a860'), 'translate(60,150)') + G(R(-30, -6, 60, 12, '#d8d0c0', 6) + Ci(0, 0, 10, '#e8e0d0'), 'translate(130,170)'), False)
S_('global-warming', earth_(100, 110, 56) + Ci(100, 110, 56, '#e2463b', 'opacity=".3"') + G(R(-10, -50, 20, 80, '#ffffff', 10, 'stroke="#c4cbd0" stroke-width="2"') + R(-4, -40, 8, 64, '#e2463b', 4) + Ci(0, 34, 12, '#e2463b'), 'translate(170,90)') + flame(40, 60, .6) + arrow(170, 40, 170, 14, '#e2463b', 4))
S_('sort-the-trash', ''.join(bin_(30 + k * 47, 186, 38, 80, c, recycle_sym(30 + k * 47, 140, 20) if k == 0 else '') for k, c in enumerate(['#3c7fc1', '#5ba644', '#e2463b', '#5d6469'])) + G(R(-6, -16, 12, 24, '#9fd0ec', 3), 'translate(30,60)') + arrow(30, 80, 30, 96, '#2f3437', 3) + apple(77, 70, .4, '#8a6a3a') + arrow(77, 84, 77, 96, '#2f3437', 3))
S_('reusable-bag', Pa('M50,70 L150,70 L160,180 L40,180 Z', '#c8b890') + St('M70,70 Q70,30 100,30 Q130,30 130,70', '#a89870', 6) + leaf(100, 140, 30, 14, -60, '#5ba644') + recycle_sym(100, 110, 0) + St('M90,150 L100,120', '#5ba644', 0))
S_('endangered', R(0, 0, 200, 200, '#e6f0d8') + G(Ci(0, 0, 40, '#ffffff') + Ci(-30, -32, 14, '#2f3437') + Ci(30, -32, 14, '#2f3437') + E(-14, -4, 10, 13, '#2f3437') + E(14, -4, 10, 13, '#2f3437') + Ci(-12, -4, 3, '#ffffff') + Ci(14, -4, 3, '#ffffff') + E(0, 12, 6, 4, '#2f3437') + E(0, 60, 40, 30, '#2f3437'), 'translate(90,90)') + G(Pa('M0,-30 L30,22 L-30,22 Z', '#f3c234') + T(0, 16, '!', 30, '#2f3437', 900), 'translate(160,160)') + ''.join(leaf(20 + k * 14, 180, 20, 6, -70, '#5aaa3a') for k in range(3)), False)
S_('carbon-footprint', Pa('M60,140 Q50,80 70,50 Q90,30 110,50 Q130,80 120,140 Q100,170 80,160 Q60,160 60,140 Z', '#2f3437') + ''.join(Ci(x, y, r_, '#2f3437') for x, y, r_ in [(60, 30, 9), (80, 20, 10), (100, 18, 10), (118, 26, 9), (132, 40, 8)]) + T(92, 120, 'CO₂', 22, '#ffffff', 900))
S_('deforestation', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#a8905a') + ''.join(E(30 + k * 40, 160, 12, 5, '#d9a868') + R(18 + k * 40, 148, 24, 12, '#8a5a35') for k in range(4)) + G(R(-60, -8, 120, 16, '#8a5a35', 6) + E(-60, 0, 6, 8, '#d9a868'), 'translate(110,180) rotate(-6)') + pine(180, 150, .6) + saw_(60, 100, .5, 0), False)

# ================= 岩石宝石 =================
S_('rock', rock_(100, 120, 1.3))
S_('pebble', ''.join(E(50 + (k % 3) * 50, 90 + (k // 3) * 50, 24 - k % 2 * 4, 16, ['#a7adb1', '#c8b8a0', '#8a9196', '#d0c8bc', '#9a8a7a', '#b8c0c4'][k]) + hi(42 + (k % 3) * 50, 84 + (k // 3) * 50, 6, 3, .5) for k in range(6)))
S_('jade', G(Ci(0, 0, 60, '#4aaa7a') + Ci(0, 0, 24, '#f6efe0') + Ci(0, 0, 60, 'none', 'stroke="#3a8a5a" stroke-width="3"') + hi(-30, -30, 14, 6, .5, -40), 'translate(100,100)') + St('M100,40 L100,10', '#e2463b', 3))
S_('diamond-rocks', G(Pa('M-60,-20 L-36,-50 L36,-50 L60,-20 L0,60 Z', '#dff1fb') + Pa('M-60,-20 L60,-20 L0,60 Z', '#bfe0f0') + Pa('M-36,-50 L-16,-20 L16,-20 L36,-50 Z', '#ffffff') + L(-16, -20, 0, 60, '#9fd0ec', 1.5) + L(16, -20, 0, 60, '#9fd0ec', 1.5), 'translate(100,100)') + ''.join(star(x, y, s_, '#ffffff') for x, y, s_ in [(50, 50, 8), (160, 70, 6)]))
S_('pearl', G(Pa('M-60,10 Q-60,-50 0,-50 Q60,-50 60,10 Z', '#c8b8d0') + Pa('M-64,10 Q0,40 64,10 Q0,70 -64,10 Z', '#a898b0'), 'translate(100,100)') + Ci(100, 100, 22, '#f6f2f8') + hi(92, 92, 7, 5, .9))
S_('crystal', crystal_cluster(100, 170, 1.2))
S_('gem', gem_(60, 90, 1.0, '#e2463b') + gem_(130, 80, .8, '#3c7fc1') + oval_gem(100, 150, 1.0, '#2f9a5a'))
S_('marble', R(30, 40, 140, 120, '#f2f0ec', 4) + ''.join(St(f'M{30+k*20},{40} Q{60+k*15},{100} {40+k*30},{160}', '#c4c0b8', 2) for k in range(5)) + St('M40,80 Q100,60 160,120', '#a8a49c', 3))
S_('granite', R(30, 40, 140, 120, '#c8b8b0', 4) + specks(34, 44, 132, 112, ['#2f3437', '#ffffff', '#a8705a', '#5d6469'], 120))
S_('mineral', rock_(100, 120, 1.2, '#8a7a6a') + crystal_cluster(100, 110, .5, '#9fd0ec') + specks(60, 120, 80, 30, ['#f3c234'], 10))
S_('fossil', rock_(100, 110, 1.4, '#c8b8a0') + Ci(100, 106, 40, '#b8a88e') + St('M100,106 ' + ' '.join(f'L{100+(2+t*1.15)*math.cos(t*.3):.1f},{106+(2+t*1.15)*math.sin(t*.3):.1f}' for t in range(34)), '#6a5a4a', 4) + ''.join(L(100 + 22 * math.cos(a), 106 + 22 * math.sin(a), 100 + 38 * math.cos(a), 106 + 38 * math.sin(a), '#8a7a6a', 2) for a in [k * .5 for k in range(12)]))
S_('ruby', gem_(100, 100, 1.8, '#c8102e'))
S_('emerald', G(R(-40, -50, 80, 100, '#1f9a5a', 10) + R(-28, -38, 56, 76, '#3cba7a', 6) + R(-16, -26, 32, 52, '#5ad49a', 4) + hi(-20, -30, 10, 5, .6), 'translate(100,100)'))
S_('sapphire', oval_gem(100, 100, 2.0, '#1f4aa8'))
S_('amber', G(Pa('M-50,0 Q-56,-50 0,-56 Q56,-50 50,10 Q40,60 0,56 Q-50,50 -50,0 Z', '#e8962a', 'opacity=".9"') + G(E(0, 0, 10, 6, '#3a2a20') + E(-8, -6, 8, 4, '#c8b8a0', 'opacity=".8"') + E(8, -6, 8, 4, '#c8b8a0', 'opacity=".8"'), 'translate(0,4)') + hi(-24, -26, 12, 6, .5), 'translate(100,100)'))
S_('quartz', crystal_cluster(100, 170, 1.2, '#f2eef6'))

dump()
