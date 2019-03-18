from Items.Resources.module_metaResource import metaResource

class GoldBar(metaResource):

	def __init__(self):

		super().__init__('Gold bar', 'Use to create masterpieces', 'rare', GoldBar)

GoldBar()