from time import sleep
from pynput.keyboard import Key

from Methods.smart_input import smart_input
from Methods.distributor import distributor
from Methods.effect import effect
import links

def turn(avatar):

	if avatar.choice:

		avatar.check()

		choice = avatar.choice

		effect()
		
		if choice == 'esc': links.esc = True

		elif choice == 'skills': avatar.skill_tree()

		elif choice == 'inv': avatar.open_inventory()

		elif links.res == False:

			if choice in ['North', 'East', 'South', 'West', 'up', 'down']: distributor(avatar, choice, 'mov')

			else:
				distributor(avatar, smart_input({

								Key.up: 'North',
								Key.right: 'East',
								Key.down: 'South',
								Key.left: 'West',
								Key.space:'up',
								Key.ctrl_l:'down'

								}), choice)

			avatar.check()
		else:
			links.res = False

		avatar.check()