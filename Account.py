from uuid import uuid4
from json import dump

from Dungeon import create_player, global_turn

id = uuid4()

player = create_player(str(id))

while True:
	
	player.stat()
	player.area.print_map(str(id))
	
	dump(list(input()), open(Dungeon.__file__() + '/uuid/' + str(id)+'.json', 'w'))
	
	global_turn(str(id))