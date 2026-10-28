import math
from kit5 import *

def _star5(cx, cy, r, col, rot=0):
    pts = []
    for k in range(10):
        a = math.radians(-90 + rot + k * 36)
        rr = r if k % 2 == 0 else r * .4
        pts.append(f'{cx+rr*math.cos(a):.2f},{cy+rr*math.sin(a):.2f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
def hstripes(cols, w=150, h=100, weights=None):
    weights = weights or [1] * len(cols)
    tot = sum(weights); y = 0; g = ''
    for c, wt in zip(cols, weights):
        hh = h * wt / tot; g += R(0, y, w, hh + .5, c); y += hh
    return g
def vstripes(cols, w=150, h=100, weights=None):
    weights = weights or [1] * len(cols)
    tot = sum(weights); x = 0; g = ''
    for c, wt in zip(cols, weights):
        ww = w * wt / tot; g += R(x, 0, ww + .5, h, c); x += ww
    return g
def nordic(bg, cross, inner=None, w=150, h=100):
    g = R(0, 0, w, h, bg)
    cx = h * .45
    if inner:
        g += R(cx - 13, 0, 26, h, cross) + R(0, h / 2 - 13, w, 26, cross)
        g += R(cx - 7, 0, 14, h, inner) + R(0, h / 2 - 7, w, 14, inner)
    else:
        g += R(cx - 9, 0, 18, h, cross) + R(0, h / 2 - 9, w, 18, cross)
    return g
def union_jack(w=150, h=100):
    g = R(0, 0, w, h, '#1f3a8a')
    g += L(0, 0, w, h, '#ffffff', h * .2) + L(w, 0, 0, h, '#ffffff', h * .2)
    g += L(0, 0, w, h, '#c8102e', h * .066) + L(w, 0, 0, h, '#c8102e', h * .066)
    g += R(w / 2 - h * .167, 0, h * .333, h, '#ffffff') + R(0, h / 2 - h * .167, w, h * .333, '#ffffff')
    g += R(w / 2 - h * .1, 0, h * .2, h, '#c8102e') + R(0, h / 2 - h * .1, w, h * .2, '#c8102e')
    return g
def flag_svg(code):
    W_, H_ = 150, 100
    F = {
    'china': lambda: R(0, 0, W_, H_, '#de2910') + _star5(25, 25, 15, '#ffde00') + ''.join(_star5(x, y, 5, '#ffde00', r) for x, y, r in [(50, 10, 20), (60, 20, 45), (60, 33, 0), (50, 43, 20)]),
    'america': lambda: ''.join(R(0, k * H_ / 13, W_, H_ / 13 + .5, '#b22234' if k % 2 == 0 else '#ffffff') for k in range(13)) + R(0, 0, 60, H_ * 7 / 13, '#3c3b6e') + ''.join(Ci(6 + (k % 6) * 10 + (k // 6 % 2) * 5, 5 + (k // 6) * 6.5, 1.6, '#ffffff') for k in range(48)),
    'canada': lambda: R(0, 0, W_, H_, '#ffffff') + R(0, 0, 37.5, H_, '#d52b1e') + R(112.5, 0, 37.5, H_, '#d52b1e') + Pa('M75,18 L80,30 L88,26 L85,44 L96,34 L99,40 L108,38 L104,50 L110,54 L92,66 L94,72 L77,70 L77,86 L73,86 L73,70 L56,72 L58,66 L40,54 L46,50 L42,38 L51,40 L54,34 L65,44 L62,26 L70,30 Z', '#d52b1e'),
    'uk': lambda: union_jack(),
    'australia': lambda: R(0, 0, W_, H_, '#00247d') + G(union_jack(), 'scale(.5)') + _star5(37, 76, 12, '#ffffff') + ''.join(_star5(x, y, r_, '#ffffff') for x, y, r_ in [(112, 22, 7), (96, 48, 7), (128, 42, 7), (112, 82, 7), (120, 58, 4)]),
    'japan': lambda: R(0, 0, W_, H_, '#ffffff') + Ci(75, 50, 30, '#bc002d'),
    'korea': lambda: R(0, 0, W_, H_, '#ffffff') + Ci(75, 50, 25, '#cd2e3a') + Pa('M50,50 A25,25 0 0,0 100,50 A12.5,12.5 0 0,0 75,50 A12.5,12.5 0 0,1 50,50 Z', '#0047a0') + ''.join(G(''.join(R(-12, -9 + j * 7, 24, 4, '#000000') for j in range(3)), f'translate({x},{y}) rotate({a})') for x, y, a in [(28, 22, -56), (122, 78, -56), (122, 22, 56), (28, 78, 56)]),
    'france': lambda: vstripes(['#0055a4', '#ffffff', '#ef4135']),
    'germany': lambda: hstripes(['#000000', '#dd0000', '#ffce00']),
    'italy': lambda: vstripes(['#009246', '#ffffff', '#ce2b37']),
    'spain': lambda: hstripes(['#aa151b', '#f1bf00', '#aa151b'], weights=[1, 2, 1]) + R(30, 36, 18, 26, '#aa151b', 3, 'opacity=".7"'),
    'russia': lambda: hstripes(['#ffffff', '#0039a6', '#d52b1e']),
    'india': lambda: hstripes(['#ff9933', '#ffffff', '#138808']) + Ci(75, 50, 13, 'none', 'stroke="#000080" stroke-width="2"') + ''.join(L(75, 50, 75 + 12 * math.cos(k * math.pi / 12), 50 + 12 * math.sin(k * math.pi / 12), '#000080', .8) for k in range(24)),
    'thailand': lambda: hstripes(['#a51931', '#f4f5f8', '#2d2a4a', '#f4f5f8', '#a51931'], weights=[1, 1, 2, 1, 1]),
    'singapore': lambda: hstripes(['#ef3340', '#ffffff']) + Ci(28, 25, 15, '#ffffff') + Ci(34, 25, 14, '#ef3340') + ''.join(_star5(42 + 9 * math.cos(math.radians(-90 + k * 72)), 25 + 9 * math.sin(math.radians(-90 + k * 72)), 3, '#ffffff') for k in range(5)),
    'new-zealand': lambda: R(0, 0, W_, H_, '#00247d') + G(union_jack(), 'scale(.5)') + ''.join(_star5(x, y, r_ + 1.5, '#ffffff') + _star5(x, y, r_, '#cc142b') for x, y, r_ in [(112, 22, 7), (98, 50, 7), (126, 44, 6), (112, 82, 8)]),
    'brazil': lambda: R(0, 0, W_, H_, '#009c3b') + Pa('M75,10 L140,50 L75,90 L10,50 Z', '#ffdf00') + Ci(75, 50, 24, '#002776') + St('M52,46 Q75,38 98,54', '#ffffff', 4),
    'mexico': lambda: vstripes(['#006847', '#ffffff', '#ce1126']) + Ci(75, 50, 12, '#8a5a35') + E(75, 60, 14, 4, '#3c8a3a'),
    'egypt': lambda: hstripes(['#ce1126', '#ffffff', '#000000']) + Pa('M68,40 L82,40 L80,58 L75,62 L70,58 Z', '#c09300'),
    'greece': lambda: ''.join(R(0, k * H_ / 9, W_, H_ / 9 + .5, '#0d5eaf' if k % 2 == 0 else '#ffffff') for k in range(9)) + R(0, 0, 55.5, 55.5, '#0d5eaf') + R(22, 0, 11, 55.5, '#ffffff') + R(0, 22, 55.5, 11, '#ffffff'),
    'switzerland': lambda: R(25, 0, 100, 100, '#da291c') + R(65, 20, 20, 60, '#ffffff') + R(45, 40, 60, 20, '#ffffff'),
    'netherlands': lambda: hstripes(['#ae1c28', '#ffffff', '#21468b']),
    'sweden': lambda: nordic('#006aa7', '#fecc00'),
    'norway': lambda: nordic('#ba0c2f', '#ffffff', '#00205b'),
    'portugal': lambda: vstripes(['#006600', '#ff0000'], weights=[2, 3]) + Ci(60, 50, 18, 'none', 'stroke="#ffcc00" stroke-width="4"') + R(52, 40, 16, 20, '#ffffff', 3, 'stroke="#ff0000" stroke-width="2"'),
    'ireland': lambda: vstripes(['#169b62', '#ffffff', '#ff883e']),
    'turkey-countries2': lambda: R(0, 0, W_, H_, '#e30a17') + Ci(55, 50, 25, '#ffffff') + Ci(62, 50, 20, '#e30a17') + _star5(88, 50, 12, '#ffffff', -18),
    'vietnam': lambda: R(0, 0, W_, H_, '#da251d') + _star5(75, 52, 30, '#ffff00'),
    'malaysia': lambda: ''.join(R(0, k * H_ / 14, W_, H_ / 14 + .5, '#cc0001' if k % 2 == 0 else '#ffffff') for k in range(14)) + R(0, 0, 75, H_ * 8 / 14, '#010066') + Ci(28, 28, 18, '#ffcc00') + Ci(34, 28, 16, '#010066') + _star5(56, 28, 13, '#ffcc00'),
    'indonesia': lambda: hstripes(['#ce1126', '#ffffff']),
    'philippines': lambda: hstripes(['#0038a8', '#ce1126']) + Pa('M0,0 L86,50 L0,100 Z', '#ffffff') + Ci(28, 50, 9, '#fcd116') + ''.join(L(28, 50, 28 + 16 * math.cos(k * math.pi / 4), 50 + 16 * math.sin(k * math.pi / 4), '#fcd116', 2) for k in range(8)) + ''.join(_star5(x, y, 5, '#fcd116') for x, y in [(8, 12), (8, 88), (70, 50)]),
    'south-africa': lambda: R(0, 0, W_, H_, '#ffffff') + R(0, 0, W_, 33, '#e03c31') + R(0, 67, W_, 33, '#001489') + Pa('M0,0 L60,40 L150,40 L150,60 L60,60 L0,100 Z', '#ffffff') + Pa('M0,10 L50,46 L150,46 L150,54 L50,54 L0,90 Z', '#007749') + Pa('M0,20 L44,50 L0,80 Z', '#ffb81c') + Pa('M0,28 L34,50 L0,72 Z', '#000000'),
    'argentina': lambda: hstripes(['#74acdf', '#ffffff', '#74acdf']) + Ci(75, 50, 9, '#f6b40e') + ''.join(L(75, 50, 75 + 14 * math.cos(k * math.pi / 8), 50 + 14 * math.sin(k * math.pi / 8), '#f6b40e', 1.5) for k in range(16)),
    'chile': lambda: hstripes(['#ffffff', '#d52b1e']) + R(0, 0, 50, 50, '#0039a6') + _star5(25, 25, 12, '#ffffff'),
    'peru': lambda: vstripes(['#d91023', '#ffffff', '#d91023']),
    'kenya': lambda: hstripes(['#000000', '#ffffff', '#bb0000', '#ffffff', '#006600'], weights=[6, 1, 6, 1, 6]) + E(75, 50, 12, 30, '#bb0000') + E(75, 50, 5, 30, '#000000', 'opacity=".8"') + L(55, 20, 95, 80, '#ffffff', 2) + L(95, 20, 55, 80, '#ffffff', 2),
    'morocco': lambda: R(0, 0, W_, H_, '#c1272d') + '<polygon points="75,26 81,44 100,44 85,55 91,74 75,62 59,74 65,55 50,44 69,44" fill="none" stroke="#006233" stroke-width="4"/>',
    'saudi-arabia': lambda: R(0, 0, W_, H_, '#006c35') + St('M40,40 q10,-10 20,0 t20,0 t20,0 t20,0', '#ffffff', 4) + R(40, 66, 70, 4, '#ffffff') + Pa('M110,64 L118,68 L110,72 Z', '#ffffff'),
    'united-arab-emirates': lambda: hstripes(['#00732f', '#ffffff', '#000000']) + R(0, 0, 38, H_, '#ff0000'),
    'pakistan': lambda: R(0, 0, 38, H_, '#ffffff') + R(38, 0, 112, H_, '#01411c') + Ci(94, 50, 24, '#ffffff') + Ci(102, 44, 21, '#01411c') + _star5(110, 38, 8, '#ffffff', 30),
    'nepal': lambda: Pa('M10,2 L100,50 L40,50 L100,98 L10,98 Z', '#003893') + Pa('M16,12 L84,46 L30,46 L84,92 L16,92 Z', '#dc143c') + Ci(34, 38, 8, '#ffffff') + Pa('M24,32 A10,10 0 0,0 44,32 A10,6 0 0,1 24,32 Z', '#ffffff') + _star5(34, 74, 9, '#ffffff'),
    'mongolia': lambda: vstripes(['#c4272f', '#015197', '#c4272f']) + Ci(25, 22, 6, '#f9cf02') + Pa('M18,14 Q25,0 32,14 Z', '#f9cf02') + R(18, 32, 14, 4, '#f9cf02') + R(18, 40, 14, 30, 'none', 0, 'stroke="#f9cf02" stroke-width="3"') + Ci(25, 55, 5, '#f9cf02'),
    'cambodia': lambda: hstripes(['#032ea1', '#e00025', '#032ea1'], weights=[1, 2, 1]) + R(52, 46, 46, 18, '#ffffff') + ''.join(Pa(f'M{56+k*12},46 L{60+k*12},32 L{64+k*12},46 Z', '#ffffff') for k in range(4)) + Pa('M70,46 L75,24 L80,46 Z', '#ffffff'),
    'finland': lambda: nordic('#ffffff', '#002f6c'),
    'denmark': lambda: nordic('#c8102e', '#ffffff'),
    'poland': lambda: hstripes(['#ffffff', '#dc143c']),
    'austria': lambda: hstripes(['#ed2939', '#ffffff', '#ed2939']),
    'belgium': lambda: vstripes(['#000000', '#fdda24', '#ef3340']),
    }
    return F[code]()
def flag_at(code, x, y, s=1, shadow=True, border=True):
    inner = flag_svg(code)
    g = ''
    if shadow: g += R(x + 4 * s, y + 6 * s, 150 * s, 100 * s, '#000000', 4 * s, 'opacity=".12"')
    g += f'<svg x="{x}" y="{y}" width="{150*s}" height="{100*s}" viewBox="0 0 150 100"><clipPath id="fc{code}{int(x)}{int(y)}"><rect width="150" height="100" rx="6"/></clipPath><g clip-path="url(#fc{code}{int(x)}{int(y)})">{inner}</g></svg>'
    if border: g += R(x, y, 150 * s, 100 * s, 'none', 6 * s, 'stroke="#000" stroke-opacity=".12" stroke-width="1.5"')
    return g
def flag_card(code):
    if code == 'switzerland':
        return R(54, 46, 100, 100, '#000000', 6, 'opacity=".12"') + R(50, 40, 100, 100, '#da291c', 6) + R(90, 60, 20, 60, '#ffffff') + R(70, 80, 60, 20, '#ffffff')
    if code == 'nepal':
        return f'<svg x="40" y="30" width="180" height="120" viewBox="0 0 150 100">' + flag_svg('nepal') + '</svg>'
    return flag_at(code, 25, 50, 1.0)
def flag_pole(code, x, y, s=.4):
    return R(x - 2, y - 4, 3, 100 * s + 40, '#5d6469') + flag_at(code, x, y, s, False)
