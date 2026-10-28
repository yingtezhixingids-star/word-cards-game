from kit5 import *

def suitcase_(x, base, w, h, col='#e2463b'):
    return R(x - w * .2, base - h - 14, w * .4, 18, 'none', 6, f'stroke="{shade(col,-.3)}" stroke-width="5"') + R(x - w / 2, base - h, w, h, col, 8) + ''.join(R(x - w / 2 + w * k / 4 - 3, base - h, 6, h, shade(col, -.12)) for k in (1, 3)) + Ci(x - w * .3, base + 4, 6, '#2f3437') + Ci(x + w * .3, base + 4, 6, '#2f3437')
def backpack_(x, y, s=1, col='#3c7fc1'):
    return G(R(-30, -40, 60, 80, col, 16) + R(-22, 0, 44, 30, shade(col, -.12), 8) + R(-14, -50, 28, 14, 'none', 6, f'stroke="{shade(col,-.3)}" stroke-width="4"'), f'translate({x},{y}) scale({s})')
def hotel_room(beds=1):
    g = R(0, 0, 200, 200, '#f2ead8') + R(0, 140, 200, 60, '#c8a070') + window_(130, 20, 56, 56)
    if beds == 1:
        g += bed_(70, 180, 76, '#ffffff') + G(Ci(0, -10, 8, '#3c7fc1') + Pa('M-12,14 Q0,-4 12,14 Z', '#3c7fc1'), 'translate(30,30)')
    else:
        g += bed_(100, 184, 170, '#ffffff', 2) + ''.join(G(Ci(0, -10, 8, '#3c7fc1') + Pa('M-12,14 Q0,-4 12,14 Z', '#3c7fc1'), f'translate({24+k*24},30)') for k in range(2))
    return g + lamp_(176, 130, 50)
def key_card(x, y, s=1, rot=0):
    return G(R(-50, -32, 100, 64, '#3c7fc1', 8) + R(-50, -12, 100, 10, '#2f3437') + R(-40, 10, 30, 14, '#f3c234', 3) + Ci(30, 16, 8, '#ffffff', 'opacity=".5"'), f'translate({x},{y}) rotate({rot}) scale({s})')
def bell_desk(x, y, s=1):
    return G(E(0, 0, 18, 5, '#d9a33a') + Pa('M-14,0 Q-14,-18 0,-18 Q14,-18 14,0 Z', '#d9a33a') + Ci(0, -20, 3, '#d9a33a'), f'translate({x},{y}) scale({s})')
def landmark_tower(x, base, s=1):
    return G(Pa('M-30,0 L-8,-120 L8,-120 L30,0 L18,0 L0,-60 L-18,0 Z', '#8a6a4a') + R(-22, -60, 44, 6, '#8a6a4a') + R(-14, -96, 28, 5, '#8a6a4a') + L(0, -120, 0, -140, '#8a6a4a', 3), f'translate({x},{base}) scale({s})')
def pagoda(x, base, s=1):
    g = ''
    for k in range(4):
        w = 60 - k * 10
        y = -k * 30
        g += R(-w / 2 + 6, y - 22, w - 12, 22, '#c0302a') + Pa(f'M{-w/2-10},{y-22} L{w/2+10},{y-22} L{w/2-4},{y-34} L{-w/2+4},{y-34} Z', '#3a4a3a')
    return G(g + L(0, -120, 0, -140, '#d9a33a', 3), f'translate({x},{base}) scale({s})')
def binoculars(x, y, s=1):
    return G(R(-34, -20, 28, 50, '#2f3437', 10) + R(6, -20, 28, 50, '#2f3437', 10) + R(-8, -10, 16, 16, '#5d6469', 3) + Ci(-20, 30, 12, '#3c7fc1') + Ci(20, 30, 12, '#3c7fc1') + hi(-24, 26, 4, 3, .6) + hi(16, 26, 4, 3, .6), f'translate({x},{y}) scale({s})')
def compass_(x, y, r):
    return Ci(x, y, r, '#d9a33a') + Ci(x, y, r * .85, '#ffffff') + Pa(f'M{x},{y-r*.7} L{x+r*.15},{y} L{x-r*.15},{y} Z', '#e2463b') + Pa(f'M{x},{y+r*.7} L{x+r*.15},{y} L{x-r*.15},{y} Z', '#5d6469') + T(x, y - r * .45, 'N', r * .22, '#2f3437', 900) + Ci(x, y, 4, '#2f3437') + Ci(x, y - r - 6, 6, 'none', 'stroke="#d9a33a" stroke-width="3"')
def tent_(x, base, w, col='#f08a24'):
    h = w * .7
    return Pa(f'M{x-w/2},{base} L{x},{base-h} L{x+w/2},{base} Z', col) + Pa(f'M{x},{base-h} L{x+w*.12},{base} L{x-w*.12},{base} Z', shade(col, -.3)) + L(x, base - h, x, base - h - 10, '#5d6469', 2) + L(x - w / 2, base, x - w / 2 - 12, base + 2, '#5d6469', 1.5) + L(x + w / 2, base, x + w / 2 + 12, base + 2, '#5d6469', 1.5)
def campfire(x, base, s=1):
    return G(R(-30, -8, 60, 10, '#8a5a35', 4, 'transform="rotate(15)"') + R(-30, -8, 60, 10, '#6a3a20', 4, 'transform="rotate(-15)"') + flame(0, -6, .9), f'translate({x},{base}) scale({s})')
def night_bg(y=150):
    return R(0, 0, 200, 200, '#24304f') + R(0, y, 200, 200 - y, '#2f4a3a') + ''.join(star(x, yy, 3, '#ffffff') for x, yy in [(20, 30), (60, 20), (120, 40), (170, 25), (90, 70)]) + moon(160, 60, 14)
def beach_bg(sea=100, sand=140):
    return R(0, 0, 200, 200, SKY) + R(0, sea, 200, sand - sea, '#3c9ad4') + St(f'M0,{sand} q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', '#ffffff', 3) + R(0, sand, 200, 200 - sand, '#f0d890')
def beach_umb(x, base, s=1, c1='#e2463b', c2='#ffffff'):
    g = R(-2, -110, 4, 110, '#a7adb1')
    for k in range(6):
        a0 = math.pi + k * math.pi / 6; a1 = a0 + math.pi / 6
        g += Pa(f'M0,-110 L{60*math.cos(a0)},{-110+30*math.sin(a0)+30} L{60*math.cos(a1)},{-110+30*math.sin(a1)+30} Z', c1 if k % 2 else c2)
    return G(g, f'translate({x},{base}) scale({s})')
def shell_(x, y, s=1, col='#f6c8b0'):
    return G(Pa('M0,20 L-30,-10 Q-20,-34 0,-36 Q20,-34 30,-10 Z', col) + ''.join(L(0, 20, -26 + k * 10.4, -18 + abs(k - 2.5) * -3, shade(col, -.2), 2) for k in range(6)) + R(-8, 16, 16, 8, shade(col, -.1), 3), f'translate({x},{y}) scale({s})')
def deck_chair(x, base, s=1, col='#3c7fc1'):
    return G(Pa('M-30,0 L-10,-50 L0,-50 L-20,0 Z', '#c8a070') + Pa('M10,0 L-14,-46 L-4,-46 L20,0 Z', '#c8a070') + Pa('M-10,-50 L30,-20 L30,-10 L-14,-40 Z', col) + ''.join(R(-6 + k * 8, -46 + k * 6, 6, 30, ['#ffffff', col][k % 2], 0, 'transform="rotate(-50)"') for k in range(0)), f'translate({x},{base}) scale({s})')
def lounger(x, base, s=1, col='#ffffff'):
    return G(Pa('M-60,-10 L40,-10 L70,-40 L76,-34 L48,-4 L-60,-4 Z', col, 'stroke="#c4cbd0" stroke-width="2"') + L(-50, -4, -54, 10, '#a7adb1', 3) + L(30, -4, 34, 10, '#a7adb1', 3), f'translate({x},{base}) scale({s})')
def flipflop(x, y, s=1, rot=0, col='#3c7fc1'):
    return G(E(0, 0, 18, 40, col) + St('M0,-24 L-14,6 M0,-24 L14,6', '#f3c234', 4) + Ci(0, -24, 3, '#f3c234'), f'translate({x},{y}) rotate({rot}) scale({s})')
def tv_set(x, y, w, h, inner=''):
    return R(x, y, w, h, '#2f3437', 8) + R(x + 6, y + 6, w - 12, h - 12, '#9fd0ec', 3) + '<clipPath id="tvs"><rect x="%s" y="%s" width="%s" height="%s"/></clipPath><g clip-path="url(#tvs)">' % (x + 6, y + 6, w - 12, h - 12) + inner + '</g>' + R(x + w / 2 - 20, y + h, 40, 8, '#5d6469', 2)

# ================= 旅行 =================
S_('travel', R(0, 0, 200, 200, SKY) + jet(120, 50, .8, -10, '#ffffff') + suitcase_(60, 180, 60, 70, '#e2463b') + G(R(-40, -30, 80, 60, '#3c7fc1', 3) + R(-40, -30, 80, 14, '#2f5a9a'), 'translate(150,150) scale(.5)') + Ci(170, 30, 0, '#000'), False)
S_('trip', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#8cc06a') + Pa('M0,140 L50,80 L100,140 Z', '#7a9a7a') + car_side(100, 180, '#f3c234', .8) + R(66, 120, 50, 14, '#c8903a', 3) + St('M20,190 Q100,150 190,170', '#ffffff', 0) + Ci(170, 40, 14, '#f3c234'), False)
S_('vacation', beach_bg() + beach_umb(60, 170, .8) + lounger(130, 180, .8) + Ci(160, 40, 18, '#f3c234') + G(R(-6, -30, 12, 30, '#a7adb1') + Pa('M0,-30 Q-30,-50 -40,-30 M0,-30 Q-30,-60 -10,-60 M0,-30 Q20,-60 40,-46 M0,-30 Q30,-40 40,-20', 'none', 'stroke="#4a9a3a" stroke-width="6"'), 'translate(170,140)'), False)
S_('luggage', suitcase_(70, 180, 70, 100, '#3c7fc1') + suitcase_(140, 180, 56, 70, '#e2463b') + backpack_(150, 80, .6, '#5ba644'))
S_('tour', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, WALK) + pagoda(150, 150, .7) + W(50, 196, .7, '#f08a24', '#3b4a5a', 'cap', '#f08a24', arms='wave') + R(76, 60, 2, 30, '#5d6469') + Pa('M78,60 L96,66 L78,72 Z', '#e2463b') + ''.join(fig(90 + k * 22, 196, ['man', 'woman', 'oldman'][k], s=.4) for k in range(3)), False)
S_('check-out', R(0, 0, 200, 200, '#f2ead8') + R(0, 120, 200, 80, '#c8a070') + R(0, 116, 200, 8, '#8a5a35') + person_bust(140, 80, 22, '#2f3a4a', '#5a3a2a', 'bun') + key_card(60, 150, .6, -10) + arrow(80, 150, 120, 150, '#5ba644', 4) + suitcase_(30, 196, 30, 40) + bell_desk(170, 116, 1.0), False)
S_('key-card', key_card(100, 100, 1.4, -10) + G(R(-16, -30, 32, 50, '#5d6469', 4) + Ci(0, -10, 6, '#5ba644'), 'translate(160,60) scale(.8)'))
S_('single-room', hotel_room(1) + T(150, 120, '', 0), False)
S_('double-room', hotel_room(2), False)
S_('reception', R(0, 0, 200, 200, '#e8dcc8') + R(0, 0, 200, 50, '#c8a070') + ''.join(clock(30 + k * 46, 26, 14, (k * 3 + 1, 0)) for k in range(4)) + person_bust(100, 100, 26, '#2f3a4a', '#5a3a2a', 'bun') + R(10, 136, 180, 64, '#8a5a35', 4) + R(10, 130, 180, 10, '#a8703e', 3) + bell_desk(150, 130, 1.1), False)
S_('breakfast-included', R(0, 0, 200, 200, '#fef3e2') + plate(80, 120, 50) + egg(70, 112, .9, True) + R(90, 104, 30, 16, '#d9a868', 4) + cup(150, 120, 30, 30, '#ffffff', '#c98a3a') + glass(140, 140, 24, 40, '#f3a234', .8) + Ci(160, 50, 22, '#5ba644') + St('M150,50 l7,8 l13,-16', '#ffffff', 5) + R(30, 160, 140, 6, '#c8a070', 3) + T(50, 50, '', 0), False)
S_('guesthouse', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + house(100, 170, 120, 80, '#f6e8c8', '#8a5a35', '#5a3a24', '#f3e070') + flower(40, 170, 1.2) + flower(160, 170, 1.2, '#f3c234') + tree(20, 160, .6) + G(R(-20, -8, 40, 16, '#ffffff', 3), 'translate(100,110)'), False)
S_('travel-agency', R(0, 0, 200, 200, '#e8eef2') + R(10, 20, 80, 60, '#ffffff', 3) + landscape_ if False else R(0, 0, 200, 200, '#e8eef2') + G(R(-40, -30, 80, 60, '#ffffff', 3) + R(-36, -26, 72, 52, SKY) + Pa('M-36,26 L-10,-6 L10,10 L36,-14 L36,26 Z', '#5aa040'), 'translate(60,56)') + G(R(-30, -24, 60, 48, '#ffffff', 3) + R(-26, -20, 52, 40, '#3c9ad4') + R(-26, 6, 52, 14, '#f0d890'), 'translate(150,60)') + R(0, 130, 200, 70, '#c8a070') + person_bust(100, 110, 22, '#3c7fc1') + jet(150, 150, .3, -10, '#ffffff') + G(R(-14, -18, 28, 36, '#ffffff', 2), 'translate(50,160) rotate(-10)'), False)
S_('wake-up-call', R(0, 0, 200, 200, '#ffe2b8') + bed_(90, 190, 140, '#7fb7d8') + bare_head(50, 140, 16, '#3a2a20', 'short') + eyes_closed(50, 140, 16) + G(Pa('M-30,10 L-24,-16 L24,-16 L30,10 Z', '#e2463b') + Pa('M-34,-20 Q-34,-34 -20,-34 L20,-34 Q34,-34 34,-20 L20,-20 L16,-28 L-16,-28 L-20,-20 Z', '#e2463b'), 'translate(160,110)') + ''.join(L(160 + 30 * math.cos(a), 80 + 30 * math.sin(a), 160 + 40 * math.cos(a), 80 + 40 * math.sin(a), '#e2463b', 3) for a in [math.pi * 1.2 + k * .3 for k in range(4)]) + clock(40, 40, 18, (7, 0)), False)
S_('room-service', R(0, 0, 200, 200, '#f2ead8') + R(0, 160, 200, 40, '#c8a070') + R(40, 110, 120, 10, '#ffffff', 2) + R(50, 120, 6, 50, '#a7adb1') + R(144, 120, 6, 50, '#a7adb1') + wheel(53, 172, 6) + wheel(147, 172, 6) + Pa('M60,110 Q60,60 100,60 Q140,60 140,110 Z', '#c4cbd0') + Ci(100, 56, 6, '#a7adb1') + hi(80, 80, 10, 14, .5) + door_(150, 20, 40, 140), False)
S_('itinerary', R(30, 16, 140, 170, '#ffffff', 4, 'stroke="#c4cbd0" stroke-width="2"') + R(30, 16, 140, 26, '#3c7fc1', 4) + ''.join(Ci(52, 64 + k * 32, 8, ['#e2463b', '#f3c234', '#5ba644', '#3c7fc1'][k]) + T(52, 68 + k * 32, str(k + 1), 10, '#ffffff', 900) + R(68, 60 + k * 32, 80 - (k % 2) * 20, 8, '#a7adb1', 3) for k in range(4)) + St('M52,72 L52,152', '#c4cbd0', 2, 'stroke-dasharray="3 3"') + jet(150, 30, .2, 0, '#ffffff'))

# ================= 观光 =================
S_('tourist', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(100, 196, 1.0, '#f3c234', '#3b4a5a', 'cap', '#e2463b', arms='front') + camera_(102, 80, .35) + backpack_(70, 90, 0) + G(R(-14, -10, 28, 20, '#ffffff', 2), 'translate(40,40)'), False)
S_('famous', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + landmark_tower(100, 170, 1.0) + ''.join(star(x, y, 8, '#f3c234') for x, y in [(40, 50), (160, 40), (150, 110)]) + ''.join(camera_(30 + k * 140, 150, .25) for k in range(2)), False)
S_('beautiful', R(0, 0, 200, 200, '#ffd8c0') + Pa('M0,120 L50,60 L90,100 L140,40 L200,110 L200,200 L0,200 Z', '#7a8ac0') + Pa('M140,40 L156,60 L124,60 Z', '#ffffff') + R(0, 140, 200, 60, '#5aa1d4') + Ci(50, 40, 18, '#f3a234') + ''.join(star(x, y, 6, '#ffffff') for x, y in [(100, 20), (180, 30)]) + ''.join(flower(20 + k * 30, 190, 1.0, ['#ef8fa4', '#f3c234'][k % 2]) for k in range(7)), False)
S_('view', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,120 L40,90 L80,110 L130,60 L200,100 L200,200 Z', '#7a9a7a') + Pa('M0,200 L0,160 L60,150 L120,170 L200,150 L200,200 Z', '#5a8a5a') + W(40, 150, .45, '#e2463b', '#3b4a5a', arms='wave') + R(0, 150, 80, 50, '#8a7a6a') + Ci(160, 40, 14, '#f3c234'), False)
S_('crowded', R(0, 0, 200, 200, '#e8eef2') + ''.join(Ci(10 + (k % 10) * 20 + (k // 10 % 2) * 10, 60 + (k // 10) * 26, 10, SK) + Pa(f'M{(k%10)*20+(k//10%2)*10},{58+(k//10)*26} Q{10+(k%10)*20+(k//10%2)*10},{46+(k//10)*26} {20+(k%10)*20+(k//10%2)*10},{58+(k//10)*26} Z', ['#3a2a20', '#5a3a2a', P['grey'], '#2a1a10'][k % 4]) + R((k % 10) * 20 + (k // 10 % 2) * 10, 70 + (k // 10) * 26, 20, 26, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644', '#ef8fa4', '#7a4fa0'][k % 6], 6) for k in range(50)), False)
S_('take-a-picture', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(50, 196, .8, '#3c7fc1', '#3b4a5a', arms='front') + camera_(60, 92, .3) + W(150, 196, .75, '#ef8fa4', '#5d6469', arms='wave', style='long', hair='#5a3a2a') + burst(76, 80, 8, '#f3c234', 8), False)
S_('souvenir', R(0, 0, 200, 200, '#f6efe0') + G(R(-30, -40, 60, 80, '#9fd0ec', 3) + landmark_tower(0, 30, .4), 'translate(60,90) rotate(-8)') + G(Ci(0, 0, 30, '#dff1fb', 'stroke="#c4cbd0" stroke-width="2"') + pagoda(0, 14, .25) + R(-24, 24, 48, 12, '#8a5a35', 3), 'translate(140,90)') + cup(70, 160, 30, 30, '#ffffff') + heart(70, 160, 6) + G(R(-20, -12, 40, 24, '#e2463b', 3), 'translate(150,170) rotate(10)'), False)
S_('selfie', R(0, 0, 200, 200, SKY) + landmark_tower(160, 200, .9) + person_bust(80, 110, 34, '#5ba644', '#5a3a2a', 'long') + arm([(104, 150), (140, 110), (150, 60)], '#5ba644', SK, 12) + phone_(152, 52, 24, 40, '', '#2f3437', '#2f3437'), False)
S_('guidebook', G(R(-56, -76, 112, 152, '#f3c234', 6) + R(-46, -60, 92, 70, '#ffffff', 3) + landmark_tower(0, 6, .4) + R(-40, 24, 80, 10, '#2f3437', 3) + R(-40, 40, 60, 6, '#8a5a35', 3) + R(-56, -76, 12, 152, '#e0a020', 4), 'translate(100,100) rotate(-6)'))
S_('tour-bus', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, ROAD) + G(R(-90, -80, 180, 70, '#e2463b', 10) + R(-90, -100, 180, 24, '#f3c234', 6) + ''.join(R(-80 + k * 30, -70, 22, 22, '#9fd0ec', 3) for k in range(6)) + ''.join(Ci(-74 + k * 30, -90, 5, SK) for k in range(6)) + wheel(-56, -6, 14) + wheel(56, -6, 14), 'translate(100,176)'), False)
S_('tour-group', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(36, 196, .7, '#f08a24', '#3b4a5a', 'cap', '#f08a24', arms='wave') + R(60, 50, 2, 26, '#5d6469') + Pa('M62,50 L80,56 L62,62 Z', '#e2463b') + ''.join(W(80 + (k % 4) * 30, 196 - (k // 4) * 14, .5 - (k // 4) * .06, ['#e2463b', '#3c7fc1', '#5ba644', '#ef8fa4'][k % 4], '#3b4a5a', 'cap', '#f08a24') for k in range(8)), False)
S_('landmark', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, WALK) + landmark_tower(100, 170, 1.1) + G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', '#e2463b') + Ci(0, -34, 6, '#ffffff'), 'translate(150,80)'), False)
S_('attraction', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + Ci(100, 90, 70, 'none', 'stroke="#5d6469" stroke-width="4"') + ''.join(L(100, 90, 100 + 70 * math.cos(a), 90 + 70 * math.sin(a), '#a7adb1', 2) + R(100 + 70 * math.cos(a) - 8, 90 + 70 * math.sin(a), 16, 14, ['#e2463b', '#f3c234', '#3c7fc1', '#5ba644'][k % 4], 3) for k, a in enumerate([j * math.pi / 4 for j in range(8)])) + L(100, 90, 70, 170, '#5d6469', 5) + L(100, 90, 130, 170, '#5d6469', 5), False)
S_('scenery', R(0, 0, 200, 200, '#cfe8f6') + Pa('M0,130 L40,60 L80,110 L120,40 L170,100 L200,80 L200,200 L0,200 Z', '#6a8a9a') + Pa('M120,40 L134,62 L106,62 Z', '#ffffff') + Pa('M40,60 L52,80 L28,80 Z', '#ffffff') + Pa('M0,150 Q100,120 200,150 L200,200 L0,200 Z', '#5aa040') + E(100, 175, 50, 10, '#5aa1d4') + ''.join(pine(10 + k * 40, 170, .4) for k in range(0)) + Ci(170, 30, 12, '#f3c234'), False)
S_('brochure', G(Pa('M-60,-60 L-20,-66 L-20,66 L-60,60 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + Pa('M-20,-66 L20,-60 L20,60 L-20,66 Z', '#f6efe0', 'stroke="#c4cbd0" stroke-width="2"') + Pa('M20,-60 L60,-66 L60,66 L20,60 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + R(-56, -50, 32, 30, SKY) + Pa('M-56,-20 L-44,-36 L-32,-26 L-24,-34 L-24,-20 Z', '#5aa040') + R(-16, -50, 32, 30, '#3c9ad4') + R(24, -50, 32, 30, '#f3a234') + ''.join(R(-54 + j * 40, -10 + k * 10, 28, 4, '#a7adb1', 2) for j in range(3) for k in range(5)), 'translate(100,100)'))
S_('sightseeing', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + pagoda(150, 160, .8) + landmark_tower(40, 160, .5) + W(100, 196, .6, '#f3c234', '#3b4a5a', 'cap', '#e2463b', arms='front') + binoculars(102, 90, .3), False)

# ================= 户外 =================
S_('picnic', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 90, '#8cc06a') + Pa('M20,180 L180,180 L160,120 L40,120 Z', '#e2463b') + ''.join(R(40 + k * 24, 120, 12, 60, '#ffffff', 0, 'opacity=".4"') for k in range(6)) + G(R(-24, -20, 48, 30, '#c8903a', 4) + St('M-16,-20 Q0,-40 16,-20', '#8a5a35', 4), 'translate(80,150)') + apple(130, 150, .5) + glass(140, 130, 14, 24, '#f3a234', .8) + tree(170, 110, .6), False)
S_('hike', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,140 L80,80 L200,140 L200,200 Z', '#7aaa5a') + St('M20,200 Q60,160 100,130 Q130,110 160,120', '#c8a070', 8) + W(90, 170, .6, '#e2463b', '#3b4a5a', 'cap', '#3c7fc1', legs='walk') + backpack_(80, 98, .35, '#3c7fc1') + L(108, 128, 116, 170, '#8a5a35', 3), False)
S_('trail', R(0, 0, 200, 200, SKY) + R(0, 80, 200, 120, '#5a9a3a') + Pa('M80,200 Q100,150 90,120 Q80,100 100,80 L110,80 Q94,100 104,120 Q116,150 120,200 Z', '#c8a070') + ''.join(pine(20 + k * 40, 120 + (k % 2) * 30, .5) for k in range(0)) + pine(30, 140, .6) + pine(170, 150, .6) + G(R(-3, 0, 6, 40, '#8a5a35') + Pa('M3,4 L40,4 L48,12 L40,20 L3,20 Z', '#f3c234'), 'translate(140,90)'), False)
S_('fly-a-kite', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + G(Pa('M0,-40 L28,0 L0,40 L-28,0 Z', '#e2463b') + L(0, -40, 0, 40, '#ffffff', 2) + L(-28, 0, 28, 0, '#ffffff', 2) + St('M0,40 q10,10 0,20 q-10,10 0,20', '#f3c234', 2), 'translate(150,50) rotate(20)') + fig(60, 196, 'boy', s=1.2, arms='up') + St('M74,90 Q120,100 140,86', '#5d6469', 1.5), False)
S_('walking-stick', G(R(-5, -80, 10, 170, '#8a5a35', 4) + Pa('M-5,-80 Q-5,-110 20,-110 Q40,-110 40,-90 L30,-90 Q30,-100 20,-100 Q5,-100 5,-80 Z', '#8a5a35') + R(-6, 84, 12, 8, '#2f3437', 3), 'translate(100,100) rotate(10)'))
S_('bird-watching', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + tree(160, 160, 1.0) + G(E(0, 0, 10, 7, '#e2463b') + Ci(8, -4, 5, '#e2463b') + Pa('M12,-4 l5,1 l-5,2 Z', '#f3c234'), 'translate(160,70)') + W(60, 196, .9, '#7a8a6a', '#5d6469', 'straw', arms='front') + binoculars(66, 64, .3), False)
S_('binoculars', binoculars(100, 90, 1.6))
S_('compass', compass_(100, 104, 66))
S_('sun-hat', E(100, 120, 84, 26, '#e8c870') + Pa('M50,120 Q50,60 100,60 Q150,60 150,120 Z', '#e8c870') + R(52, 100, 96, 14, '#e2463b') + flower(140, 106, 1.0, '#ffffff'))
S_('insect-repellent', R(60, 60, 60, 120, '#5ba644', 8) + R(60, 90, 60, 50, '#ffffff', 2) + leaf(90, 124, 18, 8, -60, '#5ba644') + R(70, 40, 40, 24, '#2f3437', 6) + R(80, 30, 20, 14, '#ffffff', 3) + R(98, 34, 10, 5, '#2f3437', 1) + ''.join(Ci(116 + k * 9, 36 - k * 3 + (k % 2) * 6, 3 + k * .5, '#dfeec8') for k in range(4)) + G(E(0, 0, 8, 6, '#2f3437') + E(-6, -6, 6, 3, '#c4cbd0') + E(6, -6, 6, 3, '#c4cbd0'), 'translate(160,90)') + L(148, 78, 172, 102, '#e2463b', 4) + L(172, 78, 148, 102, '#e2463b', 4))
S_('picnic-blanket', G(R(-70, -50, 140, 100, '#e2463b', 4) + ''.join(R(-70 + k * 28, -50, 14, 100, '#ffffff', 0, 'opacity=".45"') for k in range(5)) + ''.join(R(-70, -50 + k * 25, 140, 12, '#ffffff', 0, 'opacity=".45"') for k in range(4)), 'translate(100,110) skewX(-15)'))
S_('hammock', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + R(10, 40, 14, 130, '#8a5a35') + R(176, 40, 14, 130, '#8a5a35') + Ci(17, 40, 24, '#4a9a3a') + Ci(183, 40, 24, '#4a9a3a') + L(24, 80, 50, 110, '#5d6469', 2) + L(176, 80, 150, 110, '#5d6469', 2) + Pa('M40,110 Q100,160 160,110 Q100,140 40,110 Z', '#f08a24') + lying(60, 118, '#3c7fc1', '#3b4a5a', 'sleep', .55) + zzz(130, 80, .6), False)
S_('boating', water_bg(110) + Pa('M40,140 L160,140 L146,160 L54,160 Z', '#f6efe0') + W(100, 146, .4, '#e2463b', '#3b4a5a', arms='front') + L(60, 130, 30, 170, '#8a5a35', 3) + L(140, 130, 170, 170, '#8a5a35', 3) + tree(170, 110, .5), False)
S_('viewpoint', R(0, 0, 200, 200, SKY) + Pa('M0,200 L0,160 L60,100 L120,160 L200,140 L200,200 Z', '#7a9a7a') + R(10, 80, 80, 12, '#8a5a35') + ''.join(R(14 + k * 18, 92, 4, 30, '#8a5a35') for k in range(5)) + R(10, 120, 80, 6, '#8a5a35') + binoculars(160, 50, .3) + G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', '#e2463b') + Ci(0, -34, 6, '#ffffff'), 'translate(50,70)'), False)
S_('nature-reserve', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#5a9a3a') + ''.join(pine(20 + k * 32, 150 + (k % 2) * 10, .55) for k in range(6)) + G(R(-3, 0, 6, 50, '#8a5a35') + R(-40, -30, 80, 36, '#3c7a2c', 4) + leaf(0, -12, 20, 8, -60, '#ffffff') + G(E(0, 0, 10, 6, '#ffffff') + Ci(8, -4, 4, '#ffffff'), 'translate(-20,-12)'), 'translate(100,120)'), False)
S_('orienteering', R(0, 0, 200, 200, '#9ac070') + G(R(-60, -50, 120, 100, '#ffffff', 3) + St('M-50,-30 Q-20,-50 10,-20 T50,10', '#3c7fc1', 2) + St('M-40,30 Q-10,10 20,30', '#8a5a35', 2) + Ci(-30, -10, 6, 'none', 'stroke="#e2463b" stroke-width="2"') + Ci(30, 20, 6, 'none', 'stroke="#e2463b" stroke-width="2"') + L(-30, -10, 30, 20, '#e2463b', 1.5), 'translate(80,90) rotate(-6)') + compass_(160, 150, 26) + G(R(-14, -14, 28, 28, '#ffffff') + Pa('M-14,-14 L14,14 L-14,14 Z', '#f08a24'), 'translate(160,50)'), False)

# ================= 海滩 =================
S_('beach', beach_bg() + beach_umb(60, 176, .8) + Ci(160, 40, 18, '#f3c234') + shell_(150, 170, .4) + lounger(140, 186, .6), False)
S_('sea', R(0, 0, 200, 200, SKY) + R(0, 80, 200, 120, '#2f7ab0') + ''.join(St(f'M{-10+(k%2)*20},{100+k*22} q20,-8 40,0 t40,0 t40,0 t40,0 t40,0', '#5aa1d4', 3) for k in range(5)) + sailboat(150, 90, .3) + Ci(40, 40, 16, '#f3c234'), False)
S_('sand', R(0, 0, 200, 200, '#f0d890') + ''.join(Ci((k * 37) % 200, (k * 53) % 200, 2, '#d9c070') for k in range(60)) + spade_(70, 120, .5, 30) + bucket_(140, 170, 50, 46, '#e2463b', False) + St('M0,160 Q50,140 100,160 T200,160', '#e0c070', 3), False)
S_('sun', R(0, 0, 200, 200, SKY) + sun(100, 100, 46), False)
S_('waves', R(0, 0, 200, 200, SKY) + Pa('M0,120 Q40,40 90,90 Q110,110 120,90 Q100,60 130,50 Q170,40 200,90 L200,200 L0,200 Z', '#2f7ab0') + Pa('M90,90 Q110,110 120,90 Q100,60 130,50 Q110,70 116,84 Q104,96 90,90 Z', '#ffffff') + St('M0,140 q20,-10 40,0 t40,0 t40,0 t40,0 t40,0', '#9fd0ec', 4), False)
S_('shell', shell_(100, 100, 1.8))
S_('sandcastle', beach_bg(60, 100) + G(R(-50, -40, 100, 40, '#e0c070') + ''.join(R(-50 + k * 20, -48, 10, 8, '#e0c070') for k in range(5)) + R(-60, -80, 30, 80, '#e0c070') + R(30, -80, 30, 80, '#e0c070') + Pa('M-64,-80 L-45,-104 L-26,-80 Z', '#d9b860') + Pa('M26,-80 L45,-104 L64,-80 Z', '#d9b860') + R(-10, -26, 20, 26, '#c8a050', 10) + R(-46, -112, 2, 14, '#5d6469') + Pa('M-44,-112 L-32,-108 L-44,-104 Z', '#e2463b'), 'translate(100,180)'), False)
S_('beach-umbrella', beach_bg() + beach_umb(100, 190, 1.4), False)
S_('beach-towel', beach_bg(60, 90) + G(R(-60, -40, 120, 80, '#3c7fc1', 4) + ''.join(R(-60, -40 + k * 20, 120, 10, '#ffffff', 0, 'opacity=".5"') for k in range(4)), 'translate(100,150) skewX(-20)') + flipflop(170, 110, .5, 10), False)
S_('sunbathe', beach_bg(70, 100) + lounger(100, 170, 1.0) + G(lying(0, 0, '#e2463b', '#e2463b', 'sleep', .7), 'translate(46,134) rotate(-10)') + sun(170, 30, 14) + G(R(-14, -4, 28, 8, '#2f3437', 4), 'translate(54,130)'), False)
S_('sunburn', person_bust(100, 110, 40, '#f3c234', m='o') + Ci(100, 110, 36, '#e2463b', 'opacity=".35"') + Ci(84, 120, 8, '#e2463b', 'opacity=".4"') + Ci(116, 120, 8, '#e2463b', 'opacity=".4"') + sun(170, 30, 14) + ''.join(L(150 - k * 16, 50 + k * 10, 130 - k * 16, 70 + k * 10, '#f3c234', 3) for k in range(3)))
S_('flip-flops', flipflop(70, 110, 1.3, -10, '#3c7fc1') + flipflop(130, 100, 1.3, 10, '#e2463b'))
S_('deck-chair', G(Pa('M-60,60 L-30,-60 L-16,-60 L-46,60 Z', '#c8a070') + Pa('M30,60 L-20,-40 L-8,-40 L44,60 Z', '#c8a070') + Pa('M-30,-60 L40,10 L36,30 L-34,-40 Z', '#3c7fc1') + ''.join(Pa(f'M{-30+k*14},{-60+k*14} L{-26+k*14},{-56+k*14} L{-30+k*14},{-36+k*14} L{-34+k*14},{-40+k*14} Z', '#ffffff') for k in range(0)) + L(-50, 20, 40, 20, '#c8a070', 5), 'translate(100,110)') + St('M70,50 L140,120', '#ffffff', 6))
S_('swimming-trunks', Pa('M40,50 L160,50 L170,170 L110,170 L100,100 L90,170 L30,170 Z', '#3c7fc1') + R(40, 50, 120, 20, '#2f5a9a') + St('M90,60 l-4,24 M110,60 l4,24', '#ffffff', 3) + ''.join(Ci(60 + k * 20, 130 - (k % 2) * 20, 6, '#f3c234') for k in range(5)))
S_('coast', R(0, 0, 200, 200, SKY) + Pa('M0,0 L200,0 L200,200 L120,200 Q80,160 110,120 Q140,90 100,60 Q70,30 90,0 Z', '#2f7ab0') + Pa('M0,200 L120,200 Q80,160 110,120 Q140,90 100,60 Q70,30 90,0 L0,0 Z', '#d9c28a') + Pa('M0,200 L100,200 Q66,160 96,120 Q120,90 86,60 Q60,30 78,0 L0,0 Z', '#7aaa5a') + lighthouse(40, 150, .6) + St('M120,200 Q80,160 110,120 Q140,90 100,60 Q70,30 90,0', '#ffffff', 3), False)
S_('sun-lounger', beach_bg(60, 100) + lounger(100, 170, 1.3, '#ffffff') + G(R(-24, -6, 48, 12, '#f08a24', 4), 'translate(140,124) rotate(-40)'), False)

# ================= 露营 =================
S_('tent', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#8cc06a') + tent_(100, 170, 140, '#f08a24') + pine(20, 160, .6) + pine(180, 160, .6), False)
S_('camp', night_bg() + tent_(70, 170, 90, '#3c7fc1') + campfire(150, 170, .9) + E(150, 170, 40, 10, '#f3a234', 'opacity=".2"'), False)
S_('campfire', night_bg() + campfire(100, 160, 1.6) + E(100, 160, 70, 14, '#f3a234', 'opacity=".25"'), False)
S_('sleeping-bag', R(0, 0, 200, 200, '#2f4a3a') + Pa('M30,140 Q30,80 70,70 L170,70 Q190,70 190,100 L190,150 L30,150 Z', '#e2463b') + R(30, 140, 160, 10, '#c0283a', 4) + L(70, 74, 70, 150, '#c0283a', 3) + bare_head(54, 100, 16, '#3a2a20', 'short') + eyes_closed(54, 100, 16) + zzz(40, 40, .6, '#ffffff'), False)
S_('lantern', G(R(-6, -76, 12, 10, '#5d6469', 3) + St('M-14,-70 Q0,-90 14,-70', '#5d6469', 3) + R(-26, -66, 52, 10, '#2f3437', 3) + R(-22, -56, 44, 80, '#f3e070', 6, 'opacity=".9"') + R(-26, 24, 52, 12, '#2f3437', 3) + flame(0, 10, .4) + L(-22, -56, -22, 24, '#2f3437', 3) + L(22, -56, 22, 24, '#2f3437', 3), 'translate(100,110) scale(1.3)') + Ci(100, 110, 80, '#f3e070', 'opacity=".12"'))
S_('matches', G(R(-50, -30, 100, 60, '#e2463b', 4) + R(-50, -10, 100, 20, '#ffffff') + R(-46, 26, 92, 4, '#8a5a35'), 'translate(80,130)') + ''.join(G(R(-2, -50, 4, 50, '#e8c890') + E(0, -52, 4, 6, '#c0283a'), f'translate({130+k*10},{100}) rotate({-20+k*10})') for k in range(3)) + flame(150, 40, .4))
S_('firewood', ''.join(G(R(-50, -12, 100, 24, '#8a5a35', 12) + E(-50, 0, 8, 12, '#d9a868') + Ci(-50, 0, 4, '#a8703e'), f'translate({100+(k%3-1)*0},{150-k*22}) translate({(k%2)*10-5},0)') for k in range(5)) + G(spade_(0, 0, 0), ''))
S_('thermos', R(70, 50, 60, 130, '#5ba644', 10) + R(70, 70, 60, 6, '#4a8a3a') + R(76, 30, 48, 24, '#c4cbd0', 6) + R(82, 16, 36, 18, '#a7adb1', 4) + hi(80, 110, 6, 30, .4) + cup(160, 160, 30, 26, '#c4cbd0', '#c98a3a') + steam(150, 140, 2, 10))
S_('campsite', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, '#8cc06a') + ''.join(tent_(40 + k * 60, 170 - (k % 2) * 20, 60, ['#f08a24', '#3c7fc1', '#5ba644'][k]) for k in range(3)) + pine(10, 140, .5) + pine(190, 140, .5) + campfire(100, 190, .5), False)
S_('put-up-a-tent', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#8cc06a') + Pa('M60,170 L100,110 L140,170 Z', '#f08a24', 'opacity=".9"') + L(100, 110, 100, 170, '#5d6469', 3) + W(160, 196, .7, '#3c7fc1', '#3b4a5a', arms='front') + hammer_(150, 120, .3, 0) + G(R(-2, 0, 4, 16, '#a7adb1') + Pa('M-6,0 L6,0 L0,-4 Z', '#a7adb1'), 'translate(60,168)'), False)
S_('camping-stove', R(0, 0, 200, 200, '#2f4a3a') + R(60, 120, 80, 40, '#5d6469', 6) + R(50, 110, 100, 10, '#2f3437', 3) + flame(100, 112, .5) + potk(100, 82, 70, 40, '#a7adb1') + steam(92, 50, 3, 10) + Ci(130, 140, 6, '#e2463b'), False)
S_('air-mattress', G(R(-80, -24, 160, 48, '#3c7fc1', 20) + ''.join(L(-60 + k * 24, -20, -60 + k * 24, 20, '#2f5a9a', 3) for k in range(6)) + R(-76, -18, 30, 36, '#5aa1d4', 14) + R(70, -6, 12, 8, '#2f3437', 2), 'translate(100,120) skewX(-10)') + G(R(-10, -20, 20, 40, '#e2463b', 4) + R(-4, -40, 8, 20, '#a7adb1'), 'translate(170,50)'))
S_('pocketknife', G(R(-60, -14, 100, 28, '#e2463b', 12) + R(-20, -6, 16, 12, '#ffffff', 2) + R(-14, -2, 4, 4, '#e2463b') + R(-18, -4, 12, 4, '#e2463b', 0, 'opacity="0"') + Pa('M30,-10 L110,-30 L100,-8 L30,0 Z', '#c4cbd0') + Pa('M-60,-8 L-110,-20 L-104,-4 L-60,0 Z', '#a7adb1'), 'translate(100,110) rotate(-10) scale(.8)'))
S_('caravan', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + G(R(-80, -80, 130, 70, '#ffffff', 16) + R(-80, -40, 130, 10, '#3c7fc1') + R(-60, -66, 30, 20, '#9fd0ec', 4) + R(0, -66, 34, 46, '#c4cbd0', 4) + wheel(-20, -6, 14) + L(50, -20, 80, -20, '#5d6469', 4), 'translate(110,176)') + car_side(30, 170, '#e2463b', 0), False)
S_('tent-peg', ''.join(G(R(-3, -60, 6, 80, '#a7adb1') + St('M0,-60 Q0,-76 16,-76', '#a7adb1', 6) + Pa('M-3,20 L0,34 L3,20 Z', '#a7adb1'), f'translate({60+k*40},{100}) rotate({-15+k*15})') for k in range(3)) + hammer_(150, 160, .4, -40))
S_('trailer-camping', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + car_side(50, 176, '#3c7fc1', .7) + G(R(-40, -60, 80, 50, '#f6efe0', 10) + R(-30, -50, 22, 16, '#9fd0ec', 3) + wheel(0, -6, 10) + L(-40, -16, -60, -16, '#5d6469', 3) + Pa('M40,-50 L70,-30 L70,-10 L40,-10 Z', '#f08a24'), 'translate(140,176)') + campfire(170, 196, .3) + pine(190, 160, .4), False)

dump()
