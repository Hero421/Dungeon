from uuid import uuid4
from json import dump
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from Methods.module_smart_input import smart_input

from Dungeon import create_player, global_turn

import module_links

id = uuid4()

player = create_player(id)

from module_links import uuid, path, clear, esc

var = True

while not esc:
	
	if var:
		print(player.area.name)
		sleep(1)
		var = False

	clear()
	
	#player.stat()
	player.area.print_map(id)

	# try:
	dump(
		smart_input([

			(Key.up, 'up'), 
			(Key.right, 'right'), 
			(Key.down, 'down'), 
			(Key.left, 'left'), 
			(Key.esc, 'esc'), 
			(keyboard.KeyCode(char='e'), 'act'),
			(keyboard.KeyCode(char='i'), 'inv'),
			(keyboard.KeyCode(char='k'), 'skills')

			]), 

		open(path + uuid + str(id) + '.json', 'w')
	)
	
	global_turn(id)
	# except TypeError:
	# 	print('Oups!')
	
	from module_links import esc

clear()