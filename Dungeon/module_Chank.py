from Blocks.module_GameNone import GameNone

class Chank(object):

	def __init__(self, row, elm, num=10):   # number of rows and elms

		self.row = row
		self.elm = elm
		self.num = num

		self.strt_row = row*num
		self.strt_elm = elm*num

		self.fin_row = self.strt_row + num
		self.fin_elm = self.strt_elm + num

		from module_links import ses_area

		for row in range(-1, self.fin_row - self.strt_row - 1):
			for elm in range(-1, self.fin_elm - self.strt_elm - 1):
				ses_area.map[self.strt_row + row][self.strt_elm + elm] = GameNone()

	def check(self, avatar, way):

		if way == 'up':
			for row in range(self.strt_row - 10, self.strt_row):
				for elm in range(self.strt_elm, self.fin_elm):
					try:
						if avatar.map[row][elm] == avatar:
							self.generator(avatar)
					except IndexError:
						pass

		elif way == 'right':
			for row in range(self.strt_row, self.fin_row):
				for elm in range(self.fin_elm, self.fin_elm + 10):
					try:
						if avatar.map[row][elm] == avatar:
							self.generator(avatar)
					except IndexError:
						pass

		elif way == 'down':
			for row in range(self.fin_row, self.fin_row + 10):
				for elm in range(self.strt_elm, self.fin_elm):
					try:
						if avatar.map[row][elm] == avatar:
							self.generator(avatar)
					except IndexError:
						pass

		elif way == 'left':
			for row in range(self.strt_row, self.fin_row):
				for elm in range(self.strt_elm - 10, self.strt_elm):
					try:
						if avatar.map[row][elm] == avatar:
							self.generator(avatar)
					except IndexError:
						pass

	def generator(self, avatar):

		for row in range(self.strt_row, self.fin_row):
			for elm in range(self.strt_elm, self.fin_elm):
				if type(avatar.map[row][elm]) is GameNone:
					avatar.map[row][elm].act(row, elm)

	def msg(self, avatar):
		
		if not self.row == 0:
			avatar.area.chank_map[self.row - 1][self.elm].check(avatar, 'down')
		if not self.elm == 0:
			avatar.area.chank_map[self.row][self.elm + 1].check(avatar, 'left')
		avatar.area.chank_map[self.row + 1][self.elm].check(avatar, 'up')
		avatar.area.chank_map[self.row][self.elm - 1].check(avatar, 'right')