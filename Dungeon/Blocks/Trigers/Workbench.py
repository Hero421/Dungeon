from time import sleep
from pynput.keyboard import Key

from links import clear
from Methods.smart_input import smart_input

from Blocks.Trigers.metaTriger import Triger

class Workbench(Triger):

	des = 'W'

	def __init__(self):
		self.name = 'Workbench'
		self.type_= 'Triger'
		self.desc = 'Something'

	def act(self, obj):

		self.recepts = []

		index = len(obj.backpack) + 1

		while True:

			obj.check()

			clear()

			obj.print_inventory(index, prints=self.print_recepts(index-len(obj.backpack)-1, obj))

			choices = {Key.up: 'up', Key.down: 'down', Key.left: 'left', Key.right: 'right', Key.enter: 'select', Key.esc: 'esc'}
			choice = smart_input(choices)

			if choice == 'esc': break

			elif choice == 'up':
				if len(obj.backpack)+1 < index:
					index -= 1

			elif choice == 'down':
				if index < len(obj.backpack) + len(self.recepts):
					index += 1

			elif choice == 'select':

				selected_recept = self.recepts[index-len(obj.backpack)-1]

				chk = True

				for key in selected_recept.keys():
					try:
						if not key in ('place', 'result'):
							if self.resources_in_backpack[key] < selected_recept[key]:
								chk = False
					except KeyError:
						chk = False

				if chk:
					for resource in selected_recept.keys():
						var = True
						for slot in obj.backpack:
							if type(slot) is list and var:
								if len(slot) > 0:
									if type(slot[0]) == resource:
										for _ in range(selected_recept[resource]):
											del slot[0]
										var = False
										break

					obj.add_to_inventory(selected_recept['result'])

				else:
					print('\nyou don\'t have enough resources')
					sleep(0.8)

	def print_recepts(self, index, obj):

		self.resources_in_backpack = {}
		for slot in obj.backpack:
			if slot:
				if type(slot) is list:
					if slot[0].type_== 'Resource':
						if not type(slot[0]) in self.resources_in_backpack.keys():
							self.resources_in_backpack[type(slot[0])] = len(slot)
				else:
					if slot.type_== 'Resource':
						if not type(slot) in self.resources_in_backpack.keys():
							self.resources_in_backpack[type(slot)] = 1

		resources_in_obj_recepts = {}
		for recept in obj.recepts:
			for resource in recept.keys():
				if not resource in ('place', 'result'):
					if not resource in resources_in_obj_recepts.keys():
						if recept['place'] == type(self):
							resources_in_obj_recepts[resource] = obj.recepts.index(recept)

		count = 0
		recepts = []
		strings = []

		for res_b in self.resources_in_backpack.keys():
			if res_b in resources_in_obj_recepts.keys():
				recept = obj.recepts[resources_in_obj_recepts[res_b]]
				if not recept in self.recepts:
					self.recepts.append(recept)

		for recept in self.recepts:
			string = ''	
			var = False
			for key in recept:
				if key == 'result':
					result = recept['result']
					string += f' = {result.name}'
					break
				elif not key == 'place':
					if var:
						plus = ' + '
					else:
						var = True
						plus= ''
					num = recept[key]
					string += f'{plus}{key.name} x{num}'
			if count == index:
				string += ' <'
			count += 1
			if not string in strings:
				strings.insert(self.recepts.index(recept), string)

		print(strings)

		return strings

