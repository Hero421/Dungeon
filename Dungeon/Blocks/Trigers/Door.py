class Door(object):
	"""open-close-open-close"""

	def __init__(self, stat=False):
		self.stat = stat
		if self.stat == False:
			self.des = '<'
		else:
			self.des = '>'

	def act(self, obj):
		if self.stat == False:
			self.stat = True
			self.des  = '>'
		else:
			self.stat = False
			self.des  = '<'
			
	def walk(self, choice, obj):
		'''
		Helps the subject walk on it.
		'''
		
		from links import ses_avatars

		if self.stat == True:
			map = ses_area.map

			from Enemys.metaEnemy import metaEnemy

			if obj in ses_avatars.values():
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
