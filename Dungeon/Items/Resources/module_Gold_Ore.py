from Items.Resources.module_metaResource import metaResource

class GoldOre(metaResource):

	def __init__(self):
		super().__init__('Gold ore', 'You can melt a gold bar', 'common', GoldOre)
	
	def remelting(self, oven, obj, index):

		obj.inventory[1][index].remove(self)

		for slot in oven.slots:
			if type(slot[0]) is GoldOre or not slot:
				slot.append(self)
				break

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'desc:   {self.desc}')
		print(f'rarity: {self.rarity}')

	def using(self, obj):
		pass
