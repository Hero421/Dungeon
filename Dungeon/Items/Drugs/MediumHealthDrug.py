from Items.Drugs.metaDrug import Drug

class MediumHealthDrug(Drug):

	cost = 300
	name = 'Medium health drug'

	def __init__(self):
		super().__init__('Medium health drug', 15, 4, 'drug hlt up', 'common', 'restores health', MediumHealthDrug)

MediumHealthDrug()