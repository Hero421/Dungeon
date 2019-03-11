from random import randint
from termcolor import colored
from Blocks.module_Surfaces import Ground
from Methods.module_effect_overlay import effect_overlay

from Enemys.module_metaEnemy import metaEnemy

class Spike(object):
	
	des = Ground.des

	def walk(self, choice, obj):

		dmg = randint(1, 3)
		degree = randint(1, 15)

		from module_links import ses_avatars

		if isinstance(obj, metaEnemy):
			obj.res = False

		elif obj in ses_avatars.values():
			location = obj.location
			if obj.inventory[0]['wings']:
				obj.map[obj.location['row']][obj.location['elm']] = obj.memo()
				obj.memo = Spike
				if choice == 'up':
					obj.location['row'] -= 1
				elif choice == 'right':
					obj.location['elm'] += 1
				elif choice == 'down':
					obj.location['row'] += 1
				elif choice == 'left':
					obj.location['elm'] -= 1

			else:
				if self.des == ' ':
					self.des = colored('^', 'red')
				
				obj.get_hit(dmg)
				
				if randint(1, 100) in range(20):
					effect_overlay(obj, dmg, degree, 'spike hlt down')

	def act(self, obj,row, elm):
		'''
		Breaks the block
		'''

		from module_links import ses_avatars

		if obj in ses_avatars.values():
			obj.map[row][elm] = Ground()

		elif isinstance(obj, metaEnemy):
			obj.res = False
