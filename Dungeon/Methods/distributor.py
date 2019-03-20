from Blocks.Surfaces import metaSurface as Surface, Chasm
from Blocks.Stone import Stone
from Blocks.Trigers.Spike import Spike
from Blocks.Trigers.Door  import Door
from Blocks.Trigers.Oven  import Oven
from Blocks.Trigers.Chest import Chest
from Blocks.Trigers.Table import Table
from Blocks.Trigers.Portal import Portal
from Blocks.Trigers.Source import Source
from Blocks.Trigers.DieChest import DieChest
from Blocks.Trigers.Simulator import Simulator
from Blocks.Trigers.Workbench import Workbench

from Enemys.metaEnemy import metaEnemy

from Blocks.metaContainer import Container

import links

def distributor(obj, dir_, type_):

	if   dir_ == 'up':    cell = obj.map[obj.row - 1][obj.elm]
	elif dir_ == 'right': cell = obj.map[obj.row][obj.elm + 1]
	elif dir_ == 'down':  cell = obj.map[obj.row + 1][obj.elm]
	elif dir_ == 'left':  cell = obj.map[obj.row][obj.elm - 1]

	if   type_== 'mov' and isinstance(cell, (Surface, Spike, Door, Stone, Container, Chasm)):
		cell.walk(dir_, obj)

	elif type_== 'hit': 
		obj.give_hit(cell, dir_)

	elif type_== 'act' and type(cell) in (Chest, Table, Source, Portal, DieChest, Door, Spike, Oven, Workbench):
		if type(cell) is Spike:
			cell.act(obj, dir_)
		else:
			cell.act(obj)