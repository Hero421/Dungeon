class Item(object):
	'''
	Main class for all subjects. 
	Adds items to the items dictionary 
	using rarity and item type.
	'''
	def __init__(self, link):

		from links import items
		
		if not link in items[self.rarity][self.type_]:
			items[self.rarity][self.type_].append(link)