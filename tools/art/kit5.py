from kit4 import *

def road_top(lines=True):
    g = R(0, 0, 200, 200, '#8cc06a') + R(70, 0, 60, 200, ROAD)
    if lines: g += ''.join(R(98, 10 + k * 30, 4, 16, '#ffffff') for k in range(7))
    return g

def sign_round(x, y, r, ring_col='#e2463b', inner=''):
    return R(x - 3, y + r, 6, 190 - y - r, '#8a9196') + Ci(x, y, r, '#ffffff') + Ci(x, y, r, 'none', f'stroke="{ring_col}" stroke-width="{r*.22}"') + inner

def sign_blue(x, y, r, inner=''):
    return R(x - 3, y + r, 6, 190 - y - r, '#8a9196') + Ci(x, y, r, '#3c7fc1') + inner

def bus_side(cx, base, s=1, col='#3c7fc1', double=False):
    h = 90 if double else 56
    g = R(-80, -h - 10, 160, h, col, 8) + ''.join(R(-70 + k * 28, -h - 2, 22, 22, '#cfe8f6', 3) for k in range(5)) + R(64, -h - 2, 12, 40, '#cfe8f6', 2)
    if double: g += ''.join(R(-70 + k * 28, -h + 32, 22, 20, '#cfe8f6', 3) for k in range(5)) + R(-80, -h + 26, 160, 4, '#ffffff')
    g += R(-80, -24, 160, 6, '#ffffff') + wheel(-50, -6, 13) + wheel(50, -6, 13) + R(70, -26, 10, 6, '#f3d058', 2)
    return G(g, f'translate({cx},{base}) scale({s})')

def taxi_(cx, base, s=1):
    return G(car_side(0, 0, '#f3c234', 1) + R(-14, -70, 30, 12, '#2f3437', 3) + T(1, -61, 'TAXI', 8, '#f3c234', 900) + ''.join(R(-58 + k * 12, -18, 6, 6, '#2f3437') for k in range(10)), f'translate({cx},{base}) scale({s})')

def train_side(cx, base, s=1, col='#e2463b', nose=True):
    g = R(-90, -50, 170, 44, col, 6) + R(-90, -40, 170, 10, '#ffffff') + ''.join(R(-80 + k * 30, -38, 22, 8, '#5aa1d4', 2) for k in range(5))
    if nose: g += Pa('M80,-50 Q110,-40 116,-6 L80,-6 Z', col) + Pa('M84,-44 Q102,-38 106,-26 L84,-26 Z', '#5aa1d4')
    g += wheel(-60, -2, 7) + wheel(-40, -2, 7) + wheel(40, -2, 7) + wheel(60, -2, 7)
    return G(g, f'translate({cx},{base}) scale({s})')

def plane_(cx, cy, s=1, rot=0, col='#ffffff'):
    g = Pa('M-80,0 Q-80,-12 -60,-12 L60,-12 Q90,-10 96,0 Q90,10 60,12 L-60,12 Q-80,12 -80,0 Z', col) + Pa('M-10,-8 L20,-60 L36,-60 L26,-8 Z', '#c4cbd0') + Pa('M-10,8 L20,60 L36,60 L26,8 Z', '#a7adb1') + Pa('M-70,-8 L-80,-34 L-66,-34 L-56,-8 Z', '#e2463b') + ''.join(Ci(-40 + k * 14, -2, 3, '#5aa1d4') for k in range(7)) + Pa('M80,-6 Q90,-4 92,0 L80,0 Z', '#5aa1d4')
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def heli(cx, cy, s=1):
    g = E(0, 0, 40, 26, '#e2463b') + E(14, -4, 18, 14, '#cfe8f6') + R(-90, -6, 60, 10, '#e2463b', 4) + Pa('M-92,-20 L-86,-20 L-80,10 L-86,10 Z', '#e2463b') + R(-4, -34, 8, 10, '#5d6469') + R(-80, -38, 160, 4, '#5d6469', 2) + L(-20, 26, -26, 40, '#5d6469', 3) + L(20, 26, 26, 40, '#5d6469', 3) + R(-40, 38, 80, 4, '#5d6469', 2)
    return G(g, f'translate({cx},{cy}) scale({s})')

def boat_hull_t(cx, base, w, h, col='#ffffff', bottom='#e2463b'):
    return Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w/2-h*.6},{base} L{cx-w/2+h*.4},{base} Z', col) + Pa(f'M{cx-w/2+h*.25},{base-h*.4} L{cx+w/2-h*.35},{base-h*.4} L{cx+w/2-h*.6},{base} L{cx-w/2+h*.4},{base} Z', bottom)

def sea(y=140):
    return R(0, 0, 200, y, SKY) + R(0, y, 200, 200 - y, SEA) + ''.join(St(f'M{10+k*44},{y+20+(k%2)*20} q10,-5 20,0', '#9fd0ec', 2) for k in range(5))

def bike_(cx, base, s=1, col='#e2463b'):
    g = wheel(-40, -26, 26, '#2f3437', '#f2ead8') + wheel(40, -26, 26, '#2f3437', '#f2ead8') + Ci(-40, -26, 20, 'none', 'stroke="#c4cbd0" stroke-width="1.5"') + Ci(40, -26, 20, 'none', 'stroke="#c4cbd0" stroke-width="1.5"')
    g += St('M-40,-26 L-10,-26 L20,-60 L-20,-60 L-10,-26 M20,-60 L40,-26 M-20,-60 L-24,-70 M20,-60 L18,-74', col, 5) + R(-34, -74, 22, 6, '#2f3437', 3) + St('M12,-74 L28,-78', '#2f3437', 4) + Ci(-10, -26, 6, '#5d6469')
    return G(g, f'translate({cx},{base}) scale({s})')

def moto(cx, base, s=1, col='#e2463b'):
    g = wheel(-46, -24, 24) + wheel(50, -24, 24) + Pa('M-40,-30 L-20,-56 L30,-56 L50,-30 Z', col) + R(-20, -66, 40, 12, '#2f3437', 5) + St('M30,-56 L44,-80 L56,-80', '#5d6469', 5) + R(-30, -36, 30, 14, '#a7adb1', 4) + St('M-50,-36 L-80,-30', '#a7adb1', 6)
    return G(g, f'translate({cx},{base}) scale({s})')

def helmet(cx, cy, s=1, col='#e2463b'):
    return G(Pa('M-40,10 Q-44,-40 0,-44 Q44,-40 40,10 L30,20 L-30,20 Z', col) + Pa('M-6,-20 Q30,-24 38,0 L38,10 L-6,10 Z', '#2f3437') + hi(-20, -26, 10, 6, .4, -20), f'translate({cx},{cy}) scale({s})')

def ticket_(x, y, s=1, rot=0, col='#f3c234', txt=''):
    return G(R(-50, -26, 100, 52, col, 4) + Ci(-50, 0, 8, '#f2ead8') + Ci(50, 0, 8, '#f2ead8') + L(20, -24, 20, 24, shade(col, -.2), 2) + T(-14, 6, txt, 16, '#2f3437', 900) + ''.join(L(28, -14 + k * 8, 42, -14 + k * 8, shade(col, -.3), 1.5) for k in range(4)), f'translate({x},{y}) rotate({rot}) scale({s})')

def suitcase(cx, base, w=60, h=80, col='#3c7fc1'):
    return R(cx - w / 2, base - h, w, h, col, 8) + R(cx - 12, base - h - 14, 24, 16, 'none', 4, 'stroke="#2f3437" stroke-width="4"') + ''.join(L(cx - w / 2 + 12 + k * (w - 24) / 2, base - h + 6, cx - w / 2 + 12 + k * (w - 24) / 2, base - 6, shade(col, -.2), 2) for k in range(3)) + wheel(cx - w / 2 + 8, base + 4, 4) + wheel(cx + w / 2 - 8, base + 4, 4)

def passport_(x, y, s=1, rot=0):
    return G(R(-34, -46, 68, 92, '#7a1a24', 4) + Ci(0, -6, 16, 'none', 'stroke="#d9a33a" stroke-width="2.5"') + L(-16, -6, 16, -6, '#d9a33a', 1.5) + St('M0,-22 Q8,-6 0,10 Q-8,-6 0,-22', '#d9a33a', 1.5) + R(-20, 24, 40, 4, '#d9a33a', 1) + R(-14, 32, 28, 3, '#d9a33a', 1), f'translate({x},{y}) rotate({rot}) scale({s})')

def anchor_(x, y, s=1, col='#5d6469'):
    return G(Ci(0, -50, 10, 'none', f'stroke="{col}" stroke-width="6"') + R(-4, -40, 8, 80, col) + R(-24, -26, 48, 8, col, 3) + St('M-40,20 Q-30,50 0,50 Q30,50 40,20', col, 8) + Pa('M-46,26 L-40,10 L-30,24 Z M46,26 L40,10 L30,24 Z', col), f'translate({x},{y}) scale({s})')

def lighthouse(cx, base, s=1):
    g = Pa('M-20,0 L-12,-110 L12,-110 L20,0 Z', '#ffffff') + ''.join(Pa(f'M{-20+k*3.2*0},{-k*30} L{20},{-k*30} L{19},{-k*30-14} L{-19},{-k*30-14} Z', '#e2463b') for k in range(0)) + ''.join(R(-18 + k * 2, -24 - k * 30, 36 - k * 4, 14, '#e2463b') for k in range(3))
    g += R(-16, -130, 32, 20, '#fff3a0') + Pa('M-20,-130 L0,-148 L20,-130 Z', '#2f3437') + R(-18, -112, 36, 4, '#2f3437') + Pa('M16,-124 L90,-150 L90,-100 Z', '#fff3a0', 'opacity=".5"')
    return G(g, f'translate({cx},{base}) scale({s})')

def container_(x, y, w, h, col):
    return R(x, y, w, h, col, 1) + ''.join(L(x + 6 + k * 8, y + 3, x + 6 + k * 8, y + h - 3, shade(col, -.2), 2) for k in range(int((w - 8) / 8)))


GRASS2 = '#6fb04f'
def pitch_bg(y=110, col=GRASS2, sky=SKY, lines=True):
    g = R(0, 0, 200, 200, sky) + R(0, y, 200, 200 - y, col) + ''.join(R(k * 40, y, 20, 200 - y, shade(col, .06)) for k in range(5))
    if lines: g += L(0, y + 30, 200, y + 30, '#ffffff', 2)
    return g
def stands(y=40, h=70, cols=('#e2463b', '#3c7fc1', '#f3c234', '#5ba644', '#ffffff')):
    g = R(0, y, 200, h, '#5d6469')
    for r_ in range(int(h / 12)):
        for k in range(20):
            g += Ci(5 + k * 10 + (r_ % 2) * 5, y + 8 + r_ * 12, 4, cols[(k * 3 + r_) % len(cols)])
    return g
def soccer_ball(x, y, r):
    g = Ci(x, y, r, '#ffffff', 'stroke="#2f3437" stroke-width="2"')
    g += Pa(' '.join(f'{"M" if k == 0 else "L"}{x+r*.38*math.cos(k*1.2566-1.57)},{y+r*.38*math.sin(k*1.2566-1.57)}' for k in range(5)) + ' Z', '#2f3437')
    for k in range(5):
        a = k * 1.2566 + .63 - 1.57
        g += L(x + r * .38 * math.cos(a - .63), y + r * .38 * math.sin(a - .63), x + r * .75 * math.cos(a - .63), y + r * .75 * math.sin(a - .63), '#2f3437', 1.5)
        g += Ci(x + r * .9 * math.cos(a), y + r * .9 * math.sin(a), r * .2, '#2f3437')
    return g
def basket_ball(x, y, r):
    return Ci(x, y, r, '#f08a24') + L(x - r, y, x + r, y, '#7a3a10', 2) + L(x, y - r, x, y + r, '#7a3a10', 2) + St(f'M{x-r*.7},{y-r*.7} Q{x-r*.2},{y} {x-r*.7},{y+r*.7}', '#7a3a10', 2) + St(f'M{x+r*.7},{y-r*.7} Q{x+r*.2},{y} {x+r*.7},{y+r*.7}', '#7a3a10', 2) + hi(x - r * .4, y - r * .4, r * .2, r * .12, .4)
def tennis_ball(x, y, r):
    return Ci(x, y, r, '#d4e040') + St(f'M{x-r*.8},{y-r*.5} Q{x},{y} {x-r*.8},{y+r*.5}', '#ffffff', 2) + St(f'M{x+r*.8},{y-r*.5} Q{x},{y} {x+r*.8},{y+r*.5}', '#ffffff', 2)
def base_ball(x, y, r):
    return Ci(x, y, r, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + St(f'M{x-r*.6},{y-r*.75} Q{x-r*.2},{y} {x-r*.6},{y+r*.75}', '#e2463b', 1.5, 'stroke-dasharray="2 2"') + St(f'M{x+r*.6},{y-r*.75} Q{x+r*.2},{y} {x+r*.6},{y+r*.75}', '#e2463b', 1.5, 'stroke-dasharray="2 2"')
def rugby_ball(x, y, r, rot=-30, col='#8a4a2a'):
    return G(E(0, 0, r, r * .6, col) + L(-r * .4, 0, r * .4, 0, '#ffffff', 2) + ''.join(L(-r * .3 + k * r * .15, -4, -r * .3 + k * r * .15, 4, '#ffffff', 1.5) for k in range(5)), f'translate({x},{y}) rotate({rot})')
def volley_ball(x, y, r):
    return Ci(x, y, r, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + St(f'M{x-r},{y} Q{x},{y-r*.4} {x+r*.6},{y-r*.8}', '#3c7fc1', 3) + St(f'M{x-r*.3},{y+r*.95} Q{x-r*.2},{y} {x+r*.4},{y-r*.9}', '#f3c234', 3) + St(f'M{x+r},{y+r*.1} Q{x+r*.1},{y+r*.3} {x-r*.6},{y+r*.8}', '#3c7fc1', 3)
def golf_ball(x, y, r):
    return Ci(x, y, r, '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + ''.join(Ci(x + r * .5 * math.cos(a), y + r * .5 * math.sin(a), r * .1, '#d9dcde') for a in [k * 1.05 for k in range(6)]) + Ci(x, y, r * .1, '#d9dcde')
def cricket_ball(x, y, r):
    return Ci(x, y, r, '#b8282a') + St(f'M{x-r*.2},{y-r} Q{x+r*.2},{y} {x-r*.2},{y+r}', '#f6efe0', 1.5, 'stroke-dasharray="2 2"') + hi(x - r * .4, y - r * .4, r * .25, r * .15, .4)
def shuttle(x, y, s=1, rot=0):
    return G(Pa('M-12,-40 L12,-40 L6,0 L-6,0 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="1.5"') + ''.join(L(-10 + k * 5, -40, -5 + k * 2.5, 0, '#d9dcde', 1) for k in range(5)) + R(-12, -26, 24, 3, '#e2463b') + Pa('M-7,0 L7,0 Q7,12 0,12 Q-7,12 -7,0 Z', '#f6efe0'), f'translate({x},{y}) rotate({rot}) scale({s})')
def racket(x, y, s=1, rot=0, col='#e2463b', head=1.0):
    return G(E(0, -50, 30 * head, 38 * head, 'none', f'stroke="{col}" stroke-width="6"') + ''.join(L(-26 * head + k * 8 * head, -50 - 34 * head * math.sqrt(max(0, 1 - ((-26 + k * 8) / 30) ** 2)), -26 * head + k * 8 * head, -50 + 34 * head * math.sqrt(max(0, 1 - ((-26 + k * 8) / 30) ** 2)), '#c4cbd0', 1) for k in range(7)) + ''.join(L(-28 * head, -50 + j * 9 * head, 28 * head, -50 + j * 9 * head, '#c4cbd0', 1) for j in range(-3, 4)) + R(-3, -12 - 4 * head, 6, 30, col) + R(-5, 16, 10, 34, '#2f3437', 4), f'translate({x},{y}) rotate({rot}) scale({s})')
def pingpong_bat(x, y, s=1, rot=0, col='#e2463b'):
    return G(Ci(0, -30, 30, col) + R(-6, -2, 12, 34, '#c58b54', 4), f'translate({x},{y}) rotate({rot}) scale({s})')
def stick_hockey(x, y, s=1, rot=0, col='#8a5a35'):
    return G(R(-4, -100, 8, 100, col, 3) + Pa('M-4,-4 L4,-4 L40,4 Q46,10 40,14 L-4,10 Z', col) + R(-4, -100, 8, 26, '#2f3437', 3), f'translate({x},{y}) rotate({rot}) scale({s})')
def bat_base(x, y, s=1, rot=0, col='#c58b54'):
    return G(Pa('M-3,0 L-8,-90 Q0,-100 8,-90 L3,0 Z', col) + R(-4, 0, 8, 24, '#2f3437', 3) + Ci(0, 26, 6, '#2f3437'), f'translate({x},{y}) rotate({rot}) scale({s})')
def bat_cricket(x, y, s=1, rot=0):
    return G(R(-12, -100, 24, 80, '#e8c890', 4) + R(-3, -20, 6, 36, '#2f3437', 3), f'translate({x},{y}) rotate({rot}) scale({s})')
def golf_club(x, y, s=1, rot=0):
    return G(R(-2, -110, 4, 110, '#a7adb1') + R(-4, -110, 8, 26, '#2f3437', 3) + Pa('M-2,-4 L24,0 Q28,8 20,10 L-4,8 Z', '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')
def trophy(x, y, s=1, col='#f3c234'):
    return G(Pa('M-30,-60 L30,-60 Q30,-10 0,-6 Q-30,-10 -30,-60 Z', col) + St('M-30,-50 Q-50,-50 -44,-30 Q-40,-22 -26,-24', col, 5) + St('M30,-50 Q50,-50 44,-30 Q40,-22 26,-24', col, 5) + R(-5, -8, 10, 20, shade(col, -.1)) + R(-22, 10, 44, 12, shade(col, -.2), 3) + hi(-14, -44, 6, 12, .4), f'translate({x},{y}) scale({s})')
def whistle(x, y, s=1):
    return G(Ci(0, 0, 22, '#c4cbd0') + R(0, -22, 40, 18, '#c4cbd0', 3) + Ci(0, 0, 8, '#8a9196') + R(28, -22, 4, 18, '#8a9196') + St('M-20,-10 Q-50,-40 -30,-70', '#e2463b', 3), f'translate({x},{y}) scale({s})')
def goal_net(x, y, w, h):
    return R(x, y, w, h, '#ffffff', 0, 'opacity=".25"') + ''.join(L(x + k * w / 10, y, x + k * w / 10, y + h, '#ffffff', 1) for k in range(11)) + ''.join(L(x, y + k * h / 6, x + w, y + k * h / 6, '#ffffff', 1) for k in range(7)) + St(f'M{x},{y+h} L{x},{y} L{x+w},{y} L{x+w},{y+h}', '#ffffff', 5)
def jersey(x, y, s=1, col='#e2463b', num='10', col2='#ffffff'):
    return G(Pa('M-30,-50 L-14,-56 Q0,-46 14,-56 L30,-50 L50,-26 L36,-14 L30,-24 L30,50 L-30,50 L-30,-24 L-36,-14 L-50,-26 Z', col) + T(0, 20, num, 34, col2, 900), f'translate({x},{y}) scale({s})')
def football_helmet(x, y, s=1, col='#3c7fc1'):
    return G(Pa('M-40,10 Q-44,-46 4,-48 Q44,-46 44,0 L44,20 L10,22 Q-10,30 -40,10 Z', col) + St('M22,0 L54,0 M22,14 L54,14 M50,-4 L50,24', '#c4cbd0', 4) + Ci(-10, 0, 8, shade(col, -.25)) + R(-30, -40, 8, 40, '#ffffff', 3, 'transform="rotate(-20)"'), f'translate({x},{y}) scale({s})')
def sportsman(x, ground, s=1, shirt='#e2463b', pants='#ffffff', num='', arms='down', legs='stand', hat='', hatcol=None, mood='smile', style='short', hair='#3a2a20'):
    g = W(x, ground, s, shirt, pants, hat, hatcol, arms, legs, style, hair, mood=mood)
    if num: g += T(x, ground - 98 * s, num, 16 * s, '#ffffff', 900)
    return g
def kick_pose(x, ground, shirt='#e2463b', pants='#ffffff', s=1, mood='smile'):
    k = s
    return pose((x, ground - 150 * k), (x + 2 * k, ground - 126 * k), (x, ground - 72 * k), arms=[[(x + 10 * k, ground - 122 * k), (x + 34 * k, ground - 110 * k), (x + 44 * k, ground - 130 * k)]], legs=[[(x + 4 * k, ground - 72 * k), (x + 30 * k, ground - 44 * k), (x + 58 * k, ground - 40 * k)]], back_arm=[[(x - 8 * k, ground - 122 * k), (x - 34 * k, ground - 104 * k), (x - 44 * k, ground - 90 * k)]], back_leg=[[(x - 4 * k, ground - 72 * k), (x - 6 * k, ground - 36 * k), (x - 10 * k, ground - 4 * k)]], shirt=shirt, pants=pants, hr=15 * k, tw=30 * k, lw=13 * k, aw=10 * k, mood=mood)
def run_pose(x, ground, shirt='#e2463b', pants='#3b4a5a', s=1, mood='smile', hair='#3a2a20', style='short'):
    k = s
    return pose((x + 6 * k, ground - 152 * k), (x + 2 * k, ground - 128 * k), (x - 6 * k, ground - 74 * k), arms=[[(x + 10 * k, ground - 124 * k), (x + 30 * k, ground - 104 * k), (x + 44 * k, ground - 120 * k)]], legs=[[(x - 2 * k, ground - 74 * k), (x + 26 * k, ground - 50 * k), (x + 18 * k, ground - 12 * k)]], back_arm=[[(x - 6 * k, ground - 124 * k), (x - 28 * k, ground - 104 * k), (x - 40 * k, ground - 86 * k)]], back_leg=[[(x - 10 * k, ground - 74 * k), (x - 26 * k, ground - 40 * k), (x - 50 * k, ground - 30 * k)]], shirt=shirt, pants=pants, hr=15 * k, tw=30 * k, lw=13 * k, aw=10 * k, mood=mood, hair=hair, style=style)
def card_ref(x, y, col, rot=10):
    return G(R(-20, -28, 40, 56, col, 4), f'translate({x},{y}) rotate({rot})')
def scoreboard(txt, x=40, y=30, w=120, h=60):
    return R(x, y, w, h, '#2f3437', 6) + R(x + 6, y + 6, w - 12, h - 12, '#1a2025', 3) + T(x + w / 2, y + h / 2 + 12, txt, 30, '#f3c234', 900, family='Courier New, monospace')
def pool_bg(y=90):
    return R(0, 0, 200, y, '#e8f0f4') + R(0, y, 200, 200 - y, '#5ab4e0') + ''.join(St(f'M0,{y+20+k*28} q25,-6 50,0 t50,0 t50,0 t50,0', '#8fd0f0', 3) for k in range(4))
def lane_rope(y):
    return ''.join(Ci(k * 10 + 5, y, 4, ['#e2463b', '#ffffff', '#3c7fc1'][k % 3]) for k in range(20))
def water_bg(y=120, sky=SKY, col='#3c9ad4'):
    return R(0, 0, 200, 200, sky) + R(0, y, 200, 200 - y, col) + ''.join(St(f'M{-10+(k%2)*20},{y+12+k*18} q20,-6 40,0 t40,0 t40,0 t40,0 t40,0', shade(col, .2), 2.5) for k in range(4))
def snow_bg(y=130):
    return R(0, 0, 200, 200, '#cfe2f0') + Pa(f'M0,{y} L60,{y-60} L120,{y-20} L170,{y-70} L200,{y-40} L200,200 L0,200 Z', '#ffffff') + Pa(f'M60,{y-60} L72,{y-48} L50,{y-46} Z', '#e8f0f6')
def lying(x, y, shirt='#2f6a3a', pants='#ffffff', mood='sad', s=1, arm_up=False):
    k = s
    arms = [[(x + 20 * k, y), (x + 30 * k, y - 22 * k), (x + 20 * k, y - 40 * k)]] if arm_up else [[(x + 20 * k, y), (x + 44 * k, y + 6 * k), (x + 64 * k, y + 4 * k)]]
    return pose((x, y), (x + 22 * k, y + 2 * k), (x + 74 * k, y + 4 * k), arms=arms, legs=[[(x + 74 * k, y + 4 * k), (x + 110 * k, y + 2 * k), (x + 140 * k, y + 4 * k)], [(x + 74 * k, y + 8 * k), (x + 104 * k, y - 14 * k), (x + 130 * k, y + 6 * k)]], shirt=shirt, pants=pants, mood=mood, hr=15 * k, tw=28 * k, lw=13 * k, aw=10 * k)

def big_num(txt, col='#3c7fc1', size=80, y=125, extra=''):
    return T(100, y, txt, size, col, 900) + extra
def dots(n, cols=5, r=7, x0=40, y0=150, gap=20, col='#f08a24'):
    return ''.join(Ci(x0 + (k % cols) * gap, y0 + (k // cols) * gap, r, col) for k in range(n))
def podium3(hl):
    g = R(70, 100, 60, 80, '#f3c234' if hl == 1 else '#c4cbd0', 3) + R(10, 130, 60, 50, '#a7adb1' if hl != 2 else '#c4cbd0', 3) + R(130, 150, 60, 30, '#c8703a' if hl == 3 else '#c4cbd0', 3)
    g += T(100, 150, '1', 34, '#ffffff', 900) + T(40, 166, '2', 28, '#ffffff', 900) + T(160, 174, '3', 22, '#ffffff', 900)
    return g
def weight_(cx, base, w, col='#5d6469', txt=''):
    h = w * .8
    return St(f'M{cx-w*.18},{base-h} Q{cx-w*.18},{base-h-w*.3} {cx},{base-h-w*.3} Q{cx+w*.18},{base-h-w*.3} {cx+w*.18},{base-h}', col, w * .1) + Pa(f'M{cx-w*.38},{base-h} L{cx+w*.38},{base-h} L{cx+w/2},{base} L{cx-w/2},{base} Z', col) + T(cx, base - h * .3, txt, w * .26, '#ffffff', 900)
def road_sign(txt, col='#3c7fc1', sub=''):
    return R(0, 0, 200, 200, SKY) + R(0, 150, 200, 50, '#8cc06a') + Pa('M80,200 L95,120 L105,120 L120,200 Z', ROAD) + R(96, 70, 8, 110, '#8a9196') + R(40, 30, 120, 60, col, 8) + R(46, 36, 108, 48, 'none', 6, 'stroke="#ffffff" stroke-width="3"') + T(100, 72, txt, 30, '#ffffff', 900) + sub
def kitchen_scale(cx, base, s=1, txt='', item=''):
    return G(R(-50, -40, 100, 40, '#e6ecef', 8) + R(-56, -50, 112, 12, '#c4cbd0', 5) + R(-26, -30, 52, 22, '#2f3437', 4) + T(0, -13, txt, 14, '#7cc05a', 900), f'translate({cx},{base}) scale({s})') + item
def id_card(hl):
    g = G(R(-80, -50, 160, 100, '#ffffff', 8) + R(-80, -50, 160, 22, '#3c7fc1', 8) + R(-80, -36, 160, 8, '#3c7fc1') + R(-68, -18, 44, 56, '#dff1fb', 3) + Ci(-46, 2, 12, SK) + Pa('M-58,-2 Q-46,-16 -34,-2 Z', '#3a2a20') + Pa('M-64,38 Q-46,16 -28,38 Z', '#3c7fc1'), 'translate(100,100)')
    g += R(86, 84 + 0, 38 if hl == 0 else 0, 22, '#f3e070', 3) + R(126, 84, 50 if hl == 1 else 0, 22, '#f3e070', 3)
    g += T(90, 100, 'Tom', 16, '#2f3437', 900, 'start') + T(130, 100, 'Smith', 16, '#2f3437', 900, 'start') + R(90, 116, 76, 5, '#a7adb1', 2) + R(90, 126, 56, 5, '#a7adb1', 2)
    return g

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


def pine(x, base, s=1):
    return G(R(-4, -10, 8, 14, '#6a4a2a') + Pa('M0,-80 L24,-40 L12,-40 L30,-10 L-30,-10 L-12,-40 L-24,-40 Z', '#2f6a4a') + Pa('M0,-80 L10,-62 L-10,-62 Z', '#ffffff'), f'translate({x},{base}) scale({s})')

def frame_(x, y, w, h, inner='', col='#c8903a'):
    return R(x - 8, y - 8, w + 16, h + 16, col, 2) + R(x - 3, y - 3, w + 6, h + 6, shade(col, -.2)) + R(x, y, w, h, '#ffffff') + inner
def landscape(x, y, w, h):
    return R(x, y, w, h, SKY) + Pa(f'M{x},{y+h} L{x},{y+h*.6} L{x+w*.3},{y+h*.3} L{x+w*.55},{y+h*.6} L{x+w*.75},{y+h*.4} L{x+w},{y+h*.65} L{x+w},{y+h} Z', '#5aa040') + Ci(x + w * .8, y + h * .2, h * .1, '#f3c234')

def popcorn_(x, base, s=1):
    return G(Pa('M-36,-70 L36,-70 L28,0 L-28,0 Z', '#ffffff') + ''.join(Pa(f'M{-36+k*14.4},-70 L{-36+k*14.4+7.2},-70 L{-28+k*11.2+5.6},0 L{-28+k*11.2},0 Z', '#e2463b') for k in range(5)) + ''.join(Ci(-30 + (k * 17) % 60, -76 - (k * 11) % 18, 9, '#fbf3d0') for k in range(12)), f'translate({x},{base}) scale({s})')
def piano_(x, base, s=1):
    return G(R(-80, -90, 160, 70, '#2f3437', 6) + R(-74, -40, 148, 20, '#ffffff') + ''.join(L(-74 + k * 10.6, -40, -74 + k * 10.6, -20, '#c4cbd0', 1) for k in range(14)) + ''.join(R(-70 + k * 10.6, -40, 6, 12, '#2f3437') for k in range(13) if k % 7 not in (2, 6)) + R(-76, -20, 6, 20, '#2f3437') + R(70, -20, 6, 20, '#2f3437') + R(-30, -84, 60, 26, '#f6efe0', 2), f'translate({x},{base}) scale({s})')
def speaker_(x, y, s=1):
    return G(R(-36, -56, 72, 112, '#2f3437', 8) + Ci(0, -26, 16, '#5d6469') + Ci(0, -26, 6, '#2f3437') + Ci(0, 22, 26, '#5d6469') + Ci(0, 22, 10, '#2f3437'), f'translate({x},{y}) scale({s})')
def headphones_(x, y, s=1, col='#3c7fc1'):
    return G(St('M-50,10 Q-50,-56 0,-56 Q50,-56 50,10', col, 10) + R(-62, -6, 26, 46, col, 10) + R(36, -6, 26, 46, col, 10) + R(-58, 0, 14, 34, '#2f3437', 6) + R(44, 0, 14, 34, '#2f3437', 6), f'translate({x},{y}) scale({s})')

def earth_(x, y, r):
    return Ci(x, y, r, '#3c8ad4') + Pa(f'M{x-r*.6},{y-r*.5} Q{x-r*.2},{y-r*.8} {x+r*.1},{y-r*.5} Q{x},{y-r*.1} {x-r*.3},{y} Q{x-r*.7},{y-r*.1} {x-r*.6},{y-r*.5} Z', '#5aaa4a') + Pa(f'M{x+r*.2},{y} Q{x+r*.7},{y-r*.2} {x+r*.7},{y+r*.3} Q{x+r*.5},{y+r*.8} {x+r*.2},{y+r*.6} Q{x},{y+r*.3} {x+r*.2},{y} Z', '#5aaa4a') + hi(x - r * .4, y - r * .4, r * .2, r * .12, .3)

def barn_(cx, base, w, col='#c0392b'):
    h = w * .7
    return R(cx - w / 2, base - h, w, h, col) + Pa(f'M{cx-w/2-6},{base-h} L{cx},{base-h-w*.42} L{cx+w/2+6},{base-h} Z', '#7a2a20') + R(cx - w * .2, base - h * .6, w * .4, h * .6, '#ffffff') + R(cx - w * .17, base - h * .57, w * .34, h * .57, col) + L(cx - w * .17, base - h * .57, cx + w * .17, base, '#ffffff', 3) + L(cx + w * .17, base - h * .57, cx - w * .17, base, '#ffffff', 3) + R(cx - w * .1, base - h - w * .22, w * .2, w * .14, '#ffffff')


def umbrella(cx, cy, r, col='#e2463b'):
    return Pa(f'M{cx-r},{cy} Q{cx-r},{cy-r} {cx},{cy-r} Q{cx+r},{cy-r} {cx+r},{cy} Q{cx+r*.75},{cy-r*.15} {cx+r*.5},{cy} Q{cx+r*.25},{cy-r*.15} {cx},{cy} Q{cx-r*.25},{cy-r*.15} {cx-r*.5},{cy} Q{cx-r*.75},{cy-r*.15} {cx-r},{cy} Z', col) + L(cx, cy - r, cx, cy + r * .8, '#5d6469', 4) + St(f'M{cx},{cy+r*.8} q0,10 -10,10', '#5d6469', 4)

