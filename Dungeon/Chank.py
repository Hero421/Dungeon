from Blocks.GameNone import GameNone

class Chank(object):

	def __init__(self, row, elm, area, length=10):   # lengthber of rows and elms

		self.length = length

		self.gen = False
		self.message = False

		self.row = row
		self.elm = elm

		self.strt_row = row*length
		self.strt_elm = elm*length

		self.map_ = area.map
		self.area = area

		for row in range(length):
			for elm in range(length):
				self.map_[self.strt_row + row][self.strt_elm + elm] = GameNone()

	def generator(self):

		self.gen = True

		for row in range(self.length):
			for elm in range(self.length):
				if type(self.map_[self.strt_row + row][self.strt_elm + elm]) is GameNone:
					self.map_[self.strt_row + row][self.strt_elm + elm].act(self.strt_row + row, self.strt_elm + elm)

		del self.length
		del self.strt_row
		del self.strt_elm
		del self.map_

	def msg(self):

		self.message = True

		for row in self.area.chank_map[self.row-2 : self.row+2]:
			for chank in row[self.elm-2 : self.elm+2]:
				try:
					if not chank.gen:
						chank.generator()
				except IndexError:
					pass

		del self.area
		del self.row
		del self.elm