from random import randint
from Blocks.module_Surfaces import Ground

from Enemys.module_metaEnemy import metaEnemy

class Spike(object):
	
	des = Ground.des
	
	bool = True
	
	dmg = None
	degree = None
	
	def __init__(self):
		
		self.dmg = randint(1, 3)
		self.degree = randint(1, 15)

		super().__init__()

	def walk(self, choice, obj):

		from module_links import ses_area, ses_avatars
		map = ses_area.map
		if isinstance(obj, metaEnemy):
			obj.res = False

		else:
			if obj in ses_avatars:
				location = avatar.location
				if obj.inventory[0]['wings']:
					map[obj.location['row']][obj.location['elm']] = obj.memo()
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
					if self.bool == True:
						if self.des == ' ':
							self.des = colored('^', 'red')
						
						obj.get_hit(self.dmg)
						
						if randint(1, 100) in range(20):
							potioning(obj, self.dmg, self.degree, 'spike hlt down')
	
	def act(self, obj):
		'''
		Breaks the block
		'''

		from module_links import ses_avatars

		if obj in ses_avatars:
			self = Ground()

		elif isinstance(obj, metaEnemy):
			obj.res = False