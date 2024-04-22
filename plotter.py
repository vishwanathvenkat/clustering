from typing import Any
from utils import generate_color_codes
import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, num_clusters, xLabel, yLabel, title):
            self.colors = generate_color_codes(num_clusters)
            self.xLabel = xLabel
            self.yLabel = yLabel
            self.title = title

    def __call__(self, data, timestamps, labels) -> Any:
        for i in range(data.shape[0]):
            plt.plot(timestamps, data[i, :], '-', c=self.colors[labels[i]], label=f'Cluster {labels[i]}')
            plt.title(self.title)
            plt.xlabel(self.xLabel)
            plt.ylabel(self.yLabel)
        plt.show()