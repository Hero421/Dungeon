from Items.module_metaItem import metaItem

class metaWings(metaItem):
	"""docstring for Wings"""
	type_= 'Wings'
	def __init__(self, nam):
		super().__init__(nam)

	def using(self, obj):
		if obj.inventory[0]['wings'] and not obj.inventory[0]['wings'] == self:
			obj.add_to_inventory(obj.inventory[0]['wings'])
		obj.inventory[0]['wings'] = self