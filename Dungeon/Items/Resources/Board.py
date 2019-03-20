from Items.Resources.metaResource import Resource
from Items.Resources.Broken_Board import BrokenBoard

from Blocks.Trigers.Workbench import Workbench

class Board(Resource):

	name = 'Board'

	def __init__(self):

		self.recept = {BrokenBoard: 5, 'result': Board, 'place': Workbench}
		super().__init__('Board', 'Something', 'common', Board)

Board()