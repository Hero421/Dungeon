from Blocks.module_metaSurfaces import Floor, Wall, Ground

from Blocks.Trigers.module_Simulator import Simulator
from Blocks.Trigers.module_Portal import Portal
from Blocks.Trigers.module_Source import Source
from Blocks.Trigers.module_Chest  import Chest
from Blocks.Trigers.module_Table  import Table
from Blocks.Trigers.module_Spike  import Spike
from Blocks.Trigers.module_Door   import Door

class Rooms(object):
	'''
	docstring for Rooms
	'''
	def __init__(self, row, elm, ses_area, veiws=[], width=5, height=5):
		self.row = row
		self.elm = elm
		print(self.row)
		print(self.elm)
		input()
		self.veiws = veiws
		self.width = width
		self.height= height
		self.area = ses_area
		self.map  = ses_area.map
		self.choice()

	def choice(self, ways):
		room = Room(self.row, self.elm, self.veiws[0])
		del self.veiws[0]
		for veiw in self.veiws:
			way = random.choice(ways)
			self.spawn(way, veiw)
	
	def spawn(self, way, veiw, ways):
		if way == 'up':
			if self.row - 4 - self.height in range(self.area.rows):
				room = Room(self.row - self.height - 4, self.elm, veiw, self.width, self.height)
				room.spawn()
				del room
				self.row -= self.height - 4
			else:
				way = random.choice(ways)
				self.spawn(way, veiw)

		elif way == 'right':
			if self.elm + 4 + self.width in range(self.area.elms):
				room = Room(self.row, self.elm + self.width + 4, veiw, self.width, self.height)
				room.spawn()
				del room
				self.elm += self.width + 4
			else:
				way = random.choice(ways)
				self.spawn(way, veiw)

		elif way == 'down':
			if self.row + 4 + self.height in range(self.area.rows):
				room = Room(self.row + self.height + 4, self.elm, veiw, self.width, self.height)
				room.spawn()
				self.row += self.height + 4
			else:
				way = random.choice(ways)
				self.spawn(way, veiw)

		elif way == 'left':
			if self.elm - 4 - self.width in range(self.area.elms):
				room = Room(self.row, self.elm - self.width - 4, veiw, self.width, self.height)
				room.spawn()
				self.elm += self.width + 4
			else:
				way = random.choice(ways)
				self.spawn(way, veiw)

class Room(object):

	def __init__(self, strt_row, strt_elm, ses_area, veiw=None, width=5, height=5):
		if veiw:
			self.veiw = veiw
		else:
			self.veiw = random.choice(['room with the monster', 'room with the chest', 'a room with a chest and a monster'])
		self.strt_elm = strt_elm
		self.strt_row = strt_row
		self.width  = width
		self.height = height
		self.fin_elm = self.strt_elm + self.width
		self.fin_row = self.strt_row + self.height
		self.map = ses_area.map


	def spawn(self):

		for row in range(-1, self.fin_row - self.strt_row - 1):
			for elm in range(-1, self.fin_elm - self.strt_elm - 1):
				self.map[self.strt_row + row][self.strt_elm + elm] = Wall()

		for row in range(self.fin_row - self.strt_row - 2):
			for elm in range(self.fin_elm - self.strt_elm - 2):
				self.map[self.strt_row + row][self.strt_elm + elm] = Floor()

		self.map[self.fin_row - 2][self.strt_elm + int(self.width/2) - 1] = Ground()
		self.map[self.fin_row - 1][self.strt_elm + int(self.width/2) - 1] = Ground()

		if self.veiw == 'the initial room':
			self.map[self.strt_row][self.strt_elm] = Chest()
			self.map[self.strt_row + 1][self.strt_elm] = Portal()
			self.map[self.strt_row][self.fin_elm - 3] = Source()
			self.map[self.fin_row - 1][self.strt_elm + int(self.width/2) - 2] = Table('Test table')
			self.map[self.fin_row][self.strt_elm] = Spike()
			self.map[self.fin_row - 1][self.strt_elm + int(self.width/2)] = Simulator()
			self.map[self.fin_row - 2][self.strt_elm + int(self.width/2) - 1] = Door()

		elif self.veiw == 'end room':
			self.map[self.strt_row][self.strt_elm] = Portal()
			self.map[self.strt_row + 2][self.strt_elm] = Source()
			self.map[self.strt_row][self.strt_elm + 2] = Chest()

		elif self.veiw == 'room with the monster':
			self.map[self.strt_row + int(self.height/2)][self.strt_elm + int(self.width/2)] = Goblin()

		elif self.veiw == 'room with the chest':
			self.map[self.strt_row + int(self.height/2)][self.strt_elm + int(self.width/2)] = Chest()

		elif self.veiw == 'a room with a chest and a monster':
			self.map[self.strt_row + int(self.height/2)][self.strt_elm + int(self.width/2)] = Chest()
			self.map[self.strt_row + int(self.height/2)][self.strt_elm + int(self.width/2) + 1] = Goblin()

		elif self.veiw == 'shop':
			self.map[self.strt_row + int(self.height/2)][self.strt_elm + int(self.width/2)] = Trader()
			