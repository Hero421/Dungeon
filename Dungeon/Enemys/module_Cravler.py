from Enemys.module_metaEnemy import metaEnemy

from termcolor import colored

class Cravler(metaEnemy):

	des = colored('r', 'red')
	type= 'Cravler'

	def __init__(self, row, elm):
		self.row = row
		self.elm = elm
		from module_links import ses_area
		self.map = ses_area.map
		super().__init__( self.row,
						  self.elm,
						  hlt=5, 
						  dmg=10, 
						  radius=4, 
						  dodge_Atk=5, 
						  dodge_MAtk=0, 
						  chance_hit=70, exp=4
						)
		self.list = ['move']