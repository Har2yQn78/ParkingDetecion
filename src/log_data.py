import pandas as pd
from datetime import datetime
import os


def log_detection_data(num_detections, log_file='../detection_log.csv'):
    current_date = datetime.now().strftime('%Y-%m-%d')
    data = {'date': current_date, 'detections': num_detections}

    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        df = df.append(data, ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_csv(log_file, index=False)


def check_parking_status(num_detections, full_capacity=150):
    if num_detections >= full_capacity:
        print(f"Parking is full. {num_detections} cars detected.")
    elif num_detections > 0:
        print(f"Parking is not empty. {num_detections} cars detected.")
    else:
        print("Parking is empty.")


if __name__ == "__main__":
    # Example usage
    log_file = '../detection_log.csv'
    num_detections = 155  # Example number of detections

    log_detection_data(num_detections, log_file)
    check_parking_status(num_detections, full_capacity=150)
