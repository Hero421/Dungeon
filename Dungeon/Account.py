from uuid import uuid4
from json import dump
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from Methods.module_smart_input import smart_input

from Dungeon import create_player, global_turn

import module_links

from module_links import uuid, path, clear, esc

id_ = uuid4()

player = create_player(str(id_))

print(player.area.name)

var = False

player.map[0][0] = type('Test', (), {'des': '?'})

while not esc:
	
	if var:
		print(player.area.name)
		sleep(1)
		var = False

	clear()
	
	player.stat()
	print(player.location)
	player.area.print_map(str(id_))

	# try:
	dump(
		smart_input([

			(Key.up, 'up'), 
			(Key.right, 'right'), 
			(Key.down, 'down'), 
			(Key.left, 'left'), 
			(Key.esc, 'esc'), 
			('e', 'act'),
			('h', 'hit'),
			('i', 'inv'),
			('k', 'skills')

			]), 

		open(path + uuid + str(id_) + '.json', 'w')
	)

	global_turn(id_)

	# except TypeError:
	# 	print('Oups!')
	
	from module_links import esc

clear()