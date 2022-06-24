import cv2 as cv

# BGR image which is the default
img = cv.imread('Photos/akko.jpg')
camera = cv.VideoCapture(0)

cv.imshow('Frame name', img)

# Converting an image into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray frame', gray)

# How to blur an image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur frame', blur)

# Create an Edge Cascade
# Replace img with the blur to reduce edges
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Frame', canny)

# Dilate an image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize an image
resize = cv.resize(img, (300, 300))
cv.imshow('Resized Image', resize)

# Cropping an image
crop = img[50:200, 200:400]
cv.imshow('Cropped Image', crop)

cv.waitKey(0)
