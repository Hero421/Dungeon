from random import choice, randint

from Blocks.module_Surfaces import Floor, Wall, Ground
from Blocks.Trigers.module_Simulator import Simulator
from Blocks.Trigers.module_Portal import Portal
from Blocks.Trigers.module_Source import Source
from Blocks.Trigers.module_Chest  import Chest
from Blocks.Trigers.module_Table  import Table
from Blocks.Trigers.module_Spike  import Spike
from Blocks.Trigers.module_Door   import Door

from Blocks.module_Stone import Stone

from Enemys.module_metaEnemy import Enemy

from module_links import ways

from pprint import pprint

class Rooms(object):
	'''
	docstring for Rooms
	'''

	def __init__(self, generations=None, num=None, doors='on', width=5, height=5, lenght=2):

		self.doors = doors

		if len(generations) > 1:
			if not num:

				chance = randint(1, 100)

				if chance in range(2):
					num = 5
				elif chance in range(8):
					num = 4
				elif chance in range(20):
					num = 3
				elif chance in range(50):
					num = 2
				else:
					num = 1

			self.map_of_rooms = [[' ' for elm in range(20)] for row in range(20)]
			self.room_row = 10
			self.room_elm = 10
		
		self.width  = width
		self.height = height
		
		self.lenght = lenght

		if not generations:
			self.generations = [choice(['room with the monster', 'room with the chest', 'a room with a chest and a monster']) for count in range(num)]
		else:
			self.generations = generations

	def spawn(self, row, elm, map_):

		way = True
		var = True

		if len(self.generations) > 1:
			for generation in self.generations:

				Room(way, generation=generation, doors=self.doors, width=self.width, height=self.height).spawn(row, elm, map_)

				self.map_of_rooms[self.room_row][self.room_elm] = 'R'

				while True:

					way = choice(['up', 'right', 'down', 'left'])

					if way == 'up':
						if self.map_of_rooms[self.room_row - 2][self.room_elm] != 'R':
							break
					elif way == 'right':
						if self.map_of_rooms[self.room_row][self.room_elm + 2] != 'R':
							break
					elif way == 'down':
						if self.map_of_rooms[self.room_row + 2][self.room_elm] != 'R':
							break
					elif way == 'left':
						if self.map_of_rooms[self.room_row][self.room_elm - 2] != 'R':
							break
				
				if way == 'up':
					row -= self.height + self.lenght
					self.room_row -= 2
					if var:
						Corridor('vertical', doors=self.doors, lenght=self.lenght).spawn(row+self.height-1, elm+1, map_)
						self.map_of_rooms[self.room_row + 1][self.room_elm] = 'C'

				elif way == 'right':
					elm += self.width + self.lenght
					self.room_elm += 2
					if var:
						Corridor('horizontal', doors=self.doors, lenght=self.lenght).spawn(row+1, elm-self.lenght-1, map_)
						self.map_of_rooms[self.room_row][self.room_elm - 1] = 'C'

				elif way == 'down':
					row += self.height + self.lenght
					self.room_row += 2
					if var:
						Corridor('vertical', doors=self.doors, lenght=self.lenght).spawn(row-self.lenght-1, elm+1, map_)
						self.map_of_rooms[self.room_row - 1][self.room_elm] = 'C'

				elif way == 'left':
					elm -= self.width + self.lenght
					self.room_elm -= 2
					if var:
						Corridor('horizontal', doors=self.doors, lenght=self.lenght).spawn(row+1, elm+self.width-1, map_)
						self.map_of_rooms[self.room_row][self.room_elm + 1] = 'C'

				if generation == self.generations[-1]:
					var = False
					Room(way, type_='last_room', generation=generation, doors=self.doors, width=self.width, height=self.height).spawn(row, elm, map_)
					break
		else:
			Room(way, type_='last_room', generation=self.generations, doors=self.doors, width=self.width, height=self.height).spawn(row, elm, map_)


class Room(object):

	def __init__(self, way=choice([ways]), type_='common', generation=choice(['room with the monster', 'room with the chest', 'a room with a chest and a monster']), doors='on', width=5, height=5):
		self.generation = generation
		self.way = way
		self.type_ = type_
		self.doors = doors
		self.width  = width
		self.height = height

	def spawn(self, strt_row, strt_elm, map_):

		fin_elm = strt_elm + self.width
		fin_row = strt_row + self.height

		for row in range(-1, fin_row - strt_row - 1):
			for elm in range(-1, fin_elm - strt_elm - 1):
				if not type(map_[strt_row + row][strt_elm + elm]) in (Door, Floor):
					map_[strt_row + row][strt_elm + elm] = Wall()

		for row in range(fin_row - strt_row - 2):
			for elm in range(fin_elm - strt_elm - 2):
				map_[strt_row + row][strt_elm + elm] = Floor()
		
		choice = Door if self.doors == 'on' else Floor

		if self.way == 'up':
			if self.type_ == 'last_room':
				rand = randint(1, 3)
				if rand == 1:
					map_[strt_row + int(self.height/2)-1][strt_elm-1] = choice()
				elif rand == 2:
					map_[strt_row-1][strt_elm + int(self.width/2)-1] = choice()
				elif rand == 3:
					map_[strt_row + int(self.height/2)-1][fin_elm-2] = choice()
		elif self.way == 'right':
			if self.type_ == 'last_room':
				rand = randint(1, 3)
				if rand == 1:
					map_[fin_row-2][strt_elm + int(self.width/2)-1] = choice()
				elif rand == 2:
					map_[strt_row-1][strt_elm + int(self.width/2)-1] = choice()
				elif rand == 3:
					map_[strt_row + int(self.height/2)-1][fin_elm-2] = choice()
		elif self.way == 'down':
			if self.type_ == 'last_room':
				rand = randint(1, 3)
				if rand == 1:
					map_[fin_row-2][strt_elm + int(self.width/2)-1] = choice()
				elif rand == 2:
					map_[strt_row + int(self.height/2)-1][strt_elm-1] = choice()
				elif rand == 3:
					map_[strt_row + int(self.height/2)-1][fin_elm-2] = choice()
		elif self.way == 'left':
			if self.type_ == 'last_room':
				rand = randint(1, 3)
				if rand == 1:
					map_[fin_row-2][strt_elm + int(self.width/2)-1] = choice()
				if rand == 2:
					map_[strt_row + int(self.height/2)-1][strt_elm-1] = choice()
				if rand == 3:
					map_[strt_row-1][strt_elm + int(self.width/2)-1] = choice()

		if self.generation == 'the initial room':
			map_[strt_row][strt_elm] = Chest()
			map_[strt_row + 2][strt_elm] = Portal()
			map_[strt_row][fin_elm - 3] = Source()
			map_[fin_row - 1][strt_elm + int(self.width/2) - 2] = Table('Test table')
			map_[fin_row][strt_elm] = Spike()
			map_[fin_row - 1][strt_elm + int(self.width/2)] = Simulator()
			map_[fin_row - 2][strt_elm + int(self.width/2) - 1] = choice()

		elif self.generation == 'end room':
			map_[strt_row][strt_elm] = Portal()
			map_[strt_row + 2][strt_elm] = Source()
			map_[strt_row][strt_elm + 2] = Chest()

		elif self.generation == 'room with the monster':
			Enemy().spawn(strt_row + int(self.height/2), strt_elm + int(self.width/2), map_)

		elif self.generation == 'room with the chest':
			map_[strt_row + int(self.height/2)-1][strt_elm + int(self.width/2)-1] = Chest()

		elif self.generation == 'a room with a chest and a monster':
			map_[strt_row + int(self.height/2)][strt_elm + int(self.width/2)] = Chest()
			Enemy().spawn(strt_row + int(self.height/2), strt_elm + int(self.width/2) + 1, map_)

		elif self.generation == 'shop':
			map_[strt_row + int(self.height/2)][strt_elm + int(self.width/2)] = Trader()


class Corridor(object):
	"""
	docstring for Corridor
	"""
	def __init__(self, type_, doors='on', lenght=2):
		
		self.type_ = type_ # 'horizontal'/'vertical'
		self.doors = doors
		self.lenght = lenght

	def spawn(self, row, elm, map_):

		# start: {'row': start_row, 'elm': start_elem} on the map
		
		choice = Door if self.doors == 'on' else Floor
		
		if self.type_ == 'horizontal':

			for count in range(self.lenght):
				map_[row][elm + count] = Floor()
				map_[row+1][elm + count] = Wall()
				map_[row-1][elm + count] = Wall()

			map_[row][elm-1] = choice()
			map_[row][elm+self.lenght] = choice()

		elif self.type_ == 'vertical':

			for count in range(self.lenght):
				map_[row + count][elm] = Floor()
				map_[row + count][elm+1] = Wall()
				map_[row + count][elm-1] = Wall()

			map_[row-1][elm] = choice()
			map_[row+self.lenght][elm] = choice()