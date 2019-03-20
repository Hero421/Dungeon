from Blocks.Surfaces import Ground
from Enemys.metaEnemy import metaEnemy
from links import ses_avatars

class Container(object):
	"""docstring for GoldOre"""
		
	def walk(self, choice, obj):
		'''
		Breaks the block
		'''

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

		obj.map[row][elm] = obj.memo()
