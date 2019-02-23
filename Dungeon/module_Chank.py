from Blocks.module_GameNone import GameNone

class Chank(object):

	def __init__(self, row, elm, glob_ses_area, glob_ses_avatars, num=50):   # number of rows and elms

		self.row = row
		self.elm = elm
		self.num = num

		self.map = glob_ses_area.map
		self.area = glob_ses_area
		self.avatars = glob_ses_avatars

		self.strt_row = row*num
		self.strt_elm = elm*num

		self.fin_row = self.strt_row + num
		self.fin_elm = self.strt_elm + num

		for row in range(-1, self.fin_row - self.strt_row - 1):
			for elm in range(-1, self.fin_elm - self.strt_elm - 1):
				self.map[self.strt_row + row][self.strt_elm + elm] = GameNone()

	def check(self):

		for avatar in self.avatars:

			if avatar.chank.row < self.row:

				for row in range(self.strt_row, self.strt_row - 6):
					for elm in range(self.strt_elm, self.fin_elm):
						if self.map[row][elm] == avatar:
							self.generator()


			elif avatar.chank.elm > self.elm:

				for row in range(self.strt_row, self.fin_row):
					for elm in range(self.fin_elm, self.fin_elm + 6):
						if self.map[row][elm] == avatar:
							self.generator()

			elif avatar.chank.row > self.row:

				for row in range(self.fin_row, self.fin_row + 6):
					for elm in range(self.strt_elm, self.fin_elm):
						if self.map[row][elm] == avatar:
							self.generator()

			elif avatar.chank.elm < self.row:

				for row in range(self.strt_row, self.fin_row):
					for elm in range(self.strt_elm, self.strt_elm - 6):
						if self.map[row][elm] == avatar:
							self.generator()

	def generator(self):

		for row in range(self.strt_row, self.fin_row):
			for elm in range(self.strt_elm, self.fin_elm):
				if type(self.map[row][elm]) is GameNone:
					self.map[row][elm].act(row, elm)

	def msg(self):

		self.area.chank_map[self.row - 1][self.elm].check()
		self.area.chank_map[self.row][self.elm + 1].check()
		self.area.chank_map[self.row + 1][self.elm].check()
		self.area.chank_map[self.row][self.elm - 1].check()