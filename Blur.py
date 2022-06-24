import cv2 as cv

img = cv.imread('Photos/Akko.jpg')
cv.imshow('Akko', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
