from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

image = red

coordinates = (100, 0, image.width, image.height)
cropped_left = image.crop(coordinates)

coordinates = (50, 0, image.width - 50, image.height)
cropped_middle = image.crop(coordinates)

red_channel_displaced = Image.blend(cropped_left, cropped_middle, 0.5)

image = blue

coordinates = (0, 0, image.width - 100, image.height)
cropped_right = image.crop(coordinates)

coordinates = (50, 0, image.width - 50, image.height)
cropped_middle = image.crop(coordinates)

blue_channel_displaced = Image.blend(cropped_right, cropped_middle, 0.5)

image = green

coordinates = (50, 0, image.width - 50, image.height)
green_channel_cropped_middle = image.crop(coordinates)

red = red_channel_displaced
green = green_channel_cropped_middle
blue = blue_channel_displaced

rgb_image = Image.merge("RGB", (red, green, blue))

thumbnail_image = rgb_image.copy()
thumbnail_image.thumbnail((80, 80))
thumbnail_image.save("MerlinMonro_finish.jpg")
