from time import sleep
from json import load
from pynput.keyboard import Key

from module_Area import Area
from module_Avatar import Avatar

from Methods.module_effect import effect
from Methods.module_distributor import distributor

from module_links import game, esc, ses_avatars, ses_area, enemys, res, get_script_dir
import module_links

from Methods.module_smart_input import smart_input

import Items.Drugs.module_SmallHealthDrug
import Items.Drugs.module_MediumHealthDrug
import Items.Swords.module_RustyBlade
import Items.Swords.module_BrokenSword
import Items.Swords.module_Sword
import Items.Swords.module_FireySword
import Items.Swords.module_SwordRecovery1
import Items.Sticks.module_StickCreateGoldOre
import Items.Sticks.module_StickCreateStone
import Items.Wings.module_Wings

# Problems: type

# Plan:  Skills
#		 Stak
#		 Generation
#		 Portal
#		 Choice(Enemy)

Dungeon_1 = Area('Dungeon 1', 100, 100, stones=30, spikes=0, chasms=0, enemys=0)

def turn(avatar):

	if avatar.choice:

		choice = avatar.choice

		effect()
		
		if choice == 'esc': module_links.esc = True

		elif choice == 'skills': avatar.skill_tree()

		elif choice == 'inv': avatar.open_inventory()

		elif module_links.res == False:

			if choice in ['up', 'left', 'down', 'right']: distributor(avatar, choice, 'mov')

			elif len(choice) == 1:
				if choice == 'hit':
					distributor(avatar, 'hit')

			elif choice == 'act' or choice == 'hit':
				if choice == 'act':
					distributor(avatar, smart_input([

									(Key.up, 'up'),
									(Key.right, 'right'),
									(Key.down, 'down'),
									(Key.left, 'left')

									]), 'act')
				elif choice == 'hit':
					distributor(avatar, smart_input([

									(Key.up, 'up'),
									(Key.right, 'right'),
									(Key.down, 'down'),
									(Key.left, 'left')

									]), 'hit')

			avatar.check()
		else:
			module_links.res = False

		avatar.check()


def global_turn(id_):

	for avatar in ses_avatars.values():
		avatar.recovery()
		avatar.check()

	avatar = ses_avatars[str(id_)]

	avatar.choice = load(open(get_script_dir() + '\\uuid\\' + str(id_) + '.json', 'r'))

	for avatar in ses_avatars.values():
		turn(avatar)

	for enemy in enemys:
		enemy.act()
		enemy.check()

def create_player(id_, room=True):
	
	created_player = Avatar(id_, room=room)
	
	from Items.Drugs.module_SmallHealthDrug import SmallHealthDrug
	from Items.Swords.module_Sword import Sword
	from Items.Sticks.module_StickCreateStone import StickCreateStone
	from Items.Sticks.module_StickCreateGoldOre import StickCreateGoldOre
	created_player.add_to_inventory([Sword(), SmallHealthDrug(), StickCreateStone(), StickCreateGoldOre()])
	
	return created_player