from module_Chank import Chank
from random import randint

from Blocks.module_Surfaces import Wall

from module_Rooms import Room
from module_links import ses_avatars
import module_links

class Area(object):

	def __init__( self, 
				  name, 
				  rows, elms,
				  stones=50, 
				  spikes=11, 
				  chasms=4, 
				  enemys=3
				  ):
		self.name   = name
		self.rows   = rows + 2
		self.elms   = elms + 2
		self.stones = stones
		self.spikes = spikes
		self.chasms = chasms
		self.enemys = enemys
		module_links.levels.append(self)
		if not module_links.ses_area:
			self.generator()

	def generator(self):
		'''
		Create features on the map
		'''

		module_links.ses_area = self

		self.map = [[None for elm in range(self.elms)] for row in range(self.rows)]

		self.chank_map = [[Chank(row, elm) for elm in range(int(self.elms/10))] for row in range(int(self.rows/10))]

		for row in self.map:
			self.map[self.map.index(row)][self.elms - 1] = Wall()

		for row in self.map:
			for elm in row:
				if self.map[0] == row or self.map[self.rows - 1] == row:
					self.map[self.map.index(row)][row.index(elm)] = Wall()
				elif self.map[self.map.index(row)][0] == elm:
					self.map[self.map.index(row)][row.index(elm)] = Wall()

		while True:
			end_room_elm = randint(1, self.elms)
			end_room_row = randint(1, self.rows)
			if end_room_elm in range(self.elms//2 - 7, self.elms//2 + 7) or end_room_row in range(self.rows//2 - 7, self.rows//2 + 7) or end_room_row in range(self.rows//2 + 8, self.elms//2 - 8) or end_room_elm in range(self.elms//2 + 8, self.elms//2 - 8) or end_room_elm > self.elms - 5 or end_room_row > self.rows - 5:
				continue
			else:
				break

		Room(generation='end room').spawn(end_room_row, end_room_elm, self.map)

	def print_map(self, id_, radius=5):
		'''
		Show the map and the objects on it to the player
		'''

		radius_row = radius
		radius_elm = radius

		from module_links import ses_avatars
		
		location = ses_avatars[id_].location

		if location['row'] < radius:
			radius_row = location['row']

		if location['elm'] < radius:
			radius_elm = location['elm']

		for row in ses_avatars[id_].map[location['row'] - radius_row : location['row'] + radius+1]:
			print(' '.join([elm.des for elm in row[location['elm'] - radius_elm : location['elm'] + radius+1]]))