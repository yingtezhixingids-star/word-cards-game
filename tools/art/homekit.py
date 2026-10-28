from flat import *
from fig import *
import random

SK = P['skin']
WOOD = '#c58b54'; WOODD = '#a8703e'; WOODL = '#d9a868'

def house(cx, base, w, h, wall='#f4e6c8', roof='#c0503a', door='#8a5a35', win='#8ec3e6', chimney=False):
    g = ''
    if chimney: g += R(cx + w * .2, base - h - h * .55, w * .12, h * .4, '#a8503a')
    g += R(cx - w / 2, base - h, w, h, wall) + R(cx + w / 2 - w * .12, base - h, w * .12, h, shade(wall, -.08))
    g += Pa(f'M{cx-w/2-10},{base-h+2} L{cx},{base-h-h*.6} L{cx+w/2+10},{base-h+2} Z', roof) + Pa(f'M{cx},{base-h-h*.6} L{cx+w/2+10},{base-h+2} L{cx+w/2},{base-h+2} Z', shade(roof, -.15))
    g += R(cx - w * .1, base - h * .55, w * .2, h * .55, door, 2) + Ci(cx + w * .06, base - h * .28, 2.5, '#f3c234')
    for sx in (-1, 1):
        x = cx + sx * w * .3
        g += R(x - w * .1, base - h * .75, w * .2, w * .2, win, 2) + L(x, base - h * .75, x, base - h * .75 + w * .2, '#ffffff', 2) + L(x - w * .1, base - h * .75 + w * .1, x + w * .1, base - h * .75 + w * .1, '#ffffff', 2)
    return g

def building(x, y, w, h, col='#d9cfc0', win='#8ec3e6', cols=3, rows=6, hl=None):
    g = R(x, y, w, h, col) + R(x + w - 8, y, 8, h, shade(col, -.1)) + R(x - 3, y - 6, w + 6, 8, shade(col, -.2))
    cw = (w - 16) / cols; rh = (h - 30) / rows
    for r_ in range(rows):
        for c in range(cols):
            fill = '#f3d058' if hl is not None and r_ == hl else win
            g += R(x + 8 + c * cw + 3, y + 8 + r_ * rh + 3, cw - 8, rh - 8, fill, 1)
    g += R(x + w / 2 - 10, y + h - 22, 20, 22, '#5a3a24', 1)
    return g

def door_(x, y, w, h, col=WOOD, frame='#f4f1ea'):
    g = R(x - 5, y - 5, w + 10, h + 5, frame, 2) + R(x, y, w, h, col, 2) + R(x + w * .12, y + h * .08, w * .76, h * .36, shade(col, -.08), 3) + R(x + w * .12, y + h * .52, w * .76, h * .4, shade(col, -.08), 3)
    g += Ci(x + w * .82, y + h * .5, w * .06 + 1, '#d9a33a') + hi(x + w * .25, y + h * .15, 3, h * .15, .2)
    return g

def window_(x, y, w, h, sky='#a9d8f2', frame='#ffffff', curtain=None):
    g = R(x - 4, y - 4, w + 8, h + 8, frame, 3) + R(x, y, w, h, sky) + L(x + w / 2, y, x + w / 2, y + h, frame, 4) + L(x, y + h / 2, x + w, y + h / 2, frame, 4)
    g += Pa(f'M{x+6},{y+h-6} L{x+w*.3},{y+6}', 'none', 'stroke="#ffffff" stroke-width="3" opacity=".5"')
    if curtain:
        g += Pa(f'M{x-8},{y-8} L{x+w*.3},{y-8} Q{x+w*.12},{y+h*.5} {x+w*.2},{y+h+8} L{x-8},{y+h+8} Z', curtain) + Pa(f'M{x+w+8},{y-8} L{x+w*.7},{y-8} Q{x+w*.88},{y+h*.5} {x+w*.8},{y+h+8} L{x+w+8},{y+h+8} Z', curtain)
        g += R(x - 12, y - 12, w + 24, 6, '#8a5a35', 3)
    return g

def room_bg(wall='#f2ead8', floor='#d9b07a', fy=140):
    return R(0, 0, 200, fy, wall) + R(0, fy, 200, 200 - fy, floor) + L(0, fy, 200, fy, shade(floor, -.15), 3)

def sofa(cx, base, w, col='#5aa1d4', s=1):
    h = 56 * s
    g = R(cx - w / 2, base - h, w, h * .62, shade(col, -.08), 12 * s) + R(cx - w / 2 + 8 * s, base - h * .5, w - 16 * s, h * .36, col, 8 * s)
    g += R(cx - w / 2 - 6 * s, base - h * .62, 18 * s, h * .62, shade(col, -.15), 8 * s) + R(cx + w / 2 - 12 * s, base - h * .62, 18 * s, h * .62, shade(col, -.15), 8 * s)
    g += ''.join(L(cx - w / 2 + 8 * s + k * (w - 16 * s) / 2, base - h * .5, cx - w / 2 + 8 * s + k * (w - 16 * s) / 2, base - h * .14, shade(col, -.15), 2) for k in (1,))
    g += R(cx - w / 2, base - h * .14, 6 * s, h * .14, '#5a3a24') + R(cx + w / 2 - 6 * s, base - h * .14, 6 * s, h * .14, '#5a3a24')
    return g

def chair_side(x, base, col=WOOD, s=1):
    g = R(x - 2 * s, base - 100 * s, 7 * s, 100 * s, shade(col, -.1), 2) + R(x, base - 50 * s, 46 * s, 8 * s, col, 2) + R(x + 40 * s, base - 50 * s, 6 * s, 50 * s, shade(col, -.1), 2)
    g += R(x + 2 * s, base - 96 * s, 6 * s, 40 * s, col, 2)
    return g

def table_(cx, top, w, h=60, col=WOOD):
    return R(cx - w / 2, top, w, 10, col, 3) + R(cx - w / 2 + 6, top + 10, 8, h, shade(col, -.15), 2) + R(cx + w / 2 - 14, top + 10, 8, h, shade(col, -.15), 2) + R(cx - w / 2, top + 6, w, 4, shade(col, -.15))

def lamp_(cx, base, h=100, shade_c='#f3d58a', col='#5d6469'):
    return E(cx, base, 20, 5, col) + R(cx - 2, base - h * .7, 4, h * .7, col) + Pa(f'M{cx-26},{base-h*.65} L{cx+26},{base-h*.65} L{cx+16},{base-h} L{cx-16},{base-h} Z', shade_c) + Pa(f'M{cx-26},{base-h*.65} L{cx+26},{base-h*.65} L{cx+30},{base-h*.45} L{cx-30},{base-h*.45} Z', '#fff6c8', 'opacity=".5"')

def bed_(cx, base, w, quilt='#7fb7d8', pillows=1, s=1):
    g = R(cx - w / 2 - 6, base - 90 * s, 12, 90 * s, '#8a5a35', 4) + R(cx + w / 2 - 6, base - 56 * s, 12, 56 * s, '#8a5a35', 4)
    g += R(cx - w / 2, base - 44 * s, w, 26 * s, '#ffffff', 4) + R(cx - w / 2, base - 20 * s, w, 10 * s, '#a8703e', 2)
    pw = (w * .34) / pillows
    for k in range(pillows):
        g += R(cx - w / 2 + 6 + k * (pw + 4), base - 58 * s, pw, 18 * s, '#ffffff', 8) + R(cx - w / 2 + 6 + k * (pw + 4), base - 46 * s, pw, 6 * s, '#e6ecef', 3)
    g += Pa(f'M{cx-w/2+w*.36},{base-50*s} L{cx+w/2},{base-48*s} L{cx+w/2},{base-14*s} L{cx-w/2+w*.32},{base-14*s} Z', quilt) + R(cx - w / 2 + w * .34, base - 50 * s, 14, 36 * s, shade(quilt, .25), 3)
    return g

def wardrobe_(x, y, w, h, col=WOODL):
    g = R(x, y, w, h, col, 3) + L(x + w / 2, y + 4, x + w / 2, y + h - 10, shade(col, -.2), 2) + R(x + w / 2 - 10, y + h * .45, 4, 18, '#5d6469', 2) + R(x + w / 2 + 6, y + h * .45, 4, 18, '#5d6469', 2)
    g += R(x + 6, y + 6, w / 2 - 10, h - 20, shade(col, -.05), 2) + R(x + w / 2 + 4, y + 6, w / 2 - 10, h - 20, shade(col, -.05), 2) + R(x + 4, y + h, 8, 8, '#5a3a24') + R(x + w - 12, y + h, 8, 8, '#5a3a24')
    return g

def drawers_(x, y, w, h, n=4, col=WOODL):
    g = R(x, y, w, h, col, 3)
    dh = (h - 10) / n
    for k in range(n):
        g += R(x + 5, y + 5 + k * dh, w - 10, dh - 4, shade(col, -.06), 2) + R(x + w / 2 - 8, y + 5 + k * dh + dh / 2 - 4, 16, 4, '#5d6469', 2)
    g += R(x + 4, y + h, 8, 6, '#5a3a24') + R(x + w - 12, y + h, 8, 6, '#5a3a24')
    return g

def fork_(x, y, s=1, rot=0):
    return G(R(-3, -10, 6, 80, '#c4cbd0', 3) + R(-9, -40, 18, 34, '#c4cbd0', 5) + ''.join(R(-9 + k * 6, -60, 3, 26, '#c4cbd0', 1) for k in range(4)), f'translate({x},{y}) rotate({rot}) scale({s})')

def knife_(x, y, s=1, rot=0):
    return G(R(-4, 0, 8, 50, '#5a3a24', 3) + Pa('M-4,0 L-4,-70 Q4,-76 6,-60 L4,0 Z', '#c4cbd0') + Ci(0, 12, 1.5, '#d9a33a') + Ci(0, 36, 1.5, '#d9a33a'), f'translate({x},{y}) rotate({rot}) scale({s})')

def spoon_(x, y, s=1, rot=0):
    return G(R(-3, -10, 6, 80, '#c4cbd0', 3) + E(0, -30, 13, 20, '#c4cbd0') + E(-3, -34, 4, 9, '#ffffff', 'opacity=".6"'), f'translate({x},{y}) rotate({rot}) scale({s})')

def pan_(cx, cy, r, s=1, fill='#50565c'):
    return G(Ci(0, 0, r, '#3a3f44') + Ci(0, 0, r * .86, fill) + R(r - 4, -7, r * 1.1, 14, '#2f3437', 7), f'translate({cx},{cy}) scale(1,{.6*s})')

def potk(cx, cy, w, h, col='#a7adb1', lid=True, fill=None):
    g = R(cx - w / 2, cy, w, h, col, 6) + R(cx - w / 2 + 6, cy + 4, 6, h - 10, '#ffffff', 3, 'opacity=".3"') + R(cx - w / 2 - 14, cy + 8, 16, 8, '#2f3437', 4) + R(cx + w / 2 - 2, cy + 8, 16, 8, '#2f3437', 4)
    if lid: g += E(cx, cy, w / 2 + 4, 8, shade(col, -.1)) + Pa(f'M{cx-w/2-2},{cy} Q{cx},{cy-22} {cx+w/2+2},{cy} Z', shade(col, .1)) + R(cx - 8, cy - 22, 16, 8, '#2f3437', 4)
    else: g += E(cx, cy, w / 2, 7, fill or shade(col, -.25))
    return g

def stove_(x, y, w, h, flames=True, big=True):
    g = R(x, y, w, h, '#e6ecef', 4) + R(x, y, w, 10, '#2f3437', 3) + ''.join(Ci(x + 16 + k * 12, y + h - 12, 4, '#5d6469') for k in range(3))
    for k, cx in enumerate((x + w * .28, x + w * .72)):
        g += E(cx, y + 4, w * .16, 4, '#5d6469')
        if flames and (k == 0 or big):
            g += ''.join(Pa(f'M{cx+j*8-6},{y+2} Q{cx+j*8-10},{y-8} {cx+j*8-6},{y-16} Q{cx+j*8-2},{y-8} {cx+j*8-6},{y+2} Z', '#3c7fc1' if not big else '#f08a24') for j in range(3))
    return g

def bubbles(cx, cy, w, n=8, seed=1, col='#ffffff'):
    random.seed(seed)
    return ''.join(Ci(cx + random.uniform(-w / 2, w / 2), cy + random.uniform(-4, 4), random.uniform(2, 5), col) for _ in range(n))

def hand_(x, y, s=1, rot=0, sleeve='#5aa1d4'):
    g = St('M0,60 L0,20', sleeve, 18) + R(-14, -10, 28, 30, SK, 8) + ''.join(R(-13 + k * 7, -26, 6.5, 20, SK, 3) for k in range(4)) + G(R(-4, -14, 9, 22, SK, 4), 'translate(-16,4) rotate(-40)')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def arrow(x1, y1, x2, y2, col='#d9453a', w=4):
    a = math.atan2(y2 - y1, x2 - x1)
    return L(x1, y1, x2 - 6 * math.cos(a), y2 - 6 * math.sin(a), col, w) + Pa(f'M{x2},{y2} L{x2-12*math.cos(a)+7*math.sin(a)},{y2-12*math.sin(a)-7*math.cos(a)} L{x2-12*math.cos(a)-7*math.sin(a)},{y2-12*math.sin(a)+7*math.cos(a)} Z', col)

def person_bust(cx, cy, r, shirt, hair='#3a2a20', style='short', eyes='dot', m='smile', blush=None, w=None):
    return body(cx, cy, r, shirt, w=w) + face_full(cx, cy, r, hair, style, eyes, m, None, blush)

def flower(x, y, s=1, col='#ef8fa4', center='#f3c234'):
    return ''.join(Ci(x + 7 * s * math.cos(k * 1.2566), y + 7 * s * math.sin(k * 1.2566), 6 * s, col) for k in range(5)) + Ci(x, y, 4 * s, center)

# ---------- 城市通用 ----------
SKY = '#bfe6fa'; ROAD = '#6a6f74'; WALK = '#c4bcae'
def sky_ground(gy=150, ground=ROAD, sky=SKY):
    return R(0, 0, 200, gy, sky) + R(0, gy, 200, 200 - gy, ground)

def storefront(x, y, w, h, wall='#f4e6c8', awning='#e2463b', icon='', sign=None, door=True):
    g = R(x, y, w, h, wall) + R(x - 4, y - 6, w + 8, 10, shade(wall, -.2))
    if sign: g += R(x + 8, y + 6, w - 16, 22, sign, 3)
    ay = y + (32 if sign else 6)
    g += ''.join(Pa(f'M{x+k*w/6},{ay} L{x+(k+1)*w/6},{ay} L{x+(k+1)*w/6},{ay+16} Q{x+(k+.5)*w/6},{ay+24} {x+k*w/6},{ay+16} Z', awning if k % 2 == 0 else '#ffffff') for k in range(6))
    wy = ay + 28
    if door:
        g += R(x + 10, wy, w * .55, y + h - wy - 8, '#a9d8f2', 2) + R(x + w * .7, wy, w * .22, y + h - wy, '#5a3a24', 2)
    else:
        g += R(x + 10, wy, w - 20, y + h - wy - 8, '#a9d8f2', 2)
    return g + icon

def sign_post(x, y, w, h, col, inner='', post=True):
    g = ''
    if post: g += R(x + w / 2 - 3, y + h, 6, 190 - y - h, '#5d6469')
    return g + R(x, y, w, h, col, 6) + inner

def person_stand(x, ground, shirt, pants='#3b4a5a', hair='#3a2a20', style='short', arms='down', s=1, coat=None, mood='smile'):
    return person(x, ground, shirt=shirt, pants=pants, hair=hair, style=style, arms=arms, s=s, coat=coat, mood=mood)

def car_side(cx, base, col='#3c7fc1', s=1):
    g = Pa(f'M{-60},{0} L{-60},{-22} Q{-56},{-30} {-40},{-32} L{-26},{-52} Q{-20},{-58} {-8},{-58} L{24},{-58} Q{34},{-58} {40},{-50} L{52},{-32} Q{64},{-30} {64},{-18} L{64},{0} Z', col)
    g += Pa('M-20,-50 L-6,-50 L-6,-34 L-34,-34 Z', '#cfe8f6') + Pa('M0,-50 L22,-50 Q30,-50 34,-44 L42,-34 L0,-34 Z', '#cfe8f6') + R(58, -24, 8, 6, '#f3d058', 2) + R(-62, -22, 6, 6, '#e2463b', 2)
    g += wheel(-34, 0, 13) + wheel(38, 0, 13)
    return G(g, f'translate({cx},{base}) scale({s})')

def money_note(x, y, s=1, rot=0, col='#e2463b'):
    return G(R(-40, -20, 80, 40, col, 3) + R(-34, -14, 68, 28, 'none', 2, 'stroke="#ffffff" stroke-width="1.5" opacity=".6"') + Ci(14, 0, 10, shade(col, .3)) + T(-16, 6, '¥', 16, '#ffffff', 900), f'translate({x},{y}) rotate({rot}) scale({s})')

def coin_(x, y, r=14, col='#d9a33a'):
    return Ci(x, y, r, shade(col, -.15)) + Ci(x, y, r * .8, col) + T(x, y + r * .35, '¥', r, shade(col, -.3), 900)

def card_(x, y, s=1, rot=0, col='#3c7fc1'):
    return G(R(-40, -26, 80, 52, col, 6) + R(-28, -12, 16, 12, '#f3c234', 2) + R(-40, 8, 80, 6, '#2f3437', 0, 'opacity=".0"') + ''.join(R(-28 + k * 16, 8, 12, 4, '#ffffff', 1, 'opacity=".7"') for k in range(4)), f'translate({x},{y}) rotate({rot}) scale({s})')

def envelope_(x, y, w, h, col='#ffffff', stamp=True):
    g = R(x, y, w, h, col, 3) + Pa(f'M{x},{y} L{x+w/2},{y+h*.55} L{x+w},{y}', 'none', 'stroke="#d9dcde" stroke-width="2"')
    if stamp: g += R(x + w - 24, y + 8, 16, 18, '#e2463b', 1)
    return g

def box_(x, y, w, h, col='#c8a070'):
    return Pa(f'M{x},{y+h*.25} L{x+w*.55},{y+h*.25} L{x+w*.55},{y+h} L{x},{y+h} Z', col) + Pa(f'M{x+w*.55},{y+h*.25} L{x+w},{y} L{x+w},{y+h*.75} L{x+w*.55},{y+h} Z', shade(col, -.15)) + Pa(f'M{x},{y+h*.25} L{x+w*.45},{y} L{x+w},{y} L{x+w*.55},{y+h*.25} Z', shade(col, .15)) + St(f'M{x+w*.27},{y+h*.25} L{x+w*.27},{y+h}', '#d9b880', 4)

def price_tag(x, y, s=1, rot=0, col='#f3c234', txt='¥'):
    return G(Pa('M0,0 L50,0 L62,20 L50,40 L0,40 Z', col) + Ci(52, 20, 4, '#ffffff') + T(24, 28, txt, 18, '#2f3437', 900), f'translate({x},{y}) rotate({rot}) scale({s})')

def bag_(x, y, w, h, col='#e2463b'):
    return R(x, y, w, h, col, 4) + R(x + w - 10, y, 10, h, shade(col, -.12), 2) + St(f'M{x+w*.25},{y} Q{x+w*.25},{y-h*.4} {x+w*.5},{y-h*.4} Q{x+w*.75},{y-h*.4} {x+w*.75},{y}', shade(col, -.25), 4)

def cart_(x, y, s=1):
    return G(Pa('M-40,-40 L50,-40 L40,0 L-30,0 Z', '#c4cbd0') + ''.join(L(-36 + k * 12, -40, -28 + k * 10, 0, '#a7adb1', 2) for k in range(8)) + L(-36, -20, 46, -20, '#a7adb1', 2) + St('M-40,-40 L-56,-60 L-68,-60', '#5d6469', 5) + L(-30, 0, -26, 12, '#5d6469', 4) + L(40, 0, 36, 12, '#5d6469', 4) + L(-30, 12, 40, 12, '#5d6469', 4) + wheel(-24, 20, 6) + wheel(34, 20, 6), f'translate({x},{y}) scale({s})')

def flame(x, y, s=1):
    return G(Pa('M0,-60 Q30,-30 24,0 Q20,20 0,22 Q-22,20 -24,0 Q-28,-24 -10,-40 Q-8,-20 2,-18 Q-4,-40 0,-60 Z', '#f08a24') + Pa('M0,-20 Q14,-6 10,8 Q6,16 0,16 Q-8,14 -10,4 Q-10,-8 0,-20 Z', '#f3c234'), f'translate({x},{y}) scale({s})')

def bolt_icon(x, y, s=1, col='#f3c234'):
    return G(Pa('M6,-40 L-18,4 L-2,4 L-10,40 L18,-6 L2,-6 L12,-40 Z', col), f'translate({x},{y}) scale({s})')

def cross_sign(x, y, s=1, col='#e2463b'):
    return G(R(-6, -18, 12, 36, col, 2) + R(-18, -6, 36, 12, col, 2), f'translate({x},{y}) scale({s})')
