
from PIL import Image, ImageDraw, ImageFont
import os
from fpdf import FPDF

# imagelist is the list with all image filenames



images = [Image.open(r"../cards/buff-0.png"), Image.open(r"../cards/buff-1.png"), Image.open(r"../cards/buff-2.png")]
images = [r"../cards/buff-0.png",r"../cards/buff-1.png", r"../cards/buff-2.png", r"../cards/buff-3.png", r"../cards/buff-4.png"]
images = os.listdir("../cards/")
#import glob
#mylist = [f for f in glob.glob("../cards/*.png")]
#print(mylist)

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


    pdf.image("../cards/" + image,column*(63.5+2)+2,row*(88.9+2)+2,63.5,88.9) #
pdf.output("yourfile.pdf", "F")