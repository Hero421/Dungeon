from Items.Swords.metaSword  import Sword
from Items.Resources.Board   import Board
from Items.Resources.Iron_Ore import IronBar

from Blocks.Trigers.Workbench import Workbench

class Sword_(Sword):

	name = 'Sword'

	def __init__(self):
		self.recept = {Board: 2, IronBar: 4, 'place': Workbench, 'result':Sword_}
		super().__init__('Sword', 'Simply sword, not expected, Yes?', 10, 'common', 5 , None, Sword_)

Sword_()