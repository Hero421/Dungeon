from Items.Swords.module_metaSword import metaSword

class SwordRecovery1(metaSword):

	name = 'Sword recovery 1'

	def __init__(self):
		super().__init__('Sword recovery 1', 'For each enemy killed restores 5 HP', 2,  'common', 0, 'recovery', SwordRecovery1)

SwordRecovery1()