import csv
from datetime import datetime
import os


def init_log_file(log_file):
    if not os.path.exists(log_file):
        with open(log_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['timestamp', 'car_count'])
            writer.writeheader()


def log_detection(car_count, log_file):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(log_file, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'car_count'])
        writer.writerow({
            'timestamp': timestamp,
            'car_count': car_count
        })

    print(f"Logged detection: {car_count} cars at {timestamp}")