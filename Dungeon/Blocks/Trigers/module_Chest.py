from random import choice as ch
from termcolor import colored
from pynput import keyboard
from pynput.keyboard import Key

from Methods.module_smart_input import smart_input
from module_links import clear, items

class Chest(object):
	'''
	The chest for the Avatar
	'''

	des = colored('C', 'yellow')

	def __init__(self, rarity=None):
		self.open  = False
		self.items = []
		self.rarity= rarity
		if self.rarity is None:
		#	rarity_of(self)
			self.rarity = 'common'

		super().__init__()

	def generator(self):

		types_of_items = ['Sword', 'Wings', 'Drug', 'Stick']

		if self.rarity == 'common':
			for count in range(3):
				self.items.append(ch(items['common'][ch(types_of_items)]))

		elif self.rarity == 'rare':
			for count in range(6):
				self.items.append(ch(items['common'][ch(types_of_items)]))
			for count in range(3):
				self.items.append(ch(items['rare'][ch(types_of_items)]))

		elif self.rarity == 'Epic':
			for count in range(9):
				self.items.append(ch(items['common'][ch(types_of_items)]))
			for count in range(6):
				self.items.append(ch(items['rare'][ch(types_of_items)]))
			for count in range(3):
				self.items.append(ch(items['Epic'][ch(types_of_items)]))

		elif self.rarity == 'GODLY':
			for count in range(15):
				self.items.append(ch(items['common'][ch(types_of_items)]))
			for count in range(10):
				self.items.append(ch(items['rare'][ch(types_of_items)]))
			for count in range(5):
				self.items.append(ch(items['Epic'][ch(types_of_items)]))
			for count in range(2):
				self.items.append(ch(items['GODLY'][ch(types_of_items)]))

	def print_items(self, index):

		items = [slot.name if slot else '_____' for slot in self.items]

		count = 0
		for slot in items:
			if len(items) < 10:
				if len(str(items.index(slot))) == 1:
					dot = '.'
			elif len(items) < 100:
				if len(str(items.index(slot))) == 1:
					dot = '. '
				if len(str(items.index(slot))) == 2:
					dot = '.'

			if index == count:
				mark = ' <'
			else:
				mark = ''

			print(f'{count+1}{dot}{slot}{mark}')

			count += 1

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

		index = 0

		while True:

			clear()

			print(f'\n{self.rarity}\n')

			self.print_items(index)

			choices = [(Key.up, 'up'), (Key.down, 'down'), (Key.enter, 'select'), (Key.esc, 'esc')]

			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if 0 < index:
					index -= 1

			elif choice == 'down':
				if index < len(self.items):
					index += 1

			elif choice == 'select':

				item = self.items[index]

				if item:
					print()
					item.print_details(item)

				else:
					print('None')

				print('\nGet?')

				choices = [(Key.enter, 'yes'), (Key.esc, 'no')]

				second_choice = smart_input(choices)
				
				if second_choice == 'yes':
					obj.add_to_inventory([item()])
					self.items[index] = None