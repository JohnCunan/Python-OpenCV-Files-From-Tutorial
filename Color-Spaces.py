import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('Photos/akko.jpg')
cv.imshow('Akko', img)

plt.imshow(img)
plt.show()

# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)
#
# # BGR to l*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)
#
#
#
# cv.waitKey(0)
