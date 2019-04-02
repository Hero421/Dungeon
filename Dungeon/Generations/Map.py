class Map(list):

	def __new__(cls, lst):
		if type(lst) is list:
			return list.__new__(cls, list)

	def __init__(self, lst):
		self.list = lst
		self.RADIUS = int(self.list.__len__()/2)

	def __len__(self):
		return self.list.__len__()

	def __iter__(self):
		return self.list.__iter__()

	def __next__(self):
		return self[self.list.index(self.list.__next__()) - self.RADIUS]

	def __index__(self, obj):

		idx = -self.RADIUS

		for elm in self.list:
			if elm is obj:
				return idx
			idx += 1

		raise ValueError(f'{obj} is not in list')

	def __getitem__(self, n):

		idx = -self.RADIUS

		if isinstance(n, slice):
			return self.list[n.start-self.RADIUS : n.stop-self.RADIUS : n.step]

		else:
			for elm in self.list:
				if idx == n and not type(elm) is None:
					return elm
				idx += 1

			raise IndexError(f'index {n} is not in list')

			if -(3*self.RADIUS) < n < -self.RADIUS:
				return self.list[n + self.RADIUS]

	def __setitem__(self, n, value):

		idx = -self.RADIUS

		error = True
		cont  = True

		for index in range(self.list.__len__()):
			if idx == n:
				self.list[index] = value
				cont = False
				break
			idx += 1

		if cont:

			if -(3*self.RADIUS) < n < -self.RADIUS:
				self.list[n + self.RADIUS] = value
				error = False

			if error:
				raise IndexError(f'index {n} is not in list')

