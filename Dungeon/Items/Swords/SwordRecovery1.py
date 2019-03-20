from Items.Swords.metaSword import Sword

class SwordRecovery1(Sword):

	name = 'Sword recovery 1'

	def __init__(self):
		super().__init__('Sword recovery 1', 'For each enemy killed restores 5 HP', 2,  'common', 0, 'recovery', SwordRecovery1)

SwordRecovery1()