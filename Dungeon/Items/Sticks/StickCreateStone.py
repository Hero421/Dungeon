from Items.Sticks.metaStickCreate import StickCreate
from Blocks.Containers.Stone_block import StoneBlock

class StickCreateStone(StickCreate):
	"""docstring for StickCreateStone"""
	name = 'stick create stone'

	def __init__(self):
		super().__init__('stick create stone', 'Epic', 'common', StoneBlock, StickCreateStone)

StickCreateStone()