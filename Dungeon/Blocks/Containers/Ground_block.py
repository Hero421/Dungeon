from random import randint

from Blocks.Containers.metaContainer import Container

class GroundBlock(Container):
	'''
	On the ground you can walk,
	of course, if it's not spike.
	'''
	
	des = '.'
	type_ = 'Block'

	def give(self, obj):
		obj.add_to_inventory([GroundBlock()])
