"""color.py
A simple class definition for defining colors and calculating color distance.

Author: Wes Modes <wmodes@csumb.edu>, Avner Biblarz <abiblarz@csumb.edu>
Date: February 2018
"""

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

class Color:
    """A slightly more complicated color class"""

    # class variables shared by all instances
    color_count = 0

    def __init__(self, name, red, green, blue):
        """initialize an instantiated class"""
        # we store these variables internally within an instantiated object
        # store the color name
        self.name = name
        # store the RGB values
        self.red = red
        self.green = green
        self.blue = blue

        # increment class variable
        Color.color_count += 1
        
    def rgb_to_lab(self):
        """convert rgb colors to lab colors"""
        color_srgb = sRGBColor(self.red, self.green, self.blue, True)
        return convert_color(color_srgb, LabColor)

    def de2000_compare(self, color2):
        """Get color distance between instantiated color object and a new color""" 
        color1_lab = self.rgb_to_lab()
        color2_lab = color2.rgb_to_lab()
        return delta_e_cie2000(color1_lab, color2_lab)

    def __str__(self):
        """Reports color name"""
        return f"Hi, I'm {self.name}."

    def __eq__(self, color2):
        """Boolean comparison of this color object and a new color"""
        return self.red == color2.red and self.green == color2.green and self.blue == color2.blue

# instantiate a new color object from Color class
my_red = Color('red', 255, 0, 0)
print(my_red)

my_other_red = Color('red2', 255, 0, 0)

# check for equality
print(f'Are {my_red.name} and {my_other_red.name} the same?')
print(my_red == my_other_red)

# create some more color objects
my_blue = Color('blue', 0, 0, 255)
my_marsala = Color('marsala', 173, 101, 95)
my_white = Color('white', 255, 255, 255)
my_black = Color('black', 0, 0, 0)

# get the distances for some of these colors
print(f'The difference between {my_red.name} and {my_blue.name} is {my_red.de2000_compare(my_blue)}')

print(f'The difference between {my_red.name} and {my_marsala.name} is {my_red.de2000_compare(my_marsala)}')

print(f'The difference between {my_white.name} and {my_black.name} is {my_white.de2000_compare(my_black)}')