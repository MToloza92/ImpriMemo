from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import logging
from app.config import font_paths

logger = logging.getLogger("ImpriMemo")

def get_font(size=24):
    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def render_text_to_image(text, width=384, size=24):
    font = get_font(size)
    spacing = 5
    if not text.strip():
        text = " "
    wrapped = []
    for line in text.split('\n'):
        wrapped.extend(textwrap.wrap(line, width=width//(size//2)))
    height = len(wrapped)*(size+spacing)+20
    img = Image.new("1", (width, height), 1)
    draw = ImageDraw.Draw(img)
    y = 10
    for line in wrapped:
        draw.text((10, y), line, font=font, fill=0)
        y += size+spacing
    return img

def image_to_printer_data(image, threshold=128):
    image = image.convert("L")
    image = image.point(lambda p: 0 if p < threshold else 255, '1')
    image = image.rotate(90, expand=True)
    w, h = image.size
    bpr = (w+7)//8
    data = bytearray()
    for y in range(h):
        for x in range(bpr):
            byte = 0
            for bit in range(8):
                px = x*8+bit
                if px < w:
                    if image.getpixel((px, y)) == 0:
                        byte |= 1 << (7-bit)
            data.append(byte)
    return bytes(data)