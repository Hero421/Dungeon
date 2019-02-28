from Blocks.module_Surfaces import metaSurface as Surface, Wall
from Blocks.module_Stone import Stone
from Blocks.Trigers.module_Spike import Spike
from Blocks.Trigers.module_Door  import Door
from Blocks.Trigers.module_Chest import Chest
from Blocks.Trigers.module_Table import Table
from Blocks.Trigers.module_Portal import Portal
from Blocks.Trigers.module_Source import Source
from Blocks.Trigers.module_DieChest import DieChest

import module_links

def moving(obj, *choice):

	if not (choice[0] == 'act') and not (choice[0] == 'hit'):
		if choice[0] == 'up':
			if isinstance(obj.map[obj.row - 1][obj.elm], (Surface, Spike, Door, Stone)):
				obj.map[obj.row - 1][obj.elm].walk(choice[0], obj)
		
		elif choice[0] == 'right':
			if isinstance(obj.map[obj.row][obj.elm + 1], (Surface, Spike, Door, Stone)):
				obj.map[obj.row][obj.elm + 1].walk(choice[0], obj)
		
		elif choice[0] == 'down':
			if isinstance(obj.map[obj.row + 1][obj.elm], (Surface, Spike, Door, Stone)):
				obj.map[obj.row + 1][obj.elm].walk(choice[0], obj)
		
		elif choice[0] == 'left':
			if isinstance(obj.map[obj.row][obj.elm - 1], (Surface, Spike, Door, Stone)):
				obj.map[obj.row][obj.elm - 1].walk(choice[0], obj)

	elif choice[0] == 'act' or choice[0] == 'hit':
		if len(choice) > 1:
			if choice[1] == 'w':

				if len(choice) > 2:
					if choice[2] == 'a':
						dir = obj.map[obj.row - 1][obj.elm - 1]
						row = obj.row - 1
						elm = obj.elm - 1
					elif choice[2] == 'd':
						dir = obj.map[obj.row - 1][obj.elm + 1]
						row = obj.row - 1
						elm = obj.elm + 1
				else:
					dir = obj.map[obj.row - 1][obj.elm]
					row = obj.row - 1
					elm = obj.elm

			elif choice[1] == 'd':

				if len(choice) > 2:

					if choice[2] == 'w':
						dir = obj.map[obj.row - 1][obj.elm + 1]
						row = obj.row - 1
						elm = obj.elm + 1
					elif choice[2] == 's':
						dir = obj.map[obj.row + 1][obj.elm + 1]
						row = obj.row + 1
						elm = obj.elm + 1
				else:
					dir = obj.map[obj.row][obj.elm + 1]
					row = obj.row
					elm = obj.elm + 1

			elif choice[1] == 's':
				if len(choice) > 2:

					if choice[2] == 'd':
						dir = obj.map[obj.row + 1][obj.elm + 1]
						row = obj.row + 1
						elm = obj.elm + 1
					elif choice[2] == 'a':
						dir = obj.map[obj.row + 1][obj.elm - 1]
						row = obj.row + 1
						elm = obj.elm - 1
				else:
					dir = obj.map[obj.row + 1][obj.elm]
					row = obj.row + 1
					elm = obj.elm

			elif choice[1] == 'a':
				if len(choice) > 2:
					if choice[2] == 's':
						dir = obj.map[obj.row + 1][obj.elm - 1]
						row = obj.row + 1
						elm = obj.elm - 1
					elif choice[2] == 'w':
						dir = obj.map[obj.row - 1][obj.elm - 1]
						row = obj.row - 1
						elm = obj.elm - 1
				else:
					dir = obj.map[obj.row][obj.elm - 1]
					row = obj.row
					elm = obj.elm - 1

			if choice[0] == 'act':
				if type(dir) is Chest or type(dir) is Table or type(dir) is Source or type(dir) is Portal or type(dir) is DieChest or type(dir) is Door or type(dir) is Wall or type(dir) is Spike:
					dir.act(obj)
	
			elif choice[0] == 'hit':
				if obj.selected:
					if obj.selected.type != 'Stick':
						if type(dir) is Simulator or type(obj) is Goblin or type(obj) is Cravler:
							obj.give_hit(dir)
					else:
						obj.selected.hit(row, elm)
	
		elif choice[0] == 'act':
			obj.open_inventory()