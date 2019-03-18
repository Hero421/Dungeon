from Items.module_metaItem import metaItem
from Methods.module_effect_overlay import effect_overlay

class metaDrug(metaItem):
	
	type_= 'Drug'
	
	def __init__(self, name, num, degree, ability, rarity, desc, nam):
		self.name = name
		self.desc = desc 
		self.num  = num
		self.degree = degree
		self.rarity = rarity
		self.ability= ability

		super().__init__(nam)
	
	def using(self, obj):
		effect_overlay(obj, self.degree, self.num, self.ability)
		obj.inventory[1].remove(self)

	def print_details(self):

		print(self.num)

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'health: {self.num}/turn ')
		print(f'degree: {self.degree} turns')
		print(f'rarity: {self.rarity}')
		print(f'desc:   {self.desc}')
