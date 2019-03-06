from module_Chank import Chank
from random import randint

from Blocks.module_Surfaces import Wall

from module_Rooms import Room
from module_links import levels, ses_avatars
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

		self.fst_chank = self.chank_map[int(len(self.chank_map)/2)][int(len(self.chank_map[int(len(self.chank_map)/2)])/2)]

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
			if end_room_elm in range(self.elms//2 - 7, self.elms//2 + 7) or end_room_row in range(self.rows//2 - 7, self.rows//2 + 7) or end_room_elm > self.elms - 5 or end_room_row > self.rows - 5 or end_room_elm in range(self.elms//2 + 8, self.elms//2 - 8) or end_room_row in range(self.rows//2 + 8, self.elms//2 - 8):
				continue
			else:
				break

		Room('end room').spawn(end_room_row, end_room_elm, self.map)

	def print_map(self, id):
		'''
		Create the map and the objects on it to the player
		'''

		from module_links import ses_avatars
		
		location = ses_avatars[id].location

		new_rows = []

		for row in ses_avatars[id].map:
			if ses_avatars[id].map.index(row) in range(location['row'] - 11, location['row'] + 12):
				new_rows.append(row)

		for row in new_rows:
			rows = []
			for elm in row:
				if row.index(elm) in range(location['elm'] - 11, location['elm'] + 12):
					rows.append(elm)
			print(' '.join([elm.des for elm in rows]))
