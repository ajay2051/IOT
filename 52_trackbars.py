# LESSON 52: Understanding and Using Trackbars in OpenCV

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


def track_x(value):
    global x_position
    x_position = value
    print("Tracking X:", x_position)


def track_y(value):
    global y_position
    y_position = value
    print("Tracking Y:", y_position)


def track_w(value):
    global box_width
    box_width = value
    print("Tracking Width:", box_width)


def track_h(value):
    global box_height
    box_height = value
    print("Tracking Height:", box_height)

box_color = (0, 255, 0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar('X Pos', 'My Trackers', 10, display_width - 1, track_x)
cv2.createTrackbar('Y Pos', 'My Trackbars', 10, display_height - 1, track_y)
cv2.createTrackbar('Box Width', 'My Trackbars', 10, display_width - 1, track_w)
cv2.createTrackbar('Box Height', 'My Trackbars', 10, display_height - 1, track_h)

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
    region_of_interest = frame[y_position:y_position + box_height, x_position:x_position + box_width]
    cv2.putText(frame, str(int(frame_per_second)), pos, font, height, color, weight)
    cv2.rectangle(frame, pos[0], pos[1], box_color, box_width)
    cv2.imshow('Pi Cam', frame)
    cv2.imshow('Trackbars', region_of_interest)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressing q will exit the frame
        break
    time_end = time.time()
    loop_time = time_end - time_start
    frame_per_second = 0.9 * fps + 0.1 * (1 / loop_time)
    # print(int(frame_per_second))
    time.sleep(0.2)
cv2.destroyAllWindows()
