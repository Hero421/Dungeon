from termcolor import colored

class Table(object):
	'''
	Plaque with the inscription
	'''

	des = colored('=', 'yellow')

	def __init__(self, text):
		self.text = text
		super().__init__()

	def act(self, arg):
		'''
		Shows the inscription on the plate
		'''
		input(self.text + '\n')
