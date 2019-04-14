from Methods.generator_for_blocks import generator_for_blocks
from links import NewInt

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
					if type(self.map_[t_lay][t_row][t_elm]) is NewInt:
						v_map  = self.area.vector_map
						v_list = v_map[self.row][self.elm]
						point  = type('point', (), {'x2': t_elm, 'y2': t_row})
						mul0   = v_list[0]*point
						mul1   = v_list[1]*point
						mul2   = v_list[2]*point
						mul3   = v_list[3]*point
						height = int((mul0 + mul1 + mul2 + mul3)/(4*2))
						generator_for_blocks(t_lay, t_row, t_elm, self.map_, height)

		del self.length
		del self.strt_lay
		del self.strt_row
		del self.strt_elm
		del self.map_

	def msg(self):

		self.message = True

		map_ = self.area.chank_map

		strt_lay = min([self.lay - 2  , len(map_) - self.lay])
		fin_lay  = self.lay + min([2+1, int(len(map_)/2) - self.lay-1])

		strt_row = min([self.row - 2  , len(map_) - self.row])
		fin_row  = self.row + min([2+1, int(len(map_[0])/2) - self.row-1])

		strt_elm = min([self.elm - 2  , len(map_) - self.elm])
		fin_elm  = self.elm + min([2+1, int(len(map_[0][0])/2) - self.elm-1])

		for lay in self.area.chank_map[strt_lay : fin_lay]:
			for row in lay[strt_row : fin_row]:
				for chank in row[strt_elm : fin_elm]:
					if not chank.gen:
						chank.generator()

		del self.area
		del self.row
		del self.elm