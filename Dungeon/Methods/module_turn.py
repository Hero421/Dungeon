from pynput.keyboard import Key

from Methods.module_smart_input import smart_input
from Methods.module_distributor import distributor
from Methods.module_effect import effect
import module_links

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