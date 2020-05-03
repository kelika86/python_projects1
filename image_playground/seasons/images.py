from PIL import Image, ImageFilter

img = Image.open('./seasons/winter.jpg')
filtered_img = img.filter(ImageFilter.DETAIL)

filtered_img.thumbnail((400,200))
filtered_img.save('thumbnail.jpg')