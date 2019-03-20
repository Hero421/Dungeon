from random import randint
from termcolor import colored
from Blocks.Surfaces import Ground
from Methods.effect_overlay import effect_overlay

from Enemys.metaEnemy import metaEnemy

class Spike(object):
	
	des = Ground.des

	def walk(self, choice, obj):

		dmg = randint(1, 3)
		degree = randint(1, 15)

		from links import ses_avatars

		if isinstance(obj, metaEnemy):
			obj.res = False

		elif obj in ses_avatars.values():
			location = obj.location
			if obj.inventory['wings']:
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

	def act(self, obj, dir_):
		'''
		Breaks the block
		'''

		from links import ses_avatars

		if obj in ses_avatars.values():

			row = obj.row
			elm = obj.elm

			if dir_ == 'up':
				row -= 1
			elif dir_ == 'right':
				elm += 1
			elif dir_ == 'down':
				row += 1
			elif dir_ == 'left':
				elm -= 1

			obj.map[row][elm] = Ground()

		elif isinstance(obj, metaEnemy):
			obj.res = False
