# LESSON 61: Finding and Tracking Faces and Eyes In OpenCV


import cv2
from picamera2 import Picamera2
import time

fps = 0
frame_per_second = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
color = (0, 0, 255)
weight = 3
display_width = 1280
display_height = 720

pi_camera = Picamera2()
pi_camera.preview_configuration.main.size = (display_width, display_height)
pi_camera.preview_configuration.main.format = "RGB888"
pi_camera.preview_configuration.controls.FrameRate = 30
pi_camera.preview_configuration.align()
pi_camera.configure('preview')
pi_camera.start()

face_cascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haar/haarcascade_eye.xml')

while True:
    time_start = time.time()
    frame = pi_camera.capture_array()
    frame = cv2.flip(frame, -1)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = frame_gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
    # eyes = eye_cascade.detectMultiScale(frame_gray, 1.3, 5)
        for eye in eyes:
            x, y, w, h = eye
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (255, 0, 0), 3)
            # cv2.imshow('ROI', roi_color)
    cv2.putText(frame, str(int(frame_per_second)), pos, font, height, color, weight)
    cv2.imshow('Pi Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()