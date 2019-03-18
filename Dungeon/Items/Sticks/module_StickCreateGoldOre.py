from Items.Sticks.module_metaStickCreate import metaStickCreate
from Blocks.module_Containers import GoldOreBlock

class StickCreateGoldOre(metaStickCreate):
	"""docstring for StickCreateGold"""
	name = 'stick create gold ore'

	def __init__(self):
		super().__init__('stick create gold ore', 'creates a gold ore', 'common', GoldOreBlock, StickCreateGoldOre)

StickCreateGoldOre()