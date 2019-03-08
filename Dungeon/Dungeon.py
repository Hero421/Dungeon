from time import sleep
from json import load

from module_Area import Area
from module_Avatar import Avatar

from Methods.module_effect import effect
from Methods.module_moving import moving

from module_links import game, esc, ses_avatars, ses_area, clear, enemys, res, path, uuid
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
import Items.Wings.module_TheWingsOfTheLordOfTheStorm
import Items.Wings.module_Wings

# Problems: type

# Plan:  Skills
#		 Stak
#		 Generation
#		 Portal
#		 Choice(Enemy)

Dungeon_1 = Area('Dungeon 1', 48, 48, stones=40, spikes=1.5, chasms=1.4, enemys=0.5)

def turn(avatar):

	if avatar.choice:

		choice = avatar.choice

		effect()
		
		if choice == 'esc':
			module_links.esc = True

		elif choice == 'skills':
			avatar.skill_tree()

		elif choice == 'inv':
			avatar.open_inventory()

		elif module_links.res == False:

			if choice in ['up', 'left', 'down', 'right']:
				moving(avatar, choice)

			elif len(choice) == 1:
				if choice == 'hit':
					moving(avatar, 'hit')

			elif choice == 'act' or choice == 'hit':
				if choice == 'act':
					moving(avatar, 'act', choice[choice.index(choice) + 1])
				elif choice == 'hit':
					moving(avatar, 'hit', choice[choice.index(choice) + 1])
				choice.remove(choice[choice.index(choice) + 1])

			avatar.check()
		else:
			res = False

		avatar.check()


def global_turn(id):

	for avatar in ses_avatars.values():
		avatar.recovery()
		avatar.check()

	ses_avatars[id].choice = load(open(path + uuid + str(id) + '.json', 'r'))

	for avatar in ses_avatars.values():
		turn(avatar)

	for enemy in enemys:
		enemy.act()
		enemy.check()

def create_player(id, room=True):
	
	created_player = Avatar(id, room=room)
	
	from Items.Drugs.module_SmallHealthDrug import SmallHealthDrug
	from Items.Swords.module_Sword import Sword
	from Items.Sticks.module_StickCreateStone import StickCreateStone
	from Items.Sticks.module_StickCreateGoldOre import StickCreateGoldOre
	created_player.add_to_inventory([Sword(), SmallHealthDrug(), StickCreateStone(), StickCreateGoldOre()])
	
	return created_player

clear()
if game:
	print(game)
