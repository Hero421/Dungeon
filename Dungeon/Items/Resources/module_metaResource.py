from Items.module_metaItem import metaItem

class metaResource(metaItem):

	type_= 'Resource'

	def __init__(self, name, desc, rarity, link):

		self.name = name
		self.desc = desc
		self.rarity = rarity

		super().__init__(link)