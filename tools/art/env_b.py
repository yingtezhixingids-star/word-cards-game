from flags import *

def street_map(hl=None):
    g = R(10, 10, 180, 180, '#eef2e6', 6) + ''.join(R(10, 40 + k * 60, 180, 14, '#ffffff') for k in range(3)) + ''.join(R(40 + k * 60, 10, 14, 180, '#ffffff') for k in range(3))
    g += ''.join(R(14 + (k % 3) * 60, 58 + (k // 3) * 60, 22, 18, ['#f4e6c8', '#dff1fb', '#f6d0dc'][k % 3], 2) for k in range(6))
    return g
def person_top(x, y, col='#3c7fc1'):
    return Ci(x, y, 10, SK) + Pa(f'M{x-10},{y-2} Q{x},{y-14} {x+10},{y-2} Z', '#3a2a20') + R(x - 12, y + 10, 24, 20, col, 6)
def arrow_sign(dir_, col='#3c7fc1'):
    pts = {'left': 'M40,100 L90,60 L90,84 L160,84 L160,116 L90,116 L90,140 Z', 'right': 'M160,100 L110,60 L110,84 L40,84 L40,116 L110,116 L110,140 Z'}[dir_]
    return Ci(100, 100, 80, col) + Pa(pts, '#ffffff')
def box_ref(x, y, col='#c8a070', s=1):
    return G(R(-24, -24, 48, 48, col, 4) + R(-24, -10, 48, 6, shade(col, -.15)), f'translate({x},{y}) scale({s})')
def ball_ref(x, y, r=14):
    return Ci(x, y, r, '#e2463b') + hi(x - r * .3, y - r * .3, r * .3, r * .2, .5)
def nat_person(code, kind='man', shirt=None):
    return R(0, 0, 200, 200, '#f6efe0') + flag_at(code, 20, 18, .5) + W(130, 196, .95, shirt or '#3c7fc1', '#3b4a5a', arms='wave' if kind != 'woman' else 'down', style='long' if kind == 'woman' else 'short', hair='#5a3a2a' if kind == 'woman' else '#3a2a20')
def speech_flag(code, txt, col='#3c7fc1'):
    return bubble(100, 80, 150, 100, (60, 150)) + flag_at(code, 40, 40, .3, False) + T(120, 96, txt, 26, col, 900) + person_bust(46, 170, 0 or 20, '#3c7fc1')

# ================= 方向 =================
S_('map', G(Pa('M-80,-60 L-30,-70 L30,-60 L80,-70 L80,60 L30,70 L-30,60 L-80,70 Z', '#f6efe0') + Pa('M-30,-70 L-30,60 L30,70 L30,-60 Z', '#efe6d0') + St('M-70,30 Q-40,-20 0,10 T70,-30', '#e2463b', 3, 'stroke-dasharray="6 4"') + Pa('M60,-40 C52,-50 50,-56 50,-60 A10,10 0 1,1 70,-60 C70,-56 68,-50 60,-40 Z', '#e2463b') + E(-40, 30, 14, 10, '#9fd0ec') + Ci(10, -30, 10, '#9ac070'), 'translate(100,100)'))
S_('here', street_map() + G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', '#e2463b') + Ci(0, -34, 6, '#ffffff'), 'translate(100,108) scale(1.4)') + E(100, 110, 16, 5, '#e2463b', 'opacity=".3"'))
S_('there', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#9ac070') + W(40, 196, .8, '#3c7fc1', '#3b4a5a', arms='wave') + house(160, 140, 40, 30) + St('M70,90 Q120,40 150,90', '#e2463b', 3, 'stroke-dasharray="6 5"') + Pa('M150,92 L142,80 L156,82 Z', '#e2463b'), False)
S_('left', arrow_sign('left', '#3c7fc1'))
S_('right', arrow_sign('right', '#5ba644'))
S_('near', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#9ac070') + W(70, 196, .8, '#3c7fc1', '#3b4a5a') + house(130, 170, 60, 50) + St('M84,180 L104,180', '#e2463b', 3) + St('M84,174 L84,186 M104,174 L104,186', '#e2463b', 3), False)
S_('far', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#9ac070') + W(30, 196, .8, '#3c7fc1', '#3b4a5a') + house(180, 154, 16, 12) + St('M46,180 L176,160', '#e2463b', 3, 'stroke-dasharray="6 5"') + Pa('M176,160 l-12,-2 l4,10 Z', '#e2463b'), False)
S_('next-to', box_ref(70, 120, '#3c7fc1', 1.4) + ball_ref(140, 136, 18) + R(20, 154, 160, 6, '#a7adb1', 3))
S_('opposite', R(0, 0, 200, 200, '#9ac070') + R(0, 80, 200, 40, ROAD) + St('M0,100 L200,100', '#ffffff', 2, 'stroke-dasharray="10 8"') + house(50, 70, 50, 36) + G(storefront(0, 0, 60, 46, '#f4e6c8', '#e2463b'), 'translate(120,124)') + St('M50,76 L150,124', '#e2463b', 2, 'stroke-dasharray="4 4"'), False)
S_('behind', R(0, 150, 200, 50, '#9ac070', 0, 'opacity="0"') + ball_ref(120, 80, 20) + box_ref(100, 120, '#c8a070', 1.8) + St('M150,70 Q170,90 150,110', '#e2463b', 0))
S_('in-front-of', box_ref(100, 100, '#c8a070', 1.8) + ball_ref(100, 150, 22))
S_('between', box_ref(50, 120, '#3c7fc1', 1.2) + box_ref(150, 120, '#3c7fc1', 1.2) + ball_ref(100, 128, 18) + R(10, 150, 180, 6, '#a7adb1', 3))
S_('which-way', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#9ac070') + Pa('M80,200 L92,140 L50,120 L60,114 L100,132 L140,114 L150,120 L108,140 L120,200 Z', WALK) + R(97, 40, 6, 100, '#8a5a35') + Pa('M60,50 L100,50 L100,70 L60,70 L50,60 Z', '#3c7fc1') + Pa('M104,74 L144,74 L154,84 L144,94 L104,94 Z', '#5ba644') + T(100, 26, '?', 30, '#e2463b', 900), False)
S_('directions', street_map() + St('M47,190 L47,107 L107,107 L107,47 L190,47', '#e2463b', 5) + Pa('M190,47 l-12,-8 l0,16 Z', '#e2463b') + Ci(47, 186, 8, '#5ba644'))
S_('distance', R(0, 0, 200, 200, '#f6efe0') + G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', '#3c7fc1') + Ci(0, -34, 6, '#ffffff'), 'translate(30,120)') + G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', '#e2463b') + Ci(0, -34, 6, '#ffffff'), 'translate(170,120)') + L(30, 140, 170, 140, '#2f3437', 3) + St('M30,132 L30,148 M170,132 L170,148', '#2f3437', 3) + T(100, 170, '5 km', 22, '#2f3437', 900), False)
S_('around-the-corner', R(0, 0, 200, 200, '#9ac070') + R(0, 110, 200, 40, ROAD) + R(110, 0, 40, 150, ROAD) + building(10, 20, 90, 84, '#e6dcc8', cols=3, rows=3) + St('M40,130 L120,130 Q130,130 130,120 L130,40', '#e2463b', 4, 'stroke-dasharray="7 5"') + Pa('M130,36 l-8,12 l16,0 Z', '#e2463b') + W(40, 150, .3, '#3c7fc1', '#3b4a5a', legs='walk'), False)

# ================= 国家 =================
for c in ['china', 'america', 'canada', 'uk', 'australia', 'japan', 'korea', 'france', 'germany', 'italy', 'spain', 'russia', 'india', 'thailand', 'singapore', 'new-zealand',
          'brazil', 'mexico', 'egypt', 'greece', 'switzerland', 'netherlands', 'sweden', 'norway', 'portugal', 'ireland', 'turkey-countries2', 'vietnam', 'malaysia', 'indonesia', 'philippines', 'south-africa',
          'argentina', 'chile', 'peru', 'kenya', 'morocco', 'saudi-arabia', 'united-arab-emirates', 'pakistan', 'nepal', 'mongolia', 'cambodia', 'finland', 'denmark', 'poland', 'austria', 'belgium']:
    S_(c, flag_card(c))

# ================= 国籍 1 =================
NAT1 = {'chinese': 'china', 'american': 'america', 'canadian': 'canada', 'british': 'uk', 'australian': 'australia', 'japanese': 'japan', 'korean': 'korea', 'french': 'france', 'german': 'germany', 'italian': 'italy', 'spanish': 'spain', 'russian': 'russia', 'indian': 'india', 'thai': 'thailand'}
SHIRTS = ['#3c7fc1', '#e2463b', '#5ba644', '#f08a24', '#7a4fa0', '#2fa59b', '#ef8fa4']
for k, (nid, code) in enumerate(NAT1.items()):
    S_(nid, nat_person(code, 'woman' if k % 2 else 'man', SHIRTS[k % len(SHIRTS)]), False)
S_('foreigner', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, WALK) + W(110, 196, 1.0, '#f3c234', '#3b4a5a', 'cap', '#3c7fc1', hair='#e8c060') + G(R(-20, -24, 40, 46, '#e2463b', 6) + R(-8, -32, 16, 10, 'none', 3, 'stroke="#5d6469" stroke-width="3"'), 'translate(160,174)') + G(R(-20, -14, 40, 28, '#2f4a7a', 3) + Ci(0, 0, 7, '#d9a33a'), 'translate(50,60) rotate(-10)') + jet(50, 120, .3, -10, '#ffffff'), False)
S_('nationality', G(R(-56, -76, 112, 152, '#7a1a2a', 6) + Ci(0, -20, 26, 'none', 'stroke="#d9a33a" stroke-width="4"') + star(0, -20, 14, '#d9a33a') + R(-36, 20, 72, 8, '#d9a33a', 3) + R(-26, 36, 52, 6, '#d9a33a', 3) + R(-20, 50, 40, 6, '#d9a33a', 3), 'translate(90,104) rotate(-6)') + flag_at('china', 120, 20, .35) + flag_at('france', 130, 70, .3) + flag_at('brazil', 140, 120, .3))

# ================= 国籍 2 =================
S_('english', bubble(100, 80, 160, 110, (60, 150)) + flag_at('uk', 34, 40, .3, False) + T(116, 100, 'ABC', 34, '#c8102e', 900) + person_bust(50, 180, 18, '#3c7fc1'))
S_('language', bubble(60, 60, 90, 60, (60, 110)) + T(60, 72, 'A', 30, '#3c7fc1', 900) + bubble(150, 50, 80, 56, (130, 100)) + T(150, 62, '文', 28, '#e2463b', 900) + bubble(110, 130, 80, 50, (100, 170)) + T(110, 142, 'あ', 26, '#5ba644', 900) + person_bust(100, 196, 0 or 1, '#3c7fc1', '#3a2a20', 'short') if False else bubble(60, 60, 90, 60, (60, 110)) + T(60, 72, 'A', 30, '#3c7fc1', 900) + bubble(150, 50, 80, 56, (130, 100)) + T(150, 62, '文', 28, '#e2463b', 900) + bubble(110, 140, 80, 50, (90, 176)) + T(110, 152, 'あ', 26, '#5ba644', 900) + bubble(40, 150, 60, 44, (40, 184)) + T(40, 160, 'Ж', 22, '#7a4fa0', 900))
S_('mandarin', bubble(100, 80, 160, 110, (60, 150)) + T(100, 100, '你好', 40, '#de2910', 900) + flag_at('china', 150, 150, .25) + person_bust(50, 180, 18, '#e2463b'))
S_('cantonese', bubble(100, 80, 160, 110, (60, 150)) + T(100, 100, '早晨', 40, '#c0283a', 900) + G(Pa('M0,-14 Q10,-4 6,8 Q0,2 -6,8 Q-10,-4 0,-14 Z', '#ffffff'), 'translate(150,160) scale(1.4)') + Ci(150, 160, 22, '#de2910') + G(''.join(Pa(f'M0,0 Q6,-12 0,-18 Q-4,-8 0,0 Z', '#ffffff', f'transform="rotate({k*72})"') for k in range(5)), 'translate(150,160)') + person_bust(50, 180, 18, '#f08a24'))
S_('international', earth_(100, 100, 50) + ''.join(flag_at(c, 100 + 76 * math.cos(a) - 18, 100 + 76 * math.sin(a) - 12, .24) for c, a in zip(['china', 'america', 'france', 'brazil', 'japan', 'india'], [k * math.pi / 3 - math.pi / 2 for k in range(6)])))
NAT2 = {'brazilian': 'brazil', 'mexican': 'mexico', 'egyptian': 'egypt', 'greek': 'greece', 'swiss': 'switzerland', 'dutch': 'netherlands', 'swedish': 'sweden', 'irish': 'ireland', 'turkish': 'turkey-countries2', 'vietnamese': 'vietnam', 'filipino': 'philippines'}
for k, (nid, code) in enumerate(NAT2.items()):
    S_(nid, nat_person(code, 'man' if k % 2 else 'woman', SHIRTS[(k + 3) % len(SHIRTS)]), False)

dump()
