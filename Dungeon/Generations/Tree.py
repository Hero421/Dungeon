from random import randint

from Blocks.Containers.Wood_block import WoodBlock

class Tree(object):

	def spawn(self, lay, row, elm, map_):

		height = randint(3, 5)

		for count_lay in range(height):
			map_[lay+count_lay][row][elm] = WoodBlock()

		for count_lay in range(height-1, height+1):
			for count_row in range(row-1, row+1):
				for count_elm in range(elm-1, elm+1):
					if not type(map_[lay+count_lay][row+count_row][elm+count_elm]) is Wood:
						map_[lay+count_lay][row+count_row][elm+count_elm] = FoliageBlock()
		

