# LESSON 53: Using Trackbars to Track Colored Objects in OpenCV


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


def on_track_1(val):
    global hue_low
    hue_low = val
    print('HUe Low', hue_low)


def on_track_2(val):
    global hue_high
    hue_high = val
    print('HUe High', hue_high)


def on_track_3(val):
    global sat_low
    sat_low = val
    print('Sat Low', sat_low)


def on_track_4(val):
    global sat_high
    sat_high = val
    print('Sat High', sat_high)


def on_track_5(val):
    global val_low
    val_low = val
    print('Val Low', val_low)


def on_track_6(val):
    global val_high
    val_high = val
    print('Val High', val_high)


cv2.namedWindow('My Tracker')

cv2.createTrackbar('Hue Low', 'My Tracker', 10, 179, on_track_1)
cv2.createTrackbar('Hue High', 'My Tracker', 30, 179, on_track_2)
cv2.createTrackbar('Sat Low', 'My Tracker', 100, 255, on_track_3)
cv2.createTrackbar('Sat High', 'My Tracker', 255, 255, on_track_4)
cv2.createTrackbar('Val Low', 'My Tracker', 100, 255, on_track_5)
cv2.createTrackbar('Val High', 'My Tracker', 255, 255, on_track_6)

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

    lower_bound = np.array([hue_low, sat_low, val_low])
    upper_bound = np.array([hue_high, sat_high, val_high])

    frame_hsv = (cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
    my_mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    my_mask_small = cv2.resize(my_mask, (int(display_width / 2), int(display_height / 2)))
    my_object = cv2.bitwise_and(frame, frame, mask=my_mask)
    my_object_small = cv2.resize(my_object, (int(display_width / 2), int(display_height / 2)))
    cv2.imshow('My Mask', my_mask_small)
    cv2.imshow('My Object', my_object_small)
    cv2.imshow('Pi Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()