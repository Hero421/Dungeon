from random import randint, choice

from module_links import ses_avatars, items, types_of_items

class Container(object):
	"""docstring for GoldOre"""
	
	des = ':'

	def __init__(self):

		super().__init__()
		
	def walk(self, choice, obj):
		'''
		Breaks the block
		'''

		if obj in ses_avatars:
			self = Ground()
			self.give(obj)

		elif isinstance(obj, metaEnemy):
			obj.res = False

class GoldOre(Container):
	
	des = '*'
	
	def give(self, obj):
		random_num = randint(1, 15)
		obj.gold += random_num
		input('You got', random_num, 'gold')

class Pot(Container):
	
	des = '+'
	
	def give(self, obj):

		for count in range(3):
			obj.gold += randint(10, 50)
			obj.add_to_inventory([choice(items['common'][choice([types_of_items])] for count in range(randint(1, 5)))])