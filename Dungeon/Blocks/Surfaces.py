from Blocks.metaSurface import metaSurface

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

	def walk(self, choice, obj):

		from links import ses_avatars
		from Enemys.metaEnemy import metaEnemy

		if obj in ses_avatars.values():
			if obj.inventory[0]['wings']:
				location = obj.location
				obj.map[location['row']][location['elm']] = obj.memo()
				obj.memo = Chasm
				if choice == 'up':   location['row'] -= 1
				elif choice == 'right': location['elm'] += 1
				elif choice == 'down': location['row'] += 1
				elif choice == 'left': location['elm'] -= 1