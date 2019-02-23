from module_Chank import Chank
from random import randint

from Blocks.module_metaSurfaces import Wall

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

		self.chank_map = [[Chank(row, elm, self, ses_avatars) for elm in range(int(self.elms/50))] for row in range(int(self.rows/50))]

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
			room_elm  = randint(1, self.elms)
			room_row = randint(1, self.rows)
			if room_elm in range(self.elms//2 - 7, self.elms//2 + 7) or room_row in range(self.rows//2 - 7, self.rows//2 + 7) or room_elm > self.elms - 5 or room_row > self.rows - 5 or room_elm in range(self.elms//2 + 8, self.elms//2 - 8) or room_row in range(self.rows//2 + 8, self.elms//2 - 8):
				continue
			else:
				break

		_End_room = Room(room_row, room_elm, self, 'end room')
		_End_room.spawn()

	def print_map(self, id):
		'''
		Create the map and the objects on it to the player
		'''
		
		map = []

		from module_links import ses_avatars, ses_area
		
		location = ses_avatars[id].location

		new_rows = []

		for row in ses_area.map:
			if ses_area.map.index(row) in range(location['row'] - 5, location['row'] + 6):
				new_rows.append(row)

		for row in new_rows:
			rows = []
			for elm in row:
				if row.index(elm) in range(location['elm'] - 5, location['elm'] + 6):
					rows.append(elm)
			print(' '.join([elm.des for elm in rows]))
