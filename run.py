from cluster import Cluster
from plotter import Plotter
import numpy as np
from data_generation import  generate_all_data

def main():
    num_clusters = 6
    num_points_original = 20

    # Define time stamps
    time_stamps = np.linspace(0, 1, num_points_original)
    
    cluster = Cluster(num_clusters=num_clusters, max_iterations=100)
    plotter = Plotter(num_clusters=num_clusters, 
                      xLabel='Time',
                      yLabel='Amplitude',
                      title='Time Series Data with K-Means Clustering')
    
    data = generate_all_data(time_stamps)
    # np.save('/home/wizav/src/timeseries_embedding/data/sample.npy', data)
    embedded_data = np.load('/home/wizav/src/timeseries_embedding/data/encoded_data.npy')
    source_data = np.load('/home/wizav/src/timeseries_embedding/data/sample.npy')

    labels = cluster.train(data)

    plotter(timestamps=time_stamps, labels=labels, data=data)




if __name__ == "__main__":
    main()