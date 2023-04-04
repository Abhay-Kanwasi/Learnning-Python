from PIL import Image, ImageFilter

img =  Image.open('./Pokedex/206_pikachu.jpg')

print(img.format)
filtered_blur_image =img.filter(ImageFilter.BLUR)
filtered_blur_image.save("blur_pikachu.png", 'png')
filtered_smooth_image = img.filter(ImageFilter.SMOOTH)
filtered_smooth_image.save("smooth_pikachu.png", 'png')
