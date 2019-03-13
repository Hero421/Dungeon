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

def distributor(obj, dir_, type_):

	if   dir_ == 'up':    cell = obj.map[obj.row - 1][obj.elm]
	elif dir_ == 'right': cell = obj.map[obj.row][obj.elm + 1]
	elif dir_ == 'down':  cell = obj.map[obj.row + 1][obj.elm]
	elif dir_ == 'left':  cell = obj.map[obj.row][obj.elm - 1]

	if   type_== 'mov' and isinstance(cell, (Surface, Spike, Door, Stone, Container, Chasm)):   cell.walk(dir_, obj)
	elif type_== 'hit' and isinstance(cell, (Simulator, metaEnemy)): obj.give_hit(cell)
	elif type_== 'act' and type(cell) in (Chest, Table, Source, Portal, DieChest, Door, Spike): cell.act(obj, dir_) if type(cell) is Spike else cell.act(obj)