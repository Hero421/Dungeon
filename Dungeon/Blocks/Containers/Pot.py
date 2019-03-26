from random import randint
from termcolor import colored

from time import sleep

from Blocks.Containers.metaContainer import Container

class Pot(Container):
	
	des = colored('+', 'yellow')
	
	def give(self, obj):

		gold = randint(10, 30)
		obj.gold += gold
		
		print(f'You got: {gold} gold')
		
		sleep(0.5)