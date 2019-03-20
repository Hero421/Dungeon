from pynput.keyboard import Key

from Methods.smart_input import smart_input
from Methods.distributor import distributor
from Methods.effect import effect
import links

def turn(avatar):

	if avatar.choice:

		choice = avatar.choice

		effect()
		
		if choice == 'esc': links.esc = True

		elif choice == 'skills': avatar.skill_tree()

		elif choice == 'inv': avatar.open_inventory()

		elif links.res == False:

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
			links.res = False

		avatar.check()