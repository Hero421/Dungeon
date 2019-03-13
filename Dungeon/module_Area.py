from module_Chank import Chank
from random import randint

from Blocks.module_Surfaces import Wall

from module_Rooms import Room
from module_links import ses_avatars, clear
import module_links

class Map(list):

	def __new__(cls, lst):
		return list.__new__(cls, list)

	def __init__(self, lst):
		self.list = lst
		self.len  = 0
		for _ in self.list:
			self.len += 1

	def __getitem__(self, n):

		idx = -int(len(self.list)/2)

		for elm in self.list:
			if idx == n:
				return elm
			idx += 1

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
		self.rows   = rows
		self.elms   = elms
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

		clear()
		print(self.name)
		print('\ncreate a big dummy')

		self.map = Map([Map([None for elm in range(self.elms)]) for row in range(self.rows)])
		self.chank_map = Map([Map([Chank(row, elm) for elm in range(int(self.elms/10))]) for row in range(int(self.rows/10))])

		clear()
		print(self.name)
		print('\ncreate the boundaries of the world')

		for row in range(len(self.map)):
			self.map[row][self.elms - 1] = Wall()

		for elm in self.map[-int(self.map.len/2)]:
			elm = Wall()

		for elm in self.map[int(self.map.len/2)]:
			elm = Wall()

		for row in self.map:
			row[-int(self.map.len/2)] = Wall()
			row[ int(self.map.len/2)] = Wall()

		clear()
		print(self.name)
		print('\ncreate the final room')

		while True:
			end_room_elm = randint(1, self.elms)
			end_room_row = randint(1, self.rows)
			if  end_room_row in range(self.rows//2 - 7, self.rows//2 + 7) or \
				end_room_row in range(self.rows//2 + 8, self.elms//2 - 8) or \
				end_room_elm in range(self.elms//2 - 7, self.elms//2 + 7) or \
				end_room_elm in range(self.elms//2 + 8, self.elms//2 - 8) or \
				end_room_elm > self.elms - 5 or \
				end_room_row > self.rows - 5:
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
		
		avatar = ses_avatars[id_]

		if avatar.location['row'] < radius:
			radius_row = avatar.location['row']

		if avatar.location['elm'] < radius:
			radius_elm = avatar.location['elm']

		for row in avatar.map[avatar.location['row'] - radius_row : avatar.location['row'] + radius+1]:
			print(' '.join([elm.des for elm in row[avatar.location['elm'] - radius_elm : avatar.location['elm'] + radius+1]]))