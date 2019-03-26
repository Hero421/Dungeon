from Blocks.Air import Air

class Triger:

	def __init__(self):
		self.type_ = 'Triger'

	def raze(self, choice, obj):
		'''
		Breaks the block
		'''

		from links import ses_avatars

		if obj in ses_avatars.values():
			
			obj.add_to_inventory(self)
			
			lay = obj.lay
			row = obj.row
			elm = obj.elm

			if choice == 'up':
				row -= 1
			elif choice == 'right':
				elm += 1
			elif choice == 'down':
				row += 1
			elif choice == 'left':
				elm -= 1

		from Blocks.Containers.Stone_block import StoneBlock

		obj.map[lay][row][elm] = Air(lay, row, elm, obj.map)

	def using(self, obj):

		if obj.selected:
			obj.selected.stop_using(obj)
		obj.selected = self
		for idx in range(len(obj.backpack)):
			if obj.backpack[idx] == self:
				obj.backpack[idx] = None
				break

	def stop_using(self, obj):

		obj.selected = None
		obj.add_to_inventory(self)

	def print_details(self):
		
		print(f'name: {self.name}')
		print(f'type: {self.type_}')
		print(f'desc: {self.desc}')