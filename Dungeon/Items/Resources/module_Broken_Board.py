from Items.Resources.module_metaResource import metaResource

class BrokenBoard(metaResource):

	def __init__(self):

		super().__init__('Broken board', 'Apparently, it was a box', 'common', BrokenBoard)

BrokenBoard()