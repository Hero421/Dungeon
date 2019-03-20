from Items.Resources.metaResource import Resource

class IronBar(Resource):

	name = 'Iron bar'

	def __init__(self):

		super().__init__('Iron bar', 'Something', 'common', IronBar)

	def remelting(self, oven, obj, index):
		pass

IronBar()