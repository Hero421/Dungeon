from Items.Wings.module_metaWings import metaWings

class Wings(metaWings):

	name = 'Wings'
	rarity = 'common'

	def __init__(self):
		super().__init__(Wings)

Wings()