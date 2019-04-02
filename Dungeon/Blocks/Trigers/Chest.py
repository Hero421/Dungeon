from random import randint, choice as ch
from termcolor import colored
from pynput import keyboard
from pynput.keyboard import Key

from Methods.smart_input import smart_input
from links import clear, items

from Blocks.Trigers.metaTriger import Triger
from Blocks.Trigers.Workbench import Workbench

from Items.Resources.Board import Board
from Items.Resources.Iron_bar import IronBar

class Chest(Triger):
	'''
	The chest for the Avatar
	'''

	des = colored('C', 'yellow')

	def __init__(self, rarity=None):

		self.recept = {Board: 5, IronBar: 1, 'place': Workbench, 'resut': Chest}
		self.name = 'Chest'
		self.type_= 'Triger'
		self.desc = 'Something'
		self.open  = False
		self.items = list()
		self.rarity= rarity
		if self.rarity is None:
		#	rarity_of(self)
			self.rarity = 'common'

		super().__init__()

	def generator(self):

		types_of_items = ['Sword', 'Drug', 'Resource']

		if self.rarity == 'common':
			for count in range(randint(3, 6)):
				type_= ch(types_of_items)
				if type_ == 'Resource':
					num = randint(5, 20)
					recour = ch(items['common'][type_])
					item = list()
					for _ in range(num):
						item.append(recour())
					self.items.append(item)
				else:
					self.items.append(ch(items['common'][type_])())

		elif self.rarity == 'rare':
			for count in range(6):
				self.items.append(ch(items['common'][ch(types_of_items)])())
			for count in range(3):
				self.items.append(ch(items['rare'][ch(types_of_items)])())

		elif self.rarity == 'Epic':
			for count in range(9):
				self.items.append(ch(items['common'][ch(types_of_items)])())
			for count in range(6):
				self.items.append(ch(items['rare'][ch(types_of_items)])())
			for count in range(3):
				self.items.append(ch(items['Epic'][ch(types_of_items)])())

		elif self.rarity == 'GODLY':
			for count in range(15):
				self.items.append(ch(items['common'][ch(types_of_items)])())
			for count in range(10):
				self.items.append(ch(items['rare'][ch(types_of_items)])())
			for count in range(5):
				self.items.append(ch(items['Epic'][ch(types_of_items)])())
			for count in range(2):
				self.items.append(ch(items['GODLY'][ch(types_of_items)])())

		for _ in range(8-len(self.items)):
			self.items.append(None)

	def print_items(self, index, obj):

		prints = list()
		count  = 1

		for slot in self.items:
			if len(self.items) < 10:
				if len(str(self.items.index(slot))) == 1:
					dot = '.'
			elif len(self.items) < 100:
				if len(str(self.items.index(slot))) == 1:
					dot = '. '
				if len(str(self.items.index(slot))) == 2:
					dot = '.'

			if type(slot) is list:
				item = f'{slot[0].name} x{len(slot)}'
			elif slot:
				item = slot.name
			else:
				item = '_____'

			if index == count + len(obj.backpack):
				mark = ' <'
			else:
				mark = ''

			prints.append(f'{count}{dot}{item}{mark}')

			count += 1

		return prints

	def act(self, obj):
		'''
		The first time creates in the chest of random things, 
		depending on the rarity of the chest. 
		Open it.
		'''

		if not self.open:

			self.generator()

			self.open = True
			self.des  = colored('c', 'yellow')

		index = 1

		while True:

			clear()

			print(f'\n{self.rarity}\n')

			obj.print_inventory(index, prints=self.print_items(index, obj))

			choices = {Key.up: 'up', Key.down: 'down', Key.left: 'left', Key.right: 'right', Key.enter: 'select', Key.esc: 'esc'}

			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if 1 < index and not index == len(obj.backpack)+1:
					index -= 1

			elif choice == 'down':
				if index < len(obj.backpack) + len(self.items) and not index == len(obj.backpack):
					index += 1

			elif choice == 'left':
				if index > len(obj.backpack):
					index -= len(obj.backpack)

			elif choice == 'right':
				if index < len(obj.backpack):
					if index > len(self.items):
						index = len(obj.backpack) + len(self.items)
					else:
						index += len(obj.backpack)

			elif choice == 'select':

				if index > len(obj.backpack)-1:

					item = self.items[index-len(obj.backpack)-1]

					if type(item) is list:
						print()
						item[0].print_details()

					elif item:
						print()
						item.print_details()

					else:
						print('\nNone')
						continue

					print('\nGet?')

					choices = {Key.enter: 'yes', Key.esc: 'no'}

					second_choice = smart_input(choices)
					
					if second_choice == 'yes':
						obj.add_to_inventory(item)
						self.items[index-len(obj.backpack)-1] = None

				else:

					item = obj.backpack[index-1]

					if None in self.items:
						self.items[self.items.index(None)] = item
						obj.backpack[index-1] = None
