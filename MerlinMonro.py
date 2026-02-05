from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

coordinates = (100, 0, red.width, red.height)
cropped_left = image.crop(coordinates)

coordinates = (50, 0, red.width - 50, red.height)
cropped_middle = image.crop(coordinates)

red_channel_displaced = Image.blend(cropped_left, cropped_middle, 0.5)

coordinates = (0, 0, blue.width - 100, blue.height)
cropped_right = image.crop(coordinates)

coordinates = (50, 0, blue.width - 50, blue.height)
cropped_middle = image.crop(coordinates)

blue_channel_displaced = Image.blend(cropped_right, cropped_middle, 0.5)

coordinates = (50, 0, green.width - 50, green.height)
green_channel_cropped_middle = image.crop(coordinates)

thumbnail_image = Image.merge("RGB", (red, green, blue))
thumbnail_image.save("thumbnail_image.jpg")

thumbnail_image.thumbnail((80, 80))
thumbnail_image.save("MerlinMonro_finish.jpg")
