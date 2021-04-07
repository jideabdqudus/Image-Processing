from PIL import Image, ImageFilter

img = Image.open("./Images/pikachu.jpg")

#filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert("L")

filtered_img.save("grey.jpeg", "jpeg")
print(img.mode)