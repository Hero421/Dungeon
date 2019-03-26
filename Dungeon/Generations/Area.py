from Generations.Chank import Chank
from random import randint

from Blocks.Containers.Wall import Wall
from Blocks.Air import Air

from Generations.Rooms import Room
from links import ses_avatars, clear
import links

class Map(list):

	def __new__(cls, lst):
		if type(lst) is list:
			return list.__new__(cls, list)

	def __init__(self, lst):
		self.list = lst

	def __len__(self):
		return self.list.__len__()

	def __iter__(self):
		return self.list.__iter__()

	def __next__(self):
		return self[self.list.index(self.list.__next__()) - int(self.list.__len__()/2)]

	def __index__(self, obj):

		idx = -int(self.list.__len__()/2)

		for elm in self.list:
			if elm is obj:
				return idx
			idx += 1

		raise AttributeError(f'{obj} is not in list')

	def __getitem__(self, n):

		idx = -int(self.list.__len__()/2)
		radius = -idx

		if isinstance(n, slice):
			return self.list[n.start-radius : n.stop-radius : n.step]

		else:
			for elm in self.list:
				if idx == n and not type(elm) is None:
					return elm
				idx += 1

			raise IndexError(f'index {n} is not in list')

			if -(3*radius) < n < -radius:
				return self.list[n + radius]

	def __setitem__(self, n, value):

		idx = -int(self.list.__len__()/2)
		radius = -idx

		error = True
		cont  = True

		for index in range(self.list.__len__()):
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
				raise IndexError(f'index {n} is not in list')

class Area(object):

	def __init__( self, 
				  name, 
				  layers, rows, elms,
				  length_of_chank=10,
				  ):
		self.name   = name
		self.lays   = layers + 4
		self.rows   = rows + 4
		self.elms   = elms + 4
		self.length_of_chank = length_of_chank
		links.levels.append(self)
		if not links.ses_area:
			self.generator()

	def generator(self):
		'''
		Create features on the map
		'''

		links.ses_area = self

		clear()

		print(self.name)
		print('\ncreate a big dummy')

		self.map = 	Map([
						Map([
							Map(
								[int() for elm in range(self.elms)]
								) 
							for row in range(self.rows)
							])
						for lay in range(self.lays)
						])

		self.chank_map = Map([
							Map([
								Map([
									Chank(lay, row, elm, self, length=self.length_of_chank)

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
							for lay in range(
											-int(self.lays/(self.length_of_chank*2)),
											 int(self.lays/(self.length_of_chank*2))
											)
							])

		chank = self.chank_map[0][0][0]

		chank.generator()
		chank.msg()

		clear()
		print(self.name)
		print('\ncreate the boundaries of the world')

		for lay in self.map:

			for row in lay:
				row[-int(len(self.map)/2)-1] = Wall()
				row[ int(len(self.map)/2)-1] = Wall()

			for elm in range(-int(len(self.map[0][0])/2), int(len(self.map[0][0])/2)-1):
				lay[-int(len(self.map)/2)][elm] = Wall()
				lay[ int(len(self.map)/2)-2][elm] = Wall()

		clear()
		print(self.name)
		print('\ncreate the final room')

		# while True:
		# 	end_room_elm = randint(1, self.elms)
		# 	end_room_row = randint(1, self.rows)
		# 	if  end_room_row in range(self.rows//2 - 7, self.rows//2 + 7) or \
		# 		end_room_row in range(self.rows//2 + 8, self.elms//2 - 8) or \
		# 		end_room_elm in range(self.elms//2 - 7, self.elms//2 + 7) or \
		# 		end_room_elm in range(self.elms//2 + 8, self.elms//2 - 8) or \
		# 		end_room_elm > self.elms - 5 or \
		# 		end_room_row > self.rows - 5:
		# 		continue
		# 	else:
		# 		break

		# Room(generation='end room').spawn(lay, end_room_row-int(self.rows/2), end_room_elm-int(self.elms/2), self.map)

	def print_map(self, id_, radius=5):
		'''
		Show the map and the objects on it to the player
		'''

		from links import ses_avatars
		
		avatar = ses_avatars[id_]
		a = avatar

		strt_row = min([a.row - radius  , len(self.map) - a.row])
		fin_row  = a.row + min([radius+1, int(len(self.map)/2) - a.row-1])

		strt_elm = min([a.elm - radius  , len(self.map) - a.elm])
		fin_elm  = a.elm + min([radius+1, int(len(self.map)/2) - a.elm-1])

		for row in a.map[a.lay][strt_row : fin_row]:
			print(' '.join([
								elm.des(a.lay, self.map[a.lay].__index__(row), row.__index__(elm), self.map) 
								if type(elm) is Air 
								else 
								elm.des 

							for elm in row[strt_elm : fin_elm]
						   ]
						  )
				 )