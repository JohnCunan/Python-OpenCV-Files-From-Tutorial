import cv2
import cv2 as cv

capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in face_rect:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        cv.imshow('Frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
