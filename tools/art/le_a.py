from kit5 import *

CURT = '#a8202a'
def stage_bg(inner='', spot=True, curtain_open=True):
    g = R(0, 0, 200, 200, '#2a1a2a')
    if spot: g += Pa('M80,0 L120,0 L170,170 L30,170 Z', '#f3e070', 'opacity=".18"')
    g += inner
    g += R(0, 160, 200, 40, '#8a5a35') + R(0, 156, 200, 6, '#a8703e')
    if curtain_open:
        g += Pa('M0,0 L40,0 Q30,80 0,160 Z', CURT) + Pa('M200,0 L160,0 Q170,80 200,160 Z', CURT)
    else:
        g += R(0, 0, 200, 160, CURT) + ''.join(L(k * 20, 0, k * 20, 160, shade(CURT, -.15), 3) for k in range(1, 10))
    g += R(0, 0, 200, 18, shade(CURT, -.1)) + ''.join(Pa(f'M{k*25},18 Q{k*25+12},30 {k*25+25},18 Z', shade(CURT, -.1)) for k in range(8))
    return g
def heads_back(y=180, n=8, cols=('#3a2a20', '#5a3a2a', '#c8c3bc', '#2a1a10')):
    return ''.join(Ci(12 + k * (176 / (n - 1)), y, 13, cols[k % len(cols)]) + R(k * (176 / (n - 1)), y + 10, 24, 20, '#3a3a4a', 8) for k in range(n))
def screen_bg(inner='', col='#1a1a2a'):
    return R(0, 0, 200, 200, '#1a1a2a') + R(14, 20, 172, 110, '#ffffff', 2) + '<clipPath id="scr"><rect x="14" y="20" width="172" height="110"/></clipPath><g clip-path="url(#scr)">' + inner + '</g>' + heads_back(178, 7)
def clapper(x, y, s=1):
    return G(R(-50, -20, 100, 60, '#2f3437', 3) + R(-50, -40, 100, 18, '#ffffff', 2, 'transform="rotate(-12 -50 -22)"') + ''.join(Pa(f'M{-44+k*24},-38 l12,0 l-8,16 l-12,0 Z', '#2f3437', 'transform="rotate(-12 -50 -22)"') for k in range(4)) + ''.join(L(-40, -4 + k * 14, 40, -4 + k * 14, '#ffffff', 1.5) for k in range(3)), f'translate({x},{y}) scale({s})')
def reel(x, y, r):
    return Ci(x, y, r, '#2f3437') + ''.join(Ci(x + r * .55 * math.cos(a), y + r * .55 * math.sin(a), r * .22, '#5d6469') for a in [k * 1.2566 for k in range(5)]) + Ci(x, y, r * .15, '#a7adb1')
def popcorn_(x, base, s=1):
    return G(Pa('M-36,-70 L36,-70 L28,0 L-28,0 Z', '#ffffff') + ''.join(Pa(f'M{-36+k*14.4},-70 L{-36+k*14.4+7.2},-70 L{-28+k*11.2+5.6},0 L{-28+k*11.2},0 Z', '#e2463b') for k in range(5)) + ''.join(Ci(-30 + (k * 17) % 60, -76 - (k * 11) % 18, 9, '#fbf3d0') for k in range(12)), f'translate({x},{base}) scale({s})')
def mask(x, y, s=1, happy=True, col='#f3c234'):
    m = 'M-14,10 Q0,26 14,10' if happy else 'M-14,20 Q0,4 14,20'
    return G(Pa('M-30,-30 Q0,-40 30,-30 Q34,10 0,40 Q-34,10 -30,-30 Z', col) + E(-12, -8, 7, 5, '#2f3437') + E(12, -8, 7, 5, '#2f3437') + St(m, '#2f3437', 4), f'translate({x},{y}) scale({s})')
def piano_(x, base, s=1):
    return G(R(-80, -90, 160, 70, '#2f3437', 6) + R(-74, -40, 148, 20, '#ffffff') + ''.join(L(-74 + k * 10.6, -40, -74 + k * 10.6, -20, '#c4cbd0', 1) for k in range(14)) + ''.join(R(-70 + k * 10.6, -40, 6, 12, '#2f3437') for k in range(13) if k % 7 not in (2, 6)) + R(-76, -20, 6, 20, '#2f3437') + R(70, -20, 6, 20, '#2f3437') + R(-30, -84, 60, 26, '#f6efe0', 2), f'translate({x},{base}) scale({s})')
def guitar_(x, y, s=1, rot=-30, col='#c0603a', electric=False):
    body = (Pa('M-30,-10 Q-44,-30 -26,-44 Q-14,-50 -2,-40 L14,-50 Q36,-50 36,-24 Q36,10 0,30 Q-40,20 -30,-10 Z', col) if electric else E(0, 6, 34, 30, col) + E(0, -30, 26, 24, col))
    return G(body + (Ci(0, -6, 9, '#3a2a20') if not electric else R(-10, -10, 20, 6, '#2f3437')) + R(-4, -120, 8, 100, '#5a3a24') + R(-7, -136, 14, 18, '#3a2a20', 3) + ''.join(L(-2 + k * 1.5, -118, -2 + k * 1.5, 20, '#c4cbd0', .6) for k in range(4)), f'translate({x},{y}) rotate({rot}) scale({s})')
def violin_(x, y, s=1, rot=-30):
    return G(Pa('M0,-40 Q22,-40 22,-24 Q14,-12 20,0 Q28,24 0,34 Q-28,24 -20,0 Q-14,-12 -22,-24 Q-22,-40 0,-40 Z', '#a8502a') + R(-3, -96, 6, 60, '#3a2a20') + Ci(0, -100, 6, '#3a2a20') + St('M-6,-6 q-4,6 0,12 M6,-6 q4,6 0,12', '#3a2a20', 2) + L(0, -90, 0, 30, '#f6efe0', .8), f'translate({x},{y}) rotate({rot}) scale({s})')
def bow_(x1, y1, x2, y2):
    return L(x1, y1, x2, y2, '#8a5a35', 3) + L(x1 + 2, y1 + 4, x2 + 2, y2 + 4, '#f6efe0', 1)
def drum_(x, y, s=1, col='#e2463b'):
    return G(R(-50, -20, 100, 50, col) + E(0, -20, 50, 14, '#f6efe0') + E(0, 30, 50, 14, col) + ''.join(L(-46 + k * 23, -14, -36 + k * 23, 34, '#f3c234', 2) for k in range(5)) + L(-30, -50, 0, -24, '#c8a070', 4) + L(34, -54, 10, -24, '#c8a070', 4), f'translate({x},{y}) scale({s})')
def flute_(x, y, s=1, rot=-20):
    return G(R(-90, -6, 180, 12, '#c4cbd0', 6) + ''.join(Ci(-30 + k * 16, 0, 3, '#5d6469') for k in range(6)) + E(-70, 0, 5, 3, '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')
def trumpet_(x, y, s=1, rot=0):
    return G(R(-70, -5, 110, 10, '#e0b030', 4) + Pa('M40,-5 L80,-30 L80,30 L40,5 Z', '#e0b030') + E(80, 0, 8, 30, '#c89820') + R(-20, -20, 40, 14, 'none', 6, 'stroke="#e0b030" stroke-width="5"') + ''.join(R(-14 + k * 10, -28, 6, 22, '#c89820', 2) for k in range(3)) + R(-80, -6, 12, 12, '#c89820', 3), f'translate({x},{y}) rotate({rot}) scale({s})')
def sax_(x, y, s=1):
    return G(St('M0,-80 L0,30 Q0,60 30,60 Q50,60 50,40 L50,20', '#e0b030', 16) + E(50, 14, 16, 8, '#c89820') + St('M0,-80 Q-6,-96 -20,-96', '#2f3437', 5) + ''.join(Ci(-8, -50 + k * 16, 5, '#c89820') for k in range(5)), f'translate({x},{y}) scale({s})')
def harmonica_(x, y, s=1):
    return G(R(-70, -18, 140, 36, '#c4cbd0', 4) + R(-66, -6, 132, 12, '#5d6469', 2) + ''.join(R(-62 + k * 13, -4, 8, 8, '#2f3437', 1) for k in range(10)) + R(-70, -18, 140, 8, '#e6ecef', 3), f'translate({x},{y}) scale({s})')
def accordion_(x, y, s=1):
    return G(R(-80, -40, 30, 80, '#e2463b', 4) + R(50, -40, 30, 80, '#e2463b', 4) + ''.join(Pa(f'M{-50+k*12.5},-36 L{-44+k*12.5},-40 L{-38+k*12.5},-36 L{-38+k*12.5},36 L{-44+k*12.5},40 L{-50+k*12.5},36 Z', ['#2f3437', '#5d6469'][k % 2]) for k in range(8)) + ''.join(R(-76, -32 + k * 10, 22, 6, '#ffffff', 1) for k in range(7)) + ''.join(Ci(65, -26 + k * 12, 3.5, '#ffffff') for k in range(5)), f'translate({x},{y}) scale({s})')
def erhu_(x, y, s=1):
    return G(R(-3, -130, 6, 140, '#5a3a24') + Pa('M-16,0 L16,0 L16,26 L-16,26 Z', '#5a3a24') + R(-18, 0, 36, 4, '#3a2a20') + R(-8, -120, 16, 6, '#3a2a20', 2) + R(-8, -104, 16, 6, '#3a2a20', 2) + L(-2, -120, -2, 10, '#c4cbd0', 1) + L(2, -120, 2, 10, '#c4cbd0', 1) + St('M-60,-20 Q0,-10 60,-28', '#8a5a35', 3), f'translate({x},{y}) scale({s})')
def staff(y, x0=10, x1=190):
    return ''.join(L(x0, y + k * 8, x1, y + k * 8, '#5d6469', 1.5) for k in range(5))
def speaker_(x, y, s=1):
    return G(R(-36, -56, 72, 112, '#2f3437', 8) + Ci(0, -26, 16, '#5d6469') + Ci(0, -26, 6, '#2f3437') + Ci(0, 22, 26, '#5d6469') + Ci(0, 22, 10, '#2f3437'), f'translate({x},{y}) scale({s})')
def headphones_(x, y, s=1, col='#3c7fc1'):
    return G(St('M-50,10 Q-50,-56 0,-56 Q50,-56 50,10', col, 10) + R(-62, -6, 26, 46, col, 10) + R(36, -6, 26, 46, col, 10) + R(-58, 0, 14, 34, '#2f3437', 6) + R(44, 0, 14, 34, '#2f3437', 6), f'translate({x},{y}) scale({s})')
def frame_(x, y, w, h, inner='', col='#c8903a'):
    return R(x - 8, y - 8, w + 16, h + 16, col, 2) + R(x - 3, y - 3, w + 6, h + 6, shade(col, -.2)) + R(x, y, w, h, '#ffffff') + inner
def landscape(x, y, w, h):
    return R(x, y, w, h, SKY) + Pa(f'M{x},{y+h} L{x},{y+h*.6} L{x+w*.3},{y+h*.3} L{x+w*.55},{y+h*.6} L{x+w*.75},{y+h*.4} L{x+w},{y+h*.65} L{x+w},{y+h} Z', '#5aa040') + Ci(x + w * .8, y + h * .2, h * .1, '#f3c234')
def vase(x, base, s=1, col='#ffffff', pat='#2f5a9a'):
    return G(Pa('M-14,-120 L14,-120 L12,-104 Q50,-80 44,-30 Q36,0 20,0 L-20,0 Q-36,0 -44,-30 Q-50,-80 -12,-104 Z', col) + St('M-40,-50 Q0,-30 40,-50', pat, 4) + St('M-30,-80 Q-10,-60 0,-80 Q10,-100 30,-80', pat, 3) + Ci(0, -40, 8, pat) + leaf(-20, -40, 14, 5, -30, pat) + leaf(20, -40, 14, 5, -150, pat) + R(-16, -124, 32, 6, pat, 2) + R(-22, -6, 44, 6, pat, 2), f'translate({x},{base}) scale({s})')
def statue_(x, base, s=1, col='#d9d4cc'):
    return G(R(-40, -30, 80, 30, '#c4bcae') + R(-34, -36, 68, 8, '#d9d0c0') + pose((0, -150), (0, -130), (0, -86), arms=[[(10, -126), (26, -150), (30, -170)]], legs=[[(-6, -86), (-8, -36)], [(6, -86), (10, -36)]], back_arm=[[(-10, -126), (-20, -100), (-16, -86)]], shirt=col, pants=col, skin=col, hair=shade(col, -.1), hr=14, tw=28, mood='flat', shoes=col), f'translate({x},{base}) scale({s})')

# ================= 舞台 =================
S_('show', stage_bg(W(100, 162, .8, '#f3c234', '#2f3437', arms='up') + ''.join(star(x, y, 6, '#f3e070') for x, y in [(60, 50), (140, 40), (150, 90)])) + heads_back(186, 8), False)
S_('stage', stage_bg('') + R(60, 150, 80, 4, '#f3e070', 0, 'opacity=".5"'), False)
S_('play', stage_bg(W(70, 162, .7, '#7a4fa0', '#2f3437', arms='wave') + crown(70, 36, .25) + W(130, 162, .7, '#e2463b', '#2f3437', arms='front', style='long', hair='#3a2a20') + bubble(100, 40, 40, 20)), False)
S_('audience', R(0, 0, 200, 200, '#2a1a2a') + R(20, 10, 160, 60, '#a8202a') + R(20, 60, 160, 14, '#8a5a35') + ''.join(heads_back(110 + r_ * 36, 7 + r_) for r_ in range(3)), False)
S_('clap', G(Pa('M-10,40 L-24,-30 Q-26,-46 -12,-44 L0,-10 Z', SK) + ''.join(R(-30 + k * 8, -60, 7, 40, SK, 4, 'transform="rotate(-15)"') for k in range(4)), 'translate(80,120) rotate(20)') + G(Pa('M10,40 L24,-30 Q26,-46 12,-44 L0,-10 Z', shade(SK, -.06)) + ''.join(R(-6 + k * 8, -60, 7, 40, shade(SK, -.06), 4, 'transform="rotate(15)"') for k in range(4)), 'translate(120,120) rotate(-20)') + ''.join(L(100 + 50 * math.cos(a), 60 + 50 * math.sin(a), 100 + 64 * math.cos(a), 60 + 64 * math.sin(a), '#f3c234', 4) for a in [math.pi + k * .5 for k in range(7)]))
S_('theater', R(0, 0, 200, 200, '#2a1a2a') + R(0, 140, 200, 60, '#5a1a2a') + ''.join(R(6 + k * 24, 150 + r_ * 22, 20, 18, '#c0283a', 4) for k in range(8) for r_ in range(2)) + stage_bg('')[0:0] + R(20, 20, 160, 100, CURT) + ''.join(L(20 + k * 16, 20, 20 + k * 16, 120, shade(CURT, -.15), 3) for k in range(1, 10)) + R(16, 118, 168, 10, '#d9a33a') + mask(70, 60, .5, True) + mask(130, 60, .5, False, '#9fd0ec'), False)
S_('comedy', mask(100, 100, 1.8, True, '#f3c234') + ''.join(T(x, y, 'ha', 16, '#e2463b', 900) for x, y in [(40, 40), (160, 50), (170, 150)]))
S_('ballet', R(0, 0, 200, 200, '#f6e8ee') + R(0, 176, 200, 24, '#c8a070') + pose((100, 40), (100, 62), (100, 104), arms=[[(108, 66), (130, 40), (110, 20)]], legs=[[(98, 104), (96, 140), (98, 176)]], back_arm=[[(92, 66), (70, 40), (90, 20)]], back_leg=[[(102, 104), (130, 120), (160, 116)]], shirt='#ef8fa4', pants='#f6d0dc', hr=13, tw=24, style='bun', lw=9, aw=7, shoes='#ef8fa4') + E(100, 108, 40, 10, '#f6c8dc'), False)
S_('opera', stage_bg(W(100, 162, .9, '#7a2a6a', '#7a2a6a', arms='wave', style='long', hair='#3a2a20', mood='o') + Pa('M76,96 L124,96 L140,162 L60,162 Z', '#7a2a6a') + note(150, 50, 1.0, '#f3e070') + note(50, 60, .8, '#f3e070')), False)
S_('peking-opera', R(0, 0, 200, 200, '#f6e8d0') + G(Pa('M-60,-40 Q-60,60 0,80 Q60,60 60,-40 Q60,-70 0,-70 Q-60,-70 -60,-40 Z', '#ffffff') + Pa('M-60,-40 Q-60,30 -30,60 L-10,-10 Q-30,-40 -60,-40 Z', '#e2463b') + Pa('M60,-40 Q60,30 30,60 L10,-10 Q30,-40 60,-40 Z', '#e2463b') + Pa('M-40,-20 Q-24,-34 -8,-20 Q-24,-6 -40,-20 Z', '#2f3437') + Pa('M40,-20 Q24,-34 8,-20 Q24,-6 40,-20 Z', '#2f3437') + Pa('M-50,-40 Q-30,-56 -6,-40', 'none', 'stroke="#2f3437" stroke-width="6"') + Pa('M50,-40 Q30,-56 6,-40', 'none', 'stroke="#2f3437" stroke-width="6"') + R(-4, -60, 8, 50, '#2f3437', 3) + Pa('M-16,36 Q0,46 16,36 Q0,56 -16,36 Z', '#a8202a') + Pa('M-30,40 Q0,90 30,40 L20,80 L-20,80 Z', '#2f3437'), 'translate(100,110)') + Pa('M30,40 Q100,-10 170,40 L160,50 Q100,10 40,50 Z', '#f3c234') + ''.join(Ci(50 + k * 25, 34 - abs(k - 2) * 4, 7, ['#e2463b', '#5ba644', '#3c7fc1'][k % 3]) for k in range(5)), False)
S_('musical', stage_bg(W(60, 162, .65, '#e2463b', '#2f3437', arms='up') + W(100, 162, .7, '#f3c234', '#2f3437', arms='wave', style='long', hair='#5a3a2a') + W(140, 162, .65, '#3c7fc1', '#2f3437', arms='up') + note(40, 40, .9, '#f3e070') + note(160, 50, .8, '#f3e070')), False)
S_('costume', R(0, 0, 200, 200, '#f2ead8') + L(30, 30, 170, 30, '#8a9196', 4) + St('M100,30 L100,44 Q80,50 70,60 L130,60 Q120,50 100,44', '#8a9196', 3) + Pa('M70,60 L130,60 L150,180 L50,180 Z', '#7a4fa0') + Pa('M70,60 L130,60 L120,100 L80,100 Z', '#f3c234') + ''.join(Ci(70 + k * 15, 170, 5, '#f3c234') for k in range(5)) + Pa('M50,60 L70,60 L60,130 L40,120 Z', '#7a4fa0') + Pa('M150,60 L130,60 L140,130 L160,120 Z', '#7a4fa0') + crown(160, 170, .3), False)
S_('performance', stage_bg(pose((100, 90), (100, 110), (104, 160), arms=[[(108, 114), (130, 100), (150, 90)]], legs=[[(100, 160), (90, 162)], [(106, 160), (116, 162)]], back_arm=[[(92, 114), (70, 100), (50, 90)]], shirt='#5ba644', pants='#2f3437', hr=14, tw=28) + ''.join(G(Pa('M0,0 Q14,-10 20,6 Q10,4 0,0 Z', '#e2463b'), f'translate({60+k*30},{150})') for k in range(3))) + heads_back(188, 8), False)
S_('front-row', R(0, 0, 200, 200, '#2a1a2a') + R(0, 0, 200, 40, CURT) + ''.join(R(4 + k * 28, 60 + r_ * 44, 24, 30, '#5a1a2a' if r_ else '#e2463b', 6) + R(4 + k * 28, 86 + r_ * 44, 24, 8, shade('#5a1a2a' if r_ else '#e2463b', -.2), 3) for k in range(7) for r_ in range(3)) + R(0, 54, 200, 44, 'none', 6, 'stroke="#f3c234" stroke-width="4"'), False)
S_('interval', stage_bg('', False, False) + clock(100, 80, 26, (8, 15)) + ''.join(G(cup(0, 0, 14, 18, '#ffffff', '#c98a3a'), f'translate({40+k*60},{176})') for k in range(3)) + heads_back(196, 6), False)
S_('rehearsal', stage_bg(W(70, 162, .7, '#5aa1d4', '#3b4a5a', arms='front') + G(R(-12, -16, 24, 32, '#ffffff', 2) + ''.join(L(-6, -8 + k * 6, 6, -8 + k * 6, '#a7adb1', 1.5) for k in range(4)), 'translate(72,90)') + G(R(-20, -40, 40, 6, '#2f3437') + R(-20, -10, 40, 6, '#2f3437') + L(-16, -4, -24, 30, '#c8a070', 3) + L(16, -4, 24, 30, '#c8a070', 3) + L(-16, -34, 16, -10, '#c8a070', 3), 'translate(150,170)'), True), False)

# ================= 电影 =================
S_('movie', reel(70, 70, 40) + reel(140, 80, 30) + clapper(100, 150, .9))
S_('popcorn', popcorn_(100, 180, 1.4))
S_('actress', R(0, 0, 200, 200, '#2a1a2a') + Pa('M60,0 L140,0 L170,200 L30,200 Z', '#f3e070', 'opacity=".15"') + person_bust(100, 100, 40, '#c0283a', '#2a1a10', 'long', blush='#ef7a7a') + ''.join(Ci(80 + k * 10, 150 + abs(k - 2) * 2, 4, '#ffffff') for k in range(5)) + star(40, 40, 10, '#f3e070') + star(160, 50, 8, '#f3e070'), False)
S_('movie-star', R(0, 0, 200, 200, '#c8b8a8') + G(Pa('M0,-60 L16,-18 L60,-18 L24,8 L38,52 L0,26 L-38,52 L-24,8 L-60,-18 L-16,-18 Z', '#ef8fa4') + Pa('M0,-44 L10,-14 L42,-14 L16,4 L26,36 L0,18 L-26,36 L-16,4 L-42,-14 L-10,-14 Z', '#d9a33a'), 'translate(100,100)') + E(100, 100, 30, 10, '#2f3437', 'opacity="0"') + G(R(-30, -8, 26, 16, '#2f3437', 6) + R(4, -8, 26, 16, '#2f3437', 6) + R(-6, -4, 12, 4, '#2f3437'), 'translate(100,100)'), False)
S_('director', R(0, 0, 200, 200, '#e6dcc8') + G(R(-30, -60, 60, 30, '#2f3437') + R(-30, -20, 60, 8, '#2f3437') + L(-26, -12, -36, 40, '#c8a070', 4) + L(26, -12, 36, 40, '#c8a070', 4) + L(-26, -12, 26, 30, '#c8a070', 3) + L(26, -12, -26, 30, '#c8a070', 3), 'translate(70,150)') + G(Pa('M-30,-10 L20,-30 L20,30 L-30,10 Z', '#f3c234') + R(-40, -10, 12, 20, '#2f3437', 3), 'translate(150,60) rotate(-20)') + clapper(150, 150, .5) + hat_('beret', 70, 60, 0), False)
S_('cartoon', screen_bg(G(Ci(0, 0, 40, '#f3c234') + Ci(-30, -34, 14, '#f3c234') + Ci(30, -34, 14, '#f3c234') + Ci(-14, -6, 8, '#ffffff') + Ci(14, -6, 8, '#ffffff') + Ci(-12, -6, 4, '#2f3437') + Ci(16, -6, 4, '#2f3437') + St('M-14,14 Q0,26 14,14', '#2f3437', 3) + Ci(-24, 10, 5, '#ef8fa4') + Ci(24, 10, 5, '#ef8fa4'), 'translate(100,76)')), False)
S_('action-movie', screen_bg(R(14, 20, 172, 110, '#f3a234') + burst(110, 70, 40, '#e2463b', 12) + burst(110, 70, 22, '#f3e070', 10) + G(car_side(0, 0, '#2f3437', .5), 'translate(60,120) rotate(-15)')), False)
S_('horror-movie', screen_bg(R(14, 20, 172, 110, '#2a2a4a') + Pa('M80,120 L80,60 Q80,30 100,30 Q120,30 120,60 L120,120 L113,112 L106,120 L100,112 L93,120 L86,112 Z', '#ffffff') + E(92, 60, 4, 6, '#2f3437') + E(108, 60, 4, 6, '#2f3437') + E(100, 76, 5, 7, '#2f3437') + moon(160, 40, 10)), False)
S_('love-story', screen_bg(R(14, 20, 172, 110, '#f6d0dc') + person_bust(76, 76, 18, '#3c7fc1') + person_bust(124, 76, 18, '#ef8fa4', '#5a3a2a', 'long') + heart(100, 40, 12)), False)
S_('documentary', screen_bg(landscape(14, 20, 172, 110) + G(E(0, 0, 18, 10, '#8a6a4a') + Ci(16, -8, 8, '#8a6a4a') + L(-10, 8, -10, 20, '#6a4a2a', 3) + L(10, 8, 10, 20, '#6a4a2a', 3) + Pa('M18,-16 L14,-26 M20,-16 L26,-26', 'none', 'stroke="#6a4a2a" stroke-width="2"'), 'translate(80,100)')) + camera_(170, 170, .3), False)
S_('subtitles', screen_bg(landscape(14, 20, 172, 110) + R(30, 104, 140, 20, '#2f3437', 3, 'opacity=".7"') + T(100, 119, '你好 Hello', 13, '#ffffff', 800)), False)
S_('3d-glasses', G(R(-80, -24, 70, 48, '#ffffff', 8) + R(10, -24, 70, 48, '#ffffff', 8) + R(-74, -18, 58, 36, '#e2463b', 4, 'opacity=".85"') + R(16, -18, 58, 36, '#3c9ad4', 4, 'opacity=".85"') + R(-12, -6, 24, 8, '#ffffff') + St('M-80,-10 L-96,-20 M80,-10 L96,-20', '#ffffff', 6), 'translate(100,100)') + R(0, 0, 0, 0, '#000'))
S_('trailer', screen_bg(landscape(14, 20, 172, 110) + Ci(100, 75, 24, '#2f3437', 'opacity=".7"') + Pa('M92,62 L114,75 L92,88 Z', '#ffffff') + R(30, 118, 140, 4, '#ffffff', 2, 'opacity=".6"') + R(30, 118, 40, 4, '#e2463b', 2)), False)
S_('scene', ''.join(R(10 + k * 64, 50, 56, 90, '#2f3437') + ''.join(R(12 + k * 64 + j * 12, 54, 6, 6, '#ffffff', 1) for j in range(5)) + ''.join(R(12 + k * 64 + j * 12, 130, 6, 6, '#ffffff', 1) for j in range(5)) + R(14 + k * 64, 64, 48, 62, ['#9fd0ec', '#f3a234', '#9fd0ec'][k]) for k in range(3)) + R(72, 62, 56, 66, 'none', 2, 'stroke="#e2463b" stroke-width="4"') + W(100, 124, .32, '#e2463b', '#2f3437', arms='wave') + clapper(100, 176, .35))
S_('ending', screen_bg(R(14, 20, 172, 110, '#2f3437') + T(100, 90, '剧终', 30, '#ffffff', 900) + R(60, 104, 80, 3, '#a7adb1')), False)
S_('sequel', R(0, 0, 200, 200, '#e6dcc8') + ''.join(G(R(-36, -56, 72, 112, c, 4) + landscape(-30, -50, 60, 60) + T(0, 40, n, 36, '#ffffff', 900), f'translate({60+k*80},100) rotate({-5+k*10})') for k, (c, n) in enumerate([('#3c7fc1', '1'), ('#e2463b', '2')])) + arrow(90, 170, 120, 170, '#5d6469', 4), False)

# ================= 音乐 1 =================
S_('music', staff(70) + note(60, 110, 1.6, '#3c7fc1') + note(110, 96, 1.6, '#e2463b') + note(160, 104, 1.6, '#5ba644') + T(20, 110, '𝄞', 0, '#000'))
S_('song', person_bust(80, 110, 36, '#ef8fa4', '#5a3a2a', 'long', m='o') + note(140, 60, 1.2, '#3c7fc1') + note(170, 100, 1.0, '#e2463b') + note(130, 120, .8, '#5ba644'))
S_('listen', person_bust(80, 110, 36, '#5ba644') + hand(50, 110, .5) + ''.join(St(f'M{150-k*14},{80+k*4} q-10,20 0,40', '#3c7fc1', 3) for k in range(3)) + note(170, 60, 1.0) + speaker_(180, 150, 0))
S_('piano', piano_(100, 170, 1.0) + R(26, 170, 8, 20, '#2f3437') + R(166, 170, 8, 20, '#2f3437'))
S_('guitar', guitar_(100, 130, 1.0, -30))
S_('violin', violin_(90, 130, 1.05, -30) + bow_(60, 176, 170, 60))
S_('drum', drum_(100, 120, 1.3))
S_('flute', flute_(100, 100, 1.0, -20) + note(150, 50, 1.0))
S_('band', stage_bg(guitar_(50, 140, .45, -30) + W(50, 162, .5, '#3c7fc1', '#2f3437', arms='front') + guitar_(50, 132, .45, -30) + W(100, 162, .55, '#e2463b', '#2f3437', arms='front') + mic_(108, 104, .35, 0) + drum_(150, 144, .5) + W(150, 132, .4, '#5ba644', '#2f3437', arms='up')), False)
S_('concert', R(0, 0, 200, 200, '#1a1a3a') + ''.join(Pa(f'M{40+k*40},0 L{20+k*40},120 L{60+k*40},120 Z', ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644'][k], 'opacity=".3"') for k in range(4)) + R(0, 110, 200, 20, '#3a3a5a') + W(100, 120, .4, '#ef8fa4', '#2f3437', arms='up') + ''.join(G(Ci(0, 0, 9, '#2a2a3a') + arm([(0, 10), (6 * (1 if k % 2 else -1), -14)], '#2a2a3a', '#2a2a3a', 5), f'translate({10+k*20},{170+(k%2)*8})') for k in range(10)), False)
S_('choir', R(0, 0, 200, 200, '#f2ead8') + ''.join(G(Ci(0, -16, 10, SK) + Pa('M-10,-20 Q0,-30 10,-20 Z', ['#3a2a20', '#5a3a2a', P['grey']][(k + r_) % 3]) + E(0, -12, 3, 3, '#a8502a') + Pa('M-14,30 L-12,-4 L12,-4 L14,30 Z', '#7a2a6a') + R(-6, -4, 12, 6, '#ffffff', 2), f'translate({30+k*35+r_*17},{90+r_*50})') for r_ in range(2) for k in range(5 - r_)) + note(100, 30, 1.0), False)
S_('erhu', erhu_(100, 160, 1.0))
S_('trumpet', trumpet_(100, 100, 1.0, -10))
S_('saxophone', sax_(90, 110, 1.2))
S_('harmonica', harmonica_(100, 100, 1.1) + note(150, 50, .9))
S_('accordion', accordion_(100, 100, 1.0))

# ================= 音乐 2 =================
S_('loud', speaker_(60, 100, 1.0) + ''.join(St(f'M{110+k*20},{50-k*10} Q{140+k*24},100 {110+k*20},{150+k*10}', '#e2463b', 6) for k in range(3)))
S_('soft', speaker_(60, 100, 1.0) + St('M110,90 Q118,100 110,110', '#9fd0ec', 3) + G(Pa('M0,0 Q-20,-30 6,-60 Q26,-30 0,0 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"'), 'translate(150,140) rotate(40)'))
S_('volume', ''.join(R(30 + k * 26, 150 - k * 20, 18, 20 + k * 20, '#3c7fc1' if k < 4 else '#c4cbd0', 3) for k in range(6)) + G(Ci(0, 0, 26, '#5d6469') + Ci(0, 0, 20, '#2f3437') + L(0, 0, 12, -14, '#ffffff', 3), 'translate(150,50)') + speaker_(40, 50, .35))
S_('headphones', headphones_(100, 110, 1.4))
S_('speaker', speaker_(100, 100, 1.3))
S_('melody', staff(80) + St('M20,110 Q50,60 80,90 T140,80 T190,70', '#e2463b', 3) + ''.join(note(30 + k * 32, 110 - (k % 3) * 12, .8, '#3c7fc1') for k in range(5)))
S_('rhythm', G(Pa('M-40,60 L-20,-70 L20,-70 L40,60 Z', '#a8603a') + R(-30, 40, 60, 20, '#8a4a2a') + L(0, 50, 30, -50, '#2f3437', 3) + R(26, -30, 12, 10, '#5d6469', 2), 'translate(70,110)') + ''.join(R(130 + k * 16, 100 - (20 if k % 2 == 0 else 0), 10, 60 + (20 if k % 2 == 0 else 0), '#3c7fc1', 3) for k in range(4)))
S_('instrument', guitar_(60, 130, .6, -20) + violin_(130, 80, .7, 20) + trumpet_(140, 150, .5, 0) + drum_(60, 170, .4) + flute_(100, 30, .5, 0))
S_('practice', R(0, 0, 200, 200, '#f2ead8') + piano_(110, 170, .8) + G(pose((0, -120), (0, -100), (0, -56), arms=[[(8, -96), (30, -80), (44, -76)]], legs=[[(0, -56), (20, -54), (24, -10)]], back_arm=[[(-6, -96), (24, -80), (40, -78)]], shirt='#f3c234', pants='#3b4a5a', hr=14, tw=26, style='long', hair='#3a2a20'), 'translate(36,190)') + calendar_(140, 20, 50, 46, [1, 2, 3, 4, 5], '#e2463b', '#5ba644'), False)
S_('karaoke', R(0, 0, 200, 200, '#2a1a4a') + R(30, 20, 140, 80, '#1a1a2a', 4) + R(36, 26, 128, 68, '#3c3a7a') + R(50, 70, 100, 8, '#f3c234', 4) + R(50, 70, 50, 8, '#e2463b', 4) + note(80, 50, .7, '#ffffff') + mic_(100, 140, .8, 10) + ''.join(Ci(20 + k * 40, 180, 6, ['#e2463b', '#3c7fc1', '#f3c234', '#5ba644', '#ef8fa4'][k]) for k in range(5)), False)
S_('classical-music', R(0, 0, 200, 200, '#f2ead8') + staff(30) + violin_(70, 130, .9, -20) + bow_(40, 170, 120, 90) + G(R(-20, -10, 40, 50, '#e6dcc8') + Ci(0, -24, 16, '#d9d4cc') + Pa('M-16,-30 Q-20,-46 0,-44 Q20,-46 16,-30 Q20,-10 14,-14 L-14,-14 Q-20,-10 -16,-30 Z', '#f6efe0'), 'translate(150,140)'), False)
S_('pop-music', R(0, 0, 200, 200, '#3a1a5a') + ''.join(Ci(30 + k * 36, 30 + (k % 2) * 16, 10, ['#ef8fa4', '#f3c234', '#7cc05a', '#9fd0ec', '#e2463b'][k], 'opacity=".8"') for k in range(5)) + W(100, 196, .95, '#ef8fa4', '#2f3437', arms='wave', style='long', hair='#f3c234') + mic_(90, 70, .4, -10) + note(160, 120, 1.0, '#f3c234'), False)
S_('folk-song', R(0, 0, 200, 200, '#fbe8cc') + Pa('M0,140 Q60,110 120,130 Q160,140 200,120 L200,200 L0,200 Z', '#9ac070') + house(160, 140, 40, 30) + G(pose((0, -120), (0, -100), (0, -56), arms=[[(8, -96), (30, -80)]], legs=[[(0, -56), (24, -54), (24, -10)]], shirt='#e2463b', pants='#3b4a5a', hr=14, tw=26) + guitar_(18, -70, .35, -60), 'translate(70,190)') + note(120, 60, 1.0, '#8a5a35'), False)
S_('jazz', R(0, 0, 200, 200, '#1a1a3a') + Pa('M60,0 L140,0 L170,200 L30,200 Z', '#7a4fa0', 'opacity=".25"') + sax_(100, 100, 1.1) + note(160, 50, 1.0, '#f3c234') + note(40, 60, .8, '#f3c234') + moon(170, 160, 12), False)
S_('rock-music', R(0, 0, 200, 200, '#2a2a2a') + guitar_(100, 120, 1.0, -30, '#e2463b', True) + bolt_icon(40, 50, .8) + bolt_icon(160, 40, .7), False)
S_('orchestra', R(0, 0, 200, 200, '#2a1a2a') + R(0, 150, 200, 50, '#8a5a35') + ''.join(G(Ci(0, -14, 8, SK) + Pa('M-12,20 L-10,-4 L10,-4 L12,20 Z', '#2f3437') + violin_(10, 2, .25, 30), f'translate({20+k*24+(r_%2)*12},{110+r_*30})') for r_ in range(2) for k in range(7)) + W(100, 196, .5, '#2f3437', '#2f3437', arms='up') + L(118, 104, 136, 84, '#ffffff', 2), False)

# ================= 博物馆 =================
S_('museum', R(0, 0, 200, 200, SKY) + R(0, 176, 200, 24, WALK) + Pa('M10,70 L100,26 L190,70 Z', '#e6dcc8') + R(10, 70, 180, 10, '#d9d0c0') + ''.join(R(20 + k * 32, 80, 16, 86, '#f4f1ea') for k in range(6)) + R(4, 166, 192, 10, '#d9d0c0') + Pa('M70,58 L100,40 L130,58 Z', '#c4bcae'), False)
S_('art', G(E(0, 0, 60, 46, '#e8c890') + Ci(30, 14, 12, '#f6efe0') + ''.join(Ci(-30 + k * 16, -22 + (k % 2) * 8, 9, c) for k, c in enumerate(['#e2463b', '#f3c234', '#5ba644', '#3c7fc1', '#7a4fa0'])), 'translate(80,120)') + paint_brush(150, 60, .9, 40, '#e2463b'))
S_('painting', frame_(30, 40, 140, 100, landscape(30, 40, 140, 100)))
S_('gallery', R(0, 0, 200, 200, '#f2ead8') + R(0, 160, 200, 40, '#c8a070') + frame_(20, 30, 60, 46, landscape(20, 30, 60, 46)) + frame_(110, 20, 70, 60, R(110, 20, 70, 60, '#f6d0dc') + Ci(145, 50, 18, '#e2463b')) + frame_(40, 100, 40, 50, R(40, 100, 40, 50, '#9fd0ec') + Pa('M40,150 L60,110 L80,150 Z', '#3c7fc1')) + W(140, 196, .45, '#3c7fc1', '#3b4a5a') + R(96, 150, 30, 6, '#a7adb1', 0, 'opacity="0"'), False)
S_('statue', R(0, 0, 200, 200, SKY) + statue_(100, 190, 1.0), False)
S_('exhibition', R(0, 0, 200, 200, '#f2ead8') + R(0, 160, 200, 40, '#c8a070') + ''.join(R(20 + k * 64, 110, 40, 50, '#5d6469') + R(20 + k * 64, 70, 40, 40, '#dff1fb', 2, 'opacity=".7"') for k in range(3)) + vase(40, 106, .3) + G(Ci(0, 0, 12, '#d9a33a') + star(0, 0, 6, '#f3e070'), 'translate(104,92)') + G(R(-10, -14, 20, 28, '#8a5a35', 3), 'translate(168,92)') + W(140, 196, .4, '#e2463b', '#3b4a5a') + W(80, 196, .42, '#5ba644', '#3b4a5a'), False)
S_('sculpture', R(30, 150, 140, 30, '#c4bcae') + Pa('M60,150 Q50,100 80,80 Q110,60 100,30 Q140,50 130,100 Q120,130 140,150 Z', '#a7adb1') + hi(90, 80, 10, 24, .4, 20))
S_('antique', vase(70, 180, .7, '#c8a070', '#7a3a20') + G(R(-30, -60, 60, 90, '#8a5a35', 6) + Ci(0, -30, 20, '#f6efe0') + clock(0, -30, 18, (10, 10)) + R(-30, 24, 60, 8, '#6a3a20'), 'translate(150,150)'))
S_('porcelain', vase(100, 180, 1.2))
S_('calligraphy', R(30, 10, 140, 180, '#f6efe0', 2) + R(30, 10, 140, 10, '#8a5a35') + R(30, 180, 140, 10, '#8a5a35') + T(100, 120, '福', 90, '#2f3437', 900, family='KaiTi, STKaiti, serif') + R(130, 150, 20, 20, '#e2463b', 2))
S_('audio-guide', R(0, 0, 200, 200, '#f2ead8') + G(R(-24, -60, 48, 120, '#2f3437', 12) + R(-18, -50, 36, 30, '#9fd0ec', 4) + ''.join(Ci(-10 + (k % 3) * 10, 0 + (k // 3) * 12, 4, '#a7adb1') for k in range(9)), 'translate(70,110)') + headphones_(145, 80, .6, '#2f3437') + ''.join(St(f'M{140+k*10},{120+k*6} q8,10 0,20', '#3c7fc1', 2) for k in range(0)), False)
S_('entrance-fee', R(0, 0, 200, 200, '#f2ead8') + R(20, 40, 160, 120, '#c8a070', 4) + R(30, 50, 140, 60, '#dff1fb', 2) + person_bust(100, 82, 18, '#3c7fc1') + R(20, 110, 160, 10, '#8a5a35') + G(R(-40, -20, 80, 40, '#f3c234', 4) + T(-10, 8, '¥40', 18, '#2f3437', 900) + L(18, -20, 18, 20, '#ffffff', 2), 'translate(100,150) rotate(-6)'), False)
S_('no-flash', camera_(100, 100, 1.1) + bolt_icon(140, 50, .6) + Ci(100, 100, 80, 'none', 'stroke="#e2463b" stroke-width="10"') + L(44, 44, 156, 156, '#e2463b', 10))
S_('collection', R(20, 20, 160, 160, '#8a5a35', 4) + ''.join(R(26, 26 + r_ * 52, 148, 46, '#dff1fb', 2, 'opacity=".5"') for r_ in range(3)) + ''.join(G(c, f'translate({50+k*50},{60+r_*52})') for r_ in range(3) for k, c in enumerate([Ci(0, 0, 12, ['#d9a33a', '#c4cbd0', '#c8703a'][r_]), Pa('M-10,14 L-8,-10 L8,-10 L10,14 Z', ['#3c7fc1', '#e2463b', '#5ba644'][r_]), star(0, 0, 10, ['#f3c234', '#ef8fa4', '#7a4fa0'][r_])])))
S_('masterpiece', R(0, 0, 200, 200, '#3a2a2a') + Pa('M70,0 L130,0 L180,200 L20,200 Z', '#f3e070', 'opacity=".15"') + frame_(40, 40, 120, 100, landscape(40, 40, 120, 100), '#d9a33a') + R(70, 160, 60, 16, '#d9a33a', 2) + star(100, 20, 10, '#f3e070'), False)
S_('gift-shop', R(0, 0, 200, 200, '#f6efe0') + R(0, 0, 200, 30, '#e2463b') + ''.join(Pa(f'M{k*25},30 Q{k*25+12},44 {k*25+25},30 Z', '#e2463b') for k in range(8)) + R(10, 60, 180, 4, WOOD) + R(10, 110, 180, 4, WOOD) + ''.join(R(16 + k * 30, 64, 24, 30, ['#9fd0ec', '#f6d0dc', '#dff1d8', '#f3e070', '#e6dcf0', '#9fd0ec'][k], 2) for k in range(6)) + ''.join(cup(28 + k * 34, 98, 20, 18, ['#ffffff', '#e2463b', '#3c7fc1', '#f3c234', '#5ba644'][k]) for k in range(5)) + teddy(60, 160, .4) + bag_(130, 140, 34, 40, '#e2463b'), False)

dump()
