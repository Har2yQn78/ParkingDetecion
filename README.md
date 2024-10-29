# YOLOv8 Parking Detection

This project demonstrates object detection using the YOLOv8 model, specifically aimed at detecting cars and other vehicles in a parking lot. The project logs the number of detections and determines if the parking lot is full.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Training](#training)
- [Detection](#detection)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Har2yQn78/YOLOv8_Parking_Detection.git
    cd YOLOv8_Parking_Detection
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the YOLOv8 model with your custom dataset, follow these steps:

1. Ensure your dataset is in the correct format and placed in the `dataset` directory.
2. Update the `data.yaml` file to point to your dataset paths.
3. Run the training script:
    ```bash
    python src/train.py
    ```

### Detection

To run the object detection on sample images and log the results:

1. Place your images in the `data/sample_images` directory.
2. Run the detection script:
    ```bash
    python src/detect.py
    ```

This will:
- Load the trained YOLOv8 model from the `models` directory.
- Perform object detection on the specified image.
- Log the number of detections to `detection_log.csv`.
- Check if the parking lot is full based on the specified capacity.
- Display the detection results.

## Project Structure

ParkingDetection/
│
├── .gitignore
├── data/
│   └── sample_images/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
├── src/
│   ├── detect.py
│   ├── log_data.py
│   ├── visualize.py
│   ├── utils.py
├── models/
│   └── yolov8_trained_model.pt
├── detection_log.csv
├── README.md
└── requirements.txt


## Training

### `src/train.py`

This script trains the YOLOv8 model on your custom dataset. Ensure your dataset is structured correctly and the `data.yaml` file is properly configured. To train the model, run:

```bash
python src/train.py
```

## Detection
This script performs object detection using the trained YOLOv8 model. It also logs the number of detections and checks if the parking lot is full. To run detection, use:
```
python src/detect.py
```

## Acknowledgements
1. The YOLOv8 model was used for object detection.
2. The dataset used for training was obtained from Roboflow Vehicles OpenImages.

# Future of this project will contain train a model base on data we collect to predict when will the parking will be full or empty
