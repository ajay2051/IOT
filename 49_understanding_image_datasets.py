# LESSON 49: Understanding Images as Array Data Sets

import cv2
from picamera2 import Picamera2
import time
import numpy as np

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

box_width = 250
box_height = 125
top_left_column = 50
top_left_row = 75
lower_right_column = top_left_column + box_width
lower_right_row = top_left_row + box_height
delta_column = 2
delta_row = 2
thickness = -1
rectangle_color = (0, 125, 255)

while True:
    time_start = time.time()
    # frame = pi_camera.capture_array()
    # frame = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    frame = np.array([
        [[255, 0, 0],
        [0, 255, 0],
        [0, 0, 255]],
        [[1, 0, 0],
         [0, 0, 1],
         [0, 1, 0]]
    ])
    cv2.putText(frame, str(int(frame_per_second)), pos, font, height, color, weight)

    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()