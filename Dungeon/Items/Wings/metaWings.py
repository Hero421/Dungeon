from Items.metaItem import Item

class Wings(Item):
	"""docstring for Wings"""
	type_= 'Wings'
	def __init__(self, nam):
		super().__init__(nam)

	def using(self, obj):
		if obj.inventory['wings'] and not obj.inventory['wings'] == self:
			obj.add_to_inventory(obj.inventory['wings'])
		obj.inventory['wings'] = self

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'rarity: {self.rarity}')
