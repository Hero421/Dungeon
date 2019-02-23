class DieChest(object):
	'''
	Chest with all the things of the Avatar, which is created at death
	'''

	des = '%'

	def __init__(self):
		self.inventory = self.object.inventory[1].copy()
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
		choice = input()
		corrected_choices = [str(num) for num in range(1, len(list(self.inventory)) + 1)]
		if choice in corrected_dirs:
			self.object.add_to_inventory(self.inventory[int(choice)])
			self.inventory[int(choice)] = None