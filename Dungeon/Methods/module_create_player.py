from module_Avatar import Avatar

from Items.Drugs.module_SmallHealthDrug import SmallHealthDrug
from Items.Swords.module_Sword import Sword
from Items.Sticks.module_StickCreateStone import StickCreateStone
from Items.Sticks.module_StickCreateGoldOre import StickCreateGoldOre
from Items.Resources.module_Gold_Ore import GoldOre

def create_player(id_, room=True):
	
	created_player = Avatar(id_, room=room)

	created_player.add_to_inventory(Sword(), SmallHealthDrug(), StickCreateStone(), StickCreateGoldOre())
	
	return created_player