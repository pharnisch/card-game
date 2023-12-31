
from PIL import Image, ImageDraw, ImageFont
import os
from fpdf import FPDF

# imagelist is the list with all image filenames
images = os.listdir("../cards/new_and_not_printed_yet/")
tmp = []
for image in images:
    if "buff" in image:
        tmp.append(image)
        tmp.append(image)
        tmp.append(image)
    else:
        tmp.append(image)

images = tmp

pdf = FPDF("L", "mm", "a4")
pdf.add_page()
full_pages = 0
for _idx,  image in enumerate(images):
    if _idx != 0 and _idx % 8 == 0:
        full_pages += 1
        pdf.add_page()

    idx = _idx - full_pages * 8
    column = (idx%4)
    row = round((idx/4)-0.49)
    print(f"{row}, {column} ({idx})")


    pdf.image("../cards/new_and_not_printed_yet/" + image,column*(63.5+2)+10,row*(88.9+2)+10,63.5,88.9) #
pdf.output("new_cards.pdf", "F")