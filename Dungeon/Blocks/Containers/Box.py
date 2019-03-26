from termcolor import colored
from random import randint
from time import sleep

from Blocks.Containers.metaContainer import Container
from Items.Resources.Broken_board import BrokenBoard
from Items.Resources.Board import Board

class Box(Container):

	des = colored(':', 'yellow')

	def give(self, obj):
		items = []
		sleep_num = 0
		if randint(1, 100) in range(20):
			num_boards = randint(1, 5)
			items.append([Board() for _ in range(num_boards)])
			boards = f'{num_boards} boards, '
			sleep_num += 0.3
		else:
			boards = ''

		if randint(1, 100) in range(40):
			num_gold = randint(1, 15)
			obj.gold += num_gold
			gold = f'{num_gold} gold, '
			sleep_num += 0.3
		else:
			gold = ''

		num_exp = randint(1, 10)
		obj.Exp += num_exp
		exp = f'{num_exp} exp, '

		num_broken_boards = randint(2, 8)
		items.append([BrokenBoard() for _ in range(num_broken_boards)])
		broken_boards = f'{num_broken_boards} broken boards'

		obj.add_to_inventory(*items)

		print(f'You got: {exp}{gold}{boards}{broken_boards}')

		sleep(0.5 + sleep_num)