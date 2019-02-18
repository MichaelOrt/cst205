# warm-image-filer.py - apply a strange filter
# author: Wes Modes wmodes@csumb.edu
# date: 18 Sep 2018

# get Image class from Pillow module
from PIL import Image

# constants
# these define how much we want to change each pixel color
warm_delta_red = 30
warm_delta_green = 20
warm_delta_blue = -10
cool_delta_red = -20
cool_delta_green = -10
cool_delta_blue = 30

def fix_color(n):
    """Take an integer and make sure it isn't too high
    or too low (in the range 0 to 255). If it is, fix it."""
    # check to see if n has exceeded upper bound
    if n > 255:
        return 255
    # check to see if n has exceeded lower bound 
    if n < 0:
        return 0
    # otherwise, n is good, return it
    return n

#open image
im = Image.open("../images/bit.jpg")
width, height = im.size # returns tuple of width & height

# apply cool filter to left most 1/3
for x in range(0,int(width/3)):
    for y in range(height):
        red,green,blue = im.getpixel((x,y))
        newcolor = (fix_color(red + cool_delta_red),
                    fix_color(green + cool_delta_green),
                    fix_color(blue + cool_delta_blue))
        im.putpixel((x,y), newcolor)

# apply warm filter to right most 1/3
for x in range(2*int(width/3), width):
    for y in range(height):
        red,green,blue = im.getpixel((x,y))
        newcolor = (fix_color(red + warm_delta_red),
                    fix_color(green + warm_delta_green),
                    fix_color(blue + warm_delta_blue))
        im.putpixel((x,y), newcolor)

im.show()
