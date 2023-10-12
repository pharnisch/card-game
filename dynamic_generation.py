#!/usr/bin/env python
# coding: utf-8

# You need PIL <http://www.pythonware.com/products/pil/> to run this script
# Download unifont.ttf from <http://unifoundry.com/unifont.html> (or use
# any TTF you have)
# Copyright 2011 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from image_utils import ImageText
from PIL import Image, ImageDraw, ImageFont


color = (50, 50, 50)
text = 'Python is a cool programming language. You should learn it!'
font = 'arial.ttf'
img = ImageText("./assets/c.jpg")

#write_text_box will split the text in many lines, based on box_width
#`place` can be 'left' (default), 'right', 'center' or 'justify'
#write_text_box will return (box_width, box_calculed_height) so you can
#know the size of the wrote text
#img.write_text_box((120, 50), text, box_width=200, font_filename=font,                   font_size=15, color=color)
#img.write_text_box((120, 125), text, box_width=200, font_filename=font,      font_size=15, color=color, place='right')
img.write_text_box((120, 200), text, box_width=200, font_filename=font,
                   font_size=15, color=color, place='center')
img.write_text_box((120, 275), text, box_width=200, font_filename=font,
                   font_size=15, color=color, place='justify')

#You don't need to specify text size: can specify max_width or max_height
# and tell write_text to fill the text in this space, so it'll compute font
# size automatically
#write_text will return (width, height) of the wrote text
img.write_text((120, 250), 'test fill', font_filename=font,
               font_size='fill', max_height=20, color=color)


# fill_text_box will attempt to use up all available space in both x and
# y dimensions, where the above example will only stick to one line

img2 = ImageText((240,336), mode="RGBA", background=(0,0,0,30))
img2.fill_text_box((120,200), text, box_width=200, box_height=40, font_filename=font)
overlay = img2.image


img.image = img.image.convert("RGBA")


# Alpha composite these two images together to obtain the desired result.
test = Image.alpha_composite(img.image, overlay)
test = test.convert("RGB")
test.show()



img.image.show()
img.save('sample-imagetext.png')