from uuid import uuid4
from json import dump
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from Methods.smart_input import smart_input
from Methods.create_player import create_player
from Methods.global_turn import global_turn
from Methods.get_script_dir import get_script_dir
import links
from links import clear, esc, game
import Dungeon

id_ = uuid4()

player = create_player(str(id_))

print(player.area.name)

var = False

while True:

	if esc:

		clear()

		print('exit?')

		choices = [(Key.enter, 'yes'), (Key.esc, 'no')]
		choice  = smart_input(choices)

		if choice == 'yes': break

		links.esc = False
	
	if var:
		print(player.area.name)
		sleep(1)
		var = False

	clear()
	
	player.stat()
	player.area.print_map(str(id_), radius=8)

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
	
	from links import esc


clear()
if game:
	print(game)