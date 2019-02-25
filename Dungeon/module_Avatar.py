from random import randint

from module_Rooms import Room
import module_links

from Blocks.module_metaSurfaces import Floor


class Avatar(object):

	empt_slot = 0
	status    = []
	count     = {}    # {'self.name': [start, stop, stat(on/off), self]}
	chance    = {}	# {'potion': []}
	location  = {'row': None, 'elm': None}
	choices   = None
	selected  = None
	chank     = None

	bool_ = False

	gold = 0

	des  = '0'

	full_hlt = 100
	full_mana = 0

	mid_dmg   = 20
	mid_m_dmg = 1

	dodge_Atk = 5
	dodge_MAtk= 1

	hit   = 20
	armor = 15
	
	power = 1

	backpack = 20

	Atk  = 1
	MAtk = 1
	Agi  = 1
	Vit  = 1
	Int  = 1
	Dcs  = 1
	Luc  = 1

	Lvl  = 1

	Exp = 0
	End_exp = 100

	Skill_points = 0

	crit = 0

	id = 'host'

	def __init__(self, id, room='yes'):

		self.hlt  = self.full_hlt
		self.mana = self.full_mana
		self.dmg  = randint(self.mid_dmg - 1, self.mid_dmg + 1)
		self.m_dmg= randint(self.mid_m_dmg - 1, self.mid_m_dmg + 1)
		
		self.id = id

		self.area = module_links.ses_area
		self.map  = self.area.map
		# if len(list(ses_avatars)) == 0:
		# 	self.id == 'host'
		# else:
		# 	self.id = os.getpid()
		module_links.ses_avatars[id] = self

		self.chank = self.area.fst_chank
		self.chank.generator(self)

		self.chance['dodge Atk']  = 100 - self.dodge_Atk
		self.chance['dodge MAtk'] = 100 - self.dodge_MAtk
		self.chance['hit']        = 100 - self.hit

		self.count['Source']    = [40, 0, 'on', None]

		super().__init__()

		self.memo = Floor

		self._fst_row = int(float(self.area.rows)/2)
		self._fst_elm = int(float(self.area.elms)/2)

		if room == 'yes':
			Room(self._fst_row - 1, self._fst_elm - 1, self.area, 'the initial room').spawn()
		#	avatar_rooms = Rooms(self._fst_row - 1, self._fst_elm - 1, ['the initial room', 'room with the chest'])


		self.row, self.location['row'] = self._fst_row, self._fst_row
		self.elm, self.location['elm'] = self._fst_elm, self._fst_row

		self.map[self.location['row']][self.location['elm']] = self

		self.inventory = [
			{
				'head' : None, 
				'torso': None, 
				'wings': None, 
				'feet' : None, 
				'shoes': None, 
				'rings': []
			}, 

			[None for count in range(1, self.backpack + 1)]
		]

	def check(self):
		'''
		Checks to see if all is in order with personagem
		'''

		self.map[self.location['row']][self.location['elm']] = self
		self.row = self.location['row']
		self.elm = self.location['elm']

		self.chank = self.area.chank_map[int(self.location['row']/50)][int(self.location['elm']/50)]

		self.chank.msg(self)

		self.level()

		self.crity()

		self.emp_slot()

		self.select()

		self.using_items()

		self.game()

	def level(self):
		if self.Exp >= self.End_exp:
			self.Skill_points += 3
			self.skill_up()
			if self.Exp > self.End_exp:
				Exp = self.Exp - self.End_exp
			else:
				Exp = 0
			self.Exp = 0
			self.End_exp = self.End_exp*2 + Exp
			Exp = 0

	def crity(self):
		if self.selected:
			if randint(1, 100) in range(self.crit):
				self.dmg = 2*randint(self.mid_dmg - 1, self.mid_dmg + 1)
			else:
				self.dmg =   randint(self.mid_dmg - 1, self.mid_dmg + 1)
		else:
			self.dmg = randint(self.mid_dmg - 1, self.mid_dmg + 1)

	def emp_slot(self):
		for slot in self.inventory[1]:
			if slot is None:
				self.empt_slot = self.inventory[1].index(slot)
				break
			else:
				self.empt_slot = None

	def select(self):
		if self.selected != None:
			if not(self.selected in used_items):
				self.selected.using(self)

	def using_items(self):
		for item in module_links.used_items:
			item.using(self)

	def game(self):
		if self.hlt <= 0:
			module_links.hp -= 1
			module_links.game = 'Game over'
			self.reset()

	def reset(self):
		'''
		Restart the level and Avatar
		'''
		if self.selected != None:
			self.selected.use = False
		self.map[self.location['row']][self.location['elm']] = DieChest()
		self.location['row'], self.location['elm'] = self._fst_row, self._fst_elm
		self.map[self._fst_row + 1][self._fst_elm] = Floor()
		for slot in self.inventory[1]:
			slot = None
		self.hlt = self.full_hlt
		self.armor = self.full_armor
		self.mana = self.full_mana
		self.memo = Floor
		global intoxicated
		if self in intoxicated:
			del intoxicated[self]

	def move(self, dir):
		moving(self, dir)
		pass

	def open_inventory(self, chest=0):
		'''
		Shows the contents of the inventory, 
		allows the player to view the data on the desired item, 
		as well as to use this item
		'''
		if self.selected:
			print(self.selected.name)

		for key in self.inventory[0].keys():
			if key != 'rings':
				if self.inventory[0][key] != None:
					if key == 'head' or key == 'feet':
						print(key + ':  ' + self.inventory[0][key].name)
					else:
						print(key + ': '  + self.inventory[0][key].name)
				else:
					if key == 'head' or key == 'feet':
						print(key + ':  ' + 'None')
					else:
						print(key + ': '  + 'None' )
			else:
				if self.inventory[0][key] != None:
					print(key + ': ' + ' '.join(ring.name + ', ' if not(type(ring) is None) else 'None' for ring in self.inventory[0]['rings']))
				else:
					print(key + ': ' + 'None')

		print()
		count = 1
		for item in self.inventory[1]:
			if item is None:
				if len(str(count)) == 1:
					print(str(count) +'.  None')
				else:
					print(str(count) + '. None')
			elif type(item) is list:
				if len(str(count)) == 1:
					print(str(count) + '. ', item[0].name, 'x' + str(len(item)))
				else:
					print(str(count) + '.' , item[0].name, 'x' + str(len(item)))
			else:
				if len(str(count)) == 1:
					print(str(count) + '.  '+ item.name)
				else:
					print(str(count) + '. ' + item.name)
			count += 1

		choice = input()

		if choice == 'selected':
			print()
			print(self.selected.name)
			print(self.selected.type)
			if type(self.selected) is Sword:
				print(self.selected.dmg)
			print(self.selected.rarity)
			print(self.selected.desc)

		self.corrected_choices = [str(slot_num) for slot_num in range(self.backpack)]
		if choice in self.corrected_choices:
			choice = int(choice) - 1
			if self.inventory[1][choice]:
				print()
				print(self.inventory[1][choice].name)
				print(self.inventory[1][choice].type)
				print(self.inventory[1][choice].rarity)
				print(self.inventory[1][choice].desc)
			else:
				print('None')

			second_choice = input()

			if second_choice == 'use':
				if self.inventory[1][choice]:
					self.inventory[1][choice].using(self)
				else:
					if self.selected:
						self.selected.stop_using(self)
					
			elif second_choice == 'transfer':
				third_choice = int(input()) - 1
				self.inventory[1][choice], self.inventory[1][third_choice] = self.inventory[1][third_choice], self.inventory[1][choice]

	def add_to_inventory(self, items):
		for item in items:
			if type(item) is list:
				if self.empt_slot != None:
					self.inventory[1][self.empt_slot] = item
					self.emp_slot()
			elif item.type == 'Helmet' and self.inventory[0]['head'] == None:
				self.inventory[0]['head'] = item
			elif item.type == 'Cuirass' and self.inventory[0]['body'] == None:
				self.inventory[0]['body'] = item
			elif item.type == 'Wings' and self.inventory[0]['wings'] == None:
				self.inventory[0]['wings'] = item
			elif item.type == 'Leggings' and self.inventory[0]['feet'] == None:
				self.inventory[0]['feet'] = item
			elif item.type == 'Shoes' and self.inventory[0]['shoes'] == None:
				self.inventory[0]['shoes'] = item
			elif self.empt_slot != None:
				self.inventory[1][self.empt_slot] = item
				self.emp_slot()
			else:
				print('inventory is full')
				break

	def stat(self):
		if self in module_links.intoxicated:
			print(*list(set(self.status)))
		print('health: ' + str(self.hlt))
		print('armor:  ' + str(self.armor))
		print('mana:   ' + str(self.mana))
		print('gold:   ' + str(self.gold))
		print()
		print(str(self.Exp) + '/' + str(self.End_exp))
		print()


	def get_hit(self, dmg):
		random_num = randint(1, 100)
		if random_num in range(self.chance['dodge Atk']):
			if self.armor < dmg:
				self.hlt -= dmg - self.armor
				print(dmg - self.armor)
				input()
			else:
				print('miss')
				input()
		else:
			print('miss')
			input()

	def give_hit(self, obj):
		random_num = randint(1, 100)
		if random_num in range(self.chance['hit']):
			obj.get_hit(self.dmg)
		else:
			print('miss')
			input()


	def del_of_inventory(self, item):
		self.inventory.remove(item)
		pass

	def recovery(self):
		if self.mana < self.full_mana:
			self.mana += 1
		for para in list(self.count):
			if self.count[para][3]:
				if self.count[para][2] == 'on':
					if self.count[para][0] < self.count[para][1]:
						self.count[para][0] += 1
					elif self.count[para][0] > self.count[para][1]:
						self.count[para][0] -= 1
					elif self.count[para][0] == self.count[para][1]:
						if self.count[para][3].ablity == 'break':
							self.selected = None
							self.inventory[1][self.selected[1] - 1] = None

	def skill_tree(self):

		print()
		print('Atk: ', self.Atk)
		print('MAtk:', self.MAtk)
		print('Agi: ', self.Agi)
		print('Vit: ', self.Vit)
		print('Int: ', self.Int)
		print('Dcs: ', self.Dcs)
		print('Luc: ', self.Luc)

	def skill_up(self):
		
		esc = False
		
		while self.Skill_points > 0 and esc == False:
			print('Skill points:', self.Skill_points)

			self.skill_tree()

			choice = input()
			if choice == 'Atk':
				self.Atk += 1
				if self.Atk % 5 == 0:
					self.mid_dmg += 100
			elif choice == 'MAtk':
				self.MAtk += 1
				self.mid_m_dmg += 100
			elif choice == 'Agi':
				self.Agi += 1
			elif choice == 'Vit':
				self.Vit += 1

				self.hlt += 100
			elif choice == 'Int':
				self.Int += 1
			elif choice == 'Dcs':
				self.Dcs += 1
			elif choice == 'Luc':
				self.Luc += 1
			
			elif choice == 'esc':
				esc = True
			
			if choice != 'esc' and choice != '':
				self.Skill_points -= 1
			
			clear()
		
		self.skill_tree()
		input()
		clear()
