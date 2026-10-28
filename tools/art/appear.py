from kit3 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)

def tshirt(x, y, s, col, collar=None, long_=False):
    sl = 'L36,-18 L30,-4 L22,-8' if not long_ else 'L44,30 L32,34 L22,-4'
    sr = 'L-22,-8 L-30,-4 L-36,-18' if not long_ else 'L-22,-4 L-32,34 L-44,30'
    g = Pa(f'M-16,-30 L16,-30 {sl} L22,30 L-22,30 {sr} Z', col) + Pa('M-9,-30 Q0,-20 9,-30 Z', collar or shade(col, -.2))
    return G(g, f'translate({x},{y}) scale({s})')

def shirt_c(x, y, s, col, tie=None):
    g = Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', col) + Pa('M-12,-32 L0,-18 L12,-32 L4,-34 L0,-28 L-4,-34 Z', '#ffffff') + L(0, -18, 0, 34, shade(col, -.15), 1.5) + ''.join(Ci(2, -10 + k * 10, 1.6, shade(col, -.3)) for k in range(4)) + R(-16, -6, 10, 10, shade(col, -.08), 1)
    if tie: g += Pa('M-3,-22 L3,-22 L5,10 L0,16 L-5,10 Z', tie)
    return G(g, f'translate({x},{y}) scale({s})')

def pants_(x, y, s, col, short=False):
    h = 40 if short else 80
    return G(Pa(f'M-26,-40 L26,-40 L30,{h-40} L6,{h-40} L0,-8 L-6,{h-40} L-30,{h-40} Z', col) + R(-26, -40, 52, 8, shade(col, -.15), 2) + L(0, -32, 0, -14, shade(col, -.25), 1.5), f'translate({x},{y}) scale({s})')

def dress_(x, y, s, col):
    return G(Pa('M-14,-50 L14,-50 L18,-30 L12,-6 L40,50 L-40,50 L-12,-6 L-18,-30 Z', col) + Pa('M-14,-50 L-22,-46 L-18,-30 Z M14,-50 L22,-46 L18,-30 Z', shade(col, -.1)) + R(-13, -8, 26, 6, shade(col, -.2), 2) + St('M-30,46 Q-10,30 -6,0 M30,46 Q10,30 6,0', shade(col, -.12), 1.5), f'translate({x},{y}) scale({s})')

def coat_(x, y, s, col, long_=True):
    h = 70 if long_ else 36
    g = Pa(f'M-22,-34 L22,-34 L44,-20 L46,{h-10} L34,{h-8} L30,0 L28,{h} L-28,{h} L-30,0 L-34,{h-8} L-46,{h-10} L-44,-20 Z', col) + Pa('M-10,-34 L0,-10 L10,-34 Z', '#ffffff') + L(0, -10, 0, h, shade(col, -.2), 2) + ''.join(Ci(6, k * 14, 2.5, shade(col, -.35)) for k in range(int(h / 14) + 1)) + Pa('M-10,-34 L-18,-18 L-4,-10 Z M10,-34 L18,-18 L4,-10 Z', shade(col, -.1))
    return G(g, f'translate({x},{y}) scale({s})')

def sock(x, y, s, col, rot=0):
    return G(Pa('M-10,-50 L10,-50 L10,10 Q14,22 30,24 Q36,28 32,36 L-6,36 Q-14,34 -12,20 Z', col) + R(-10, -50, 20, 8, shade(col, -.15)) + ''.join(R(-10, -36 + k * 12, 20, 4, shade(col, .3)) for k in range(3)), f'translate({x},{y}) rotate({rot}) scale({s})')

def hat_(x, y, s, col='#c8a070', band='#5a3a24'):
    return G(E(0, 10, 60, 14, col) + Pa('M-34,10 Q-34,-36 0,-38 Q34,-36 34,10 Z', shade(col, .1)) + R(-34, -6, 68, 10, band), f'translate({x},{y}) scale({s})')

def glasses_(x, y, s=1, col='#2f3437', lens='#cfe8f6', w=4):
    return G(Ci(-26, 0, 20, lens, 'opacity=".7"') + Ci(26, 0, 20, lens, 'opacity=".7"') + Ci(-26, 0, 20, 'none', f'stroke="{col}" stroke-width="{w}"') + Ci(26, 0, 20, 'none', f'stroke="{col}" stroke-width="{w}"') + St('M-8,-4 Q0,-10 8,-4', col, w) + St('M-46,-4 L-60,-10 M46,-4 L60,-10', col, w), f'translate({x},{y}) scale({s})')

def shoe2(x, y, s, col, sole='#2f3437', rot=0):
    return G(Pa('M-30,0 L-30,-20 Q-28,-28 -18,-26 L-4,-16 Q14,-12 28,-8 Q36,-4 34,4 L-30,4 Z', col) + R(-32, 2, 68, 6, sole, 3) + L(-14, -20, -8, -14, '#ffffff', 2) + L(-10, -22, -4, -16, '#ffffff', 2), f'translate({x},{y}) rotate({rot}) scale({s})')

def leather_shoe(x, y, s, col='#5a3018'):
    return G(Pa('M-36,0 Q-38,-22 -20,-24 Q0,-26 14,-16 Q36,-10 40,-2 Q40,6 30,6 L-34,6 Z', col) + R(-36, 4, 78, 6, '#2a1a10', 3) + Pa('M-20,-24 Q-4,-28 6,-18 Q-8,-14 -20,-16 Z', shade(col, -.2)) + hi(14, -12, 10, 3, .3, -10), f'translate({x},{y}) scale({s})')

def boot(x, y, s, col='#8a5a35', sole='#3a2a1a', h=70):
    return G(Pa(f'M-22,0 L-22,-{h} L10,-{h} L10,-20 Q30,-16 40,-8 Q44,0 40,4 L-22,4 Z', col) + R(-24, 2, 66, 8, sole, 3) + R(-22, -h, 32, 8, shade(col, -.15)), f'translate({x},{y}) scale({s})')

def bottle_c(cx, base, w, h, col, cap, label='#ffffff', pump=False):
    g = R(cx - w / 2, base - h, w, h, col, 10) + R(cx - w / 2 + 6, base - h * .65, w - 12, h * .38, label, 3) + R(cx - w / 2 + 5, base - h + 6, 5, h - 12, '#ffffff', 3, 'opacity=".3"')
    if pump: g += R(cx - 8, base - h - 18, 16, 20, cap, 3) + R(cx - 3, base - h - 34, 6, 18, cap) + R(cx - 3, base - h - 34, 26, 7, cap, 3)
    else: g += R(cx - w * .35, base - h - 18, w * .7, 20, cap, 4)
    return g

def jar_c(cx, base, w, h, col, lid):
    return R(cx - w / 2, base - h, w, h, col, 8) + R(cx - w / 2 - 3, base - h - 12, w + 6, 14, lid, 4) + R(cx - w / 2 + 6, base - h * .7, w - 12, h * .4, '#ffffff', 3, 'opacity=".6"')

# ================= 外貌和头发 =================
S_('tall', R(0, 186, 200, 14, WALK) + fig(70, 190, 'man', s=1.08) + fig(140, 190, 'man', shirt='#7a8a6a', s=.78) + St('M30,8 L30,186', '#e2463b', 3) + Pa('M24,16 L30,4 L36,16 Z', '#e2463b') + ring(70, 30, 0), False)
S_('short', R(0, 186, 200, 14, WALK) + fig(60, 190, 'man', s=1.08) + fig(140, 190, 'man', shirt='#d9645a', s=.72) + E(140, 190 - 168 * .72 - 6, 30, 10, 'none', 'stroke="#e2463b" stroke-width="3"') + arrow(176, 80, 176, 180, '#e2463b', 3), False)
S_('young', big_face(100, 100, 60, hair='#2a1a10', style='long', m='smile', blush='#ef9a8a') + star(170, 40, 8) + star(30, 50, 6))
S_('old', R(0, 186, 200, 14, WALK) + fig(100, 190, 'oldman', s=1.05) + R(126, 110, 5, 80, '#8a5a35') + St('M118,110 Q126,100 134,110', '#8a5a35', 5), False)
S_('pretty', big_face(100, 100, 60, hair='#2a1a10', style='long', eyes='dot', m='smile', blush='#ef9a8a') + flower(150, 52, 1.4, '#ef8fa4') + E(100, 136, 10, 4, '#e2463b') + star(40, 40, 7, '#f3c234') + star(170, 120, 6, '#f3c234'))
S_('handsome', big_face(100, 100, 60, hair='#2a1a10', style='short', eyes='dot', m='smile') + Pa('M40,200 L40,180 Q40,162 70,160 L130,160 Q160,162 160,180 L160,200 Z', '#2f3437') + Pa('M86,160 L100,184 L114,160 Z', '#ffffff') + Pa('M96,166 L104,166 L100,184 Z', '#e2463b') + star(160, 40, 8, '#f3c234') + star(36, 60, 6, '#f3c234'))
S_('slim', R(0, 186, 200, 14, WALK) + person(100, 190, shirt='#7fc4c0', pants='#3b5f8f', s=1.05) + St('M76,118 Q100,126 124,118', '#f3c234', 4) + ''.join(L(80 + k * 6, 119 + abs(k - 3.5) * -.6, 80 + k * 6, 124, '#2f3437', 1) for k in range(8)) + T(160, 110, '↔', 0, '#000'), False)
S_('beard', big_face(100, 96, 58, hair='#3a2a20', eyes='dot', m='') + Pa('M46,104 Q50,170 100,180 Q150,170 154,104 Q140,140 100,142 Q60,140 46,104 Z', '#5a3a24') + Pa('M78,130 Q100,122 122,130 Q100,138 78,130 Z', '#5a3a24') + E(100, 134, 10, 4, '#9a4a3a'))
S_('haircut', R(0, 0, 200, 200, '#e6f0f4') + big_face(80, 110, 46, hair='#3a2a20', eyes='closed', m='smile') + Pa('M40,200 L40,170 Q40,150 80,150 Q120,150 120,170 L120,200 Z', '#ffffff') + G(Pa('M0,0 L40,-8 L41,-4 Z', '#c4cbd0') + Pa('M0,0 L40,8 L41,4 Z', '#a7adb1') + Ci(-12, -8, 8, 'none', 'stroke="#2f3437" stroke-width="3"') + Ci(-12, 8, 8, 'none', 'stroke="#2f3437" stroke-width="3"'), 'translate(120,60) rotate(200)') + G(R(-30, -5, 60, 10, '#2f3437', 3) + ''.join(R(-28 + k * 5, 4, 2, 10, '#2f3437') for k in range(12)), 'translate(150,100) rotate(-30)') + ''.join(St(f'M{50+k*16},{170+k*4} l6,-4', '#3a2a20', 2) for k in range(4)), False)
# curly 卷的：一头卷卷的头发
random.seed(131)
S_('curly', ''.join(Ci(100 + 60 * math.cos(a) * random.uniform(.8, 1.05), 96 + 60 * math.sin(a) * random.uniform(.8, 1.05), random.uniform(14, 20), '#5a3a24') for a in [k * math.pi / 12 - math.pi for k in range(26)]) + big_face(100, 110, 50, hair='#5a3a24', style='none', m='smile') + ''.join(Ci(70 + k * 15, 66 - (k % 2) * 6, 12, '#5a3a24') for k in range(5)))
S_('straight', Pa('M40,190 L40,80 Q40,30 100,28 Q160,30 160,80 L160,190 Z', '#2a1a10') + ''.join(L(50 + k * 12, 100, 50 + k * 12, 186, '#3a2a20', 1.5) for k in range(10)) + big_face(100, 100, 44, hair='#2a1a10', style='short', m='smile'))
S_('grey-hair', big_face(100, 104, 60, style='long', hair=P['grey'], eyes='dot', m='smile') + ring(100, 50, 30))
S_('bald', big_face(100, 104, 60, style='none', eyes='dot', m='smile') + Pa('M40,110 Q38,74 50,72 L52,110 Z M160,110 Q162,74 150,72 L148,110 Z', P['grey']) + hi(84, 60, 18, 8, .6, -10) + ring(100, 60, 30))
S_('mustache', big_face(100, 100, 60, hair='#3a2a20', eyes='dot', m='smile') + Pa('M100,124 Q82,114 66,124 Q60,134 72,132 Q86,126 100,130 Q114,126 128,132 Q140,134 134,124 Q118,114 100,124 Z', '#3a2a20'))
S_('ponytail', Pa('M110,40 Q170,50 160,120 Q150,170 130,180 Q140,130 120,90 Z', '#3a2a20') + Ci(120, 70, 8, '#e2463b') + big_face(90, 100, 52, hair='#3a2a20', style='short', eyes='side', m='smile'))
S_('wrinkle', big_face(100, 104, 62, style='grey', hair=P['grey'], eyes='dot', m='smile') + ''.join(St(f'M{70+k*0},{64+k*7} q30,-6 60,0', SKD, 2) for k in range(3)) + St('M50,112 l-6,-4 M50,118 l-8,0 M150,112 l6,-4 M150,118 l8,0', SKD, 2) + St('M70,140 q-6,10 -2,20 M130,140 q6,10 2,20', SKD, 2))

# ================= 衣服（一） =================
S_('shirt', shirt_c(100, 100, 2.0, '#9fd0ec'))
S_('t-shirt', tshirt(100, 100, 2.1, '#e2463b') + star(100, 104, 14, '#ffffff'))
S_('pants', pants_(100, 100, 1.6, '#5d6469'))
S_('dress', dress_(100, 100, 1.6, '#ef8fa4') + ''.join(Ci(80 + (k % 4) * 14, 130 + (k // 4) * 16, 3, '#ffffff') for k in range(8)))
S_('skirt', G(Pa('M-30,-40 L30,-40 L60,40 L-60,40 Z', '#7a4fa0') + R(-30, -40, 60, 10, '#5a2f80', 2) + ''.join(L(-20 + k * 14, -30, -36 + k * 24, 40, '#6a3f90', 2) for k in range(4)), 'translate(100,110) scale(1.5)'))
S_('coat', coat_(100, 90, 1.7, '#8a5a35'))
S_('jacket', coat_(100, 100, 1.9, '#2f5a8a', False) + R(84, 130, 32, 6, '#a7adb1', 0, 'opacity="0"'))
S_('sweater', G(Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', '#d9645a') + Pa('M-10,-30 Q0,-22 10,-30 L8,-34 L-8,-34 Z', '#b8443a') + R(-22, 28, 44, 8, '#b8443a', 2) + ''.join(St(f'M-18,{-14+k*10} l6,4 l6,-4 l6,4 l6,-4 l6,4 l6,-4', '#f6efe0', 1.5) for k in range(4)), 'translate(100,100) scale(2.0)'))
S_('jeans', pants_(100, 100, 1.6, '#3b5f8f') + G(St('M-20,-20 q8,8 16,0 M4,-20 q8,8 16,0', '#f3c234', 1.5) + ''.join(L(-26 + k * 26, -40, -26 + k * 26, -32, '#f3c234', 1.5) for k in range(3)), 'translate(100,100) scale(1.6)'))
S_('shorts', pants_(100, 100, 1.8, '#c8a070', True))
S_('socks', sock(80, 110, 1.4, '#5aa1d4', -6) + sock(130, 120, 1.4, '#5aa1d4', 6))
S_('pajamas', G(Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', '#9fd0ec') + ''.join(R(-20 + k * 10, -28, 4, 62, '#ffffff') for k in range(5)) + Pa('M-10,-32 L0,-18 L10,-32 Z', '#ffffff') + ''.join(Ci(1, -10 + k * 10, 2, '#3c7fc1') for k in range(4)), 'translate(70,80) scale(1.3)') + G(pants_(0, 0, 1, '#9fd0ec') + ''.join(R(-24 + k * 10, -40, 4, 80, '#ffffff', 0, 'opacity=".8"') for k in range(5)), 'translate(140,130) scale(.9)') + Pa('M150,30 A12,12 0 1,0 164,48 A10,10 0 1,1 150,30 Z', '#f3c234'))
S_('underwear', G(Pa('M-20,-30 Q-26,-40 -16,-40 L-10,-40 Q0,-30 10,-40 L16,-40 Q26,-40 20,-30 L22,34 L-22,34 Z', '#ffffff', 'stroke="#d9dcde" stroke-width="1"'), 'translate(64,96) scale(1.3)') + G(Pa('M-30,-20 L30,-20 L30,-6 Q12,0 6,20 L-6,20 Q-12,0 -30,-6 Z', '#9fd0ec') + R(-30, -20, 60, 6, '#3c7fc1', 2), 'translate(144,120) scale(1.4)'))
S_('vest', G(Pa('M-12,-40 L-6,-40 Q0,-28 6,-40 L12,-40 L16,-20 Q22,-10 22,0 L22,40 L-22,40 L-22,0 Q-22,-10 -16,-20 Z', '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"'), 'translate(100,104) scale(2.0)'))
S_('suit', coat_(100, 90, 1.7, '#2f3437', False) + shirt_c(100, 70, .5, '#ffffff', '#e2463b').replace('scale(.5)', 'scale(.6)') + pants_(100, 166, .9, '#2f3437'))
S_('uniform', coat_(100, 90, 1.7, '#2f4a7a', False) + R(80, 74, 40, 4, '#f3c234', 1) + star(124, 64, 6, '#f3c234') + R(70, 56, 16, 6, '#f3c234', 1) + R(114, 56, 16, 6, '#f3c234', 1) + hat_(100, 30, .6, '#2f4a7a', '#1f3a5a'))

# ================= 衣服（二） =================
def tag_(x, y, s, txt, col='#ffffff'):
    return G(R(-22, -18, 44, 36, col, 6) + R(-22, -18, 44, 36, 'none', 6, 'stroke="#2f3437" stroke-width="2"') + T(0, 8, txt, 20, '#2f3437', 900) + Ci(0, -12, 3, '#2f3437'), f'translate({x},{y}) scale({s})')
S_('size', tshirt(40, 140, .7, '#5aa1d4') + tshirt(96, 130, .95, '#5aa1d4') + tshirt(160, 116, 1.2, '#5aa1d4') + tag_(40, 50, .7, 'S') + tag_(96, 50, .7, 'M') + tag_(160, 50, .7, 'L'))
S_('small', tshirt(100, 120, 1.0, '#ef8fa4') + tag_(150, 60, 1.0, 'S', '#f3c234'))
S_('medium', tshirt(100, 116, 1.5, '#7fc4c0') + tag_(160, 50, 1.0, 'M', '#f3c234'))
S_('large', tshirt(100, 110, 2.2, '#5ba644') + tag_(166, 40, .9, 'L', '#f3c234'))
S_('try-on', R(0, 0, 200, 200, '#f2ead8') + E(150, 100, 40, 80, '#c8903a') + E(150, 100, 34, 74, '#dff1fb') + fig(70, 190, 'woman') + G(dress_(0, 0, .6, '#e2463b'), 'translate(64,110)') + G(dress_(0, 0, .5, '#e2463b'), 'translate(150,120)'), False)
S_('tight', R(0, 186, 200, 14, WALK) + person(100, 190, shirt='#e2463b', pants='#3b4a5a', arms='down', s=1.05) + R(80, 88, 40, 10, '#e2463b') + ''.join(St(f'M{84+k*10},70 l4,6', '#ffffff', 1.5) for k in range(4)) + St('M66,90 l-8,-4 M134,90 l8,-4', '#e2463b', 3) + drop(60, 40, 5), False)
S_('loose', R(0, 186, 200, 14, WALK) + person(100, 190, shirt='#5ba644', pants='#3b4a5a', arms='down', s=1.0) + Pa('M60,62 L140,62 L156,140 L44,140 Z', '#5ba644') + Pa('M60,62 L44,110 L34,104 Z M140,62 L156,110 L166,104 Z', '#4a9a3a') + ''.join(St(f'M{60+k*16},80 q-4,30 2,56', '#4a9a3a', 2) for k in range(6)), False)
S_('pocket', pants_(100, 100, 1.6, '#3b5f8f') + Pa('M62,62 L92,62 L90,92 L76,98 L64,92 Z', '#2f4f78') + ring(78, 80, 24))
S_('button', ''.join(G(Ci(0, 0, 26, c) + Ci(0, 0, 20, shade(c, .15)) + ''.join(Ci(6 * math.cos(a), 6 * math.sin(a), 3, shade(c, -.35)) for a in [k * math.pi / 2 + .78 for k in range(4)]), f'translate({x},{y}) scale({s})') for x, y, s, c in [(70, 80, 1.3, '#e2463b'), (140, 110, 1.0, '#3c7fc1'), (90, 150, .9, '#f3c234')]))
S_('zipper', R(70, 20, 60, 170, '#3c7fc1') + ''.join(R(96 - (k % 2) * 6, 20 + k * 8, 10, 6, '#c4cbd0', 1) for k in range(10)) + Pa('M100,100 L80,190 L120,190 Z', '#3c7fc1') + Pa('M100,100 L84,190 L116,190 Z', '#7fc4e8', 'opacity="0"') + R(90, 96, 20, 16, '#a7adb1', 4) + R(96, 110, 8, 26, '#a7adb1', 3) + Pa('M100,100 L70,190 L74,190 L100,104 L126,190 L130,190 Z', '#f2ead8'))
S_('sleeve', shirt_c(100, 100, 2.0, '#f3d058') + ring(100 + 36 * 2, 100 + 14 * 2, 24))
S_('collar', shirt_c(100, 110, 2.0, '#f6efe0') + ring(100, 110 - 26 * 2, 30))
S_('fitting-room', R(0, 0, 200, 200, '#f2ead8') + R(30, 20, 140, 6, '#5d6469') + Pa('M30,26 Q40,110 34,190 L100,190 Q90,110 100,26 Z', '#7a4fa0') + Pa('M100,26 Q110,110 104,190 L170,190 Q164,110 170,26 Z', '#8a5fb0') + ''.join(St(f'M{40+k*14},28 Q{36+k*14},110 {42+k*14},188', '#6a3f90', 2) for k in range(9)) + R(94, 150, 20, 40, '#3b4a5a', 0, 'opacity="0"') + shoe2(118, 190, .4, '#e2463b') + shoe2(140, 190, .4, '#e2463b') + hanger_icon if False else R(0, 0, 200, 200, '#f2ead8') + R(30, 20, 140, 6, '#5d6469') + Pa('M30,26 Q40,110 34,190 L100,190 Q90,110 100,26 Z', '#7a4fa0') + Pa('M100,26 Q110,110 104,190 L170,190 Q164,110 170,26 Z', '#8a5fb0') + ''.join(St(f'M{40+k*14},28 Q{36+k*14},110 {42+k*14},188', '#6a3f90', 2) for k in range(9)) + shoe2(118, 194, .4, '#e2463b') + shoe2(146, 194, .4, '#e2463b'), False)
S_('cotton', St('M100,190 L100,110', '#8a6a3a', 4) + ''.join(Ci(100 + 22 * math.cos(a), 80 + 22 * math.sin(a), 22, '#ffffff', 'stroke="#ece6da" stroke-width="2"') for a in [k * math.pi * 2 / 5 for k in range(5)]) + Ci(100, 80, 18, '#ffffff') + ''.join(Pa(f'M100,104 L{100+30*math.cos(a)},{104+20*math.sin(a)} L{100+24*math.cos(a+.3)},{104+24*math.sin(a+.3)} Z', '#8a6a3a') for a in [.3, 1.5, 2.8]) + leaf(100, 150, 30, 10, -30, '#5aaa3a'))
S_('wool', Ci(80, 110, 50, '#e6dcc8') + ''.join(St(f'M{40+k*10},{80+k*2} Q80,{60+k*12} 120,{100+k*4}', '#d0c4ac', 2.5) for k in range(6)) + St('M120,140 Q150,170 180,150', '#e6dcc8', 5) + G(R(-3, -50, 6, 70, '#c4cbd0', 3), 'translate(150,80) rotate(30)') + G(R(-3, -50, 6, 70, '#c4cbd0', 3), 'translate(160,90) rotate(10)') + badge(160, 40, 'sheep', 16))
S_('silk', Pa('M20,60 Q60,30 100,60 Q140,90 180,60 L180,150 Q140,180 100,150 Q60,120 20,150 Z', '#e8a0c0') + Pa('M20,60 Q60,30 100,60 Q140,90 180,60 L180,80 Q140,110 100,80 Q60,50 20,80 Z', '#f6c8dc') + hi(80, 90, 30, 6, .5, -10) + E(40, 176, 14, 9, '#f6f1e4') + E(64, 180, 14, 9, '#f6f1e4'))

# ================= 衣服（三） =================
S_('hat', hat_(100, 116, 1.4))
S_('scarf', G(Pa('M-60,-20 Q0,-40 60,-20 L60,0 Q0,-20 -60,0 Z', '#e2463b') + R(24, -10, 24, 90, '#e2463b', 4) + ''.join(R(24, 6 + k * 18, 24, 6, '#ffffff') for k in range(4)) + ''.join(L(26 + k * 5, 80, 26 + k * 5, 92, '#e2463b', 2) for k in range(5)), 'translate(90,80) scale(1.3)'))
S_('gloves', ''.join(G(R(-22, 0, 44, 50, c, 8) + R(-24, 40, 48, 18, shade(c, .3), 6) + ''.join(R(-22 + k * 11, -36 + abs(k - 1.5) * 6, 10, 40, c, 5) for k in range(4)) + G(R(-6, -14, 12, 34, c, 6), 'translate(-24,14) rotate(-40)'), f'translate({x},{100}) rotate({r_})') for x, r_, c in [(70, -12, '#5aa1d4'), (132, 12, '#5aa1d4')]))
S_('cap', G(Pa('M-40,10 Q-40,-40 0,-42 Q40,-40 40,10 Z', '#e2463b') + Pa('M10,10 Q60,0 76,16 Q50,22 10,16 Z', '#c0302a') + Ci(0, -40, 4, '#c0302a') + St('M-30,-10 Q0,-30 30,-10', '#c0302a', 1.5), 'translate(90,110) scale(1.6)'))
S_('tie', Pa('M88,30 L112,30 L108,50 L92,50 Z', '#3c7fc1') + Pa('M92,50 L108,50 L122,150 L100,176 L78,150 Z', '#3c7fc1') + ''.join(L(84 + k * 2, 66 + k * 22, 116 - k * 2, 56 + k * 22, '#f3c234', 4) for k in range(5)))
S_('raincoat', coat_(100, 90, 1.7, '#f3c234') + Pa('M76,32 Q100,0 124,32 L120,40 Q100,20 80,40 Z', '#f3c234') + ''.join(drop(40 + k * 40, 30 + (k % 2) * 20, 5, '#9fd0ec') for k in range(4)))
S_('apron', Pa('M70,40 L130,40 L130,80 Q160,84 160,100 L150,190 L50,190 L40,100 Q40,84 70,80 Z', '#ef8fa4') + St('M70,40 Q100,10 130,40', '#ef8fa4', 4) + R(76, 120, 48, 30, '#e2708a', 4) + St('M40,96 L10,110 M160,96 L190,110', '#ef8fa4', 4) + ''.join(Ci(70 + (k % 3) * 30, 60 + (k // 3) * 80, 4, '#ffffff') for k in range(6)))
S_('swimsuit', G(Pa('M-12,-50 L-6,-50 Q0,-36 6,-50 L12,-50 L18,-20 Q30,10 24,40 Q10,30 0,50 Q-10,30 -24,40 Q-30,10 -18,-20 Z', '#3c7fc1') + ''.join(Ci(-10 + (k % 3) * 10, -10 + (k // 3) * 16, 3, '#ffffff') for k in range(6)), 'translate(100,100) scale(1.8)'))
S_('blouse', G(Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', '#f6e2ec') + Pa('M-14,-32 Q-4,-6 0,-20 Q4,-6 14,-32 Q0,-20 -14,-32 Z', '#ffffff') + Pa('M-12,-30 Q-20,-16 -6,-14 Q0,-20 -12,-30 Z M12,-30 Q20,-16 6,-14 Q0,-20 12,-30 Z', '#ffffff') + ''.join(Ci(0, -6 + k * 10, 1.8, '#e2708a') for k in range(4)), 'translate(100,100) scale(2.0)'))
S_('cardigan', G(Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', '#9a8ac8') + Pa('M-6,-30 L6,-30 L4,34 L-4,34 Z', '#f6efe0') + ''.join(Ci(-8, -18 + k * 12, 2.5, '#5a3a7a') for k in range(5)) + R(-22, 28, 44, 6, '#7a6aa8', 2) + R(-18, 2, 10, 10, '#7a6aa8', 2) + R(8, 2, 10, 10, '#7a6aa8', 2), 'translate(100,100) scale(2.0)'))
S_('hoodie', G(Pa('M-18,-30 L18,-30 L44,26 L32,30 L22,-2 L22,34 L-22,34 L-22,-2 L-32,30 L-44,26 Z', '#5ba644') + Pa('M-20,-30 Q-20,-58 0,-58 Q20,-58 20,-30 Q0,-40 -20,-30 Z', '#4a9a3a') + Pa('M-12,-34 Q0,-48 12,-34', '#3a7a2a') + R(-14, 6, 28, 18, '#4a9a3a', 4) + L(-4, -28, -4, -12, '#ffffff', 1.5) + L(4, -28, 4, -12, '#ffffff', 1.5), 'translate(100,110) scale(1.9)'))
S_('down-jacket', G(Pa('M-22,-34 L22,-34 L46,-18 L48,30 L34,32 L30,0 L28,40 L-28,40 L-30,0 L-34,32 L-48,30 L-46,-18 Z', '#e2463b') + ''.join(Pa(f'M-28,{-24+k*14} Q0,{-18+k*14} 28,{-24+k*14}', 'none', 'stroke="#c0302a" stroke-width="2"') for k in range(5)) + L(0, -34, 0, 40, '#c4cbd0', 2) + Pa('M-16,-34 Q0,-46 16,-34 L16,-28 Q0,-38 -16,-28 Z', '#c0302a'), 'translate(100,104) scale(1.8)'))
S_('on-sale', R(20, 30, 160, 6, '#5d6469', 2) + L(30, 36, 30, 190, '#5d6469', 3) + L(170, 36, 170, 190, '#5d6469', 3) + ''.join(St(f'M{50+k*30},36 L{50+k*30},44', '#5d6469', 2) + tshirt(50 + k * 30, 80, .6, ['#e2463b', '#5aa1d4', '#f3c234', '#5ba644', '#ef8fa4'][k]) for k in range(5)) + G(R(-40, -24, 80, 48, '#e2463b', 6) + T(0, 10, '-50%', 24, '#ffffff', 900), 'translate(100,150) rotate(-6)'))
S_('wash', E(100, 130, 80, 40, '#5aa1d4') + E(100, 120, 72, 30, '#9fd0ec') + tshirt(84, 116, .6, '#e2463b') + ''.join(Ci(50 + k * 18, 106 - (k % 3) * 8, 9, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(7)) + hand_(150, 120, .5, -30, '#ef8fa4'))
S_('fold', ''.join(R(40, 150 - k * 22, 120, 22, ['#5aa1d4', '#ef8fa4', '#f3c234', '#5ba644', '#ffffff'][k], 4) + L(40, 150 - k * 22 + 11, 160, 150 - k * 22 + 11, '#000', 0) for k in range(5)) + ''.join(L(100, 150 - k * 22, 100, 172 - k * 22, shade(['#5aa1d4', '#ef8fa4', '#f3c234', '#5ba644', '#ffffff'][k], -.15), 1.5) for k in range(5)))
S_('fashionable', R(0, 186, 200, 14, WALK) + person(100, 190, shirt='#e2463b', pants='#2f3437', style='long', hair='#2a1a10', arms='hips', s=1.02) + glasses_(100, 36, .25, '#2f3437', '#2f3437') + bag_(126, 100, 22, 22, '#f3c234') + star(40, 40, 9) + star(160, 30, 7) + star(160, 120, 6), False)

# ================= 配饰 =================
S_('bag', Pa('M40,90 L160,90 L170,180 L30,180 Z', '#8a5a35') + R(40, 90, 120, 26, '#7a4a25', 2) + R(92, 108, 16, 14, '#d9a33a', 3) + St('M60,90 Q60,40 100,40 Q140,40 140,90', '#7a4a25', 8))
S_('watch', R(84, 20, 32, 160, '#5a3a24', 8) + Ci(100, 100, 34, '#c4cbd0') + clock(100, 100, 28, (10, 10), '#ffffff', '#a7adb1') + R(132, 96, 8, 8, '#a7adb1', 2))
S_('glasses', glasses_(100, 100, 1.4))
S_('ring', G(Ci(0, 0, 40, 'none', 'stroke="#d9a33a" stroke-width="12"') + Pa('M-16,-40 L0,-66 L16,-40 Z', '#bfe6fa') + Pa('M-16,-40 L0,-50 L16,-40 Z', '#ffffff'), 'translate(100,110)') + star(150, 50, 6, '#ffffff'))
S_('umbrella', Pa('M20,96 Q100,10 180,96 Q160,86 140,96 Q120,86 100,96 Q80,86 60,96 Q40,86 20,96 Z', '#e2463b') + ''.join(Pa(f'M100,30 Q{60+k*40},40 {40+k*40},96 Q{60+k*40},86 {80+k*40},96 Z', '#c0302a') for k in range(0, 4, 2)) + L(100, 24, 100, 170, '#2f3437', 4) + St('M100,170 Q100,186 86,186 Q76,186 76,176', '#2f3437', 5))
S_('wallet', R(30, 70, 140, 90, '#5a3a24', 10) + R(30, 70, 140, 40, '#6a4a2a', 10) + R(130, 96, 40, 30, '#4a2a14', 6) + Ci(150, 111, 5, '#d9a33a') + money_note(80, 70, .6, 0) + card_(110, 66, .4, 0, '#3c7fc1'))
S_('belt', G(R(-90, -14, 180, 28, '#5a3a24', 6) + ''.join(Ci(30 + k * 14, 0, 3, '#2f3437') for k in range(3)) + R(-50, -22, 36, 44, 'none', 6, 'stroke="#d9a33a" stroke-width="6"') + L(-32, 0, -10, 0, '#d9a33a', 4), 'translate(100,100) rotate(-10)'))
S_('necklace', St('M40,40 Q40,140 100,150 Q160,140 160,40', '#d9a33a', 3) + ''.join(Ci(100 + 60 * math.cos(a), 60 + 80 * math.sin(a), 6, '#f6f1ea', 'stroke="#d9cfb8" stroke-width="1"') for a in [math.pi * (k / 14) for k in range(1, 14)]) + heart(100, 160, 12, '#e2463b'))
S_('earrings', big_face(100, 100, 56, style='short', hair='#2a1a10', m='smile') + ''.join(Ci(100 + sx * 53, 128, 4, '#d9a33a') + L(100 + sx * 53, 132, 100 + sx * 53, 146, '#d9a33a', 2) + Pa(f'M{100+sx*53},146 L{100+sx*53-7},156 L{100+sx*53},168 L{100+sx*53+7},156 Z', '#5aa1d4') for sx in (-1, 1)))
S_('sunglasses', glasses_(100, 100, 1.4, '#2f3437', '#2f3437', 5) + Ci(60, 92, 6, '#ffffff', 'opacity=".4"') + Ci(132, 92, 6, '#ffffff', 'opacity=".4"') + Ci(170, 40, 16, '#f3c234'))
S_('bracelet', E(100, 110, 60, 30, 'none', 'stroke="#d9a33a" stroke-width="10"') + E(100, 104, 60, 30, 'none', 'stroke="#f0c860" stroke-width="3"') + ''.join(Ci(100 + 60 * math.cos(a), 110 + 30 * math.sin(a), 7, ['#e2463b', '#5aa1d4', '#5ba644'][k % 3]) for k, a in enumerate([j * math.pi / 4 for j in range(8)])))
S_('purse', Pa('M40,100 Q40,60 100,60 Q160,60 160,100 L156,170 L44,170 Z', '#c0302a') + Pa('M40,100 Q100,120 160,100 L160,96 Q100,112 40,96 Z', '#a01e30') + St('M70,64 Q100,20 130,64', '#2f3437', 4) + Ci(100, 112, 7, '#d9a33a'))
S_('backpack', R(50, 50, 100, 130, '#3c7fc1', 20) + R(66, 110, 68, 50, '#2f5a8a', 10) + L(66, 120, 134, 120, '#f3c234', 3) + St('M80,50 Q100,24 120,50', '#2f5a8a', 8) + R(40, 70, 14, 90, '#2f5a8a', 6) + R(146, 70, 14, 90, '#2f5a8a', 6))
S_('handkerchief', G(R(-60, -60, 120, 120, '#ffffff', 4) + R(-52, -52, 104, 104, 'none', 2, 'stroke="#5aa1d4" stroke-width="3"') + flower(-38, -38, .8, '#5aa1d4') + flower(38, 38, .8, '#5aa1d4') + Pa('M60,60 L20,60 L60,20 Z', '#f2efe8'), 'translate(100,100) rotate(10)'))
S_('brooch', G(''.join(E(18 * math.cos(a), 18 * math.sin(a), 14, 9, '#d9a33a', f'transform="rotate({math.degrees(a):.0f} {18*math.cos(a):.1f} {18*math.sin(a):.1f})"') for a in [k * math.pi / 3 for k in range(6)]) + Ci(0, 0, 16, '#c0283a') + hi(-5, -5, 5, 3, .7) + ''.join(Ci(30 * math.cos(a), 30 * math.sin(a), 4, '#ffffff') for a in [k * math.pi / 3 + .5 for k in range(6)]), 'translate(100,100) scale(1.6)'))
S_('jewelry', R(30, 100, 140, 70, '#c0283a', 6) + Pa('M30,100 L40,50 L160,50 L170,100 Z', '#a01e30') + R(38, 104, 124, 50, '#f2d8e0', 4) + St('M50,124 Q100,150 150,124', '#f6f1ea', 6) + ''.join(Ci(56 + k * 10, 126 + math.sin(k / 9 * math.pi) * 20, 4, '#f6f1ea') for k in range(10)) + G(Ci(0, 0, 10, 'none', 'stroke="#d9a33a" stroke-width="4"') + Pa('M-5,-10 L0,-18 L5,-10 Z', '#bfe6fa'), 'translate(100,118)') + star(160, 40, 6, '#f3c234'))

# ================= 鞋 =================
S_('shoes', leather_shoe(70, 140, 1.1) + leather_shoe(130, 150, 1.1))
S_('boots', boot(70, 170, 1.3) + boot(130, 176, 1.3))
S_('sneakers', shoe2(70, 140, 1.2, '#ffffff', '#5aa1d4') + shoe2(140, 156, 1.2, '#ffffff', '#5aa1d4') + G(R(-30, -14, 30, 6, '#5aa1d4', 2), 'translate(70,140) scale(1.2)'))
S_('slippers', G(E(0, 0, 40, 18, '#f6c8d8') + Pa('M-14,-18 Q10,-30 30,-10 L30,6 L-14,6 Z', '#ef8fa4') + ''.join(Ci(4 + k * 8, -8, 3, '#ffffff') for k in range(3)), 'translate(70,130) scale(1.2)') + G(E(0, 0, 40, 18, '#f6c8d8') + Pa('M-14,-18 Q10,-30 30,-10 L30,6 L-14,6 Z', '#ef8fa4'), 'translate(130,150) scale(1.2)'))
S_('sandals', ''.join(G(E(0, 0, 18, 46, '#c8903a') + R(-18, -24, 36, 10, '#8a5a35', 4) + R(-18, 4, 36, 10, '#8a5a35', 4) + St('M-14,26 Q0,12 14,26', '#8a5a35', 4), f'translate({x},100) rotate({r_}) scale(1.3)') for x, r_ in [(70, -10), (130, 10)]))
S_('pair', leather_shoe(70, 130, .9) + leather_shoe(130, 140, .9) + St('M30,170 L30,180 L170,180 L170,170', '#e2463b', 3) + T(100, 196, '1 + 1', 0, '#000') + Ci(100, 180, 12, '#e2463b') + T(100, 186, '2', 16, '#ffffff', 900))
S_('high-heels', ''.join(G(Pa('M-40,0 Q-40,-14 -30,-14 Q0,-10 14,-40 Q22,-50 30,-40 L34,-36 Q40,-30 40,-10 L40,40 L34,40 L30,0 Z', '#c0283a') + R(30, -10, 8, 50, '#a01e30', 2), f'translate({x},{y}) scale(1.2)') for x, y in [(60, 120), (130, 140)]))
S_('shoelace', shoe2(100, 150, 2.0, '#ffffff', '#5aa1d4') + G(''.join(L(-12 + k * 4, -24 + k * 3, -2 + k * 4, -18 + k * 3, '#e2463b', 2) for k in range(4)) + St('M2,-12 Q20,-30 30,-10 M2,-12 Q-14,-34 -20,-14', '#e2463b', 2.5), 'translate(100,150) scale(2.0)') + ring(96, 100, 30))
S_('leather', Pa('M30,60 Q60,40 100,56 Q150,40 170,70 Q180,110 160,140 Q130,170 100,150 Q60,170 36,140 Q20,100 30,60 Z', '#8a5030') + St('M40,70 Q100,50 160,80', '#a8683a', 2, 'stroke-dasharray="4 4"') + hi(70, 80, 20, 6, .2, -10) + leather_shoe(150, 176, .5))
S_('comfortable', shoe2(100, 140, 2.0, '#9fd0ec', '#ffffff') + ''.join(Ci(60 + k * 30, 170, 14, '#ffffff', 'opacity=".9"') for k in range(4)) + heart(160, 50, 12) + St('M40,60 q10,-6 20,0', '#5ba644', 0))
S_('flat-shoes', ''.join(G(Pa('M-40,0 Q-42,-16 -26,-18 Q0,-20 20,-12 Q40,-6 40,0 Z', '#2f3437') + R(-42, 0, 84, 4, '#1a1a1a', 2) + Pa('M-6,-18 Q4,-24 12,-16 Q4,-12 -6,-18 Z', '#e2463b'), f'translate({x},{y}) scale(1.3)') for x, y in [(70, 120), (130, 150)]))
S_('rain-boots', boot(70, 170, 1.3, '#f3c234', '#2f3437') + boot(130, 176, 1.3, '#f3c234', '#2f3437') + ''.join(drop(40 + k * 40, 30 + (k % 2) * 16, 6, '#9fd0ec') for k in range(4)) + E(100, 186, 70, 6, '#9fd0ec', 'opacity=".6"'))
S_('hiking-boots', boot(100, 160, 1.8, '#8a6a3a', '#3a2a1a', 50) + G(''.join(L(-18, -44 + k * 9, 6, -44 + k * 9, '#e2463b', 2) for k in range(4)) + R(-24, 6, 66, 4, '#5a4a3a'), 'translate(100,160) scale(1.8)') + Pa('M150,40 L170,70 L130,70 Z', '#7a8a6a') + Pa('M164,52 L178,72 L150,72 Z', '#5a6a4a'))
S_('insole', ''.join(G(Pa('M0,-60 Q22,-60 22,-30 Q22,10 14,40 Q8,60 0,60 Q-14,60 -16,40 Q-20,0 -20,-30 Q-20,-60 0,-60 Z', '#e8d4b0') + ''.join(Ci(-6 + (j % 3) * 6, -30 + (j // 3) * 10, 1.5, '#c8b490') for j in range(9)), f'translate({x},100) scale(1.3)') for x in (70, 130)))
S_('shoe-polish', Ci(70, 140, 34, '#2f3437') + E(70, 126, 34, 10, '#c4cbd0') + E(70, 124, 28, 6, '#1a1a1a') + T(70, 150, '◆', 0, '#000') + R(46, 140, 48, 14, '#f3c234', 2) + leather_shoe(140, 100, .9) + G(R(-20, -8, 40, 16, '#8a5a35', 4) + R(-20, 6, 40, 8, '#2f3437', 2), 'translate(130,60) rotate(-20)') + star(170, 80, 6, '#ffffff'))
S_('shoehorn', G(R(-6, -80, 12, 80, '#8a5a35', 6) + Ci(0, -84, 6, '#f2ead8') + Pa('M-16,0 L16,0 Q20,50 0,64 Q-20,50 -16,0 Z', '#c8903a'), 'translate(80,110) rotate(-10)') + leather_shoe(140, 170, .9))

# ================= 美容 =================
S_('mirror', E(100, 80, 54, 66, '#c8903a') + E(100, 80, 46, 58, '#dff1fb') + Pa('M72,60 L94,40 M76,80 L110,48', 'none', 'stroke="#ffffff" stroke-width="5" opacity=".7"') + R(94, 144, 12, 30, '#c8903a', 3) + E(100, 176, 30, 8, '#a8703e'))
S_('comb', G(R(-70, -14, 140, 20, '#e2463b', 4) + ''.join(R(-66 + k * 7, 4, 3.5, 30 - (k > 12) * 10, '#e2463b', 1) for k in range(19)), 'translate(100,100) rotate(-15)'))
S_('soap', R(40, 90, 120, 60, '#ef8fa4', 24) + R(40, 90, 120, 30, '#f6b0c0', 20) + E(100, 114, 34, 10, '#f6c8d4') + ''.join(Ci(50 + k * 22, 80 - (k % 2) * 14, 10 - k, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(5)) + E(100, 160, 70, 8, '#c4cbd0', 'opacity=".5"'))
S_('shampoo', bottle_c(80, 180, 60, 120, '#7fc4c0', '#ffffff', pump=True) + E(80, 120, 14, 18, '#5aa0a0', 'opacity=".0"') + St('M64,116 q16,-10 32,0 q-16,10 -32,0', '#ffffff', 0) + ''.join(St(f'M{66+k*6},104 q4,10 0,20', '#5aa0a0', 1.5) for k in range(5)) + ''.join(Ci(140 + k * 12, 150 - (k % 2) * 10, 8, '#ffffff', 'stroke="#d9e8f0" stroke-width="1.5"') for k in range(3)))
S_('cream', jar_c(100, 170, 100, 60, '#ffffff', '#d9a33a') + Pa('M60,110 Q100,90 140,110', 'none', 'stroke="none"') + E(100, 98, 46, 8, '#f6efe0') + Pa('M84,98 Q100,76 116,98 Z', '#ffffff') + flower(100, 140, 1.0, '#ef8fa4'))
S_('lipstick', R(76, 110, 48, 70, '#2f3437', 4) + R(80, 90, 40, 24, '#d9a33a', 2) + Pa('M84,90 L84,50 Q100,30 116,40 L116,90 Z', '#c0283a') + R(146, 120, 30, 60, '#2f3437', 4, 'opacity="0"') + E(150, 170, 26, 6, '#c0283a', 'opacity=".0"') + Pa('M140,160 Q156,150 172,160 Q156,172 140,160 Z', '#c0283a'))
S_('perfume', R(60, 90, 80, 90, '#f6c8dc', 14, 'opacity=".9"') + R(60, 90, 80, 90, 'none', 14, 'stroke="#e8a0c0" stroke-width="2"') + R(88, 70, 24, 22, '#d9a33a', 3) + E(100, 60, 18, 12, '#d9a33a') + E(100, 140, 24, 20, '#ffffff', 'opacity=".5"') + ''.join(Ci(150 + k * 10, 60 - k * 6, 3, '#e8a0c0') for k in range(4)) + St('M144,70 q10,-10 20,0 t20,0', '#e8a0c0', 2))
S_('makeup', R(20, 120, 80, 50, '#2f3437', 6) + ''.join(Ci(36 + k * 22, 140 + (0) * 14, 8, ['#ef8fa4', '#c8903a', '#9a7ab8'][k]) for k in range(3)) + E(60, 160, 30, 6, '#f6c8a8') + G(R(-3, -40, 6, 60, '#8a5a35', 3) + Pa('M-8,-40 L8,-40 L10,-60 Q0,-70 -10,-60 Z', '#e8c8b0'), 'translate(130,120) rotate(20)') + R(150, 100, 14, 60, '#2f3437', 3) + Pa('M150,100 L164,100 L160,80 L154,80 Z', '#c0283a'))
S_('nail-polish', R(70, 100, 60, 70, '#e2463b', 12) + R(84, 60, 32, 44, '#2f3437', 4) + hi(84, 120, 6, 18, .4) + G(R(-14, -20, 28, 40, SK, 12) + E(0, -12, 10, 8, '#e2463b'), 'translate(160,120) rotate(-20)') + G(R(-14, -20, 28, 40, SK, 12) + E(0, -12, 10, 8, '#e2463b'), 'translate(40,140) rotate(20)'))
S_('hairdryer', G(Ci(0, 0, 40, '#ef8fa4') + Ci(0, 0, 30, '#f6b0c0') + R(30, -18, 60, 36, '#ef8fa4', 8) + R(-14, 30, 28, 70, '#e2708a', 10) + R(-6, 44, 12, 14, '#ffffff', 3), 'translate(70,80)') + ''.join(St(f'M164,{70+k*14} q10,-4 20,0', '#c4cbd0', 3) for k in range(3)))
S_('sunscreen', bottle_c(84, 180, 60, 110, '#f3c234', '#e2463b') + Ci(84, 130, 14, '#f08a24') + ''.join(L(84 + 18 * math.cos(a), 130 + 18 * math.sin(a), 84 + 24 * math.cos(a), 130 + 24 * math.sin(a), '#f08a24', 2) for a in [k * math.pi / 4 for k in range(8)]) + Ci(160, 40, 18, '#f3c234') + ''.join(L(160 + 22 * math.cos(a), 40 + 22 * math.sin(a), 160 + 30 * math.cos(a), 40 + 30 * math.sin(a), '#f3c234', 3) for a in [k * math.pi / 4 for k in range(8)]))
S_('lotion', bottle_c(90, 180, 64, 120, '#ffffff', '#9fd0ec', pump=True) + R(64, 110, 52, 40, '#9fd0ec', 3) + leaf(90, 136, 16, 6, -60, '#5ba644') + Pa('M140,150 q10,-20 24,-8 q8,10 -8,16 Z', '#ffffff', 'stroke="#e6ecef" stroke-width="2"') + G(R(-14, -20, 28, 40, SK, 12), 'translate(160,170) rotate(-60)'))
S_('razor', G(R(-6, -10, 12, 110, '#3c7fc1', 6) + R(-40, -30, 80, 22, '#5d6469', 4) + R(-38, -12, 76, 4, '#c4cbd0'), 'translate(100,80) rotate(15)'))
S_('massage', R(0, 140, 200, 60, '#c8a070') + R(10, 120, 180, 24, '#ffffff', 8) + pose((40, 112), (60, 120), (120, 124), arms=[[(60, 126), (50, 136)]], legs=[[(120, 124), (160, 126), (186, 128)]], shirt='#9fd0ec', pants='#5d6469', mood='closed', hr=13, tw=26) + G(R(-14, -10, 28, 30, SK, 8), 'translate(80,106)') + G(R(-14, -10, 28, 30, SK, 8), 'translate(104,104)') + St('M70,80 q4,-10 8,0 M100,76 q4,-10 8,0', '#e2708a', 2) + heart(150, 60, 10), False)
S_('manicure', G(R(-30, -30, 60, 56, SK, 16) + ''.join(R(-28 + k * 14, -80 + abs(k - 1.5) * 8, 12, 56, SK, 6) + E(-22 + k * 14, -74 + abs(k - 1.5) * 8, 5, 6, '#ef8fa4') for k in range(4)) + G(R(-7, -36, 14, 40, SK, 7), 'translate(-30,-10) rotate(-40)'), 'translate(80,130)') + G(R(-3, -40, 6, 50, '#c4cbd0', 2) + E(0, -44, 5, 8, '#ef8fa4'), 'translate(150,100) rotate(-30)') + R(130, 150, 30, 40, '#ef8fa4', 6) + R(138, 136, 14, 16, '#2f3437', 2))
S_('beauty-salon', R(0, 180, 200, 20, WALK) + storefront(20, 30, 160, 150, '#fbe8f0', '#ef8fa4', sign='#e2708a', door=False) + E(100, 112, 22, 28, '#c8903a') + E(100, 112, 18, 24, '#dff1fb') + G(R(-3, -12, 6, 24, '#ffffff', 2) + E(0, -14, 6, 4, '#ffffff'), 'translate(150,120)') + G(Pa('M0,0 L20,-4 L21,-2 Z', '#ffffff') + Pa('M0,0 L20,4 L21,2 Z', '#ffffff') + Ci(-6, -4, 4, 'none', 'stroke="#ffffff" stroke-width="2"') + Ci(-6, 4, 4, 'none', 'stroke="#ffffff" stroke-width="2"'), 'translate(90,47)') + flower(50, 150, .8, '#ef8fa4') + E(150, 158, 0, 0, '#000'), False)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
