from random import randint, choice
from termcolor import colored

from time import sleep

from Blocks.module_metaContainer import Container
from Items.Resources.module_Gold_Ore import GoldOre

from module_links import items, types_of_items

class GoldOreBlock(Container):
	
	des = colored('*', 'yellow')
	
	def give(self, obj):
		num = randint(5, 15)
		exp = randint(3, 8)
		obj.add_to_inventory([GoldOre() for _ in range(num)])
		obj.Exp += exp
		print(f'You got: {num} gold ore and {exp} exp')
		sleep(0.8)

class Pot(Container):
	
	des = colored('+', 'yellow')
	
	def give(self, obj):

		for count in range(3):
			obj.gold += randint(10, 50)
			obj.add_to_inventory([choice(items['common'][choice([types_of_items])] for count in range(randint(1, 5)))])