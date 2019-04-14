from os import system
from pynput.keyboard import Key

from NPC.meta_NPC import NPC
from links import items
from Methods.smart_input import smart_input

class Trader(NPC):
	
	stat = False
	des = '$'

	items = [None for _ in range(10)]
	
	# def __init__(self):
	# 	self.generator()

	# def generator(self):
		
		

	def print_items(self, index, obj):

		for slot in self.items:

			if type(slot) is list:
				item = f'{slot[0].name} x{len(slot)}'
			elif slot:
				item = slot.name
			else:
				item = '_____'

			if slot:
				cost = f' cost: {item.cost} gold'
			else:
				cost = str()

			if index == count + len(obj.backpack):
				mark = ' <'
			else:
				mark = str()

			print(f'{item}{cost}{mark}')

	def choice_item(self, obj):

		index = 1

		while True:

			clear()

			obj.print_inventory(index, prints=self.print_items(index, obj))

			choices = {Key.up:    'up', 
					   Key.down:  'down', 
					   Key.left:  'left', 
					   Key.right: 'right', 
					   Key.enter: 'select', 
					   Key.esc:   'esc'}

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

					choices = {Key.enter: True, 
							   Key.esc:   False}

					answer = smart_input(choices)
					
					if answer:
						obj.add_to_inventory(item)
						self.items[index-len(obj.backpack)-1] = None

				else:

					item = obj.backpack[index-1]

					if None in self.items:
						self.items[self.items.index(None)] = item
						obj.backpack[index-1] = None
						obj.gold += item.cost

	def act(self, obj):

		index = 0

		while True:
			system('cls')
			print('Здравствуй, одинокий путник! С чем ты ко мне пожаловал?')
			questions = ['Что у тебя есть на продажу?', 'Есть ли для меня задание?']
			for qun in questions:
				if index == questions.index(qun):
					mark = ' <'
				else:
					mark = str()
				print(f'{qun}{mark}')

			choices = {Key.up:    'up', 
					   Key.down:  'down', 
					   Key.enter: 'select', 
					   Key.esc:   'esc'}

			choice = smart_input(choices)

			if choice == 'esc': break
			elif choice == 'up':
				if index > 0:
					index -= 1
			elif choice == 'down':
				if index < len(questions)-1:
					index += 1
			elif choice == 'select':
				if index == 0:
					pass
