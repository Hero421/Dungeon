from random import randint
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key

from Methods.smart_input import smart_input
from Methods.choice_of import choice_of

from Generations.Rooms import Room, Rooms, Corridor
import links
from links import intoxicated, clear

from Blocks.Air import Air
from Blocks.Trigers.DieChest import DieChest

from Items.Swords.metaSword import Sword
from Items.Sticks.metaStickCreate import StickCreate

class Avatar(object):

	def __init__(self, ID, room=True):

		self.status    = list()
		self.used_items= list()
		self.recepts   = list()
		self.count     = dict()  # {'self.name': [start, stop, stat(on/off), self]}
		self.chance    = dict()  # {'ivent': chance}
		self.choices   = None

		self.gold = 0

		self.des  = '0'

		self.full_hlt  = 10
		self.full_mana = 0

		self.mid_dmg   = 2
		self.mid_m_dmg = 1

		self.dodge_Atk = 5
		self.dodge_MAtk= 1

		self.hit   = 1
		self.armor = 0

		self.power = 1

		self.backpack_slots = 20

		self.Atk  = 1
		self.MAtk = 1
		self.Agi  = 1
		self.Vit  = 1
		self.Int  = 1
		self.Dcs  = 1
		self.Luc  = 1

		self.Lvl  = 1

		self.Exp = 0
		self.End_exp = 20

		self.Skill_points = 0

		self.crit = 0

		self.hlt  = self.full_hlt
		self.mana = self.full_mana
		self.dmg  = randint(self.mid_dmg   - 1, self.mid_dmg   + 1)
		self.m_dmg= randint(self.mid_m_dmg - 1, self.mid_m_dmg + 1)

		self.ID = ID

		self.area = links.ses_area
		self.map  = self.area.map

		links.ses_avatars[ID] = self

		self.chance['dodge Atk']  = 100 - self.dodge_Atk
		self.chance['dodge MAtk'] = 100 - self.dodge_MAtk
		self.chance['hit']        = 100 - self.hit

		self.count['Source'] = [40, 0, 'on', None]

		self.lay = 0
		self.row = 0
		self.elm = 0

		if room:
			Rooms(

				['the initial room', 'room with the chest'],
				WIDTH=5, HEIGHT=5

				).spawn(
					  0,
					- 1, 
					- 1, 
					self.map
					)

		self.map[self.lay][self.row][self.elm] = self

		self.select= None
		self.head  = None 
		self.torso = None 
		self.wings = None 
		self.feet  = None 
		self.shoes = None 
		self.rings = []

		self.backpack = [None for _ in range(self.backpack_slots)]

		self.fall_var = False
		# self.fall_var2= False

	def check(self):
		'''
		Checks to see if all is in order with avatar
		'''

		self.map[self.lay][self.row][self.elm] = self

		chank = self.area.chank_map[int(self.lay/10)][int(self.row/10)][int(self.elm/10)]

		if not chank.message:
			chank.msg()

		for idx in range(len(self.backpack)):
			slot = self.backpack[idx]
			if type(slot) is list:
				if len(slot) == 0:
					self.backpack[idx] = None
				elif len(slot) == 1:
					self.backpack[idx] = slot[0]

		self.level()
		self.crity()
		self.selected()
		self.using_items()
		self.game()

	def chk_walk(self, obj):
		return True
		pass

	def fall(self):

		if self.fall_var and type(self.map[self.lay-1][self.row][self.elm]) is Air:
			self.map[self.lay][self.row][self.elm] = Air()
			self.lay -= 1
			self.fall_var = False

		if type(self.map[self.lay-1][self.row][self.elm]) is Air:
			self.fall_var = True

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
		if self.select and randint(1, 100) in range(self.crit):
			self.dmg = 2*randint(self.mid_dmg - 1, self.mid_dmg + 1)
		else:
			self.dmg = randint(self.mid_dmg - 1, self.mid_dmg + 1)

	def selected(self):
		if self.select:
			if not(self.select in self.used_items):
				self.select.using(self)

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
		if self.selected:
			self.selected.use = False
		self.map[self.lay][self.row][self.elm] = DieChest()
		self.lay = 0
		self.row = 0
		self.elm = 0
		for slot in self.backpack:
			slot = None
		self.hlt = self.full_hlt
		self.armor = self.full_armor
		self.mana = self.full_mana
		self.memo = Floor
		if self in intoxicated:
			del intoxicated[self]

	def open_inventory(self):
		'''
		Shows the contents of the inventory, 
		allows the player to view the data on the desired item, 
		as well as to use this item
		'''

		idx = 0
		slot= None

		while True:

			item, idx, lst, esc = choice_of(self.backpack, idx=idx, slot=slot, obj=self, inv=True)

			self.check()

			if esc: break

			choices = {Key.enter: True, Key.esc: False}
			use = smart_input(choices)

			if use:
				if type(item) is list:
					item[0].using(self)
				elif item:
					item.using(self)
				elif self.select:
					self.select.stop_using(self)

	def add_to_inventory(self, *items):

		for item in items:

			self.check()
			
			tmp  = item
			cont = True
			tmp_dict = {'Helmet': 'head', 'Cuirass': 'body', 'Wings': 'wings', 'Leggings': 'feet', 'Shoes': 'shoes'}

			if type(item) is list:
				tmp = item[0]
				if len(item) == 1:
					item = tmp = item[0]
			try:
				if not tmp.recept in self.recepts: self.recepts.append(tmp.recept)
			except AttributeError: pass

			if tmp:
				if tmp.type_ in ('Resource', 'Drug', 'Block'):
					if not type(item) is list: item = [item]
					for index in range(len(self.backpack)):
						slot = self.backpack[index]
						if type(slot) is list:
							if type(slot[0]) == type(tmp):
								if type(item) is list:self.backpack[index].extend(item)
								else:self.backpack[index].append(item)
								cont = False
					if cont and None in self.backpack:
						self.backpack[self.backpack.index(None)] = item
					continue

				elif tmp.type_ in tmp_dict.keys():
					if self.get(tmp_dict[tmp.type_]) == None:
						item.using(self)
				elif None in self.backpack:
					self.backpack[self.backpack.index(None)] = item
				else:
					print('inventory is full')
					sleep(0.4)
					break

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

	def skill_tree(self, idx=False):

		skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
		skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

		count = 0

		for skl in skl_nams:
			
			dub_dot = ': ' if len(skl) == 3  else ':  '
			mark    = ' <' if count == idx else ''

			print(f'{skl}{dub_dot}{skls[skl_nams.index(skl)]}{mark}')

			count += 1

		if not idx:
			smart_input({Key.enter: None})

	def skill_up(self):

		clear()

		skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
		skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

		idx = 0
		
		while self.Skill_points > 0:

			print(f'Skill points: {self.Skill_points}')

			self.skill_tree(idx)

			choices = {Key.up: 'up', Key.down: 'down', Key.enter: 'select', Key.esc: 'esc'}
			choice  = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if idx > 0:
					idx -= 1

			elif choice == 'down':
				if idx < len(skl_nams)-1:
					idx += 1

			elif choice == 'select':

				choice = skl_nams[idx]

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

	def locate(self, dir_):

		if self.select:
			
			row = self.row
			elm = self.elm

			if   dir_ == 'up':    row -= 1
			elif dir_ == 'right': elm += 1
			elif dir_ == 'down':  row += 1
			elif dir_ == 'left':  elm -= 1

			if self.select.type_ == 'Triger':
				if type(self.select) is list:
					self.map[row][elm] = self.select[0]
					if len(self.select) > 1:
						del self.select[0]
					else:
						self.select = None
				else:
					self.map[row][elm] = self.select
					self.select = None

	def get_hit(self, dmg):
		if randint(1, 100) in range(self.chance['dodge Atk']) and self.armor < dmg:
			self.hlt -= dmg - self.armor
			print(f'get damage: {dmg - self.armor}')
			smart_input({Key.enter: None})
		else:
			print('miss')
			smart_input({Key.enter: None})

	def give_hit(self, obj, dir_):
		if isinstance(self.selected, metaStickCreate):
			stick = self.selected
			if dir_ == 'up':
				stick.hit(self.lay, self.row-1, self.elm, self.map)
			elif dir_ == 'right':
				stick.hit(self.lay, self.row, self.elm+1, self.map)
			elif dir_ == 'down':
				stick.hit(self.lay, self.row+1, self.elm, self.map)
			elif dir_ == 'left':
				stick.hit(self.lay, self.row, self.elm-1, self.map)

		elif randint(1, 100) in range(self.chance['hit']):
			obj.get_hit(self.dmg, self)

		else:
			print('miss')
			sleep(0.3)
