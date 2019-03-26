from random import randint
from termcolor import colored

from Blocks.Air import Air
from Blocks.Trigers.metaTriger import Triger
from Methods.effect_overlay import effect_overlay

from Enemys.metaEnemy import metaEnemy

class Spike(Triger):
	
	des = Air.des

	def __init__(self):
		self.name = 'Spike'
		self.type_= 'Triger'
		self.desc = 'Something'

	def walk(self, choice, obj):

		dmg = randint(1, 3)
		degree = randint(1, 15)

		from links import ses_avatars

		if self.des == ' ':
			self.des = colored('^', 'red')
		
		obj.get_hit(dmg)
		
		if randint(1, 100) in range(20):
			effect_overlay(obj, dmg, degree, 'spike hlt down')

	def act(self, obj, dir_):
		'''
		Breaks the block
		'''

		from links import ses_avatars

		row = obj.row
		elm = obj.elm

		if dir_ == 'up':
			row -= 1
		elif dir_ == 'right':
			elm += 1
		elif dir_ == 'down':
			row += 1
		elif dir_ == 'left':
			elm -= 1

		obj.map[row][elm] = ()
