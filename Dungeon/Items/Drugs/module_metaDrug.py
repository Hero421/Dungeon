from Items.module_metaItem import metaItem
from Methods.module_effect_overlay import effect_overlay

class metaDrug(metaItem):
	
	type_= 'Drug'
	
	def __init__(self, name, dmg, degree, ability, rarity, desc, nam):
		self.name = name
		self.desc = desc 
		self.dmg  = dmg
		self.degree = degree
		self.rarity = rarity
		self.ability= ability

		super().__init__(nam)
	
	def using(self, obj):
		effect_overlay(obj, self.degree, self.dmg, self.ability)
		obj.backpack.remove(self)

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'health: {self.dmg}/turn ')
		print(f'degree: {self.degree} turns')
		print(f'rarity: {self.rarity}')
		print(f'desc:   {self.desc}')
