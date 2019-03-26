from random import randint
from time import sleep

from Blocks.Containers.metaContainer import Container
from Items.Resources.Iron_ore import IronOre

class IronOreBlock(Container):
	
	des = '*'
	
	def give(self, obj):
		num = randint(1, 3)
		exp = randint(1, 4)
		obj.add_to_inventory([IronOre() for _ in range(num)])
		obj.Exp += exp
		print(f'You got: {num} iron ore and {exp} exp')
		sleep(0.8)