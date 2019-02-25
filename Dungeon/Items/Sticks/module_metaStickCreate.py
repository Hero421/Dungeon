from Items.module_metaItem import metaItem
import module_links

class metaStickCreate(metaItem):
	"""docstring for StickCreateStone"""

	type = 'Stick'
	use  = False

	def __init__(self, name, desc, rarity, object_, nam):
		self.name = name
		self.desc = desc
		self.rarity = rarity
		self.object = object_
		super().__init__(nam)
	
	def using(self, obj):

		if self.use == False:
			self.use = True
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			if obj.type == 'Avatar':
				module_linksused_items.append(self)
			obj.inventory[1].remove(self)
			obj.selected = self

	def hit(self, row, elm):
		module_links.ses_area.map[row][elm] = self.object()
		
	def stop_using(self, obj):

		if obj.type == 'Avatar':
			obj.add_to_inventory([self])
			module_links.used_items.remove(self)
		obj.selected = None