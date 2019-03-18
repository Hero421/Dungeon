from pynput.keyboard import Key

from Items.Resources.module_Gold_Ore import GoldOre
from Methods.module_smart_input import smart_input
from module_links import clear

class Oven:

	des = '&'

	def __init__(self):
		self.slots = [[] for _ in range(5)]

	def act(self, obj):

		slot = 0

		while True:

			obj.check()

			clear()

			obj.print_inventory(slot)

			print()

			self.print_slots(slot, obj)

			choices = [(Key.up, 'up'), (Key.down, 'down'), (Key.enter, 'select'), (Key.esc, 'esc')]
			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if 0 < slot:
					slot -= 1

			elif choice == 'down':
				if slot < len(obj.backpack) + len(self.slots):
					slot += 1

			elif choice == 'select':

				if slot-1 in range(len(obj.backpack)):

					item = obj.backpack[slot-1]

					if type(item) is list:
						if type(item[0]) is GoldOre:
							lenght = len(item)-1
							for index in range(len(item)):
								item[lenght - index].remelting(self, obj, slot-1)
				
				elif slot < len(self.slots) + len(obj.backpack):

					item = self.slots[slot-len(obj.backpack)-1]

					if item:
						obj.add_to_inventory(item)
						self.slots[self.slots.index(item)] = []

	def print_slots(self, index, obj):

		count = 1

		for slot in self.slots:

			if count < 10:
				dot = '.  '
			else:
				dot = '. '

			if len(slot) == 0:
				name = '_____'
			elif len(slot) == 1:
				name = slot[0].name
			else:
				name = f'{slot[0].name} x{len(slot)}'

			if index == count + len(obj.backpack):
				mark = ' <'
			else:
				mark = ''

			print(f'{count}{dot}{name}{mark}')

			count += 1