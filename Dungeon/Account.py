from uuid import uuid4
from json import dump

import Dungeon

from Dungeon import create_player, global_turn

id = uuid4()

player = create_player(str(id))

from module_links import uuid, path, clear, esc

while not esc:

	clear()
	
	player.stat()
	print(player.location, '\n')
	player.area.print_map(str(id))
	
	dump(list(input()), open(path + uuid + str(id) + '.json', 'w'))
	
	global_turn(str(id))
	
	from module_links import esc