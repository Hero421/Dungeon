from random import randint

from termcolor import colored

class Stone(object):
	'''
	docstring for Stone
	'''

	des = '#'

	def walk(self, choice, obj):
		'''
		Breaks the block
		'''

		from module_links import ses_avatars
		from Enemys.module_metaEnemy import metaEnemy
		from Blocks.Trigers.module_Chest import Chest
		from Blocks.module_Surfaces import Ground
		
		if obj in ses_avatars.values():
		
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

			obj.map[row][elm] = Chest() if randint(1, 100) in range(2) else Ground()