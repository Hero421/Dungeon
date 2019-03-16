from uuid import uuid4
from json import dump
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from Methods.module_smart_input import smart_input
from Dungeon import create_player, global_turn
import module_links
from module_links import clear, esc, get_script_dir

id_ = uuid4()

player = create_player(str(id_))

print(player.area.name)

var = False

while not esc:
	
	if var:
		print(player.area.name)
		sleep(1)
		var = False

	clear()
	
	player.stat()
	player.area.print_map(str(id_), radius=8)

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

		open(get_script_dir() + '\\uuid\\' + str(id_) + '.json', 'w')
	)

	global_turn(id_)

	# except TypeError:
	# 	print('Oups!')
	
	from module_links import esc


clear()
if game:
	print(game)