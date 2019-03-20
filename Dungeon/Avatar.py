from random import randint
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key

from Methods.smart_input import smart_input

from Rooms import Room, Rooms, Corridor
import links
from links import intoxicated, clear

from Blocks.Surfaces import Floor
from Blocks.Trigers.DieChest import DieChest

from Items.Swords.metaSword import Sword
from Items.Sticks.metaStickCreate import StickCreate

class Avatar(object):

	empt_slot = 0
	status    = []
	used_items= []
	count     = {}  # {'self.name': [start, stop, stat(on/off), self]}
	chance    = {}	# {'ivent': chance}
	location  = {'row': None, 'elm': None}
	choices   = None
	selected  = None

	gold = 0

	des  = '0'

	full_hlt  = 10
	full_mana = 0

	mid_dmg   = 2
	mid_m_dmg = 1

	dodge_Atk = 5
	dodge_MAtk= 1

	hit   = 1
	armor = 0
	
	power = 1

	backpack_slots = 20

	Atk  = 1
	MAtk = 1
	Agi  = 1
	Vit  = 1
	Int  = 1
	Dcs  = 1
	Luc  = 1

	Lvl  = 1

	Exp = 0
	End_exp = 20

	Skill_points = 0

	crit = 0

	memo = Floor

	def __init__(self, id_, room=True):

		self.hlt  = self.full_hlt
		self.mana = self.full_mana
		self.dmg  = randint(self.mid_dmg   - 1, self.mid_dmg   + 1)
		self.m_dmg= randint(self.mid_m_dmg - 1, self.mid_m_dmg + 1)
		
		self.id_ = id_

		self.area = links.ses_area
		self.map  = self.area.map

		links.ses_avatars[id_] = self

		self.chance['dodge Atk']  = 100 - self.dodge_Atk
		self.chance['dodge MAtk'] = 100 - self.dodge_MAtk
		self.chance['hit']        = 100 - self.hit

		self.count['Source'] = [40, 0, 'on', None]

		self.location['row'] = 0
		self.location['elm'] = 0

		if room:
			Rooms(

				['the initial room', 'room with the chest'], 
				doors='off', 
				width=5, height=5, lenght=1

				).spawn(
					- 1, 
					- 1, 
					self.map
					)

		self.map[self.location['row']][self.location['elm']] = self

		self.inventory = {

				'head' : None, 
				'torso': None, 
				'wings': None, 
				'feet' : None, 
				'shoes': None, 
				'rings': []
			}

		self.backpack = [None for _ in range(self.backpack_slots)]

		self.recepts = []


	def check(self):
		'''
		Checks to see if all is in order with personagem
		'''

		self.map[self.location['row']][self.location['elm']] = self
		self.row = self.location['row']
		self.elm = self.location['elm']

		chank = self.area.chank_map[int(self.location['row']/10)][int(self.location['elm']/10)]

		if not chank.message:
			chank.msg()

		for index in range(len(self.backpack)):
			slot = self.backpack[index]
			if type(slot) is list:
				if len(slot) == 0:
					self.backpack[index] = None

		self.level()
		self.crity()
		self.emp_slot()
		self.select()
		self.using_items()
		self.game()

	def level(self):
		if self.Exp >= self.End_exp:
			self.Lvl += 1
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
		if self.selected and randint(1, 100) in range(self.crit):
			self.dmg = 2*randint(self.mid_dmg - 1, self.mid_dmg + 1)
		else:
			self.dmg = randint(self.mid_dmg - 1, self.mid_dmg + 1)

	def emp_slot(self):
		for slot in self.backpack:
			if slot is None:
				self.empt_slot = self.backpack.index(slot)
				break
			else:
				self.empt_slot = None

	def select(self):
		if self.selected != None:
			if not(self.selected in self.used_items):
				self.selected.using(self)

	def using_items(self):
		for item in self.used_items:
			item.using(self)

	def game(self):
		if self.hlt <= 0:
			links.hp -= 1
			links.game = 'Game over'
			self.reset()

	def reset(self):
		'''
		Restart the level and Avatar
		'''
		fst_row = int(float(self.area.rows)/2)
		fst_elm = int(float(self.area.elms)/2)
		if self.selected:
			self.selected.use = False
		self.map[self.location['row']][self.location['elm']] = DieChest()
		self.location['row'] = fst_row
		self.location['elm'] = fst_elm
		self.map[fst_row + 1][fst_elm] = Floor()
		for slot in self.backpack:
			slot = None
		self.hlt = self.full_hlt
		self.armor = self.full_armor
		self.mana = self.full_mana
		self.memo = Floor
		if self in intoxicated:
			del intoxicated[self]

	def print_inventory(self, index, names=None, prints=None):

		lenght = 0

		for item in self.backpack:

			if type(item) is list:
				item = item[0]

			if item:
				new_lenght = 2 + 2 + len(item.name)
			else:
				new_lenght = 2 + 2 + 5

			if new_lenght > lenght:
				lenght = new_lenght

		lenght_add = 0

		if prints:
			if len(prints) > 1:

				for slot in prints:
					if len(slot) > lenght_add:
						lenght_add = len(slot)

		if names:
			if self.selected:
				names[-6] = 'selected'

				if index == 'selected':
					mark = ' <'
				else:
					mark = ''
				name = self.selected.name
				print(f'{name}{mark}')

			prints = []

			for key in self.inventory.keys():
				item = self.inventory[key]
				if item:
					name = item.name
				else:
					name = '_____'
				if key in ('head', 'feet'):
					dub_point = ':  '
				else:
					dub_point = ': '
				if index == key:
					mark = ' <'
				else:
					mark = ''
				print(f'{key}{dub_point}{name}{mark}')

			print()

				
		count = 1
		for item in self.backpack:
			if len(str(count)) == 1:
				point = '.   '
			else:
				point = '.  '
			if not item:
				item = '_____'
			elif type(item) is list:
				item = str(f'{item[0].name} x{len(item)}')
			else:
				item = item.name
			if count == index:
				mark = ' <'
			else:
				mark = ''
			add = ''
			if prints:
				if len(prints) >= count:
					add = prints[count-1]
			residue = ' ' * (lenght - len(item) - len(mark))
			print(f'{count}{point}{item}{mark}{residue}{add}')
			count += 1

	def open_inventory(self):
		'''
		Shows the contents of the inventory, 
		allows the player to view the data on the desired item, 
		as well as to use this item
		'''

		types = ['rings', 'shoes', 'feet', 'wings', 'torso', 'head']

		transfer = False

		slot = 1
		idx = slot

		while True:

			clear()

			self.check()
			self.stat()

			names = {-types.index(type_): type_ for type_ in types}

			self.print_inventory(slot, names)

			choices = [(Key.up, 'up'), (Key.down, 'down'), (Key.enter, 'select'), (Key.right, 'transfer'), (Key.esc, 'esc'), ('i', 'esc')]

			choice = smart_input(choices)

			if choice == 'esc': 
				break

			elif choice == 'up':
				if self.selected:
					num = -6
				elif transfer:
					num = 1
				else:
					num = -5
				if idx > num:
					idx -= 1 
					if 1 < idx+1 < len(self.backpack)+1:
						slot -= 1
					else:
						slot = names[idx]

			elif choice == 'down':
				if idx < len(self.backpack):
					idx += 1
					if 1 < idx+1:
						try:
							slot += 1
						except TypeError:
							slot = 1
					else:
						slot = names[idx]

			elif choice == 'select':
				if transfer:
					trans_item = self.backpack[idx]	

				elif idx > 0 or slot == 'selected':
					if slot == 'selected':
						item = self.selected
						idx += 1
					else:
						item = self.backpack[idx-1]
					print()
					if type(item) is list:
						item[0].print_details()
					elif item:
						item.print_details()
					else:
						print('None')

				else:
					item = self.inventory[slot]

					if item:
						print()
						item.print_details()
					else:
						print('\nNone')

				if not transfer:
					choices = [(Key.enter, 'use'), (Key.esc, 'esc')]
					second_choice = smart_input(choices)

					if second_choice == 'use' and not transfer:
						item = self.backpack[idx-1]
						if type(item) is list:
							item[0].using(self)
						elif item:
							item.using(self)
						elif self.selected:
							self.selected.stop_using(self)
						
			elif choice == 'transfer':

				if not transfer:
					transfer = True
					memo = self.backpack[idx]
				elif transfer:
					transfer = False
					memo, trans_item = trans_item, memo

	def add_to_inventory(self, *items):
		for item in items:

			try:
				if type(item) is list:
					if not item[0].recept in self.recepts:
						self.recepts.append(item[0].recept)
				if not item.recept in self.recepts:
					self.recepts.append(item.recept)
			except AttributeError:
				pass

			self.check()
			if type(item) is list:
				cont = True
				for index in range(len(self.backpack)):
					slot = self.backpack[index]
					if type(slot) is list:
						if type(slot[0]) == type(item[0]):
							self.backpack[index].extend(item)
							cont = False
				if cont:
					if self.empt_slot:
						self.backpack[self.empt_slot] = item
						self.emp_slot()

			elif item.type_ == 'Helmet' and self.inventory['head'] == None:
				item.using(self)
			elif item.type_ == 'Cuirass' and self.inventory['body'] == None:
				item.using(self)
			elif item.type_ == 'Wings' and self.inventory['wings'] == None:
				item.using(self)
			elif item.type_ == 'Leggings' and self.inventory['feet'] == None:
				item.using(self)
			elif item.type_ == 'Shoes' and self.inventory['shoes'] == None:
				item.using(self)
			elif self.empt_slot != None:
				self.backpack[self.empt_slot] = item
				self.emp_slot()
			else:
				print('inventory is full')
				sleep(0.3)
				break

			try:
				if not item.recept in self.recepts:
					self.recepts.append(item.recept)

			except AttributeError:
				pass

	def stat(self):
		print(f'level:  {self.Lvl}')
		if self in intoxicated:
			print(*list(set(self.status)))
		print(f'health: {self.hlt}')
		print(f'armor:  {self.armor}')
		print(f'mana:   {self.mana}')
		print(f'gold:   {self.gold}')
		print()
		print(f'exp: {self.Exp}/{self.End_exp}')
		print()

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
						self.count[para][2] = 'off'

	def skill_tree(self, index='off'):

		skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
		skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

		count = 0

		for skl in skl_nams:

			if skl == 'MAtk':
				dub_dot = ': '
			else:
				dub_dot = ':  '

			if count == index:
				mark = ' <'
			else:
				mark = ''

			print(f'{skl}{dub_dot}{skls[skl_nams.index(skl)]}{mark}')

			count += 1

		if index == 'off':
			input()

	def skill_up(self):

		clear()

		skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
		skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

		index = 0
		
		while self.Skill_points > 0:

			print(f'Skill points: {self.Skill_points}')

			self.skill_tree(index)

			choices = [(Key.up, 'up'), (Key.down, 'down'), (Key.enter, 'select'), (Key.esc, 'esc')]

			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if index > 0:
					index -= 1

			elif choice == 'down':
				if index < len(skl_nams)-1:
					index += 1

			elif choice == 'select':

				choice = skl_nams[index]

				if choice == 'Atk':
					self.Atk += 1
					if self.Atk % 10 == 0:
						self.mid_dmg += 20
				elif choice == 'MAtk':
					self.MAtk += 1
					self.mid_m_dmg += 100
				elif choice == 'Agi':
					self.Agi += 1
				elif choice == 'Vit':
					self.Vit += 1
					if self.Vit % 10 == 0:
						self.hlt += 10
				elif choice == 'Int':
					self.Int += 1
					if self.Int % 10 == 0:
						self.mid_m_dmg += 5
				elif choice == 'Dcs':
					self.Dcs += 1
				elif choice == 'Luc':
					self.Luc += 1
				
				self.Skill_points -= 1
			
			clear()
		
		clear()

		self.skill_tree()

		clear()

	def get_hit(self, dmg):
		if randint(1, 100) in range(self.chance['dodge Atk']) and self.armor < dmg:
			self.hlt -= dmg - self.armor
			print(f'get damage: {dmg - self.armor}')
			sleep(0.3)
		else:
			print('miss')
			sleep(0.3)

	def give_hit(self, obj, dir_):
		if isinstance(self.selected, metaStickCreate):
			stick = self.selected
			if dir_ == 'up':
				stick.hit(self.row-1, self.elm, self.map)
			elif dir_ == 'right':
				stick.hit(self.row, self.elm+1, self.map)
			elif dir_ == 'down':
				stick.hit(self.row+1, self.elm, self.map)
			elif dir_ == 'left':
				stick.hit(self.row, self.elm-1, self.map)

		elif randint(1, 100) in range(self.chance['hit']):
			obj.get_hit(self.dmg, self)

		else:
			print('miss')
			sleep(0.3)
