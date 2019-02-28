from Blocks.module_metaSurface import metaSurface

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
		from Enemys.module_metaEnemy import metaEnemy

		if isinstanse(obj, metaEnemy):
			obj.res = False

		else:
			for avatar in ses_avatars.values():
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