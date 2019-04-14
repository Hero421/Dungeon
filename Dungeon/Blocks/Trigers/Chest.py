from random import randint, choice as ch
from termcolor import colored
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep

from Methods.smart_input import smart_input
from Methods.choice_of import choice_of
from links import clear, items

from Blocks.Trigers.metaTriger import Triger
from Blocks.Trigers.Workbench import Workbench

from Items.Resources.Board import Board
from Items.Resources.Iron_bar import IronBar

class Chest(Triger):
	'''
	The chest for the Avatar
	'''

	des = colored('C', 'yellow')

	def __init__(self, rarity=None):

		self.recept = {Board: 5, IronBar: 1, 'place': Workbench, 'resut': Chest}
		self.name = 'Chest'
		self.type_= 'Triger'
		self.desc = 'Something'
		self.items= list()
		self.open = False
		self.rarity= rarity
		if self.rarity is None:
		#	rarity_of(self)
			self.rarity = 'common'

		super().__init__()

	def func(self, rarity, num):

		types_of_items = ['Sword', 'Drug', 'Resource']

		for count in range(num):
			type_= ch(types_of_items)
			if type_ == 'Resource':
				num = randint(5, 20)
				res = ch(items[rarity][type_])
				item = [res() for _ in range(1, num)]
			else:
				item = ch(items[rarity][type_])()

			self.items.append(item)

	def generator(self):

		if self.rarity == 'common':
			self.func('common', randint(2, 4))

		elif self.rarity == 'rare':
			self.func('common', randint(2, 5))
			self.func('rare'  , randint(1, 2))

		elif self.rarity == 'Epic':
			self.func('common', randint(5, 10))
			self.func('rare'  , randint(2, 5))
			self.func('Epic'  , randint(1, 2))

		elif self.rarity == 'GODLY':
			self.func('common', randint(8, 16))
			self.func('rare'  , randint(4, 10))
			self.func('Epic'  , randint(0, 2))
			self.func('GODLY', 1)

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

		idx = 0

		clear()
		print(f'\n{self.rarity}\n')
		sleep(0.5)

		while True:

			item, idx, lst, esc = choice_of(obj.backpack, self.items, idx)
			
			if esc: break

			if lst == 'sec':
				obj.add_to_inventory(item)
				self.items[idx] = None

			elif None in self.items:
				self.items[self.items.index(None)] = item
				obj.backpack[idx] = None
