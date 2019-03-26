from random import randint
from time import sleep

from Blocks.Air import Air

class Enemy(object):

	des = ' '

	def __init__(self, types=False):

		self.types = types

	def spawn(self, row, elm, map_):
		
		from Enemys.Goblin import Goblin
		from Enemys.Cravler import Cravler

		if self.types:

			if len(self.types) > 1:

				sorted(types, key=lambda x: x[::-1])

				chance = randint(1, 100)

				for pair in self.types:
					if pair[1] in range(chance):
						self = pair[0]()

			elif len(self.types) == 1:
				self = types()

		elif not self.types:
			
			chance = randint(1, 100)

			if chance in range(50):
				self = Goblin(row, elm, map_)
			else:
				self = Cravler(row, elm, map_)

class metaEnemy(object):

	dir_ = 'up'
	memo = Air
	chance= {}
	count = 0

	dirs = ['up', 'up-right', 'right', 'down-right', 'down', 'down-left', 'left', 'up-left']

	all_acts = ['turn', 'move', 'foto', 'eat', 'aff', 'hit', 'mul', 'inv', 'check']

	left = {'up': 'up-left', 'up-left': 'left', 'left': 'down-left', 'down-left': 'down', 'down': 'down-right', 'down-right': 'right', 'right': 'up-right', 'up-right': 'up'}

	def __init__( self, 
				  row, 
				  elm, 
				  hlt=0, 
				  dmg=0, 
				  radius=0, 
				  dodge_Atk=0,
				  dodge_MAtk=0, 
				  chance_hit=0, 
				  exp=0):

		self.right = {self.left[key]: key for key in self.left}

		self.hlt = hlt
		self.dmg = dmg
		self.exp = exp
		self.row = row
		self.elm = elm
		self.radius = radius

		self.dodge_Atk  = dodge_Atk
		self.dodge_MAtk = dodge_MAtk
		self.chance_hit = chance_hit

		self.chance['dodge Atk']  = 100 - self.dodge_Atk
		self.chance['dodge MAtk'] = 100 - self.dodge_MAtk
		self.chance['hit']        = 100 - self.chance_hit

		super().__init__()
		import links
		links.enemys.append(self)

	def check(self):

		if isinstance(self.map[self.row][self.elm], Surface):
			self.map[self.row][self.elm] = self

	def uncond_move(self):

		act = self.list.act(self.count)

		self.count += 4

	def cond_move(self):

		from links import ses_avatars
		from Methods.random_moving import random_moving
		from Methods.distributor import distributor

		for avatar in ses_avatars.values():
			location = avatar.location

			if self.row == location['row']:

				if location['elm'] < self.elm and self.dir_ in ['left', 'up-left', 'down-left']:
					if self.elm - location['elm'] == 1:
						self.give_hit('left')
					else:
						distributor(self, 'left', 'mov')

				elif self.elm < location['elm'] and self.dir_ in ['right', 'up-right', 'down-right']:
					if location['elm'] - self.elm == 1:
						self.give_hit('right')
					else:
						distributor(self, 'right', 'mov')

			elif self.elm == location['elm']:

				if location['row'] < self.row and self.dir_ in ['up-left', 'up', 'up-right']:
					if self.row - location['row'] == 1:
						self.give_hit('up')
					else:
						distributor(self, 'up', 'mov')

				elif self.row < location['row'] and self.dir_ in ['down-left', 'down', 'down-right']:
					if location['row'] - self.row == 1:
						self.give_hit('down')
					else:
						distributor(self, 'down', 'mov')


			elif location['row'] in range(self.row - self.radius, self.row):
				if location['elm'] in range(self.elm - self.radius, self.elm) and self.dir_ in ['up', 'up-left', 'left']:
					random_moving(self, 'up', 'left')

				elif location['elm'] in range(self.elm, self.elm + self.radius) and self.dir_ in ['up', 'up-right', 'right']:
					random_moving(self, 'up', 'right')

			elif location['row'] in range(self.row, self.row + self.radius):
				if location['elm'] in range(self.elm - self.radius, self.elm) and self.dir_ in ['down', 'down-left', 'left']:
					random_moving(self, 'down', 'left')

				elif location['elm'] in range(self.elm, self.elm + self.radius) and self.dir_ in ['down', 'down-right', 'right']:
					random_moving(self, 'down', 'right')

			else:
				random_moving(self, 'all')

		self.count += 1

	def give_hit(self, choice):

		if randint(1, 100) in range(self.chance['hit']):
			if choice == 'up':
				self.map[self.row - 1][self.elm].get_hit(self.dmg)

			elif choice == 'right':
				self.map[self.row][self.elm + 1].get_hit(self.dmg)

			elif choice == 'down':
				self.map[self.row + 1][self.elm].get_hit(self.dmg)

			elif choice == 'left':
				self.map[self.row][self.elm - 1].get_hit(self.dmg)

		else:
			print(self.hlt)
			print('miss')
			sleep(0.3)

		self.count += 1

	def get_hit(self, dmg, obj):
		input(self.chance['dodge Atk'])
		if randint(1, 100) in range(self.chance['dodge Atk']):
			self.hlt -= dmg
			input(self.hlt)
			if self.hlt <= 0:
				if type(obj.selected.ablity) == 'recovery':
					obj.hlt += 5
				obj.Exp += self.exp
				self.map[self.row][self.elm] = self.memo()
				enemys.remove(self)

	def act(self):

		if self.count + 1 > len(self.list):
			self.count -= len(self.list)

		cage_bef_dict = {

			'up'   : self.map[self.row - 1][self.elm],
			'right': self.map[self.row][self.elm + 1],
			'down' : self.map[self.row + 1][self.elm],
			'left' : self.map[self.row][self.elm - 1],

			'up-left'   : self.map[self.row - 1][self.elm - 1],
			'up-right'  : self.map[self.row - 1][self.elm + 1],
			'down-right': self.map[self.row + 1][self.elm + 1],
			'down-left' : self.map[self.row + 1][self.elm - 1]

			}

		self.cage_bef = cage_bef_dict[self.dir_]

		return {

			'eat' : lambda: self.eat(),
			'turn': lambda: self.turn(),
			'foto': lambda: self.foto(),
			'aff' : lambda: self.affect(),
			'inv' : lambda: self.use_inv(),
			'hit' : lambda: self.give_hit(),
			'mul' : lambda: self.multiply(),
			'move': lambda: self.cond_move()

		}.get(self.list[self.count], lambda: None)()