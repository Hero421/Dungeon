from Blocks.Containers.metaContainer import Container

from Blocks.Trigers.Workbench import Workbench
from Items.Resources.Board import Board

class FloorBlock(Container):
	'''
	Usually, he is in the room.
	'''
	
	des = '_'

	def __init__(self):
		self.recept = {Board: 4, 'result': FloorBlock, 'num': 1, 'place': Workbench}

	def give(self, obj):
		obj.add_to_inventory(Floor())