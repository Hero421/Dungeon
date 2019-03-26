from Items.Resources.metaResource import Resource

class BrokenBoard(Resource):

	name = 'Broken board'

	def __init__(self):
		super().__init__('Broken board', 'Apparently, it was a box', 'common', BrokenBoard)

BrokenBoard()