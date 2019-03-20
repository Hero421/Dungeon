from Enemys.metaEnemy import metaEnemy

from termcolor import colored

class Cravler(metaEnemy):

	des = colored('r', 'red')

	def __init__(self, row, elm, map_):
		self.row = row
		self.elm = elm
		self.map = map_
		super().__init__( self.row,
						  self.elm,
						  hlt=5, 
						  dmg=10, 
						  radius=4, 
						  dodge_Atk=5, 
						  dodge_MAtk=0, 
						  chance_hit=70, 
						  exp=4
						)
		self.list = ['move' for count in range(100)]