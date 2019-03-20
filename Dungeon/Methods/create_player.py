from Avatar import Avatar

from Items.Drugs.SmallHealthDrug import SmallHealthDrug
from Items.Swords.Sword import Sword_
from Items.Resources.Iron_Bar import IronBar
from Items.Resources.Board import Board

def create_player(id_, room=True):
	
	created_player = Avatar(id_, room=room)

	created_player.add_to_inventory(Sword_(), SmallHealthDrug(), [IronBar() for _ in range(5)], [Board() for _ in range(5)])
	
	return created_player