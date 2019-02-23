from Items.Drugs.module_metaDrug import metaDrug

class SmallHealthDrug(metaDrug):

	cost = 150
	name = 'Small health drug'

	def __init__(self):
		super().__init__('Small health Drug', 5, 3, 'drug hlt up', 'common', 'slightly restores health', SmallHealthDrug)

SmallHealthDrug()