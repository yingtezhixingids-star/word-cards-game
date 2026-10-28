# 生成两个版本的图标：python3 mkicon2.py en|ja 输出目录
from PIL import Image, ImageDraw, ImageFont
import sys, os
ed, outdir = sys.argv[1], sys.argv[2]
F = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
def icon(size, path):
    S = 4; W = size * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, W - 1, W - 1], radius=int(W * .22), fill=(38, 37, 34, 255) if ed == 'en' else (44, 30, 34, 255))
    def card(x, y, w, h, angle, band, txt, font):
        c = Image.new('RGBA', (w, h), (0, 0, 0, 0)); cd = ImageDraw.Draw(c)
        cd.rounded_rectangle([0, 0, w - 1, h - 1], radius=int(w * .08), fill=(236, 226, 200, 255), outline=(180, 164, 121, 255), width=max(2, w // 40))
        cd.rounded_rectangle([int(w * .08), int(h * .08), int(w * .92), int(h * .30)], radius=int(w * .04), fill=band)
        tw = cd.textbbox((0, 0), txt, font=font); cd.text(((w - (tw[2] - tw[0])) / 2 - tw[0], h * .48 - tw[1]), txt, font=font, fill=(43, 42, 37, 255))
        c = c.rotate(angle, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(c, (int(x - c.width / 2), int(y - c.height / 2)))
    fz = ImageFont.truetype(F, int(W * .20), index=0); fe = ImageFont.truetype(F, int(W * .22), index=0)
    card(W * .38, W * .52, int(W * .42), int(W * .60), 12, (91, 107, 58, 255), '词', fz)
    if ed == 'en': card(W * .62, W * .50, int(W * .42), int(W * .60), -8, (217, 169, 59, 255), 'A', fe)
    else: card(W * .62, W * .50, int(W * .42), int(W * .60), -8, (196, 48, 58, 255), 'あ', fe)
    im = im.resize((size, size), Image.LANCZOS); im.save(path)
for name, sz in [('mdpi', 48), ('hdpi', 72), ('xhdpi', 96), ('xxhdpi', 144), ('xxxhdpi', 192)]:
    os.makedirs(f'{outdir}/mipmap-{name}', exist_ok=True); icon(sz, f'{outdir}/mipmap-{name}/ic_launcher.png')
icon(512, f'{outdir}/../icon-{ed}.png')
