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
					t_lay = self.strt_lay + lay
					t_row = self.strt_row + row
					t_elm = self.strt_elm + elm
					if type(self.map_[t_lay][t_row][t_elm]) is int:
						v_map  = self.area.vector_map
						v_list = v_map[self.row][self.elm]
						tmp_cls= type('tmp_cls', (), {'x2': t_elm, 'y2': t_row})
						mul0   = v_list[0]*tmp_cls
						mul1   = v_list[1]*tmp_cls
						mul2   = v_list[2]*tmp_cls
						mul3   = v_list[3]*tmp_cls
						height = int((mul0 + mul1 + mul2 + mul3)/4)
						generator_for_blocks(t_lay, t_row, t_elm, self.map_, height)

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