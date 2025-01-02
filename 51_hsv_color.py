# LESSON 51: Understanding and Working in the HSV Color Space


import cv2
import numpy as np
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

hue_low = 20
hue_high = 20

saturation_low = 100
saturation_high = 255

value_low = 100
value_high = 255

lower_bound = np.array([hue_low, saturation_low, value_low])
upper_bound = np.array([hue_high, saturation_high, value_high])

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
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    my_mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    my_mask_small = cv2.resize(my_mask, (int(display_width/2), int(display_height/2)))
    object_of_interest = cv2.bitwise_and(frame, frame, mask=my_mask_small)
    object_of_interest_small = cv2.resize(object_of_interest, (int(display_width/2), int(display_height/2)))
    print(frame_hsv[int(display_height/2), int(display_width/2)])
    cv2.putText(frame, str(int(frame_per_second)), pos, font, height, color, weight)
    cv2.imshow('Pi Cam', frame)
    cv2.imshow('my_mask', my_mask_small)
    cv2.imshow('object_of_interest', object_of_interest)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()