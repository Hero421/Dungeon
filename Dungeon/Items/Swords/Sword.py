from Items.Swords.metaSword  import Sword
from Items.Resources.Board   import Board
from Items.Resources.Iron_bar import IronBar

from Blocks.Trigers.Workbench import Workbench

class Sword_(Sword):

	name = 'Sword'

	def __init__(self):
		self.recept = {Board: 2, IronBar: 4, 'result':Sword_, 'num': 1, 'place': Workbench}
		super().__init__('Sword', 'Simply sword, not expected, Yes?', 10, 'common', 5 , None, Sword_)

Sword_()