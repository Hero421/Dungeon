from Items.metaItem import Item

import links

class Sword(Item):
	'''
	The main class for all swords. 
	Adds the swords to the dictionary items, 
	using the ancestor Item.
	'''
	
	type_= 'Sword'
	use  = False
	
	def __init__(self, name, desc, dmg, rarity, crit, ability, link):
		self.dmg = dmg
		self.name = name
		self.rarity = rarity
		self.desc = desc
		self.crit = crit
		self.ability = ability
		super().__init__(link)
		
	def using(self, obj):
		'''
		If the sword does not stipulate the use, 
		he uses it.
		'''

		from links import ses_avatars

		if not self.use:
			self.use = True
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			if obj in ses_avatars:
				links.used_items.append(self)
			obj.backpack.remove(self)
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
		obj.add_to_inventory(self)
		obj.selected = None
		self.use = False

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'damage: {self.dmg}')
		print(f'rarity: {self.rarity}')
		print(f'desc:   {self.desc}')