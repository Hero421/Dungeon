from random import choice as ch

class Chest(object):
	'''
	The chest for the Avatar
	'''

	des = 'C'

	def __init__(self, rarity=None):
		self.stat  = False
		self.items_= []
		self.items = []
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
		
		print(items)
		types_of_items = ['Sword', 'Wings', 'Drug', 'Stick']

		if self.stat == False:
			self.stat = True
			self.des  = 'c'

			if self.rarity == 'common':
				for count in range(3):
					self.items_.append(ch(items['common']['Sword']))

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

		self.items = [slot.name if not(slot is None) else slot for slot in self.items_]

		print(self.rarity)

		count = 1
		for slot in self.items:
			if len(self.items) < 10:
				if len(str(self.items.index(slot))) == 1:
					print(str(count) + '.' , slot)
			elif len(self.items) < 100:
				if len(str(self.items.index(slot))) == 1:
					print(str(count) + '. ', slot)
				if len(str(self.items.index(slot))) == 2:
					print(str(count) + '.' , slot)
			count += 1

		choice = input()

		self.corrected_choices = [str(slot) for slot in range(len(self.items)+1)]

		if choice in self.corrected_choices:
			choice = int(choice) - 1
			obj.add_to_inventory([self.items_[choice]()])
			self.items_[choice] = None
			self.items [choice] = None