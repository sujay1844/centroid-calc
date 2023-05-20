from dataclasses import dataclass

class Shape:
	x: float
	y: float
	is_filled = True
	def __init__(self, x: float, y: float, is_filled: bool = True):
		self.x = x
		self.y = y
		self.is_filled = is_filled

	def area(self):
		raise NotImplementedError

class Circle(Shape):
	radius: float
	name: str = 'circle'

	def area(self):
		_area = 3.14 * self.radius ** 2
		if not self.is_filled:
			_area = -_area
		return _area

class Rectangle(Shape):
	width: float
	height: float
	name: str = 'rectangle'

	def area(self):
		_area = self.width * self.height
		if not self.is_filled:
			_area = -_area
		return _area

class Triangle(Shape):
	base: float
	height: float
	name: str = 'triangle'

	def area(self):
		_area = 0.5 * self.base * self.height
		if not self.is_filled:
			_area = -_area
		return _area