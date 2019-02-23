from random import randint

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
		from Blocks.module_metaSurfaces import Ground
		
		if obj in ses_avatars:
			if choice == 'up':
				obj.map[obj.row - 1][obj.elm] = Chest() if randint(1, 100) in range(2) else Ground
			elif choice == 'right':
				obj.map[obj.row][obj.elm + 1] = Chest() if randint(1, 100) in range(2) else Ground
			elif choice == 'down':
				obj.map[obj.row + 1][obj.elm] = Chest() if randint(1, 100) in range(2) else Ground
			elif choice == 'left':
				obj.map[obj.row][obj.elm - 1] = Chest() if randint(1, 100) in range(2) else Ground

		elif isinstance(obj, metaEnemy):
			obj.res = False