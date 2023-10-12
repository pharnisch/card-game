from PIL import Image, ImageDraw, ImageFont
import os

from image_utils import ImageText

def text_on_img(filename='01.png', text="Hello", size=12):
	"Draw a text on an Image, saves it, show it"
	font = ImageFont.truetype("WernickeSchwabacher.ttf", 16)
	font_main = ImageFont.truetype('arial.ttf', 12)
	font = ImageFont.truetype('arial.ttf', 10)
	font_name = 'arial.ttf'

	neutralColorA = (66,66,66)

	x_mid = 240/2

	info_start = 5
	info_end = 24
	name_start = 25
	name_end = 49
	instant_start = 185
	instant_end = 257
	instant_mid = instant_start + (instant_end-instant_start)/2
	instant_third = instant_start + (instant_end-instant_start)/3
	instant_two_third = instant_start + 2 * (instant_end - instant_start) / 3
	epoch_start = 258
	epoch_end = 331
	epoch_mid = epoch_start + (epoch_end-epoch_start)/2
	epoch_third = epoch_start + (epoch_end-epoch_start)/3
	epoch_two_third = epoch_start + 2 * (epoch_end - epoch_start) / 3

	# create image
	#image = Image.new(mode = "RGB", size = (240,336), color = "white")
	image = Image.open(r"assets/c.jpg")
	image = image.convert("RGBA")
	d = image.getdata()
	new_image = []
	for item in d:
		r = item[0]
		g = item[1]
		b = item[2]
		a = item[3]

		total = r+g+b
		change = round(total/40)

		new_image.append((r-2*change,g+1*change,b+1*change,a))
	image.putdata(new_image)
	draw = ImageDraw.Draw(image, mode="RGBA")
	# draw text
	draw.text((10, 8), "Level 2-3", font=font, fill=neutralColorA)
	draw.line(xy=[(60, 0), (60, 25)], fill=neutralColorA, width=1)
	draw.text((65, 8), "Person | <Goblin>", font=font, fill=neutralColorA)
	draw.text((10,33), "Goblin-Journalist: Verleumdung", font=font_main, fill=neutralColorA)

	draw.line(xy=[(0,0), (image.width, 0), (image.width, image.height), (0, image.height), (0,0)], fill=neutralColorA, width=10)
	draw.line(xy=[(0,25), (image.width, 25)], fill=neutralColorA, width=1)
	draw.line(xy=[(0,50), (image.width, 50)], fill=neutralColorA, width=1)
	draw.line(xy=[(0,185), (image.width, 185)], fill=neutralColorA, width=1)
	draw.line(xy=[(0, 258), (image.width, 258)], fill=neutralColorA, width=1)

	#durchstreichen
	#draw.line(xy=[(0, epoch_start), (image.width, epoch_end)], fill=neutralColorA, width=1)
	#draw.line(xy=[(0, epoch_end), (image.width, epoch_start)], fill=neutralColorA, width=1)

	overlay = Image.new('RGBA', image.size, (0,0,0,0))
	draw_overlay = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.
	draw_overlay.rectangle([(7, name_start+3), (image.width-7, name_end-2)], fill=(60,60,60,30))
	draw_overlay.rectangle([(0, epoch_start), (image.width, epoch_end)], fill=(60,60,60,60))

	# Alpha composite these two images together to obtain the desired result.
	image = Image.alpha_composite(image, overlay)
	image = image.convert("RGB")
	draw = ImageDraw.Draw(image)


	#message = "- 1"
	#_, _, w, h = draw.textbbox((0, 0), message, font=font)
	#draw.multiline_text((x_mid-w/2, instant_third-h/2), message, font=font, fill=neutralColorA)
	#draw.rectangle([(x_mid-w/2+w, instant_third-h/2+2),(x_mid-w/2+w+h, instant_third-h/2+h+2)], fill="yellow")
	#message = ", - 2"
	#_, _, w2, h2 = draw.textbbox((0, 0), message, font=font)
	#draw.multiline_text((x_mid - w / 2 + w + h+2, instant_third - h / 2 ), message, font=font, fill=neutralColorA)

	message = "2 HP"
	left, top, w, h = draw.textbbox((0, 0), message, font=font)
	draw.multiline_text((x_mid-w/2, instant_start+9-h/2), message, font=font, fill=(80,160,80))
	draw.rectangle([(x_mid-w/2-1, instant_start+9-h/2), (x_mid-w/2+w+2, instant_start+11-h/2+h)], outline=(80,160,80))

	message = "-1 Silber, -1 Worker"
	_, _, w, h = draw.textbbox((0, 0), message, font=font)
	draw.multiline_text((x_mid-w/2, instant_third-h/2), message, font=font, fill=neutralColorA)

	message = "+1 Silber"
	_, _, w, h = draw.textbbox((0, 0), message, font=font)
	draw.multiline_text((x_mid-w/2, instant_mid-h/2), message, font=font, fill=(255,50,50))

	message = "Zerstöre eine oberste Karte mit Typ: Person.\nasfdsfdsdfsdf"
	_, _, w, h = draw.textbbox((0, 0), message, font=font)
	print(w)
	#draw.multiline_text((x_mid-w/2, instant_two_third-h/2), message, font=font, fill=neutralColorA, anchor="mm")
	draw.multiline_text((x_mid, instant_two_third), message, font=font, fill=neutralColorA, anchor="mm")


	# ADD NEW LAYER OF TEXT
	img2 = ImageText((240, 336), mode="RGBA", background=(0, 0, 0, 30))
	img2.fill_text_box((120, epoch_mid), "asfjsd", box_width=200, box_height=50, font_filename=font_name)
	overlay = img2.image
	image = image.convert("RGBA")
	image = Image.alpha_composite(image, overlay)
	image = image.convert("RGB")



	im2 = Image.open('assets/goblin.png')
	#im2.resize((4,4))
	im2.thumbnail((232,232), Image.Resampling.LANCZOS)
	im2 = im2.crop((0,49,im2.width-1,im2.height-49))
	image = image.copy()
	image.paste(im2, (5, 51))





	# save file
	image.save(filename)
	# show file
	os.system(filename)


text_on_img(text="Text", size=52)
