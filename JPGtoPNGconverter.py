import os
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import sys

# ToDo: Add a feature to remove the background of the provided photo.
# Todo: Edge detection using the canny method.
# ToDo: Adding an increase, decrease contrast function.

if len(sys.argv) == 3:
    sourceDir = sys.argv[1]
    destinationDir = sys.argv[2]
    print('Source Dir', sourceDir)
    print('Destination Dir', destinationDir)

    # Make folder if already does not exist
    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)

    for idz, imgName in enumerate(os.listdir(f'./{sourceDir}')):
        img = Image.open(f'./{sourceDir}/{imgName}')
        imgBasename, imgExtension = os.path.splitext(imgName)
        print(imgBasename+imgExtension)
        img.save(f'./{destinationDir}/{imgBasename}.png', 'png')
        print(f'Converted {idz+1} photo.')

# This case is for handling when no arguments have been passed and the photos are in the root directory
else:
    for i in os.listdir('.'):
        if i.endswith('jpg'):
            theImage = Image.open(i)
            imgName, imgExt = os.path.splitext(i)
            theImage.save(f'pngs/{imgName}.png')

enhanceMents = {
    "imgSHR": ImageEnhance.Sharpness,
    "imgBRI": ImageEnhance.Brightness,
    "imgCLR": ImageEnhance.Color,
    "imgCTR": ImageEnhance.Contrast
}

filters = {
    'blur': ImageFilter.BLUR,
    'contour': ImageFilter.CONTOUR,
    'emboss': ImageFilter.EMBOSS,
    'edge_enhance': ImageFilter.EDGE_ENHANCE,
    'edge_enhance_more': ImageFilter.EDGE_ENHANCE_MORE,
    'detail': ImageFilter.DETAIL,
    'smooth': ImageFilter.SMOOTH,
    'smooth_more': ImageFilter.SMOOTH_MORE
}


def adjustEffect(effect, factor):  # Factor is in between 0-1 for most cases
    enhanced_object = enhanceMents[effect](im)
    enhanced_output = enhanced_object.enhance(factor)
    enhanced_output.thumbnail(size)
    enhanced_output.show()


def addFilter(effect):
    filtered_image = im.filter(filters[effect])
    filtered_image.thumbnail(size)
    filtered_image.show()
