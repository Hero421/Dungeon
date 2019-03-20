from Items.Sticks.metaStickCreate import StickCreate
from Blocks.Stone import Stone

class StickCreateStone(StickCreate):
	"""docstring for StickCreateStone"""
	name = 'stick create stone'

	def __init__(self):
		super().__init__('stick create stone', 'Epic', 'common', Stone, StickCreateStone)

StickCreateStone()