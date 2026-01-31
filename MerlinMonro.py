from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split() 

new_image = Image.merge("RGB", (red, green, blue))

image1 = red
image2 = red

coordinates = (100, 0, image1.width, image1.height)
cropped_left = image1.crop(coordinates)

coordinates = (50, 0, image1.width - 50, image1.height)
cropped_middle = image2.crop(coordinates)

image3 = Image.blend(cropped_left, cropped_middle, 0.5)
red_channel_displaced = image3

image1 = blue 
image2 = blue

coordinates = (0, 0, image1.width - 100, image1.height)
cropped_right = image1.crop(coordinates)

coordinates = (50, 0, image1.width - 50, image1.height)
cropped_middle = image2.crop(coordinates)

image3 = Image.blend(cropped_right, cropped_middle, 0.5)

blue_channel_dicplaced = image3

image1 = green

coordinates = (70, 0, image1.width - 30, image1.height)
cropped_middle = image1.crop(coordinates)

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
