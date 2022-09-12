#!/usr/bin/python3
from PIL import Image
from PIL.ImageOps import exif_transpose

def img_pad(src_file, dest_file, size=(480, 360), color=(0, 0, 0, 0)):
    """
    transforms the image (src_file) to a padded and centered image of (size)
    with background (color) and converts and saves it to the format of (dest_file) extention
    """

    # create a base image #
    base = Image.new('RGBA', size, color)

    with Image.open(src_file) as img:
        # align image as per camera rotation #
        img = exif_transpose(img)
        # create a thumbnail of specified size #
        img.thumbnail(size)
        # calculate placement co-ordinates for the loaded image on the base #
        left_top = (size[0]-img.width)//2, (size[1]-img.height)//2
        base.paste(img, left_top)

    # destination filename #
    base.save(dest_file)

if __name__ == '__main__':
    img_pad('test.jpg','images/test.webp')
