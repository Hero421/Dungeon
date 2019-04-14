from random import seed
from uuid import uuid4
from json import dump
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from Methods.smart_input import smart_input
from Methods.create_player import create_player
from Methods.global_turn import global_turn
from Methods.get_script_dir import get_script_dir
from Blocks.Air import Air
import links
from links import clear, esc, game
import Dungeon

ID = uuid4()

player = create_player(str(ID))

print(player.area.name)

var = False
fall_var2 = False

while True:

	if esc:

		clear()

		print('exit?')

		choices = {Key.enter: True, Key.esc: False}
		choice  = smart_input(choices)

		if choice: break

		links.esc = False
	
	if var:
		print(player.area.name)
		sleep(1)
		var = False

	clear()

	player.stat()
	print(player.lay, player.row, player.elm)
	print()
	player.area.print_map(str(ID), radius=8)

	dump(
		smart_input({

			Key.up:     'North',
			Key.right:  'East',
			Key.down:   'South',
			Key.left:   'West',
			Key.esc:    'esc',
			Key.enter:  '',
			Key.space:  'up',
			Key.ctrl_l: 'down',
			'e': 'act',
			'h': 'hit',
			'i': 'inv',
			'k': 'skills',
			'b': 'raze',
			'l': 'locate'

			}),

		open(get_script_dir() + '\\uuid\\' + str(ID) + '.json', 'w')
	)

	global_turn(ID)

	player.fall()

	from links import esc

clear()
if game:
	print(game)