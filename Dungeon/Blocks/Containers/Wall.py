from Blocks.Containers.metaContainer import Container

class Wall(Container):
	
	'''
	An impregnable barrier to the object.
	'''
	
	des = 'X'

	def give(self, obj):
		obj.add_to_inventory(Wall())