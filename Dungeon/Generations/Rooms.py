from random import choice, randint

from NPC.Trader import Trader
from Blocks.Containers.Wood_block   import WoodBlock
from Blocks.Containers.Ground_block import GroundBlock
from Blocks.Trigers.Simulator       import Simulator
from Blocks.Trigers.Workbench       import Workbench
from Blocks.Trigers.Portal          import Portal
from Blocks.Trigers.Source          import Source
from Blocks.Trigers.Chest           import Chest
from Blocks.Trigers.Table           import Table
from Blocks.Trigers.Spike           import Spike
from Blocks.Trigers.Oven            import Oven
from Blocks.Trigers.Door            import Door
from Blocks.Air import Air

from Enemys.metaEnemy import Enemy

from links import WAYS

class Rooms(object):
	'''
	Rooms(

		  [the generation you need] or None, 
		  quantity you need or None, 
		  doors='on'/'off', 
		  HEIGHT= and WIDTH= of rooms,
		  LEN_OF_COR=corridor length

		 ).spawn(

		  row on the map,
		  elm on the map,
		  and map

		 )
	'''

	def __init__(self, 
				 generations=None, 
				 num=None,
				 HEIGHT=5,
				 WIDTH =5,
				 LENGTH=5,
				 LEN_OF_COR=2):

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
		
		self.HEIGHT = HEIGHT
		self.WIDTH  = WIDTH
		self.LENGTH = LENGTH
		
		self.LEN_OF_COR = LEN_OF_COR

		if not generations:
			self.generations = [choice(['room with the monster', 'room with the chest', 'a room with a chest and a monster']) for count in range(num)]
		else:
			self.generations = generations

	def spawn(self, lay, row, elm, map_):

		way = True
		var = True

		if len(self.generations) > 1:
			for generation in self.generations:

				if generation == self.generations[-1]:
					var = False
					Room(way, generation=generation, WIDTH=self.WIDTH, LENGTH=self.LENGTH).spawn(lay, row, elm, map_)
					break

				Room(way, generation=generation, WIDTH=self.WIDTH, LENGTH=self.LENGTH).spawn(lay, row, elm, map_)
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
					row -= self.LENGTH + self.LEN_OF_COR
					self.room_row -= 2
					if var:
						Corridor('vertical', LENGTH=self.LEN_OF_COR).spawn(lay-1, row+self.LENGTH-1, elm+1, map_)
						self.map_of_rooms[self.room_row + 1][self.room_elm] = 'C'

				elif way == 'right':
					elm += self.WIDTH + self.LEN_OF_COR
					self.room_elm += 2
					if var:
						Corridor('horizontal', LENGTH=self.LEN_OF_COR).spawn(lay-1, row+1, elm-self.LEN_OF_COR-1, map_)
						self.map_of_rooms[self.room_row][self.room_elm - 1] = 'C'

				elif way == 'down':
					row += self.LENGTH + self.LEN_OF_COR
					self.room_row += 2
					if var:
						Corridor('vertical', LENGTH=self.LEN_OF_COR).spawn(lay-1, row-self.LEN_OF_COR-1, elm+1, map_)
						self.map_of_rooms[self.room_row - 1][self.room_elm] = 'C'

				elif way == 'left':
					elm -= self.WIDTH + self.LEN_OF_COR
					self.room_elm -= 2
					if var:
						Corridor('horizontal', LENGTH=self.LEN_OF_COR).spawn(lay-1, row+1, elm+self.WIDTH-1, map_)
						self.map_of_rooms[self.room_row][self.room_elm + 1] = 'C'

		else:
			Room(way, generation=self.generations, HEIGHT=self.HEIGHT, WIDTH=self.WIDTH, LENGTH=self.LENGTH).spawn(row, elm, map_)


class Room(object):

	def __init__(self, 
				 way=choice(['North', 'South', 'East', 'West']),
				 generation=choice(['room with the monster', 'room with the chest', 'a room with a chest and a monster']),
				 HEIGHT=5,
				 WIDTH=5, 
				 LENGTH=5):
		self.generation = generation
		self.way = way
		self.HEIGHT = HEIGHT
		self.WIDTH  = WIDTH
		self.LENGTH = LENGTH

	def spawn(self, strt_lay, strt_row, strt_elm, map_):

		fin_lay = strt_lay + self.HEIGHT
		fin_row = strt_row + self.LENGTH
		fin_elm = strt_elm + self.WIDTH

		for lay in range(-1, fin_lay - strt_lay + 1):
			for row in range(-1, fin_row - strt_row - 1):
				for elm in range(-1, fin_elm - strt_elm - 1):
					map_[strt_lay + lay][strt_row + row][strt_elm + elm] = WoodBlock()

		for lay in range(-1, fin_lay - strt_lay + 1):
			for row in range(fin_row - strt_row - 2):
				for elm in range(fin_elm - strt_elm - 2):
					map_[strt_lay + lay][strt_row + row][strt_elm + elm] = WoodBlock() if lay in (strt_lay-1, fin_lay) else Air()

		if self.generation == 'the initial room':
			map_[strt_lay][strt_row][strt_elm] = Chest()
			map_[strt_lay][strt_row + 2][strt_elm] = Oven()
			map_[strt_lay][strt_row + 2][strt_elm + 2] = Workbench()
			map_[strt_lay][strt_row][fin_elm - 3] = Trader()
			map_[strt_lay][fin_row - 1][strt_elm + int(self.WIDTH/2) - 2] = Table('Test table')
			map_[strt_lay][fin_row - 1][strt_elm + int(self.WIDTH/2)] = Simulator()

		elif self.generation == 'end room':
			map_[strt_lay][strt_row][strt_elm] = Portal()
			map_[strt_lay][strt_row + 2][strt_elm] = Source()
			map_[strt_lay][strt_row][strt_elm + 2] = Chest()

		elif self.generation == 'room with the monster':
			Enemy().spawn(strt_lay, strt_row + int(self.LENGTH/2), strt_elm + int(self.WIDTH/2), map_)

		elif self.generation == 'room with the chest':
			map_[strt_lay][strt_row + int(self.LENGTH/2)-1][strt_elm + int(self.WIDTH/2)-1] = Chest()

		elif self.generation == 'a room with a chest and a monster':
			map_[strt_lay][strt_row + int(self.LENGTH/2)][strt_elm + int(self.WIDTH/2)] = Chest()
			Enemy().spawn(strt_row + int(self.LENGTH/2), strt_elm + int(self.WIDTH/2) + 1, map_)

		elif self.generation == 'shop':
			map_[strt_lay][strt_row + int(self.LENGTH/2)][strt_elm + int(self.WIDTH/2)] = Trader()


class Corridor(object):
	"""
	docstring for Corridor
	"""
	def __init__(self, orientation, LENGTH=2, HEIGHT=3):
		
		self.orientation = orientation # 'horizontal'/'vertical'
		self.LENGTH = LENGTH
		self.HEIGHT = HEIGHT

	def spawn(self, lay, row, elm, map_):

		# start: {'row': start_row, 'elm': start_elem} on the map

		if self.orientation == 'horizontal':

			for count_elm in range(self.LENGTH):
				for count_lay in range(self.HEIGHT):
					map_[lay+count_lay][row  ][elm+count_elm] = WoodBlock() if count_lay in (0, self.HEIGHT) else Air()
					map_[lay+count_lay][row+1][elm+count_elm] = WoodBlock()
					map_[lay+count_lay][row-1][elm+count_elm] = WoodBlock()

		elif self.orientation == 'vertical':

			for count_row in range(self.LENGTH):
				for count_lay in range(self.HEIGHT):
					map_[lay+count_lay][row+count_row][elm  ] = WoodBlock() if count_lay in (0, self.HEIGHT) else Air()
					map_[lay+count_lay][row+count_row][elm+1] = WoodBlock()
					map_[lay+count_lay][row+count_row][elm-1] = WoodBlock()