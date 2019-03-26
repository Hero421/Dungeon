from termcolor import colored

class Air:

	def des(self, lay, row, elm, map_):

		cell = map_[lay - 1][row][elm]
		if not type(cell) is Air:
			return colored(cell.des, 'yellow')
		else:
			cell = map_[lay - 2][row][elm]
			if not type(cell) is Air:
				return colored(cell.des, 'red')
			else:
				return ' '

	def walk(self, dir_, obj):

		lay = obj.lay
		row = obj.row
		elm = obj.elm

		if   dir_ == 'North': row -= 1
		elif dir_ == 'East':  elm += 1
		elif dir_ == 'South': row += 1
		elif dir_ == 'West':  elm -= 1
		elif dir_ == 'up':    lay += 1
		elif dir_ == 'down':  lay -= 1

		if obj.map[lay-1][row][elm].chk_walk(obj):

			obj.map[obj.lay][obj.row][obj.elm] = self

			if   dir_ == 'North': obj.row -= 1
			elif dir_ == 'East':  obj.elm += 1
			elif dir_ == 'South': obj.row += 1
			elif dir_ == 'West':  obj.elm -= 1
			elif dir_ == 'up':    obj.lay += 1

		elif dir_ == 'down':

			input(self)

			obj.map[obj.lay][obj.row][obj.elm] = self
			obj.lay -= 1

	def chk_walk(self, obj):

		block = obj.map[obj.lay-1][obj.row][obj.elm]

		if not type(block) in (Air, type(obj)):
			obj.fall_var = True
			return True
		return False