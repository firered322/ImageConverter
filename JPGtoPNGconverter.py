import os
from PIL import Image
import sys


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
