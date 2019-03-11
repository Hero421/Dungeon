from termcolor import colored
from pynput import keyboard
from pynput.keyboard import Key

from Methods.module_smart_input import smart_input

class DieChest(object):
	'''
	Chest with all the things of the Avatar, which is created at death
	'''

	des = colored('%', 'blue')

	def __init__(self, obj):
		self.obj = obj
		self.inventory = self.obj.inventory[1].copy()
		self.inv = {num: (self.inventory[key].name if not(key is None) else None) for num in range(1, len(self.inventory) + 1) for key in list(self.inventory)}

		super().__init__()

	def act(self, obj):
		'''
		Open it
		'''
		for count in range(len(list(self.inv))):
			count += 1
			if self.inventory[i]:
				print(i, self.inventory[i].name)
			else:
				print(i, 'None')

		choices = [(str(num), num) for num in range(1, len(list(self.inventory)) + 1)]

		choices.append((Key.esc, 'esc'))
		choices.append(('e', 'esc'))

		choice = smart_input(choices)

		if not choice == 'esc':
			self.object.add_to_inventory(self.inventory[int(choice)])
			self.inventory[int(choice)] = None

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