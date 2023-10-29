import json
from PIL import Image, ImageDraw, ImageFont
import os
from image_utils import ImageText


class Card:
    def __init__(self, idx, data):
        self.data = data

        self.file_name = f"../cards/{idx}.png"

        self.font_name = 'arial.ttf'
        self.font_main_name = 'arial.ttf'
        self.font_main = ImageFont.truetype(self.font_main_name, 12)
        self.font = ImageFont.truetype(self.font_name, 10)
        self.neutralColorA = (66, 66, 66)

        #########################

        image = Image.open(r"../../assets/c.jpg")

        image = self.change_color(image)

        self.draw_lines(image)

        image = self.draw_main_stats(image)

        image = self.add_image(image)

        text_layer = self.get_text_layer()
        image = Image.alpha_composite(image, text_layer)

        image = self.add_special_info(image)

        #########################

        image.save(self.file_name)
        #os.system(self.file_name) # show file

    def add_special_info(self, image):
        if self.data["equipment_slot"] == True and self.data["spell_slot"] == True:
            image = self.add_text(image, f"(Slot: Ausrüstung o. Zauber)", 120, 60, 200, 12)
        elif self.data["spell_slot"] == True:
            image = self.add_text(image, f"(Slot: Zauber)", 120, 60, 200, 12)
        elif self.data["equipment_slot"] == True:
            image = self.add_text(image, f"(Slot: Ausrüstung)", 120, 60, 200, 12)
        return image

    def get_text_layer(self):
        img2 = ImageText((240, 336), mode="RGBA", background=(0, 0, 0, 30), maximum_font_size=16)
        img2.image.convert("PA")
        img2.fill_text_box((120, 20), self.data["name"], box_width=180, box_height=40, font_filename=self.font_name)
        overlay = img2.image
        overlay.convert("RGBA")
        return overlay

    def add_text(self, image, text, centerX, centerY, width, height):
        img2 = ImageText((240, 336), mode="RGBA", background=(0, 0, 0, 30), maximum_font_size=16)
        img2.image.convert("PA")
        img2.fill_text_box((centerX, centerY), text, box_width=width, box_height=height, font_filename=self.font_name)
        overlay = img2.image
        overlay.convert("RGBA")
        image = Image.alpha_composite(image, overlay)
        return image

    def add_image(self, image):
        im2 = Image.open('../../assets/goblin.png')

        #im2.thumbnail((232, 232), Image.Resampling.LANCZOS)
        #im2 = im2.crop((0, 49, im2.width - 1, im2.height - 49))

        im2.thumbnail((232, 232), Image.Resampling.LANCZOS)
        #im2 = im2.crop((0, 49, im2.width - 1, im2.height - 49))

        image = image.copy()
        image.paste(im2, (5, 336-232-28))
        return image

    def draw_lines(self, image):
        draw = ImageDraw.Draw(image, mode="RGBA")
        # draw text
        draw.text((10, 20), f"{self.data['cost_silver']} S", font=self.font, fill=self.neutralColorA)
        if self.data['victory_points'] > 0:
            draw.text((image.width-30, 20), f"{self.data['victory_points']} VP", font=self.font, fill=self.neutralColorA)

        draw.line(xy=[(0, 0), (image.width, 0), (image.width, image.height), (0, image.height), (0, 0)],
                  fill=self.neutralColorA, width=10)
        #draw.line(xy=[(0, 25), (image.width, 25)], fill=self.neutralColorA, width=1)
        #draw.line(xy=[(0, 50), (image.width, 50)], fill=self.neutralColorA, width=1)
        draw.line(xy=[(0, 336-232-28-2), (image.width, 336-232-28-2)], fill=self.neutralColorA, width=2)
        #draw.line(xy=[(0, 185), (image.width, 185)], fill=self.neutralColorA, width=1)
        draw.line(xy=[(0, 310), (image.width, 310)], fill=self.neutralColorA, width=5)

    def draw_main_stats(self, image):
        draw = ImageDraw.Draw(image, mode="RGBA")
        draw.line(xy=[(61, 310), (61, 336)], fill=self.neutralColorA, width=6)
        draw.line(xy=[(120, 310), (120, 336)], fill=self.neutralColorA, width=6)
        draw.line(xy=[(179, 310), (179, 336)], fill=self.neutralColorA, width=6)

        helligkeit = 200
        draw.rectangle([(5, 313), (58, 331)], fill=(255,255,helligkeit))
        draw.rectangle([(64, 313), (117, 331)], fill=(255, helligkeit, helligkeit))
        draw.rectangle([(123, 313), (176, 331)], fill=(helligkeit, helligkeit, 255))
        draw.rectangle([(182, 313), (235, 331)], fill=(helligkeit, 255, helligkeit))
        # total_width = 240 - 5*5 = 215, 215/4= 53,75

        image = self.add_text(image, f"{self.data['initiative']} INIT", 31, 323, 50, 16)
        image = self.add_text(image, f"{self.data['attack']} ATK", 89, 323, 50, 16)
        image = self.add_text(image, f"{self.data['defense']} DEF", 151, 323, 50, 16)
        image = self.add_text(image, f"{self.data['health_points']} HP", 209, 323, 50, 16)

        return image

    def change_color(self, image):
        image = image.convert("RGBA")
        d = image.getdata()
        new_image = []
        for idx, item in enumerate(d):
            r = item[0]
            g = item[1]
            b = item[2]
            a = item[3]
            total = r + g + b
            change = round(total / 40)

            tmp = idx % 240

            if self.data["equipment_slot"] == True and self.data["spell_slot"] == True:
                if tmp < 120:
                    new_image.append((r - 5 * change, g + 2 * change, b + 3 * change, a))
                else:
                    new_image.append((r + 2 * change, g, b + 5 * change, a))
            elif self.data["spell_slot"] == True:
                new_image.append((r + 2 * change, g, b + 5 * change, a))
            elif self.data["equipment_slot"] == True:
                new_image.append((r - 5 * change, g + 2 * change, b + 3 * change, a))
            else:
                new_image.append((r, g, b, a))
        image.putdata(new_image)
        return image


with open("../card_data/creatures", "r") as f:
    content = f.read()
    content = json.loads(content)
    for idx, card_data in enumerate(content):
        card = Card(idx, card_data)