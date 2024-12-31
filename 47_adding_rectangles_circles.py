# LESSON 47: Adding Boxes, Rectangles and Circles on Images in OpenCV

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

upper_left = (250, 50)
lower_right = (350, 125)
rectangle_color = (255, 0, 255)
thickness = 3

center = (640, 360)
radius = 5

pi_camera = Picamera2()
pi_camera.preview_configuration.main.size = (display_width, display_height)
pi_camera.preview_configuration.main.format = "RGB888"
pi_camera.preview_configuration.controls.FrameRate = 30
pi_camera.preview_configuration.align()
pi_camera.configure('preview')
pi_camera.start()

while True:
    time_start = time.time()
    frame = pi_camera.capture_array()
    cv2.putText(frame, str(int(frame_per_second)), pos, font, height, color, weight)
    cv2.rectangle(frame, upper_left, lower_right, rectangle_color, thickness)
    cv2.circle(frame, center, radius, thickness)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()