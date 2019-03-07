from uuid import uuid4
from json import dump
from time import sleep

from Dungeon import create_player, global_turn

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
	
	dump(list(input()), open(path + uuid + str(id) + '.json', 'w'))
	
	global_turn(id)
	
	from module_links import esc