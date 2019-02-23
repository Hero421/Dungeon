class metaItem(object):
	'''
	Main class for all subjects. 
	Adds items to the items dictionary 
	using rarity and item type.
	'''
	def __init__(self, name):

		from module_links import items
		
		if not(name in items[self.rarity][self.type]):
			items[self.rarity][self.type].append(name)