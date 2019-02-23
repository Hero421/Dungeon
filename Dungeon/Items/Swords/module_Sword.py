from Items.Swords.module_metaSword import metaSword

class Sword(metaSword):

	name = 'Sword'

	def __init__(self):
		super().__init__('Sword', 'Simply sword, not expected, Yes?', 10, 'common', 5 , None, Sword)

Sword()