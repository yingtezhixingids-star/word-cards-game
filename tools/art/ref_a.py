from kit4 import *

NIGHT = '#24304f'
def moon(x, y, r, col='#f6efe0'):
    return Pa(f'M{x},{y-r} A{r},{r} 0 1,0 {x+r},{y+r*.3} A{r*.8},{r*.8} 0 1,1 {x},{y-r} Z', col)
def sun(x, y, r, col='#f3c234', rays=True):
    g = Ci(x, y, r, col)
    if rays: g += ''.join(L(x + (r + 6) * math.cos(a), y + (r + 6) * math.sin(a), x + (r + 16) * math.cos(a), y + (r + 16) * math.sin(a), col, 4) for a in [k * .785 for k in range(8)])
    return g
def stars(pts, s=4):
    return ''.join(star(x, y, s, '#ffffff') for x, y in pts)
def hourglass(x, y, s=1):
    return G(Pa('M-20,-34 L20,-34 L4,0 L20,34 L-20,34 L-4,0 Z', '#dff1fb', 'stroke="#8a5a35" stroke-width="3"') + Pa('M-12,-26 L12,-26 L2,-6 L-2,-6 Z', '#e8c060') + Pa('M-14,30 L14,30 L0,16 Z', '#e8c060') + R(-24, -40, 48, 8, '#8a5a35', 3) + R(-24, 32, 48, 8, '#8a5a35', 3), f'translate({x},{y}) scale({s})')
def wedge_clock(cx, cy, r, a0, a1, col='#5aa1d4', hm=(12, 0)):
    """shade angle range in minutes (0-60)"""
    t0 = math.radians(a0 * 6 - 90); t1 = math.radians(a1 * 6 - 90)
    large = 1 if (a1 - a0) > 30 else 0
    g = Ci(cx, cy, r, '#ffffff', 'stroke="#2f3437" stroke-width="6"')
    if a1 - a0 >= 60: g += Ci(cx, cy, r - 4, col)
    else: g += Pa(f'M{cx},{cy} L{cx+(r-4)*math.cos(t0)},{cy+(r-4)*math.sin(t0)} A{r-4},{r-4} 0 {large},1 {cx+(r-4)*math.cos(t1)},{cy+(r-4)*math.sin(t1)} Z', col)
    g += ''.join(L(cx + (r - 6) * math.cos(k * math.pi / 6), cy + (r - 6) * math.sin(k * math.pi / 6), cx + (r - 14) * math.cos(k * math.pi / 6), cy + (r - 14) * math.sin(k * math.pi / 6), '#2f3437', 3) for k in range(12))
    h, m = hm
    ha = math.radians((h % 12 + m / 60) * 30 - 90); ma = math.radians(m * 6 - 90)
    g += L(cx, cy, cx + r * .45 * math.cos(ha), cy + r * .45 * math.sin(ha), '#2f3437', 6) + L(cx, cy, cx + r * .72 * math.cos(ma), cy + r * .72 * math.sin(ma), '#2f3437', 4) + Ci(cx, cy, 5, '#e2463b')
    return g
def week_strip(hl, col='#e2463b', y=70):
    days = '一二三四五六日'
    g = ''
    for k in range(7):
        x = 12 + k * 26
        on = k in (hl if isinstance(hl, (list, tuple)) else [hl])
        g += R(x, y, 24, 60, col if on else '#ffffff', 4, '' if on else 'stroke="#c4cbd0" stroke-width="2"') + T(x + 12, y + 38, days[k], 16, '#ffffff' if on else '#5d6469', 900)
    return g
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
def punct(ch, size=150, y=150):
    return Ci(100, 100, 80, '#f6efe0') + T(100, y, ch, size, '#3c7fc1', 900, family='Georgia, serif')

def day_pos(x, y, w, h, k):
    cw, chh = (w - 16) / 7, (h * .78 - 12) / 5
    return x + 8 + (k % 7) * cw + cw / 2, y + h * .22 + 6 + (k // 7) * chh + chh / 2
def pin_(x, y, col='#5d6469', s=.6):
    return G(Pa('M0,0 C-14,-20 -16,-28 -16,-34 A16,16 0 1,1 16,-34 C16,-28 14,-20 0,0 Z', col) + Ci(0, -34, 6, '#ffffff'), f'translate({x},{y}) scale({s})')
def daycal(hl, today=17, col='#e2463b'):
    x, y, w, h = 30, 30, 140, 130
    g = calendar_(x, y, w, h, None, col)
    tx, ty = day_pos(x, y, w, h, today); hx, hy = day_pos(x, y, w, h, hl)
    g += Ci(hx, hy, 9, col)
    if hl != today: g += pin_(tx, ty + 4, '#5d6469')
    else: g += pin_(tx, ty + 4, col, .8)
    return g

# ================= 时间 =================
S_('time', clock(80, 100, 60, (10, 10)) + hourglass(160, 140, .9))
S_('hour', wedge_clock(100, 100, 74, 0, 60, '#cfe8f6', (3, 0)) + St('M100,14 A86,86 0 1,1 99,14', '#5ba644', 5) + Pa('M92,8 L104,14 L92,20 Z', '#5ba644'))
S_('minute', wedge_clock(100, 100, 74, 0, 1, '#e2463b', (10, 0)) + Pa('M100,100 L100,26 A74,74 0 0,1 108,26 Z', '#e2463b') + G(Ci(0, 0, 22, '#ffffff', 'stroke="#2f3437" stroke-width="4"') + L(0, 0, 0, -14, '#e2463b', 3) + R(-5, -30, 10, 8, '#2f3437', 2), 'translate(164,164)'))
S_('o-clock', clock(100, 100, 74, (3, 0)))
S_('morning', R(0, 0, 200, 200, '#ffe2b8') + R(0, 130, 200, 70, '#8cc06a') + sun(100, 130, 30, '#f3a234') + R(0, 130, 200, 70, '#8cc06a') + G(E(0, 0, 18, 14, '#ffffff') + Ci(14, -14, 8, '#ffffff') + Pa('M10,-24 l4,-8 l4,8 Z', '#e2463b') + Pa('M22,-14 l8,2 l-8,2 Z', '#f3c234') + Pa('M-16,-6 Q-30,-24 -24,0 Z', '#3c6a3a') + L(-4, 12, -4, 26, '#f3c234', 3) + L(4, 12, 4, 26, '#f3c234', 3), 'translate(150,150)') + clock(36, 36, 20, (7, 0)), False)
S_('afternoon', R(0, 0, 200, 200, '#bfe6fa') + R(0, 150, 200, 50, '#8cc06a') + sun(140, 60, 24) + tree(50, 150, .9) + cup(110, 150, 34, 30, '#ffffff', '#c98a3a') + clock(36, 36, 20, (3, 0)), False)
S_('evening', R(0, 0, 200, 200, '#f08a5a') + R(0, 0, 200, 90, '#c0507a') + Ci(100, 140, 34, '#f3c234') + R(0, 140, 200, 60, '#5a3a5a') + house(50, 170, 60, 44, '#7a5a6a', '#4a2a3a', '#3a2a2a', '#f3e070') + house(150, 175, 50, 36, '#7a5a6a', '#4a2a3a', '#3a2a2a', '#f3e070'), False)
S_('night', R(0, 0, 200, 200, NIGHT) + moon(130, 50, 26) + stars([(30, 40), (70, 70), (170, 110), (40, 100), (100, 30)]) + R(0, 150, 200, 50, '#1a2238') + house(70, 170, 60, 44, '#3a4560', '#2a3450', '#1a2238', '#f3e070'), False)
S_('now', R(10, 100, 180, 8, '#a7adb1', 4) + ''.join(Ci(20 + k * 32, 104, 6, '#a7adb1') for k in range(6)) + Ci(100, 104, 12, '#e2463b') + Pa('M86,60 L114,60 L100,84 Z', '#e2463b') + clock(100, 34, 24, (10, 10)) + T(30, 150, '←', 0, '#000') + arrow(70, 150, 20, 150, '#c4cbd0', 4) + arrow(130, 150, 180, 150, '#c4cbd0', 4))
S_('early', R(0, 0, 200, 200, '#3a4a7a') + R(0, 130, 200, 70, '#5a6a8a') + Pa('M0,130 A100,30 0 0,1 200,130 Z', '#f3a234', 'opacity=".5"') + Ci(100, 134, 20, '#f3c234') + R(0, 134, 200, 66, '#4a5a7a') + G(clock(0, 0, 30, (5, 0)) + Ci(-24, -26, 10, '#e2463b') + Ci(24, -26, 10, '#e2463b') + L(-18, 26, -26, 36, '#2f3437', 4) + L(18, 26, 26, 36, '#2f3437', 4), 'translate(100,74)') + stars([(30, 30), (170, 40), (150, 20)]), False)
S_('late', R(0, 0, 200, 200, SKY) + R(0, 160, 200, 40, ROAD) + G(R(-60, -56, 120, 56, '#f3c234', 8) + ''.join(R(-50 + k * 26, -48, 20, 20, '#9fd0ec', 2) for k in range(4)) + wheel(-36, 0, 12) + wheel(36, 0, 12), 'translate(150,160)') + St('M80,150 l-10,0 M80,140 l-14,0', '#a7adb1', 3) + W(50, 194, .7, '#3c7fc1', '#3b4a5a', legs='run', arms='wave', mood='o') + clock(40, 40, 20, (9, 20)) + drop(70, 66, 5), False)
S_('noon', R(0, 0, 200, 200, '#bfe6fa') + R(0, 160, 200, 40, '#8cc06a') + sun(100, 50, 28) + clock(100, 130, 30, (12, 0)), False)
S_('midnight', R(0, 0, 200, 200, NIGHT) + moon(150, 40, 22) + stars([(30, 30), (70, 20), (40, 170), (170, 160)]) + G(clock(0, 0, 50, (12, 0)), 'translate(96,110)'), False)
S_('half-past', wedge_clock(100, 100, 74, 0, 30, '#9fd0ec', (3, 30)))
S_('quarter', wedge_clock(100, 100, 74, 0, 15, '#f3c234', (3, 15)))
S_('second', G(Ci(0, 0, 66, '#ffffff', 'stroke="#2f3437" stroke-width="7"') + ''.join(L(56 * math.cos(k * math.pi / 30), 56 * math.sin(k * math.pi / 30), (52 if k % 5 else 46) * math.cos(k * math.pi / 30), (52 if k % 5 else 46) * math.sin(k * math.pi / 30), '#2f3437', 1.5 if k % 5 else 3) for k in range(60)) + L(0, 0, 40, -30, '#e2463b', 3) + Ci(0, 0, 5, '#e2463b') + R(-8, -84, 16, 14, '#2f3437', 3) + R(-14, -92, 28, 10, '#5d6469', 4), 'translate(100,110)'))

# ================= 日历 =================
S_('today', daycal(17))
S_('tomorrow', daycal(18) + arrow(70, 180, 140, 180, '#5ba644', 6))
S_('yesterday', daycal(16) + arrow(140, 180, 70, 180, '#3c7fc1', 6))
S_('day', R(0, 0, 200, 200, SKY) + sun(100, 70, 34) + R(0, 140, 200, 60, '#8cc06a') + R(70, 120, 60, 70, '#ffffff', 4) + R(70, 120, 60, 18, '#e2463b', 4) + T(100, 178, '1', 36, '#2f3437', 900), False)
S_('week', week_strip([0, 1, 2, 3, 4, 5, 6], '#3c7fc1') + St('M12,150 L188,150', '#3c7fc1', 4) + St('M12,142 L12,158 M188,142 L188,158', '#3c7fc1', 4) + T(100, 50, '7', 30, '#3c7fc1', 900))
S_('month', calendar_(20, 30, 160, 150))
S_('year', ''.join(calendar_(14 + (k % 4) * 46, 20 + (k // 4) * 58, 40, 46, None, ['#3c7fc1', '#5ba644', '#f3c234', '#e2463b'][k // 3]) for k in range(12)))
S_('weekend', week_strip([5, 6], '#5ba644', 30) + R(0, 120, 200, 80, '#f0d890', 0, 'opacity="0"') + G(Pa('M-40,10 L40,10 L30,-10 L-50,-20 Z', '#3c7fc1') + L(-30, 10, -36, 30, '#5d6469', 3) + L(30, 10, 36, 30, '#5d6469', 3), 'translate(80,160)') + umbrella_ if False else week_strip([5, 6], '#5ba644', 30) + G(Pa('M-40,10 L40,10 L30,-10 L-50,-20 Z', '#3c7fc1') + L(-30, 10, -36, 30, '#5d6469', 3) + L(30, 10, 36, 30, '#5d6469', 3), 'translate(90,150)') + cup(160, 166, 22, 26, '#ffffff', '#f08a24') + sun(170, 116, 10))
S_('monday', week_strip(0) + T(25, 160, '▲', 20, '#e2463b', 900))
S_('wednesday', week_strip(2) + T(77, 160, '▲', 20, '#e2463b', 900))
S_('friday', week_strip(4) + T(129, 160, '▲', 20, '#e2463b', 900))
S_('sunday', week_strip(6) + T(181, 160, '▲', 20, '#e2463b', 900))
S_('spring', R(0, 0, 200, 200, '#dff1fb') + R(0, 150, 200, 50, '#9ad070') + G(R(-6, -60, 12, 60, '#8a5a35') + ''.join(Ci(dx, dy, 18, '#f6c8dc') for dx, dy in [(-24, -70), (0, -86), (24, -70), (-12, -56), (14, -56)]) + ''.join(flower(dx, dy, .6, '#ffffff', '#ef8fa4') for dx, dy in [(-24, -74), (6, -88), (24, -66)]), 'translate(70,160)') + tulip_(150, 170, .8) + tulip_(170, 176, .6, '#f3c234') + G(Pa('M0,0 Q-10,-10 -16,0 Q-10,6 0,0 Q10,-10 16,0 Q10,6 0,0 Z', '#f08a24'), 'translate(150,60)'), False)
S_('summer', R(0, 0, 200, 200, '#9fd8f6') + R(0, 110, 200, 40, '#3c9ad4') + R(0, 150, 200, 50, '#f0d890') + sun(160, 40, 22) + R(68, 90, 4, 80, '#a7adb1') + Pa('M20,96 Q70,40 120,96 Z', '#e2463b') + Pa('M50,96 Q70,56 90,96 Z', '#ffffff') + G(Pa('M-6,-30 L6,-30 L4,10 L-4,10 Z', '#e2463b') + Ci(0, -36, 10, '#f3e070'), 'translate(150,170)'), False)
S_('autumn', R(0, 0, 200, 200, '#fbe8cc') + G(R(-8, -80, 16, 80, '#8a5a35') + Ci(0, -100, 44, '#e08a24') + Ci(-30, -80, 30, '#d9532a') + Ci(30, -80, 30, '#f3a234'), 'translate(100,170)') + ''.join(leaf(x, y, 14, 7, r_, c) for x, y, r_, c in [(30, 140, 30, '#d9532a'), (160, 160, -40, '#f3a234'), (60, 180, 80, '#e08a24'), (150, 120, 10, '#d9532a')]) + R(0, 170, 200, 30, '#c8903a'), False)
S_('winter', R(0, 0, 200, 200, '#cfe2f0') + R(0, 150, 200, 50, '#ffffff') + Ci(100, 140, 36, '#ffffff', 'stroke="#c4d4e0" stroke-width="2"') + Ci(100, 84, 26, '#ffffff', 'stroke="#c4d4e0" stroke-width="2"') + Ci(92, 80, 3, '#2f3437') + Ci(108, 80, 3, '#2f3437') + Pa('M100,86 L120,90 L100,92 Z', '#f08a24') + R(76, 100, 48, 10, '#e2463b', 4) + R(110, 100, 10, 26, '#e2463b', 3) + R(84, 50, 32, 14, '#2f3437') + R(78, 62, 44, 5, '#2f3437') + ''.join(Ci(x, y, 3, '#ffffff') for x, y in [(20, 30), (60, 50), (150, 30), (180, 80), (30, 110), (170, 120)]), False)

# ================= 数字 =================
S_('number', T(50, 110, '1', 70, '#e2463b', 900) + T(100, 110, '2', 70, '#3c7fc1', 900) + T(150, 110, '3', 70, '#5ba644', 900) + T(75, 175, '4', 50, '#f3c234', 900) + T(125, 175, '5', 50, '#7a4fa0', 900))
S_('count', ''.join(apple(40 + k * 32, 60, .55) + T(40 + k * 32, 100, str(k + 1), 18, '#3c7fc1', 900) for k in range(5)) + hand(100, 176, .7, 0, spread=True))
S_('zero', big_num('0', '#3c7fc1', 130, 150) + plate(100, 0, 0))
S_('ten', big_num('10', '#e2463b', 70, 90) + dots(10, 5, 8, 40, 130, 30))
S_('twelve', big_num('12', '#5ba644', 70, 90) + dots(12, 6, 7, 28, 130, 28, '#5ba644'))
S_('fifteen', big_num('15', '#f08a24', 90, 130))
S_('fifty', big_num('50', '#7a4fa0', 90, 130))
S_('hundred', big_num('100', '#3c7fc1', 80, 130))
S_('thousand', big_num('1,000', '#e2463b', 54, 120))
S_('ten-thousand', big_num('10,000', '#5ba644', 46, 120))
S_('million', big_num('1,000,000', '#7a4fa0', 32, 116))
S_('first', podium3(1) + medal_(100, 60, .55))
S_('third', podium3(3) + medal_(160, 104, .45, '#c8703a', '#3c7fc1'))
S_('last', R(0, 180, 200, 20, WALK) + ''.join(fig(26 + k * 36, 186, ['man', 'woman', 'oldman', 'youngwoman', 'boy'][k], s=.55) for k in range(5)) + Ci(170, 70, 0, '#000') + Pa('M160,40 L180,40 L170,56 Z', '#e2463b') + R(140, 20, 60, 140, 'none', 10, 'stroke="#e2463b" stroke-width="3" stroke-dasharray="6 4"'))
S_('dozen', R(20, 80, 160, 80, '#c8b090', 8) + ''.join(egg(38 + (k % 6) * 25, 104 + (k // 6) * 32, .8) for k in range(12)) + R(20, 140, 160, 20, '#b8a080', 6))
S_('phone-number', phone_(100, 100, 90, 166, R(66, 32, 68, 20, '#ffffff', 3) + T(100, 47, '138…', 13, '#2f3437', 900) + ''.join(Ci(74 + (k % 3) * 26, 70 + (k // 3) * 24, 9, '#ffffff') + T(74 + (k % 3) * 26, 75 + (k // 3) * 24, '123456789*0#'[k], 12, '#2f3437', 900) for k in range(12))))

# ================= 量 =================
S_('heavy', R(0, 0, 200, 200, '#e8eef2') + R(0, 176, 200, 24, '#c4cbd0') + W(100, 196, .95, '#e2463b', '#3b4a5a', arms='up', mood='o') + R(30, 26, 140, 8, '#5d6469', 3) + R(20, 10, 22, 40, '#2f3437', 5) + R(158, 10, 22, 40, '#2f3437', 5) + drop(140, 70, 6) + drop(56, 80, 5), False)
S_('light-measures', G(R(-4, -40, 8, 60, '#8a9196') + L(-60, -40, 60, -40, '#8a9196', 5) + E(-50, 0, 30, 6, '#c4cbd0') + E(54, -10, 30, 6, '#c4cbd0') + L(-50, -40, -50, 0, '#8a9196', 1) + L(54, -40, 54, -10, '#8a9196', 1) + R(-30, 20, 60, 8, '#8a9196', 3), 'translate(100,120)') + G(Pa('M0,0 Q-20,-30 6,-60 Q26,-30 0,0 Z', '#ffffff', 'stroke="#c4cbd0" stroke-width="2"') + L(0, 0, 4, -50, '#c4cbd0', 1.5), 'translate(154,104) rotate(60)') + weight_(50, 116, 34, '#5d6469'))
S_('long', G(Pa('M0,0 Q40,-30 80,0 T160,0', 'none', 'stroke="#5ba644" stroke-width="18" stroke-linecap="round"') + Ci(166, -4, 12, '#5ba644') + Ci(170, -8, 3, '#2f3437') + St('M178,-4 l8,0 l4,-4 M186,-4 l4,4', '#e2463b', 2), 'translate(10,90)') + arrow(30, 150, 10, 150, '#3c7fc1', 4) + arrow(170, 150, 190, 150, '#3c7fc1', 4) + L(20, 150, 180, 150, '#3c7fc1', 4))
S_('kilo', weight_(100, 170, 120, '#5d6469', '1 kg'))
S_('gram', kitchen_scale(100, 170, 1.4, '5 g') + Ci(100, 90, 0, '#000') + G(R(-10, -10, 20, 20, '#e8c060', 2), 'translate(100,92) scale(.8)'))
S_('half-a-kilo', kitchen_scale(100, 180, 1.3, '0.5 kg') + apple(80, 92, .7) + apple(112, 94, .7) + apple(96, 74, .7))
S_('pound', weight_(100, 170, 120, '#8a9196', '1 lb'))
S_('meter-measures', G(R(-40, -40, 80, 80, '#f3c234', 16) + Ci(0, 0, 24, '#d9a020') + Ci(0, 0, 10, '#f3c234'), 'translate(50,100)') + R(86, 84, 104, 30, '#f3e070', 2) + ''.join(L(90 + k * 10, 84, 90 + k * 10, 84 + (14 if k % 5 == 0 else 8), '#2f3437', 1.5) for k in range(10)) + T(160, 108, '1 m', 14, '#2f3437', 900))
S_('centimeter', G(R(-90, -30, 180, 60, '#f3e070', 4) + ''.join(L(-80 + k * 8, -30, -80 + k * 8, -30 + (24 if k % 10 == 0 else (16 if k % 5 == 0 else 10)), '#2f3437', 2 if k % 10 == 0 else 1.2) for k in range(21)) + T(-80, 20, '0', 14, '#2f3437', 900) + T(0, 20, '1', 14, '#2f3437', 900) + T(80, 20, '2', 14, '#2f3437', 900) + T(60, 20, 'cm', 0, '#fff'), 'translate(100,100)') + St('M20,150 L100,150', '#e2463b', 4) + St('M20,144 L20,156 M100,144 L100,156', '#e2463b', 4))
S_('kilometer', road_sign('1 km', '#5ba644'), False)
S_('mile', road_sign('1 mi', '#3c7fc1'), False)
S_('liter', bottle_shape(60, 30, 80, 150, '#9fd0ec', .3) + R(84, 18, 32, 18, '#3c7fc1', 4) + R(64, 100, 72, 40, '#ffffff', 4) + T(100, 128, '1 L', 22, '#3c7fc1', 900))
S_('inch', G(R(-90, -30, 180, 60, '#e8c890', 4) + ''.join(L(-80 + k * 10, -30, -80 + k * 10, -30 + (24 if k % 8 == 0 else (16 if k % 4 == 0 else 9)), '#2f3437', 1.5) for k in range(17)) + T(-80, 20, '0', 14, '#2f3437', 900) + T(0, 20, '1', 14, '#2f3437', 900) + T(80, 20, '2', 14, '#2f3437', 900), 'translate(100,100)') + St('M20,150 L100,150', '#e2463b', 4) + T(60, 176, 'in', 18, '#e2463b', 900))
S_('height', R(0, 0, 200, 200, '#f2ead8') + R(110, 10, 30, 180, '#f3e070', 2) + ''.join(L(110, 10 + k * 15, 110 + (16 if k % 2 == 0 else 8), 10 + k * 15, '#2f3437', 2) for k in range(12)) + fig(70, 190, 'boy', s=1.4) + L(56, 50, 130, 50, '#e2463b', 3) + R(128, 44, 20, 12, '#e2463b', 2), False)
S_('length', fish_shape(100, 100, 120, '#5aa1d4') + L(30, 150, 170, 150, '#e2463b', 3) + St('M30,140 L30,160 M170,140 L170,160', '#e2463b', 3) + Pa('M30,150 l10,-6 l0,12 Z', '#e2463b') + Pa('M170,150 l-10,-6 l0,12 Z', '#e2463b'))
S_('scale', kitchen_scale(100, 170, 1.3, '') + G(Ci(0, 0, 30, '#ffffff', 'stroke="#2f3437" stroke-width="4"') + L(0, 0, 16, -18, '#e2463b', 3) + ''.join(L(24 * math.cos(a), 24 * math.sin(a), 28 * math.cos(a), 28 * math.sin(a), '#2f3437', 2) for a in [math.pi + k * .4 for k in range(9)]), 'translate(100,90)'))

# ================= 书写 =================
S_('write', doc_(30, 30, 120, 140, 0, '#ffffff', False) + St('M44,70 q8,-14 16,0 t16,0 t16,0 t16,0', '#3c7fc1', 3) + St('M44,100 q8,-14 16,0 t16,0 t16,0', '#3c7fc1', 3) + pen_(130, 120, .7, -50) + hand_(150, 140, .8, -50))
S_('name', G(R(-80, -50, 160, 100, '#ffffff', 10, 'stroke="#e2463b" stroke-width="5"') + R(-80, -50, 160, 34, '#e2463b', 10) + R(-80, -26, 160, 10, '#e2463b') + T(0, 30, '李明', 34, '#2f3437', 900), 'translate(100,100)'))
S_('word', ''.join(R(20 + k * 42, 70, 38, 44, '#f3e0b0', 4) + R(20 + k * 42, 108, 38, 6, '#d9b880', 2) + T(39 + k * 42, 102, 'BOOK'[k], 26, '#2f3437', 900) for k in range(4)) + book_(100, 160, .4, '#3c7fc1', 90))
S_('spell', ''.join(R(14 + k * 46, 80, 40, 46, ['#e2463b', '#3c7fc1', '#5ba644', '#f3c234'][k], 6) + T(34 + k * 46, 114, 'C-A-T'.replace('-', '')[k] if k < 3 else '', 28, '#ffffff', 900) for k in range(3)) + T(160, 114, '?', 0, '#fff') + G(E(0, 0, 26, 18, '#f08a24') + Ci(22, -14, 12, '#f08a24') + Pa('M16,-24 l4,-10 l6,10 Z', '#f08a24') + Pa('M28,-24 l4,-10 l4,10 Z', '#f08a24') + Ci(26, -14, 2, '#2f3437'), 'translate(160,160)') + ''.join(Ci(57 + k * 46, 103, 3, '#5d6469') for k in range(2)))
S_('sentence', R(10, 70, 180, 60, '#ffffff', 6) + T(20, 110, 'I like tea.', 30, '#2f3437', 800, 'start') + R(20, 116, 26, 4, '#e2463b') + Ci(150, 108, 6, '#e2463b', 'opacity="0"') + St('M20,140 L176,140', '#3c7fc1', 3))
S_('alphabet', ''.join(T(25 + (k % 6) * 30, 44 + (k // 6) * 32, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[k], 24, ['#e2463b', '#3c7fc1', '#5ba644', '#f08a24', '#7a4fa0'][k % 5], 900) for k in range(26)) + T(170, 202, '', 0))
S_('first-name', id_card(0))
S_('surname', id_card(1))
S_('signature', R(20, 40, 160, 120, '#ffffff', 4) + ''.join(R(36, 56 + k * 12, 128 - (k % 2) * 30, 4, '#c4cbd0', 2) for k in range(3)) + L(40, 136, 160, 136, '#2f3437', 2) + St('M48,130 q6,-30 14,-6 q6,16 14,-8 q10,-20 12,4 q4,14 14,-4 q8,-10 14,6 q6,8 22,-6', '#2f4a8a', 3) + pen_(150, 160, .5, -40))
S_('fill-in', R(30, 20, 140, 160, '#ffffff', 4) + ''.join(R(44, 44 + k * 32, 30, 5, '#5d6469', 2) + R(80, 36 + k * 32, 76, 18, '#ffffff', 3, 'stroke="#a7adb1" stroke-width="2"') for k in range(4)) + St('M86,112 q6,-8 12,0 t12,0 t12,0', '#3c7fc1', 2.5) + pen_(150, 118, .5, -40) + R(80, 132, 76, 18, '#f3e070', 3, 'opacity=".5"'))
S_('date-of-birth', G(R(-50, -20, 100, 50, '#ef8fa4', 6) + R(-50, -20, 100, 12, '#ffffff', 6) + ''.join(R(-30 + k * 26, -40, 6, 22, ['#3c7fc1', '#f3c234', '#5ba644'][k], 2) + E(-27 + k * 26, -46, 4, 7, '#f08a24') for k in range(3)) + R(-60, 30, 120, 8, '#e6ecef', 4), 'translate(70,140)') + calendar_(120, 30, 70, 70, 9, '#e2463b'))
S_('capital-letter', T(70, 150, 'A', 130, '#e2463b', 900) + T(160, 150, 'a', 60, '#a7adb1', 900) + St('M18,165 L130,165', '#e2463b', 4))
S_('handwriting', R(30, 20, 140, 160, '#fbf8f0', 4) + ''.join(L(40, 50 + k * 24, 160, 50 + k * 24, '#cfe8f6', 2) for k in range(6)) + ''.join(St(f'M44,{46+k*24} ' + ' '.join(f'q4,-{10+(j%3)*3} 8,0 q2,6 6,0' for j in range(7 - k % 3)), '#2f4a8a', 2.2) for k in range(5)) + L(56, 20, 56, 180, '#ef8fa4', 1.5))
S_('comma', punct(',', 200, 120))
S_('question-mark', punct('?', 150, 150))
S_('full-stop', punct('', 0) + Ci(100, 110, 26, '#3c7fc1') + T(60, 120, 'Hi', 40, '#a7adb1', 900, 'end'))

dump()
