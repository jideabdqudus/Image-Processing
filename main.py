from PIL import Image

img = Image.open("./blur.png")
img.save("new_image.jpg")
img.show()



img = Image.open("./Images/pikachu.jpg")

#filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert("L")

filtered_img.save("grey.jpeg", "jpeg")
filtered_img.show()
print(img.mode)


astro = Image.open("./Images/astro.jpg")

new_image = astro.resize((400, 400))
new_image.save("astro_thumbnail.jpg")
new_image.show()

