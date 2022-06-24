import cv2 as cv

# Capture image file path
# img = cv.imread('Photos/akko.jpg');
# Show image
# cv.imshow('Akko', img)

capture = cv.VideoCapture('Videos/heroin.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# Wait for Key Press
#cv.waitKey(0)
