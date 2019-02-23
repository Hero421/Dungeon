from Items.Swords.module_metaSword import metaSword

from Methods.module_effect_overlay import effect_overlay

import module_links

class FierySword(metaSword):

	name = 'Fiery sword'

	def __init__(self):
		super().__init__('Fiery sword', 'While holding each turn removed 2 HP', 5, 'common', 0, 'Fire', FierySword)

	def using(self, obj):

		if self.use == False:
			self.use = True
			if type(obj) is Avatar:
				module_links.used_items.append(self)
			effect_overlay(obj, 2, 'WTS', 'set fire')
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			obj.inventory[1].remove(self)
			obj.selected = self
			obj.mid_dmg += self.dmg
			obj.crit += self.crit
	
	def stop_using(self, obj):
		self.use = False
		del module_links.intoxicated[obj]
		obj.mid_dmg -= self.dmg
		obj.crit -= self.crit
		if type(obj) is Avatar:
			module_links.used_items.remove(self)
		obj.add_to_inventory(self)
		obj.selected = None

FierySword()