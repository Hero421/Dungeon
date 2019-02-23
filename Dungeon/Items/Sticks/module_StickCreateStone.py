from Items.Sticks.module_metaStickCreate import metaStickCreate
from Blocks.module_Stone import Stone

class StickCreateStone(metaStickCreate):
	"""docstring for StickCreateStone"""
	name = 'stick create stone'

	def __init__(self):
		super().__init__('stick create stone', 'creates a stone', 'common', Stone, StickCreateStone)

StickCreateStone()