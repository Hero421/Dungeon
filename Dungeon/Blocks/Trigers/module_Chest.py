from random import choice as ch
from termcolor import colored
from pynput import keyboard
from pynput.keyboard import Key
from Methods.module_smart_input import smart_input

class Chest(object):
	'''
	The chest for the Avatar
	'''

	des = colored('C', 'yellow')

	def __init__(self, rarity=None):
		self.stat  = False
		self.items_= []
		self.rarity= rarity
		if self.rarity is None:
		#	rarity_of(self)
			self.rarity = 'common'

		super().__init__()

	def act(self, obj):
		'''
		The first time creates in the chest of random things, 
		depending on the rarity of the chest. 
		Open it.
		'''
		
		from module_links import items

		types_of_items = ['Sword', 'Wings', 'Drug', 'Stick']

		if self.stat == False:
			self.stat = True
			self.des  = colored('c', 'yellow')

			if self.rarity == 'common':
				for count in range(3):
					self.items_.append(ch(items['common'][ch(types_of_items)]))

			elif self.rarity == 'rare':
				for count in range(6):
					self.items_.append(ch(items['common'][ch(types_of_items)]))
				for count in range(3):
					self.items_.append(ch(items['rare'][ch(types_of_items)]))

			elif self.rarity == 'Epic':
				for count in range(9):
					self.items_.append(ch(items['common'][ch(types_of_items)]))
				for count in range(6):
					self.items_.append(ch(items['rare'][ch(types_of_items)]))
				for count in range(3):
					self.items_.append(ch(items['Epic'][ch(types_of_items)]))

			elif self.rarity == 'GODLY':
				for count in range(15):
					self.items_.append(ch(items['common'][ch(types_of_items)]))
				for count in range(10):
					self.items_.append(ch(items['rare'][ch(types_of_items)]))
				for count in range(5):
					self.items_.append(ch(items['Epic'][ch(types_of_items)]))
				for count in range(2):
					self.items_.append(ch(items['GODLY'][ch(types_of_items)]))

		items = [slot.name if not slot is None else slot for slot in self.items_]

		print(self.rarity)

		count = 1
		for slot in items:
			if len(items) < 10:
				if len(str(items.index(slot))) == 1:
					print(str(count) + '.' , slot)
			elif len(items) < 100:
				if len(str(items.index(slot))) == 1:
					print(str(count) + '. ', slot)
				if len(str(items.index(slot))) == 2:
					print(str(count) + '.' , slot)
			count += 1

		choices = [(keyboard.KeyCode(char=str(slot)), slot-1) for slot in range(len(items)+1)]

		choices.append((Key.esc, 'esc'))

		choice = smart_input(choices)

		if not choice == 'esc':

			item = self.items_[choice]

			if item:
				print()
				try:
					print(item.name)
				except AttributeError:
					pass
				try:
					print(item.type)
				except AttributeError:
					pass
				try:
					print(item.rarity)
				except AttributeError:
					pass
				try:
					print(item.desc)
				except AttributeError:
					pass
			else:
				print('None')

			print('\nGet?')

			choices = [(Key.enter, 'yes'), (Key.esc, 'no')]

			second_choice = smart_input(choices)
			
			if second_choice == 'yes':
				obj.add_to_inventory([item()])
				self.items_[choice] = None