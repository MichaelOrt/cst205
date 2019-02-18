from PIL import Image # an error here means that Pillow is not installed

im = Image.open('chualar_sign.jpg')

# print(im)
print(im.size) # (1024, 768)
width, height = im.size

pic_width = 4
pic_height = 5
for x in range(pic_width): # loop from 0 to pic_width - 1
    for y in range(pic_height): # loop from 0 to pic_height - 1
        print("Coordinates:", (x,y))
        print("Pixel:", im.getpixel((x,y)))