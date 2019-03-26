from pynput.keyboard import Key

from Methods.smart_input import smart_input
from links import clear

from Blocks.Trigers.metaTriger import Triger
from Items.Resources.metaResource import Resource

class Oven(Triger):

	des = '&'

	def __init__(self):
		self.name = 'Oven'
		self.type_= 'Triger'
		self.desc = 'Something'
		self.slots = [[] for _ in range(5)]

	def act(self, obj):

		slot = 1

		while True:

			obj.check()

			clear()

			obj.print_inventory(slot, prints=self.gen_slots(slot, obj))

			print()

			choices = {Key.up: 'up', Key.down: 'down', Key.left: 'left', Key.right: 'right', Key.enter: 'select', Key.esc: 'esc'}
			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if 1 < slot:
					slot -= 1

			elif choice == 'down':
				if slot < len(obj.backpack) + len(self.slots):
					slot += 1

			elif choice == 'left':
				if slot > len(obj.backpack):
					slot -= len(obj.backpack)

			elif choice == 'right':
				if slot < len(obj.backpack):
					if slot > len(self.slots):
						slot = len(obj.backpack) + len(self.slots)
					else:
						slot += len(obj.backpack)

			elif choice == 'select':

				if slot-1 in range(len(obj.backpack)):

					item = obj.backpack[slot-1]

					if type(item) is list:
						if isinstance(item[0], Resource):
							lenght = len(item)-1
							for index in range(len(item)):
								item[lenght - index].remelting(self, obj, slot-1)
				
				elif slot < len(self.slots) + len(obj.backpack):

					item = self.slots[slot-len(obj.backpack)-1]

					if item:
						obj.add_to_inventory(item)
						self.slots[self.slots.index(item)] = []

	def gen_slots(self, index, obj):

		prints = []
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

			prints.append(f'{count}{dot}{name}{mark}')

			count += 1

		return prints