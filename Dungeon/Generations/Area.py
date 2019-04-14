from math import ceil
from random import randint

from Generations.Vector import Vector
from Generations.Chank import Chank
from Generations.Rooms import Room
from Generations.Map import Map

from Blocks.Containers.Wall import Wall
from Blocks.Trigers.Spike import Spike
from Blocks.Air import Air

from links import ses_avatars, clear, NewInt
import links

class Area(object):

	def __init__( self, 
				  name, 
				  layers, rows, elems,
				  len_of_chank=10,
				  ):
		self.name = name
		self.LAYS = layers + 4
		self.ROWS = rows   + 4
		self.ELMS = elems  + 4
		self.LEN_OF_CHANK = len_of_chank
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
								[NewInt() for elm in range(self.ELMS)]
								) 
							for row in range(self.ROWS)
							])
						for lay in range(self.LAYS)
						])

		self.chank_map = Map([
							Map([
								Map([
									Chank(lay, row, elm, self, length=self.LEN_OF_CHANK)

										for elm in range(
														-int(self.ELMS/(self.LEN_OF_CHANK*2)),
														 int(self.ELMS/(self.LEN_OF_CHANK*2))
														)
									])
								for row in range(
												-int(self.ROWS/(self.LEN_OF_CHANK*2)),
												 int(self.ROWS/(self.LEN_OF_CHANK*2))
												)
								])
							for lay in range(
											-int(self.LAYS/(self.LEN_OF_CHANK*2)),
											 int(self.LAYS/(self.LEN_OF_CHANK*2))
											)
							])

		self.vector_map = Map([Map([[] for elm in range(ceil(self.ELMS/self.LEN_OF_CHANK))]) for row in range(ceil(self.ROWS/self.LEN_OF_CHANK))])

		map_ = Map([Map([None for elm in range(ceil(self.ELMS/self.LEN_OF_CHANK+2))]) for row in range(ceil(self.ROWS/self.LEN_OF_CHANK+2))])

		vector_row = -ceil(len(self.vector_map)/2)
		for row in range(-map_.RADIUS, map_.RADIUS):
			vector_elm = -ceil(len(self.vector_map[0])/2)
			for elm in range(-map_[0].RADIUS, map_[0].RADIUS):
				map_[row][elm] = Vector(vector_elm, vector_row)
				vector_elm += 1
			vector_row += 1

		vector_row = -ceil(len(self.vector_map)/2)+1
		for row in range(-map_.RADIUS, map_.RADIUS-1):
			vector_elm = -ceil(len(self.vector_map[0])/2)+1
			for elm in range(-map_[0].RADIUS, map_[0].RADIUS-1):
				vector_list = self.vector_map[vector_row][vector_elm]
				vector_list.append(map_[row  ][elm  ])
				vector_list.append(map_[row  ][elm+1])
				vector_list.append(map_[row+1][elm+1])
				vector_list.append(map_[row+1][elm  ])
				vector_elm += 1
			vector_row += 1

		del map_
		
		chank = self.chank_map[0][0][0]

		chank.generator()
		chank.msg()

		clear()
		print(self.name)
		print('\ncreate the boundaries of the world')

		for lay in self.map:

			for row in lay:
				row[-int(len(self.map)/2)  ] = Wall()
				row[ int(len(self.map)/2)-1] = Wall()

			for elm in range(-int(len(self.map[0][0])/2), int(len(self.map[0][0])/2)-1):
				lay[-int(len(self.map)/2)][elm] = Wall()
				lay[ int(len(self.map)/2)-5][elm] = Wall()

		clear()
		print(self.name)
		print('\ncreate the final room')

		# while True:
		# 	end_room_elm = randint(1, self.ELMS)
		# 	end_room_row = randint(1, self.ROWS)
		# 	if  end_room_row in range(self.ROWS//2 - 7, self.ROWS//2 + 7) or \
		# 		end_room_row in range(self.ROWS//2 + 8, self.ELMS//2 - 8) or \
		# 		end_room_elm in range(self.ELMS//2 - 7, self.ELMS//2 + 7) or \
		# 		end_room_elm in range(self.ELMS//2 + 8, self.ELMS//2 - 8) or \
		# 		end_room_elm > self.ELMS - 5 or \
		# 		end_room_row > self.ROWS - 5:
		# 		continue
		# 	else:
		# 		break

		# Room(generation='end room').spawn(lay, end_room_row-int(self.ROWS/2), end_room_elm-int(self.ELMS/2), self.map)

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
								if type(elm) in (Air, Spike)
								else 
								elm.des 

							for elm in row[strt_elm : fin_elm]
						   ])
				 )