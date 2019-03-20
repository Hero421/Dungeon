from Items.Swords.metaSword import Sword

class BrokenSword(Sword):

	name = 'Broken sword'

	def __init__(self):
		super().__init__('Broken sword', 'Broken sword Size isn\'t important!', 2, 'common', 0, 'break', BrokenSword)

BrokenSword()