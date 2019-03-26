from time import sleep

from Blocks.Chasm import Chasm
from Blocks.Trigers.Spike import Spike
from Blocks.Trigers.Door import Door
from Blocks.Air import Air
from Blocks.Trigers.metaTriger import Triger

from Enemys.metaEnemy import metaEnemy

from Blocks.Containers.metaContainer import Container

import links

def distributor(obj, dir_, type_):

	if   dir_ == 'North': cell = obj.map[obj.lay][obj.row - 1][obj.elm]
	elif dir_ == 'East':  cell = obj.map[obj.lay][obj.row][obj.elm + 1]
	elif dir_ == 'South': cell = obj.map[obj.lay][obj.row + 1][obj.elm]
	elif dir_ == 'West':  cell = obj.map[obj.lay][obj.row][obj.elm - 1]

	elif dir_ == 'up':    cell = obj.map[obj.lay + 1][obj.row][obj.elm]
	elif dir_ == 'down':  cell = obj.map[obj.lay - 1][obj.row][obj.elm]

	if   type_== 'mov' and isinstance(cell, (Spike, Door, Air)):
		cell.walk(dir_, obj)

	elif type_== 'raze' and isinstance(cell, (Container, Triger)):
		cell.raze(dir_, obj)

	elif type_== 'locate' and isinstance(cell, (Surface)):
		obj.locate(dir_)

	elif type_== 'hit': 
		obj.give_hit(cell, dir_)

	elif type_== 'act' and isinstance(cell, Triger):
		if type(cell) is Spike:
			cell.act(obj, dir_)
		else:
			cell.act(obj)