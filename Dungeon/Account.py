from uuid import uuid4
from json import dump

from Dungeon import create_player, global_turn

id = uuid4()

player = create_player(id)

while True:
	
	player.stat()
	player.area.print_map(id)
	
	dump(list(input()), open(str(id)+'.json', 'w'))
	
	global_turn(id)