from kit4 import *

def splash(col, obj=''):
    return Pa('M100,30 Q130,20 140,50 Q176,50 166,86 Q190,110 160,130 Q166,170 126,160 Q100,186 76,160 Q36,170 40,130 Q10,110 36,86 Q26,50 62,50 Q72,20 100,30 Z', col) + obj
def check_badge(x, y, r=22, col='#5ba644'):
    return Ci(x, y, r, col) + St(f'M{x-r*.45},{y} l{r*.35},{r*.38} l{r*.6},{-r*.66}', '#ffffff', r * .25)
def x_badge(x, y, r=22, col='#e2463b'):
    return Ci(x, y, r, col) + L(x - r * .4, y - r * .4, x + r * .4, y + r * .4, '#ffffff', r * .25) + L(x + r * .4, y - r * .4, x - r * .4, y + r * .4, '#ffffff', r * .25)
def chair_front(cx, base, col='#c58b54'):
    return R(cx - 30, base - 100, 60, 50, col, 6) + R(cx - 34, base - 54, 68, 14, shade(col, -.1), 4) + R(cx - 30, base - 40, 6, 40, shade(col, -.2)) + R(cx + 24, base - 40, 6, 40, shade(col, -.2))
def sitter(cx, base, shirt='#3c7fc1', mood='smile'):
    return pose((cx, base - 118), (cx, base - 96), (cx, base - 56), arms=[[(cx - 10, base - 92), (cx - 18, base - 66), (cx - 8, base - 56)], [(cx + 10, base - 92), (cx + 18, base - 66), (cx + 8, base - 56)]], legs=[[(cx - 8, base - 56), (cx - 10, base - 52), (cx - 12, base - 6)], [(cx + 8, base - 56), (cx + 10, base - 52), (cx + 12, base - 6)]], shirt=shirt, pants='#3b4a5a', mood=mood, hr=15, tw=30)
def door_scene(open_=True, col='#8a5a35'):
    g = R(0, 0, 200, 200, '#f2ead8') + R(50, 20, 100, 170, '#ffffff') + R(56, 26, 88, 164, SKY if open_ else col)
    if open_:
        g += Pa('M56,26 L30,16 L30,198 L56,190 Z', col) + Ci(38, 110, 4, '#d9a33a') + R(56, 140, 88, 50, '#8cc06a')
    else:
        g += Ci(130, 110, 5, '#d9a33a') + R(64, 40, 72, 50, shade(col, .1), 3) + R(64, 110, 72, 64, shade(col, .1), 3)
    return g
def wave_person(x, ground, shirt='#3c7fc1', kind='short', hair='#3a2a20', s=1.0, mood='smile'):
    return W(x, ground, s, shirt, '#3b4a5a', arms='wave', style=kind, hair=hair, mood=mood)
def heart_eyes(x, y):
    return ''
def snail(x, y, s=1):
    return G(E(0, 14, 40, 10, '#c8b880') + Ci(30, 0, 9, '#c8b880') + L(28, -8, 30, -20, '#c8b880', 3) + L(34, -8, 40, -18, '#c8b880', 3) + Ci(0, 0, 22, '#c8903a') + St('M0,0 m-12,0 a12,12 0 1,1 24,0 a8,8 0 1,1 -16,0', '#a8703e', 3), f'translate({x},{y}) scale({s})')
def clover(x, y, s=1):
    return G(St('M0,0 Q4,30 -6,50', '#3c8a3a', 5) + ''.join(G(Ci(-9, -9, 14, '#4aaa3a') + Ci(9, -9, 14, '#4aaa3a') + Pa('M-21,-4 L0,18 L21,-4 Z', '#4aaa3a'), f'rotate({a}) translate(0,-24)') for a in (0, 90, 180, 270)), f'translate({x},{y}) scale({s})')
def firework(x, y, r, col):
    return ''.join(L(x + r * .3 * math.cos(a), y + r * .3 * math.sin(a), x + r * math.cos(a), y + r * math.sin(a), col, 3) + Ci(x + r * math.cos(a), y + r * math.sin(a), 3, col) for a in [k * math.pi / 6 for k in range(12)])

# ================= 描述 1 =================
S_('big', R(0, 160, 200, 40, '#8cc06a', 0, 'opacity="0"') + G(E(0, 0, 60, 44, '#9aa6ae') + Ci(50, -20, 30, '#9aa6ae') + E(30, -20, 14, 24, '#8a959c') + St('M74,-10 Q90,20 76,46', '#9aa6ae', 12) + ''.join(R(-44 + k * 26, 30, 16, 36, '#9aa6ae', 4) for k in range(4)) + Ci(60, -26, 3, '#2f3437'), 'translate(80,110)') + G(Ci(0, -14, 5, SK) + R(-4, -9, 8, 14, '#e2463b', 2), 'translate(170,176)'))
S_('little', G(E(0, 0, 18, 12, '#a7adb1') + Ci(16, -6, 8, '#a7adb1') + Ci(14, -14, 6, '#ef8fa4') + Ci(20, -6, 2, '#2f3437') + St('M-18,0 q-14,2 -18,-8', '#ef8fa4', 2), 'translate(70,170)') + G(Pa('M0,0 L80,0 Q100,0 100,-20 L100,-40 Q60,-40 40,-70 L0,-70 Z', '#5a3a24'), 'translate(90,180)') + Ci(70, 140, 30, 'none', 'stroke="#e2463b" stroke-width="3" stroke-dasharray="5 4"'))
S_('good', thumbs_up(100, 110, 1.6) + star(40, 50, 14) + star(160, 50, 14) + star(100, 30, 10))
S_('bad', G(thumbs_up(0, 0, 1.6), 'translate(100,100) rotate(180)') + apple(160, 160, .6, '#8a6a3a') + Ci(166, 152, 4, '#5a4a2a') + Ci(40, 50, 18, '#e2463b') + L(32, 42, 48, 58, '#ffffff', 4) + L(48, 42, 32, 58, '#ffffff', 4))
S_('easy', R(30, 40, 140, 70, '#ffffff', 8) + T(100, 90, '1 + 1 = 2', 30, '#3c7fc1', 900) + big_face(100, 150, 30, m='smile') + check_badge(160, 40, 16))
S_('difficult', R(10, 30, 180, 70, '#ffffff', 8) + T(100, 64, '∫ x² dx = ?', 24, '#2f3437', 900) + T(100, 90, '√(a²+b²)', 16, '#5d6469', 800) + big_face(100, 150, 30, m='o', brows='sad') + drop(140, 136, 6) + drop(60, 130, 5))
S_('clean-describe1', plate(100, 110, 70) + ''.join(star(x, y, s_, '#ffffff') + star(x, y, s_ * .6, '#9fd0ec') for x, y, s_ in [(60, 70, 12), (140, 80, 16), (110, 150, 10)]))
S_('dirty', Pa('M60,40 L90,30 Q100,44 110,30 L140,40 L172,74 L150,92 L140,80 L140,176 L60,176 L60,80 L50,92 L28,74 Z', '#f6f1e6') + ''.join(Pa(f'M{x},{y} q{r_},-{r_} {r_*2},0 q{r_},{r_} 0,{r_*2} q-{r_},{r_} -{r_*2},0 q-{r_},-{r_} 0,-{r_*2} Z', '#8a6a3a', 'opacity=".85"') for x, y, r_ in [(70, 90, 8), (110, 120, 10), (84, 150, 6), (120, 64, 5), (96, 104, 4)]) + ''.join(G(E(0, 0, 4, 3, '#2f3437') + E(-3, -3, 3, 2, '#c4cbd0') + E(3, -3, 3, 2, '#c4cbd0'), f'translate({x},{y})') for x, y in [(160, 120), (40, 130), (170, 150)]) + St('M160,120 q-10,-10 -20,0 q-6,10 4,14', '#5d6469', 1, 'stroke-dasharray="2 3"'))
S_('open', door_scene(True), False)
S_('closed', door_scene(False) + R(84, 100, 40, 30, '#e2463b', 3) + L(90, 100, 104, 84, '#5d6469', 2) + L(118, 100, 104, 84, '#5d6469', 2), False)
S_('empty', glass(60, 40, 80, 130, '#bfe0ef', 0) + Ci(150, 50, 0, '#000'))
S_('wet', R(0, 0, 200, 200, '#a8b8c8') + ''.join(L(x, y, x - 6, y + 16, '#5aa1d4', 2) for x, y in [(20, 20), (60, 40), (100, 10), (140, 30), (180, 50), (30, 80), (170, 100), (40, 140), (160, 150)]) + W(100, 194, .95, '#5aa1d4', '#3b4a5a', mood='sad') + ''.join(drop(x, y, 5) for x, y in [(80, 60), (124, 80), (76, 120), (126, 150)]) + E(100, 194, 50, 6, '#5aa1d4', 'opacity=".6"'), False)
S_('dry', R(0, 0, 200, 200, '#f6d890') + R(0, 140, 200, 60, '#e8b860') + ''.join(L(20 + k * 30, 150 + (k % 2) * 16, 34 + k * 30, 170 + (k % 2) * 10, '#b8803a', 2) for k in range(6)) + Ci(150, 50, 28, '#f3a234') + G(R(-4, -40, 8, 60, '#4a8a3a', 4) + R(-24, -20, 8, 30, '#4a8a3a', 4) + R(-24, 4, 24, 8, '#4a8a3a', 3) + R(16, -30, 8, 24, '#4a8a3a', 4) + R(0, -10, 24, 8, '#4a8a3a', 3), 'translate(60,140)'), False)
S_('hard', Pa('M40,150 L60,90 L110,70 L160,96 L170,150 Z', '#8a9196') + Pa('M60,90 L110,70 L120,100 L70,110 Z', '#a7adb1') + hammer_(120, 50, .6, -30) + burst(110, 80, 12, '#f3c234', 8) + ''.join(L(150 + k * 10, 40 + k * 4, 160 + k * 10, 30 + k * 4, '#5d6469', 2) for k in range(2)))
S_('same', apple(60, 100, 1.0) + T(100, 116, '=', 50, '#5d6469', 900) + apple(140, 100, 1.0))
S_('different', apple(56, 100, 1.0) + T(100, 116, '≠', 50, '#e2463b', 900) + G(Pa('M-30,20 Q0,30 30,-20 Q20,10 -30,14 Z', '#f3d040') + St('M30,-20 l4,-6', '#8a6a2a', 3), 'translate(150,100) scale(1.2)'))

# ================= 描述 2 =================
S_('red', splash('#e2463b'))
S_('yellow', splash('#f3c234'))
S_('green-describe2', splash('#5ba644'))
S_('blue', splash('#3c7fc1'))
S_('white', R(0, 0, 200, 200, '#5d6469') + splash('#ffffff'), False)
S_('black', splash('#2f3437'))
S_('pink', splash('#ef8fa4'))
S_('purple', splash('#7a4fa0'))
S_('brown', splash('#8a5a35'))
S_('grey', splash('#9aa1a6'))
S_('round-describe2', Ci(100, 100, 70, '#f08a24') + hi(76, 74, 18, 10, .5, -30) + St('M30,100 Q100,130 170,100', '#d9701a', 3) + St('M100,30 Q74,100 100,170', '#d9701a', 3) + St('M100,30 Q126,100 100,170', '#d9701a', 3))
S_('smooth', E(100, 110, 70, 46, '#9aa6ae') + hi(76, 92, 30, 12, .6, -15) + ''.join(star(x, y, s_, '#ffffff') for x, y, s_ in [(150, 80, 10), (60, 140, 6)]) + St('M30,170 L170,170', '#c4cbd0', 3))
S_('rough', Pa('M30,140 L40,100 L56,96 L64,70 L84,78 L96,56 L116,70 L130,60 L146,80 L160,82 L170,110 L176,140 Z', '#8a7a6a') + ''.join(Ci(40 + (k * 37) % 130, 90 + (k * 23) % 46, 3 + k % 3, '#6a5a4a') for k in range(20)) + R(30, 140, 146, 10, '#6a5a4a', 3))
S_('sharp', G(R(-80, -10, 50, 20, '#2f3437', 4) + Pa('M-30,-12 L80,-12 L60,12 L-30,12 Z', '#c4cbd0') + L(-30, 12, 60, 12, '#ffffff', 2), 'translate(100,100) rotate(-20)') + star(160, 60, 12, '#ffffff') + star(160, 60, 8, '#f3c234') + L(140, 140, 162, 162, '#ffffff', 0) + Pa('M136,138 L164,138 L150,166 Z', '#f3c234', 'opacity="0"'))
S_('noisy', person_bust(100, 120, 32, '#3c7fc1', m='o') + brows_sad(100, 120, 32) + hand(66, 116, .5) + hand(134, 116, .5) + G(Pa('M-40,-14 L20,-40 L20,40 L-40,14 Z', '#e2463b') + R(-56, -16, 18, 32, '#c4cbd0', 4), 'translate(50,40) scale(.6) rotate(20)') + ''.join(St(f'M{70+k*12},{30+k*4} q8,10 0,20', '#e2463b', 3) for k in range(2)) + T(160, 50, '!!', 30, '#e2463b', 900))
S_('interesting', person_bust(100, 120, 32, '#5ba644', m='smile') + open_book(100, 166, .6, '#3c7fc1') + star(40, 40, 12) + star(160, 30, 10) + star(150, 80, 8) + T(60, 90, '!', 30, '#f08a24', 900))

# ================= 短语动词 =================
S_('sit-down', chair_front(100, 190, '#c58b54') + sitter(100, 190) + arrow(160, 40, 160, 110, '#e2463b', 6))
S_('stand-up', chair_front(70, 190, '#c58b54') + W(130, 192, .8, '#3c7fc1', '#3b4a5a', arms='down') + arrow(176, 150, 176, 60, '#5ba644', 6))
S_('come-back', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + house(40, 160, 70, 50) + W(150, 194, .55, '#3c7fc1', '#3b4a5a', legs='walk') + St('M150,90 Q100,50 70,80', '#e2463b', 5, 'stroke-dasharray="8 6"') + Pa('M62,74 L80,70 L72,88 Z', '#e2463b'), False)
S_('go-out', door_scene(True) + W(110, 196, .75, '#3c7fc1', '#3b4a5a', legs='walk') + arrow(130, 60, 180, 60, '#5ba644', 5), False)
S_('look-for', R(0, 0, 200, 200, '#f2ead8') + W(70, 196, .9, '#3c7fc1', '#3b4a5a', arms='front') + Ci(110, 80, 22, 'none', 'stroke="#5d6469" stroke-width="5"') + Ci(110, 80, 18, '#9fd0ec', 'opacity=".4"') + L(96, 96, 80, 112, '#5d6469', 6) + T(160, 60, '?', 40, '#e2463b', 900) + G(R(-14, -8, 28, 16, '#f3c234', 3), 'translate(160,180)'), False)
S_('look-after', R(0, 0, 200, 200, '#f6e8ee') + W(80, 196, 1.0, '#ef8fa4', '#5d6469', style='long', hair='#5a3a2a') + fig(140, 196, 'girl', s=1.1) + arm([(92, 76), (120, 82), (134, 92)], '#ef8fa4', SK, 11) + heart(110, 30, 12), False)
S_('pick-up', R(0, 176, 200, 24, '#d9b07a') + pose((80, 80), (90, 100), (120, 140), arms=[[(94, 104), (110, 140), (124, 170)]], legs=[[(120, 140), (110, 160), (104, 190)], [(122, 140), (138, 160), (140, 190)]], back_arm=[[(90, 104), (104, 140), (116, 168)]], shirt='#3c7fc1', pants='#3b4a5a', hr=15, tw=28) + G(Ci(0, 0, 10, '#e2463b') + hi(-3, -3, 3, 2, .6), 'translate(128,172)') + arrow(160, 170, 160, 110, '#5ba644', 5), False)
S_('put-on', W(100, 194, 1.0, '#ffffff', '#3b4a5a', arms='up', coat='#e2463b') + St('M40,60 Q40,120 70,120', '#5ba644', 4) + Pa('M62,112 L76,122 L60,128 Z', '#5ba644'))
S_('put-away', box_(40, 110, 120, 70, '#c8a070') + Pa('M40,110 L20,80 L60,80 L60,110 Z', '#b8905a') + Pa('M160,110 L180,80 L140,80 L140,110 Z', '#b8905a') + teddy(100, 70, .5) + G(R(-14, -14, 28, 28, '#3c7fc1', 3), 'translate(60,50) rotate(20)') + Ci(150, 50, 12, '#e2463b') + arrow(100, 20, 100, 60, '#5ba644', 5))
S_('find-out', doc_(30, 40, 100, 130, 6) + Ci(110, 100, 34, 'none', 'stroke="#5d6469" stroke-width="7"') + Ci(110, 100, 30, '#9fd0ec', 'opacity=".4"') + L(134, 124, 166, 156, '#5d6469', 10) + bulb(160, 40, 20))
S_('hurry-up', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + W(90, 196, .9, '#e2463b', '#3b4a5a', arms='wave', legs='run', mood='o') + ''.join(L(20, 80 + k * 20, 50, 80 + k * 20, '#a7adb1', 4) for k in range(3)) + clock(160, 50, 26, (8, 58)) + T(160, 100, '!', 0, '#000'), False)
S_('calm-down', R(0, 0, 200, 200, '#dff1fb') + E(100, 186, 70, 10, '#7fc4c0') + pose((100, 66), (100, 88), (100, 140), arms=[[(88, 92), (70, 120), (64, 148)], [(112, 92), (130, 120), (136, 148)]], legs=[[(96, 140), (60, 160), (110, 176)], [(104, 140), (140, 160), (90, 176)]], shirt='#7fc4c0', pants='#5d6469', mood='sleep', hr=16, tw=30) + St('M40,50 q10,-10 20,0 t20,0', '#9fd0ec', 3) + St('M140,50 q10,-10 20,0 t20,0', '#9fd0ec', 3), False)
S_('give-up', R(0, 0, 200, 200, '#e8eef2') + W(80, 196, .95, '#5d6469', '#3b4a5a', arms='wave', mood='sad') + R(124, 20, 4, 70, '#8a5a35') + Pa('M128,22 Q150,16 170,24 L170,56 Q150,50 128,56 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"'), False)
S_('hold-on', person_bust(80, 100, 32, '#3c7fc1') + phone_(52, 96, 16, 34) + G(R(-24, -10, 48, 64, SK, 12) + ''.join(R(-24 + k * 12, -40, 10, 40, SK, 5) for k in range(4)) + R(22, 0, 14, 30, SK, 7, 'transform="rotate(-30 22 0)"'), 'translate(150,90)') + clock(150, 30, 0))
S_('call-back', phone_(80, 100, 76, 140, Ci(80, 70, 18, SK) + Pa('M62,96 Q80,80 98,96 Z', '#3c7fc1') + Ci(66, 130, 10, '#5ba644')) + St('M150,140 Q190,100 150,60', '#3c7fc1', 6) + Pa('M140,56 L160,48 L156,70 Z', '#3c7fc1') + G(Pa('M-12,-4 Q-12,-14 -4,-14 L4,-6 L0,0 Q4,8 10,10 L16,6 L22,14 Q22,22 14,22 Q-12,16 -12,-4 Z', '#5ba644'), 'translate(160,110)'))
S_('run-out-of', G(Pa('M-60,0 A60,60 0 0,1 60,0', 'none', 'stroke="#2f3437" stroke-width="10"') + Pa('M-60,0 A60,60 0 0,1 -42,-42', 'none', 'stroke="#e2463b" stroke-width="10"') + L(0, 0, -50, -14, '#e2463b', 5) + Ci(0, 0, 8, '#2f3437') + T(-56, 22, 'E', 18, '#e2463b', 900) + T(56, 22, 'F', 18, '#2f3437', 900), 'translate(100,100)') + G(R(-14, -20, 28, 36, '#2f3437', 3) + R(-10, -16, 20, 12, '#ffffff') + St('M14,-10 q10,0 10,10 l0,14', '#2f3437', 3), 'translate(100,160) scale(.9)') + x_badge(170, 40, 16))

# ================= 表达 1 =================
S_('hello', R(0, 0, 200, 200, '#fef3e2') + person_bust(100, 100, 40, '#ef8fa4', '#5a3a2a', 'long') + G(hand(0, 0, 1.1, -10, spread=True), 'translate(160,60)') + St('M178,36 q8,6 6,16 M184,26 q12,10 10,26', '#5d6469', 2.5), False)
S_('goodbye', door_scene(True) + W(100, 196, .8, '#3c7fc1', '#3b4a5a', arms='wave') + G(R(-20, -24, 40, 46, '#e2463b', 6) + R(-8, -32, 16, 10, 'none', 3, 'stroke="#5d6469" stroke-width="3"'), 'translate(150,172)'), False)
S_('thank-you', R(0, 0, 200, 200, '#fef3e2') + pose((86, 86), (96, 104), (110, 150), arms=[[(100, 108), (110, 126), (100, 136)]], legs=[[(108, 150), (104, 194)], [(114, 150), (118, 194)]], shirt='#5ba644', pants='#3b4a5a', hr=16, tw=30) + G(box_(0, 0, 40, 34, '#e2463b') + R(16, 0, 8, 34, '#f3c234') + R(0, 12, 40, 8, '#f3c234'), 'translate(94,118) scale(.7)') + heart(150, 50, 14) + heart(176, 80, 8), False)
S_('please', R(0, 0, 200, 200, '#fef3e2') + person_bust(100, 90, 36, '#7fc4c0', m='smile') + G(Pa('M-12,40 L-14,-20 Q-14,-34 -2,-34 L0,40 Z', SK) + Pa('M12,40 L14,-20 Q14,-34 2,-34 L0,40 Z', shade(SK, -.06)), 'translate(100,160)'), False)
S_('sorry', R(0, 0, 200, 200, '#eef0f2') + pose((84, 92), (96, 108), (110, 150), arms=[[(98, 112), (104, 140), (108, 150)]], legs=[[(108, 150), (104, 194)], [(114, 150), (118, 194)]], shirt='#5aa1d4', pants='#3b4a5a', mood='sad', hr=16, tw=30) + G(cup(0, 0, 24, 22, '#ffffff'), 'translate(160,180) rotate(90)') + E(150, 190, 24, 4, '#c98a3a') + drop(60, 70, 6), False)
S_('excuse-me', R(0, 0, 200, 200, '#e8eef2') + fig(40, 196, 'man', s=.8) + fig(160, 196, 'woman', s=.8) + W(100, 196, .82, '#f08a24', '#3b4a5a', arms='wave') + bubble(140, 30, 40, 24, (122, 50)) + T(140, 37, '…', 18, '#5d6469', 900), False)
S_('yes', person_bust(80, 110, 36, '#5ba644') + St('M80,40 l0,-14 M70,44 q10,6 20,0', '#5d6469', 0) + St('M60,40 q20,-20 40,0', '#5d6469', 3) + Pa('M96,36 l6,4 l-8,4 Z', '#5d6469') + St('M60,58 q20,20 40,0', '#5d6469', 0) + check_badge(160, 70, 28))
S_('no', person_bust(80, 110, 36, '#e2463b') + St('M40,50 Q80,30 120,50', '#5d6469', 3) + Pa('M36,44 l8,10 l4,-12 Z', '#5d6469') + Pa('M124,44 l-8,10 l-4,-12 Z', '#5d6469') + x_badge(160, 140, 28))
S_('you-re-welcome', R(0, 0, 200, 200, '#fef3e2') + person_bust(60, 110, 32, '#3c7fc1') + arm([(84, 150), (120, 140), (150, 130)], '#3c7fc1', SK, 14) + Ci(150, 130, 0, '#000') + heart(150, 70, 14) + St('M120,90 q10,-14 20,0 M160,90 q10,-14 20,0', '#f3c234', 0) + ''.join(star(x, y, 6) for x, y in [(130, 50), (176, 100)]), False)
S_('how-are-you', R(0, 0, 200, 200, '#fef3e2') + person_bust(60, 120, 30, '#3c7fc1') + person_bust(150, 130, 26, '#ef8fa4', P['grey'], 'bun') + bubble(70, 46, 70, 44, (64, 84)) + T(70, 58, '?', 30, '#3c7fc1', 900) + big_face(70, 46, 0) , False)
S_('i-m-fine', R(0, 0, 200, 200, '#fef3e2') + person_bust(90, 110, 36, '#5ba644') + thumbs_up(160, 120, .9) + sun(160, 40, 14), False)
S_('nice-to-meet-you', R(0, 0, 200, 200, '#fef3e2') + W(50, 196, .9, '#3c7fc1', '#3b4a5a') + W(150, 196, .9, '#ef8fa4', '#5d6469', style='long', hair='#5a3a2a') + St('M66,80 L100,100 L134,80', 'none', 0) + St('M68,72 L98,100', '#3c7fc1', 10) + St('M132,72 L102,100', '#ef8fa4', 10) + E(100, 100, 10, 8, SK) + heart(100, 30, 10), False)
S_('good-morning', R(0, 0, 200, 200, '#ffe2b8') + R(0, 150, 200, 50, '#8cc06a') + sun(150, 50, 22, '#f3a234') + W(70, 196, .9, '#f3c234', '#3b4a5a', arms='wave') + window_(120, 100, 60, 40), False)
S_('good-night', R(0, 0, 200, 200, '#24304f') + moon(150, 40, 20) + ''.join(star(x, y, 4, '#ffffff') for x, y in [(40, 30), (90, 20), (180, 90)]) + bed_(100, 190, 150, '#7fb7d8') + bare_head(70, 140, 16, '#3a2a20', 'short') + eyes_closed(70, 140, 16) + arm([(84, 150), (100, 120), (110, 100)], '#7fb7d8', SK, 9) + zzz(130, 90, .8, '#ffffff'), False)
S_('see-you-later', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(50, 196, .85, '#3c7fc1', '#3b4a5a', arms='wave') + W(150, 196, .85, '#ef8fa4', '#5d6469', arms='wave', style='long', hair='#5a3a2a') + clock(100, 40, 22, (5, 0)), False)
S_('take-care', R(0, 0, 200, 200, '#fef3e2') + W(70, 196, .95, '#5ba644', '#5d6469', style='grey', hair=P['grey']) + W(130, 196, .95, '#ef8fa4', '#5d6469', style='long', hair='#5a3a2a') + arm([(116, 76), (96, 70), (84, 74)], '#ef8fa4', SK, 11) + heart(100, 26, 14), False)

# ================= 表达 2 =================
S_('i-don-t-understand', person_bust(100, 120, 36, '#3c7fc1', m='o') + brows_sad(100, 120, 36) + T(60, 60, '?', 50, '#e2463b', 900) + T(140, 50, '?', 36, '#f08a24', 900) + T(100, 40, '?', 26, '#3c7fc1', 900))
S_('pardon', person_bust(90, 110, 36, '#7a8a6a', P['grey'], 'grey') + G(Pa('M0,0 Q-10,-30 10,-40 Q30,-30 20,0 Z', SK), 'translate(126,124)') + ''.join(St(f'M{150+k*10},{80-k*6} q8,30 0,60', '#5d6469', 3) for k in range(3)) + T(176, 50, '?', 30, '#e2463b', 900))
S_('please-speak-slowly', person_bust(60, 110, 30, '#3c7fc1') + bubble(140, 60, 90, 50, (100, 100)) + snail(140, 64, .7))
S_('what-s-this', R(0, 0, 200, 200, '#f2ead8') + person_bust(60, 110, 30, '#5ba644') + arm([(84, 150), (120, 140), (140, 130)], '#5ba644', SK, 12) + G(Pa('M0,-20 L20,0 L0,20 L-20,0 Z', '#7a4fa0') + Ci(0, 0, 6, '#f3c234'), 'translate(160,130)') + T(160, 80, '?', 40, '#e2463b', 900), False)
S_('can-you-help-me', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + W(60, 196, .85, '#9a7ab8', '#5d6469', 'oldwoman' and '', mood='sad', style='bun', hair=P['grey']) + box_(20, 120, 40, 40, '#c8a070') + bag_(80, 120, 26, 34, '#e2463b') + W(150, 196, .85, '#5ba644', '#3b4a5a', arms='wave') + bubble(70, 30, 50, 30, (64, 52)) + T(70, 40, '?', 22, '#3c7fc1', 900), False)
S_('i-d-like-this', R(0, 0, 200, 200, '#fef3e2') + R(20, 20, 100, 140, '#ffffff', 6, 'stroke="#8a5a35" stroke-width="4"') + ''.join(R(32, 40 + k * 26, 50, 6, '#a7adb1', 3) + Ci(98, 43 + k * 26, 8, ['#f08a24', '#e2463b', '#5ba644', '#8a5a35'][k]) for k in range(4)) + R(26, 62, 88, 24, 'none', 4, 'stroke="#e2463b" stroke-width="3"') + G(hand_(0, 0, 1.0, 180, '#3c7fc1'), 'translate(150,80)'), False)
S_('wait-a-moment', person_bust(70, 110, 32, '#3c7fc1') + G(R(-24, -10, 48, 64, SK, 12) + ''.join(R(-24 + k * 12, -40, 10, 40, SK, 5) for k in range(4)) + R(22, 0, 14, 30, SK, 7, 'transform="rotate(-30 22 0)"'), 'translate(150,100)') + clock(150, 30, 20, (12, 5)))
S_('of-course', person_bust(80, 110, 36, '#5ba644') + thumbs_up(160, 110, .8) + check_badge(150, 40, 22) + St('M50,40 q30,-20 60,0', '#5d6469', 0))
S_('never-mind', R(0, 0, 200, 200, '#fef3e2') + person_bust(70, 110, 32, '#f08a24') + G(R(-20, -10, 40, 50, SK, 12) + ''.join(R(-20 + k * 10, -36, 9, 34, SK, 4) for k in range(4)), 'translate(140,110) rotate(30)') + St('M160,60 q20,10 20,30 M170,50 q24,14 22,40', '#a7adb1', 3) + G(cup(0, 0, 22, 20, '#ffffff'), 'translate(150,180) rotate(80)') + E(130, 190, 20, 4, '#c98a3a'), False)
S_('that-s-right', person_bust(70, 110, 34, '#3c7fc1') + G(hand_(0, 0, 1.0, -20, '#3c7fc1'), 'translate(140,90)') + check_badge(160, 40, 26))
S_('me-too', R(0, 0, 200, 200, '#fef3e2') + W(60, 196, .9, '#3c7fc1', '#3b4a5a', arms='wave') + W(140, 196, .9, '#ef8fa4', '#5d6469', arms='wave', style='long', hair='#5a3a2a') + T(100, 40, '=', 40, '#5ba644', 900), False)
S_('let-s-go', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + W(60, 196, .8, '#e2463b', '#3b4a5a', arms='wave', legs='walk') + W(110, 196, .7, '#3c7fc1', '#3b4a5a', legs='walk') + W(150, 196, .65, '#f3c234', '#3b4a5a', legs='walk', style='long', hair='#5a3a2a') + arrow(130, 40, 190, 40, '#5ba644', 6), False)
S_('have-a-nice-day', R(0, 0, 200, 200, '#bfe6fa') + sun(150, 50, 26) + G(Ci(0, 0, 0, '#000'), '') + St('M140,52 q10,10 20,0', '#c0703a', 3) + Ci(142, 44, 2.5, '#c0703a') + Ci(158, 44, 2.5, '#c0703a') + R(0, 150, 200, 50, '#8cc06a') + W(60, 194, .85, '#ef8fa4', '#5d6469', arms='wave', style='long', hair='#5a3a2a') + flower(130, 170, 1.4, '#e2463b') + flower(170, 176, 1.2, '#f3c234'), False)
S_('happy-new-year', R(0, 0, 200, 200, '#1f2a4f') + firework(60, 60, 34, '#f3c234') + firework(150, 50, 28, '#ef8fa4') + firework(110, 110, 20, '#7cc05a') + R(40, 150, 120, 40, '#c0283a', 6) + T(100, 180, '2027', 28, '#f3c234', 900) + lantern(20, 20, .6) + lantern(180, 20, .6), False)
S_('good-luck', clover(100, 90, 1.6) + ''.join(star(x, y, 8) for x, y in [(40, 40), (160, 40), (170, 150)]))
S_('help-yourself', R(0, 0, 200, 200, '#fef3e2') + R(0, 130, 200, 70, WOOD) + plate(60, 150, 30) + drumstick(60, 146, .6) + bowl(130, 150, 60, fill='#f6efe0') + apple(170, 120, .5) + person_bust(90, 70, 26, '#ef8fa4', '#5a3a2a', 'bun') + arm([(110, 100), (140, 110), (160, 104)], '#ef8fa4', SK, 11), False)

dump()
