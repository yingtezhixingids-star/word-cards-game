from kit5 import *

WOODF = '#d9a868'
def court_bg(col=WOODF, y=120):
    return R(0, 0, 200, 200, '#e8eef2') + R(0, y, 200, 200 - y, col) + ''.join(L(0, y + 10 + k * 18, 200, y + 10 + k * 18, shade(col, -.05), 1) for k in range(5))
def hoop(x, y, s=1):
    return G(R(-40, -60, 80, 54, '#ffffff', 2, 'stroke="#c4cbd0" stroke-width="3"') + R(-14, -34, 28, 22, 'none', 0, 'stroke="#e2463b" stroke-width="3"') + E(0, 0, 22, 5, 'none', 'stroke="#f08a24" stroke-width="4"') + ''.join(L(-20 + k * 8, 2, -14 + k * 6, 30, '#ffffff', 1.5) for k in range(6)) + L(-14, 30, 14, 30, '#ffffff', 1.5), f'translate({x},{y}) scale({s})')
def bb_player(x, ground, s=1, col='#e2463b', num='23', arms='down', legs='stand'):
    return sportsman(x, ground, s, col, col, num, arms, legs)
def diamond_bg():
    return R(0, 0, 200, 200, SKY) + R(0, 80, 200, 120, GRASS2) + Pa('M100,100 L170,150 L100,200 L30,150 Z', '#d9b07a') + Pa('M100,116 L150,150 L100,184 L50,150 Z', GRASS2) + ''.join(R(x - 5, y - 5, 10, 10, '#ffffff', 1, f'transform="rotate(45 {x} {y})"') for x, y in [(100, 100), (170, 150), (30, 150)]) + Pa('M94,192 L106,192 L106,198 L100,200 L94,198 Z', '#ffffff')
def bb_cap(x, y, s=1, col='#2f4a7a'):
    return G(Pa('M-40,10 Q-40,-40 0,-40 Q40,-40 40,10 Z', col) + Pa('M10,6 L80,14 Q70,26 10,20 Z', shade(col, -.2)) + Ci(0, -40, 4, shade(col, -.2)) + L(0, -40, 0, 8, shade(col, -.15), 1.5), f'translate({x},{y}) scale({s})')
def baseballer(x, ground, s=1, col='#2f4a7a', arms='down', legs='stand', num=''):
    return sportsman(x, ground, s, '#ffffff', '#ffffff', '', arms, legs, 'cap', col) + (T(x, ground - 98 * s, num, 14 * s, col, 900) if num else '')
def mitt_(x, y, s=1, rot=0):
    return G(Pa('M-30,30 L-36,-10 Q-40,-40 -20,-44 Q-14,-60 0,-56 Q14,-62 22,-50 Q40,-46 36,-20 Q50,-10 40,10 L30,30 Z', '#a8603a') + St('M-20,-30 L-10,10 M0,-40 L0,10 M16,-36 L10,10', '#7a3a1a', 2) + R(-30, 26, 60, 12, '#7a3a1a', 4), f'translate({x},{y}) rotate({rot}) scale({s})')
def tennis_court(y=110, col='#3c8a5a'):
    return R(0, 0, 200, 200, SKY) + R(0, y, 200, 200 - y, col) + Pa(f'M30,{y+10} L170,{y+10} L196,196 L4,196 Z', '#4aa06a') + St(f'M30,{y+10} L170,{y+10} L196,196 L4,196 Z', '#ffffff', 2) + L(20, 150, 180, 150, '#ffffff', 0)
def tennis_net(y=140):
    return R(0, y - 30, 200, 30, '#2f3437', 0, 'opacity=".2"') + ''.join(L(k * 8, y - 30, k * 8, y, '#2f3437', 1) for k in range(26)) + ''.join(L(0, y - 30 + j * 6, 200, y - 30 + j * 6, '#2f3437', 1) for j in range(6)) + R(0, y - 34, 200, 6, '#ffffff') + R(2, y - 36, 5, 40, '#5d6469') + R(193, y - 36, 5, 40, '#5d6469')
def tennis_player(x, ground, s=1, col='#ffffff', arms='wave', style='short', hair='#3a2a20'):
    hand = hands(x, ground, s, arms)[1]
    return sportsman(x, ground, s, col, col if col != '#ffffff' else '#ffffff', '', arms, 'stand', '', None, 'smile', style, hair) + racket(hand[0], hand[1] + 6 * s, .5 * s, 20, '#3c7fc1')
def green_bg(y=110):
    return R(0, 0, 200, 200, SKY) + Pa(f'M0,{y+10} Q60,{y-20} 120,{y} Q170,{y+14} 200,{y-4} L200,200 L0,200 Z', '#5aa040') + E(110, 160, 80, 28, '#7ac850')
def flag_hole(x, base, s=1):
    return G(E(0, 0, 10, 4, '#2f3437') + R(-2, -90, 4, 90, '#ffffff') + Pa('M2,-90 L34,-80 L2,-70 Z', '#e2463b'), f'translate({x},{base}) scale({s})')
def track_bg(y=100):
    return R(0, 0, 200, 200, SKY) + R(0, y - 30, 200, 30, '#8cc06a') + R(0, y, 200, 200 - y, '#c8503a') + ''.join(L(0, y + 20 + k * 24, 200, y + 20 + k * 24, '#ffffff', 2) for k in range(4))
def athlete(x, ground, s=1, col='#e2463b', num='', arms='down', legs='stand', style='short', hair='#3a2a20'):
    g = sportsman(x, ground, s, col, '#2f3437', '', arms, legs, style=style, hair=hair)
    if num: g += R(x - 10 * s, ground - 112 * s, 20 * s, 16 * s, '#ffffff', 2) + T(x, ground - 99 * s, num, 11 * s, '#2f3437', 900)
    return g
def hurdle(x, base, s=1):
    return G(R(-30, -50, 60, 10, '#ffffff') + R(-30, -50, 12, 10, '#e2463b') + R(6, -50, 12, 10, '#e2463b') + R(-28, -40, 4, 40, '#5d6469') + R(24, -40, 4, 40, '#5d6469') + R(-34, -4, 16, 4, '#5d6469') + R(18, -4, 16, 4, '#5d6469'), f'translate({x},{base}) scale({s})')

# ================= 篮球/排球 =================
S_('basketball', basket_ball(100, 100, 70))
S_('volleyball', volley_ball(100, 100, 70))
S_('hoop', R(96, 120, 8, 80, '#5d6469') + hoop(100, 80, 1.6))
S_('serve', R(0, 0, 200, 200, '#e8eef2') + R(0, 150, 200, 50, '#e8a060') + sportsman(80, 194, 1.0, '#3c7fc1', '#2f3437', '7', 'up') + volley_ball(130, 26, 14), False)
S_('court-basketball', R(0, 0, 200, 200, '#e8eef2') + R(0, 80, 200, 120, WOODF) + St('M0,80 L200,80 M100,80 L100,200', '#ffffff', 3) + Ci(100, 140, 30, 'none', 'stroke="#ffffff" stroke-width="3"') + St('M0,110 L40,110 L40,170 L0,170 M200,110 L160,110 L160,170 L200,170', '#ffffff', 3) + R(4, 40, 4, 60, '#5d6469') + R(192, 40, 4, 60, '#5d6469') + R(6, 40, 20, 14, '#ffffff', 1) + R(174, 40, 20, 14, '#ffffff', 1), False)
S_('dribble', court_bg() + bb_player(90, 194, 1.0, '#e2463b', '23', 'down', 'walk') + basket_ball(124, 170, 14) + St('M116,140 L120,152 M128,140 L126,152', '#a7adb1', 2), False)
S_('free-throw', court_bg() + hoop(160, 60, .7) + bb_player(70, 194, 1.0, '#3c7fc1', '8', 'up') + basket_ball(70, 22, 12) + St('M80,20 Q130,0 158,56', '#a7adb1', 2, 'stroke-dasharray="5 5"') + St('M30,190 L110,190', '#ffffff', 3), False)
S_('slam-dunk', court_bg() + hoop(130, 70, .9) + pose((100, 90), (100, 112), (96, 160), arms=[[(108, 116), (120, 90), (126, 70)]], legs=[[(94, 160), (80, 180), (86, 196)], [(100, 160), (110, 184), (104, 196)]], back_arm=[[(94, 116), (80, 96), (74, 80)]], shirt='#e2463b', pants='#e2463b', hr=14, tw=28) + basket_ball(128, 64, 12) + burst(140, 50, 14, '#f3c234', 8), False)
S_('three-pointer', court_bg(WOODF, 100) + St('M0,200 Q100,100 200,200', '#ffffff', 3) + bb_player(100, 160, .55, '#3c7fc1', '3', 'up') + basket_ball(100, 50, 10) + T(160, 50, '3', 36, '#f3c234', 900), False)
S_('rebound', court_bg() + hoop(100, 50, .8) + basket_ball(110, 76, 12) + sportsman(60, 194, .75, '#e2463b', '#e2463b', '', 'up') + sportsman(140, 194, .75, '#3c7fc1', '#3c7fc1', '', 'up'), False)
S_('backboard', R(96, 130, 8, 70, '#5d6469') + hoop(100, 110, 2.0))
S_('spike', R(0, 0, 200, 200, '#e8eef2') + R(0, 160, 200, 40, '#e8a060') + R(0, 110, 200, 6, '#ffffff') + ''.join(L(k * 10, 116, k * 10, 160, '#2f3437', 1) for k in range(21)) + pose((70, 40), (72, 62), (70, 110), arms=[[(80, 64), (100, 50), (120, 30)]], legs=[[(68, 110), (60, 140)], [(74, 110), (84, 140)]], back_arm=[[(64, 64), (50, 80)]], shirt='#3c7fc1', pants='#2f3437', hr=13, tw=26) + volley_ball(130, 28, 12) + arrow(140, 40, 180, 100, '#e2463b', 4), False)
S_('block-basketball', court_bg() + bb_player(70, 194, .9, '#e2463b', '5', 'up') + bb_player(140, 194, .8, '#3c7fc1', '9', 'up') + basket_ball(104, 34, 12) + x_badge(170, 40, 14) if False else court_bg() + bb_player(70, 194, .9, '#e2463b', '5', 'up') + bb_player(140, 194, .8, '#3c7fc1', '9', 'up') + basket_ball(104, 34, 12) + burst(92, 34, 12, '#f3c234', 8), False)
S_('beach-volleyball', R(0, 0, 200, 200, SKY) + R(0, 110, 200, 30, '#3c9ad4') + R(0, 140, 200, 60, '#f0d890') + R(98, 70, 4, 100, '#5d6469') + R(0, 70, 200, 30, '#2f3437', 0, 'opacity="0"') + R(30, 70, 140, 24, 'none', 0, 'stroke="#2f3437" stroke-width="1"') + ''.join(L(30 + k * 10, 70, 30 + k * 10, 94, '#2f3437', 1) for k in range(15)) + volley_ball(140, 40, 12) + sportsman(50, 196, .6, '#f3c234', '#f08a24', '', 'up') + sportsman(150, 196, .6, '#ef8fa4', '#e2463b', '', 'up', style='long', hair='#5a3a2a') + Ci(170, 20, 12, '#f3c234'), False)
S_('timeout', court_bg() + G(R(-50, -8, 100, 16, '#2f3437', 6) + R(-8, -8, 16, 70, '#2f3437', 6), 'translate(100,60)') + clock(160, 150, 22, (12, 1)), False)
S_('substitute', court_bg() + bb_player(50, 194, .75, '#e2463b', '6', legs='walk') + bb_player(150, 194, .75, '#e2463b', '11', legs='walk') + arrow(70, 50, 130, 50, '#5ba644', 5) + arrow(130, 76, 70, 76, '#e2463b', 5), False)

# ================= 棒球 =================
S_('baseball', base_ball(100, 100, 66))
S_('pitcher', diamond_bg() + pose((96, 62), (98, 84), (100, 134), arms=[[(104, 88), (120, 70), (136, 50)]], legs=[[(98, 134), (80, 160), (70, 190)], [(102, 134), (126, 140), (136, 120)]], back_arm=[[(92, 88), (76, 106), (80, 120)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28) + hat_('cap', 96, 62, 14, '#2f4a7a') + base_ball(140, 46, 6) + mitt_(80, 120, .3), False)
S_('catcher', diamond_bg() + pose((100, 112), (100, 132), (100, 162), arms=[[(108, 136), (124, 140), (130, 130)]], legs=[[(96, 162), (78, 176), (82, 196)], [(104, 162), (122, 176), (118, 196)]], back_arm=[[(92, 136), (80, 150), (86, 160)]], shirt='#2f3437', pants='#ffffff', hr=15, tw=30) + R(86, 104, 28, 20, 'none', 6, 'stroke="#2f3437" stroke-width="3"') + mitt_(134, 126, .4), False)
S_('batter', diamond_bg() + baseballer(90, 196, .95, '#e2463b', 'front') + bat_base(92, 80, .8, 60), False)
S_('home-run', R(0, 0, 200, 200, '#2f3a5a') + stands(100, 60) + R(0, 160, 200, 40, GRASS2) + base_ball(160, 40, 10) + St('M40,170 Q100,0 160,40', '#ffffff', 2, 'stroke-dasharray="6 5"') + ''.join(firework_ if False else '' for _ in range(1)) + baseballer(40, 196, .5, '#e2463b', 'up') + star(110, 30, 10), False)
S_('strike', diamond_bg() + G(Ci(0, 0, 40, '#e2463b') + L(-20, -20, 20, 20, '#ffffff', 8) + L(20, -20, -20, 20, '#ffffff', 8), 'translate(100,50)') + base_ball(140, 130, 8) + bat_base(70, 150, .6, -40), False)
S_('first-base', diamond_bg() + R(150, 140, 22, 22, '#ffffff', 2, 'transform="rotate(45 161 151)"') + run_pose(140, 160, '#ffffff', '#ffffff', .6) + T(161, 120, '1', 26, '#e2463b', 900), False)
S_('baseball-bat', bat_base(100, 160, 1.5, 40))
S_('baseball-cap', bb_cap(76, 124, 1.15, '#2f4a7a'))
S_('mitt', mitt_(100, 100, 1.6) + base_ball(104, 80, 18))
S_('outfield', R(0, 0, 200, 200, SKY) + stands(30, 40) + R(0, 70, 200, 130, GRASS2) + ''.join(R(k * 40, 70, 20, 130, '#7ac050') for k in range(5)) + Pa('M60,200 L100,170 L140,200 Z', '#d9b07a') + baseballer(60, 140, .4, '#2f4a7a') + baseballer(150, 130, .4, '#2f4a7a') + mitt_(76, 82, .2), False)
S_('dugout', R(0, 0, 200, 200, SKY) + R(0, 140, 200, 60, GRASS2) + R(0, 40, 200, 110, '#5d6469') + R(0, 40, 200, 14, '#3c4048') + R(10, 120, 180, 10, WOOD) + ''.join(baseballer(30 + k * 46, 140, .45, '#2f4a7a') for k in range(4)) + R(0, 130, 200, 10, '#3c4048'), False)
S_('diamond', diamond_bg() + R(0, 0, 0, 0, '#000'), False)
S_('inning', scoreboard('7', 60, 20, 80, 60) + ''.join(R(14 + k * 20, 110, 16, 26, '#2f3437', 2) + T(22 + k * 20, 128, str(k + 1), 12, '#f3c234' if k == 6 else '#ffffff', 900) for k in range(9)) + base_ball(100, 166, 18))
S_('bullpen', R(0, 0, 200, 200, SKY) + R(0, 120, 200, 80, GRASS2) + R(0, 110, 200, 10, '#5d6469') + ''.join(R(k * 20, 60, 3, 60, '#8a9196') for k in range(11)) + ''.join(L(0, 60 + j * 12, 200, 60 + j * 12, '#8a9196', 1) for j in range(6)) + baseballer(60, 196, .5, '#2f4a7a', 'wave') + baseballer(150, 196, .5, '#2f4a7a', 'front') + base_ball(110, 140, 6), False)
S_('foul-ball', diamond_bg() + St('M100,190 L0,120 M100,190 L200,120', '#ffffff', 3) + base_ball(26, 40, 10) + St('M100,180 Q40,60 26,40', '#ffffff', 2, 'stroke-dasharray="5 5"') + G(R(-3, 0, 6, 60, '#f3c234'), 'translate(10,60)'), False)

# ================= 网球/羽毛球 =================
S_('tennis', tennis_court() + tennis_net(150) + tennis_player(100, 150, .55, '#ffffff', 'wave') + tennis_ball(150, 50, 8), False)
S_('racket', racket(100, 140, 1.3, 20, '#3c7fc1'))
S_('tennis-ball', tennis_ball(100, 100, 60))
S_('badminton', racket(80, 150, 1.0, -20, '#7a4fa0', .7) + shuttle(140, 90, 1.3, 30))
S_('table-tennis', G(R(-90, -10, 180, 20, '#2f6a9a', 2) + R(-90, -10, 180, 4, '#ffffff') + R(-2, -40, 4, 30, '#ffffff') + R(-90, 10, 6, 50, '#5d6469') + R(84, 10, 6, 50, '#5d6469'), 'translate(100,130)') + pingpong_bat(50, 90, .7, -30, '#e2463b') + pingpong_bat(150, 90, .7, 30, '#2f3437') + Ci(100, 60, 6, '#ffffff', 'stroke="#c4cbd0" stroke-width="1"'))
S_('shuttlecock', shuttle(100, 140, 2.2, 0))
S_('singles', tennis_court() + tennis_net(150) + tennis_player(100, 140, .45) + tennis_player(100, 200, .5, '#3c7fc1') + T(30, 50, '1', 0, '#000'), False)
S_('doubles', tennis_court() + tennis_net(150) + tennis_player(70, 140, .4) + tennis_player(130, 140, .4) + tennis_player(60, 200, .48, '#3c7fc1') + tennis_player(140, 200, .48, '#3c7fc1', style='long', hair='#5a3a2a'), False)
S_('ace', tennis_court() + tennis_net(150) + tennis_ball(160, 170, 8) + ''.join(L(110 + k * 10, 160 + k * 2, 140 + k * 10, 166 + k * 2, '#ffffff', 2) for k in range(2)) + tennis_player(50, 200, .5, '#3c7fc1', 'up') + star(100, 40, 16), False)
S_('love', scoreboard('0 : 0', 30, 40, 140, 70) + tennis_ball(60, 150, 16) + tennis_ball(140, 150, 16) + heart(100, 150, 0))
S_('deuce', scoreboard('40 : 40', 20, 40, 160, 70) + tennis_ball(100, 150, 18))
S_('forehand', tennis_court() + pose((90, 60), (92, 82), (96, 132), arms=[[(100, 86), (124, 96), (150, 92)]], legs=[[(94, 132), (80, 180)], [(98, 132), (118, 180)]], back_arm=[[(86, 86), (70, 104), (66, 120)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28) + racket(150, 92, .55, 80, '#3c7fc1') + tennis_ball(186, 80, 7), False)
S_('backhand', tennis_court() + pose((110, 60), (108, 82), (104, 132), arms=[[(100, 86), (80, 96), (54, 92)]], legs=[[(102, 132), (86, 180)], [(106, 132), (124, 180)]], back_arm=[[(104, 86), (84, 98), (58, 94)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28) + racket(54, 92, .55, -80, '#3c7fc1') + tennis_ball(16, 80, 7), False)
S_('volley', tennis_court() + tennis_net(170) + pose((100, 50), (100, 72), (100, 120), arms=[[(108, 76), (120, 90), (126, 110)]], legs=[[(96, 120), (88, 150)], [(104, 120), (112, 150)]], back_arm=[[(92, 76), (84, 96)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28) + racket(126, 110, .45, 0, '#3c7fc1') + tennis_ball(130, 60, 7), False)
S_('lob', tennis_court() + tennis_net(150) + St('M40,170 Q100,-20 170,130', '#ffffff', 2, 'stroke-dasharray="5 5"') + tennis_ball(100, 30, 8) + tennis_player(40, 200, .45, '#3c7fc1') + tennis_player(160, 150, .35), False)
S_('smash', tennis_court() + pose((100, 60), (100, 82), (100, 130), arms=[[(108, 86), (120, 60), (124, 30)]], legs=[[(96, 130), (86, 180)], [(104, 130), (114, 180)]], back_arm=[[(92, 86), (76, 70)]], shirt='#ffffff', pants='#ffffff', hr=14, tw=28) + racket(124, 40, .5, 20, '#3c7fc1') + tennis_ball(150, 20, 7) + burst(150, 20, 10, '#f3c234', 8) + arrow(150, 30, 180, 100, '#e2463b', 4), False)

# ================= 高尔夫 =================
S_('golf', green_bg() + flag_hole(130, 160) + pose((60, 70), (62, 92), (64, 140), arms=[[(68, 96), (90, 70), (100, 50)]], legs=[[(60, 140), (52, 190)], [(68, 140), (78, 190)]], back_arm=[[(58, 96), (84, 74), (98, 54)]], shirt='#ef8fa4', pants='#ffffff', hr=14, tw=26) + hat_('cap', 60, 70, 14, '#ffffff') + golf_ball(110, 186, 5), False)
S_('golf-ball', golf_ball(100, 90, 56) + R(96, 146, 8, 30, '#ffffff') + Pa('M84,146 L116,146 L106,154 L94,154 Z', '#ffffff'))
S_('club', golf_club(90, 170, 1.4, 20) + golf_club(120, 176, 1.3, -10))
S_('hole', green_bg(80) + E(100, 140, 40, 14, '#2f3437') + R(98, 30, 4, 110, '#ffffff') + Pa('M102,30 L150,44 L102,58 Z', '#e2463b') + golf_ball(70, 150, 7), False)
S_('swing-golf', green_bg() + pose((96, 70), (98, 92), (100, 140), arms=[[(104, 96), (130, 80), (150, 50)]], legs=[[(96, 140), (88, 190)], [(104, 140), (118, 186)]], back_arm=[[(94, 96), (124, 86), (146, 56)]], shirt='#5ba644', pants='#2f3437', hr=14, tw=26) + golf_club(150, 50, .7, 200) + St('M60,170 Q110,200 160,60', '#ffffff', 2, 'stroke-dasharray="4 5"'), False)
S_('tee', green_bg(130) + R(94, 120, 12, 50, '#ffffff', 2) + Pa('M80,120 L120,120 L108,132 L92,132 Z', '#ffffff') + golf_ball(100, 102, 18), False)
S_('caddie', green_bg() + W(80, 196, .9, '#ffffff', '#5d6469', 'cap', '#5ba644') + G(R(-14, -60, 28, 80, '#2f4a7a', 10) + ''.join(golf_club(-6 + k * 6, -50, .4, -10 + k * 8) for k in range(3)), 'translate(130,180) rotate(10)'), False)
S_('green', R(0, 0, 200, 200, SKY) + E(100, 140, 100, 50, '#7ac850') + E(100, 140, 100, 50, 'none', 'stroke="#5aa040" stroke-width="6"') + flag_hole(110, 150, .9) + golf_ball(70, 150, 6), False)
S_('putt', green_bg() + E(160, 170, 12, 4, '#2f3437') + pose((70, 76), (72, 98), (72, 140), arms=[[(78, 102), (80, 140), (84, 170)]], legs=[[(68, 140), (64, 190)], [(76, 140), (84, 190)]], back_arm=[[(68, 102), (76, 140), (82, 170)]], shirt='#3c7fc1', pants='#ffffff', hr=14, tw=26) + golf_club(84, 186, .5, -4) + golf_ball(110, 186, 5) + St('M118,186 L150,172', '#ffffff', 2, 'stroke-dasharray="3 4"'), False)
S_('hole-in-one', green_bg() + flag_hole(100, 150, 1.1) + golf_ball(100, 152, 5) + T(150, 60, '1', 40, '#f3c234', 900) + confetti(2, 16, (10, 10, 180, 70)), False)
S_('bunker', R(0, 0, 200, 200, SKY) + R(0, 100, 200, 100, '#5aa040') + E(100, 150, 80, 34, '#f0d890') + golf_ball(110, 146, 6) + ''.join(Ci(80 + k * 10, 140 - k * 6, 3, '#e0c070') for k in range(4)), False)
S_('fairway', R(0, 0, 200, 200, SKY) + R(0, 70, 200, 130, '#4a8a30') + Pa('M60,200 Q80,120 110,70 L130,70 Q130,140 160,200 Z', '#7ac850') + tree(30, 110, .6) + tree(170, 120, .6) + flag_hole(120, 80, .3) + golf_ball(110, 170, 5), False)
S_('golf-cart', green_bg() + G(R(-60, -50, 120, 40, '#ffffff', 6) + R(-56, -100, 4, 50, '#5d6469') + R(52, -100, 4, 50, '#5d6469') + R(-64, -106, 128, 10, '#5ba644', 4) + R(-40, -50, 40, 24, '#2f4a7a', 3) + wheel(-40, -10, 14) + wheel(40, -10, 14), 'translate(100,180)'), False)
S_('par', R(30, 30, 140, 140, '#ffffff', 6, 'stroke="#5aa040" stroke-width="4"') + ''.join(T(50 + (k % 3) * 50, 70 + (k // 3) * 40, str([4, 3, 5, 4, 4, 3, 5, 4, 3][k]), 22, '#5aa040' if k != 4 else '#e2463b', 900) for k in range(9)) + Ci(100, 110, 18, 'none', 'stroke="#e2463b" stroke-width="3"'))
S_('birdie', green_bg() + flag_hole(130, 160) + G(E(0, 0, 18, 12, '#f3c234') + Ci(16, -8, 9, '#f3c234') + Pa('M24,-8 l8,2 l-8,2 Z', '#f08a24') + Ci(18, -10, 2, '#2f3437') + Pa('M-6,-4 Q-20,-24 4,-14 Z', '#e0a020'), 'translate(70,60)') + golf_ball(130, 162, 5) + T(60, 140, '−1', 24, '#e2463b', 900), False)
S_('handicap', R(40, 30, 120, 140, '#ffffff', 6) + R(40, 30, 120, 30, '#5aa040', 6) + T(100, 120, '12', 50, '#2f3437', 900) + golf_ball(60, 160, 8) + golf_club(150, 176, .5, 20))

# ================= 田径 =================
S_('race', track_bg() + run_pose(60, 170, '#e2463b', '#2f3437', .55) + run_pose(110, 194, '#3c7fc1', '#2f3437', .6) + run_pose(160, 150, '#5ba644', '#2f3437', .5), False)
S_('track', R(0, 0, 200, 200, '#8cc06a') + E(100, 100, 94, 70, '#c8503a') + E(100, 100, 66, 42, '#8cc06a') + ''.join(E(100, 100, 66 + k * 7, 42 + k * 7, 'none', 'stroke="#ffffff" stroke-width="1.5"') for k in range(5)), False)
S_('start', track_bg() + ''.join(pose((x, 150), (x + 10, 152), (x + 34, 140), arms=[[(x + 10, 154), (x + 8, 178)]], legs=[[(x + 34, 140), (x + 26, 160), (x + 30, 178)], [(x + 34, 140), (x + 50, 160), (x + 60, 178)]], shirt=c, pants='#2f3437', hr=8, tw=16, lw=8, aw=6) for x, c in [(20, '#e2463b'), (90, '#3c7fc1'), (150, '#5ba644')]) + G(R(-4, -20, 30, 10, '#5d6469', 3) + R(-4, -10, 8, 20, '#5d6469', 2), 'translate(100,40)') + Ci(130, 30, 0, '#000') + ''.join(Ci(140 + k * 8, 28 - k * 4, 3, '#a7adb1') for k in range(3)), False)
S_('lap', track_bg(80) + E(100, 140, 80, 40, 'none', 'stroke="#ffffff" stroke-width="3" stroke-dasharray="8 6"') + Pa('M176,140 l6,-10 l6,10 Z', '#ffffff') + run_pose(40, 150, '#e2463b', '#2f3437', .4) + T(100, 150, '1', 26, '#ffffff', 900), False)
S_('finish-line', track_bg() + ''.join(R(k * 12, 100, 6, 100, '#ffffff' if k % 2 else '#2f3437') for k in range(0)) + ''.join(R(80 + (j % 2) * 10, 100 + j * 10, 10, 10, '#2f3437') + R(90 - (j % 2) * 10, 100 + j * 10, 10, 10, '#ffffff') for j in range(10)) + R(0, 60, 200, 4, '#ffffff') + run_pose(120, 194, '#e2463b', '#2f3437', .7), False)
S_('record', trophy(70, 150, .8) + R(110, 40, 80, 50, '#2f3437', 6) + T(150, 74, '9.58', 20, '#f3c234', 900) + arrow(150, 150, 150, 100, '#5ba644', 6) + star(40, 40, 12))
S_('champion', R(0, 0, 200, 200, '#f6efe0') + podium3(1) + W(100, 100, .5, '#e2463b', '#2f3437', arms='up') + medal_(100, 46, 0) + confetti(9, 14, (10, 10, 180, 40)), False)
S_('stopwatch', G(Ci(0, 0, 64, '#ffffff', 'stroke="#2f3437" stroke-width="7"') + ''.join(L(54 * math.cos(k * math.pi / 30), 54 * math.sin(k * math.pi / 30), (50 if k % 5 else 44) * math.cos(k * math.pi / 30), (50 if k % 5 else 44) * math.sin(k * math.pi / 30), '#2f3437', 1.5 if k % 5 else 3) for k in range(60)) + L(0, 0, 30, -36, '#e2463b', 3) + Ci(0, 0, 5, '#e2463b') + R(-8, -82, 16, 14, '#2f3437', 3) + R(-14, -90, 28, 10, '#5d6469', 4) + R(46, -64, 12, 10, '#5d6469', 3, 'transform="rotate(45 52 -60)"'), 'translate(100,110)'))
S_('marathon', R(0, 0, 200, 200, SKY) + building(0, 40, 40, 120) + building(160, 60, 40, 100) + R(0, 150, 200, 50, ROAD) + ''.join(run_pose(30 + k * 40, 196 - (k % 2) * 10, ['#e2463b', '#3c7fc1', '#5ba644', '#f3c234', '#7a4fa0'][k], '#2f3437', .45) for k in range(5)) + R(0, 30, 200, 20, '#f3c234', 2) + T(100, 45, '42 km', 14, '#2f3437', 900), False)
S_('relay', track_bg() + run_pose(50, 194, '#e2463b', '#2f3437', .7) + run_pose(140, 194, '#e2463b', '#2f3437', .7) + R(92, 100, 20, 6, '#f3c234', 3, 'transform="rotate(-20 100 103)"'), False)
S_('hurdles', track_bg() + hurdle(60, 190, 1.0) + hurdle(160, 190, 1.0) + pose((100, 60), (102, 82), (104, 126), arms=[[(108, 86), (130, 80)]], legs=[[(104, 126), (140, 124), (150, 132)], [(104, 126), (86, 140), (70, 130)]], back_arm=[[(96, 86), (76, 96)]], shirt='#3c7fc1', pants='#2f3437', hr=14, tw=28), False)
S_('long-jump', R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#c8503a') + R(110, 150, 90, 50, '#f0d890') + R(100, 150, 10, 50, '#ffffff') + pose((80, 60), (84, 80), (90, 120), arms=[[(90, 84), (110, 64), (124, 56)]], legs=[[(90, 120), (120, 116), (140, 120)], [(90, 120), (116, 130), (136, 134)]], back_arm=[[(80, 84), (100, 70)]], shirt='#e2463b', pants='#2f3437', hr=14, tw=26) + St('M20,150 Q60,40 150,130', '#ffffff', 2, 'stroke-dasharray="4 6"'), False)
S_('high-jump', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#c8503a') + R(30, 50, 6, 110, '#5d6469') + R(164, 50, 6, 110, '#5d6469') + R(30, 74, 140, 4, '#f3c234') + R(60, 150, 120, 30, '#3c7fc1', 6) + pose((70, 70), (86, 64), (126, 60), arms=[[(84, 68), (70, 80)]], legs=[[(126, 60), (150, 74), (160, 90)], [(126, 60), (148, 80), (156, 96)]], shirt='#e2463b', pants='#2f3437', hr=13, tw=24), False)
S_('javelin', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + pose((80, 70), (82, 92), (84, 140), arms=[[(90, 96), (110, 80), (122, 62)]], legs=[[(84, 140), (70, 190)], [(86, 140), (110, 180)]], back_arm=[[(76, 96), (56, 104)]], shirt='#5ba644', pants='#2f3437', hr=14, tw=26) + L(70, 90, 190, 30, '#c4cbd0', 3) + Pa('M190,30 L176,34 L180,40 Z', '#5d6469'), False)
S_('shot-put', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, '#8cc06a') + E(100, 178, 60, 12, '#c4bcae') + pose((90, 60), (90, 82), (92, 132), arms=[[(98, 86), (104, 70), (100, 58)]], legs=[[(90, 132), (76, 176)], [(94, 132), (116, 176)]], back_arm=[[(82, 86), (60, 90)]], shirt='#e2463b', pants='#2f3437', hr=14, tw=30) + Ci(104, 54, 12, '#5d6469') + hi(100, 50, 3, 2, .6), False)
S_('pole-vault', R(0, 0, 200, 200, SKY) + R(0, 170, 200, 30, '#c8503a') + R(150, 40, 6, 130, '#5d6469') + R(30, 44, 130, 4, '#f3c234') + St('M40,170 Q60,100 100,40', '#3c7fc1', 4) + pose((110, 30), (104, 46), (92, 76), arms=[[(100, 44), (96, 42)]], legs=[[(92, 76), (110, 70), (130, 40)], [(92, 76), (116, 74), (136, 48)]], shirt='#e2463b', pants='#2f3437', hr=12, tw=22, lw=10, aw=8) + R(120, 150, 70, 20, '#3c7fc1', 4), False)

dump()
