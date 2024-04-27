from typing import Any
import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, num_clusters, xLabel, yLabel, title):
            self.colors = self.generate_color_codes(num_clusters)
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

    def generate_color_codes(self, num_clusters):
        """
        Generates a list of random color code strings in various formats (hex, rgb)

        Args:
            num_clusters: The number of random color codes to generate.

        Returns:
            A list of random color code strings.
        """
        color_codes = []
        for _ in range(num_clusters):
            # Random choice between using hex or rgb format

            # Generate random RGB values (between 0 and 1)
            color_code = (random.random(), random.random(), random.random())
            color_codes.append(color_code)
        return color_codes