# LESSON 45: Using the Raspberry Pi Camera in Bullseye with OpenCV

import cv2
from picamera2 import Picamera2

pi_camera = Picamera2()
pi_camera.preview_configuration.main.size = (1280, 720)
pi_camera.preview_configuration.main.format = "RGB888"
pi_camera.preview_configuration.align()
pi_camera.configure('preview')
pi_camera.start()
while True:
    frame = pi_camera.capture_array()
    cv2.imshow('Pi Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
cv2.destroyAllWindows()