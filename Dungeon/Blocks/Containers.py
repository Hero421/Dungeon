from random import randint, choice
from termcolor import colored

from time import sleep

from Blocks.metaContainer import Container
from Items.Resources.Gold_Ore import GoldOre
from Items.Resources.Iron_Ore import IronOre
from Items.Resources.Broken_Board import BrokenBoard

from links import items, types_of_items

class GoldOreBlock(Container):
	
	des = colored('*', 'yellow')
	
	def give(self, obj):
		num = randint(1, 3)
		exp = randint(3, 7)
		obj.add_to_inventory([GoldOre() for _ in range(num)])
		obj.Exp += exp
		print(f'You got: {num} gold ore and {exp} exp')
		sleep(0.8)

class IronOreBlock(Container):
	
	des = '*'
	
	def give(self, obj):
		num = randint(1, 3)
		exp = randint(1, 4)
		obj.add_to_inventory([IronOre() for _ in range(num)])
		obj.Exp += exp
		print(f'You got: {num} iron ore and {exp} exp')
		sleep(0.8)

class Box(Container):

	des = colored(':', 'yellow')

	def give(self, obj):
		if randint(1, 100) in range(40):
			gold = randint(1, 15)
			obj.gold += gold
			gold = f'{gold} gold, '
		else:
			gold = ''

		boards = randint(2, 8)
		obj.add_to_inventory([BrokenBoard() for _ in range(boards)])

		print(f'You got: {gold}{boards} boards')

		sleep(0.5)

class Pot(Container):
	
	des = colored('+', 'yellow')
	
	def give(self, obj):

		gold = randint(10, 30)
		obj.gold += gold
		
		print(f'You got: {gold} gold')
		
		sleep(0.5)