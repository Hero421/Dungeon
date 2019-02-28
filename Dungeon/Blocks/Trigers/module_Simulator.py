from termcolor import colored

class Simulator(object):
	
	des = colored('{', 'yellow')
	
	def __init__(self):

		super().__init__()
	
	def get_hit(self, dmg):
		print('Taked domage:', dmg)
		input()
