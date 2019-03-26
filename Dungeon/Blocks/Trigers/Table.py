from time import sleep
from termcolor import colored

from Blocks.Trigers.metaTriger import Triger

class Table(Triger):
	'''
	Plaque with the inscription
	'''

	des = colored('=', 'yellow')

	def __init__(self, text=None):
		self.name = 'Table'
		self.type_= 'Triger'
		if text:
			self.text = text
		else:
			self.text = input('Text: ')
		super().__init__()

	def act(self, arg):
		'''
		Shows the inscription on the plate
		'''
		print(self.text + '\n')
		sleep(0.5)