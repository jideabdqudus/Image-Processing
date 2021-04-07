import os, sys
from PIL import Image


#for images in "./Images"

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".png"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert", infile)


print("Current Working Directory ", os.getcwd())
print(os.chdir("Images"))
print("Current Working Directory ", os.getcwd())


# define the name of the directory to be created
path = "/newImages"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


listOfFiles = getListOfFiles(os.getcwd())


print(listOfFiles)

for item in listOfFiles:
    img = Image.open(item)
    img.save("new_image.png", "png")
    img.show()


'''
        with open("my_note.txt", mode="w") as file:
        file.write("\nWritten into you")

with open("my_note.txt", mode="a") as file:
    file.write("\nAppended into you")
'''


"""
img = Image.open("./blur.png")
img.save("new_image.jpg")
img.show()
"""


"""
img = Image.open("./Images/pikachu.jpg")

#filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert("L")

filtered_img.save("grey.jpeg", "jpeg")
filtered_img.show()
print(img.mode)

"""

"""
astro = Image.open("./Images/astro.jpg")

new_image = astro.resize((400, 400))
new_image.save("astro_thumbnail.jpg")
new_image.show()

"""