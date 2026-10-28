from homekit import *

TILE = '#e6f0f4'

def tiles(x0=0, y0=0, w=200, h=200, s=28, col=TILE):
    return R(x0, y0, w, h, col) + ''.join(L(x0, y0 + k * s, x0 + w, y0 + k * s, '#d0dfe6', 1.5) for k in range(1, int(h / s) + 1)) + ''.join(L(x0 + k * s, y0, x0 + k * s, y0 + h, '#d0dfe6', 1.5) for k in range(1, int(w / s) + 1))


def toilet(cx, base, s=1):
    g = R(cx + 6 * s, base - 120 * s, 50 * s, 60 * s, '#ffffff', 6) + R(cx + 6 * s, base - 124 * s, 50 * s, 10 * s, '#f2efe8', 4) + R(cx + 40 * s, base - 112 * s, 10 * s, 5 * s, '#a7adb1', 2)
    g += Pa(f'M{cx-50*s},{base-60*s} L{cx+20*s},{base-60*s} Q{cx+20*s},{base-24*s} {cx-6*s},{base-20*s} L{cx-6*s},{base} L{cx-30*s},{base} L{cx-30*s},{base-22*s} Q{cx-50*s},{base-30*s} {cx-50*s},{base-60*s} Z', '#ffffff')
    g += E(cx - 15 * s, base - 62 * s, 36 * s, 8 * s, '#e6ecef') + E(cx - 15 * s, base - 64 * s, 30 * s, 5 * s, '#dff1fb')
    return g


def tap_(x, y, s=1, water=False):
    g = St(f'M{x},{y} L{x},{y-30*s} Q{x},{y-44*s} {x+18*s},{y-44*s} L{x+30*s},{y-44*s} L{x+30*s},{y-34*s}', '#a7adb1', 8 * s) + R(x - 12 * s, y - 56 * s, 24 * s, 8 * s, '#5d6469', 3) + R(x - 3 * s, y - 64 * s, 6 * s, 10 * s, '#5d6469', 2)
    if water: g += St(f'M{x+30*s},{y-30*s} L{x+30*s},{y+30*s}', '#9fd0ec', 5 * s)
    return g


def towel(x, y, w, h, col):
    return R(x, y, w, h, col, 4) + R(x, y + h - 14, w, 6, '#ffffff', 0, 'opacity=".6"') + R(x, y + h - 26, w, 4, '#ffffff', 0, 'opacity=".4"')


def bulb(cx, cy, r, on=True):
    g = Ci(cx, cy, r, '#fff3a0' if on else '#e6ecef') + Pa(f'M{cx-r*.5},{cy+r*.8} L{cx+r*.5},{cy+r*.8} L{cx+r*.4},{cy+r*1.2} L{cx-r*.4},{cy+r*1.2} Z', '#fff3a0' if on else '#e6ecef')
    g += R(cx - r * .45, cy + r * 1.2, r * .9, r * .5, '#a7adb1', 2) + ''.join(L(cx - r * .45, cy + r * 1.3 + k * 4, cx + r * .45, cy + r * 1.3 + k * 4, '#8a9196', 1.5) for k in range(2))
    g += St(f'M{cx-r*.3},{cy+r*.6} L{cx-r*.2},{cy} L{cx},{cy+r*.3} L{cx+r*.2},{cy} L{cx+r*.3},{cy+r*.6}', '#d9a020', 2)
    if on: g += ''.join(L(cx + r * 1.3 * math.cos(a), cy + r * 1.3 * math.sin(a), cx + r * 1.7 * math.cos(a), cy + r * 1.7 * math.sin(a), '#f3c234', 3) for a in [math.pi + k * math.pi / 5 for k in range(6)])
    return g


def plug_(x, y, s=1, rot=0, cable=True):
    g = R(-18, -16, 36, 40, '#ffffff', 6) + R(-12, -32, 6, 18, '#c4cbd0', 2) + R(6, -32, 6, 18, '#c4cbd0', 2)
    if cable: g += St('M0,24 Q0,60 40,70', '#2f3437', 5)
    return G(g, f'translate({x},{y}) rotate({rot}) scale({s})')


def socket_(x, y, s=1):
    return G(R(-30, -30, 60, 60, '#ffffff', 8) + R(-30, -30, 60, 60, 'none', 8, 'stroke="#d9dcde" stroke-width="2"') + Ci(0, 0, 20, '#f2efe8') + R(-10, -6, 5, 14, '#5d6469', 1) + R(5, -6, 5, 14, '#5d6469', 1), f'translate({x},{y}) scale({s})')


def battery_(x, y, s=1, level=1.0, col='#5ba644'):
    g = R(-20, -44, 40, 88, '#2f3437', 6) + R(-8, -52, 16, 10, '#a7adb1', 2) + R(-14, 38 - 76 * level, 28, 76 * level, col, 3)
    return G(g, f'translate({x},{y}) scale({s})')


def broom_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 110, WOOD, 3) + Pa('M-24,0 L24,0 L34,50 L-34,50 Z', '#e0b050') + ''.join(L(-30 + k * 6, 10, -34 + k * 7, 50, '#c8963a', 1.5) for k in range(11)) + R(-26, -4, 52, 10, '#d9453a', 3), f'translate({x},{y}) rotate({rot}) scale({s})')


def mop_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 112, '#5aa1d4', 3) + R(-20, 0, 40, 10, '#5d6469', 3) + ''.join(St(f'M{-18+k*5},10 q{(k-3.5)*2},20 {(k-3.5)*4},36', '#f2efe8', 5) for k in range(8)), f'translate({x},{y}) rotate({rot}) scale({s})')


def bucket_(cx, base, w=70, h=60, col='#5aa1d4', water=True):
    g = Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w*.4},{base} L{cx-w*.4},{base} Z', col) + E(cx, base - h, w / 2, 8, shade(col, -.2))
    if water: g += E(cx, base - h + 2, w / 2 - 4, 5, '#9fd0ec')
    g += St(f'M{cx-w/2},{base-h} Q{cx},{base-h-40} {cx+w/2},{base-h}', '#5d6469', 3)
    return g


def washer(x, y, w=120, h=140, door_fill='#9fd0ec'):
    g = R(x, y, w, h, '#f2efe8', 8) + R(x, y, w, 26, '#e6e1d8', 6) + ''.join(Ci(x + w - 18 - k * 14, y + 13, 5, '#a7adb1') for k in range(2)) + R(x + 10, y + 8, 40, 10, '#7fe08a', 2)
    g += Ci(x + w / 2, y + 26 + (h - 26) / 2, w * .34, '#a7adb1') + Ci(x + w / 2, y + 26 + (h - 26) / 2, w * .28, door_fill) + Pa(f'M{x+w*.3},{y+90} Q{x+w*.5},{y+76} {x+w*.7},{y+90}', 'none', 'stroke="#ffffff" stroke-width="3" opacity=".7"')
    return g


def hammer_(x, y, s=1, rot=0):
    return G(R(-5, -10, 10, 100, WOOD, 4) + Pa('M-34,-26 L20,-26 L28,-18 L28,-4 L-34,-4 Q-40,-10 -38,-20 Z', '#5d6469') + Pa('M20,-26 L34,-34 L40,-28 L28,-18 Z', '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')


def screwdriver_(x, y, s=1, rot=0, col='#e2463b'):
    return G(R(-12, 0, 24, 56, col, 10) + ''.join(L(-6 + k * 4, 8, -6 + k * 4, 48, shade(col, -.2), 1.5) for k in range(4)) + R(-3, -60, 6, 62, '#c4cbd0', 2) + Pa('M-3,-60 L3,-60 L1,-68 L-1,-68 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')


def saw_(x, y, s=1, rot=0):
    return G(Pa('M0,0 L130,-16 L130,16 L0,30 Z', '#c4cbd0') + ''.join(Pa(f'M{k*10},{30-k*1.1} l5,6 l5,-7', '#c4cbd0') for k in range(13)) + R(-40, -4, 46, 36, '#c8903a', 10) + R(-30, 4, 26, 16, '#f1e8d4', 6), f'translate({x},{y}) rotate({rot}) scale({s})')


def ladder_(x1, y1, x2, y2, w=40, col='#c8903a', rungs=6):
    g = L(x1, y1, x2, y2, col, 7) + L(x1 + w, y1, x2 + w, y2, col, 7)
    return g + ''.join(L(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, x1 + (x2 - x1) * t + w, y1 + (y2 - y1) * t, col, 5) for t in [(k + .5) / rungs for k in range(rungs)])


def drill_(x, y, s=1):
    return G(R(-50, -20, 80, 36, '#f3c234', 10) + R(30, -10, 16, 16, '#2f3437', 3) + R(46, -4, 40, 4, '#a7adb1') + Pa('M-30,16 L-6,16 L-10,70 L-36,70 Z', '#2f3437') + R(-40, 64, 40, 18, '#2f3437', 4) + R(-6, 20, 10, 14, '#e2463b', 3), f'translate({x},{y}) scale({s})')


def pliers_(x, y, s=1, rot=0):
    return G(Pa('M0,0 L-14,-60 Q-4,-70 6,-60 Z', '#5d6469') + Pa('M0,0 L14,-60 Q4,-70 -6,-60 Z', '#a7adb1') + St('M-4,4 Q-26,50 -30,90', '#e2463b', 14) + St('M4,4 Q26,50 30,90', '#e2463b', 14) + Ci(0, 0, 7, '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')


def wrench_(x, y, s=1, rot=0):
    return G(R(-8, -10, 16, 120, '#a7adb1', 7) + Pa('M-22,-30 Q-28,-10 -8,-4 L8,-4 Q28,-10 22,-30 L12,-30 L12,-14 L-12,-14 L-12,-30 Z', '#a7adb1') + Ci(0, 104, 8, '#f1e8d4'), f'translate({x},{y}) rotate({rot}) scale({s})')


def glove(x, y, rot, col='#f3c234'):
    g = R(-22, 0, 44, 50, col, 8) + R(-24, 40, 48, 30, shade(col, -.1), 6) + ''.join(R(-22 + k * 11, -36 + abs(k - 1.5) * 6, 10, 40, col, 5) for k in range(4)) + G(R(-6, -14, 12, 34, col, 6), 'translate(-24,14) rotate(-40)')
    return G(g, f'translate({x},{y}) rotate({rot})')

GRASS = '#8cc06a'; SOIL = '#7a5236'; SOILL = '#9a6a46'

def paint_can(cx, base, w, h, col, open_=True):
    g = R(cx - w / 2, base - h, w, h, '#c4cbd0', 4) + R(cx - w / 2, base - h * .7, w, h * .45, '#ffffff', 2) + R(cx - w / 2 + 8, base - h * .62, w - 16, h * .3, col, 2)
    if open_: g += E(cx, base - h, w / 2, 8, '#a7adb1') + E(cx, base - h, w / 2 - 4, 6, col) + Pa(f'M{cx-w/2+6},{base-h} q4,20 8,0 q4,14 8,0', col)
    g += St(f'M{cx-w/2},{base-h+6} Q{cx},{base-h-36} {cx+w/2},{base-h+6}', '#5d6469', 3)
    return g


def paint_brush(x, y, s=1, rot=0, col='#3c7fc1'):
    return G(R(-5, 0, 10, 70, WOOD, 5) + R(-12, -16, 24, 20, '#c4cbd0', 2) + Pa('M-12,-16 L12,-16 L14,-50 Q0,-56 -14,-50 Z', '#e0c090') + Pa('M-14,-50 Q0,-56 14,-50 L13,-40 L-13,-40 Z', col), f'translate({x},{y}) rotate({rot}) scale({s})')


def roller_(x, y, s=1, rot=0, col='#5aa1d4'):
    return G(R(-40, -16, 80, 32, col, 14) + R(-40, -16, 80, 10, shade(col, .25), 8) + St('M40,0 L56,0 L56,40 L6,40 L6,60', '#a7adb1', 4) + R(0, 60, 12, 50, '#e2463b', 5), f'translate({x},{y}) rotate({rot}) scale({s})')


def potted(cx, base, w=40, h=34, col='#c0603a'):
    return Pa(f'M{cx-w/2},{base-h} L{cx+w/2},{base-h} L{cx+w*.38},{base} L{cx-w*.38},{base} Z', col) + R(cx - w / 2 - 3, base - h - 6, w + 6, 10, shade(col, -.1), 2)


def soil_ground(y=150, h=50):
    return R(0, y, 200, h, SOIL) + ''.join(Ci(10 + k * 23, y + 10 + (k % 3) * 12, 3, SOILL) for k in range(9))


def tulip_(x, y, s=1, col='#e2463b'):
    return St(f'M{x},{y} L{x},{y+60*s}', '#4a9a3a', 4 * s) + leaf(x, y + 50 * s, 30 * s, 8 * s, -70, '#5aaa3a') + Pa(f'M{x-14*s},{y-20*s} L{x-14*s},{y} Q{x},{y+10*s} {x+14*s},{y} L{x+14*s},{y-20*s} L{x+7*s},{y-10*s} L{x},{y-22*s} L{x-7*s},{y-10*s} Z', col)


def rose_(x, y, s=1, col='#d9283a'):
    g = St(f'M{x},{y} L{x},{y+70*s}', '#3c7a2c', 4 * s) + leaf(x, y + 30 * s, 22 * s, 9 * s, -20, '#4a8a3a') + leaf(x, y + 46 * s, 22 * s, 9 * s, -160, '#4a8a3a')
    g += Ci(x, y - 6 * s, 20 * s, col) + Pa(f'M{x-12*s},{y-10*s} Q{x},{y-26*s} {x+12*s},{y-10*s} Q{x},{y-2*s} {x-12*s},{y-10*s} Z', shade(col, -.2)) + St(f'M{x-6*s},{y-8*s} q6,-8 12,0', shade(col, .2), 2)
    g += Pa(f'M{x-18*s},{y} Q{x},{y+16*s} {x+18*s},{y} Q{x},{y+6*s} {x-18*s},{y} Z', shade(col, -.1))
    return g


def daisy(x, y, r, petal='#ffffff', center='#f3c234', n=10):
    return ''.join(E(x + r * .6 * math.cos(a), y + r * .6 * math.sin(a), r * .45, r * .18, petal, f'transform="rotate({math.degrees(a):.0f} {x+r*.6*math.cos(a):.1f} {y+r*.6*math.sin(a):.1f})"') for a in [k * 2 * math.pi / n for k in range(n)]) + Ci(x, y, r * .3, center)


def watering_can_(x, y, s=1, rot=0, col='#5ba644'):
    return G(Pa('M-30,-30 L30,-30 L34,30 L-34,30 Z', col) + St('M-26,-30 Q0,-60 26,-30', shade(col, -.2), 6) + Pa('M30,10 L70,-30 L76,-24 L36,20 Z', col) + E(76, -28, 10, 6, shade(col, -.2), 'transform="rotate(45 76 -28)"'), f'translate({x},{y}) rotate({rot}) scale({s})')


def spade_(x, y, s=1, rot=0):
    return G(R(-4, -100, 8, 100, WOOD, 3) + Pa('M-14,-112 L14,-112 L14,-100 L-14,-100 Z', '#2f3437') + St('M-14,-110 L14,-110', '#2f3437', 4) + Pa('M-22,0 L22,0 L20,50 Q0,62 -20,50 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')


def rake_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 120, WOOD, 3) + R(-36, 8, 72, 8, '#5d6469', 2) + ''.join(R(-34 + k * 8, 14, 4, 18, '#5d6469', 1) for k in range(9)), f'translate({x},{y}) rotate({rot}) scale({s})')


def hoe_(x, y, s=1, rot=0):
    return G(R(-3, -110, 6, 120, WOOD, 3) + Pa('M-2,6 L36,6 L40,30 L4,30 Z', '#5d6469'), f'translate({x},{y}) rotate({rot}) scale({s})')


def trowel_(x, y, s=1, rot=0):
    return G(R(-6, 0, 12, 44, '#5ba644', 5) + R(-2, -10, 4, 12, '#a7adb1') + Pa('M-16,-10 L16,-10 Q14,-50 0,-60 Q-14,-50 -16,-10 Z', '#a7adb1'), f'translate({x},{y}) rotate({rot}) scale({s})')


def shears_(x, y, s=1, rot=0, short=False):
    bl = 40 if short else 80
    return G(Pa(f'M0,0 L-8,{-bl} L4,{-bl+6} L6,0 Z', '#c4cbd0') + Pa(f'M0,0 L8,{-bl} L-4,{-bl+6} L-6,0 Z', '#a7adb1') + Ci(0, 0, 5, '#5d6469') + St('M-3,4 Q-20,30 -26,70', '#e2463b', 10) + St('M3,4 Q20,30 26,70', '#e2463b', 10), f'translate({x},{y}) rotate({rot}) scale({s})')


def mower(x, y, s=1):
    return G(R(-50, -30, 90, 40, '#e2463b', 10) + R(-40, -44, 50, 20, '#2f3437', 6) + wheel(-40, 12, 12) + wheel(30, 12, 12) + St('M30,-24 L80,-90 L100,-90', '#2f3437', 5) + R(-36, -36, 14, 6, '#ffffff', 2), f'translate({x},{y}) scale({s})')


def gglove(x, y, rot, col='#5ba644'):
    g = R(-22, 0, 44, 50, col, 8) + R(-24, 40, 48, 24, '#f3c234', 6) + ''.join(R(-22 + k * 11, -36 + abs(k - 1.5) * 6, 10, 40, col, 5) for k in range(4)) + G(R(-6, -14, 12, 34, col, 6), 'translate(-24,14) rotate(-40)') + ''.join(Ci(-12 + k * 8, 20, 2, shade(col, -.25)) for k in range(4))
    return G(g, f'translate({x},{y}) rotate({rot})')


def bench_(cx, base, w=120, col=WOOD):
    return ''.join(R(cx - w / 2, base - 44 + k * 10, w, 7, col, 2) for k in range(2)) + ''.join(R(cx - w / 2, base - 84 + k * 12, w, 8, col, 2) for k in range(3)) + R(cx - w / 2 + 8, base - 84, 6, 84, '#2f3437') + R(cx + w / 2 - 14, base - 84, 6, 84, '#2f3437')


def tree_(x, y, s=1):
    return tree(x, y, s)


def lantern(x, y, s=1):
    return G(L(0, -40, 0, -26, '#d9a33a', 2) + R(-14, -28, 28, 6, '#d9a33a', 2) + E(0, 0, 26, 24, '#e2302a') + ''.join(St(f'M{k*9},-22 Q{k*14},0 {k*9},22', '#c0201a', 1.5) for k in (-2, -1, 0, 1, 2)) + R(-14, 22, 28, 6, '#d9a33a', 2) + ''.join(L(-8 + j * 4, 28, -8 + j * 4, 44, '#d9a33a', 1.5) for j in range(5)), f'translate({x},{y}) scale({s})')

def lily(x, y, s):
    g = ''.join(G(Pa('M0,0 Q-14,-20 -6,-56 Q0,-62 6,-56 Q14,-20 0,0 Z', '#ffffff') + St('M0,-4 L0,-50', '#f2d0d8', 2), f'rotate({a})') for a in (-70, -35, 0, 35, 70, 180))
    g += ''.join(St(f'M0,0 L{14*math.cos(math.radians(-90+a))},{14*math.sin(math.radians(-90+a))-10}', '#5aaa3a', 1.5) + E(14 * math.cos(math.radians(-90 + a)), 14 * math.sin(math.radians(-90 + a)) - 12, 3, 5, '#d9641a') for a in (-30, 0, 30))
    return G(g, f'translate({x},{y}) scale({s})')

def orchid_f(x, y, s, col='#c86ab8'):
    return G(E(-14, -8, 14, 10, col) + E(14, -8, 14, 10, col) + E(-12, 10, 11, 9, col) + E(12, 10, 11, 9, col) + E(0, 2, 7, 9, '#f3c234') + Ci(0, 0, 3, '#d9453a'), f'translate({x},{y}) scale({s})')

def chrys(x, y, r, col='#f3c234'):
    g = ''
    for ring, rr in enumerate((r, r * .75, r * .5)):
        n = 20 - ring * 4
        g += ''.join(E(x + rr * .5 * math.cos(a), y + rr * .5 * math.sin(a), rr * .5, rr * .09 + 1, shade(col, -.08 * ring), f'transform="rotate({math.degrees(a):.0f} {x+rr*.5*math.cos(a):.1f} {y+rr*.5*math.sin(a):.1f})"') for a in [k * 2 * math.pi / n + ring * .2 for k in range(n)])
    return g + Ci(x, y, r * .14, shade(col, -.25))
