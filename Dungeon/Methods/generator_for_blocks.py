from random import randint

from Blocks.Containers.Stone_block import StoneBlock
from Blocks.Containers.Wall import Wall
from Blocks.Containers.Ground_block import GroundBlock
from Blocks.Chasm import Chasm
from Blocks.Air import Air
from Blocks.Containers.Gold_ore_block import GoldOreBlock
from Blocks.Containers.Iron_ore_block import IronOreBlock
from Blocks.Containers.Box import Box
from Blocks.Containers.Pot import Pot

from Blocks.Trigers.Spike import Spike
from Blocks.Trigers.Simulator import Simulator
from Blocks.Trigers.Chest import Chest

from Enemys.metaEnemy import Enemy

from Generations.Rooms import Rooms, Room

def generator_for_blocks(lay, row, elm, map_, height=0):

	if lay < height:

		num  = randint(1, 10000)

		if num in range(3 * 100):
			block = GoldOreBlock

		elif num in range(12 * 100):
			block = IronOreBlock

		elif num in range(40 * 100):
			block = StoneBlock

		else:
			block = GroundBlock

		map_[lay][row][elm] = block()

	elif lay == height:

		if randint(1, 100) in range(30):
			block = StoneBlock
		else:
			block = Air

		map_[lay][row][elm] = block()

	elif lay > height:

		map_[lay][row][elm] = Air()

		# random_num = randint(1, 10000)
		
		# if random_num in range(1):
		# 	Rooms().spawn(row, elm, map_)

		# if random_num in range(70):
		# 	map_[lay][row][elm] = Wall()

		# elif lay == 0 and random_num in range(0):
		# 	Enemy().spawn(lay, row, elm, map_)

		# elif random_num in range(int(area.chasms*100)):
		# 	random_num = randint(1, 8)
		# 	if random_num == 1:
		# 		self.ch_generation_1(row, elm, map_)
		# 	elif random_num == 2:
		# 		self.ch_generation_2(row, elm, map_)
		# 	elif random_num == 3:
		# 		self.ch_generation_3(row, elm, map_)
		# 	elif random_num == 4:
		# 		self.ch_generation_4(row, elm, map_)
		# 	elif random_num == 5:
		# 		self.ch_generation_5(row, elm, map_)
		# 	elif random_num == 6:
		# 		self.ch_generation_6(row, elm, map_)
		# 	elif random_num == 7:
		# 		self.ch_generation_7(row, elm, map_)
		# 	elif random_num == 8:
		# 		random_num = randint(1, 100)
		# 		if random_num in range(20):
		# 			self.ch_generation_8(row, elm, map_)

		# elif random_num in range(int(area.spikes*100)):
		# 	map_[row][elm] = Spike()

		# elif random_num in range(int(area.stones*100)):
		# 	random_num = randint(1, 100)
		# 	if random_num in range(4):
		# 		random_num = randint(1, 100)
		# 		if random_num in range(85):
		# 			map_[row][elm] = Box()
		# 		else:
		# 			map_[row][elm] = Pot()
		# 	elif random_num in range(10):
		# 		map_[row][elm] = GoldOreBlock()
		# 	elif random_num in range(15):
		# 		map_[row][elm] = IronOreBlock()
		# 	else:
		# 		map_[row][elm] = StoneBlock()

		# else:
		# 	map_[row][elm] = Ground()

	# def ch_generation_1(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row][elm + 1] = Chasm()
	# 	map_[row][elm + 2] = Chasm()

	# def ch_generation_2(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row][elm + 1] = Chasm()
	# 	map_[row][elm + 2] = Chasm()
	# 	map_[row + 1][elm + 1] = Chasm()

	# def ch_generation_3(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row][elm + 1] = Chasm()
	# 	map_[row][elm + 2] = Chasm()
	# 	map_[row + 1][elm] = Chasm()

	# def ch_generation_4(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row + 1][elm + 1] = Chasm()
	# 	map_[row][elm + 2] = Chasm()

	# def ch_generation_5(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row][elm + 1] = Chasm()
	# 	map_[row + 1][elm] = Chasm()
	# 	map_[row + 2][elm] = Chasm()

	# def ch_generation_6(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row + 1][elm + 1] = Chasm()
	# 	map_[row + 2][elm] = Chasm()

	# def ch_generation_7(self, row, elm, map_):
	# 	map_[row][elm] = Chasm()
	# 	map_[row][elm + 1] = Chasm()

	# def ch_generation_8(self, row, elm, map_):
	# 	map_[row][elm] = Chest()
	# 	map_[row - 1][elm] = Chasm()
	# 	map_[row][elm - 1] = Chasm()
	# 	map_[row][elm + 1] = Chasm()
	# 	map_[row + 1][elm] = Chasm()