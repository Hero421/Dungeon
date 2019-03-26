from Items.Resources.metaResource import Resource
from Items.Resources.Broken_board import BrokenBoard

from Blocks.Trigers.Workbench import Workbench

class Board(Resource):

	name = 'Board'

	def __init__(self):

		self.recept = {BrokenBoard: 2, 'result': Board, 'num': 1, 'place': Workbench}
		super().__init__('Board', 'Something', 'common', Board)

Board()