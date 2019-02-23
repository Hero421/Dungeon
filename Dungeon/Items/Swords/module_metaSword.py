from Items.module_metaItem import metaItem

import module_links

class metaSword(metaItem):
	'''
	The main class for all swords. 
	Adds the swords to the dictionary items, 
	using the ancestor Item.
	'''
	
	type = 'Sword'
	use  = False
	
	def __init__(self, name, desc, dmg, rarity, crit, ability, nam):
		self.dmg = dmg
		self.name = name
		self.rarity = rarity
		self.desc = desc
		self.crit = crit
		self.ability = ability
		super().__init__(nam)
		
	def using(self, obj):
		'''
		If the sword does not stipulate the use, 
		he uses it.
		'''
		if self.use == False:
			self.use = True
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			if obj.type == 'Avatar':
				module_links.used_items.append(self)
			obj.inventory[1].remove(self)
			obj.selected = self
			obj.crit += self.crit
			obj.mid_dmg += self.dmg
	
	def stop_using(self, obj):
		'''
		If the sword does not envisage 
		the cessation of the use, 
		he uses it.
		'''
		obj.mid_dmg -= self.dmg
		obj.crit -= self.crit
		if obj.type == 'Avatar':
			obj.add_to_inventory([self])
			module_links.used_items.remove(self)
		obj.selected = None
