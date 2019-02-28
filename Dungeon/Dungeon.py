from time import sleep
from json import dump, load

from module_Area import Area
from module_Avatar import Avatar

from Methods.module_effect import effect
from Methods.module_moving import moving

from module_links import game, esc, ses_avatars, ses_area, clear, enemys, res, dirs_dict, path, uuid
import module_links

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
#		Stak
#		Rooms
#		Generation
#		Portal
#		Chasms
#		Choice(Enemy)

Dungeon_1 = Area('Dungeon 1', 150, 150)
Dungeon_2 = Area('Dungeon 2', 150, 150)

def turn(avatar):

	if avatar.choices:
		chk = ''

		for ltr in avatar.choices:
			chk += ltr

		if chk != 'skills' and chk != 'esc':
			for choice in avatar.choices:

				effect()

				if module_links.res == False:
					if choice in ['w', 'a', 's', 'd']:
						moving(avatar, dirs_dict[choice])

					elif len(avatar.choices) == 1:
						if choice == 'e':
							moving(avatar, 'act')
						elif choice == 'h':
							moving(avatar, 'hit')

					elif choice == 'e' or choice == 'h':
						if len(avatar.choices) > avatar.choices.index(choice) + 3:
							if avatar.choices[avatar.choices.index(choice) + 2] == ',':
								avatar.choices.remove(avatar.choices[avatar.choices.index(choice) + 2])
								if avatar.choices[avatar.choices.index(choice) + 1] in ['w', 'a', 's', 'd'] and avatar.choices[avatar.choices.index(choice) + 2] in ['w', 'a', 's', 'd']:
									if choice == 'e':
										moving(avatar, 'act', avatar.choices[avatar.choices.index(choice) + 1], avatar.choices[avatar.choices.index(choice) + 2])
									elif choice == 'h':
										moving(avatar, 'hit', avatar.choices[avatar.choices.index(choice) + 1], avatar.choices[avatar.choices.index(choice) + 2])
									avatar.choices.remove(avatar.choices[avatar.choices.index(choice) + 2])
									avatar.choices.remove(avatar.choices[avatar.choices.index(choice) + 1])
						elif len(avatar.choices) > avatar.choices.index(choice) + 1:
							if avatar.choices[avatar.choices.index(choice) + 1] in ['w', 'a', 's', 'd']:
								if choice == 'e':
									moving(avatar, 'act', avatar.choices[avatar.choices.index(choice) + 1])
								elif choice == 'h':
									moving(avatar, 'hit', avatar.choices[avatar.choices.index(choice) + 1])
								avatar.choices.remove(avatar.choices[avatar.choices.index(choice) + 1])

					avatar.check()
				else:
					res = False
		
		elif chk == 'skills':
			avatar.skill_tree()

		elif chk == 'esc':
			module_links.esc == True

		avatar.check()


def global_turn(id):

	for avatar in ses_avatars.values():
		avatar.recovery()
		avatar.check()

	ses_avatars[id].choices = load(open(path + uuid + str(id) + '.json', 'r'))

	for avatar in ses_avatars.values():
		turn(avatar)

	for enemy in enemys:
		enemy.act()
		enemy.check()

def create_player(id):
	
	created_player = Avatar(id)
	
	from Items.Drugs.module_SmallHealthDrug import SmallHealthDrug
	from Items.Swords.module_Sword import Sword
	from Items.Sticks.module_StickCreateStone import StickCreateStone
	from Items.Sticks.module_StickCreateGoldOre import StickCreateGoldOre
	created_player.add_to_inventory([Sword(), SmallHealthDrug(), StickCreateStone(), StickCreateGoldOre()])
	
	return created_player

clear()
if game:
	print(game)