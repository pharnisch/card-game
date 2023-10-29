from PIL import Image, ImageDraw, ImageFont
import os

from image_utils import ImageText


def text_on_img(filename='01.png', text="Hello", size=12):
    "Draw a text on an Image, saves it, show it"


    neutralColorA = (66, 66, 66)

    x_mid = 240 / 2

    info_start = 5
    info_end = 24
    name_start = 25
    name_end = 49
    instant_start = 185
    instant_end = 257
    instant_mid = instant_start + (instant_end - instant_start) / 2
    instant_third = instant_start + (instant_end - instant_start) / 3
    instant_two_third = instant_start + 2 * (instant_end - instant_start) / 3
    epoch_start = 258
    epoch_end = 331
    epoch_mid = epoch_start + (epoch_end - epoch_start) / 2
    epoch_third = epoch_start + (epoch_end - epoch_start) / 3
    epoch_two_third = epoch_start + 2 * (epoch_end - epoch_start) / 3


    ORIGINAL_WIDTH = 240
    ORIGINAL_HEIGHT = 336
    UP_SCALE_FACTOR = 7

    font = ImageFont.truetype("WernickeSchwabacher.ttf", 16*UP_SCALE_FACTOR)
    font_main = ImageFont.truetype('arial.ttf', 12*UP_SCALE_FACTOR)
    font = ImageFont.truetype('arial.ttf', 10*UP_SCALE_FACTOR)
    font_name = 'arial.ttf'

    # create image
    # image = Image.new(mode = "RGB", size = (240,336), color = "white")
    image = Image.open(r"assets/c.jpg")

    image = Image.new("RGB", (ORIGINAL_WIDTH*UP_SCALE_FACTOR, ORIGINAL_HEIGHT*UP_SCALE_FACTOR), "white")

    draw = ImageDraw.Draw(image)
    # draw text
    draw.text((10*UP_SCALE_FACTOR, 8*UP_SCALE_FACTOR), "Level 2-3", font=font, fill=neutralColorA)
    draw.line(xy=[(60*UP_SCALE_FACTOR, 0), (60*UP_SCALE_FACTOR, 25*UP_SCALE_FACTOR)], fill=neutralColorA, width=1*UP_SCALE_FACTOR)
    draw.text((65*UP_SCALE_FACTOR, 8*UP_SCALE_FACTOR), "Person | <Goblin>", font=font, fill=neutralColorA)
    draw.text((10*UP_SCALE_FACTOR, 33*UP_SCALE_FACTOR), "Goblin-Journalist: Verleumdung", font=font_main, fill=neutralColorA)

    draw.line(xy=[(0, 0), (image.width, 0), (image.width, image.height), (0, image.height), (0, 0)], fill=neutralColorA,
              width=10*UP_SCALE_FACTOR)
    draw.line(xy=[(0, 25*UP_SCALE_FACTOR), (image.width, 25*UP_SCALE_FACTOR)], fill=neutralColorA, width=1*UP_SCALE_FACTOR)
    draw.line(xy=[(0, 50*UP_SCALE_FACTOR), (image.width, 50*UP_SCALE_FACTOR)], fill=neutralColorA, width=1*UP_SCALE_FACTOR)
    draw.line(xy=[(0, 185*UP_SCALE_FACTOR), (image.width, 185*UP_SCALE_FACTOR)], fill=neutralColorA, width=1*UP_SCALE_FACTOR)
    draw.line(xy=[(0, 258*UP_SCALE_FACTOR), (image.width, 258*UP_SCALE_FACTOR)], fill=neutralColorA, width=1*UP_SCALE_FACTOR)


    # ADD NEW LAYER OF TEXT
    img2 = ImageText((240*UP_SCALE_FACTOR, 336*UP_SCALE_FACTOR), mode="RGBA", background=(0, 0, 0, 30), maximum_font_size=30*UP_SCALE_FACTOR)
    img2.image.convert("PA")
    img2.fill_text_box((120*UP_SCALE_FACTOR-1, epoch_mid*UP_SCALE_FACTOR-1), "asf asf  sadf as sdf fh fdjdfg khgjlghj lll hjjj jjjjjjjjjjf gh  jff gjf f gjfhd fa dfs ad fds d f  fffffffffffs  asdjsd", box_width=200*UP_SCALE_FACTOR, box_height=20*UP_SCALE_FACTOR, font_filename=font_name)
    img2.write_text((120*UP_SCALE_FACTOR, 100*UP_SCALE_FACTOR), 'test fsfa  fdsffffffffffffffffffffff as         sadf adfasd ill', font_filename=font_name,
                   font_size='fill', max_width=200*UP_SCALE_FACTOR, max_height=20*UP_SCALE_FACTOR, color=neutralColorA)
    overlay = img2.image
    overlay.convert("RGBA")
    image = image.convert("RGBA")
    image = Image.alpha_composite(image, overlay)
    image = image.convert("RGB")

    image = image.resize((ORIGINAL_WIDTH, ORIGINAL_HEIGHT), resample=Image.Resampling.LANCZOS) # antialias?
    print(image.size)
    # save file
    image.save(filename)
    # show file
    os.system(filename)

text_on_img(text="Text", size=52)
