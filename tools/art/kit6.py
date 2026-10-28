from kit5 import *

def quad(x, base, s=1, col='#c8903a', belly=None, leg_h=40, body_w=60, body_h=30, head=(52, -62), head_r=18, snout=None, ears='round', ear_col=None, tail='thin', tail_col=None, eye=True, neck=False, legcol=None, hoof=None, face_left=False):
    """generic side-view quadruped facing right. base = ground y"""
    k = s
    g = ''
    bx, by = 0, -leg_h - body_h * .6
    lc = legcol or shade(col, -.06)
    # tail
    tc = tail_col or col
    if tail == 'thin': g += St(f'M{-body_w*.9},{by-6} Q{-body_w*1.3},{by+4} {-body_w*1.25},{by+26}', tc, 4)
    elif tail == 'bushy': g += Pa(f'M{-body_w*.85},{by-6} Q{-body_w*1.6},{by-30} {-body_w*1.5},{by+20} Q{-body_w*1.2},{by+10} {-body_w*.85},{by+4} Z', tc)
    elif tail == 'tuft': g += St(f'M{-body_w*.9},{by-6} Q{-body_w*1.2},{by+10} {-body_w*1.15},{by+30}', tc, 3) + E(-body_w * 1.15, by + 34, 5, 8, shade(tc, -.3))
    elif tail == 'short': g += E(-body_w * .95, by - 10, 8, 6, tc)
    elif tail == 'curly': g += St(f'M{-body_w*.9},{by-8} q-12,-4 -10,6 q2,8 8,2', tc, 3)
    # back legs
    for lx in (-body_w * .6, body_w * .55):
        g += R(lx - 7, by + body_h * .3, 14, leg_h + body_h * .3, shade(lc, -.12), 5)
    g += E(bx, by, body_w, body_h, col)
    if belly: g += E(bx + 4, by + body_h * .45, body_w * .7, body_h * .45, belly)
    for lx in (-body_w * .45, body_w * .7):
        g += R(lx - 7, by + body_h * .3, 14, leg_h + body_h * .3, lc, 5)
        if hoof: g += R(lx - 7, -6, 14, 6, hoof, 2)
    hx, hy = head
    if neck: g += Pa(f'M{body_w*.5},{by-body_h*.5} L{hx-head_r*.6},{hy} L{hx+head_r*.4},{hy+head_r*.6} L{body_w*.95},{by} Z', col)
    # ears
    ec = ear_col or shade(col, -.15)
    if ears == 'round': g += Ci(hx - head_r * .6, hy - head_r * .8, head_r * .35, ec) + Ci(hx + head_r * .3, hy - head_r * .9, head_r * .35, ec)
    elif ears == 'point': g += Pa(f'M{hx-head_r*.8},{hy-head_r*.5} L{hx-head_r*.5},{hy-head_r*1.5} L{hx-head_r*.1},{hy-head_r*.8} Z', ec) + Pa(f'M{hx},{hy-head_r*.8} L{hx+head_r*.3},{hy-head_r*1.6} L{hx+head_r*.6},{hy-head_r*.6} Z', ec)
    elif ears == 'long': g += E(hx - head_r * .4, hy - head_r * 1.5, head_r * .25, head_r * .9, ec) + E(hx, hy - head_r * 1.6, head_r * .25, head_r * .9, ec)
    elif ears == 'droop': g += E(hx - head_r * .6, hy, head_r * .3, head_r * .7, ec)
    g += Ci(hx, hy, head_r, col)
    if snout: g += E(hx + head_r * .8, hy + head_r * .3, head_r * .55, head_r * .45, snout) + Ci(hx + head_r * 1.2, hy + head_r * .2, head_r * .12, '#2f3437')
    if eye: g += Ci(hx + head_r * .3, hy - head_r * .2, head_r * .13, '#2f3437') + Ci(hx + head_r * .34, hy - head_r * .25, head_r * .05, '#ffffff')
    tr = f'translate({x},{base}) scale({-k if face_left else k},{k})'
    return G(g, tr)
def bird(x, y, s=1, col='#8a6a4a', belly='#e6dcc8', beak='#f3c234', wing=None, tail_len=20, legs=True, crest=None, rot=0, eye_ring=None, leg_col='#e0a040', beak_len=10):
    w = wing or shade(col, -.15)
    g = Pa(f'M-16,0 L{-16-tail_len},-6 L{-16-tail_len},6 Z', shade(col, -.2))
    if legs: g += L(-4, 14, -6, 30, leg_col, 2) + L(4, 14, 6, 30, leg_col, 2) + L(-10, 30, 0, 30, leg_col, 2) + L(0, 30, 12, 30, leg_col, 2)
    g += E(0, 0, 22, 16, col) + E(4, 6, 14, 9, belly) + E(-4, -2, 14, 8, w, 'transform="rotate(-10)"') + Ci(18, -12, 11, col)
    if crest: g += Pa('M14,-22 L10,-36 L20,-26 L22,-38 L26,-22 Z', crest)
    g += Pa(f'M27,-14 L{27+beak_len},-10 L27,-8 Z', beak)
    if eye_ring: g += Ci(21, -14, 4, eye_ring)
    g += Ci(21, -14, 2.4, '#2f3437')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
def flying_bird(x, y, s=1, col='#2f3437'):
    return G(Pa('M-30,0 Q-14,-16 0,0 Q14,-16 30,0 Q14,-8 0,4 Q-14,-8 -30,0 Z', col), f'translate({x},{y}) scale({s})')
def insect_body(x, y, s=1, col='#2f3437'):
    return G(E(0, 0, 10, 14, col) + Ci(0, -16, 7, col) + ''.join(L(-8, -4 + k * 7, -22, -8 + k * 10, col, 2) + L(8, -4 + k * 7, 22, -8 + k * 10, col, 2) for k in range(3)) + L(-3, -22, -10, -34, col, 1.5) + L(3, -22, 10, -34, col, 1.5), f'translate({x},{y}) scale({s})')
def fish2(x, y, s=1, col='#f08a24', fin=None, stripes=None, rot=0):
    f = fin or shade(col, -.15)
    g = Pa('M-30,0 L-48,-16 L-44,0 L-48,16 Z', f) + E(0, 0, 32, 18, col) + Pa('M-6,-16 L8,-26 L14,-14 Z', f)
    if stripes: g += ''.join(Pa(f'M{-10+k*12},-17 Q{-6+k*12},0 {-10+k*12},17 L{-4+k*12},16 Q{0+k*12},0 {-4+k*12},-16 Z', stripes) for k in range(2))
    g += Ci(18, -4, 4, '#ffffff') + Ci(19, -4, 2.5, '#2f3437')
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')
def leaf_shape(x, y, s=1, col='#5aaa3a', rot=0, kind='oval'):
    if kind == 'maple':
        d = 'M0,40 L0,20 L-30,26 L-22,10 L-40,-6 L-20,-8 L-24,-30 L-8,-20 L0,-44 L8,-20 L24,-30 L20,-8 L40,-6 L22,10 L30,26 L0,20 Z'
    elif kind == 'ginkgo':
        d = 'M0,40 L0,10 Q-40,-10 -36,-30 Q0,-44 36,-30 Q40,-10 0,10 Z'
    elif kind == 'oak':
        d = 'M0,44 L0,30 Q-14,30 -12,20 Q-24,16 -18,6 Q-28,-2 -18,-10 Q-24,-22 -10,-24 Q-8,-38 0,-40 Q8,-38 10,-24 Q24,-22 18,-10 Q28,-2 18,6 Q24,16 12,20 Q14,30 0,30 Z'
    else:
        d = 'M0,40 Q-26,10 0,-40 Q26,10 0,40 Z'
    return G(Pa(d, col) + L(0, 40, 0, -30, shade(col, -.2), 1.5), f'translate({x},{y}) rotate({rot}) scale({s})')
def mushroom(x, base, s=1, cap='#e2463b', stem='#f6efe0', spots=True, shape='dome'):
    g = R(-10, -40, 20, 40, stem, 6)
    if shape == 'dome': g += Pa('M-34,-36 Q-34,-74 0,-74 Q34,-74 34,-36 Z', cap)
    elif shape == 'flat': g += Pa('M-40,-36 Q-30,-56 0,-58 Q30,-56 40,-36 Z', cap)
    elif shape == 'bell': g += Pa('M-14,-36 Q-16,-70 0,-74 Q16,-70 14,-36 Z', cap)
    if spots: g += ''.join(Ci(dx, dy, r_, '#ffffff') for dx, dy, r_ in [(-16, -54, 5), (6, -62, 6), (20, -46, 4), (-4, -44, 3)])
    return G(g, f'translate({x},{base}) scale({s})')
def big_tree(x, base, s=1, crown='#4a9a3a', trunk='#8a5a35'):
    return G(R(-10, -60, 20, 60, trunk, 3) + Ci(0, -90, 44, crown) + Ci(-30, -70, 30, shade(crown, .08)) + Ci(30, -70, 30, shade(crown, -.05)), f'translate({x},{base}) scale({s})')
def blossom_branch(x, y, s=1, col='#f6c8dc', center='#e2463b'):
    return G(St('M-80,40 Q-20,0 80,-30', '#6a4a3a', 5) + St('M-20,10 Q0,-20 20,-40', '#6a4a3a', 3) + ''.join(flower(dx, dy, 1.2, col, center) for dx, dy in [(-50, 20), (-10, 0), (30, -16), (60, -26), (10, -30)]), f'translate({x},{y}) scale({s})')

def volcano_(x, base, s=1, erupt=True):
    g = Pa('M-90,0 L-24,-90 L24,-90 L90,0 Z', '#8a6a5a') + Pa('M-24,-90 L24,-90 L10,-70 Q0,-60 -10,-72 Z', '#5d4a40')
    if erupt: g += Pa('M-20,-92 Q0,-110 20,-92 L14,-60 Q8,-40 0,-70 Q-8,-40 -14,-60 Z', '#e2463b') + ''.join(Ci(-30 + k * 15, -110 - (k % 2) * 20, 14, '#8a837c', 'opacity=".7"') for k in range(5)) + Pa('M-10,-80 Q-30,-40 -40,0 L-30,0 Q-20,-40 -4,-70 Z', '#f08a24')
    return G(g, f'translate({x},{base}) scale({s})')
def cave_(x, base, s=1):
    return G(Pa('M-90,0 Q-90,-110 0,-110 Q90,-110 90,0 Z', '#8a7a6a') + Pa('M-46,0 Q-46,-70 0,-70 Q46,-70 46,0 Z', '#2a2420') + ''.join(Pa(f'M{-36+k*18},-62 l6,14 l6,-14 Z', '#8a7a6a') for k in range(4)), f'translate({x},{base}) scale({s})')
def rock_(x, y, s=1, col='#8a9196'):
    return G(Pa('M-50,30 L-56,-4 L-30,-34 L10,-40 L46,-20 L56,20 L30,36 Z', col) + Pa('M-30,-34 L10,-40 L0,-6 L-40,0 Z', shade(col, .15)) + Pa('M10,-40 L46,-20 L20,4 L0,-6 Z', shade(col, .05)), f'translate({x},{y}) scale({s})')

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


def yarn_ball(x, y, r, col='#ef8fa4'):
    return Ci(x, y, r, col) + ''.join(St(f'M{x-r*math.cos(a)},{y-r*math.sin(a)} Q{x},{y} {x+r*math.cos(a+.6)},{y+r*math.sin(a+.6)}', shade(col, -.15), 2) for a in [k * .6 for k in range(6)])
def shell_(x, y, s=1, col='#f6c8b0'):
    return G(Pa('M0,20 L-30,-10 Q-20,-34 0,-36 Q20,-34 30,-10 Z', col) + ''.join(L(0, 20, -26 + k * 10.4, -18 + abs(k - 2.5) * -3, shade(col, -.2), 2) for k in range(6)) + R(-8, 16, 16, 8, shade(col, -.1), 3), f'translate({x},{y}) scale({s})')
def meadow(y=150, sky=SKY):
    return R(0, 0, 200, 200, sky) + R(0, y, 200, 200 - y, '#9ac070')
def forest_bg(y=150):
    return R(0, 0, 200, 200, '#dff1d8') + pine(20, y, .6) + pine(180, y, .7) + R(0, y, 200, 200 - y, '#7aa050')
def snow_land(y=150):
    return R(0, 0, 200, 200, '#cfe2f0') + R(0, y, 200, 200 - y, '#ffffff')


def bee_(x, y, s=1):
    return G(E(-6, -16, 12, 8, '#dff1fb', 'opacity=".9" transform="rotate(-30 -6 -16)"') + E(8, -16, 12, 8, '#dff1fb', 'opacity=".9" transform="rotate(30 8 -16)"') + E(0, 0, 22, 15, '#f3c234') + R(-8, -14, 6, 28, '#2f3437') + R(6, -14, 6, 28, '#2f3437') + Ci(22, -2, 9, '#2f3437') + Ci(24, -4, 2, '#ffffff') + Pa('M-22,0 L-30,0 L-22,4 Z', '#2f3437'), f'translate({x},{y}) scale({s})')
def frog_(x, y, s=1, col='#5aaa3a'):
    return G(E(0, 10, 34, 24, col) + E(0, 18, 22, 14, '#c8e0a0') + Ci(-16, -14, 12, col) + Ci(16, -14, 12, col) + Ci(-16, -16, 7, '#ffffff') + Ci(16, -16, 7, '#ffffff') + Ci(-15, -16, 4, '#2f3437') + Ci(17, -16, 4, '#2f3437') + St('M-14,2 Q0,10 14,2', '#2f6a2a', 2) + St('M-30,20 Q-50,30 -40,40 L-24,36', col, 8) + St('M30,20 Q50,30 40,40 L24,36', col, 8), f'translate({x},{y}) scale({s})')
def fruit_tree(x, base, s=1):
    return G(R(-6, -40, 12, 40, '#8a5a35') + Ci(0, -60, 34, '#4a9a3a') + Ci(-20, -44, 22, '#5aaa3a') + Ci(20, -44, 22, '#5aaa3a') + ''.join(Ci(dx, dy, 5, '#e2463b') for dx, dy in [(-14, -64), (10, -70), (18, -48), (-20, -42), (2, -50)]), f'translate({x},{base}) scale({s})')

