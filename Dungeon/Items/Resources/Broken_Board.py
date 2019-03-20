from Items.Resources.metaResource import Resource

class BrokenBoard(Resource):

	def __init__(self):

		name = 'Broken board'

		super().__init__('Broken board', 'Apparently, it was a box', 'common', BrokenBoard)

BrokenBoard()