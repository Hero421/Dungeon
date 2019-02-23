from Items.Swords.module_metaSword import metaSword

class BrokenSword(metaSword):

	name = 'Broken sword'

	def __init__(self):
		super().__init__('Broken sword', 'Broken sword Size isn\'t important!', 2, 'common', 0, 'break', BrokenSword)

BrokenSword()