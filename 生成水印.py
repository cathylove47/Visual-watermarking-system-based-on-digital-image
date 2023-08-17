import math

from PIL import Image,ImageFont,ImageDraw
import os
from PIL import Image,ImageFont,ImageDraw
import pandas as pd

def create_watermark(text, font_path, font_size=26, opacity=100):
    # Calculate lines
    n = int(math.sqrt(len(text))) + 1
    lines = [text[i:i + n] for i in range(0, len(text), n)]
    # Create a blank image with white background
    width, height = n * font_size, n * font_size
    img = Image.new('RGBA', (width, height), (255, 255, 255))
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)
    # Set text color
    text_color = (0, 0, 0, opacity)
    # Draw text on image
    for i, line in enumerate(lines):
        # Calculate the width of the line
        text_bbox = draw.textbbox((0, 0), line, font)
        line_width = text_bbox[2] - text_bbox[0]
        # Calculate the x coordinate to center the line
        x = (width - line_width) / 2
        draw.text((x, i * font_size), line, font=font, fill=text_color)
    # Save the image
    img.save('watermark.png', 'PNG')

text = '武汉理工大学数学建模'
font_path = 'C:/Windows/Fonts/simhei.ttf'
create_watermark(text, font_path, font_size=26, opacity=100)
