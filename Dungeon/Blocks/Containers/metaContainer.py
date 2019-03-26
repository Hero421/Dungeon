from random import randint

from Blocks.Air import Air
from Blocks.Trigers.Chest import Chest
from links import ses_avatars

class Container(object):
	"""docstring for GoldOre"""
		
	def raze(self, choice, obj):
		'''
		Breaks the block
		'''

		if obj in ses_avatars.values():
			
			self.give(obj)
			
			lay = obj.lay
			row = obj.row
			elm = obj.elm

			if choice == 'North':
				row -= 1
			elif choice == 'East':
				elm += 1
			elif choice == 'South':
				row += 1
			elif choice == 'West':
				elm -= 1
			elif choice == 'up':
				lay += 1
			elif choice == 'down':
				lay -= 1

		from Blocks.Containers.Stone_block import StoneBlock

		obj.map[lay][row][elm] = Chest() if type(self) is StoneBlock and randint(1, 100) in range(2) else Air()
