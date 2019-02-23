from Blocks.Trigers.module_Door import Door

class metaSurface(object):

	def walk(self, choice, obj):
		'''
		Helps the subject walk on it.
		'''

		from module_links import ses_avatars, ses_area
		map = ses_area.map

		from Enemys.module_metaEnemy import metaEnemy

		if obj in ses_avatars:
			location = obj.location
			map[location['row']][location['elm']] = obj.memo()
			obj.memo = type(self)
			if choice == 'up':
				location['row'] -= 1
			elif choice == 'right':
				location['elm'] += 1
			elif choice == 'down':
				location['row'] += 1
			elif choice == 'left':
				location['elm'] -= 1

		elif isinstance(obj, metaEnemy):
			if type(obj.memo) is Door:
				map[obj.row][obj.elm] = obj.memo(stat=True)
			else:
				map[obj.row][obj.elm] = obj.memo()
			obj.memo = type(self)
			if choice == 'up':
				obj.row -= 1
			elif choice == 'right':
				obj.elm += 1
			elif choice == 'down':
				obj.row += 1
			elif choice == 'left':
				obj.elm -= 1
			obj.res = True

class Ground(metaSurface):
	'''
	On the ground you can walk,
	of course, if it's not spike.
	'''
	
	des = ' '

class Floor(metaSurface):
	'''
	Usually, he is in the room.
	'''
	
	des = '_'

class Wall(object):
	'''
	An impregnable barrier to the object.
	'''
	
	des = 'X'
	stat = 5

	def act(self, obj):
		self.stat -= obj.power
		print(self.stat)
		print(obj.powe)
		input()
		if self.stat <= 0:
			self = Ground()

class Potion(metaSurface):
	
	'''
	Potion to object
	'''
	
	des = '°'

class Chasm(object):
	'''
	If an object has wings, it can fly over it.
	'''
	
	des = '~'

	def __init__(self):
		super().__init__()

	def walk(self, choice, obj):

		from module_links import ses_avatars

		if type(obj) is Enemy or type(obj) is Goblin:
			obj.res = False

		else:
			for avatar in ses_avatars:
				if obj == avatar:
					if obj.inventory[0]['wings']:
						location = avatar.location
						obj.map[location['row']][location['elm']] = obj.memo()
						obj.memo = Chasm
						if choice == obj.map[obj.row - 1][obj.elm]:
							location['row'] -= 1
						elif choice == obj.map[obj.row][obj.elm + 1]:
							location['elm'] += 1
						elif choice == obj.map[obj.row + 1][obj.elm]:
							location['row'] += 1
						elif choice == obj.map[obj.row][obj.elm - 1]:
							location['elm'] -= 1