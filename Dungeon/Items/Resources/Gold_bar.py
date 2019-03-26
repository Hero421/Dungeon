from Items.Resources.metaResource import Resource

class GoldBar(Resource):

	def __init__(self):
		super().__init__('Gold bar', 'Use to create masterpieces', 'rare', GoldBar)

GoldBar()