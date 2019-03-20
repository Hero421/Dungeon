from Items.Drugs.metaDrug import Drug

class SmallHealthDrug(Drug):

	cost = 150
	name = 'Small health drug'

	def __init__(self):
		super().__init__('Small health Drug', 5, 3, 'drug hlt up', 'common', 'slightly restores health', SmallHealthDrug)

SmallHealthDrug()