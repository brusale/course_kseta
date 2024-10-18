import numpy as np


class Fitter:
    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y

    def fit(self):
        return np.polyfit(self.x_, self.y_, 1)
