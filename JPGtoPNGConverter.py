import os
from PIL import Image

print(os.chdir("Images"))
list_of_files = os.listdir(os.getcwd())

path = f"{os.getcwd()}/newImages"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


for item in list_of_files:
    image_name = os.path.splitext(item)[0]
    img = Image.open(item)
    img.save(f"{os.getcwd()}/newImages/{image_name}.png", "png")

