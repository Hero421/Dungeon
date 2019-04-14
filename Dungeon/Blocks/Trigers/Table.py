from termcolor import colored
from pynput.keyboard import Key

from Methods.smart_input import smart_input
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
		smart_input({Key.enter: None})