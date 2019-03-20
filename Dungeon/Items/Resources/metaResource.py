from Items.metaItem import Item

class Resource(Item):

	type_= 'Resource'

	def __init__(self, name, desc, rarity, link):

		self.name = name
		self.desc = desc
		self.rarity = rarity

		super().__init__(link)

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'desc:   {self.desc}')
		print(f'rarity: {self.rarity}')

	def using(self, obj):
		pass