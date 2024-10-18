import numpy as np
import matplotlib.pyplot as plt
from src.Fitter import Fitter

data = np.loadtxt("data.csv", delimiter=",")

plt.plot(
    np.arange(20),
    np.poly1d(Fitter(data[:, 0], data[:, 1]).fit())(np.arange(20)),
    color="r",
)
plt.scatter(data[:, 0], data[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot.png")
