from Blocks.Containers.metaContainer import Container
from random import randint
from termcolor import colored

from Blocks.Trigers.Workbench import Workbench

from Items.Resources.Stone import Stone
from Items.Resources.Raw_stone import RawStone

class StoneBlock(Container):
	'''
	docstring for Stone
	'''

	des = '#'
	type_= 'Block'

	def __init__(self):
		self.recept = {RawStone: 4, 'result': StoneBlock, 'num': 1, 'place': Workbench}

	def give(self, obj):
		obj.add_to_inventory([RawStone() for _ in range(randint(3, 5))])

		if randint(1, 100) in range(30):
			obj.add_to_inventory([Stone() for _ in range(randint(1, 3))])
