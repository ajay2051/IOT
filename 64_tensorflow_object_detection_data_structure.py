import cv2
import time
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

model = 'efficientdet_lite0.tflite'
num_threads = 4

display_width = 1280
display_height = 720

pi_cam_2 = Picamera2()
pi_cam_2.preview_configuration.main.size = (display_width, display_height)
pi_cam_2.preview_configuration.main.format = 'RGB888'
pi_cam_2.preview_configuration.align()
pi_cam_2.configure("preview")
pi_cam_2.start()

web_cam = '/dev/video2'
cam = cv2.VideoCapture(web_cam)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, display_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, display_height)
cam.set(cv2.CAP_PROP_FPS, 30)

pos = (20, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
weight = 0.5
my_color = (0, 255, 0)
box_color = (255, 0, 0)

label_height = 1.5
label_color = (0, 255, 0)
label_weight = 1

fps = 0
base_options = core.BaseOptions(file_name=model, use_coral=False, num_threads=num_threads)
detection_options = processor.DetectionOptions(max_results=3, score_threshold=0.2, iou_threshold=0.2, max_detections=10)
options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)
time_start = time.time()
while True:
    ret, im = cam.read()
    frame = pi_cam_2.capture_array()
    frame = cv2.flip(frame, -1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_tensor = vision.TensorImage.create_from_array(image_rgb)
    my_detects = detector.detect(image_tensor)
    for my_detect in my_detects.detections:
        # print(my_detect)
        upper_left = (my_detect.bounding_box.origin_x, my_detect.bounding_box.origin_y)
        lower_right = (my_detect.bounding_box.origin_x + my_detect.bounding_box.width, my_detect.bounding_box.origin_y + my_detect.bounding_box.height)
        obj_name = my_detect.categories[0].category_name
        im = cv2.rectangle(im, upper_left, lower_right, box_color, 2)
        cv2.putText(im, obj_name, upper_left, font, weight, my_color)
    # image = utils.visualize(frame, my_detects)
    cv2.putText(frame, str(int(fps)) + "FPS", (20, 40), font, 1, my_color, 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time_elapsed = time.time() - time_start
    fps = 0.9 * fps + 0.1 * 1 / time_elapsed
    time_start = time.time()

cv2.destroyAllWindows()
