from Items.Resources.metaResource import Resource

class RawStone(Resource):

	def __init__(self):
		super().__init__('Raw stone', 'Something', 'common', RawStone)

RawStone()