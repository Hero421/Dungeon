from Items.module_metaItem import metaItem

class metaStickCreate(metaItem):
	"""docstring for StickCreateStone"""

	type_= 'Stick'
	use  = False

	def __init__(self, name, desc, rarity, object_, nam):
		self.name = name
		self.desc = desc
		self.rarity = rarity
		self.object = object_
		super().__init__(nam)
	
	def using(self, obj):

		if not self.use:
			self.use = True
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			obj.backpack.remove(self)
			obj.selected = self

	def hit(self, row, elm, map_):
		map_[row][elm] = self.object()
		
	def stop_using(self, obj):

		obj.add_to_inventory(self)
		obj.selected = None
		self.use = False

	def print_details(self):

		print(f'name:   {self.name}')
		print(f'type:   {self.type_}')
		print(f'rarity: {self.rarity}')
		print(f'desc:   {self.desc}')