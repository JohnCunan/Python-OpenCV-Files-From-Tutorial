import cv2 as cv


# Rescale function
# Works for images, video, and live video
# Takes the frame and rescales it with a particular value
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Returns rescale value
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Other function for rescaling video
# Only works for live video
def changerRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


# Image
img = cv.imread('Photos/kanata.jpg')
cv.imshow('Kanata', img)

resized_image = rescaleFrame(img)
cv.imshow('Kanata', resized_image)

# Video
capture = cv.VideoCapture('Videos/madara.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)  # Displays Normal Video Size

    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('Video Resized', frame_resized)  # Displays Rescaled Size

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()
