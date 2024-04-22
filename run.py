from cluster import Cluster
from plotter import Plotter
import numpy as np

def main():
    num_clusters = 2
    num_points = 20

    # Define time stamps
    time_stamps = np.linspace(0, 1, num_points) 
    
    cluster = Cluster(num_clusters=num_clusters, max_iterations=100)
    plotter = Plotter(num_clusters=num_clusters, 
                      xLabel='Time',
                      yLabel='Amplitude',
                      title='Time Series Data with K-Means Clustering')
    
    data = generate_data(time_stamps)
    labels = cluster.train(data)
    plotter(timestamps=time_stamps, labels=labels, data=data)

def generate_data(time_stamps):
   

    # Define functions for generating sine waves
    
    # Generate time series data
    series1 = low_freq_low_amp(time_stamps)
    series2 = high_freq_low_amp(time_stamps)
    series3 = low_freq_high_amp(time_stamps)
    series4 = high_freq_high_amp(time_stamps)
    series5 = increasing_amp_smooth(time_stamps)
    series6 = increasing_amp_linear(time_stamps)

    # Generate a more curved parabolic curve
    parabola = -4 * (time_stamps - 0.5) ** 2 + 1  # Increased coefficient for stronger curvature

    data = np.vstack([series1, series2, series3, series4, series5, series6, parabola])
    np.save('/home/wizav/src/timeseries_embedding/data/sample.npy', data)
    return data


def low_freq_low_amp(t):
    return np.sin(2*np.pi*t * 0.5) * 0.2

def high_freq_low_amp(t):
    return np.sin(2*np.pi*t * 5) * 0.1

def low_freq_high_amp(t):
    return np.sin(2*np.pi*t) * 2  # Increased frequency for more cycles

def high_freq_high_amp(t):
    return np.sin(2*np.pi*t * 5) * 1

# Define functions for increasing amplitude with similar shape
def increasing_amp_smooth(t):
    return np.sin(2*np.pi*t * 5) * (t**2 + 0.2)  # Smooth increase

def increasing_amp_linear(t):
    return np.sin(2*np.pi*t * 5) * (t * 0.1 + 1)  # Linear increase

if __name__ == "__main__":
    main()