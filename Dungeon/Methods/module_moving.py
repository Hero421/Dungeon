from Blocks.module_Surfaces import metaSurface as Surface, Chasm
from Blocks.module_Stone import Stone
from Blocks.Trigers.module_Spike import Spike
from Blocks.Trigers.module_Door  import Door
from Blocks.Trigers.module_Chest import Chest
from Blocks.Trigers.module_Table import Table
from Blocks.Trigers.module_Portal import Portal
from Blocks.Trigers.module_Source import Source
from Blocks.Trigers.module_DieChest import DieChest
from Blocks.Trigers.module_Simulator import Simulator

from Enemys.module_metaEnemy import metaEnemy

from Blocks.module_metaContainer import Container

import module_links

def moving(obj, *choice):

	if   choice[0] == 'up':    dir_= obj.map[obj.row - 1][obj.elm]
	elif choice[0] == 'right': dir_= obj.map[obj.row][obj.elm + 1]
	elif choice[0] == 'down':  dir_= obj.map[obj.row + 1][obj.elm]
	elif choice[0] == 'left':  dir_= obj.map[obj.row][obj.elm - 1]

	if len(choice) == 1:
		if isinstance(dir_, (Surface, Spike, Door, Stone, Container, Chasm)):
			dir_.walk(choice[0], obj)

	elif choice[1] == 'act':
		if type(dir_) in (Chest, Table, Source, Portal, DieChest, Door):
			dir_.act(obj)

		elif type(dir_) is Spike:
			dir_.act(obj, choice[0])

	elif choice[1] == 'hit':
		if obj.selected:
			if obj.selected.type != 'Stick':
				if type(dir_) is Simulator or isinstance(dir_, metaEnemy):
					obj.give_hit(dir_)
			else:
				obj.selected.hit(row, elm)