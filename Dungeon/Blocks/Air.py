from termcolor import colored

class Air:

	def des(self, lay, row, elm, map_):

		num = 4

		for count in range(1, 4):
			cell = map_[lay - count][row][elm]
			if not type(cell) is Air:
				num = count
				break
		
		if   num == 1: color = 'yellow'
		elif num == 2: color = 'red'
		elif num == 3: color = 'green'
		else: return ' '

		return colored(cell.des, color)

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

		obj.map[obj.lay][obj.row][obj.elm] = self

		obj.lay = lay
		obj.row = row
		obj.elm = elm