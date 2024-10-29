import pandas as pd
import matplotlib.pyplot as plt

def plot_detection_log(log_file='detection_log.csv'):
    df = pd.read_csv(log_file)
    df['date'] = pd.to_datetime(df['date'])
    df.plot(x='date', y='detections', kind='line')
    plt.xlabel('Date')
    plt.ylabel('Number of Detections')
    plt.title('Number of Detections Over Time')
    plt.show()

if __name__ == "__main__":
    plot_detection_log()
