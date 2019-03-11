from Blocks.module_Surfaces import Ground
from Enemys.module_metaEnemy import metaEnemy
from module_links import ses_avatars

class Container(object):
	"""docstring for GoldOre"""

	def __init__(self):

		super().__init__()
		
	def walk(self, choice, obj):
		'''
		Breaks the block
		'''

		if obj in ses_avatars.values():


			if obj in ses_avatars.values():
				
				self.give(obj)
				
				row = obj.row
				elm = obj.elm

				if choice == 'up':
					row -= 1
				elif choice == 'right':
					elm += 1
				elif choice == 'down':
					row += 1
				elif choice == 'left':
					elm -= 1

			obj.map[row][elm] =  Ground()

		elif isinstance(obj, metaEnemy):
			obj.res = False
