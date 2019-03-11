from random import randint, choice
from termcolor import colored

from time import sleep

from Blocks.module_metaContainer import Container

from module_links import items, types_of_items

class GoldOre(Container):
	
	des = colored('*', 'yellow')
	
	def give(self, obj):
		random_num = randint(5, 15)
		obj.gold += random_num
		obj.Exp += 5
		print('You got: ' + str(random_num) + ' gold')
		sleep(0.5)

class Pot(Container):
	
	des = colored('+', 'yellow')
	
	def give(self, obj):

		for count in range(3):
			obj.gold += randint(10, 50)
			obj.add_to_inventory([choice(items['common'][choice([types_of_items])] for count in range(randint(1, 5)))])