from random import randint

from Blocks.module_Stone import Stone
from Blocks.module_Surfaces import Wall, Ground, Chasm
from Blocks.module_Containers import GoldOre

from Blocks.Trigers.module_Spike import Spike
from Blocks.Trigers.module_Simulator import Simulator
from Blocks.Trigers.module_Chest import Chest

from Enemys.module_metaEnemy import Enemy

from module_Rooms import Rooms, Room

class GameNone(object):
	"""docstring for GameNone"""
	
	des = ' '

	def act(self, row, elm):
		
		from module_links import ses_area
		area = ses_area
		map_ = area.map

		random_num = randint(1, 10000)
		
		# if random_num in range(1):
		# 	Rooms().spawn(row, elm, map_)

		if random_num in range(70):
			map_[row][elm] = Wall()

		elif random_num in range(int(area.enemys*100)):
			Enemy().spawn(row, elm, map_)

		elif random_num in range(int(area.chasms*100)):
			random_num = randint(1, 8)
			if random_num == 1:
				self.ch_generation_1(row, elm, map_)
			elif random_num == 2:
				self.ch_generation_2(row, elm, map_)
			elif random_num == 3:
				self.ch_generation_3(row, elm, map_)
			elif random_num == 4:
				self.ch_generation_4(row, elm, map_)
			elif random_num == 5:
				self.ch_generation_5(row, elm, map_)
			elif random_num == 6:
				self.ch_generation_6(row, elm, map_)
			elif random_num == 7:
				self.ch_generation_7(row, elm, map_)
			elif random_num == 8:
				random_num = randint(1, 100)
				if random_num in range(20):
					self.ch_generation_8(row, elm, map_)

		elif random_num in range(int(area.spikes*100)):
			map_[row][elm] = Spike()

		elif random_num in range(int(area.stones*100)):
			random_num = randint(1, 100)
			if random_num in range(10):
				map_[row][elm] = GoldOre()
			else:
				map_[row][elm] = Stone()

		else:
			map_[row][elm] = Ground()

	def ch_generation_1(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row][elm + 1] = Chasm()
		map_[row][elm + 2] = Chasm()

	def ch_generation_2(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row][elm + 1] = Chasm()
		map_[row][elm + 2] = Chasm()
		map_[row + 1][elm + 1] = Chasm()

	def ch_generation_3(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row][elm + 1] = Chasm()
		map_[row][elm + 2] = Chasm()
		map_[row + 1][elm] = Chasm()

	def ch_generation_4(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row + 1][elm + 1] = Chasm()
		map_[row][elm + 2] = Chasm()

	def ch_generation_5(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row][elm + 1] = Chasm()
		map_[row + 1][elm] = Chasm()
		map_[row + 2][elm] = Chasm()

	def ch_generation_6(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row + 1][elm + 1] = Chasm()
		map_[row + 2][elm] = Chasm()

	def ch_generation_7(self, row, elm, map_):
		map_[row][elm] = Chasm()
		map_[row][elm + 1] = Chasm()

	def ch_generation_8(self, row, elm, map_):
		map_[row][elm] = Chest()
		map_[row - 1][elm] = Chasm()
		map_[row][elm - 1] = Chasm()
		map_[row][elm + 1] = Chasm()
		map_[row + 1][elm] = Chasm()