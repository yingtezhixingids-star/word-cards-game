from flat import *
from fig import *
import os, sys

A = {}

# ---------- cold 感冒：围着围巾、红鼻头、用纸巾擤鼻涕，旁边纸巾盒 ----------
cx, cy, r = 92, 78, 34
g = body(cx, cy, r, '#8c6bb1')
# 围巾
g += bare_head(cx, cy, r, '#3a2a20', 'long')
g += R(cx - r * 1.15, cy + r * .98, r * 2.3, r * .46, '#d9453a', 11) + R(cx - r * 1.15, cy + r * 1.3, r * 2.3, r * .14, shade('#d9453a', -.15), 6)
g += R(cx - r * .85, cy + r * 1.2, r * .42, r * 1.25, shade('#d9453a', -.1), 6)
g += ''.join(L(cx - r * .8 + i * 6, cy + r * 2.45, cx - r * .8 + i * 6, cy + r * 2.65, '#d9453a', 2.5) for i in range(3))
g += ''.join(L(cx - r * 1.0 + i * 9, cy + r * 1.02, cx - r * 1.0 + i * 9, cy + r * 1.38, shade('#d9453a', -.08), 2) for i in range(8))
g += brows_sad(cx, cy, r) + St(f'M{cx-r*.34-4},{cy} q4,3 8,0', '#3a2a20', 2.2) + St(f'M{cx+r*.34-4},{cy} q4,3 8,0', '#3a2a20', 2.2)
g += cheeks(cx, cy, r, '#ef8a8a', '.6')
g += Ci(cx, cy + r * .28, r * .13, '#e25b52')   # 红鼻头
# 纸巾捂住鼻子嘴（手在纸巾后面）
g += arm([(cx + r * 1.7, 200), (cx + r * 1.6, cy + r * 1.6), (cx + r * .45, cy + r * .55)], '#8c6bb1', P['skin'], 15)
g += Pa(f'M{cx-r*.42},{cy+r*.28} Q{cx-r*.1},{cy+r*.05} {cx+r*.38},{cy+r*.2} L{cx+r*.48},{cy+r*.82} Q{cx+r*.05},{cy+r*.98} {cx-r*.4},{cy+r*.78} Z', '#ffffff')
g += Pa(f'M{cx+r*.1},{cy+r*.14} L{cx+r*.38},{cy+r*.2} L{cx+r*.48},{cy+r*.82} L{cx+r*.2},{cy+r*.9} Z', '#e6ecef')
g += drop(cx - r * .55, cy - r * 1.3, 6, '#9fd0ec')
g += tissue_box(132, 148)
A['cold'] = svg(g)

# ---------- fever 发烧：满脸通红、出汗、额头搭湿毛巾，旁边温度计显示 39.5°C ----------
cx, cy, r = 84, 82, 34
g = body(cx, cy, r, '#6f9fcf')
g += bare_head(cx, cy, r, '#3a2a20', 'short')
g += E(cx, cy + r * .2, r * .8, r * .55, '#ef6a5a', 'opacity=".35"')      # 整体泛红
g += cheeks(cx, cy, r, '#e2463b', '.7')
g += R(cx - r * .95, cy - r * .78, r * 1.9, r * .42, '#ffffff', 7) + R(cx - r * .95, cy - r * .5, r * 1.9, r * .14, '#d6e4ec', 4)   # 湿毛巾
g += L(cx - r * .7, cy - r * .7, cx + r * .7, cy - r * .7, '#bcd3e0', 2)
g += brows_sad(cx, cy + 4, r)
g += Ci(cx - r * .34, cy + 2, 2.6, '#2b211b') + Ci(cx + r * .34, cy + 2, 2.6, '#2b211b')
g += St(f'M{cx-r*.34-5},{cy+7} q5,3 10,0', '#a85a48', 1.6) + St(f'M{cx+r*.34-5},{cy+7} q5,3 10,0', '#a85a48', 1.6)   # 眼袋
g += nose_line(cx, cy, r)
g += E(cx, cy + r * .55, r * .14, r * .1, '#7a3a30')
g += drop(cx + r * 1.0, cy - r * .2, 6) + drop(cx - r * 1.05, cy + r * .1, 5) + drop(cx + r * .82, cy + r * .5, 4.5)
# 温度计（电子）
th = R(-12, -54, 24, 92, '#ffffff', 12) + R(-12, -54, 24, 92, 'none', 12, 'stroke="#c4cbd0" stroke-width="2"')
th += R(-8, -40, 16, 40, '#f6d0c8', 3) + T(0, -14, '39.5', 9.5, '#d9453a', 800, extra='transform="rotate(-90 0 -20)"')
th += Ci(0, 14, 6, '#d9453a') + R(-3, 38, 6, 22, '#c4cbd0', 3) + Ci(0, 60, 4, '#a7adb1')
g += G(th, 'translate(160,96) rotate(10)')
g += T(160, 178, '°C', 22, '#d9453a', 800)
# 热浪
g += St('M150,26 q6,-8 0,-16 q-6,-8 0,-16', '#f08a24', 3, 'opacity=".8"') + St('M166,32 q6,-8 0,-16 q-6,-8 0,-16', '#f08a24', 3, 'opacity=".8"')
A['fever'] = svg(g)

# ---------- cough 咳嗽：侧身握拳挡嘴、闭眼使劲咳，嘴前有咳嗽气流线 ----------
cx, cy, r = 84, 80, 34
g = body(cx, cy, r, '#5ba68a')
g += bare_head(cx, cy, r, P['grey'], 'grey')
g += shut_eyes(cx, cy, r)
g += L(cx - r * .34 - 6, cy - 10, cx - r * .34 + 5, cy - 7, '#7a756e', 2.4) + L(cx + r * .34 + 6, cy - 10, cx + r * .34 - 5, cy - 7, '#7a756e', 2.4)
g += nose_line(cx, cy, r)
g += cheeks(cx, cy, r, '#ef8a8a', '.5')
g += E(cx + r * .06, cy + r * .55, r * .2, r * .14, '#7a3a30')
# 握拳挡在嘴前（袖子颜色加深，和身体分开）
sl = shade('#5ba68a', -.22)
g += arm([(cx - r * 1.2, 200), (cx - r * 1.05, cy + r * 1.75), (cx - r * .25, cy + r * 1.05)], sl, P['skin'], 17, hand=False)
g += Ci(cx + r * .02, cy + r * .72, r * .34, P['skin']) + Pa(f'M{cx-r*.3},{cy+r*.62} Q{cx},{cy+r*.42} {cx+r*.3},{cy+r*.62}', 'none', f'stroke="{shade(P["skin"], -.2)}" stroke-width="2"')
g += ''.join(St(f'M{cx-r*.26+i*r*.17},{cy+r*.5} l1,{r*.14}', shade(P['skin'], -.22), 1.6) for i in range(1, 4))
g += Pa(f'M{cx-r*.34},{cy+r*.78} q{r*.1},{r*.28} {r*.36},{r*.26}', 'none', f'stroke="{shade(P["skin"], -.2)}" stroke-width="2"')
# 咳出的气团
def puff(x, y, s, op):
    return G(Ci(0, 0, 9, '#c9d6dc') + Ci(10, -4, 11, '#c9d6dc') + Ci(21, 1, 8, '#c9d6dc') + Ci(10, 6, 9, '#c9d6dc'), f'translate({x},{y}) scale({s})" opacity="{op}')
g += puff(cx + r * .62, cy + r * .66, .8, .95) + puff(cx + r * 1.55, cy + r * .2, 1.0, .8) + puff(cx + r * 1.7, cy + r * 1.15, .85, .65)
g += St(f'M{cx+r*.5},{cy+r*.35} l10,-8 M{cx+r*.55},{cy+r*.95} l10,6', '#9aa7ad', 3)
g += T(160, 54, '!', 30, '#d9453a', 900) + T(146, 50, '!', 22, '#d9453a', 900, extra='opacity=".7"')
A['cough'] = svg(g)

# ---------- headache 头疼：双手按太阳穴、皱眉闭眼，头两侧有疼痛闪电 ----------
cx, cy, r = 100, 84, 34
g = body(cx, cy, r, '#d98a4a', w=r * 3.6)
g += bare_head(cx, cy, r, '#3a2a20', 'short')
g += St(f'M{cx-r*.34-5},{cy} q5,-3 10,0', '#3a2a20', 2.4) + St(f'M{cx+r*.34-5},{cy} q5,-3 10,0', '#3a2a20', 2.4)
g += L(cx - r * .34 - 6, cy - 7, cx - r * .34 + 5, cy - 11, '#3a2a20', 2.4) + L(cx + r * .34 + 6, cy - 7, cx + r * .34 - 5, cy - 11, '#3a2a20', 2.4)
g += St(f'M{cx-4},{cy-r*.5} l2,6 M{cx+4},{cy-r*.5} l-2,6', shade(P['skin'], -.25), 1.8)   # 眉心皱纹
g += nose_line(cx, cy, r)
g += St(f'M{cx-r*.25},{cy+r*.55} q{r*.12},{-r*.1} {r*.25},0 q{r*.12},{r*.1} {r*.25},0', '#9a4a3a', 2.2)
# 双臂抬起，手按太阳穴（袖子加深）
sl = shade('#d98a4a', -.18)
g += arm([(cx - r * 1.55, 200), (cx - r * 1.95, cy + r * 1.1), (cx - r * 1.12, cy - r * .3)], sl, P['skin'], 16, hand=False)
g += arm([(cx + r * 1.55, 200), (cx + r * 1.95, cy + r * 1.1), (cx + r * 1.12, cy - r * .3)], sl, P['skin'], 16, hand=False)
for sx in (-1, 1):
    hx = cx + sx * r * .9
    g += E(hx, cy - r * .3, r * .3, r * .4, P['skin'], f'transform="rotate({sx*-15} {hx} {cy-r*.3})"')
    g += ''.join(St(f'M{hx-sx*r*.05},{cy-r*.62+i*r*.17} l{-sx*r*.22},{r*.02}', shade(P['skin'], -.2), 1.6) for i in range(1, 4))
# 疼痛闪电
bolt = lambda x, y, sx: Pa(f'M{x},{y} L{x+sx*16},{y+6} L{x+sx*9},{y+10} L{x+sx*24},{y+20} L{x+sx*6},{y+13} L{x+sx*12},{y+9} Z', '#f3c234')
g += bolt(cx - r * 1.35, cy - r * 1.35, -1) + bolt(cx + r * 1.35, cy - r * 1.35, 1)
g += Pa(f'M{cx-r*.3},{cy-r*1.6} L{cx-r*.2},{cy-r*1.3} M{cx+r*.3},{cy-r*1.6} L{cx+r*.2},{cy-r*1.3} M{cx},{cy-r*1.7} L{cx},{cy-r*1.35}', 'none', 'stroke="#d9453a" stroke-width="3.5" stroke-linecap="round"')
A['headache'] = svg(g)


SK = P['skin']; SKD = shade(P['skin'], -.12)

# ---------- pain 疼痛：咬牙皱眉，手按着肩膀，肩上红色疼痛标记 ----------
cx, cy, r = 92, 76, 32
g = body(cx, cy, r, '#4f8fc0', w=r * 3.6)
g += face_full(cx, cy, r, '#3a2a20', 'short', 'shut', 'grit', 'sad')
g += pain_lines(cx + r * 1.45, cy + r * 1.35, 16, n=5, a0=-150, a1=-30)
g += burst(cx + r * 1.45, cy + r * 1.45, 16, '#e2463b', 7)
sl = shade('#4f8fc0', -.2)
g += arm([(cx - r * 1.45, 200), (cx - r * .6, cy + r * 2.4), (cx + r * 1.15, cy + r * 1.55)], sl, SK, 16, hand=False)
g += E(cx + r * 1.25, cy + r * 1.5, 12, 9, SK) + ''.join(L(cx + r * 1.12 + i * 6, cy + r * 1.3, cx + r * 1.12 + i * 6, cy + r * 1.5, SKD, 1.5) for i in range(3))
g += T(166, 60, '!', 28, '#d9453a', 900)
A['pain'] = svg(g)

# ---------- sick 恶心想吐：脸发绿、鼓腮、手捂嘴、额头冒汗 ----------
cx, cy, r = 96, 80, 34
g = body(cx, cy, r, '#c98f5a')
g += bare_head(cx, cy, r, '#5a3a2a', 'long')
g += E(cx, cy + r * .1, r * .85, r * .85, '#9bc77a', 'opacity=".55"')
g += eyes_closed(cx, cy, r, True) + brows_sad(cx, cy, r)
g += E(cx - r * .5, cy + r * .45, r * .2, r * .15, '#8ab868') + E(cx + r * .5, cy + r * .45, r * .2, r * .15, '#8ab868')
sl = shade('#c98f5a', -.2)
g += arm([(cx + r * 1.4, 200), (cx + r * 1.2, cy + r * 1.8), (cx + r * .25, cy + r * .9)], sl, SK, 16, hand=False)
g += E(cx, cy + r * .62, r * .42, r * .3, SK) + ''.join(L(cx - r * .3 + i * r * .2, cy + r * .45, cx - r * .3 + i * r * .2, cy + r * .66, SKD, 1.5) for i in range(4))
g += drop(cx - r * 1.05, cy - r * .55, 6) + drop(cx + r * 1.05, cy - r * .4, 5)
g += St('M150,40 q8,-6 16,0 t16,0', '#7fae5a', 3.5) + St('M148,56 q8,-6 16,0 t16,0', '#7fae5a', 3.5) + St('M20,48 q8,-6 16,0 t16,0', '#7fae5a', 3.5)
A['sick'] = svg(g)

# ---------- cut 伤口：手指上有一道流血的口子，旁边菜刀和创可贴 ----------
g = hand(86, 190, 1.35, -8)
g += Pa('M57,110 L71,105', 'none', 'stroke="#c0282a" stroke-width="3.5" stroke-linecap="round"')
g += drop(64, 120, 5, '#d9302c') + drop(66, 134, 4, '#d9302c')
# 菜刀
g += G(R(0, 0, 70, 34, '#cfd5d9', 3) + Pa('M0,0 L70,0 L70,34 L8,34 Q0,20 0,0 Z', '#dfe4e7') + R(0, 28, 70, 6, '#b5bcc1') + Ci(60, 8, 4, '#a7adb1') +
       R(70, 8, 46, 16, '#5a3a24', 6) + Ci(84, 16, 2, '#c58b54') + Ci(100, 16, 2, '#c58b54'), 'translate(118,128) rotate(-30) scale(.62)')
g += bandage(150, 52, 54, 18, 25)
A['cut'] = svg(g)

# ---------- flu 流感：躺在床上盖着被子，嘴里含体温计，床头纸巾 ----------
g = R(16, 90, 12, 90, '#8a5a35', 4) + R(16, 82, 12, 12, '#a06a40', 6)
g += R(24, 130, 160, 34, '#c58b54', 4) + R(172, 112, 12, 68, '#8a5a35', 4)
g += R(30, 104, 64, 30, '#ffffff', 14) + R(30, 122, 64, 12, '#e6ecef', 8)
g += face_full(60, 104, 22, '#3a2a20', 'short', 'closed', 'flat', 'sad', '#e2463b')
g += G(R(0, -3, 34, 6, '#ffffff', 3) + Ci(30, 0, 3.5, '#d9453a'), 'translate(60,117) rotate(-18)')
g += Pa('M70,124 Q120,108 176,118 L176,164 L74,164 Q64,146 70,124 Z', '#6aa7d8') + Pa('M70,124 Q120,108 176,118 L176,128 Q120,120 72,136 Z', shade('#6aa7d8', .2))
g += L(110, 130, 110, 162, shade('#6aa7d8', -.15), 2) + L(144, 126, 144, 162, shade('#6aa7d8', -.15), 2)
g += drop(36, 84, 6) + drop(86, 86, 5)
g += tissue_box(124, 50, 46, 28)
g += Pa('M26,190 q-4,-10 4,-12 q10,-1 8,10 Z', '#ffffff') + Pa('M150,186 q-6,-12 6,-12 q10,2 4,12 Z', '#ffffff')
g += T(120, 40, 'z', 16, '#7a8a94', 800) + T(108, 30, 'z', 12, '#7a8a94', 800)
A['flu'] = svg(g, shadow=False)

# ---------- dizzy 头晕：眼睛打转，头上绕着星星，扶着额头 ----------
cx, cy, r = 100, 90, 34
g = body(cx, cy, r, '#9a7ab8')
g += bare_head(cx, cy, r, P['grey'], 'grey')
for sx in (-1, 1):
    ex = cx + sx * r * .34
    g += St(f'M{ex},{cy} m-1,0 a2,2 0 1,1 3,1 a4,4 0 1,1 -6,-2 a6,6 0 1,1 9,3', '#2b211b', 1.8)
g += nose_line(cx, cy, r) + mouth(cx, cy, r, 'wavy')
g += St(f'M{cx},{cy-r*1.45} m-46,0 a46,12 0 1,0 92,0 a46,12 0 1,0 -92,0', '#e8b53a', 2.5, 'stroke-dasharray="7 6" opacity=".9"')
def star(x, y, s, c='#f3c234'):
    import math
    pts = ' L'.join(f'{x+(s if i%2==0 else s*.45)*math.cos(math.pi/5*i-math.pi/2):.1f},{y+(s if i%2==0 else s*.45)*math.sin(math.pi/5*i-math.pi/2):.1f}' for i in range(10))
    return Pa('M' + pts + ' Z', c)
g += star(cx - 46, cy - r * 1.45, 9) + star(cx + 30, cy - r * 1.45 - 10, 8) + star(cx + 44, cy - r * 1.35 + 6, 7, '#ef8a3a') + star(cx - 10, cy - r * 1.45 + 12, 6, '#ef8a3a')
sl = shade('#9a7ab8', -.2)
g += arm([(cx - r * 1.7, 200), (cx - r * 1.95, cy + r * 1.1), (cx - r * .95, cy - r * .5)], sl, SK, 16, hand=False)
g += E(cx - r * .8, cy - r * .55, r * .32, r * .26, SK, f'transform="rotate(-25 {cx-r*.8} {cy-r*.55})"')
A['dizzy'] = svg(g)

# ---------- toothache 牙疼：半边脸肿，手捂腮帮，头上扎手帕，旁边一颗疼痛的牙 ----------
cx, cy, r = 84, 84, 34
g = body(cx, cy, r, '#5ba644')
g += bare_head(cx, cy, r, '#3a2a20', 'short')
g += E(cx + r * .55, cy + r * .45, r * .42, r * .38, SK)   # 肿起的腮帮
g += E(cx + r * .58, cy + r * .45, r * .22, r * .16, '#ef8a8a', 'opacity=".8"')
g += Pa(f'M{cx-r*.95},{cy+r*.1} Q{cx},{cy+r*1.45} {cx+r*1.05},{cy+r*.1} L{cx+r*.95},{cy-r*.15} Q{cx},{cy+r*1.15} {cx-r*.85},{cy-r*.15} Z', '#ffffff')  # 手帕
g += Pa(f'M{cx-r*.95},{cy-r*.15} Q{cx-r*.75},{cy-r*1.35} {cx},{cy-r*1.2} Q{cx+r*.75},{cy-r*1.35} {cx+r*.95},{cy-r*.15} L{cx+r*.8},{cy-r*.2} Q{cx},{cy-r*1.0} {cx-r*.8},{cy-r*.2} Z', '#ffffff')
g += Pa(f'M{cx-6},{cy-r*1.22} q-14,-18 -2,-20 q8,4 2,20 Z M{cx+6},{cy-r*1.22} q14,-18 2,-20 q-8,4 -2,20 Z', '#ffffff')
g += Pa(f'M{cx-r*.3},{cy-r*.2} L{cx-r*.25},{cy-r*.03}', 'none', 'stroke="#3a2a20" stroke-width="2.4" stroke-linecap="round"')
g += shut_eyes(cx, cy, r) + nose_line(cx, cy, r) + mouth(cx - 4, cy, r, 'sad')
sl = shade('#5ba644', -.2)
g += arm([(cx + r * 1.6, 200), (cx + r * 1.9, cy + r * 1.2), (cx + r * 1.15, cy + r * .5)], sl, SK, 16, hand=False)
g += E(cx + r * 1.0, cy + r * .45, r * .26, r * .36, SK)
def tooth(x, y, s, col='#ffffff'):
    return G(Pa('M-20,-18 Q-22,-30 -10,-30 Q0,-26 0,-26 Q0,-26 10,-30 Q22,-30 20,-18 Q18,0 14,12 Q10,26 6,26 Q2,20 0,6 Q-2,20 -6,26 Q-10,26 -14,12 Q-18,0 -20,-18 Z', col) +
             Pa('M8,-29 Q22,-30 20,-18 Q18,0 14,12 Q10,26 6,26 Q12,0 8,-29 Z', '#dfe6ea'), f'translate({x},{y}) scale({s})')
g += tooth(162, 66, 1.1) + Pa('M150,52 L158,62 L152,66 L162,76', 'none', 'stroke="#d9453a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"')
g += pain_lines(162, 62, 24, n=5, a0=-160, a1=-20)
A['toothache'] = svg(g)

# ---------- broken 骨折：胳膊打着石膏吊在胸前，旁边一根断开的骨头 ----------
cx, cy, r = 86, 70, 30
g = body(cx, cy, r, '#3c7fc1', w=r * 3.8)
g += face_full(cx, cy, r, '#3a2a20', 'short', 'dot', 'sad', 'sad')
g += Pa(f'M{cx-r*.9},{cy+r*1.1} L{cx+r*1.4},{cy+r*1.3} L{cx+r*1.2},{cy+r*3.0} Z', '#5a9fd8')  # 三角吊带
g += R(cx - r * 1.1, cy + r * 1.95, r * 2.5, r * .78, '#ffffff', 12) + R(cx - r * 1.1, cy + r * 2.5, r * 2.5, r * .23, '#e0e6e9', 6)
g += E(cx - r * 1.2, cy + r * 2.34, r * .3, r * .32, SK)
g += Pa(f'M{cx-r*.95},{cy+r*1.05} L{cx-r*.75},{cy+r*1.0} L{cx+r*1.25},{cy+r*3.1} L{cx+r*1.0},{cy+r*3.2} Z', '#3f7fb5')
def bone(x, y, s, rot):
    b = R(-30, -6, 60, 12, '#f6f1e4', 4) + Ci(-30, -8, 8, '#f6f1e4') + Ci(-30, 8, 8, '#f6f1e4') + Ci(30, -8, 8, '#f6f1e4') + Ci(30, 8, 8, '#f6f1e4')
    return G(b, f'translate({x},{y}) rotate({rot}) scale({s})')
g += G(R(-52, -46, 104, 92, '#2f3d4a', 8) + G(bone(-18, 0, .8, 0), 'rotate(-8)') + G(bone(20, 6, .8, 0), 'rotate(12)') +
       Pa('M2,-12 L-4,-2 L4,2 L-2,12', 'none', 'stroke="#e2463b" stroke-width="3" stroke-linecap="round"'), 'translate(158,42) scale(.55)')
A['broken'] = svg(g)

# ---------- sprain 扭伤：脚踝缠着弹力绷带、红肿，旁边冰袋 ----------
g = Pa('M60,10 L100,10 L104,120 Q108,140 120,148 L168,160 Q182,166 178,178 L176,182 L72,182 Q62,182 62,170 L58,120 Z', SK)
g += Pa('M100,10 L104,120 Q108,140 120,148 L168,160 Q182,166 178,178 L176,182 L150,182 Q140,168 110,160 Q92,150 90,120 L88,10 Z', SKD)
g += R(52, 0, 56, 26, '#3b5f8f', 4)
g += Pa('M58,106 L106,104 L114,152 L66,170 Z', '#e9c79c')
for i in range(5):
    g += L(58 + i * 2, 112 + i * 12, 108 + i * 2, 106 + i * 10, '#d6b083', 3)
g += E(118, 142, 12, 10, '#e2463b', 'opacity=".55"') + pain_lines(118, 140, 22, n=4, a0=-80, a1=10)
g += E(176, 182, 0, 0, SK)
g += G(R(-26, -18, 52, 36, '#7fc4ea', 12) + R(-18, -24, 36, 10, '#5aa8d6', 4) + R(-20, -10, 18, 14, '#ffffff', 3, 'opacity=".6"') + R(2, -4, 14, 10, '#ffffff', 3, 'opacity=".6"'), 'translate(160,94) rotate(10)')
g += T(160, 66, '❄', 18, '#5aa8d6', 700)
A['sprain'] = svg(g)

# ---------- bruise 淤青：小腿膝盖上一块紫青色淤痕 ----------
g = R(40, 6, 90, 50, '#3b5f8f', 10) + R(40, 44, 90, 12, '#2f4f78', 6)
g += Pa('M48,52 L124,52 Q128,90 122,120 Q118,150 116,168 L58,168 Q56,140 52,120 Q44,90 48,52 Z', SK)
g += Pa('M100,52 L124,52 Q128,90 122,120 Q118,150 116,168 L102,168 Q108,120 100,52 Z', SKD)
g += Pa('M56,166 L118,166 Q160,170 172,180 Q176,188 166,190 L56,190 Z', '#ffffff') + R(52, 160, 70, 12, '#e8e8e8', 6)
g += E(86, 96, 22, 18, '#8a5aa8', 'opacity=".8"') + E(84, 94, 14, 11, '#5d3a86', 'opacity=".8"') + E(94, 102, 9, 7, '#6a9a6a', 'opacity=".35"')
g += pain_lines(86, 96, 26, n=4, a0=-30, a1=60, col='#8a5aa8')
A['bruise'] = svg(g)

# ---------- burn 烫伤：手背上一块红肿，旁边冒热气的锅 ----------
g = G(Ci(0, 0, 40, '#3a3f44') + Ci(0, 0, 32, '#50565c') + R(36, -6, 60, 12, '#2f3437', 6), 'translate(64,140) scale(1,.45)')
g += St('M44,110 q-8,-12 0,-24 q8,-12 0,-24', '#c4cbd0', 4) + St('M64,106 q-8,-12 0,-24 q8,-12 0,-24', '#c4cbd0', 4) + St('M84,110 q-8,-12 0,-24 q8,-12 0,-24', '#c4cbd0', 4)
g += hand(146, 188, 1.0, 12)
g += E(144, 128, 16, 12, '#e2463b', 'opacity=".6"') + E(146, 128, 8, 6, '#f7a8a0') + Ci(150, 124, 3, '#ffe0d8')
g += pain_lines(144, 128, 20, n=5, a0=-170, a1=-10, col='#f08a24')
A['burn'] = svg(g)

# ---------- allergy 过敏：脸上起红疹、打喷嚏挠痒，旁边花生和花 ----------
cx, cy, r = 80, 82, 33
g = body(cx, cy, r, '#f3c234')
g += face_full(cx, cy, r, '#3a2a20', 'long', 'shut', 'o', 'sad')
import random; random.seed(3)
for _ in range(14):
    a, b = random.uniform(-.7, .7), random.uniform(-.3, .8)
    g += Ci(cx + a * r, cy + b * r, random.uniform(2, 3.4), '#e2463b', 'opacity=".75"')
g += St(f'M{cx-r*1.3},{cy+r*.2} l-8,-4 M{cx-r*1.3},{cy+r*.5} l-10,0 M{cx-r*1.3},{cy+r*.8} l-8,4', '#d9453a', 2.5)
def peanut(x, y, rot):
    return G(E(-9, 0, 11, 9, '#d9b07a') + E(9, 0, 11, 9, '#d9b07a') + E(0, 0, 6, 6, '#d9b07a') +
             ''.join(Ci(-12 + i * 6, -3 + (i % 2) * 5, 1.2, '#b88c55') for i in range(5)), f'translate({x},{y}) rotate({rot})')
g += peanut(150, 150, -20) + peanut(170, 168, 25) + peanut(140, 172, 5)
g += Ci(160, 60, 7, '#f3c234') + ''.join(E(160 + 12 * __import__('math').cos(i * 1.2566), 60 + 12 * __import__('math').sin(i * 1.2566), 8, 6, '#ffffff', f'transform="rotate({i*72} {160 + 12 * __import__("math").cos(i * 1.2566)} {60 + 12 * __import__("math").sin(i * 1.2566)})"') for i in range(5)) + Ci(160, 60, 7, '#f3c234')
g += St('M160,72 Q162,100 156,118', '#5ba644', 3) + leaf(158, 98, 20, 7, -30, '#5ba644')
A['allergy'] = svg(g)

# ---------- high blood pressure 高血压：血压计读数偏高显示红色、向上箭头 ----------
g = R(30, 46, 120, 104, '#f4f1ea', 14) + R(30, 132, 120, 18, '#e2ddd3', 10)
g += R(42, 58, 76, 60, '#f6d0c8', 6)
g += T(80, 86, '170', 26, '#d9453a', 800) + T(80, 110, '105', 20, '#2f3437', 700)
g += Ci(134, 74, 8, '#3c7fc1') + Ci(134, 100, 8, '#d9453a')
g += St('M150,120 Q182,130 176,170 Q170,186 140,182', '#4a5157', 6) + R(112, 168, 40, 22, '#2f5a8a', 8)
g += Pa('M168,24 L186,50 L174,50 L174,78 L162,78 L162,50 L150,50 Z', '#e2463b')
hx, hy, hs = 56, 30, 14
g += Pa(f'M{hx},{hy+hs*.85} C{hx-hs*1.3},{hy-hs*.05} {hx-hs*.75},{hy-hs*1.05} {hx},{hy-hs*.4} C{hx+hs*.75},{hy-hs*1.05} {hx+hs*1.3},{hy-hs*.05} {hx},{hy+hs*.85} Z', '#e2463b')
g += St(f'M{hx-14},{hy} l6,0 l3,-6 l4,12 l3,-6 l12,0', '#ffffff', 2)
A['high-blood-pressure'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
