from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split() 

new_image = Image.merge("RGB", (red, green, blue))

image1 = red
image2 = red

cmyk_image1 = image1.convert("CMYK")
cmyk_image2 = image2.convert("CMYK")
coordinates = (101, 0, cmyk_image1.width, cmyk_image1.height)
cropped_left = cmyk_image1.crop(coordinates)

coordinates = (51, 0, cmyk_image1.width - 50, cmyk_image1.height)
cropped_middle = cmyk_image2.crop(coordinates)

image3 = Image.blend(cropped_left, cropped_middle, 0.5)
red_channel_displaced = image3

image1 = blue
image2 = blue

cmyk_image1 = image1.convert("CMYK")
cmyk_image2 = image2.convert("CMYK")

coordinates = (0, 0, cmyk_image1.width - 101, cmyk_image1.height)
cropped_right = cmyk_image1.crop(coordinates)

coordinates = (51, 0, cmyk_image1.width - 50, cmyk_image1.height)
cropped_middle = cmyk_image2.crop(coordinates)

image3 = Image.blend(cropped_right, cropped_middle, 0.5)

blue_channel_dicplaced = image3

image1 = green
cmyk_image1 = image1.convert("CMYK")

coordinates = (71, 0, cmyk_image1.width - 30, cmyk_image1.height)
cropped_middle = cmyk_image1.crop(coordinates)

green_channel_cropped_middle = cropped_middle

red = red_channel_displaced
green = green_channel_cropped_middle  
blue = blue_channel_dicplaced

red = red.convert('L')
green = green.convert('L')
blue = blue.convert('L')

rgb_image = Image.merge("RGB", (red, green, blue))

thumbnail_image = rgb_image.copy()

thumbnail_image.thumbnail((80, 80))
thumbnail_image.save("MerlinMonro_finish.jpg")
