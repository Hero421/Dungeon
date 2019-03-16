from module_Chank import Chank
from random import randint

from Blocks.module_Surfaces import Wall

from module_Rooms import Room
from module_links import ses_avatars, clear
import module_links

class Map(list):

	def __new__(cls, lst):
		if type(lst) is list:
			return list.__new__(cls, list)

	def __init__(self, lst):
		self.list = lst

	def __len__(self):
		return len(self.list)

	def __iter__(self):
		return self.list.__iter__()

	def __next__(self):
		return self[self.list.index(self.list.__next__()) - int(len(self.list/2))]

	def __index__(self, obj):

		idx = -int(len(self.list)/2)

		for elm in self.list:
			if elm is obj:
				return idx
			idx += 1

		raise AttributeError(str(obj) + 'is not in list')

	def __getitem__(self, n):

		idx = -int(len(self.list)/2)
		radius = -idx

		if isinstance(n, slice):
			return self.list[n.start-radius : n.stop-radius : n.step]

		else:
			for elm in self.list:
				if idx == n and elm:
					return elm
				idx += 1

			if -(3*radius) < n < -radius:
				return self.list[n + radius]

			raise IndexError('index ' + str(n) + ' is not in list')

	def __setitem__(self, n, value):

		idx = -int(len(self.list)/2)
		radius = -idx

		error = True
		cont  = True

		for index in range(len(self.list)):
			if idx == n:
				self.list[index] = value
				cont = False
				break
			idx += 1

		if cont:

			if -(3*radius) < n < -radius:
				self.list[n + radius] = value
				error = False

			if error:
				raise IndexError('index ' + str(n) + ' is not in list')

class Area(object):

	def __init__( self, 
				  name, 
				  rows, elms,
				  length_of_chank=10,
				  stones=50, 
				  spikes=11, 
				  chasms=4, 
				  enemys=3
				  ):
		self.name   = name
		self.rows   = rows + 4
		self.elms   = elms + 4
		self.length_of_chank = length_of_chank
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

		self.map = Map([
						Map(
							[Wall() for elm in range(self.elms)]
							) 
						for row in range(self.rows)
						])

		self.chank_map = Map([
							Map([
								Chank(row, elm, self, length=self.length_of_chank)

									for elm in range(
													-int(self.elms/(self.length_of_chank*2)),
													 int(self.elms/(self.length_of_chank*2))
													)
								])
							for row in range(
											-int(self.rows/(self.length_of_chank*2)),
											 int(self.rows/(self.length_of_chank*2))
											)
							])

		# self.chank_map[0][0].msg()

		clear()
		print(self.name)
		print('\ncreate the boundaries of the world')

		for row in self.map:
			row[int(len(row)/2)-1] = Wall()

		for elm in range(-int(len(self.map[0])/2), int(len(self.map[0])/2)-1):
			self.map[-int(len(self.map)/2)][elm] = Wall()
			self.map[ int(len(self.map)/2)-2][elm] = Wall()

		for row in self.map.list:
			row[-int(len(self.map)/2)  ] = Wall()
			row[ int(len(self.map)/2)-1] = Wall()

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

		Room(generation='end room').spawn(end_room_row-int(self.rows/2), end_room_elm-int(self.elms/2), self.map)

	def print_map(self, id_, radius=5):
		'''
		Show the map and the objects on it to the player
		'''

		from module_links import ses_avatars
		
		avatar = ses_avatars[id_]

		strt_row = min([avatar.location['row'] - radius  , len(self.map) - avatar.location['row']])
		fin_row  = avatar.location['row'] + min([radius+1, int(len(self.map)/2) - avatar.location['row']-1])

		strt_elm = min([avatar.location['elm'] - radius  , len(self.map) - avatar.location['elm']])
		fin_elm  = avatar.location['elm'] + min([radius+1, int(len(self.map)/2) - avatar.location['elm']-1])

		for row in avatar.map[strt_row : fin_row]:
			print(' '.join([str(elm) if type(elm) is int else elm.des for elm in row[strt_elm : fin_elm]]))