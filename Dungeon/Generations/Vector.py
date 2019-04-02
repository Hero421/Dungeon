from math import pi, sin, cos
from random import random, randint

def point(h, k, r=1):
	theta = random() * 2 * pi
	return h + cos(theta) * r, k + sin(theta) * r

class Vector:

	def __init__(self, x1, y1):
		
		self.num = str(randint(0, 9))

		x2, y2 = point(x1, y1)

		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def __mul__(self, other):
		return (self.x2*other.x2) + (self.y2*other.y2)

	def __rmul__(other, self):
		return (self.y2*other.y2) + (self.x2*other.x2)
