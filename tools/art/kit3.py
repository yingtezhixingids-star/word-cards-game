from kit2 import *

HL = '#e2463b'

def ring(x, y, r, col=HL, w=4):
    return Ci(x, y, r, 'none', f'stroke="{col}" stroke-width="{w}"') + Ci(x, y, r, col, 'opacity=".12"')

def big_face(cx, cy, r, hair='#3a2a20', style='short', eyes='dot', m='smile', brows=None, blush=None, skin=None):
    """大脸：r 一般 50-60"""
    skin = skin or SK
    g = ''
    if style == 'long':
        g += Pa(f'M{cx-r*1.05},{cy+r*1.2} Q{cx-r*1.3},{cy-r*1.2} {cx},{cy-r*1.12} Q{cx+r*1.3},{cy-r*1.2} {cx+r*1.05},{cy+r*1.2} Z', hair)
    g += E(cx - r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08)) + E(cx + r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08))
    g += E(cx, cy, r * .92, r, skin)
    if style in ('short', 'long', 'bun'):
        g += Pa(f'M{cx-r*.95},{cy-r*.05} Q{cx-r*1.0},{cy-r*1.15} {cx},{cy-r*1.08} Q{cx+r*1.0},{cy-r*1.15} {cx+r*.95},{cy-r*.05} Q{cx+r*.7},{cy-r*.6} {cx+r*.1},{cy-r*.55} Q{cx-r*.6},{cy-r*.45} {cx-r*.95},{cy-r*.05} Z', hair)
        if style == 'bun': g += Ci(cx, cy - r * 1.05, r * .4, hair)
    elif style == 'grey':
        g += Pa(f'M{cx-r*.95},{cy-r*.1} Q{cx-r*1.0},{cy-r*1.1} {cx},{cy-r*1.06} Q{cx+r*1.0},{cy-r*1.1} {cx+r*.95},{cy-r*.1} Q{cx+r*.6},{cy-r*.7} {cx},{cy-r*.68} Q{cx-r*.6},{cy-r*.7} {cx-r*.95},{cy-r*.1} Z', P['grey'])
    ex, ey = r * .34, cy - r * .02
    sw = max(2, r * .06)
    if eyes == 'dot': g += Ci(cx - ex, ey, r * .07, '#2b211b') + Ci(cx + ex, ey, r * .07, '#2b211b') + Ci(cx - ex + r * .02, ey - r * .02, r * .02, '#ffffff') + Ci(cx + ex + r * .02, ey - r * .02, r * .02, '#ffffff')
    elif eyes == 'big': g += E(cx - ex, ey, r * .12, r * .15, '#ffffff') + E(cx + ex, ey, r * .12, r * .15, '#ffffff') + Ci(cx - ex, ey, r * .07, '#2b211b') + Ci(cx + ex, ey, r * .07, '#2b211b')
    elif eyes == 'up': g += St(f'M{cx-ex-r*.12},{ey+r*.03} q{r*.12},{-r*.12} {r*.24},0', '#3a2a20', sw) + St(f'M{cx+ex-r*.12},{ey+r*.03} q{r*.12},{-r*.12} {r*.24},0', '#3a2a20', sw)
    elif eyes == 'closed': g += St(f'M{cx-ex-r*.12},{ey} q{r*.12},{r*.08} {r*.24},0', '#3a2a20', sw) + St(f'M{cx+ex-r*.12},{ey} q{r*.12},{r*.08} {r*.24},0', '#3a2a20', sw)
    elif eyes == 'shut': g += St(f'M{cx-ex-r*.12},{ey-r*.08} L{cx-ex+r*.08},{ey} L{cx-ex-r*.12},{ey+r*.08}', '#3a2a20', sw) + St(f'M{cx+ex+r*.12},{ey-r*.08} L{cx+ex-r*.08},{ey} L{cx+ex+r*.12},{ey+r*.08}', '#3a2a20', sw)
    elif eyes == 'side': g += Ci(cx - ex + r * .06, ey, r * .07, '#2b211b') + Ci(cx + ex + r * .06, ey, r * .07, '#2b211b')
    if brows == 'sad': g += L(cx - ex - r * .14, ey - r * .16, cx - ex + r * .1, ey - r * .24, '#3a2a20', sw) + L(cx + ex + r * .14, ey - r * .16, cx + ex - r * .1, ey - r * .24, '#3a2a20', sw)
    elif brows == 'angry': g += L(cx - ex - r * .14, ey - r * .26, cx - ex + r * .12, ey - r * .14, '#3a2a20', sw * 1.3) + L(cx + ex + r * .14, ey - r * .26, cx + ex - r * .12, ey - r * .14, '#3a2a20', sw * 1.3)
    elif brows == 'up': g += St(f'M{cx-ex-r*.14},{ey-r*.2} q{r*.14},{-r*.12} {r*.28},0', '#3a2a20', sw) + St(f'M{cx+ex-r*.14},{ey-r*.2} q{r*.14},{-r*.12} {r*.28},0', '#3a2a20', sw)
    elif brows == 'flat': g += L(cx - ex - r * .12, ey - r * .2, cx - ex + r * .12, ey - r * .2, '#3a2a20', sw) + L(cx + ex - r * .12, ey - r * .2, cx + ex + r * .12, ey - r * .2, '#3a2a20', sw)
    if blush: g += E(cx - r * .5, cy + r * .3, r * .16, r * .09, blush, 'opacity=".6"') + E(cx + r * .5, cy + r * .3, r * .16, r * .09, blush, 'opacity=".6"')
    g += Pa(f'M{cx},{cy+r*.05} q{-r*.1},{r*.2} {r*.03},{r*.24}', 'none', f'stroke="{shade(skin, -.25)}" stroke-width="{sw}" stroke-linecap="round"')
    my = cy + r * .5
    if m == 'smile': g += St(f'M{cx-r*.25},{my-r*.06} q{r*.25},{r*.2} {r*.5},0', '#9a4a3a', sw)
    elif m == 'grin': g += Pa(f'M{cx-r*.32},{my-r*.08} Q{cx},{my+r*.36} {cx+r*.32},{my-r*.08} Z', '#9a3a30') + Pa(f'M{cx-r*.28},{my-r*.06} L{cx+r*.28},{my-r*.06} L{cx+r*.24},{my+r*.02} L{cx-r*.24},{my+r*.02} Z', '#ffffff')
    elif m == 'sad': g += St(f'M{cx-r*.22},{my+r*.06} q{r*.22},{-r*.16} {r*.44},0', '#9a4a3a', sw)
    elif m == 'o': g += E(cx, my + r * .02, r * .1, r * .13, '#7a3a30')
    elif m == 'O': g += E(cx, my + r * .04, r * .16, r * .2, '#7a3a30')
    elif m == 'flat': g += L(cx - r * .18, my, cx + r * .18, my, '#9a4a3a', sw)
    elif m == 'wavy': g += St(f'M{cx-r*.25},{my} q{r*.12},{-r*.1} {r*.25},0 q{r*.12},{r*.1} {r*.25},0', '#9a4a3a', sw)
    elif m == 'shout': g += Pa(f'M{cx-r*.26},{my-r*.06} Q{cx},{my-r*.14} {cx+r*.26},{my-r*.06} Q{cx+r*.2},{my+r*.3} {cx},{my+r*.3} Q{cx-r*.2},{my+r*.3} {cx-r*.26},{my-r*.06} Z', '#7a3a30')
    elif m == 'tongue': g += St(f'M{cx-r*.2},{my} L{cx+r*.2},{my}', '#9a4a3a', sw) + E(cx + r * .04, my + r * .1, r * .1, r * .12, '#ef6a7a')
    return g

def fig(x, ground, kind='man', shirt=None, pants=None, arms='down', legs='stand', s=1.0, mood='smile', coat=None):
    """常用人物：man woman oldman oldwoman boy girl youngman youngwoman"""
    cfg = dict(
        man=dict(shirt='#3c7fc1', pants='#3b4a5a', hair='#3a2a20', style='short', s=1.0),
        woman=dict(shirt='#ef8fa4', pants='#5d6469', hair='#5a3a2a', style='long', s=.96),
        oldman=dict(shirt='#7a8a6a', pants='#5d6469', hair=P['grey'], style='grey', s=.95),
        oldwoman=dict(shirt='#9a7ab8', pants='#5d6469', hair=P['grey'], style='bun', s=.92),
        boy=dict(shirt='#f3c234', pants='#3b5f8f', hair='#3a2a20', style='short', s=.62),
        girl=dict(shirt='#e2463b', pants='#e2463b', hair='#3a2a20', style='long', s=.6),
        youngman=dict(shirt='#5ba644', pants='#3b5f8f', hair='#2a1a10', style='short', s=1.0),
        youngwoman=dict(shirt='#7fc4c0', pants='#3b5f8f', hair='#2a1a10', style='bun', s=.95),
    )[kind]
    return person(x, ground, shirt=shirt or cfg['shirt'], pants=pants or cfg['pants'], hair=cfg['hair'], style=cfg['style'], arms=arms, legs=legs, s=cfg['s'] * s, mood=mood, coat=coat)

def body_front(cx=100, ground=190, shirt='#7fc4c0', pants='#3b5f8f', s=1.0):
    return person(cx, ground, shirt=shirt, pants=pants, arms='down', s=s)

def teddy(x, y, s):
    return G(Ci(-14, -30, 8, '#c8903a') + Ci(14, -30, 8, '#c8903a') + Ci(0, -18, 18, '#c8903a') + E(0, 12, 20, 22, '#c8903a') + E(0, -12, 8, 6, '#e8c8a0') + Ci(-6, -22, 2.5, '#2f3437') + Ci(6, -22, 2.5, '#2f3437') + E(0, 16, 10, 12, '#e8c8a0') + Ci(-20, 4, 8, '#c8903a') + Ci(20, 4, 8, '#c8903a') + Ci(-12, 32, 9, '#c8903a') + Ci(12, 32, 9, '#c8903a'), f'translate({x},{y}) scale({s})')

def baby_(x, y, s=1, blanket='#9fd0ec'):
    return G(E(0, 14, 30, 26, blanket) + Pa('M-30,14 Q0,40 30,14 L30,30 Q0,50 -30,30 Z', shade(blanket, -.1)) + Ci(0, -14, 20, SK) + Pa('M-12,-30 Q0,-40 10,-30', 'none', 'stroke="#3a2a20" stroke-width="2"') + St('M-9,-14 q3,2 6,0 M3,-14 q3,2 6,0', '#3a2a20', 1.6) + E(-10, -6, 4, 2, '#ef9a8a', 'opacity=".6"') + E(10, -6, 4, 2, '#ef9a8a', 'opacity=".6"') + St('M-3,-4 q3,2 6,0', '#9a4a3a', 1.5), f'translate({x},{y}) scale({s})')

def no_sign(x, y, r):
    return Ci(x, y, r, 'none', 'stroke="#d9453a" stroke-width="5"') + L(x - r * .7, y + r * .7, x + r * .7, y - r * .7, '#d9453a', 5)

def shirt_(x, y, s, col, collar='#ffffff'):
    return G(Pa('M-16,-30 L16,-30 L36,-18 L30,-4 L22,-8 L22,30 L-22,30 L-22,-8 L-30,-4 L-36,-18 Z', col) + Pa('M-8,-30 L0,-20 L8,-30 Z', collar), f'translate({x},{y}) scale({s})')

def balloon(x, y, r, col):
    return E(x, y, r, r * 1.2, col) + Pa(f'M{x-3},{y+r*1.2} L{x+3},{y+r*1.2} L{x},{y+r*1.2+5} Z', col) + St(f'M{x},{y+r*1.2+4} q-6,14 2,30', '#a7adb1', 1.2) + hi(x - r * .35, y - r * .4, r * .2, r * .3, .5, 20)

def confetti(seed=1, n=20, area=(10, 10, 180, 80)):
    random.seed(seed)
    x0, y0, w, h = area
    return ''.join(R(random.uniform(x0, x0 + w), random.uniform(y0, y0 + h), 6, 3, random.choice(['#e2463b', '#f3c234', '#5ba644', '#3c7fc1', '#ef8fa4']), 1, f'transform="rotate({random.uniform(0,180):.0f} {x0+w/2} {y0+h/2})"') for _ in range(n))

def halo(x, ground, h=150, w=40):
    return E(x, ground - h / 2, w, h / 2 + 6, '#f3c234', 'opacity=".22"') + E(x, ground - h / 2, w, h / 2 + 6, 'none', 'stroke="#f3c234" stroke-width="3"')


def officer(cx, cy, r, shirt='#2f4a7a', hat='#1f3a5a', badge='#f3c234'):
    g = person_bust(cx, cy, r, shirt, '#3a2a20', 'short', 'dot', 'flat')
    g += Pa(f'M{cx-r*1.05},{cy-r*.45} L{cx+r*1.05},{cy-r*.45} L{cx+r*.9},{cy-r*1.3} Q{cx},{cy-r*1.5} {cx-r*.9},{cy-r*1.3} Z', hat) + R(cx - r * 1.2, cy - r * .55, r * 2.4, 6, '#1a2a3a', 2) + star(cx, cy - r * .95, r * .2, badge)
    g += star(cx - r * .9, cy + r * 1.7, r * .22, badge) + R(cx + r * .4, cy + r * 1.5, r * .5, r * .1, '#ffffff', 1)
    return g


def dash_icon(x, y, r):
    return Ci(x, y, r, '#2f3437') + Ci(x, y, r * .8, '#1f2a35') + ''.join(L(x + r * .65 * math.cos(a), y + r * .65 * math.sin(a), x + r * .78 * math.cos(a), y + r * .78 * math.sin(a), '#ffffff', 1.5) for a in [math.pi + k * math.pi / 8 for k in range(9)]) + L(x, y, x + r * .6 * math.cos(-.6), y + r * .6 * math.sin(-.6), '#e2463b', 2.5) + Ci(x, y, 3, '#e2463b')

def steering(x, y, r):
    return Ci(x, y, r, 'none', 'stroke="#2f3437" stroke-width="10"') + Ci(x, y, r * .3, '#2f3437') + L(x - r, y, x + r, y, '#2f3437', 8) + L(x, y, x, y + r, '#2f3437', 8)

