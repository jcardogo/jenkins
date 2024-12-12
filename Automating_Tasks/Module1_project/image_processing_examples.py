import PIL

from PIL import Image
im = Image.open("example.jpg")
new_im = im.rezise((640,480))
new_im.save("example_resized.jpg")

from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_resized.jpg")

from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).rezise((640,480)).save("flipped_and_resized.jpg")



