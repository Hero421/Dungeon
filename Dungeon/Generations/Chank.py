from Methods.generator_for_blocks import generator_for_blocks

class Chank(object):

	def __init__(self, lay, row, elm, area, length=10):   # lengther of rows and elms

		self.length = length

		self.gen = False
		self.message = False

		self.lay = lay
		self.row = row
		self.elm = elm

		self.strt_lay = lay*length
		self.strt_row = row*length
		self.strt_elm = elm*length

		self.map_ = area.map
		self.area = area

	def generator(self):

		self.gen = True

		for lay in range(self.length):
			for row in range(self.length):
				for elm in range(self.length):
					if type(self.map_[self.strt_lay + lay][self.strt_row + row][self.strt_elm + elm]) is int:
						generator_for_blocks(self.strt_lay + lay, self.strt_row + row, self.strt_elm + elm, self.map_)

		del self.length
		del self.strt_lay
		del self.strt_row
		del self.strt_elm
		del self.map_

	def msg(self):

		self.message = True

		for lay in self.area.chank_map[self.lay-2 : self.lay+2]:
			for row in lay[self.row-2 : self.row+2]:
				for chank in row[self.elm-2 : self.elm+2]:
					try:
						if not chank.gen:
							chank.generator()
					except IndexError:
						pass

		del self.area
		del self.row
		del self.elm