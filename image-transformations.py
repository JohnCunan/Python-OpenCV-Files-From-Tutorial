import numpy as np

import cv2 as cv
from numpy import record

img = cv.imread('Photos/akko.jpg')

cv.imshow('Frame name', img)


# Translations
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x ---> left
# -y ---> up
# +x ---> right
# +y ---> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resize an Image
resized = cv.resize(img, (200, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flip an image
# 0 vertical, 1 horizontal, -1 implies both vertical and horizontal
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# Cropping
# crop = img[200:200, 300:400]
# cv.imshow('Cropped', crop)

cv.waitKey(0)
