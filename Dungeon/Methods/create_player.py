from Avatar import Avatar

from Blocks.Trigers.Workbench import Workbench
from Items.Resources.Board import Board

def create_player(ID, room=True):
	
	created_player = Avatar(ID, room=room)

	items = [Workbench, Board]

	for item in items:
		created_player.recepts.append(item().recept)

	return created_player