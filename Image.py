from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = img.crop(box)
# filtered_img = img.resize((300, 300))
region.save('resize.png', 'png')
# filtered_img = img.show()
