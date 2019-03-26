from termcolor import colored

from Blocks.Trigers.metaTriger import Triger

class Simulator(Triger):
	
	des = colored('{', 'yellow')
	
	def __init__(self):

		self.name = 'Simulator'
		self.desc = 'Something'

		super().__init__()
	
	def get_hit(self, dmg, obj):
		print('Taked domage:', dmg)
		input()
