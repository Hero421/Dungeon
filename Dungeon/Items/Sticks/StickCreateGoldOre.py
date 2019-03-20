from Items.Sticks.metaStickCreate import StickCreate
from Blocks.Containers import GoldOreBlock

class StickCreateGoldOre(StickCreate):
	"""docstring for StickCreateGold"""
	name = 'stick create gold ore'

	def __init__(self):
		super().__init__('stick create gold ore', 'creates a gold ore', 'GODLY', GoldOreBlock, StickCreateGoldOre)

StickCreateGoldOre()