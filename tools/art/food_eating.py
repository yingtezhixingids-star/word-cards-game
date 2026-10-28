from flat import *
from fig import *
import os, sys

A = {}
SK = P['skin']; SKD = shade(SK, -.12)

def noodles_bowl(cx, cy, w):
    g = bowl(cx, cy, w, fill='#f3d58a')
    g += ''.join(St(f'M{cx-w*.35+i*w*.12},{cy-2} q{w*.05},{-4} {w*.1},0', '#f6e2a8', 2) for i in range(6))
    g += Ci(cx + w * .2, cy - 3, w * .07, '#5ba644') + E(cx - w * .15, cy - 3, w * .08, w * .04, '#e0915a')
    return g

# eat 吃：一手端碗，一手用筷子夹面条往嘴里送
cx, cy, r = 92, 70, 30
g = diner(cx, cy, r, '#3c7fc1', mood := None) if False else diner(cx, cy, r, '#3c7fc1', '#3a2a20', 'short', 'up', 'o')
g += noodles_bowl(cx + 4, cy + r * 2.0, 70)
g += arm([(cx - r * 1.6, 200), (cx - r * 1.7, cy + r * 2.6), (cx - r * .9, cy + r * 2.5)], shade('#3c7fc1', -.2), SK, 15)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.0, cy + r * 1.8), (cx + r * 1.3, cy + r * 1.1)], shade('#3c7fc1', -.2), SK, 15)
g += chopsticks(cx + r * 1.4, cy + r * 1.1, cx + r * .1, cy + r * .6, '#8a5a35', 5)
g += St(f'M{cx+r*.15},{cy+r*.6} q2,14 -2,30 M{cx+r*.25},{cy+r*.62} q4,14 2,30 M{cx+r*.05},{cy+r*.6} q-2,12 -4,28', '#f3d58a', 2.5)
A['eat'] = svg(g)

# drink 喝：举杯喝水
cx, cy, r = 92, 76, 32
g = diner(cx, cy, r, '#5ba644', '#3a2a20', 'long', 'closed', '')
g += G(Pa('M-14,-26 L14,-26 L11,26 L-11,26 Z', '#dff1fb', 'opacity=".95"') + Pa('M-12,-10 L13,-10 L11,26 L-11,26 Z', '#9fd0ec') + R(-9, -22, 4, 44, '#ffffff', 2, 'opacity=".7"'), f'translate({cx+r*.75},{cy+r*.35}) rotate(-35)')
g += arm([(cx + r * 1.6, 200), (cx + r * 2.1, cy + r * 1.6), (cx + r * 1.3, cy + r * .9)], shade('#5ba644', -.2), SK, 15)
A['drink'] = svg(g)

# hungry 饿：捂着肚子、空碗，脑子里想着鸡腿
cx, cy, r = 76, 86, 30
g = diner(cx, cy, r, '#f08a24', '#3a2a20', 'short', 'dot', 'o', 'sad')
g += arm([(cx - r * 1.5, 200), (cx - r * 1.2, cy + r * 2.6), (cx + r * .3, cy + r * 2.7)], shade('#f08a24', -.2), SK, 15)
g += St(f'M{cx+r*.6},{cy+r*2.6} q8,-4 12,4 M{cx+r*.9},{cy+r*2.9} q10,-2 12,6', '#2f3437', 2)
g += bubble(150, 46, 72, 56, (112, 84)) + G(Pa('M-30,-14 Q-40,-32 -18,-34 Q4,-34 16,-14 Q24,0 12,10 Q-6,18 -20,6 Q-28,0 -30,-14 Z', '#c97a3a') + R(10, 4, 26, 8, '#f6efe0', 4, 'transform="rotate(35 10 4)"') + Ci(34, 24, 6, '#f6efe0') + Ci(28, 28, 6, '#f6efe0'), 'translate(146,46) scale(.75)')
g += G(bowl(0, 0, 50, fill='#f4f6f7'), 'translate(158,150)')
A['hungry'] = svg(g)

# thirsty 渴：大太阳下吐舌头流汗，想着一杯水
cx, cy, r = 76, 90, 30
g = Ci(30, 30, 16, '#f3c234') + ''.join(L(30 + 20 * math.cos(a * math.pi / 4), 30 + 20 * math.sin(a * math.pi / 4), 30 + 27 * math.cos(a * math.pi / 4), 30 + 27 * math.sin(a * math.pi / 4), '#f3c234', 3) for a in range(8))
g += diner(cx, cy, r, '#ef8fa4', '#5a3a2a', 'long', 'closed', 'o', 'sad', '#ef7a7a')
g += E(cx, cy + r * .75, 6, 9, '#ef6a7a')
g += drop(cx - r * 1.05, cy - r * .4, 6) + drop(cx + r * 1.05, cy - r * .2, 5) + drop(cx + r * .8, cy - r * 1.0, 5)
g += bubble(150, 50, 64, 64, (112, 86)) + Pa('M136,30 L164,30 L160,70 L140,70 Z', '#dff1fb') + Pa('M137,42 L163,42 L160,70 L140,70 Z', '#9fd0ec')
A['thirsty'] = svg(g)

# full 饱：吃饱了，摸着圆鼓鼓的肚子，面前空盘子
cx, cy, r = 92, 58, 28
g = diner(cx, cy, r, '#5aa1d4', P['grey'], 'grey', 'up', 'smile', None, '#ef9a8a', w=r * 3.8)
g += E(cx, cy + r * 3.5, r * 2.35, r * 1.5, shade('#5aa1d4', -.08)) + E(cx - 3, cy + r * 3.45, r * 2.25, r * 1.42, '#5aa1d4') + E(cx - r * .5, cy + r * 3.2, r * .6, r * .4, shade('#5aa1d4', .25))
sl = shade('#5aa1d4', -.2)
g += arm([(cx - r * 1.8, cy + r * 1.6), (cx - r * 2.1, cy + r * 2.8), (cx - r * .6, cy + r * 3.6)], sl, SK, 14)
g += arm([(cx + r * 1.8, cy + r * 1.6), (cx + r * 2.1, cy + r * 2.8), (cx + r * .7, cy + r * 3.4)], sl, SK, 14)
g += G(E(0, 4, 26, 8, '#d9dcde') + E(0, 0, 26, 8, '#ffffff') + E(0, 0, 17, 4.5, '#f4f6f7') + L(-6, -2, 26, -12, '#c4cbd0', 2.5) + L(-2, 0, 28, -6, '#c4cbd0', 2.5), 'translate(164,176)')
g += T(150, 40, '~', 24, '#7a8a94', 800) + T(36, 40, '~', 20, '#7a8a94', 800)
A['full'] = svg(g, shadow=False)

# delicious 好吃：闭眼陶醉，竖大拇指，面前一盘菜冒着香气
cx, cy, r = 84, 72, 30
g = diner(cx, cy, r, '#d9453a', P['grey'], 'grey', 'up', 'smile', None, '#ef9a8a')
g += Pa(f'M{cx-r*.3},{cy+r*.42} Q{cx},{cy+r*.8} {cx+r*.3},{cy+r*.42} Z', '#9a3a30')
g += G(E(0, 6, 46, 14, '#d9dcde') + E(0, 0, 46, 14, '#ffffff') + E(0, -4, 32, 8, '#e0915a') + E(-10, -8, 10, 6, '#c96a3a') + E(12, -6, 10, 6, '#c96a3a') + Ci(0, -10, 4, '#5ba644'), f'translate({cx},{cy+r*3.0})')
g += steam(cx - 14, cy + r * 2.6, 3, 14, '#e2b08a', .6)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.3, cy + r * 1.8), (cx + r * 2.5, cy + r * .9)], shade('#d9453a', -.2), SK, 15, hand=False)
g += thumbs_up(cx + r * 2.5, cy + r * .7, 1.0)
g += star(160, 30, 8) + star(178, 54, 5)
A['delicious'] = svg(g)

# sweet 甜：滴着蜂蜜的蜂蜜罐和一块草莓奶油蛋糕
g = Pa('M30,90 Q26,170 70,172 Q114,170 110,90 Z', '#f0b030') + R(34, 76, 72, 18, '#c58b54', 4) + R(30, 70, 80, 10, '#a06a40', 4)
g += Pa('M34,94 q8,22 16,0 q8,30 18,0 q8,18 16,0 q8,26 18,0 Z', '#e09a20') + hi(48, 120, 6, 16, .45)
g += St('M98,66 L130,30', '#c58b54', 5) + Pa('M126,30 q8,-14 16,-6 q6,10 -6,14 Z', '#e0b040') + drop(126, 54, 7, '#f0b030')
g += Pa('M112,170 L112,128 L182,112 L182,156 Z', '#f6e2c0') + Pa('M112,128 L182,112 L182,124 L112,140 Z', '#ffffff') + Pa('M112,150 L182,136 L182,142 L112,156 Z', '#ef8fa4')
g += Pa('M112,128 L150,100 L182,112 Z', '#ffffff') + Ci(150, 104, 8, '#d9453a') + leaf(150, 97, 8, 3, -90, '#5ba644')
A['sweet'] = svg(g)

# sour 酸：咬了一口柠檬，酸得眯眼噘嘴
cx, cy, r = 84, 84, 32
g = diner(cx, cy, r, '#f3c234', '#3a2a20', 'short', 'shut', 'o', None)
g += St(f'M{cx-r*1.3},{cy-r*.6} l-8,-6 M{cx+r*1.3},{cy-r*.6} l8,-6 M{cx-r*1.35},{cy-r*.1} l-10,0 M{cx+r*1.35},{cy-r*.1} l10,0', '#5ba644', 3)
g += arm([(cx + r * 1.6, 200), (cx + r * 2.1, cy + r * 1.8), (cx + r * 1.9, cy + r * .9)], shade('#f3c234', -.2), SK, 15)
g += G(Ci(0, 0, 22, '#f3d034') + Ci(0, 0, 18, '#fbe98a') + ''.join(L(0, 0, 17 * math.cos(a), 17 * math.sin(a), '#f3d034', 2) for a in [k * math.pi / 4 for k in range(8)]), f'translate({cx+r*2.3},{cy+r*.3})')
A['sour'] = svg(g)

# salty 咸：喝了一口汤，咸得吐舌头，旁边盐罐
cx, cy, r = 80, 80, 30
g = diner(cx, cy, r, '#7a9fc7', P['grey'], 'grey', 'shut', 'o', 'sad')
g += E(cx, cy + r * .78, 6, 9, '#ef6a7a')
g += G(bowl(0, 0, 60, fill='#e0a860'), f'translate({cx},{cy+r*2.6})') + G(R(-6, -26, 12, 30, '#c4cbd0', 3) + E(-14, -32, 10, 5, '#c4cbd0'), f'translate({cx+18},{cy+r*2.4}) rotate(30)')
g += G(R(-16, -26, 32, 50, '#eef6fa', 8) + R(-16, -8, 32, 32, '#ffffff', 6) + R(-17, -38, 34, 14, '#c4cbd0', 6) + ''.join(Ci(-8 + i * 8, -32, 1.8, '#5d6469') for i in range(3)), 'translate(160,130) rotate(-20)')
g += ''.join(R(140 + i * 7 - (i % 2) * 4, 80 + i * 6, 3, 3, '#ffffff', .5, 'stroke="#c4cbd0" stroke-width=".8"') for i in range(6))
A['salty'] = svg(g)

# spicy 辣：吃了红辣椒，脸通红嘴里冒火
cx, cy, r = 80, 90, 30
g = diner(cx, cy, r, '#5d6469', '#3a2a20', 'short', 'shut', 'o', None, '#e2463b')
g += E(cx, cy + r * .1, r * .85, r * .9, '#e2463b', 'opacity=".3"')
g += Pa(f'M{cx+r*.2},{cy+r*.55} Q{cx+r*1.2},{cy+r*.1} {cx+r*1.6},{cy+r*.8} Q{cx+r*2.2},{cy+r*.5} {cx+r*2.5},{cy+r*.9} Q{cx+r*2.0},{cy+r*1.4} {cx+r*1.4},{cy+r*1.2} Q{cx+r*.8},{cy+r*1.2} {cx+r*.2},{cy+r*.65} Z', '#f08a24')
g += Pa(f'M{cx+r*.3},{cy+r*.6} Q{cx+r*1.1},{cy+r*.4} {cx+r*1.5},{cy+r*.9} Q{cx+r*1.0},{cy+r*1.0} {cx+r*.3},{cy+r*.66} Z', '#f3c234')
g += drop(cx - r * 1.05, cy - r * .5, 6) + drop(cx + r * .2, cy - r * 1.4, 5)
g += G(Pa('M0,0 Q30,-6 44,14 Q50,30 40,40 Q36,20 6,14 Q-6,10 0,0 Z', '#d9302c') + Pa('M0,2 q-6,-10 -2,-16 q4,-2 6,6', '#3c8a3a') + hi(22, 4, 10, 3, .4, 20), 'translate(132,30)')
A['spicy'] = svg(g)

# bitter 苦：一口苦瓜，苦得皱眉
cx, cy, r = 80, 82, 30
g = diner(cx, cy, r, '#8a5a35', '#3a2a20', 'short', 'shut', 'wavy', 'sad')
g += St(f'M{cx-6},{cy-r*.5} l2,6 M{cx+6},{cy-r*.5} l-2,6', SKD, 1.8)
g += G(Pa('M-14,-48 Q8,-52 14,-30 Q22,0 14,30 Q8,50 -2,52 Q-14,40 -16,10 Q-22,-30 -14,-48 Z', '#5aa04a') +
       ''.join(E(-8 + (i % 3) * 8, -36 + i * 9, 3.5, 2.5, '#7cc06a') for i in range(9)) + Pa('M-6,-50 q4,-10 10,-8', 'none', 'stroke="#3c7a2c" stroke-width="3"'), 'translate(158,110) rotate(15)')
A['bitter'] = svg(g)

# tea 茶：紫砂茶壶和一杯热茶
g = E(84, 112, 50, 42, '#9a5a3a') + E(84, 76, 26, 8, '#8a4a2a') + Ci(84, 66, 7, '#8a4a2a')
g += Pa('M130,104 Q156,96 162,76 L168,80 Q164,108 134,122 Z', '#9a5a3a') + St('M36,96 q-22,6 -16,26 q6,14 20,10', '#8a4a2a', 7)
g += hi(66, 98, 10, 18, .25, 20) + E(84, 150, 40, 6, '#7a3a20')
g += G(cup(0, 0, 40, 26, '#ffffff', '#c98a3a', handle=False) + R(-20, 4, 40, 3, '#5aa1d4'), 'translate(152,150)') + steam(144, 140, 2, 12, '#c4cbd0', .7)
A['tea'] = svg(g)

# soup 汤：一碗热汤，勺子，冒着热气
g = bowl(100, 104, 130, fill='#e0a050', pattern='#d9453a')
g += Ci(80, 102, 8, '#5ba644', 'opacity=".9"') + E(116, 100, 10, 5, '#f08a24') + Ci(100, 106, 5, '#f6e6c0') + Ci(130, 104, 4, '#5ba644')
g += St('M136,100 L176,50', '#ffffff', 8) + E(132, 104, 16, 8, '#ffffff', 'transform="rotate(-40 132 104)"')
g += steam(80, 80, 3, 18, '#c4cbd0', 1)
A['soup'] = svg(g)

# chew 嚼：腮帮鼓鼓地慢慢嚼，下巴旁有咀嚼动作线
cx, cy, r = 96, 82, 34
g = diner(cx, cy, r, '#7fc4c0', P['grey'], 'grey', 'closed', '', None)
g += E(cx - r * .45, cy + r * .48, r * .3, r * .26, SK) + E(cx + r * .45, cy + r * .48, r * .3, r * .26, SK)
g += St(f'M{cx-r*.2},{cy+r*.55} q{r*.1},{r*.12} {r*.2},0 q{r*.1},{-r*.12} {r*.2},0', '#9a4a3a', 2.2)
for sx in (-1, 1):
    g += St(f'M{cx+sx*r*1.05},{cy+r*.55} q{sx*8},4 {sx*6},14 M{cx+sx*r*1.2},{cy+r*.4} q{sx*10},6 {sx*8},20', '#7a8a94', 2.5)
g += T(cx, cy - r * 1.4, '1·2·3', 16, '#7a8a94', 800)
A['chew'] = svg(g)

# swallow 吞咽：仰头吞药片，喉咙里向下的箭头
cx, cy, r = 92, 68, 30
g = diner(cx, cy, r, '#9a7ab8', '#3a2a20', 'long', 'closed', 'flat', None)
g += R(cx - r * .3, cy + r * .8, r * .6, r * .9, SK, 4)
g += Pa(f'M{cx-7},{cy+r*1.0} L{cx+7},{cy+r*1.0} L{cx+7},{cy+r*1.4} L{cx+13},{cy+r*1.4} L{cx},{cy+r*1.75} L{cx-13},{cy+r*1.4} L{cx-7},{cy+r*1.4} Z', '#d9453a')
g += pill(cx + r * 2.0, cy - r * .2, 30, 13, '#ffffff', '#3c7fc1', -30) + G(Pa('M-12,-22 L12,-22 L10,22 L-10,22 Z', '#dff1fb') + Pa('M-11,-6 L11,-6 L10,22 L-10,22 Z', '#9fd0ec'), f'translate({cx+r*2.1},{cy+r*2.6})')
A['swallow'] = svg(g)

# sip 小口喝：双手捧着小茶杯，轻轻抿一口
cx, cy, r = 92, 76, 32
g = diner(cx, cy, r, '#c98f5a', '#5a3a2a', 'bun', 'closed', '', None)
g += G(cup(0, 0, 30, 22, '#ffffff', '#c98a3a', handle=False) + R(-15, 4, 30, 3, '#5aa1d4'), f'translate({cx},{cy+r*.62})')
g += steam(cx - 6, cy + r * .4, 2, 12, '#c4cbd0', .5)
g += arm([(cx - r * 1.6, 200), (cx - r * 1.5, cy + r * 1.9), (cx - r * .5, cy + r * 1.3)], shade('#c98f5a', -.2), SK, 15)
g += arm([(cx + r * 1.6, 200), (cx + r * 1.5, cy + r * 1.9), (cx + r * .5, cy + r * 1.3)], shade('#c98f5a', -.2), SK, 15)
A['sip'] = svg(g)

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for k, v in A.items():
    open(os.path.join(out, k + '.svg'), 'w').write(v)
print(len(A), 'drawn')
