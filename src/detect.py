from ultralytics import YOLO
import cv2
import os
from logger import init_log_file, log_detection


def process_images(model_path, image_folder, output_folder, log_file):
    # Initialize the log file
    init_log_file(log_file)

    # Load the YOLO model
    model = YOLO(model_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(image_folder)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Could not read image: {image_file}")
            continue

        results = model(image)[0]

        car_count = 0

        for r in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r

            if score > 0.5:
                cv2.rectangle(image,
                              (int(x1), int(y1)),
                              (int(x2), int(y2)),
                              (0, 255, 0),
                              2)
                car_count += 1

        log_detection(car_count, log_file)

        cv2.putText(image, f'Cars: {car_count}',
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)

        output_path = os.path.join(output_folder, f'detected_{image_file}')
        cv2.imwrite(output_path, image)

        cv2.imshow('Car Detection', image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    MODEL_PATH = r"\models\best.pt"
    IMAGE_FOLDER = r"\parking pic"
    OUTPUT_FOLDER = r"\Parking Detecion Project\output"
    LOG_FILE = r"\detection_log.csv"

    process_images(MODEL_PATH, IMAGE_FOLDER, OUTPUT_FOLDER, LOG_FILE)