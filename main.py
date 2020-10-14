from google_images_search import GoogleImagesSearch
from keys import APIkey, CXkey
import os, shutil
from PIL import Image, ImageDraw, ImageFont
import random

gis = GoogleImagesSearch(
    APIkey, CXkey, validate_images=True)

folder = "./downloads"
words = "./resources/listado-general.txt"
font = "./resources/impact.ttf"

def imgDownload(imgQuery):
    _search_params = {
        'q': imgQuery,
        'num': 1
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    gis.search(search_params=_search_params, path_to_dir=folder, custom_image_name='image')

def random_line(directory):
    afile = open(directory)
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline.rstrip()
    return line

imgname = random_line(words)
imgDownload(imgname)

msg = random_line(words)
image = Image.open('./downloads/image.jpg')
width, height = image.size
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(font, size=45)
(w, h) = draw.textsize(msg, font=font)
x = (width-w)/2
y = height-60

shadowcolor = 'rgb(0,0,0)'
draw.text((x-1, y-1), msg, font=font, fill=shadowcolor)
draw.text((x+1, y-1), msg, font=font, fill=shadowcolor)
draw.text((x-1, y+1), msg, font=font, fill=shadowcolor)
draw.text((x+1, y+1), msg, font=font, fill=shadowcolor)

draw.text((x, y), msg, fill='rgb(255,255,255)', font=font)

image.save('./results/'+imgname+'.png')
