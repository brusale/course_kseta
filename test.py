import unittest
from src.Fitter import Fitter
from unittest.mock import patch
from numpy.testing import assert_almost_equal
import numpy as np

class Test(unittest.TestCase):
	
	def setUp(self):
		self.x_ = np.linspace(0,10, 1000)
		self.y_ = self.x_

	def test_fit(self):
		x = np.linspace(0,10, 1000)
		y = x
		fitter = Fitter(x,y)
		m, q = fitter.fit()
		regr_y = m * self.x_ + q
		assert_almost_equal(regr_y, y)

	def tearDown(self):
 		patch.stopall()
	
if __name__ == "__main__":
	unittest.main()
