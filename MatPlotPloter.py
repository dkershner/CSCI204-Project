import numpy as np
import matplotlib.pyplot as plt

class MatPlotPloter:

    def scatterPlot(self, frequencies):
        x = list(range(len(frequencies)))
        plt.scatter(x, frequencies)
        plt.show()

    def barGraph(self, frequencies):
        x = list(range(len(frequencies)))
        plt.bar(x, frequencies)
        plt.show()
