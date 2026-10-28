from kit5 import *

def ring_bg():
    return R(0, 0, 200, 200, '#2f3a5a') + Pa('M0,150 L200,150 L200,200 L0,200 Z', '#3c7fc1') + R(0, 146, 200, 6, '#ffffff') + ''.join(L(0, 70 + k * 22, 200, 70 + k * 22, ['#e2463b', '#ffffff', '#3c7fc1'][k], 4) for k in range(3)) + R(4, 60, 10, 92, '#c4cbd0') + R(186, 60, 10, 92, '#c4cbd0')
def glove_box(x, y, s=1, col='#e2463b', rot=0):
    return G(R(-22, -26, 44, 46, col, 18) + Ci(-16, 0, 12, col) + R(-20, 16, 40, 18, '#ffffff', 4) + hi(-8, -14, 8, 5, .4), f'translate({x},{y}) rotate({rot}) scale({s})')
def boxer(x, ground, s=1, col='#e2463b', mood='flat', punch=False):
    k = s
    sh = (x, ground - 128 * k)
    fa = [(x + 10 * k, ground - 124 * k), (x + 40 * k, ground - 122 * k), (x + 66 * k, ground - 126 * k)] if punch else [(x + 10 * k, ground - 124 * k), (x + 26 * k, ground - 104 * k), (x + 22 * k, ground - 136 * k)]
    g = pose((x, ground - 152 * k), sh, (x, ground - 74 * k), arms=[fa], legs=[[(x - 4 * k, ground - 74 * k), (x - 16 * k, ground - 36 * k), (x - 20 * k, ground - 4 * k)], [(x + 4 * k, ground - 74 * k), (x + 18 * k, ground - 36 * k), (x + 22 * k, ground - 4 * k)]], back_arm=[[(x - 10 * k, ground - 124 * k), (x - 2 * k, ground - 104 * k), (x + 6 * k, ground - 134 * k)]], shirt=SK, pants=col, hr=15 * k, tw=30 * k, lw=13 * k, aw=10 * k, mood=mood, shoes='#2f3437')
    return g + glove_box(fa[-1][0], fa[-1][1], .5 * k, col) + glove_box(x + 6 * k, ground - 134 * k, .5 * k, col)
def gi_fighter(x, ground, s=1, belt='#2f3437', col='#ffffff', arms='front', legs='stand', mood='flat'):
    g = W(x, ground, s, col, col, '', None, arms, legs, mood=mood)
    return g + R(x - 18 * s, ground - 78 * s, 36 * s, 6 * s, belt) + Pa(f'M{x-6*s},{ground-128*s} L{x},{ground-112*s} L{x+6*s},{ground-128*s}', 'none', f'stroke="#c4cbd0" stroke-width="{2*s}"')
def mat_bg(col='#e8c040'):
    return R(0, 0, 200, 200, '#e8eef2') + R(0, 130, 200, 70, col) + R(20, 140, 160, 50, shade(col, -.08))
def swimmer(x, y, s=1, cap='#e2463b', stroke='free', skin=SK):
    k = s
    g = E(x, y, 46 * k, 9 * k, shade('#3c7fc1', .1))
    if stroke == 'free':
        g += St(f'M{x-50*k},{y} L{x+30*k},{y}', skin, 16 * k) + arm([(x + 20 * k, y - 2 * k), (x + 40 * k, y - 30 * k), (x + 66 * k, y - 10 * k)], skin, skin, 10 * k) + St(f'M{x-50*k},{y} l-20,4 M{x-50*k},{y} l-20,-4', skin, 9 * k)
        g += Ci(x + 34 * k, y - 2 * k, 12 * k, skin) + Pa(f'M{x+22*k},{y-2*k} A{12*k},{12*k} 0 0,1 {x+46*k},{y-2*k} Z', cap) + E(x + 42 * k, y - 2 * k, 5 * k, 3 * k, '#2f3437')
    return g
def wave_lines(y, col='#8fd0f0'):
    return ''.join(St(f'M{-10+k*40},{y} q10,-6 20,0 t20,0', col, 3) for k in range(6))
def boat_hull(x, y, w, col='#e2463b'):
    return Pa(f'M{x-w/2},{y} L{x+w/2},{y} L{x+w/2-14},{y+20} L{x-w/2+10},{y+20} Z', col)
def sailboat(x, y, s=1, col='#ffffff', hull='#e2463b'):
    return G(R(-2, -110, 4, 110, '#8a5a35') + Pa('M2,-106 L60,-10 L2,-10 Z', col) + Pa('M-2,-96 L-40,-14 L-2,-14 Z', shade(col, -.06)) + boat_hull(0, 0, 110, hull), f'translate({x},{y}) scale({s})')
def surfboard(x, y, s=1, rot=0, col='#f08a24'):
    return G(E(0, 0, 70, 16, col) + L(-64, 0, 64, 0, '#ffffff', 3) + Pa('M-50,10 L-60,24 L-40,12 Z', shade(col, -.2)), f'translate({x},{y}) rotate({rot}) scale({s})')
def kayak_(x, y, s=1, col='#f3c234'):
    return G(Pa('M-80,0 Q0,-18 80,0 Q0,16 -80,0 Z', col) + E(0, -4, 18, 6, '#2f3437'), f'translate({x},{y}) scale({s})')
def paddle_(x, y, s=1, rot=0, double=True):
    return G(R(-2, -60, 4, 120, '#8a5a35') + E(0, -64, 7, 16, '#e2463b') + (E(0, 64, 7, 16, '#e2463b') if double else ''), f'translate({x},{y}) rotate({rot}) scale({s})')
def horse_(x, base, s=1, col='#8a5a35', mane='#3a2a20', gait='stand'):
    k = s
    legs = {'stand': [(-40, 0), (-28, 0), (32, 0), (44, 0)], 'gallop': [(-60, -10), (-30, 4), (40, -4), (66, -20)], 'trot': [(-48, 0), (-24, -10), (30, -10), (48, 0)]}[gait]
    g = ''
    for i, (lx, ly) in enumerate(legs):
        sx = -36 if i < 2 else 36
        g += St(f'M{sx},-50 L{(sx+lx)/2},{-26+ly/2} L{lx},{ly}', shade(col, -.1) if i % 2 else col, 10) + R(lx - 6, ly - 4, 12, 6, '#2f3437', 2)
    g += E(0, -60, 54, 26, col) + Pa('M34,-72 L60,-118 L76,-112 L56,-62 Z', col) + Pa('M56,-118 Q72,-130 88,-112 L94,-98 Q90,-92 82,-96 L70,-104 Z', col) + Ci(72, -114, 2.5, '#2f3437') + Pa('M60,-120 L58,-132 L66,-122 Z', col)
    g += Pa('M34,-76 Q46,-104 58,-124 Q50,-100 44,-74 Z', mane) + St('M-52,-66 Q-74,-60 -76,-20', mane, 8)
    return G(g, f'translate({x},{base}) scale({k})')
def rider(x, y, s=1, col='#e2463b', hat='#2f3437'):
    k = s
    return pose((x, y - 74 * k), (x, y - 54 * k), (x - 4 * k, y - 10 * k), arms=[[(x + 6 * k, y - 50 * k), (x + 22 * k, y - 30 * k), (x + 40 * k, y - 32 * k)]], legs=[[(x - 4 * k, y - 10 * k), (x + 14 * k, y + 10 * k), (x + 8 * k, y + 34 * k)]], shirt=col, pants='#ffffff', hr=12 * k, tw=24 * k, lw=10 * k, aw=8 * k, shoes='#2f3437') + Pa(f'M{x-13*k},{y-76*k} Q{x},{y-96*k} {x+13*k},{y-76*k} Z', hat) + R(x - 4 * k, y - 78 * k, 22 * k, 4 * k, hat, 2)
def fisher_sit(x, y, s=1, col='#5ba644', hat=True):
    k = s
    g = pose((x, y - 70 * k), (x, y - 48 * k), (x, y), arms=[[(x + 8 * k, y - 44 * k), (x + 26 * k, y - 30 * k), (x + 40 * k, y - 36 * k)]], legs=[[(x, y), (x + 30 * k, y + 2 * k), (x + 34 * k, y + 34 * k)]], shirt=col, pants='#3b4a5a', hr=13 * k, tw=26 * k, lw=12 * k, aw=9 * k)
    if hat: g += hat_('straw', x, y - 70 * k, 13 * k)
    return g
def rod(x1, y1, x2, y2, line_to=None):
    g = L(x1, y1, x2, y2, '#5d6469', 3) + Ci(x1 + (x2 - x1) * .15, y1 + (y2 - y1) * .15, 5, '#2f3437')
    if line_to: g += St(f'M{x2},{y2} Q{(x2+line_to[0])/2+10},{min(y2,line_to[1])-10} {line_to[0]},{line_to[1]}', '#5d6469', 1)
    return g
def hook_(x, y, s=1):
    return G(St('M0,-40 L0,10 Q0,26 -14,26 Q-26,26 -26,12', '#8a9196', 4) + Pa('M-26,12 L-32,4 L-22,6 Z', '#8a9196') + Ci(0, -42, 5, 'none', 'stroke="#8a9196" stroke-width="3"'), f'translate({x},{y}) scale({s})')
def worm(x, y, s=1):
    return G(St('M0,0 q10,-14 20,0 t20,0 t20,0', '#e08a8a', 8), f'translate({x},{y}) scale({s})')
def bobber_(x, y, s=1):
    return G(Ci(0, 0, 14, '#ffffff') + Pa('M-14,0 A14,14 0 0,1 14,0 Z', '#e2463b') + R(-2, -26, 4, 14, '#5d6469') + L(0, 14, 0, 30, '#5d6469', 1), f'translate({x},{y}) scale({s})')
def reel_(x, y, s=1):
    return G(Ci(0, 0, 30, '#a7adb1') + Ci(0, 0, 22, '#5d6469') + Ci(0, 0, 8, '#c4cbd0') + R(26, -4, 26, 8, '#5d6469', 3) + Ci(52, 0, 7, '#2f3437') + R(-6, -50, 12, 22, '#5d6469', 3), f'translate({x},{y}) scale({s})')
def locker_(x, y, w, h, col='#5aa1d4'):
    return R(x, y, w, h, col, 3) + ''.join(R(x + 6, y + 8 + k * 6, w - 12, 3, shade(col, -.15)) for k in range(3)) + R(x + w - 10, y + h / 2 - 8, 4, 16, '#2f3437', 2)

# ================= 格斗 =================
S_('boxing', ring_bg() + boxer(60, 190, .8, '#e2463b', punch=True) + G(boxer(0, 0, .8, '#3c7fc1'), 'translate(150,190) scale(-1,1)'), False)
S_('punch', glove_box(90, 100, 2.4, '#e2463b', 0) + ''.join(L(150, 70 + k * 30, 190, 70 + k * 30, '#a7adb1', 4) for k in range(3)) + burst(40, 90, 20, '#f3c234', 10) if False else ''.join(L(10, 70 + k * 30, 50, 70 + k * 30, '#a7adb1', 4) for k in range(3)) + glove_box(100, 100, 2.4, '#e2463b', 90) + burst(170, 100, 22, '#f3c234', 10))
S_('ring-combat', ring_bg() + R(0, 140, 200, 14, '#ffffff', 0, 'opacity=".2"'), False)
S_('round', ring_bg() + G(R(-40, -50, 80, 60, '#ffffff', 6) + T(0, -6, '3', 44, '#e2463b', 900), 'translate(100,110)') + pose((100, 150), (100, 166), (100, 196), arms=[[(108, 170), (130, 120)]], legs=[], shirt='#ef8fa4', pants='#ef8fa4', style='long', hair='#3a2a20', hr=10, tw=20, aw=7), False)
S_('kung-fu', R(0, 0, 200, 200, '#f6e8d0') + R(0, 160, 200, 40, '#c8903a') + pose((80, 60), (84, 82), (90, 130), arms=[[(92, 86), (120, 80), (150, 82)]], legs=[[(90, 130), (130, 116), (170, 106)], [(88, 130), (80, 160), (76, 190)]], back_arm=[[(80, 86), (60, 70), (50, 60)]], shirt='#2f3437', pants='#2f3437', hr=14, tw=28, mood='flat') + R(76, 112, 28, 6, '#e2463b') + Ci(150, 30, 0, '#000') + lantern(170, 20, .5), False)
S_('karate', mat_bg('#e8e0c0') + pose((90, 50), (92, 72), (96, 120), arms=[[(100, 76), (130, 70), (160, 74)]], legs=[[(96, 120), (70, 150), (60, 180)], [(98, 120), (130, 150), (140, 180)]], back_arm=[[(86, 76), (70, 96), (84, 104)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=30, mood='flat') + R(78, 108, 36, 6, '#2f3437'), False)
S_('judo', mat_bg('#e8c040') + gi_fighter(70, 186, .8, '#2f3437', '#ffffff', 'front') + gi_fighter(130, 186, .8, '#2f3437', '#3c7fc1', 'front') + St('M80,90 L120,90', '#c4cbd0', 0), False)
S_('taekwondo', mat_bg('#3c7fc1') + pose((60, 70), (66, 92), (80, 134), arms=[[(72, 96), (60, 120)]], legs=[[(80, 134), (120, 110), (166, 84)], [(78, 134), (76, 164), (72, 190)]], back_arm=[[(62, 96), (44, 110)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28, mood='flat') + R(64, 122, 30, 6, '#2f3437') + Pa('M50,80 Q60,60 70,80 L66,90 L54,90 Z', '#e2463b', 'opacity="0"') + Pa('M46,64 Q60,52 74,64 L74,74 L46,74 Z', '#e2463b'), False)
S_('wrestling', mat_bg('#e2463b') + E(100, 165, 80, 20, '#ffffff', 'opacity=".25"') + pose((70, 110), (82, 120), (120, 130), arms=[[(84, 124), (110, 140), (128, 150)]], legs=[[(120, 130), (140, 160), (150, 180)], [(122, 130), (160, 150), (176, 170)]], shirt='#3c7fc1', pants='#3c7fc1', hr=13, tw=26) + pose((130, 90), (120, 102), (90, 120), arms=[[(118, 104), (100, 130), (90, 150)]], legs=[[(90, 120), (60, 150), (50, 180)], [(92, 120), (70, 160), (66, 186)]], shirt='#e2463b', pants='#e2463b', hr=13, tw=26), False)
S_('fencing', R(0, 0, 200, 200, '#e8eef2') + R(0, 170, 200, 30, '#a7adb1') + ''.join(G(pose((0, -150), (0, -126), (0, -74), arms=[[(8, -122), (34, -110), (56, -112)]], legs=[[(-2, -74), (-30, -38), (-36, -4)], [(2, -74), (26, -38), (30, -4)]], back_arm=[[(-8, -122), (-24, -140), (-12, -156)]], shirt='#ffffff', pants='#ffffff', hr=15, tw=30, shoes='#ffffff') + Ci(0, -150, 15, '#2f3437') + R(-12, -160, 24, 20, '#5d6469', 4, 'opacity=".6"') + L(56, -112, 110, -120, '#c4cbd0', 2), f'translate({x},194) scale({d*.62},.62)') for x, d in [(50, 1), (150, -1)]), False)
S_('boxing-gloves', glove_box(70, 100, 1.8, '#e2463b', -15) + glove_box(130, 110, 1.8, '#e2463b', 15) + St('M70,140 Q100,170 130,150', '#ffffff', 3))
S_('black-belt', G(R(-80, -8, 160, 16, '#2f3437', 3) + R(-14, -14, 28, 28, '#2f3437', 4) + Pa('M-10,10 L-30,60 L-16,62 L0,14 Z', '#2f3437') + Pa('M10,10 L30,60 L16,62 L0,14 Z', '#2f3437') + R(-28, 46, 12, 4, '#d9a33a') + R(16, 46, 12, 4, '#d9a33a'), 'translate(100,80)'))
S_('knockout', ring_bg() + lying(20, 140, SK, '#3c7fc1', 'sleep', .8) + boxer(150, 190, .7, '#e2463b') + ''.join(star(40 + k * 14, 110 - (k % 2) * 8, 5) for k in range(3)), False)
S_('defend', ring_bg() + pose((100, 60), (100, 82), (100, 130), arms=[[(108, 86), (110, 70), (104, 54)]], legs=[[(96, 130), (84, 180)], [(104, 130), (116, 180)]], back_arm=[[(92, 86), (90, 70), (96, 54)]], shirt=SK, pants='#3c7fc1', hr=15, tw=30, mood='flat') + glove_box(104, 54, .5, '#3c7fc1') + glove_box(96, 58, .5, '#3c7fc1') + G(Pa('M0,-30 L28,-18 L28,8 Q28,30 0,40 Q-28,30 -28,8 L-28,-18 Z', '#5ba644', 'opacity=".5"'), 'translate(150,60)'), False)
S_('bow', mat_bg('#e8e0c0') + gi_fighter(50, 186, .7, '#2f3437') + G(pose((0, -100), (0, -86), (16, -50), arms=[[(4, -86), (10, -60)]], legs=[[(16, -50), (16, -2)], [(18, -50), (20, -2)]], shirt='#ffffff', pants='#ffffff', hr=11, tw=22, mood='flat'), 'translate(130,186) rotate(-40 16 -50)') + R(126, 140, 30, 5, '#2f3437', 0, 'transform="rotate(50 141 142)"'), False)
S_('sumo', R(0, 0, 200, 200, '#f6e8d0') + Ci(100, 180, 90, '#d9c28a') + Ci(100, 180, 80, 'none', 'stroke="#ffffff" stroke-width="3"') + E(100, 120, 50, 50, SK) + Ci(100, 60, 18, SK) + Ci(100, 46, 8, '#2f3437') + Pa('M84,52 Q100,38 116,52 L116,56 L84,56 Z', '#2f3437') + face(100, 62, 16, 'flat') + R(54, 140, 92, 22, '#3c4a8a', 6) + R(90, 140, 20, 40, '#3c4a8a', 4) + E(70, 180, 14, 20, SK) + E(130, 180, 14, 20, SK) + E(52, 120, 12, 20, SK) + E(148, 120, 12, 20, SK), False)

# ================= 游泳 =================
S_('swim', pool_bg(60) + swimmer(90, 130, 1.1) + lane_rope(90) + lane_rope(170), False)
S_('swimming-pool', R(0, 0, 200, 200, '#e8f0f4') + R(10, 60, 180, 130, '#5ab4e0', 4) + ''.join(lane_rope(80 + k * 30) for k in range(4)) + R(10, 56, 180, 6, '#ffffff') + St('M160,56 L160,24 M176,56 L176,24 M160,36 L176,36 M160,46 L176,46', '#c4cbd0', 3), False)
S_('lifeguard', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#f0d890') + R(0, 120, 200, 30, '#3c9ad4') + St('M60,150 L76,60 M120,150 L104,60 M68,110 L112,110', '#ffffff', 5) + R(70, 54, 40, 10, '#ffffff') + W(90, 56, .3, '#e2463b', '#e2463b') + G(Ci(0, 0, 20, '#e2463b') + Ci(0, 0, 10, SKY) + ''.join(R(-4, -20, 8, 10, '#ffffff', 0, f'transform="rotate({a})"') for a in (0, 90, 180, 270)), 'translate(150,100)') + R(130, 20, 4, 40, '#5d6469') + Pa('M134,20 L160,26 L134,32 Z', '#e2463b'), False)
S_('deep', R(0, 0, 200, 200, '#2a6a9a') + R(0, 0, 200, 30, '#e8f0f4') + R(0, 30, 200, 170, '#2f6aa0') + R(0, 30, 200, 60, '#4a8ac0') + St('M30,40 L30,180', '#ffffff', 2, 'stroke-dasharray="6 4"') + Pa('M24,180 L36,180 L30,190 Z', '#ffffff') + T(110, 120, '3 m', 30, '#ffffff', 900) + ''.join(Ci(150 + k * 6, 160 - k * 20, 4 + k, '#9fd0ec', 'opacity=".6"') for k in range(4)), False)
S_('shallow', R(0, 0, 200, 200, '#e8f0f4') + R(0, 120, 200, 80, '#9fd8f0') + fig(100, 196, 'girl', s=1.2) + R(0, 150, 200, 50, '#9fd8f0', 0, 'opacity=".7"') + T(160, 60, '0.5 m', 20, '#3c7fc1', 900), False)
S_('dive', R(0, 0, 200, 200, '#e8f0f4') + R(0, 150, 200, 50, '#5ab4e0') + R(0, 40, 70, 8, '#ffffff') + R(10, 48, 10, 102, '#c4cbd0') + pose((140, 110), (130, 92), (110, 60), arms=[[(134, 96), (146, 112), (152, 128)]], legs=[[(110, 60), (90, 40), (76, 30)]], back_arm=[[(130, 96), (142, 116), (148, 132)]], shirt='#e2463b', pants='#e2463b', hr=12, tw=22) + ''.join(Ci(150 + k * 10, 160 - (k % 2) * 6, 5, '#ffffff') for k in range(3)), False)
S_('float', pool_bg(40) + E(100, 120, 70, 14, '#5ab4e0') + lying(40, 112, '#e2463b', '#e2463b', 'smile', .9) + St('M20,130 q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', '#ffffff', 3), False)
S_('goggles', G(R(-70, -26, 60, 52, '#3c7fc1', 24, 'opacity=".85"') + R(10, -26, 60, 52, '#3c7fc1', 24, 'opacity=".85"') + R(-10, -6, 20, 8, '#2f3437', 3) + St('M-70,0 Q-96,0 -96,30 M70,0 Q96,0 96,30', '#2f3437', 6) + hi(-50, -10, 10, 5, .6) + hi(30, -10, 10, 5, .6), 'translate(100,100)'))
S_('swimming-cap', Pa('M30,140 Q30,40 100,40 Q170,40 170,140 Z', '#e2463b') + hi(70, 70, 20, 8, .4, -30) + R(26, 136, 148, 12, shade('#e2463b', -.15), 6))
S_('breaststroke', pool_bg(40) + E(100, 120, 60, 12, '#4a9ad0') + Ci(100, 110, 14, SK) + Pa('M86,108 A14,14 0 0,1 114,108 Z', '#3c7fc1') + R(90, 106, 20, 6, '#2f3437', 3) + St('M86,120 Q50,110 40,130 M114,120 Q150,110 160,130', SK, 9) + St('M40,130 Q60,140 80,126 M160,130 Q140,140 120,126', SK, 0), False)
S_('freestyle', pool_bg(40) + swimmer(100, 120, 1.1, '#3c7fc1') + ''.join(Ci(30 + k * 10, 116 - (k % 2) * 6, 4, '#ffffff') for k in range(3)), False)
S_('backstroke', pool_bg(40) + E(100, 120, 60, 10, '#4a9ad0') + St('M30,120 L130,120', SK, 14) + Ci(140, 116, 12, SK) + Pa('M140,104 A12,12 0 0,1 152,116 L140,116 Z', '#f3c234') + face(140, 116, 12) + arm([(120, 118), (110, 80), (80, 60)], SK, SK, 9) + arm([(124, 122), (150, 130), (172, 126)], SK, SK, 9), False)
S_('butterfly-stroke', pool_bg(40) + E(100, 130, 60, 12, '#4a9ad0') + Ci(100, 110, 14, SK) + Pa('M86,108 A14,14 0 0,1 114,108 Z', '#7a4fa0') + face(100, 112, 14) + St('M90,120 Q60,80 40,100', SK, 10) + St('M110,120 Q140,80 160,100', SK, 10) + ''.join(Ci(30 + k * 70, 104 + k * 0, 5, '#ffffff') for k in range(3)), False)
S_('changing-room', R(0, 0, 200, 200, '#e8eef2') + R(0, 170, 200, 30, '#c4cbd0') + ''.join(locker_(10 + k * 46, 30, 40, 140, ['#5aa1d4', '#7cc05a', '#5aa1d4', '#7cc05a'][k]) for k in range(4)) + R(20, 150, 160, 10, WOOD, 3) + towel(140, 70, 30, 50, '#ef8fa4'), False)
S_('locker', locker_(60, 20, 80, 170, '#5aa1d4') + R(110, 100, 14, 14, '#d9a33a', 3) + St('M114,100 Q117,90 120,100', '#a7adb1', 3) + T(80, 50, '12', 14, '#ffffff', 900))
S_('armbands', G(Ci(0, 0, 40, '#f08a24') + Ci(0, 0, 18, '#fbe8cc') + R(-6, -44, 12, 10, '#ffffff', 3) + hi(-16, -20, 10, 5, .5), 'translate(60,100)') + G(Ci(0, 0, 40, '#f08a24') + Ci(0, 0, 18, '#fbe8cc') + R(-6, -44, 12, 10, '#ffffff', 3) + hi(-16, -20, 10, 5, .5), 'translate(140,100)'))

# ================= 水上运动 =================
S_('sail', water_bg(140) + sailboat(100, 150, 1.0), False)
S_('surf', R(0, 0, 200, 200, SKY) + Pa('M0,120 Q60,60 120,90 Q170,40 200,70 L200,200 L0,200 Z', '#3c9ad4') + Pa('M120,90 Q150,50 200,70 Q170,60 150,80 Z', '#ffffff') + surfboard(100, 140, .9, -10) + W(100, 134, .55, '#3c7fc1', '#2f3437', arms='up'), False)
S_('surfboard', surfboard(100, 100, 1.3, -60, '#f08a24'))
S_('paddle', paddle_(100, 100, 1.2, 40))
S_('kayak', water_bg(120) + kayak_(100, 130, 1.1) + pose((100, 96), (100, 112), (100, 128), arms=[[(108, 114), (126, 110)]], legs=[], shirt='#e2463b', pants='#e2463b', hr=11, tw=22) + paddle_(100, 110, .7, 60), False)
S_('wetsuit', W(100, 194, 1.05, '#2f3437', '#2f3437', arms='down') + R(84, 70, 32, 6, '#3c7fc1') + R(84, 130, 32, 6, '#3c7fc1'))
S_('snorkel', R(0, 0, 200, 200, '#3c9ad4') + R(0, 0, 200, 40, SKY) + G(R(-34, -16, 68, 32, '#9fd0ec', 14, 'opacity=".8"') + R(-34, -16, 68, 32, 'none', 14, 'stroke="#2f3437" stroke-width="5"'), 'translate(90,80)') + St('M130,100 L130,20 Q130,10 140,10', '#f3c234', 8) + Ci(90, 90, 40, SK, 'opacity="0"') + fish_shape(60, 160, 30, '#f08a24') + fish_shape(150, 150, 24, '#f3c234'), False)
S_('scuba-diving', R(0, 0, 200, 200, '#2f7ab0') + R(0, 170, 200, 30, '#d9c28a') + G(lying(0, 0, '#2f3437', '#2f3437', 'smile', .8), 'translate(40,90)') + R(60, 70, 50, 14, '#f3c234', 6) + ''.join(Ci(36 - k * 4, 70 - k * 16, 4 + k, '#9fd0ec', 'opacity=".7"') for k in range(4)) + fish_shape(160, 140, 26, '#f08a24') + leaf(30, 180, 30, 8, -80, '#3c8a3a'), False)
S_('water-skiing', water_bg(110) + G(R(-40, -20, 80, 24, '#e2463b', 8), 'translate(170,100)') + L(150, 100, 70, 120, '#2f3437', 1.5) + W(60, 150, .5, '#f3c234', '#2f3437', arms='front') + R(30, 150, 60, 5, '#3c7fc1', 2) + St('M20,156 q10,-10 20,0 t20,0', '#ffffff', 3), False)
S_('jet-ski', water_bg(110) + G(Pa('M-60,0 L50,0 Q70,-10 60,-24 L10,-30 L-20,-40 L-50,-30 Z', '#f3c234') + R(-10, -48, 6, 20, '#2f3437') + Pa('M-60,0 L50,0 L46,8 L-56,8 Z', '#2f3437'), 'translate(100,150)') + W(90, 130, .45, '#e2463b', '#2f3437', arms='front') + St('M30,160 q-20,-20 -30,0', '#ffffff', 4), False)
S_('windsurfing', water_bg(130) + surfboard(100, 150, .8, 0, '#ffffff') + L(100, 146, 110, 30, '#5d6469', 3) + Pa('M110,30 L170,110 L104,140 Z', '#e2463b') + Pa('M110,30 L140,70 L106,80 Z', '#f3c234') + W(80, 144, .5, '#3c7fc1', '#2f3437', arms='front'), False)
S_('rowing', water_bg(120) + Pa('M10,130 L190,130 L180,142 L20,142 Z', '#e8e0c0') + ''.join(pose((40 + k * 40, 100), (40 + k * 40, 112), (40 + k * 40, 130), arms=[[(46 + k * 40, 114), (60 + k * 40, 122)]], legs=[], shirt='#3c7fc1', pants='#3c7fc1', hr=9, tw=18, aw=6) + L(50 + k * 40, 120, 20 + k * 40, 170, '#8a5a35', 3) for k in range(4)), False)
S_('dragon-boat', water_bg(110) + Pa('M10,130 L170,130 L160,146 L20,146 Z', '#e2463b') + Pa('M170,130 Q190,100 176,84 Q196,80 196,96 Q190,110 180,130 Z', '#f3c234') + Ci(184, 92, 3, '#2f3437') + St('M10,130 Q0,110 10,100', '#f3c234', 5) + ''.join(pose((30 + k * 26, 104), (30 + k * 26, 114), (30 + k * 26, 130), arms=[[(36 + k * 26, 116), (44 + k * 26, 128)]], legs=[], shirt='#f3c234', pants='#f3c234', hr=7, tw=14, aw=5) + L(44 + k * 26, 120, 30 + k * 26, 160, '#8a5a35', 3) for k in range(5)) + G(Ci(0, 0, 10, '#c0283a') + R(-10, -2, 20, 4, '#f3c234'), 'translate(20,100)'), False)
S_('mast', water_bg(160) + R(96, 10, 8, 160, '#8a5a35') + R(60, 40, 80, 6, '#8a5a35') + Pa('M104,46 L160,150 L104,150 Z', '#ffffff') + Pa('M104,10 L130,18 L104,26 Z', '#e2463b') + St('M100,10 L30,150 M100,10 L170,160', '#5d6469', 1) + boat_hull(100, 160, 160, '#3c7fc1'), False)
S_('rudder', water_bg(80) + Pa('M20,60 L180,60 L170,110 L30,110 Z', '#8a5a35') + R(150, 30, 8, 100, '#5d6469') + Pa('M154,100 L190,100 L184,170 L154,160 Z', '#c0603a') + St('M120,40 L154,40', '#5d6469', 4), False)
S_('capsize', water_bg(100) + G(sailboat(0, 0, .8), 'translate(100,130) rotate(110)') + W(50, 150, .4, '#f3c234', '#2f3437', arms='up', mood='o') + R(0, 140, 200, 60, '#3c9ad4', 0, 'opacity=".6"'), False)

# ================= 马术 =================
S_('horse', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + horse_(90, 176, 1.0), False)
S_('pony', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + horse_(90, 176, .7, '#f6efe0', '#c8903a') + fig(160, 196, 'girl', s=1.1), False)
S_('ride-a-horse', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + horse_(90, 186, .9) + rider(80, 120, 1.0, '#e2463b'), False)
S_('stable', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#c8a070') + R(10, 50, 180, 120, '#a8603a') + Pa('M0,54 L100,10 L200,54 Z', '#7a3a20') + ''.join(R(20 + k * 60, 80, 50, 90, '#6a3a20') + R(20 + k * 60, 120, 50, 50, '#8a5a35') + L(20 + k * 60, 120, 70 + k * 60, 170, '#c8a070', 3) for k in range(3)) + G(Pa('M0,0 Q14,-20 30,-10 L36,4 Q30,10 20,6 Z', '#8a5a35') + Ci(18, -8, 2, '#2f3437'), 'translate(30,94)'), False)
S_('gallop', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + horse_(100, 170, .9, '#5a3a24', '#2f3437', 'gallop') + ''.join(Ci(20 + k * 10, 180 - (k % 2) * 6, 5, '#c8a070', 'opacity=".7"') for k in range(4)), False)
S_('trot', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + horse_(100, 180, .9, '#c8903a', '#5a3a24', 'trot'), False)
S_('jockey', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + horse_(90, 184, .9, '#5a3a24', '#2f3437', 'gallop') + rider(84, 110, 1.0, '#f3c234', '#e2463b'), False)
S_('reins', G(Pa('M56,-118 Q72,-130 88,-112 L94,-98 Q90,-92 82,-96 L70,-104 Z', '#8a5a35') + Pa('M34,-72 L60,-118 L76,-112 L56,-62 Z', '#8a5a35') + Ci(72, -114, 2.5, '#2f3437'), 'translate(20,180) scale(1.2)') + St('M118,58 Q100,110 40,130', '#5a3a24', 5) + St('M126,64 Q110,120 50,140', '#5a3a24', 5) + hand(40, 136, .6))
S_('horseshoe', Pa('M50,160 L50,90 Q50,30 100,30 Q150,30 150,90 L150,160 L120,160 L120,90 Q120,60 100,60 Q80,60 80,90 L80,160 Z', '#8a9196') + ''.join(Ci(x, y, 4, '#2f3437') for x, y in [(65, 140), (62, 110), (72, 70), (135, 140), (138, 110), (128, 70)]))
S_('mane', G(Pa('M34,-72 L60,-118 L76,-112 L56,-62 Z', '#c8903a') + Pa('M56,-118 Q72,-130 88,-112 L94,-98 Q90,-92 82,-96 L70,-104 Z', '#c8903a') + Pa('M34,-76 Q30,-104 58,-124 Q44,-90 44,-74 Z', '#5a3a24') + ''.join(St(f'M{40+k*4},{-78-k*10} q-14,4 -20,16', '#5a3a24', 4) for k in range(5)) + Ci(72, -114, 2.5, '#2f3437'), 'translate(10,220) scale(1.5)'))
S_('racecourse', R(0, 0, 200, 200, SKY) + stands(40, 40) + R(0, 80, 200, 120, '#8cc06a') + E(100, 160, 110, 50, '#c8a070') + E(100, 160, 80, 30, '#8cc06a') + ''.join(R(k * 20, 104, 3, 14, '#ffffff') for k in range(10)) + R(0, 104, 200, 3, '#ffffff') + horse_(60, 196, .35, '#5a3a24', '#2f3437', 'gallop') + horse_(120, 200, .35, '#c8903a', '#5a3a24', 'gallop'), False)
S_('show-jumping', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#8cc06a') + R(70, 130, 6, 50, '#ffffff') + R(150, 130, 6, 50, '#ffffff') + ''.join(R(70, 136 + k * 14, 86, 6, ['#e2463b', '#ffffff', '#e2463b'][k]) for k in range(3)) + G(horse_(0, 0, .7, '#5a3a24', '#2f3437', 'gallop'), 'translate(110,130) rotate(-15)') + rider(104, 70, .7, '#2f3437'), False)
S_('bridle', G(Pa('M34,-72 L60,-118 L76,-112 L56,-62 Z', '#c8903a') + Pa('M56,-118 Q72,-130 88,-112 L94,-98 Q90,-92 82,-96 L70,-104 Z', '#c8903a') + Pa('M34,-76 Q30,-104 58,-124 Q44,-90 44,-74 Z', '#5a3a24') + Ci(72, -114, 2.5, '#2f3437') + St('M62,-122 L60,-104 L84,-96', '#2f3437', 3.5) + St('M60,-112 L80,-112 L92,-104', '#2f3437', 3.5) + Ci(86, -100, 3, '#c4cbd0') + St('M86,-100 Q70,-70 40,-60', '#2f3437', 2.5), 'translate(-20,230) scale(1.7)'))
S_('stirrup', St('M100,20 L100,70', '#5a3a24', 10) + Pa('M60,150 Q60,70 100,70 Q140,70 140,150 Z', 'none', 'stroke="#a7adb1" stroke-width="10"') + R(56, 144, 88, 16, '#8a9196', 4))
S_('riding-boots', G(Pa('M-20,-70 L20,-70 L20,40 L50,40 Q60,40 60,56 L-20,56 Z', '#2f3437') + R(-22, -76, 44, 10, '#5a3a24', 3) + hi(-10, -30, 4, 30, .3), 'translate(70,120)') + G(Pa('M-20,-70 L20,-70 L20,40 L50,40 Q60,40 60,56 L-20,56 Z', '#3a4048') + R(-22, -76, 44, 10, '#5a3a24', 3), 'translate(130,126)'))
S_('polo', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + horse_(90, 186, .8, '#c8903a', '#5a3a24', 'gallop') + rider(84, 126, .9, '#3c7fc1', '#ffffff') + L(126, 100, 170, 180, '#8a5a35', 3) + R(160, 176, 20, 6, '#8a5a35', 2) + Ci(190, 186, 6, '#ffffff'), False)

# ================= 钓鱼 =================
S_('fishing', water_bg(130) + R(0, 120, 80, 80, '#8cc06a') + fisher_sit(40, 140) + rod(70, 110, 160, 40, (170, 150)) + bobber_(170, 150, .5), False)
S_('fishing-rod', rod(30, 180, 180, 20) + reel_(56, 160, .5) + ''.join(Ci(30 + k * 30, 180 - k * 32, 3, '#a7adb1') for k in range(1, 5)) + St('M180,20 Q186,90 170,140', '#5d6469', 1) + hook_(170, 160, .5))
S_('fish-hook', hook_(110, 90, 2.0) + worm(60, 140, 0))
S_('bait', worm(50, 100, 1.4) + hook_(140, 100, 1.0) + G(R(-20, -14, 40, 28, '#8a5a35', 6) + E(0, -14, 20, 5, '#5a3a24'), 'translate(60,160)'))
S_('catch-a-fish', water_bg(150) + W(70, 196, .9, '#5ba644', '#3b4a5a', 'straw', arms='up') + rod(60, 50, 140, 20, (160, 90)) + fish_shape(160, 110, 36, '#9fb4c4', rot=80) + ''.join(drop(140 + k * 14, 140, 4) for k in range(3)), False)
S_('fishing-line', R(10, 120, 60, 60, '#a7adb1', 30) + Ci(40, 150, 14, '#5d6469') + St('M70,140 Q130,40 180,30', '#3c7fc1', 2) + ''.join(E(40, 150, 26 - k * 2, 26 - k * 2, 'none', 'stroke="#3c7fc1" stroke-width="1.5"') for k in range(5)))
S_('reel', reel_(100, 120, 1.6))
S_('fishing-net', St('M30,170 L90,80', '#8a5a35', 6) + Ci(120, 60, 46, 'none', 'stroke="#5d6469" stroke-width="5"') + ''.join(L(78 + k * 12, 30, 90 + k * 8, 120, '#a7adb1', 1.5) for k in range(7)) + ''.join(St(f'M80,{40+j*14} Q120,{60+j*14} 160,{40+j*14}', '#a7adb1', 1.5) for j in range(5)) + fish_shape(124, 100, 26, '#f08a24'))
S_('bobber', water_bg(120) + bobber_(100, 120, 2.2) + E(100, 140, 40, 6, 'none', 'stroke="#ffffff" stroke-width="2"'), False)
S_('cooler-box', R(30, 70, 140, 100, '#3c7fc1', 10) + R(26, 60, 148, 24, '#ffffff', 8) + R(80, 46, 40, 20, 'none', 6, 'stroke="#5d6469" stroke-width="5"') + R(40, 96, 120, 6, '#2f5a9a', 3) + ''.join(R(50 + k * 34, 120, 20, 20, '#ffffff', 4, 'opacity=".3"') for k in range(0)))
S_('riverbank', R(0, 0, 200, 200, SKY) + Pa('M0,120 Q60,110 100,140 Q140,170 200,150 L200,200 L0,200 Z', '#3c9ad4') + Pa('M0,120 Q60,110 100,140 Q140,170 200,150 L200,100 L0,90 Z', '#8cc06a') + ''.join(leaf(20 + k * 12, 132 + k * 2, 18, 4, -80 - k * 4, '#5aaa3a') for k in range(5)) + tree(150, 110, .7) + fisher_sit(60, 116, .6), False)
S_('tackle-box', R(30, 90, 140, 80, '#5ba644', 8) + Pa('M30,90 L40,50 L160,50 L170,90 Z', '#4a9a3a') + ''.join(R(44 + k * 38, 60, 32, 22, '#dff1d8', 3) for k in range(3)) + hook_(60, 70, .2) + bobber_(98, 70, .4) + worm(126, 70, .3) + R(84, 110, 32, 10, '#2f3437', 3))
S_('fishing-license', G(R(-80, -50, 160, 100, '#ffffff', 8) + R(-80, -50, 160, 26, '#5ba644', 8) + R(-80, -32, 160, 8, '#5ba644') + R(-68, -12, 44, 50, '#dff1fb', 3) + Ci(-46, 6, 11, SK) + Pa('M-64,38 Q-46,18 -28,38 Z', '#5ba644') + ''.join(R(-10, -6 + k * 12, 70 - (k % 2) * 16, 5, '#a7adb1', 2) for k in range(4)), 'translate(100,100) rotate(-5)') + fish_shape(130, 66, 26, '#ffffff'))
S_('release', water_bg(120) + hand(80, 110, 1.0) + fish_shape(110, 140, 40, '#9fb4c4', rot=30) + arrow(140, 110, 170, 150, '#5ba644', 4) + heart(160, 50, 12), False)
S_('ice-fishing', R(0, 0, 200, 200, '#cfe2f0') + R(0, 120, 200, 80, '#ffffff') + E(120, 160, 24, 8, '#2f6aa0') + fisher_sit(60, 150, .7, '#e2463b', False) + hat_('beret', 60, 101, 9, '#3c7fc1') + rod(84, 128, 116, 110, (120, 160)), False)
S_('fly-fishing', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, '#3c9ad4') + W(60, 194, .9, '#5ba644', '#5a3a24', 'cap', '#5ba644', arms='up') + St('M68,50 Q120,-10 150,40 Q170,80 130,70 Q100,60 140,20', '#e2463b', 1.5) + G(Pa('M0,0 L8,-6 L6,4 Z', '#f3c234'), 'translate(140,20)') + R(0, 160, 200, 40, '#3c9ad4', 0, 'opacity=".7"'), False)

dump()
