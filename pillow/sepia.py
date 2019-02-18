"""sepia.py
Tints an image brown like an old sepia photo
author: Wes Modes
date: 12 February 2019
"""

from PIL import Image

filename = "teacher.jpg"

def sepia(p):
    """Tints shadows in brown
    Takes a pixel, returns modified pixel"""
    if p[0] < 63:
        r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
    # tint midtones1.15
    elif p[0] > 62 and p[0] < 192:
        r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
    # tint highlights
    else:
        r = int(p[0] * 1.08)
        if r > 255:
            r = 255
        g,b = p[1], int(p[2] * 0.5)
    return r, g, b

im = Image.open(filename)

new_list = map(sepia, im.getdata()) 

im.putdata(list(new_list))

im.show()