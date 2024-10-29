from ultralytics import YOLO
import cv2
import os
from log_data import log_detection_data, check_parking_status


def load_model(model_path):
    return YOLO(model_path)


def detect_objects(model, image_path):
    img = cv2.imread(image_path)
    results = model.predict(img)
    return results, img


def display_results(results, img):
    img = results.plot()
    cv2.imshow('Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    model_path = '../models/yolov8_trained_model.pt'
    image_path = 'ParkingCamera.webm'

    model = load_model(model_path)
    results, img = detect_objects(model, image_path)

    # Number of detections
    num_detections = len(results.xyxy[0])

    # Log detection data and check parking status
    log_detection_data(num_detections)
    check_parking_status(num_detections, full_capacity=150)

    # Optionally display the results
    display_results(results, img)
