from flat import *

def drop(cx, cy, s, color='#9fd0ec'):
    return Pa(f'M{cx},{cy-s} Q{cx+s*.75},{cy} {cx},{cy+s*.55} Q{cx-s*.75},{cy} {cx},{cy-s} Z', color)

def cheeks(cx, cy, r, col='#ef7a7a', op='.75'):
    return E(cx - r * .5, cy + r * .3, r * .2, r * .12, col, f'opacity="{op}"') + E(cx + r * .5, cy + r * .3, r * .2, r * .12, col, f'opacity="{op}"')

def shut_eyes(cx, cy, r, col='#3a2a20'):
    """用力闭眼（><）"""
    ex, ey = r * .34, cy - r * .02
    return (St(f'M{cx-ex-5},{ey-4} L{cx-ex+3},{ey} L{cx-ex-5},{ey+4}', col, 2.4) +
            St(f'M{cx+ex+5},{ey-4} L{cx+ex-3},{ey} L{cx+ex+5},{ey+4}', col, 2.4))

def body(cx, cy, r, shirt, w=None):
    """只画肩膀和脖子，脸单独画"""
    w = w or r * 3.4
    top = cy + r * .95
    g = R(cx - r * .3, cy + r * .6, r * .6, r * .6, shade(P['skin'], -.1), 4)
    g += Pa(f'M{cx-w/2},200 L{cx-w/2},{top+r*.7} Q{cx-w/2},{top} {cx-w/2+r*.8},{top} L{cx+w/2-r*.8},{top} Q{cx+w/2},{top} {cx+w/2},{top+r*.7} L{cx+w/2},200 Z', shirt)
    g += Pa(f'M{cx+w/2-r*.2},200 L{cx+w/2-r*.2},{top+r*.8} Q{cx+w/2},{top+r*.3} {cx+w/2},{top+r*.7} L{cx+w/2},200 Z', shade(shirt, -.15))
    return g

def bare_head(cx, cy, r, hair, style):
    """头型+头发，不画五官（五官自己画）"""
    skin = P['skin']
    s = ''
    if style == 'long':
        s += Pa(f'M{cx-r*1.05},{cy+r*1.3} Q{cx-r*1.3},{cy-r*1.2} {cx},{cy-r*1.12} Q{cx+r*1.3},{cy-r*1.2} {cx+r*1.05},{cy+r*1.3} Z', hair)
    s += E(cx - r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08)) + E(cx + r * .95, cy + r * .1, r * .17, r * .25, shade(skin, -.08))
    s += E(cx, cy, r * .92, r, skin)
    if style == 'grey':
        s += Pa(f'M{cx-r*.95},{cy-r*.1} Q{cx-r*1.0},{cy-r*1.1} {cx},{cy-r*1.06} Q{cx+r*1.0},{cy-r*1.1} {cx+r*.95},{cy-r*.1} Q{cx+r*.6},{cy-r*.7} {cx},{cy-r*.68} Q{cx-r*.6},{cy-r*.7} {cx-r*.95},{cy-r*.1} Z', P['grey'])
    else:
        s += Pa(f'M{cx-r*.95},{cy-r*.05} Q{cx-r*1.0},{cy-r*1.15} {cx},{cy-r*1.08} Q{cx+r*1.0},{cy-r*1.15} {cx+r*.95},{cy-r*.05} Q{cx+r*.7},{cy-r*.6} {cx+r*.1},{cy-r*.55} Q{cx-r*.6},{cy-r*.45} {cx-r*.95},{cy-r*.05} Z', hair)
    return s

def nose_line(cx, cy, r):
    return Pa(f'M{cx},{cy+r*.05} q{-r*.1},{r*.2} {r*.03},{r*.24}', 'none', f'stroke="{shade(P["skin"], -.25)}" stroke-width="2" stroke-linecap="round"')

def brows_sad(cx, cy, r):
    ex, ey = r * .34, cy - r * .02
    return L(cx - ex - 6, ey - 8, cx - ex + 4, ey - 12, '#3a2a20', 2.2) + L(cx + ex + 6, ey - 8, cx + ex - 4, ey - 12, '#3a2a20', 2.2)

def tissue_box(x, y, w=56, h=34):
    g = R(x, y, w, h, '#7fb4d9', 5) + R(x + w - 10, y, 10, h, shade('#7fb4d9', -.15), 0)
    g += R(x + 6, y + 8, w - 22, h - 16, '#a6cbe6', 3)
    g += E(x + w / 2, y + 2, w * .25, 4, '#4f86ad')
    g += Pa(f'M{x+w/2-10},{y+2} Q{x+w/2-14},{y-22} {x+w/2+2},{y-26} Q{x+w/2+6},{y-12} {x+w/2+12},{y+2} Z', '#ffffff')
    g += Pa(f'M{x+w/2+2},{y-26} Q{x+w/2+6},{y-12} {x+w/2+12},{y+2} L{x+w/2+4},{y+2} Q{x+w/2+2},{y-12} {x+w/2+2},{y-26} Z', '#e6ecef')
    return g


def puff(x, y, s=1, op=1, col='#c9d6dc'):
    return G(Ci(0, 0, 9, col) + Ci(10, -4, 11, col) + Ci(21, 1, 8, col) + Ci(10, 6, 9, col), f'translate({x},{y}) scale({s})" opacity="{op}')

def eyes_dot(cx, cy, r, dy=0):
    return Ci(cx - r * .34, cy + dy, 2.6, '#2b211b') + Ci(cx + r * .34, cy + dy, 2.6, '#2b211b')

def eyes_closed(cx, cy, r, up=False):
    q = -3 if up else 3
    return St(f'M{cx-r*.34-5},{cy} q5,{q} 10,0', '#3a2a20', 2.4) + St(f'M{cx+r*.34-5},{cy} q5,{q} 10,0', '#3a2a20', 2.4)

def mouth(cx, cy, r, kind='smile'):
    if kind == 'smile': return St(f'M{cx-r*.25},{cy+r*.42} q{r*.25},{r*.2} {r*.5},0', '#9a4a3a', 2.2)
    if kind == 'sad': return St(f'M{cx-r*.22},{cy+r*.55} q{r*.22},{-r*.16} {r*.44},0', '#9a4a3a', 2.2)
    if kind == 'wavy': return St(f'M{cx-r*.25},{cy+r*.55} q{r*.12},{-r*.1} {r*.25},0 q{r*.12},{r*.1} {r*.25},0', '#9a4a3a', 2.2)
    if kind == 'o': return E(cx, cy + r * .55, r * .13, r * .15, '#7a3a30')
    if kind == 'grit': return R(cx - r * .25, cy + r * .44, r * .5, r * .2, '#ffffff', 3) + L(cx - r * .25, cy + r * .54, cx + r * .25, cy + r * .54, '#c4b5aa', 1.2)
    if kind == 'flat': return L(cx - r * .18, cy + r * .5, cx + r * .18, cy + r * .5, '#9a4a3a', 2.2)
    return ''

def face_full(cx, cy, r, hair='#3a2a20', style='short', eyes='dot', m='smile', brows=None, blush=None):
    g = bare_head(cx, cy, r, hair, style)
    if eyes == 'dot': g += eyes_dot(cx, cy, r)
    elif eyes == 'closed': g += eyes_closed(cx, cy, r)
    elif eyes == 'shut': g += shut_eyes(cx, cy, r)
    elif eyes == 'up': g += eyes_closed(cx, cy, r, True)
    if brows == 'sad': g += brows_sad(cx, cy, r)
    if blush: g += cheeks(cx, cy, r, blush, '.6')
    g += nose_line(cx, cy, r) + mouth(cx, cy, r, m)
    return g

def bandage(x, y, w, h, rot=0):
    g = R(-w / 2, -h / 2, w, h, '#e9c79c', h / 2) + R(-w * .18, -h / 2, w * .36, h, '#d6b083', 2)
    g += ''.join(Ci(-w * .36 + i * w * .1, (-1) ** i * h * .15, 1.2, '#c99f72') for i in range(3))
    g += ''.join(Ci(w * .18 + i * w * .1, (-1) ** i * h * .15, 1.2, '#c99f72') for i in range(3))
    return G(g, f'translate({x},{y}) rotate({rot})')

import math
def clock(cx, cy, r, hm=(10, 2), face='#ffffff', rim='#2f3437'):
    g = Ci(cx, cy, r, rim) + Ci(cx, cy, r * .86, face)
    for i in range(12):
        a = i * math.pi / 6
        g += L(cx + r * .72 * math.cos(a), cy + r * .72 * math.sin(a), cx + r * .8 * math.cos(a), cy + r * .8 * math.sin(a), '#2f3437', 2)
    h, m = hm
    g += L(cx, cy, cx + r * .4 * math.sin(h / 6 * math.pi), cy - r * .4 * math.cos(h / 6 * math.pi), '#2f3437', 4)
    g += L(cx, cy, cx + r * .6 * math.sin(m / 6 * math.pi), cy - r * .6 * math.cos(m / 6 * math.pi), '#2f3437', 3) + Ci(cx, cy, 3, '#d9453a')
    return g

def cross(cx, cy, s, col='#d9453a'):
    return R(cx - s * .3, cy - s, s * .6, s * 2, col, 1) + R(cx - s, cy - s * .3, s * 2, s * .6, col, 1)

def wheel(cx, cy, r, tire='#2f3437', hub='#c4cbd0'):
    return Ci(cx, cy, r, tire) + Ci(cx, cy, r * .55, hub) + Ci(cx, cy, r * .2, shade(hub, -.3))

def star(x, y, s, c='#f3c234'):
    pts = ' L'.join(f'{x+(s if i%2==0 else s*.45)*math.cos(math.pi/5*i-math.pi/2):.1f},{y+(s if i%2==0 else s*.45)*math.sin(math.pi/5*i-math.pi/2):.1f}' for i in range(10))
    return Pa('M' + pts + ' Z', c)

def heart(cx, cy, s, col='#e2463b'):
    return Pa(f'M{cx},{cy+s*.85} C{cx-s*1.3},{cy-s*.05} {cx-s*.75},{cy-s*1.05} {cx},{cy-s*.4} C{cx+s*.75},{cy-s*1.05} {cx+s*1.3},{cy-s*.05} {cx},{cy+s*.85} Z', col)

def coat_over(cx, cy, r, w=None, coat='#ffffff', shirt='#7fb3d8'):
    """白大褂：在 body() 之上叠两片衣襟"""
    w = w or r * 3.4; top = cy + r * .95
    g = Pa(f'M{cx-w/2},200 L{cx-w/2},{top+r*.7} Q{cx-w/2},{top} {cx-w/2+r*.8},{top} L{cx-r*.35},{top} L{cx-r*.05},200 Z', coat)
    g += Pa(f'M{cx+w/2},200 L{cx+w/2},{top+r*.7} Q{cx+w/2},{top} {cx+w/2-r*.8},{top} L{cx+r*.35},{top} L{cx+r*.05},200 Z', coat)
    g += Pa(f'M{cx+w/2-r*.2},200 L{cx+w/2-r*.2},{top+r*.8} Q{cx+w/2},{top+r*.3} {cx+w/2},{top+r*.7} L{cx+w/2},200 Z', shade(coat, -.1))
    return g

def stetho(cx, cy, r):
    top = cy + r * .95
    return (St(f'M{cx-r*.4},{top} Q{cx-r*.5},{top+r*.9} {cx-r*.1},{top+r*1.25}', '#4a5157', 3) +
            St(f'M{cx+r*.4},{top} Q{cx+r*.35},{top+r*.6} {cx+r*.15},{top+r*.95}', '#4a5157', 3) + Ci(cx - r * .1, top + r * 1.3, 5, '#a7adb1'))

def stripes_body(cx, cy, r, c1, c2, w=None):
    """条纹病号服"""
    w = w or r * 3.4; top = cy + r * .95
    clip = f'M{cx-w/2},200 L{cx-w/2},{top+r*.7} Q{cx-w/2},{top} {cx-w/2+r*.8},{top} L{cx+w/2-r*.8},{top} Q{cx+w/2},{top} {cx+w/2},{top+r*.7} L{cx+w/2},200 Z'
    cid = f'cl{int(cx)}{int(cy)}'
    g = R(cx - r * .3, cy + r * .6, r * .6, r * .6, shade(P['skin'], -.1), 4)
    g += f'<clipPath id="{cid}"><path d="{clip}"/></clipPath>' + Pa(clip, c1)
    g += f'<g clip-path="url(#{cid})">' + ''.join(R(cx - w / 2 + i * 12, top, 6, 200, c2) for i in range(int(w / 12) + 1)) + '</g>'
    g += Pa(f'M{cx-r*.4},{top} L{cx},{top+r*.5} L{cx+r*.4},{top} Z', shade(P['skin'], -.1))
    return g

SK = P['skin']; SKD = shade(P['skin'], -.12)

def hand(x, y, s=1, rot=0, skin=None, spread=False):
    """手背朝上的手，手指朝上。原点在手腕"""
    skin = skin or SK; d = shade(skin, -.12)
    g = R(-22, -46, 44, 50, skin, 16)
    fx = [(-17, 34), (-6, 42), (5, 40), (15, 32)]
    for i, (fxx, l) in enumerate(fx):
        ang = (i - 1.5) * 6 if spread else 0
        g += G(R(-5.5, -l, 11, l + 4, skin, 5.5) + R(-3.5, -l + 3, 7, 6, shade(skin, .25), 3), f'translate({fxx},-42) rotate({ang})')
    g += G(R(-6, -30, 12, 32, skin, 6), 'translate(-22,-18) rotate(-40)')
    g += R(-22, -12, 44, 16, d, 8)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')

def burst(x, y, r, col='#d9453a', n=8):
    import math
    pts = []
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2)
        rr = r if i % 2 == 0 else r * .5
        pts.append(f'{x+rr*math.cos(a):.1f},{y+rr*math.sin(a):.1f}')
    return Pa('M' + ' L'.join(pts) + ' Z', col, 'opacity=".9"')

def pain_lines(x, y, r, col='#d9453a', n=5, a0=0, a1=360):
    import math
    g = ''
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / max(1, n - 1))
        g += L(x + r * math.cos(a), y + r * math.sin(a), x + r * 1.5 * math.cos(a), y + r * 1.5 * math.sin(a), col, 3.5)
    return g


def pose(head, sh, hip, arms, legs, shirt='#3c7fc1', pants='#28456b', skin=None, hair='#3a2a20', style='short', mood='smile',
         hr=15, tw=32, lw=14, aw=11, shoes='#2f2a27', back_arm=None, back_leg=None, face_fn=None):
    """自由姿势人物。arms/legs: 折线点列表的列表（从肩/髋开始）。back_* 先画在身体后面"""
    skin = skin or P['skin']
    g = ''
    def limb(pts, col, w, end, endcol, back=False):
        c = shade(col, -.15) if back else col
        s = St('M' + ' L'.join(f'{x},{y}' for x, y in pts), c, w)
        x, y = pts[-1]
        if end == 'hand': s += Ci(x, y, w * .5, endcol)
        elif end == 'foot':
            px, py = pts[-2]
            dirx = 1 if x >= px - 2 else -1
            s += E(x + dirx * 4, y + 3, 10, 5, endcol)
        return s
    for l in (back_leg or []): g += limb(l, pants, lw, 'foot', shoes, True)
    for a in (back_arm or []): g += limb(a, shirt, aw, 'hand', skin, True)
    for l in legs: g += limb(l, pants, lw, 'foot', shoes)
    # torso as thick rounded stroke
    g += St(f'M{sh[0]},{sh[1]+4} L{hip[0]},{hip[1]}', shirt, tw)
    g += R(head[0] - 4.5, head[1] + hr * .7, 9, 10, shade(skin, -.08), 3)
    for a in arms: g += limb(a, shirt, aw, 'hand', skin)
    if face_fn: g += face_fn(head[0], head[1], hr)
    else: g += headshape(head[0], head[1], hr, skin, hair, style, mood)
    return g

def zzz(x, y, s=1, col='#7a8a94'):
    return T(x, y, 'z', 14 * s, col, 800) + T(x + 10 * s, y - 12 * s, 'z', 18 * s, col, 800) + T(x + 22 * s, y - 28 * s, 'Z', 24 * s, col, 800)

def note(x, y, s=1, col='#7a4fa0'):
    return G(E(0, 20, 7, 5.5, col, 'transform="rotate(-20 0 20)"') + R(5, -10, 3, 30, col) + Pa('M8,-10 Q20,-6 18,6 Q14,-2 8,0 Z', col), f'translate({x},{y}) scale({s})')

def tree(x, y, s=1):
    return G(R(-5, 0, 10, 40, '#8a5a35', 2) + Ci(0, -10, 26, '#5ba644') + Ci(-16, 4, 18, '#4c9a3a') + Ci(16, 2, 18, '#4c9a3a') + Ci(-6, -20, 14, '#6fbb52'), f'translate({x},{y}) scale({s})')

# ---------- 食物通用 ----------
def bowl(cx, cy, w, col='#ffffff', inner='#f4f6f7', fill=None, pattern='#3c7fc1'):
    g = Pa(f'M{cx-w/2},{cy} Q{cx-w/2},{cy+w*.55} {cx},{cy+w*.55} Q{cx+w/2},{cy+w*.55} {cx+w/2},{cy} Z', col)
    g += E(cx, cy, w / 2, w * .12, fill or inner)
    if pattern: g += St(f'M{cx-w*.44},{cy+w*.18} Q{cx},{cy+w*.3} {cx+w*.44},{cy+w*.18}', pattern, 2.5)
    g += R(cx - w * .16, cy + w * .5, w * .32, w * .08, shade(col, -.1), 2)
    return g

def chopsticks(x1, y1, x2, y2, col='#c58b54', gap=6):
    return L(x1, y1, x2, y2, col, 3.5) + L(x1 + gap, y1 + gap * .3, x2 + gap * .4, y2 + gap, col, 3.5)

def cup(cx, cy, w, h, col='#ffffff', liquid=None, handle=True):
    g = ''
    if handle: g += St(f'M{cx+w/2-2},{cy+h*.2} q{w*.3},0 {w*.3},{h*.3} q0,{h*.3} {-w*.3},{h*.3}', col, 5)
    g += Pa(f'M{cx-w/2},{cy} L{cx+w/2},{cy} L{cx+w/2-4},{cy+h} Q{cx},{cy+h+4} {cx-w/2+4},{cy+h} Z', col)
    g += E(cx, cy, w / 2, w * .14, liquid or shade(col, -.08))
    return g

def steam(x, y, n=3, gap=12, col='#c4cbd0', h=1):
    return ''.join(St(f'M{x+i*gap},{y} q-6,{-10*h} 0,{-20*h} q6,{-10*h} 0,{-20*h}', col, 3, 'opacity=".8"') for i in range(n))

def bubble(x, y, w, h, tail=(0, 0)):
    g = E(x, y, w / 2, h / 2, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"')
    tx, ty = tail
    if tx or ty:
        g += Ci(tx, ty, 4, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + Ci((tx + x) / 2 + (tx - x) * .1, (ty + y) / 2 + h * .15, 6, '#ffffff', 'stroke="#c4cbd0" stroke-width="2"')
    return g

def thumbs_up(x, y, s=1, skin=None):
    skin = skin or P['skin']
    g = R(-14, -10, 28, 30, skin, 8) + R(-6, -34, 12, 28, skin, 6) + ''.join(L(-12, -2 + i * 7, 12, -2 + i * 7, shade(skin, -.18), 1.5) for i in range(3))
    return G(g, f'translate({x},{y}) scale({s})')

def diner(cx, cy, r, shirt, hair='#3a2a20', style='short', eyes='dot', m='smile', brows=None, blush=None, w=None):
    return body(cx, cy, r, shirt, w=w) + face_full(cx, cy, r, hair, style, eyes, m, brows, blush)

def badge(x, y, kind, r=18):
    """小动物头像，用来区分 牛/猪/羊/鸭/鸡 肉"""
    g = Ci(x, y, r + 3, '#ffffff') + Ci(x, y, r + 3, 'none', 'stroke="#d9dcde" stroke-width="2"')
    s = r / 18
    if kind == 'cow':
        g += Pa(f'M{x-14*s},{y-12*s} q-8,-6 -6,-12 M{x+14*s},{y-12*s} q8,-6 6,-12', 'none', f'stroke="#d9c7a0" stroke-width="{4*s}" stroke-linecap="round"')
        g += E(x, y, 14 * s, 15 * s, '#ffffff', 'stroke="#2f3437" stroke-width="1.5"') + E(x - 6 * s, y - 6 * s, 6 * s, 5 * s, '#2f3437') + E(x, y + 8 * s, 10 * s, 6 * s, '#f2b8b8')
        g += Ci(x - 3 * s, y + 8 * s, 1.5 * s, '#9a4a3a') + Ci(x + 3 * s, y + 8 * s, 1.5 * s, '#9a4a3a') + Ci(x - 5 * s, y - 2 * s, 1.8 * s, '#2f3437') + Ci(x + 5 * s, y - 2 * s, 1.8 * s, '#2f3437')
    elif kind == 'pig':
        g += Pa(f'M{x-12*s},{y-10*s} l-4,-8 l9,3 Z M{x+12*s},{y-10*s} l4,-8 l-9,3 Z', '#f2a0b0') + Ci(x, y, 14 * s, '#f6b8c4') + E(x, y + 4 * s, 7 * s, 5 * s, '#ef8fa4')
        g += Ci(x - 2.5 * s, y + 4 * s, 1.5 * s, '#9a4a5a') + Ci(x + 2.5 * s, y + 4 * s, 1.5 * s, '#9a4a5a') + Ci(x - 6 * s, y - 4 * s, 1.8 * s, '#2f3437') + Ci(x + 6 * s, y - 4 * s, 1.8 * s, '#2f3437')
    elif kind == 'sheep':
        g += ''.join(Ci(x + 10 * s * math.cos(a), y - 4 * s + 8 * s * math.sin(a), 6 * s, '#f0ece4') for a in [i * math.pi / 4 for i in range(8)])
        g += E(x, y + 2 * s, 8 * s, 11 * s, '#4a4440') + Ci(x - 3 * s, y, 1.5 * s, '#ffffff') + Ci(x + 3 * s, y, 1.5 * s, '#ffffff')
    elif kind == 'duck':
        g += Ci(x - 2 * s, y - 2 * s, 12 * s, '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"') + E(x + 11 * s, y + 2 * s, 8 * s, 4 * s, '#f08a24') + Ci(x + 1 * s, y - 5 * s, 2 * s, '#2f3437')
    elif kind == 'chicken':
        g += Ci(x - 2 * s, y, 12 * s, '#ffffff', 'stroke="#d9dcde" stroke-width="1.5"') + Pa(f'M{x+10*s},{y-1*s} l7,3 l-7,3 Z', '#f3c234') + Pa(f'M{x-8*s},{y-12*s} q3,-7 6,0 q3,-7 6,0 q3,-6 4,2 Z', '#d9453a') + Ci(x + 2 * s, y - 3 * s, 2 * s, '#2f3437') + E(x + 9 * s, y + 6 * s, 2.5 * s, 4 * s, '#d9453a')
    return g

def board(cx, cy, w, h, col='#c58b54'):
    return R(cx - w / 2, cy - h / 2 + 4, w, h, shade(col, -.2), 8) + R(cx - w / 2, cy - h / 2, w, h, col, 8) + Ci(cx + w / 2 - 12, cy, 4, shade(col, -.25))

def fish_shape(cx, cy, l, body='#9fb4c4', belly='#e6ecef', rot=0, fin=None, spots=None, eye=True):
    fin = fin or shade(body, -.15)
    g = Pa(f'M{-l*.5},0 Q{-l*.2},{-l*.28} {l*.25},{-l*.16} Q{l*.42},{-l*.08} {l*.5},0 Q{l*.42},{l*.1} {l*.25},{l*.16} Q{-l*.2},{l*.26} {-l*.5},0 Z', body)
    g += Pa(f'M{-l*.45},{l*.04} Q{-l*.1},{l*.24} {l*.3},{l*.12} Q{l*.42},{l*.06} {l*.48},{l*.02} Q{l*.1},{l*.12} {-l*.45},{l*.04} Z', belly)
    g += Pa(f'M{-l*.46},0 L{-l*.7},{-l*.2} Q{-l*.62},0 {-l*.7},{l*.2} Z', fin)
    g += Pa(f'M{-l*.1},{-l*.2} Q{l*.05},{-l*.34} {l*.14},{-l*.17} Z', fin)
    g += St(f'M{l*.22},{-l*.12} Q{l*.16},0 {l*.22},{l*.12}', shade(body, -.25), 2)
    if spots: g += ''.join(Ci(-l * .3 + i * l * .09, -l * .06 + (i % 3) * l * .04, l * .012 + 1, spots) for i in range(7))
    if eye: g += Ci(l * .34, -l * .03, l * .045 + 1, '#ffffff') + Ci(l * .345, -l * .03, l * .025 + .5, '#2f3437')
    return G(g, f'translate({cx},{cy}) rotate({rot})')

# ---- from diet ----
def apple(cx, cy, s, col='#d93a33'):
    g = Pa(f'M{cx},{cy-18*s} C{cx+12*s},{cy-24*s} {cx+24*s},{cy-14*s} {cx+22*s},{cy+2*s} C{cx+20*s},{cy+18*s} {cx+10*s},{cy+24*s} {cx},{cy+20*s} C{cx-10*s},{cy+24*s} {cx-20*s},{cy+18*s} {cx-22*s},{cy+2*s} C{cx-24*s},{cy-14*s} {cx-12*s},{cy-24*s} {cx},{cy-18*s} Z', col)
    g += hi(cx - 10 * s, cy - 6 * s, 4 * s, 7 * s, .45, 20) + St(f'M{cx},{cy-16*s} l{2*s},{-9*s}', '#6b4423', 2.5 * s) + leaf(cx + 2 * s, cy - 22 * s, 13 * s, 5 * s, -20, '#5ba644')
    return g

def broccoli(cx, cy, s):
    g = Pa(f'M{cx-6*s},{cy+30*s} L{cx-4*s},{cy} L{cx+4*s},{cy} L{cx+6*s},{cy+30*s} Z', '#8cc06a')
    for dx, dy, rr in [(-14, -4, 12), (0, -12, 14), (14, -4, 12), (-6, 2, 10), (8, 2, 10)]:
        g += Ci(cx + dx * s, cy + dy * s, rr * s, '#3c8a3a')
    g += Ci(cx - 4 * s, cy - 16 * s, 5 * s, '#5aaa4a') + Ci(cx + 10 * s, cy - 8 * s, 4 * s, '#5aaa4a')
    return g

def carrot(cx, cy, s, rot=0):
    g = Pa(f'M-8,-30 Q0,-34 8,-30 Q6,10 0,34 Q-6,10 -8,-30 Z', '#f08a24') + Pa('M2,-32 Q8,-30 8,-28 Q6,10 0,34 Q4,6 2,-32 Z', '#d9741a')
    g += ''.join(L(-6, -16 + i * 12, 0, -14 + i * 12, '#d9741a', 1.5) for i in range(3))
    g += leaf(0, -32, 18, 4, -110, '#5ba644') + leaf(0, -32, 18, 4, -70, '#5ba644') + leaf(0, -32, 14, 4, -90, '#3c8a3a')
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def egg(cx, cy, s, cut=False):
    if not cut:
        return E(cx, cy, 16 * s, 21 * s, '#f6ead4') + E(cx + 5 * s, cy + 3 * s, 9 * s, 15 * s, '#e6d4b4', 'opacity=".6"') + hi(cx - 6 * s, cy - 8 * s, 3 * s, 6 * s, .7)
    return E(cx, cy, 18 * s, 22 * s, '#ffffff') + Ci(cx, cy + 2 * s, 10 * s, '#f3b82a')

def drumstick(cx, cy, s, rot=0):
    g = Pa('M-30,-14 Q-40,-32 -18,-34 Q4,-34 16,-14 Q24,0 12,10 Q-6,18 -20,6 Q-28,0 -30,-14 Z', '#c97a3a') + Pa('M-6,-30 Q8,-24 16,-14 Q24,0 12,10 Q8,-4 -6,-30 Z', '#a85f28')
    g += R(10, 4, 26, 8, '#f6efe0', 4, 'transform="rotate(35 10 4)"') + Ci(34, 24, 6, '#f6efe0') + Ci(28, 28, 6, '#f6efe0') + hi(-16, -20, 6, 3, .4, -20)
    return G(g, f'translate({cx},{cy}) rotate({rot}) scale({s})')

def plate(cx, cy, r, col='#ffffff'):
    return E(cx, cy + 4, r, r * .5, '#d9dcde') + E(cx, cy, r, r * .5, col) + E(cx, cy, r * .72, r * .36, '#f4f6f7')

def glass(x, y, w, h, fill='#bfe0ef', level=.75):
    g = Pa(f'M{x},{y} L{x+w},{y} L{x+w-6},{y+h} L{x+6},{y+h} Z', '#e8f4fa', 'opacity=".9"')
    g += Pa(f'M{x+w*.02+ (1-level)*0},{y+h*(1-level)} L{x+w-(1-level)*0-1},{y+h*(1-level)} L{x+w-6},{y+h} L{x+6},{y+h} Z', fill)
    g += R(x + 6, y + 8, 6, h - 16, '#ffffff', 3, 'opacity=".55"')
    return g

def bottle_shape(x, y, w, h, col, neck=.35):
    nw = w * neck
    return Pa(f'M{x+w/2-nw/2},{y} L{x+w/2+nw/2},{y} L{x+w/2+nw/2},{y+h*.2} Q{x+w},{y+h*.3} {x+w},{y+h*.42} L{x+w},{y+h} L{x},{y+h} L{x},{y+h*.42} Q{x},{y+h*.3} {x+w/2-nw/2},{y+h*.2} Z', col)

