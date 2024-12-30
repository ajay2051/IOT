# LESSON 44: Getting Started with Raspberry Pi Camera

import cv2
import  time

display_width = 1280
display_height = 720

cam = cv2.VideoCapture("videos")
cam.set(3, display_width)
cam.set(4, display_height)
while True:
    stat, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
