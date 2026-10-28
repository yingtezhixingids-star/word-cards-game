from kit3 import *
import os, sys

A = {}
def S_(k, g, shadow=True): A[k] = svg(g, shadow)

def me_star(x, y):
    return star(x, y, 8, '#f3c234')

def halo(x, ground, h=150, w=40):
    return E(x, ground - h / 2, w, h / 2 + 6, '#f3c234', 'opacity=".22"') + E(x, ground - h / 2, w, h / 2 + 6, 'none', 'stroke="#f3c234" stroke-width="3"')

def heart_link(x, y, s=10):
    return heart(x, y, s, '#e2463b')

# ================= 家人 =================
# 以“我”(带小星星)为参照，目标人物被黄色光圈圈出
# mother 妈妈：妈妈牵着小孩的手，妈妈被圈出
S_('mother', halo(76, 190, 160, 34) + fig(76, 190, 'woman', arms='down') + fig(136, 190, 'girl') + St('M96,122 L118,138', SK, 6) + me_star(136, 70))
S_('father', halo(70, 190, 168, 36) + fig(70, 190, 'man') + fig(136, 190, 'boy') + St('M90,122 L118,140', SK, 6) + me_star(136, 70))
S_('son', halo(146, 190, 110, 26) + fig(70, 190, 'oldwoman') + fig(146, 190, 'youngman', s=.8) + me_star(70, 10) + heart_link(108, 60))
S_('daughter', halo(146, 190, 110, 26) + fig(70, 190, 'oldman') + fig(146, 190, 'youngwoman', s=.8) + me_star(70, 10) + heart_link(108, 60))
S_('husband', halo(130, 190, 160, 34) + fig(70, 190, 'oldwoman') + fig(130, 190, 'oldman') + me_star(70, 18) + G(Ci(0, 0, 9, 'none', 'stroke="#d9a33a" stroke-width="3"') + Ci(10, 0, 9, 'none', 'stroke="#d9a33a" stroke-width="3"'), 'translate(95,40)'))
S_('wife', halo(70, 190, 155, 32) + fig(70, 190, 'oldwoman') + fig(130, 190, 'oldman') + me_star(130, 20) + G(Ci(0, 0, 9, 'none', 'stroke="#d9a33a" stroke-width="3"') + Ci(10, 0, 9, 'none', 'stroke="#d9a33a" stroke-width="3"'), 'translate(95,40)'))
S_('grandson', halo(140, 190, 100, 24) + fig(70, 190, 'oldman') + fig(140, 190, 'boy') + me_star(70, 18) + St('M88,120 L122,140', SK, 6) + heart_link(110, 80))
S_('granddaughter', halo(140, 190, 100, 24) + fig(70, 190, 'oldwoman') + fig(140, 190, 'girl') + me_star(70, 26) + St('M88,122 L122,140', SK, 6) + heart_link(110, 80))
S_('grandmother', halo(70, 190, 150, 32) + fig(70, 190, 'oldwoman') + fig(140, 190, 'girl') + me_star(140, 88) + St('M88,122 L122,140', SK, 6))
S_('grandfather', halo(70, 190, 156, 32) + fig(70, 190, 'oldman') + fig(140, 190, 'boy') + me_star(140, 88) + St('M88,122 L122,140', SK, 6) + R(40, 110, 4, 80, '#8a5a35'))
S_('brother', halo(136, 190, 160, 32) + fig(70, 190, 'youngwoman', s=.9) + fig(136, 190, 'youngman', s=.95) + me_star(70, 40) + ''.join(Ci(103, 100 + k * 6, 0, '#000') for k in range(1)) + St('M88,96 L118,96', '#5ba644', 0) + T(103, 60, '+', 0, '#000'))
S_('sister', halo(136, 190, 150, 32) + fig(70, 190, 'youngman', s=.95) + fig(136, 190, 'youngwoman', s=.9) + me_star(70, 34))
# uncle 叔叔：大人(叔叔)和小孩，叔叔被圈出，旁边爸爸
S_('uncle', fig(46, 190, 'man', shirt='#3c7fc1', s=.95) + halo(150, 190, 160, 32) + fig(150, 190, 'man', shirt='#d9645a', s=.95) + fig(98, 190, 'boy') + me_star(98, 90) + St('M66,96 L130,96', '#a7adb1', 0))
S_('aunt', fig(46, 190, 'woman', s=.95) + halo(150, 190, 155, 32) + fig(150, 190, 'woman', shirt='#9a7ab8', s=.95) + fig(98, 190, 'girl') + me_star(98, 90))
S_('cousin', fig(50, 190, 'boy', s=1.1) + halo(140, 190, 110, 26) + fig(140, 190, 'girl', s=1.1) + me_star(50, 80) + St('M70,140 L118,140', SK, 0) + heart_link(96, 100, 8))
S_('daughter-in-law', fig(46, 190, 'oldwoman', s=.95) + me_star(46, 20) + fig(104, 190, 'youngman', s=.85) + halo(156, 190, 140, 28) + fig(156, 190, 'youngwoman', s=.85) + G(Ci(0, 0, 7, 'none', 'stroke="#d9a33a" stroke-width="3"') + Ci(8, 0, 7, 'none', 'stroke="#d9a33a" stroke-width="3"'), 'translate(126,46)'))

# ================= 心情 =================
F = lambda **kw: big_face(100, 104, 64, **kw)
S_('happy', F(eyes='up', m='grin', blush='#ef9a8a') + star(30, 40, 8) + star(170, 50, 6))
S_('sad', F(eyes='dot', m='sad', brows='sad') + drop(60, 120, 7, '#9fd0ec') + drop(140, 124, 5, '#9fd0ec'))
S_('tired', F(eyes='closed', m='o', brows='sad') + E(100 - 22, 112, 12, 4, '#c8a0a0', 'opacity=".5"') + E(122, 112, 12, 4, '#c8a0a0', 'opacity=".5"') + zzz(140, 50, .9) + drop(52, 60, 6))
S_('angry', F(eyes='dot', m='shout', brows='angry', blush='#e2463b') + E(100, 120, 50, 40, '#e2463b', 'opacity=".2"') + Pa('M150,36 l8,10 l-10,4 l12,8', 'none', 'stroke="#e2463b" stroke-width="4" stroke-linecap="round"') + St('M40,40 q10,-10 20,0 M140,20 q10,-10 20,0', '#c4cbd0', 3))
S_('worried', F(eyes='dot', m='wavy', brows='sad') + drop(160, 60, 7) + St('M40,50 q10,-10 20,0 t20,0', '#7a8a94', 3) + T(150, 40, '?', 24, '#7a8a94', 800))
S_('excited', F(eyes='big', m='grin', brows='up', blush='#ef9a8a') + ''.join(star(30 + k * 35, 30 + (k % 2) * 20, 8, '#f3c234') for k in range(5)) + St('M20,100 l-10,0 M180,100 l10,0', '#f3c234', 4))
S_('bored', F(eyes='side', m='flat', brows='flat') + R(30, 40, 0, 0, '#000') + St('M30,40 q10,-6 20,0 q10,6 20,0', '#a7adb1', 3) + T(160, 50, '...', 30, '#7a8a94', 900))
S_('scared', F(eyes='big', m='O', brows='up') + E(100, 104, 58, 64, '#9fd0ec', 'opacity=".25"') + St('M28,90 q-8,10 0,20 q8,10 0,20 M172,90 q8,10 0,20 q-8,10 0,20', '#7a8a94', 3) + drop(46, 60, 6))
# lonely 孤单：一个老人独自坐在长椅上，四周空荡荡
S_('lonely', R(0, 0, 200, 200, '#d9dce6') + R(0, 160, 200, 40, '#a7b0a0') + bench_(100, 176, 90) + pose((100, 100), (100, 120), (100, 150), arms=[[(92, 124), (90, 146)]], legs=[[(96, 150), (120, 152), (122, 176)]], shirt='#7a8a9a', pants='#5d6469', style='grey', hair=P['grey'], mood='sad', hr=13, tw=24) + tree(30, 140, .5) + ''.join(leaf(140 + k * 14, 60 + k * 20, 10, 4, k * 60, '#c8a060') for k in range(3)), False)
S_('proud', F(eyes='closed', m='smile', brows='up') + Pa('M70,180 L130,180 L120,200 L80,200 Z', '#3c7fc1', 'opacity="0"') + G(Ci(0, 0, 18, '#f3c234') + star(0, 0, 10, '#e0a820') + Pa('M-12,14 L-18,40 L-6,32 L0,42 L0,16 Z M12,14 L18,40 L6,32 L0,42 L0,16 Z', '#e2463b'), 'translate(150,150)') + St('M40,30 l6,10 M30,50 l10,4', '#f3c234', 3))
S_('surprised', F(eyes='big', m='O', brows='up') + T(160, 50, '!', 40, '#e2463b', 900) + T(40, 50, '!', 30, '#e2463b', 900))
S_('nervous', F(eyes='dot', m='wavy', brows='sad', blush='#ef9a8a') + drop(48, 70, 7) + drop(152, 80, 6) + drop(160, 110, 5) + St('M30,140 l-8,6 M170,140 l8,6', '#7a8a94', 3))
S_('calm', R(0, 0, 200, 200, '#e6f0f4') + St('M0,170 q25,-10 50,0 t50,0 t50,0 t50,0', '#9fd0ec', 4) + big_face(100, 96, 58, eyes='closed', m='smile') + leaf(160, 40, 24, 9, 30, '#7cc05a'), False)
S_('relaxed', R(0, 0, 200, 200, '#f6efe0') + Ci(170, 30, 16, '#f3c234') + big_face(100, 100, 56, eyes='closed', m='smile', blush='#ef9a8a') + St('M30,40 q10,-6 20,0 t20,0', '#9fd0ec', 3) + note(150, 120, .8), False)
S_('confused', F(eyes='side', m='wavy', brows='sad') + T(150, 46, '?', 40, '#3c7fc1', 900) + T(56, 40, '?', 28, '#3c7fc1', 900) + St('M164,96 a6,6 0 1,1 8,6 a10,10 0 1,1 -14,-8', '#7a8a94', 2))
S_('grateful', big_face(100, 80, 50, eyes='up', m='smile', blush='#ef9a8a', style='bun', hair=P['grey']) + Pa('M40,200 L40,170 Q40,140 100,140 Q160,140 160,170 L160,200 Z', '#d9645a') + G(R(-12, -40, 24, 50, SK, 10) + R(-2, -40, 4, 40, SKD), 'translate(100,170)') + heart(150, 50, 12) + heart(46, 46, 8))

# ================= 人生大事 =================
def cake2(cx, base, s=1):
    g = E(0, 0, 70, 14, '#d9dcde') + R(-56, -50, 112, 50, '#fbf3e6', 6) + E(0, -50, 56, 12, '#ffffff') + Pa('M-56,-50 ' + ' '.join(f'q7,{12 if k%2 else 4} 14,0' for k in range(8)) + ' L56,-50 Z', '#ef8fa4')
    g += ''.join(R(-30 + k * 20, -80, 6, 26, ['#5aa1d4', '#f3c234', '#5ba644', '#ef8fa4'][k], 2) + Pa(f'M{-27+k*20},-94 Q{-21+k*20},-86 {-27+k*20},-80 Q{-33+k*20},-86 {-27+k*20},-94 Z', '#f08a24') for k in range(4))
    return G(g, f'translate({cx},{base}) scale({s})')
def gift_(x, y, s=1, col='#e2463b', rib='#f3c234'):
    return G(R(-40, -30, 80, 66, col, 4) + R(-6, -30, 12, 66, rib) + R(-44, -40, 88, 16, shade(col, -.1), 3) + R(-6, -40, 12, 16, rib) + Pa('M0,-40 Q-26,-66 -28,-50 Q-26,-38 0,-40 Z M0,-40 Q26,-66 28,-50 Q26,-38 0,-40 Z', rib), f'translate({x},{y}) scale({s})')
def ring_jewel(x, y, s=1):
    return G(Ci(0, 0, 22, 'none', 'stroke="#d9a33a" stroke-width="6"') + Pa('M-10,-22 L0,-40 L10,-22 Z', '#bfe6fa') + Pa('M-10,-22 L0,-30 L10,-22 Z', '#ffffff'), f'translate({x},{y}) scale({s})')

S_('birthday', cake2(100, 176, 1.1) + balloon(30, 50, 16, '#e2463b') + balloon(170, 46, 16, '#3c7fc1') + confetti(3, 14, (40, 10, 120, 40)))
S_('party', ''.join(balloon(30 + k * 36, 40 + (k % 2) * 16, 14, ['#e2463b', '#f3c234', '#3c7fc1', '#5ba644', '#ef8fa4'][k]) for k in range(5)) + fig(60, 196, 'woman', arms='up', s=.65) + fig(140, 196, 'man', arms='wave', s=.68) + confetti(5, 18, (10, 80, 180, 40)) + Pa('M92,110 L108,110 L100,80 Z', '#7a4fa0') + R(98, 80, 4, 6, '#f3c234'))
S_('gift', gift_(100, 120, 1.6))
# wedding 婚礼：新郎新娘，白婚纱和黑西装，头顶爱心
S_('wedding', Pa('M42,190 L60,100 L92,100 L110,190 Z', '#ffffff') + Pa('M60,100 Q76,60 92,100', 'none', 'stroke="none"') + person(76, 190, shirt='#ffffff', pants='#ffffff', style='long', hair='#3a2a20', arms='front', s=.95) + Pa('M48,190 L62,110 L90,110 L104,190 Z', '#ffffff') + Pa('M60,30 Q76,10 92,30 L100,90 L52,90 Z', '#ffffff', 'opacity=".6"') + fig(130, 190, 'man', shirt='#ffffff', pants='#2f3437', coat='#2f3437') + R(127, 54, 6, 6, '#e2463b', 1) + heart(104, 20, 14) + flower(88, 100, .8, '#ef8fa4'))
S_('born', baby_(100, 110, 2.0) + heart(40, 40, 12) + heart(160, 50, 9) + star(150, 160, 7) + star(40, 160, 6))
S_('married', ring_jewel(84, 110, 1.6) + G(Ci(0, 0, 22, 'none', 'stroke="#d9a33a" stroke-width="6"'), 'translate(124,120) scale(1.4)') + heart(104, 46, 14))
S_('celebrate', ''.join(G(''.join(L(0, 0, 30 * math.cos(a), 30 * math.sin(a), c, 3) + Ci(34 * math.cos(a), 34 * math.sin(a), 3, c) for a in [k * math.pi / 6 for k in range(12)]), f'translate({x},{y})') for x, y, c in [(50, 50, '#e2463b'), (150, 40, '#f3c234'), (110, 80, '#5aa1d4')]) + fig(70, 196, 'oldman', arms='up', s=.6) + fig(130, 196, 'oldwoman', arms='up', s=.62))
# festival 节日：红灯笼、鞭炮和月饼——中国传统节日
def lantern(x, y, s=1):
    return G(L(0, -40, 0, -26, '#d9a33a', 2) + R(-14, -28, 28, 6, '#d9a33a', 2) + E(0, 0, 26, 24, '#e2302a') + ''.join(St(f'M{k*9},-22 Q{k*14},0 {k*9},22', '#c0201a', 1.5) for k in (-2, -1, 0, 1, 2)) + R(-14, 22, 28, 6, '#d9a33a', 2) + ''.join(L(-8 + j * 4, 28, -8 + j * 4, 44, '#d9a33a', 1.5) for j in range(5)), f'translate({x},{y}) scale({s})')
S_('festival', R(0, 0, 200, 200, '#2f2a45') + St('M0,30 Q100,60 200,30', '#d9a33a', 2) + lantern(40, 74, 1.0) + lantern(100, 86, 1.1) + lantern(160, 74, 1.0) + ''.join(G(''.join(L(0, 0, 20 * math.cos(a), 20 * math.sin(a), c, 2) for a in [k * math.pi / 6 for k in range(12)]), f'translate({x},{y})') for x, y, c in [(70, 160, '#f3c234'), (150, 150, '#ef8fa4')]), False)
S_('anniversary', heart(100, 110, 70, '#e2463b') + T(100, 124, '50', 46, '#ffffff', 900) + ring_jewel(40, 170, .6) + star(170, 40, 8) + star(30, 40, 6))
# retirement 退休：老人抱着装满办公用品的箱子离开公司，挥手，摇椅
S_('retirement', R(0, 0, 70, 200, '#c8d0d8') + ''.join(R(8 + (k % 2) * 30, 20 + (k // 2) * 30, 20, 18, '#8ec3e6') for k in range(10)) + fig(110, 190, 'oldman', arms='front') + box_(86, 96, 50, 36) + R(96, 84, 10, 16, '#5ba644', 2) + R(110, 88, 12, 12, '#f3c234') + G(St('M0,40 Q20,60 50,40', '#8a5a35', 5) + R(4, -20, 6, 50, '#8a5a35', 2) + R(4, 10, 40, 8, '#8a5a35', 2), 'translate(140,130)'), False)
# graduation 毕业：学士帽和卷起来的毕业证书
S_('graduation', Pa('M30,80 L100,50 L170,80 L100,110 Z', '#2f3437') + Pa('M60,94 L60,124 Q100,144 140,124 L140,94 L100,110 Z', '#3a3f44') + St('M150,84 L150,120', '#f3c234', 3) + Ci(150, 124, 5, '#f3c234') + G(R(-50, -12, 100, 24, '#f6efe0', 12) + R(-10, -12, 14, 24, '#e2463b') + E(50, 0, 6, 12, '#e6dcc4'), 'translate(100,164) rotate(-8)'))
S_('invitation', envelope_(20, 100, 120, 80) + G(R(0, 0, 80, 100, '#ffffff', 4) + R(0, 0, 80, 100, 'none', 4, 'stroke="#d9a33a" stroke-width="3"') + heart(40, 34, 12) + ''.join(L(16, 60 + k * 10, 64, 60 + k * 10, '#a7adb1', 2) for k in range(3)), 'translate(96,30) rotate(10)'))
S_('engaged', R(60, 110, 80, 60, '#c0283a', 8) + Pa('M60,110 L60,80 Q100,60 140,80 L140,110 Z', '#a01e30') + R(64, 100, 72, 14, '#f6efe0', 4) + ring_jewel(100, 92, 1.0) + St('M150,40 l8,-8 M164,52 l10,-2 M140,30 l0,-10', '#f3c234', 3))
S_('congratulations', confetti(7, 30, (10, 10, 180, 100)) + Pa('M60,190 L100,110 L140,190 Z', '#ef8fa4') + ''.join(flower(76 + k * 16, 100 - (k % 2) * 14, 1.2, ['#e2463b', '#f3c234', '#ffffff', '#ef8fa4'][k]) for k in range(4)) + thumbs_up(40, 150, 1.2) + thumbs_up(160, 150, 1.2))
# funeral 葬礼：白菊花和黑丝带，蜡烛
S_('funeral', R(0, 0, 200, 200, '#e6e6e6') + ''.join(daisy(50 + k * 50, 80 + (k % 2) * 16, 34, '#ffffff', '#f3d058', 14) if False else '' for k in range(3)) + ''.join(''.join(E(x + 14 * math.cos(a) * .6, y + 14 * math.sin(a) * .6, 10, 3.5, '#ffffff', f'transform="rotate({math.degrees(a):.0f} {x+14*math.cos(a)*.6:.1f} {y+14*math.sin(a)*.6:.1f})"') for a in [k * math.pi / 8 for k in range(16)]) + Ci(x, y, 5, '#f3e070') for x, y in [(60, 80), (100, 70), (140, 80)]) + ''.join(St(f'M{x},90 L100,150', '#5a8a3a', 3) for x in (60, 100, 140)) + Pa('M80,150 L120,150 L130,190 L70,190 Z', '#2f3437') + R(160, 140, 14, 46, '#f6efe0', 2) + Pa('M167,124 Q173,134 167,140 Q161,134 167,124 Z', '#f3c234'), False)
S_('divorced', fig(50, 190, 'woman', s=.9) + fig(150, 190, 'man', s=.9) + G(heart(0, 0, 30, '#e2463b') + Pa('M0,-14 L-6,0 L4,8 L-2,24', 'none', 'stroke="#f6efe0" stroke-width="4"'), 'translate(100,60)') + St('M80,140 L120,140', '#a7adb1', 0))

# ================= 怀孕与童年 =================
S_('baby', baby_(100, 110, 2.2))
S_('child', fig(100, 190, 'boy', s=1.4, arms='wave'))
S_('toy', teddy(60, 120, 1.1) + car_side(140, 170, '#e2463b', .5) + G(R(-16, -16, 32, 32, '#f3c234', 3) + T(0, 8, 'A', 20, '#e2463b', 900), 'translate(150,90)') + Ci(120, 60, 14, '#5aa1d4'))
S_('bottle', G(R(-24, -40, 48, 90, '#f6f6f2', 10, 'opacity=".95"') + R(-24, 0, 48, 50, '#ffffff', 8) + ''.join(L(-24, -20 + k * 14, -14, -20 + k * 14, '#a7adb1', 2) for k in range(5)) + R(-26, -54, 52, 16, '#9fd0ec', 4) + Pa('M-12,-54 Q-12,-80 0,-84 Q12,-80 12,-54 Z', '#f2c890'), 'translate(100,116) rotate(-15)'))
S_('pregnant', person(100, 190, shirt='#ef8fa4', pants='#5d6469', style='long', hair='#5a3a2a', arms='front') + E(110, 104, 22, 24, '#ef8fa4') + heart(122, 92, 7))
S_('twins', baby_(64, 110, 1.4, '#9fd0ec') + baby_(136, 110, 1.4, '#ef8fa4') + T(100, 180, '×2', 0, '#000'))
S_('crib', R(20, 70, 160, 10, '#ffffff', 4) + R(20, 150, 160, 12, '#ffffff', 4) + ''.join(R(24 + k * 16, 78, 6, 74, '#ffffff', 3) for k in range(10)) + R(16, 40, 10, 140, '#f2efe8', 4) + R(174, 40, 10, 140, '#f2efe8', 4) + R(30, 130, 140, 20, '#9fd0ec', 6) + Ci(70, 124, 12, SK) + R(84, 118, 70, 16, '#ef8fa4', 8) + G(''.join(St(f'M{-20+k*20},0 L{-20+k*20},16', '#a7adb1', 1.5) + Ci(-20 + k * 20, 20, 5, ['#e2463b', '#f3c234', '#5aa1d4'][k]) for k in range(3)) + L(-24, 0, 24, 0, '#a7adb1', 2), 'translate(100,20)'))
S_('diaper', Pa('M30,70 L170,70 L150,110 Q120,120 110,170 L90,170 Q80,120 50,110 Z', '#ffffff') + Pa('M30,70 L170,70 L168,80 L32,80 Z', '#9fd0ec') + R(34, 82, 20, 14, '#f3c234', 3) + R(146, 82, 20, 14, '#f3c234', 3) + ''.join(star(70 + k * 30, 110 - (k % 2) * 10, 5, '#9fd0ec') for k in range(3)))
S_('stroller', Pa('M50,120 Q50,60 110,60 L110,120 Z', '#3c7fc1') + R(50, 110, 110, 30, '#5aa1d4', 10) + St('M160,120 L180,60 L194,60', '#2f3437', 5) + wheel(70, 160, 16) + wheel(146, 160, 16) + L(70, 140, 70, 150, '#2f3437', 4) + L(146, 140, 146, 150, '#2f3437', 4) + Ci(120, 106, 10, SK))
S_('teddy-bear', teddy(100, 110, 2.0) + R(84, 112, 32, 8, '#e2463b', 3))
S_('pacifier', G(E(0, 20, 34, 22, '#9fd0ec') + Ci(0, 54, 20, 'none', 'stroke="#5aa1d4" stroke-width="6"') + Pa('M-12,0 Q-14,-40 0,-44 Q14,-40 12,0 Z', '#f2c890') + Ci(0, 22, 8, '#5aa1d4'), 'translate(100,90) rotate(20)'))
S_('bib', Pa('M60,60 Q60,40 80,40 Q100,70 120,40 Q140,40 140,60 L156,150 Q100,180 44,150 Z', '#f3c234') + Pa('M80,40 Q100,70 120,40 Q100,58 80,40 Z', '#ffffff') + E(100, 120, 24, 22, '#ffffff') + Ci(92, 116, 3, '#2f3437') + Ci(108, 116, 3, '#2f3437') + St('M92,126 q8,6 16,0', '#e2463b', 2) + St('M60,46 Q40,30 50,20 M140,46 Q160,30 150,20', '#f3c234', 4))
S_('crawl', R(0, 160, 200, 40, '#c8a070') + pose((140, 106), (124, 116), (84, 124), arms=[[(124, 120), (130, 150), (134, 160)]], legs=[[(84, 128), (76, 160), (56, 162)]], back_arm=[[(118, 120), (120, 150), (122, 160)]], back_leg=[[(88, 128), (90, 160), (70, 162)]], shirt='#9fd0ec', pants='#9fd0ec', hr=14, tw=26, lw=12, aw=9, shoes=SK) + teddy(40, 140, .5))
S_('toddler', fig(100, 190, 'girl', s=1.05, arms='wave') + E(100, 196, 0, 0, '#000') + St('M60,150 l-10,0 M60,160 l-14,0', '#a7adb1', 0) + teddy(150, 170, .5))
S_('babysitter', fig(70, 190, 'youngwoman', arms='front') + baby_(76, 100, .7) + fig(150, 190, 'boy') + St('M90,120 L134,138', SK, 0))
S_('kindergarten', sky_ground(170, '#8cc06a') + R(30, 80, 140, 90, '#f6e2c8') + Pa('M24,84 L100,40 L176,84 Z', '#5aa1d4') + ''.join(R(40 + k * 38, 100, 24, 24, ['#e2463b', '#f3c234', '#5ba644'][k], 3) for k in range(3)) + R(86, 130, 28, 40, '#e2463b') + G(R(-10, -10, 20, 20, '#e2463b') + R(14, -10, 20, 20, '#f3c234') + R(2, -32, 20, 20, '#5aa1d4'), 'translate(150,150)') + fig(46, 196, 'boy', s=.5) + fig(70, 196, 'girl', s=.5), False)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
