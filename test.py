import unittest
from src.Fitter import Fitter
import numpy as np

class Test(unittest.TestCase):

	def test_fit(self):
		x = np.linspace(0,10, 1000)
		y = x
		fitter = Fitter(x,y)
		fitter.fit()

if __name__ == "__main__":
	unittest.main()
