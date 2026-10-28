from kit5 import *

AF = '#2f5a9a'
def af_player(x, ground, s=1, col=AF, num='12', arms='down', legs='stand'):
    hx, hy, hr = x, ground - 153 * s, 15 * s
    return sportsman(x, ground, s, col, '#ffffff', num, arms, legs) + football_helmet(hx + 2 * s, hy + 2 * s, .38 * s, col)
def cheer_girl(x, ground, s=1, col='#e2463b'):
    hx, hy = hands(x, ground, s, 'up')
    return W(x, ground, s, col, col, arms='up', style='long', hair='#5a3a2a') + Ci(hx[0], hx[1], 12 * s, '#f3c234') + Ci(hy[0], hy[1], 12 * s, '#f3c234') + ''.join(L(hx[0], hx[1], hx[0] + 14 * s * math.cos(a), hx[1] + 14 * s * math.sin(a), '#f3e070', 2) + L(hy[0], hy[1], hy[0] + 14 * s * math.cos(a), hy[1] + 14 * s * math.sin(a), '#f3e070', 2) for a in [k * .785 for k in range(8)])
def rugby_player(x, ground, s=1, col='#2f6a3a', num='9', arms='down', legs='stand', mood='smile'):
    g = sportsman(x, ground, s, col, '#ffffff', '', arms, legs, mood=mood)
    sh = ground - 129 * s
    return g + ''.join(R(x - 17 * s, sh + 8 * s + k * 12 * s, 34 * s, 5 * s, '#ffffff') for k in range(3))
def hockey_player(x, ground, s=1, col='#e2463b'):
    hx, hy, hr = x, ground - 153 * s, 15 * s
    return sportsman(x, ground, s, col, '#2f3437', '', 'front', 'stand', 'cap', '#2f3437') + R(hx - hr * 1.1, hy - hr * 1.15, hr * 2.2, hr * .8, '#2f3437', 6) + stick_hockey(x + 10 * s, ground - 4, .9 * s, 20)
def cricketer(x, ground, s=1):
    return sportsman(x, ground, s, '#ffffff', '#ffffff', '', 'front', 'stand', 'cap', '#2f4a7a')
def stumps_(x, base, s=1):
    return G(''.join(R(-14 + k * 12, -60, 5, 60, '#e8c890', 2) for k in range(3)) + R(-16, -64, 15, 4, '#c8a070', 2) + R(0, -64, 15, 4, '#c8a070', 2), f'translate({x},{base}) scale({s})')
def puck_(x, y, r):
    return E(x, y + r * .3, r, r * .45, '#1a1a1a') + R(x - r, y - r * .1, r * 2, r * .4, '#1a1a1a') + E(x, y - r * .1, r, r * .45, '#2f3437')
def rink_bg():
    return R(0, 0, 200, 200, '#dfeef6') + R(0, 120, 200, 80, '#eef7fb') + L(100, 120, 100, 200, '#e2463b', 3) + Ci(100, 160, 24, 'none', 'stroke="#3c7fc1" stroke-width="2"') + R(0, 116, 200, 8, '#ffffff', 2, 'stroke="#c4cbd0" stroke-width="1"')
def cricket_bg():
    return pitch_bg(110, '#7ab04f', lines=False) + R(70, 120, 60, 80, '#d9c28a')

# ================= 美式足球 =================
S_('ball', soccer_ball(60, 120, 30) + basket_ball(130, 80, 30) + tennis_ball(140, 150, 18) + rugby_ball(60, 50, 28))
S_('player', pitch_bg(120) + af_player(100, 194, 1.0, AF, '7') + rugby_ball(130, 120, 14, -20, '#8a4a2a'), False)
S_('coach-amfootball', pitch_bg(120) + W(80, 194, 1.0, '#2f3437', '#5d6469', 'cap', '#2f5a9a', arms='wave') + whistle(110, 100, .4) + G(R(-24, -32, 48, 64, '#ffffff', 3) + R(-24, -32, 48, 10, '#5d6469', 2) + ''.join(Ci(-12 + (k % 3) * 12, -10 + (k // 3) * 16, 3, '#e2463b') + St(f'M{-12+(k%3)*12},{-10+(k//3)*16} l6,8', '#3c7fc1', 2) for k in range(6)), 'translate(150,140)'), False)
S_('win', trophy(100, 140, 1.4) + confetti(5, 18, (10, 10, 180, 60)) + star(40, 120, 12) + star(160, 120, 12))
S_('lose', person_bust(100, 120, 36, '#3c7fc1', m='sad') + brows_sad(100, 120, 36) + drop(130, 110, 6) + scoreboard('1 : 4', 50, 14, 100, 50))
S_('score', scoreboard('3 : 2', 20, 40, 160, 90))
S_('fan', R(0, 0, 200, 200, '#3a4560') + stands(110, 90) + W(100, 196, 1.0, '#e2463b', '#3b4a5a', arms='up', mood='o') + R(70, 20, 10, 40, '#5d6469') + Pa('M80,20 L130,30 L80,44 Z', '#e2463b') + St('M80,96 L120,96', '#ffffff', 0) + R(86, 90, 28, 6, '#ffffff', 3), False)
S_('stadium', R(0, 0, 200, 200, SKY) + Pa('M0,60 Q100,20 200,60 L200,130 L0,130 Z', '#a7adb1') + stands(70, 50) + E(100, 160, 100, 40, GRASS2) + E(100, 160, 60, 20, 'none', 'stroke="#ffffff" stroke-width="2"') + ''.join(R(10 + k * 170, 14, 6, 50, '#5d6469') + R(4 + k * 170, 10, 18, 10, '#f3e070', 2) for k in range(2)), False)
S_('pass', pitch_bg(120) + af_player(40, 194, .8, AF, '7', arms='wave') + af_player(170, 194, .8, '#e2463b', '3', arms='up') + St('M70,60 Q110,10 160,40', '#ffffff', 3, 'stroke-dasharray="6 5"') + rugby_ball(116, 32, 14, 20), False)
S_('tackle', pitch_bg(130) + G(af_player(0, 0, .85, '#e2463b', '3', legs='run'), 'translate(130,196) rotate(25)') + pose((60, 110), (74, 124), (110, 150), arms=[[(76, 128), (110, 120), (130, 110)]], legs=[[(110, 150), (104, 190)], [(112, 150), (140, 186)]], shirt=AF, pants='#ffffff', hr=13, tw=26) + football_helmet(60, 110, .33, AF) + burst(110, 90, 14, '#f3c234', 8), False)
S_('kick', pitch_bg(130) + kick_pose(80, 196, AF, '#ffffff', 1.0) + football_helmet(80, 46, .38, AF) + rugby_ball(150, 140, 16, -50), False)
S_('touchdown', pitch_bg(110, GRASS2) + R(0, 110, 200, 40, AF) + ''.join(L(0, 150 + k * 16, 200, 150 + k * 16, '#ffffff', 2) for k in range(3)) + af_player(100, 160, .75, '#e2463b', '8', arms='up') + rugby_ball(126, 26, 14, -30) + ''.join(R(20 + k * 160, 10, 4, 110, '#f3c234') for k in range(0)) + St('M150,20 L150,100 M150,60 L190,60 M190,60 L190,20', '#f3c234', 5), False)
S_('quarterback', pitch_bg(130) + af_player(90, 194, 1.0, AF, '1', arms='wave') + rugby_ball(124, 40, 14, -20) + G(Pa('M0,0 L14,4 L0,8 Z', '#e2463b'), 'translate(150,30)'), False)
S_('cheerleader', R(0, 0, 200, 200, '#3a4560') + stands(100, 100) + cheer_girl(100, 196, 1.0), False)
S_('super-bowl', trophy(100, 130, 1.3, '#c4cbd0') + rugby_ball(100, 64, 22, -30, '#a7adb1') + confetti(7, 18, (10, 10, 180, 50)) + R(40, 170, 120, 14, '#2f5a9a', 3))
S_('half-time', pitch_bg(120) + scoreboard('14 : 7', 40, 14, 120, 54) + clock(100, 90, 0) + G(Pa('M0,0 L0,-24 A24,24 0 0,1 0,24 Z', '#f3c234') + Ci(0, 0, 24, 'none', 'stroke="#2f3437" stroke-width="4"'), 'translate(100,150)') + W(30, 196, .5, AF, '#ffffff') + W(170, 196, .5, '#e2463b', '#ffffff'), False)

# ================= 橄榄球 =================
S_('match', pitch_bg(110) + stands(50, 60) + rugby_player(60, 194, .7, '#2f6a3a', legs='run') + rugby_player(150, 194, .7, '#e2463b', legs='run') + rugby_ball(104, 100, 12), False)
S_('teammate', pitch_bg(120) + rugby_player(70, 194, .9, '#2f6a3a') + rugby_player(130, 194, .9, '#2f6a3a') + arm([(84, 76), (104, 70), (118, 76)], '#2f6a3a', SK, 10) + heart(100, 30, 10), False)
S_('opponent', pitch_bg(120) + rugby_player(50, 194, .85, '#2f6a3a', mood='flat') + rugby_player(150, 194, .85, '#e2463b', mood='flat') + T(100, 100, 'VS', 30, '#f3c234', 900), False)
S_('whistle', whistle(110, 110, 1.4) + ''.join(St(f'M{40-k*10},{80-k*8} q-10,20 0,40', '#3c7fc1', 3) for k in range(0)) + St('M170,80 q10,20 0,40 M184,70 q14,30 0,60', '#3c7fc1', 3))
S_('jersey', jersey(100, 104, 1.5, '#2f6a3a', '9'))
S_('muddy', pitch_bg(120, '#8a6a3a') + rugby_player(100, 194, 1.0, '#2f6a3a') + ''.join(Ci(x, y, r_, '#6a4a2a', 'opacity=".85"') for x, y, r_ in [(90, 80, 7), (110, 100, 9), (96, 130, 8), (106, 160, 7), (92, 176, 9), (104, 54, 4)]) + ''.join(Ci(30 + k * 40, 180, 10, '#6a4a2a') for k in range(4)), False)
S_('tough', R(0, 0, 200, 200, '#f6efe0') + pose((100, 60), (100, 84), (100, 140), arms=[[(84, 86), (54, 84), (56, 52)], [(116, 86), (146, 84), (144, 52)]], legs=[[(94, 140), (90, 190)], [(106, 140), (110, 190)]], shirt='#2f6a3a', pants='#ffffff', hr=17, tw=40, aw=16, mood='flat') + Ci(56, 52, 10, SK) + Ci(144, 52, 10, SK) + E(60, 76, 12, 8, '#2f6a3a') + E(140, 76, 12, 8, '#2f6a3a'), False)
S_('injury', pitch_bg(120) + lying(30, 160, '#2f6a3a', '#ffffff', 'sad') + G(R(-6, -14, 12, 20, SK, 5), 'translate(126,150)') + bandage(110, 164, 26, 10, 0) + Ci(160, 60, 22, '#ffffff', 'stroke="#e2463b" stroke-width="3"') + R(152, 44, 16, 32, '#e2463b', 2) + R(144, 52, 32, 16, '#e2463b', 2) + ''.join(L(150 + 12 * math.cos(a), 150 + 12 * math.sin(a), 150 + 20 * math.cos(a), 150 + 20 * math.sin(a), '#e2463b', 3) for a in [k * 1.05 - 2 for k in range(4)]), False)
S_('sprint', pitch_bg(120) + run_pose(100, 194, '#2f6a3a', '#ffffff') + ''.join(L(10, 80 + k * 18, 50, 80 + k * 18, '#ffffff', 4) for k in range(3)) + rugby_ball(140, 76, 12, 30), False)
S_('rugby-ball', rugby_ball(100, 100, 66, -30, '#8a4a2a'))
S_('try', pitch_bg(110) + L(0, 150, 200, 150, '#ffffff', 3) + St('M70,20 L70,140 M130,20 L130,140 M70,70 L130,70', '#ffffff', 5) + lying(30, 168, '#2f6a3a', '#ffffff', 'smile', 1, True) + rugby_ball(60, 186, 12, 0) + confetti(4, 10, (10, 10, 180, 40)), False)
S_('scrum', pitch_bg(120) + ''.join(pose((x, 120), (x + d * 14, 126), (x + d * 44, 128), arms=[[(x + d * 14, 130), (x + d * 6, 160)]], legs=[[(x + d * 44, 128), (x + d * 40, 160), (x + d * 54, 190)]], back_leg=[[(x + d * 44, 128), (x + d * 54, 160), (x + d * 64, 190)]], shirt=c, pants='#ffffff', hr=12, tw=24) for x, d, c in [(90, -1, '#2f6a3a'), (110, 1, '#e2463b'), (88, -1.4, '#2f6a3a'), (112, 1.4, '#e2463b')]) + rugby_ball(100, 180, 9, 0), False)
S_('goalpost', pitch_bg(150) + R(56, 20, 8, 160, '#ffffff') + R(136, 20, 8, 160, '#ffffff') + R(56, 90, 88, 8, '#ffffff') + R(52, 130, 16, 40, '#2f6a3a', 3) + R(132, 130, 16, 40, '#2f6a3a', 3) + rugby_ball(100, 50, 12, -10), False)
S_('forward', pitch_bg(120) + rugby_player(100, 194, 1.05, '#2f6a3a', legs='run', mood='flat') + arrow(140, 60, 190, 60, '#e2463b', 6), False)
S_('mouthguard', Pa('M30,70 Q30,170 100,170 Q170,170 170,70 Q170,56 156,56 L146,56 Q140,56 140,70 Q140,134 100,134 Q60,134 60,70 Q60,56 54,56 L44,56 Q30,56 30,70 Z', '#3c7fc1') + ''.join(Ci(100 + 54 * math.cos(a), 92 + 58 * math.sin(a), 7, '#5aa1d4') for a in [math.radians(d) for d in range(10, 171, 20)]) + hi(56, 110, 6, 14, .5, 20))
S_('line-out', pitch_bg(130) + rugby_player(70, 160, .7, '#2f6a3a', arms='up') + G(rugby_player(0, 0, .7, '#e2463b', arms='up'), 'translate(120,170)') + rugby_ball(96, 26, 12, 0) + L(0, 196, 200, 196, '#ffffff', 0) + R(0, 180, 200, 4, '#ffffff'), False)

# ================= 足球 =================
S_('football', soccer_ball(100, 100, 70))
S_('goal-soccer', pitch_bg(150) + goal_net(30, 60, 140, 90) + soccer_ball(130, 120, 16) + St('M40,170 Q90,150 126,128', '#ffffff', 2, 'stroke-dasharray="5 5"'), False)
S_('goalkeeper', pitch_bg(150) + goal_net(10, 40, 180, 110) + sportsman(100, 194, .95, '#f3c234', '#2f3437', '1', 'up') + Ci(64, 46, 10, '#5ba644') + Ci(136, 46, 10, '#5ba644'), False)
S_('referee', pitch_bg(130) + sportsman(90, 194, 1.0, '#2f3437', '#2f3437', '', 'wave') + whistle(100, 50, .3) + card_ref(140, 40, '#f3c234', 10), False)
S_('shoot', pitch_bg(140) + goal_net(120, 70, 80, 70) + kick_pose(50, 196, '#3c7fc1', '#ffffff', .9) + soccer_ball(120, 120, 12) + ''.join(L(80 + k * 6, 140 + k * 4, 96 + k * 6, 132 + k * 4, '#ffffff', 2) for k in range(3)), False)
S_('draw-soccer', scoreboard('1 : 1', 30, 40, 140, 80) + soccer_ball(100, 160, 18) + T(30, 160, '=', 0, '#000'))
S_('foul', pitch_bg(130) + lying(14, 172, '#3c7fc1', '#ffffff', 'o', .8, True) + kick_pose(130, 196, '#e2463b', '#ffffff', .8) + burst(116, 168, 12, '#f3c234', 8) + whistle(40, 60, .3) + G(R(-14, -20, 28, 40, '#f3c234', 3), 'translate(170,40) rotate(10)'), False)
S_('header', pitch_bg(140) + W(100, 194, 1.0, '#3c7fc1', '#ffffff', arms='down') + soccer_ball(100, 20, 16) + ''.join(L(84 + k * 16, 36, 88 + k * 12, 30, '#f3c234', 2) for k in range(3)), False)
S_('yellow-card', hand_(100, 150, 1.0, -90, '#2f3437') + card_ref(100, 80, '#f3c234', 8) if False else G(R(-30, -42, 60, 84, '#f3c234', 6), 'translate(100,80) rotate(8)') + hand(100, 140, .9))
S_('red-card', G(R(-30, -42, 60, 84, '#e2463b', 6), 'translate(100,80) rotate(8)') + hand(100, 140, .9))
S_('penalty', pitch_bg(110) + goal_net(30, 30, 140, 80) + sportsman(100, 112, .45, '#f3c234', '#2f3437', '', 'up') + Ci(100, 160, 5, '#ffffff') + soccer_ball(100, 152, 10) + St('M60,110 L40,200 M140,110 L160,200', '#ffffff', 2), False)
S_('corner-kick', pitch_bg(80, GRASS2, lines=False) + St('M0,120 L200,120 M20,80 L20,200', '#ffffff', 0) + St('M200,180 L20,180 L20,80', '#ffffff', 3) + St('M20,160 A20,20 0 0,0 40,180', '#ffffff', 2) + R(18, 120, 3, 60, '#ffffff', 0, 'opacity="0"') + R(14, 130, 4, 50, '#f3c234') + Pa('M18,130 L40,138 L18,146 Z', '#e2463b') + soccer_ball(30, 170, 8) + kick_pose(40, 196, '#3c7fc1', '#ffffff', .4), False)
S_('world-cup', trophy(100, 140, 1.3) + soccer_ball(100, 64, 26) + Ci(100, 100, 90, 'none', 'stroke="#f3c234" stroke-width="0"'))
S_('striker', pitch_bg(130) + run_pose(100, 194, '#3c7fc1', '#ffffff') + soccer_ball(140, 186, 10) + T(100, 110, '9', 18, '#ffffff', 900), False)
S_('offside', pitch_bg(110) + St('M110,110 L110,200', '#f3c234', 3, 'stroke-dasharray="6 4"') + sportsman(150, 194, .6, '#3c7fc1', '#ffffff') + sportsman(90, 194, .6, '#e2463b', '#ffffff') + sportsman(40, 194, .6, '#3c7fc1', '#ffffff') + G(R(-3, 0, 6, 60, '#5d6469') + Pa('M3,2 L34,2 L34,26 L3,26 Z', '#f3c234') + Pa('M3,2 L34,26 L3,26 Z', '#e2463b'), 'translate(160,30)'), False)
S_('extra-time', pitch_bg(130) + scoreboard('90+', 40, 20, 120, 60) + clock(100, 150, 26, (9, 30)) + Pa('M100,150 L100,124 A26,26 0 0,1 120,134 Z', '#e2463b', 'opacity=".6"'), False)

# ================= 曲棍球 =================
S_('stick', stick_hockey(110, 170, 1.4, 20))
S_('net', goal_net(30, 50, 140, 110) + Pa('M30,160 L50,180 L190,180 L170,160', 'none', 'stroke="#e2463b" stroke-width="5"') + St('M30,160 L30,50 L170,50 L170,160', '#e2463b', 6))
S_('skate', G(Pa('M-60,-10 L-60,-60 Q-60,-70 -50,-70 L-20,-70 L-10,-30 L50,-20 Q60,-16 60,0 L60,10 L-60,10 Z', '#2f3437') + R(-64, 10, 130, 6, '#c4cbd0', 2) + St('M-50,-60 l30,0', '#ffffff', 2) + ''.join(L(-40 + k * 8, -50, -32 + k * 8, -40, '#ffffff', 1.5) for k in range(4)), 'translate(100,130) scale(1.1)'))
S_('rink', rink_bg() + St('M10,130 Q100,100 190,130', '#c4cbd0', 0) + R(0, 40, 200, 76, '#5d6469') + stands(40, 70), False)
S_('ice-hockey', rink_bg() + hockey_player(80, 196, .9, '#e2463b') + puck_(150, 180, 10), False)
S_('puck', puck_(100, 100, 60))
S_('field-hockey', pitch_bg(120, '#3c8ab8') + sportsman(90, 194, .95, '#5ba644', '#2f3437', '', 'front') + stick_hockey(104, 190, .9, 30, '#f3c234') + Ci(150, 186, 7, '#ffffff'), False)
S_('lacrosse', pitch_bg(120) + sportsman(80, 194, .95, '#7a4fa0', '#ffffff', '', 'up', 'hard', '#7a4fa0') + St('M110,90 L130,20', '#c4cbd0', 4) + G(Pa('M0,0 Q-14,-10 -6,-30 Q8,-36 16,-24 Q14,-6 0,0 Z', 'none', 'stroke="#ffffff" stroke-width="3"'), 'translate(132,22)') + Ci(130, 6, 6, '#ffffff'), False)
S_('goalie', rink_bg() + goal_net(40, 80, 120, 70) + hockey_player(100, 196, .95, '#3c7fc1') + R(80, 130, 40, 50, '#ffffff', 6), False)
S_('pads', G(R(-24, -60, 48, 120, '#ffffff', 12) + ''.join(R(-20, -50 + k * 22, 40, 4, '#3c7fc1', 2) for k in range(5)), 'translate(70,100)') + G(R(-24, -60, 48, 120, '#ffffff', 12) + ''.join(R(-20, -50 + k * 22, 40, 4, '#3c7fc1', 2) for k in range(5)), 'translate(130,100)'))
S_('face-off', rink_bg() + Ci(100, 160, 30, 'none', 'stroke="#e2463b" stroke-width="3"') + hockey_player(50, 180, .7, '#e2463b') + G(hockey_player(0, 0, .7, '#3c7fc1'), 'translate(150,180) scale(-1,1)') + puck_(100, 160, 6) + sportsman(100, 120, .4, '#2f3437', '#2f3437', '', 'front'), False)
S_('penalty-box', R(0, 0, 200, 200, '#dfeef6') + R(20, 50, 160, 120, '#ffffff', 4, 'stroke="#a7adb1" stroke-width="3"') + R(26, 56, 148, 60, '#cfe8f6', 2, 'opacity=".5"') + R(30, 130, 140, 30, '#5d6469', 4) + hockey_player(100, 160, .6, '#e2463b') + clock(160, 30, 18, (2, 0)), False)
S_('slap-shot', rink_bg() + pose((80, 60), (86, 82), (90, 130), arms=[[(90, 86), (120, 60), (140, 40)]], legs=[[(88, 130), (70, 190)], [(94, 130), (120, 190)]], back_arm=[[(84, 86), (116, 70), (136, 50)]], shirt='#e2463b', pants='#2f3437', hr=14, tw=28) + G(stick_hockey(0, 0, .9, 0), 'translate(138,44) rotate(150)') + puck_(150, 176, 8) + ''.join(L(160 + k * 8, 168, 180 + k * 8, 168, '#a7adb1', 2) for k in range(2)), False)
S_('period', scoreboard('2', 60, 30, 80, 70) + ''.join(Ci(70 + k * 30, 130, 10, '#f3c234' if k < 2 else '#5d6469') for k in range(3)) + puck_(100, 170, 14))
S_('shin-guard', G(Pa('M-26,-60 Q0,-70 26,-60 L22,50 Q0,60 -22,50 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + ''.join(R(-18, -40 + k * 16, 36, 4, '#3c7fc1', 2) for k in range(6)) + R(-26, -30, 52, 6, '#2f3437', 2) + R(-26, 30, 52, 6, '#2f3437', 2), 'translate(100,100) scale(1.2)'))
S_('body-check', rink_bg() + G(hockey_player(0, 0, .7, '#3c7fc1'), 'translate(120,190) rotate(30)') + G(hockey_player(0, 0, .7, '#e2463b'), 'translate(70,190) rotate(-10)') + burst(100, 90, 14, '#f3c234', 8), False)

# ================= 板球 =================
S_('bat', bat_cricket(80, 170, 1.2, -20) + bat_base(140, 170, 1.0, 20))
S_('out', cricket_bg() + stumps_(100, 180, 1.3) + cricket_ball(90, 130, 9) + G(R(-16, -64, 15, 4, '#c8a070', 2), 'translate(100,180) rotate(-30) translate(-10,-20)') + ''.join(L(100, 90, 100 + 20 * math.cos(a), 90 + 20 * math.sin(a), '#f3c234', 3) for a in [k * .785 for k in range(8)]) + G(R(-8, -30, 16, 30, SK, 6) + R(-3, -50, 6, 22, SK, 3), 'translate(160,60)'), False)
S_('cricket-ball', cricket_ball(100, 100, 60))
S_('bowler', cricket_bg() + pose((90, 60), (92, 82), (96, 130), arms=[[(98, 86), (110, 50), (120, 20)]], legs=[[(94, 130), (80, 160), (70, 190)], [(98, 130), (120, 156), (130, 186)]], back_arm=[[(88, 86), (70, 110), (60, 130)]], shirt='#ffffff', pants='#ffffff', hr=15, tw=30) + cricket_ball(122, 16, 7), False)
S_('batsman', cricket_bg() + cricketer(90, 194, 1.0) + bat_cricket(110, 120, .8, 20) + stumps_(150, 190, .8), False)
S_('wicket', cricket_bg() + stumps_(100, 190, 1.8), False)
S_('pitch', R(0, 0, 200, 200, SKY) + E(100, 150, 110, 60, '#7ab04f') + Pa('M80,100 L120,100 L130,200 L70,200 Z', '#d9c28a') + L(76, 120, 124, 120, '#ffffff', 2) + L(70, 180, 130, 180, '#ffffff', 2) + stumps_(100, 118, .25) + stumps_(100, 184, .35), False)
S_('umpire', cricket_bg() + W(100, 194, 1.0, '#ffffff', '#2f3437', 'straw', '#ffffff', arms='wave') + R(80, 70, 40, 50, '#2f3437', 0, 'opacity="0"'), False)
S_('runs', cricket_bg() + run_pose(70, 194, '#ffffff', '#ffffff') + bat_cricket(120, 80, .6, 70) + stumps_(30, 190, .6) + stumps_(170, 190, .6) + scoreboard('120', 110, 10, 80, 40), False)
S_('over', cricket_bg() + ''.join(cricket_ball(30 + k * 28, 60, 10) for k in range(6)) + T(100, 110, '6', 0, '#000') + St('M20,80 L190,80', '#ffffff', 3), False)
S_('innings', scoreboard('245/6', 20, 30, 160, 70) + cricketer(60, 196, .5) + stumps_(140, 190, .7))
S_('boundary', R(0, 0, 200, 200, SKY) + E(100, 200, 160, 110, '#7ab04f') + E(100, 200, 140, 96, 'none', 'stroke="#ffffff" stroke-width="5"') + ''.join(R(14 + k * 34, 100 - abs(k - 2.5) * 6, 26, 10, ['#e2463b', '#3c7fc1', '#f3c234'][k % 3], 3) for k in range(6)) + cricket_ball(150, 120, 8) + St('M100,180 Q140,120 150,120', '#ffffff', 2, 'stroke-dasharray="4 4"'), False)
S_('stumps', stumps_(100, 180, 2.2))
S_('six', cricket_bg() + stands(50, 50) + T(100, 40, '6', 40, '#e2463b', 900) + cricket_ball(150, 30, 10) + St('M60,170 Q100,40 150,30', '#ffffff', 2, 'stroke-dasharray="5 5"') + cricketer(60, 196, .45), False)
S_('tea-break', cricket_bg() + cup(80, 130, 40, 36, '#ffffff', '#c98a3a') + steam(70, 106, 3, 10) + plate(140, 150, 26) + E(140, 144, 16, 8, '#e8c060') + stumps_(170, 120, .4), False)
S_('not-out', cricket_bg() + cricketer(80, 194, .9) + bat_cricket(100, 120, .7, 20) + Ci(160, 60, 26, '#5ba644') + St('M148,60 l8,9 l14,-16', '#ffffff', 6), False)

dump()
