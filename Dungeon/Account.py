from uuid import uuid4
from json import dump
from platform import system

import Dungeon

from Dungeon import create_player, global_turn

id = uuid4()

player = create_player(str(id))

from module_links import uuid, path, clear

while True:

	clear()
	
	player.stat()
	player.area.print_map(str(id))
	
	dump(list(input()), open(path + uuid + str(id) + '.json', 'w'))
	
	global_turn(str(id))