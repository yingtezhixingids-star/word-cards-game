from kit5 import *

SPACE = '#141a33'
def space_bg(n=14):
    return R(0, 0, 200, 200, SPACE) + ''.join(Ci((k * 61) % 200, (k * 37) % 200, 1 + (k % 3) * .6, '#ffffff', f'opacity="{.4+(k%3)*.2}"') for k in range(n * 3))
def earth_(x, y, r):
    return Ci(x, y, r, '#3c8ad4') + Pa(f'M{x-r*.6},{y-r*.5} Q{x-r*.2},{y-r*.8} {x+r*.1},{y-r*.5} Q{x},{y-r*.1} {x-r*.3},{y} Q{x-r*.7},{y-r*.1} {x-r*.6},{y-r*.5} Z', '#5aaa4a') + Pa(f'M{x+r*.2},{y} Q{x+r*.7},{y-r*.2} {x+r*.7},{y+r*.3} Q{x+r*.5},{y+r*.8} {x+r*.2},{y+r*.6} Q{x},{y+r*.3} {x+r*.2},{y} Z', '#5aaa4a') + hi(x - r * .4, y - r * .4, r * .2, r * .12, .3)
def planet(x, y, r, col, ring=False, bands=None):
    g = ''
    if ring: g += E(x, y, r * 1.8, r * .45, 'none', f'stroke="{shade(col,-.1)}" stroke-width="{r*.18}" transform="rotate(-15 {x} {y})"')
    g += Ci(x, y, r, col)
    if bands: g += ''.join(E(x, y - r * .5 + k * r * .35, r * .95 * math.sqrt(max(0.1, 1 - ((-.5 + k * .35)) ** 2)), r * .07, bands[k % len(bands)]) for k in range(4))
    if ring: g += Pa(f'M{x-r*1.8},{y} A{r*1.8},{r*.45} 0 0,0 {x+r*1.8},{y}', 'none', f'stroke="{shade(col,-.1)}" stroke-width="{r*.18}" transform="rotate(-15 {x} {y})"')
    return g
def rocket(x, y, s=1, rot=0):
    return G(Pa('M0,-80 Q24,-50 22,10 L-22,10 Q-24,-50 0,-80 Z', '#ffffff') + Ci(0, -36, 10, '#3c7fc1') + Ci(0, -36, 6, '#9fd0ec') + Pa('M-22,-10 L-40,20 L-22,14 Z', '#e2463b') + Pa('M22,-10 L40,20 L22,14 Z', '#e2463b') + Pa('M0,-80 Q12,-66 16,-56 L-16,-56 Q-12,-66 0,-80 Z', '#e2463b') + R(-14, 10, 28, 8, '#5d6469', 2) + Pa('M-12,18 Q0,60 12,18 Z', '#f08a24') + Pa('M-6,18 Q0,40 6,18 Z', '#f3e070'), f'translate({x},{y}) rotate({rot}) scale({s})')
def astro(x, y, s=1):
    return G(Ci(0, -50, 22, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + R(-14, -58, 28, 18, '#2f4a7a', 8) + hi(-6, -54, 5, 3, .7) + R(-26, -28, 52, 56, '#ffffff', 12, 'stroke="#c4cbd0" stroke-width="2"') + R(-10, -18, 20, 14, '#c4cbd0', 3) + Ci(-4, -11, 2, '#e2463b') + Ci(4, -11, 2, '#3c7fc1') + R(-40, -24, 16, 40, '#ffffff', 8, 'stroke="#c4cbd0" stroke-width="2"') + R(24, -24, 16, 40, '#ffffff', 8, 'stroke="#c4cbd0" stroke-width="2"') + R(-22, 26, 18, 34, '#ffffff', 6, 'stroke="#c4cbd0" stroke-width="2"') + R(4, 26, 18, 34, '#ffffff', 6, 'stroke="#c4cbd0" stroke-width="2"') + R(-30, -26, 60, 6, '#e2463b', 2, 'opacity="0"'), f'translate({x},{y}) scale({s})')
def scope(x, y, s=1):
    return G(G(R(-60, -12, 110, 24, '#3c7fc1', 6) + R(46, -16, 14, 32, '#2f5a9a', 3) + R(-70, -8, 12, 16, '#5d6469', 3), 'rotate(-30)') + L(0, 0, -30, 70, '#5d6469', 4) + L(0, 0, 30, 70, '#5d6469', 4) + L(0, 0, 0, 74, '#5d6469', 4), f'translate({x},{y}) scale({s})')
def comet_(x, y, s=1, rot=30):
    return G(Pa('M0,-10 L-120,-2 L-120,2 L0,10 Z', '#9fd0ec', 'opacity=".5"') + Pa('M0,-6 L-80,0 L0,6 Z', '#ffffff', 'opacity=".7"') + Ci(0, 0, 12, '#ffffff') + Ci(0, 0, 8, '#cfe8f6'), f'translate({x},{y}) rotate({rot}) scale({s})')
def satellite_(x, y, s=1, rot=-20):
    return G(R(-14, -14, 28, 28, '#d9a33a', 3) + R(-70, -12, 50, 24, '#3c7fc1') + R(20, -12, 50, 24, '#3c7fc1') + ''.join(L(-70 + k * 10, -12, -70 + k * 10, 12, '#9fd0ec', 1) for k in range(1, 5)) + ''.join(L(20 + k * 10, -12, 20 + k * 10, 12, '#9fd0ec', 1) for k in range(1, 5)) + L(0, 14, 0, 28, '#a7adb1', 2) + E(0, 30, 10, 4, '#c4cbd0'), f'translate({x},{y}) rotate({rot}) scale({s})')
def ufo(x, y, s=1):
    return G(E(0, 0, 60, 16, '#a7adb1') + Pa('M-30,-4 Q-30,-36 0,-36 Q30,-36 30,-4 Z', '#9fd0ec', 'opacity=".85"') + ''.join(Ci(-40 + k * 20, 4, 4, '#f3e070') for k in range(5)) + Pa('M-20,14 L20,14 L40,70 L-40,70 Z', '#f3e070', 'opacity=".25"'), f'translate({x},{y}) scale({s})')
def alien_(x, y, s=1):
    return G(E(0, 0, 30, 36, '#7cc05a') + E(-12, -4, 9, 13, '#2f3437', 'transform="rotate(-20 -12 -4)"') + E(12, -4, 9, 13, '#2f3437', 'transform="rotate(20 12 -4)"') + St('M-6,18 Q0,22 6,18', '#2f3437', 2) + L(-10, -32, -20, -54, '#7cc05a', 3) + L(10, -32, 20, -54, '#7cc05a', 3) + Ci(-20, -56, 5, '#f3c234') + Ci(20, -56, 5, '#f3c234') + R(-20, 34, 40, 40, '#7cc05a', 12), f'translate({x},{y}) scale({s})')
def globe_(x, y, r):
    return earth_(x, y, r) + E(x, y, r, r * .35, 'none', 'stroke="#ffffff" stroke-width="1" opacity=".6"') + E(x, y, r * .35, r, 'none', 'stroke="#ffffff" stroke-width="1" opacity=".6"') + St(f'M{x+r*1.1},{y-r*1.0} A{r*1.4},{r*1.4} 0 0,1 {x+r*1.1},{y+r*1.0}', '#d9a33a', 5) + R(x - 6, y + r + 6, 12, 18, '#8a5a35') + E(x, y + r + 26, r * .6, 8, '#8a5a35')
def volcano_(x, base, s=1, erupt=True):
    g = Pa('M-90,0 L-24,-90 L24,-90 L90,0 Z', '#8a6a5a') + Pa('M-24,-90 L24,-90 L10,-70 Q0,-60 -10,-72 Z', '#5d4a40')
    if erupt: g += Pa('M-20,-92 Q0,-110 20,-92 L14,-60 Q8,-40 0,-70 Q-8,-40 -14,-60 Z', '#e2463b') + ''.join(Ci(-30 + k * 15, -110 - (k % 2) * 20, 14, '#8a837c', 'opacity=".7"') for k in range(5)) + Pa('M-10,-80 Q-30,-40 -40,0 L-30,0 Q-20,-40 -4,-70 Z', '#f08a24')
    return G(g, f'translate({x},{base}) scale({s})')
def mountain_bg(sky=SKY):
    return R(0, 0, 200, 200, sky) + Pa('M0,160 L60,60 L110,130 L150,70 L200,140 L200,200 L0,200 Z', '#7a8a9a') + Pa('M60,60 L74,82 L46,82 Z', '#ffffff') + Pa('M150,70 L162,88 L138,88 Z', '#ffffff')
def cave_(x, base, s=1):
    return G(Pa('M-90,0 Q-90,-110 0,-110 Q90,-110 90,0 Z', '#8a7a6a') + Pa('M-46,0 Q-46,-70 0,-70 Q46,-70 46,0 Z', '#2a2420') + ''.join(Pa(f'M{-36+k*18},-62 l6,14 l6,-14 Z', '#8a7a6a') for k in range(4)), f'translate({x},{base}) scale({s})')
def compass_rose(x, y, r, hl=None):
    g = Ci(x, y, r, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"')
    for k, (dx, dy, lab) in enumerate([(0, -1, 'N'), (1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W')]):
        col = '#e2463b' if lab == hl else '#5d6469'
        g += Pa(f'M{x},{y} L{x+dx*r*.8+dy*r*.15},{y+dy*r*.8-dx*r*.15} L{x+dx*r*.95},{y+dy*r*.95} L{x+dx*r*.8-dy*r*.15},{y+dy*r*.8+dx*r*.15} Z', col)
        g += T(x + dx * (r + 16), y + dy * (r + 16) + 7, lab, 20, col, 900)
    return g + Ci(x, y, 5, '#2f3437')
def village_house(x, base, s=1, wall='#f4e6c8', roof='#5d6469'):
    return house(x, base, 40 * s, 30 * s, wall, roof)

# ================= 太空 1 =================
S_('sun-space1', space_bg() + Ci(100, 100, 56, '#f3a234') + Ci(100, 100, 46, '#f3c234') + ''.join(Pa(f'M{100+60*math.cos(a)},{100+60*math.sin(a)} L{100+80*math.cos(a+.1)},{100+80*math.sin(a+.1)} L{100+60*math.cos(a+.2)},{100+60*math.sin(a+.2)} Z', '#f08a24') for a in [k * .5236 for k in range(12)]), False)
S_('moon', space_bg() + Ci(100, 100, 60, '#e6e2d8') + ''.join(Ci(x, y, r_, '#c8c2b4') for x, y, r_ in [(80, 80, 12), (120, 110, 16), (90, 130, 8), (126, 70, 7)]), False)
S_('star', R(0, 0, 200, 200, '#24304f') + star(100, 100, 50, '#f3e070') + ''.join(star(x, y, 6, '#ffffff') for x, y in [(30, 40), (160, 30), (40, 160), (170, 150)]), False)
S_('sky', R(0, 0, 200, 200, '#8ccaf0') + R(0, 0, 200, 80, '#6ab4e8') + cloud_(60, 70, .9) + cloud_(150, 120, .7) + sun(160, 40, 14) + ''.join(G(St('M-8,0 Q-4,-6 0,0 Q4,-6 8,0', '#2f3437', 2), f'translate({x},{y})') for x, y in [(60, 140), (90, 150)]), False)
S_('space', space_bg(20) + planet(60, 60, 20, '#e08a5a') + earth_(140, 130, 30) + rocket(60, 150, .4, 40), False)
S_('planet', space_bg() + planet(90, 100, 52, '#5aa0c8', False, ['#3c80b0', '#8ac0e0']) + Ci(160, 50, 10, '#c4cbd0') + Ci(40, 160, 6, '#e08a5a'), False)
S_('earth', space_bg() + earth_(100, 100, 66), False)
S_('rocket', space_bg() + rocket(100, 110, 1.1, 20), False)
S_('astronaut', space_bg() + astro(100, 110, 1.3) + earth_(170, 170, 24), False)
S_('telescope', R(0, 0, 200, 200, '#24304f') + ''.join(star(x, y, 4, '#ffffff') for x, y in [(160, 30), (130, 60), (180, 80)]) + moon(160, 50, 0) + R(0, 160, 200, 40, '#2f4a3a') + scope(90, 100, 1.0), False)
S_('mars', space_bg() + Ci(100, 100, 60, '#c8502a') + ''.join(Ci(x, y, r_, '#a83a1a') for x, y, r_ in [(80, 80, 10), (120, 120, 14), (90, 130, 6)]) + E(100, 46, 20, 6, '#ffffff', 'opacity=".8"'), False)
S_('galaxy', space_bg(20) + ''.join(St(f'M100,100 ' + ' '.join(f'L{100+(4+t*2.2)*math.cos(t*.4+arm*math.pi)},{100+(4+t*2.2)*.6*math.sin(t*.4+arm*math.pi)}' for t in range(36)), ['#c8a0f0', '#9fd0ec'][arm], 8, 'opacity=".6"') for arm in range(2)) + Ci(100, 100, 14, '#ffffff') + Ci(100, 100, 22, '#f6e8ff', 'opacity=".4"'), False)
S_('milky-way', R(0, 0, 200, 200, '#1a2040') + Pa('M0,160 Q80,80 200,30 L200,80 Q100,120 0,200 Z', '#c8b8f0', 'opacity=".3"') + Pa('M0,170 Q90,100 200,50 L200,64 Q100,110 0,186 Z', '#ffffff', 'opacity=".3"') + ''.join(Ci((k * 47) % 200, (k * 89) % 200, 1.2, '#ffffff') for k in range(80)) + R(0, 170, 200, 30, '#141a2a') + pine(40, 190, .4) + pine(170, 190, .5), False)
S_('comet', space_bg() + comet_(140, 70, 1.2, 25), False)
S_('satellite', space_bg() + earth_(60, 160, 50) + satellite_(120, 70, 1.0), False)
S_('orbit', space_bg() + Ci(100, 100, 16, '#f3c234') + ''.join(E(100, 100, r_, r_ * .5, 'none', 'stroke="#5d6a9a" stroke-width="1.5"') for r_ in (36, 60, 84)) + earth_(160, 100 + 30, 10) + planet(64, 100 - 18, 7, '#e08a5a') + planet(100 + 84 * .7, 100 - 84 * .5 * .7, 8, '#c8502a') + Pa('M160,120 l-6,-6 l2,10 Z', '#ffffff'), False)

# ================= 太空 2 =================
S_('full-moon', R(0, 0, 200, 200, '#24304f') + Ci(100, 100, 60, '#f6efe0') + ''.join(Ci(x, y, r_, '#e6dcc4') for x, y, r_ in [(80, 80, 12), (120, 110, 16), (90, 130, 8)]) + R(0, 170, 200, 30, '#1a2238') + ''.join(star(x, y, 3, '#ffffff') for x, y in [(30, 30), (170, 40), (20, 120)]), False)
S_('crescent-moon', R(0, 0, 200, 200, '#24304f') + moon(90, 70, 50, '#f6efe0') + ''.join(star(x, y, 4, '#ffffff') for x, y in [(30, 40), (170, 60), (150, 150), (40, 160)]), False)
S_('shooting-star', R(0, 0, 200, 200, '#24304f') + G(Pa('M0,-6 L-110,-1 L-110,1 L0,6 Z', '#f3e070', 'opacity=".6"') + star(0, 0, 14, '#f3e070'), 'translate(150,60) rotate(30)') + ''.join(star(x, y, 3, '#ffffff') for x, y in [(30, 30), (60, 150), (170, 160)]) + R(0, 170, 200, 30, '#1a2238'), False)
S_('alien', space_bg() + alien_(100, 100, 1.4), False)
S_('spaceship', space_bg() + ufo(100, 90, 1.3), False)
S_('space-station', space_bg() + earth_(160, 170, 40) + G(R(-14, -40, 28, 80, '#c4cbd0', 6) + R(-50, -8, 100, 16, '#a7adb1', 4) + ''.join(R(x, -40, 30, 80, '#3c7fc1') for x in (-90, 60)) + ''.join(L(x + 6 + k * 6, -40, x + 6 + k * 6, 40, '#9fd0ec', 1) for x in (-90, 60) for k in range(4)) + Ci(0, 0, 10, '#d9a33a'), 'translate(100,80) rotate(-15)'), False)
S_('launch', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#a7adb1') + R(140, 30, 10, 140, '#e2463b') + ''.join(L(140, 40 + k * 20, 120, 50 + k * 20, '#e2463b', 3) for k in range(6)) + rocket(100, 100, 1.0) + ''.join(Ci(80 + k * 10, 170 - (k % 2) * 6, 20 - abs(k - 2) * 3, '#e6ecef') for k in range(5)), False)
S_('moon-landing', R(0, 0, 200, 200, SPACE) + earth_(160, 40, 20) + R(0, 140, 200, 60, '#c8c2b4') + ''.join(E(x, y, r_, r_ * .3, '#a8a294') for x, y, r_ in [(40, 170, 16), (150, 160, 12)]) + astro(70, 120, .6) + R(110, 60, 2, 80, '#a7adb1') + R(112, 60, 30, 20, '#3c7fc1') + G(Pa('M-20,0 L20,0 L28,-30 L-28,-30 Z', '#d9a33a') + L(-20, 0, -30, 20, '#a7adb1', 3) + L(20, 0, 30, 20, '#a7adb1', 3), 'translate(160,140)'), False)
S_('jupiter', space_bg() + planet(100, 100, 66, '#d8a878', False, ['#b87a4a', '#f0d0a0', '#c8905a', '#e8c090']) + E(124, 120, 12, 7, '#c0583a'), False)
S_('saturn', space_bg() + planet(100, 100, 40, '#e8c890', True, ['#d0a870', '#f0dcb0']), False)
S_('venus', space_bg() + Ci(100, 100, 56, '#f0c87a') + ''.join(St(f'M{50+k*6},{70+k*20} q40,-10 90,0', '#e0b060', 4) for k in range(4)), False)
S_('solar-eclipse', R(0, 0, 200, 200, '#141a33') + Ci(100, 100, 66, '#f3e070', 'opacity=".3"') + Ci(100, 100, 54, '#f3c234') + Ci(104, 98, 52, '#141a33'), False)
S_('meteor', R(0, 0, 200, 200, '#24304f') + R(0, 160, 200, 40, '#3a3a4a') + G(Pa('M0,-18 Q-60,-14 -130,0 Q-60,14 0,18 Z', '#f08a24', 'opacity=".8"') + Pa('M0,-10 Q-50,-8 -100,0 Q-50,8 0,10 Z', '#f3e070', 'opacity=".9"') + Ci(0, 0, 18, '#8a6a5a') + Ci(-4, -4, 5, '#6a4a3a') + Ci(6, 6, 4, '#6a4a3a'), 'translate(130,110) rotate(35)'), False)
S_('black-hole', space_bg() + E(100, 100, 80, 24, '#f08a24', 'opacity=".6"') + E(100, 100, 66, 18, '#f3e070', 'opacity=".6"') + Ci(100, 100, 34, '#000000') + Pa('M34,100 A66,18 0 0,0 166,100', 'none', 'stroke="#f3e070" stroke-width="10" opacity=".7"'), False)
S_('constellation', R(0, 0, 200, 200, '#24304f') + St('M30,60 L70,40 L110,60 L130,100 L170,90 M110,60 L100,120 L60,150', '#9fd0ec', 1.5, 'opacity=".7"') + ''.join(star(x, y, 6, '#ffffff') for x, y in [(30, 60), (70, 40), (110, 60), (130, 100), (170, 90), (100, 120), (60, 150)]), False)
S_('universe', R(0, 0, 200, 200, '#0e1226') + ''.join(Ci((k * 53) % 200, (k * 71) % 200, 1 + k % 3 * .5, '#ffffff') for k in range(60)) + Ci(60, 60, 30, '#c8a0f0', 'opacity=".25"') + Ci(140, 140, 40, '#9fd0ec', 'opacity=".2"') + planet(150, 50, 12, '#e8c890', True) + earth_(60, 150, 16) + Ci(100, 100, 6, '#f3e070'), False)

# ================= 地球 =================
S_('world', R(10, 40, 180, 110, '#3c8ad4', 6) + Pa('M30,60 Q50,50 70,60 L74,80 Q60,90 64,110 L50,120 Q40,100 30,90 Z', '#5aaa4a') + Pa('M60,110 Q70,110 76,124 L70,146 L62,140 Z', '#5aaa4a') + Pa('M90,56 Q110,50 120,60 L116,74 L100,70 Q94,80 100,96 Q110,110 104,130 L94,124 Q86,100 88,80 Z', '#5aaa4a') + Pa('M118,58 Q150,50 170,64 L166,90 L150,96 L134,80 L124,76 Z', '#5aaa4a') + Pa('M150,114 Q166,112 172,124 L160,132 L148,126 Z', '#5aaa4a') + ''.join(L(10, 40 + k * 22, 190, 40 + k * 22, '#ffffff', .5) for k in range(1, 5)))
S_('land-earth', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 100, '#9ac070') + ''.join(R(0, 120 + k * 20, 200, 4, '#8ab060') for k in range(4)) + Pa('M0,100 Q50,80 100,100 Q150,120 200,96 L200,110 L0,110 Z', '#7aa050'), False)
S_('ocean', R(0, 0, 200, 200, SKY) + R(0, 60, 200, 140, '#1f5a9a') + ''.join(St(f'M{-10+(k%2)*20},{80+k*20} q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', '#3c7fc1', 3) for k in range(6)) + G(Pa('M0,-6 Q30,-20 60,-6 L60,0 L0,0 Z', '#2f3a4a'), 'translate(130,70)') + St('M160,64 Q164,56 170,60', '#2f3a4a', 0), False)
S_('island', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#3c9ad4') + E(100, 130, 70, 20, '#f0d890') + G(R(-4, -60, 8, 60, '#a8703e', 3, 'transform="rotate(10)"') + ''.join(leaf(6, -60, 40, 10, a, '#4a9a3a') for a in (-150, -110, -60, -20, 20)), 'translate(100,124)') + St('M30,150 q10,-4 20,0 M150,160 q10,-4 20,0', '#ffffff', 2), False)
S_('globe', globe_(96, 90, 56))
S_('continent', R(0, 0, 200, 200, '#3c8ad4') + Pa('M40,40 Q70,20 100,40 Q120,60 100,80 Q80,100 90,130 Q70,160 50,130 Q30,100 40,70 Z', '#5aaa4a') + Pa('M120,90 Q150,80 170,100 Q180,130 150,150 Q130,140 120,120 Z', '#5aaa4a', 'opacity=".6"') + St('M40,40 Q70,20 100,40 Q120,60 100,80 Q80,100 90,130 Q70,160 50,130 Q30,100 40,70 Z', '#f3c234', 3, 'stroke-dasharray="6 4"'), False)
S_('volcano', R(0, 0, 200, 200, '#f6d8b8') + volcano_(100, 200, 1.0), False)
S_('earthquake', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#a8703e') + G(building(0, 0, 40, 80, cols=2, rows=4), 'translate(30,72) rotate(-8)') + G(house(0, 0, 50, 40), 'translate(140,150) rotate(6)') + St('M0,170 L40,160 L60,180 L90,156 L110,184 L140,160 L170,176 L200,164', '#2f3437', 4) + ''.join(St(f'M{20+k*60},40 l-6,6 l6,6 l-6,6', '#e2463b', 2) for k in range(3)), False)
S_('north-pole', R(0, 0, 200, 200, '#cfe2f0') + R(0, 130, 200, 70, '#ffffff') + R(96, 40, 8, 110, '#e2463b') + ''.join(R(96, 40 + k * 20, 8, 10, '#ffffff') for k in range(5)) + Ci(100, 36, 8, '#f3c234') + G(E(0, 0, 30, 18, '#ffffff', 'stroke="#c4d4e0" stroke-width="2"') + Ci(26, -12, 12, '#ffffff', 'stroke="#c4d4e0" stroke-width="2"') + Ci(34, -14, 2, '#2f3437') + Ci(38, -10, 2, '#2f3437'), 'translate(150,150)') + T(100, 26, 'N', 0, '#000'), False)
S_('south-pole', R(0, 0, 200, 200, '#cfe2f0') + R(0, 130, 200, 70, '#ffffff') + ''.join(G(E(0, 0, 14, 22, '#2f3437') + E(0, 4, 9, 16, '#ffffff') + Ci(0, -24, 10, '#2f3437') + Ci(-3, -26, 2, '#ffffff') + Ci(3, -26, 2, '#ffffff') + Pa('M-2,-20 L2,-20 L0,-16 Z', '#f08a24') + E(-6, 22, 6, 3, '#f08a24') + E(6, 22, 6, 3, '#f08a24'), f'translate({50+k*50},{150-(k%2)*6})') for k in range(3)), False)
S_('equator', R(0, 0, 200, 200, '#f6efe0') + earth_(100, 100, 70) + L(20, 100, 180, 100, '#e2463b', 4) + St('M30,100 Q100,124 170,100', '#e2463b', 0), False)
S_('glacier', R(0, 0, 200, 200, '#cfe2f0') + Pa('M0,60 L60,40 L120,70 L200,50 L200,140 L0,150 Z', '#dff1fb') + Pa('M0,100 L200,90 L200,140 L0,150 Z', '#9fd0ec') + ''.join(L(20 + k * 30, 100, 30 + k * 30, 140, '#ffffff', 2) for k in range(6)) + R(0, 150, 200, 50, '#3c7fc1'), False)
S_('tsunami', R(0, 0, 200, 200, '#9ab0c8') + Pa('M0,200 L0,100 Q30,20 100,30 Q160,40 150,90 Q130,70 110,90 Q100,110 120,120 L200,130 L200,200 Z', '#1f5a9a') + Pa('M100,30 Q160,40 150,90 Q140,70 120,74 Q130,50 100,30 Z', '#ffffff') + house(170, 180, 30, 24) + house(140, 186, 24, 20), False)
S_('atmosphere', space_bg() + Ci(100, 160, 110, '#9fd0ec', 'opacity=".35"') + Ci(100, 160, 96, '#9fd0ec', 'opacity=".35"') + Ci(100, 160, 84, '#3c8ad4') + Pa('M40,120 Q80,90 120,110 Q100,140 60,140 Z', '#5aaa4a') + cloud_(140, 100, .3), False)
S_('hemisphere', R(0, 0, 200, 200, '#f6efe0') + earth_(100, 100, 70) + Pa('M30,100 A70,70 0 0,0 170,100 Z', '#f6efe0', 'opacity=".75"') + L(22, 100, 178, 100, '#e2463b', 4) + St('M30,100 A70,70 0 0,1 170,100', '#f3c234', 5), False)
S_('lava', R(0, 0, 200, 200, '#3a2a2a') + Pa('M0,100 Q50,80 100,110 Q150,140 200,110 L200,200 L0,200 Z', '#e2463b') + Pa('M0,130 Q60,110 110,140 Q160,170 200,150 L200,200 L0,200 Z', '#f08a24') + Pa('M20,170 Q80,150 130,176 L200,180 L200,200 L0,200 Z', '#f3c234') + ''.join(Ci(30 + k * 40, 90 - (k % 2) * 20, 6, '#f08a24') for k in range(4)) + Pa('M0,100 L40,60 L80,90 L0,90 Z', '#2a1a1a'), False)

# ================= 地理 1 =================
S_('mountain', mountain_bg(), False)
S_('river', R(0, 0, 200, 200, '#9ac070') + Pa('M80,0 Q60,60 100,100 Q140,140 110,200 L150,200 Q170,140 130,96 Q96,60 110,0 Z', '#5aa1d4') + St('M90,30 Q80,60 104,90', '#9fd0ec', 2) + tree(30, 70, .5) + tree(170, 60, .5) + tree(40, 160, .5), False)
S_('lake', R(0, 0, 200, 200, SKY) + Pa('M0,110 L60,60 L110,100 L160,50 L200,90 L200,120 L0,120 Z', '#7a9a8a') + R(0, 116, 200, 84, '#9ac070') + E(100, 150, 80, 30, '#5aa1d4') + E(80, 146, 30, 6, '#9fd0ec', 'opacity=".6"') + pine(20, 150, .4) + pine(184, 160, .5), False)
S_('hill', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,140 Q60,60 120,120 Q160,90 200,130 L200,200 Z', '#7ab050') + Pa('M0,200 L0,170 Q80,130 200,170 L200,200 Z', '#9ac070') + tree(70, 96, .4) + sun(160, 40, 14), False)
S_('forest', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#5a8a3a') + ''.join(pine(10 + k * 26, 140 + (k % 2) * 20, .7) for k in range(8)) + ''.join(pine(20 + k * 30, 196, .9) for k in range(7)), False)
S_('desert', R(0, 0, 200, 200, '#fbe0a0') + sun(160, 40, 20, '#f3a234') + Pa('M0,120 Q50,90 100,120 Q150,140 200,110 L200,200 L0,200 Z', '#f0c870') + Pa('M0,160 Q60,130 120,160 Q160,180 200,150 L200,200 L0,200 Z', '#e0b060') + G(R(-6, -50, 12, 50, '#4a8a3a', 6) + R(-20, -36, 8, 22, '#4a8a3a', 4) + R(-20, -20, 18, 7, '#4a8a3a', 3) + R(12, -40, 8, 20, '#4a8a3a', 4) + R(4, -26, 16, 7, '#4a8a3a', 3), 'translate(60,150)'), False)
S_('valley', R(0, 0, 200, 200, SKY) + Pa('M0,0 L0,200 L80,200 Q90,140 70,40 Z', '#7a8a6a') + Pa('M200,0 L200,200 L120,200 Q110,140 130,40 Z', '#7a8a6a') + Pa('M70,40 Q90,140 80,200 L120,200 Q110,140 130,40 Z', '#9ac070') + St('M100,60 Q96,130 100,200', '#5aa1d4', 6), False)
S_('waterfall', R(0, 0, 200, 200, SKY) + Pa('M0,40 L60,40 L60,200 L0,200 Z', '#7a8a6a') + Pa('M140,40 L200,40 L200,200 L140,200 Z', '#7a8a6a') + R(60, 40, 80, 120, '#9fd0ec') + ''.join(L(66 + k * 12, 40, 66 + k * 12, 160, '#ffffff', 2) for k in range(7)) + E(100, 166, 70, 18, '#5aa1d4') + ''.join(Ci(70 + k * 14, 160, 8, '#ffffff', 'opacity=".8"') for k in range(5)) + R(0, 30, 200, 14, '#5a8a3a'), False)
S_('cave', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#9ac070') + cave_(100, 176, 1.0), False)
S_('cliff', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#3c9ad4') + Pa('M0,40 L110,40 L120,60 L104,90 L124,120 L110,160 L0,160 Z', '#8a7a6a') + R(0, 34, 112, 10, '#7ab050') + fig(40, 36, 'man', s=.15) + St('M140,170 q10,-4 20,0', '#ffffff', 2), False)
S_('peak', R(0, 0, 200, 200, SKY) + Pa('M0,200 L100,30 L200,200 Z', '#7a8a9a') + Pa('M100,30 L124,70 L110,66 L100,76 L88,66 L76,70 Z', '#ffffff') + R(98, 10, 3, 24, '#5d6469') + Pa('M101,10 L120,16 L101,22 Z', '#e2463b'), False)
S_('rainforest', R(0, 0, 200, 200, '#3a6a3a') + ''.join(Ci((k * 47) % 200, (k * 29) % 120, 24 + k % 3 * 6, ['#2f6a3a', '#4a8a3a', '#3c7a2c'][k % 3]) for k in range(18)) + ''.join(R(20 + k * 44, 90, 10, 110, '#6a4a2a') for k in range(4)) + ''.join(St(f'M{30+k*44},90 Q{40+k*44},140 {26+k*44},180', '#5aaa3a', 3) for k in range(4)) + G(Pa('M0,0 Q-10,-10 -16,0 Q-10,6 0,0 Q10,-10 16,0 Q10,6 0,0 Z', '#e2463b'), 'translate(150,140)') + R(0, 180, 200, 20, '#2f4a2a'), False)
S_('canyon', R(0, 0, 200, 200, SKY) + Pa('M0,50 L60,50 L70,90 L60,120 L80,200 L0,200 Z', '#c8603a') + Pa('M200,40 L140,40 L130,80 L144,120 L120,200 L200,200 Z', '#c8603a') + ''.join(L(0, 70 + k * 30, 70, 70 + k * 30, '#a8482a', 3) for k in range(4)) + ''.join(L(130, 60 + k * 30, 200, 60 + k * 30, '#a8482a', 3) for k in range(4)) + Pa('M80,200 Q100,170 120,200 Z', '#5aa1d4'), False)
S_('plain', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 100, '#9ac070') + ''.join(L(0, 110 + k * 16, 200, 110 + k * 16, '#8ab060', 2) for k in range(6)) + tree(160, 110, .3) + sun(40, 40, 14), False)
S_('grassland', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 100, '#8ab040') + ''.join(St(f'M{(k*13)%200},{200-(k%5)*16} l-3,-14 M{(k*13)%200},{200-(k%5)*16} l3,-14', '#6a9a30', 2) for k in range(60)) + ''.join(G(E(0, 0, 14, 8, '#ffffff') + Ci(12, -4, 5, '#ffffff'), f'translate({60+k*40},{120+(k%2)*10})') for k in range(3)), False)
S_('wetland', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#5aa1d4') + ''.join(E(30 + k * 50, 140 + (k % 2) * 30, 30, 10, '#7ab050') for k in range(4)) + ''.join(St(f'M{20+k*22},{150+(k%3)*10} l0,-36', '#7a8a3a', 3) + E(20 + k * 22, 112 + (k % 3) * 10, 3, 9, '#8a5a35') for k in range(8)) + G(E(0, 0, 14, 8, '#ffffff') + St('M10,-4 Q16,-24 24,-28', '#ffffff', 3) + Pa('M24,-28 l10,2 l-10,2 Z', '#f08a24') + L(-4, 8, -4, 26, '#2f3437', 1.5), 'translate(150,120)'), False)

# ================= 地理 2 =================
S_('north', compass_rose(100, 100, 50, 'N'))
S_('south', compass_rose(100, 100, 50, 'S'))
S_('east', compass_rose(100, 100, 50, 'E'))
S_('west', compass_rose(100, 100, 50, 'W'))
S_('village', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#9ac070') + house(40, 150, 50, 36, '#f4e6c8', '#5d6469') + house(110, 140, 46, 32, '#f4e6c8', '#8a5a35') + house(170, 160, 40, 30, '#f4e6c8', '#5d6469') + tree(80, 170, .4) + St('M0,190 Q100,160 200,190', '#c8a070', 8) + Pa('M0,120 L50,80 L100,120 Z', '#7a9a7a'), False)
S_('countryside', R(0, 0, 200, 200, SKY) + Pa('M0,120 Q60,90 120,110 Q170,90 200,110 L200,200 L0,200 Z', '#9ac070') + ''.join(R(0, 130 + k * 16, 200, 8, ['#e8c060', '#7ab050'][k % 2]) for k in range(5)) + barn_(150, 130, 40) + tree(40, 120, .5) + sun(40, 40, 14), False)
S_('capital', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + building(10, 80, 40, 90) + building(150, 70, 44, 100) + R(60, 110, 80, 60, '#e6dcc8') + Pa('M56,110 L100,80 L144,110 Z', '#c4bcae') + ''.join(R(66 + k * 18, 120, 8, 50, '#f4f1ea') for k in range(4)) + E(100, 70, 20, 16, '#c4bcae') + star(100, 46, 12, '#e2463b'), False)
S_('province', R(0, 0, 200, 200, '#cfe8f6') + Pa('M30,60 L80,30 L140,40 L170,90 L150,150 L90,170 L40,140 Z', '#f4e6c8', 'stroke="#a7adb1" stroke-width="2"') + Pa('M80,30 L140,40 L120,90 L70,80 Z', '#f3c234') + St('M70,80 L80,30 M120,90 L140,40 M70,80 L40,140 M120,90 L150,150 M70,80 L120,90 L90,170', '#a7adb1', 2) + star(100, 60, 6, '#e2463b'), False)
S_('border', R(0, 0, 200, 200, '#9ac070') + R(100, 0, 100, 200, '#c8b880') + St('M100,0 L100,200', '#e2463b', 4, 'stroke-dasharray="10 6"') + ''.join(R(96, 20 + k * 50, 8, 30, '#ffffff', 2) for k in range(0)) + G(R(-3, 0, 6, 60, '#5d6469') + R(0, 0, 40, 26, '#3c7fc1'), 'translate(60,40)') + G(R(-3, 0, 6, 60, '#5d6469') + R(0, 0, 40, 26, '#e2463b'), 'translate(140,40)') + R(70, 140, 60, 8, '#e2463b') + R(70, 140, 12, 8, '#ffffff'), False)
S_('population', ''.join(G(Ci(0, -14, 7, SK) + Pa('M-10,10 Q0,-8 10,10 Z', ['#3c7fc1', '#e2463b', '#5ba644', '#f3c234', '#7a4fa0'][k % 5]), f'translate({20+(k%9)*20},{40+(k//9)*30})') for k in range(36)) + R(20, 170, 160, 10, '#c4cbd0', 5) + R(20, 170, 120, 10, '#3c7fc1', 5))
S_('region', R(0, 0, 200, 200, '#cfe8f6') + Pa('M20,40 L180,30 L190,170 L20,180 Z', '#f4e6c8') + Pa('M20,40 L100,36 L110,100 L20,110 Z', '#9ac070') + Pa('M100,36 L180,30 L184,100 L110,100 Z', '#f3c234') + Pa('M20,110 L110,100 L100,176 L20,180 Z', '#ef8fa4') + Pa('M110,100 L184,100 L190,170 L100,176 Z', '#9fd0ec') + St('M20,40 L180,30 L190,170 L20,180 Z', '#5d6469', 2), False)
S_('bay', R(0, 0, 200, 200, '#9ac070') + Pa('M0,200 L0,140 Q20,60 100,60 Q180,60 200,140 L200,200 Z', '#3c8ad4') + Pa('M0,200 L0,180 Q100,170 200,180 L200,200 Z', '#2f6aa0') + sailboat(100, 130, .3) + house(40, 50, 30, 20) + tree(160, 50, .3), False)
S_('stream', R(0, 0, 200, 200, '#9ac070') + St('M60,0 Q120,50 80,100 Q40,150 120,200', '#5aa1d4', 22) + St('M60,0 Q120,50 80,100 Q40,150 120,200', '#9fd0ec', 4, 'stroke-dasharray="10 12"') + ''.join(E(x, y, 8, 5, '#a7adb1') for x, y in [(110, 50), (50, 130), (100, 170)]) + flower(160, 80, 1.0) + flower(30, 60, 1.0, '#f3c234'), False)
S_('swamp', R(0, 0, 200, 200, '#9aa880') + R(0, 100, 200, 100, '#5a7a4a') + ''.join(E(30 + k * 50, 140 + (k % 2) * 30, 24, 8, '#4a6a3a') for k in range(4)) + ''.join(G(R(-4, -80, 8, 80, '#5a4a3a') + St('M0,-80 Q-20,-60 -30,-30 M0,-70 Q20,-50 30,-30', '#4a5a3a', 3), f'translate({30+k*70},{110})') for k in range(3)) + ''.join(Ci(40 + k * 40, 170 + (k % 2) * 6, 4, '#8a9a6a', 'opacity=".8"') for k in range(4)), False)
S_('oasis', R(0, 0, 200, 200, '#fbe0a0') + Pa('M0,110 Q100,90 200,110 L200,200 L0,200 Z', '#f0c870') + E(100, 150, 50, 16, '#5aa1d4') + ''.join(G(R(-4, -70, 8, 70, '#a8703e', 3) + ''.join(leaf(0, -70, 34, 9, a, '#4a9a3a') for a in (-160, -110, -60, -20)), f'translate({x},{140})') for x in (50, 150)) + sun(170, 30, 14, '#f3a234'), False)
S_('peninsula', R(0, 0, 200, 200, '#3c8ad4') + Pa('M0,0 L200,0 L200,60 Q140,60 120,90 Q110,140 90,170 Q70,180 70,150 Q80,110 60,70 Q40,50 0,50 Z', '#9ac070') + ''.join(St(f'M{20+k*50},{120+(k%2)*40} q10,-4 20,0', '#9fd0ec', 2) for k in range(4)), False)

dump()
