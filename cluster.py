import numpy as np
from sklearn.cluster import KMeans

class Cluster:
    def __init__(self, num_clusters, max_iterations=100):
        self.num_clusters = num_clusters
        self.algorithm = KMeans(n_clusters=num_clusters, max_iter=max_iterations)
        self.max_iterations = max_iterations


    def train(self, data):        
        self.algorithm.fit(data)            
        self.centroids = self.algorithm.cluster_centers_
        return self.algorithm.labels_

    def test(self, data):
        assert len(self.centroids) == len(self.num_clusters)
        
        # Prep for test
        self.algorithm.n_clusters = self.centroids.shape[0]
        self.algorithm.max_iter = 1
        self.algorithm.init=self.centroids

        self.algorithm.fit(data)
        return self.algorithm.labels_
    
        


        
