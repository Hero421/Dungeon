from Items.Wings.module_metaWings import metaWings

class TheWingsOfTheLordOfTheStorm(metaWings):
	'''
	docstring for TheWingsOfTheLordOfTheStorm
	'''

	name = 'The wings of the Lord of the storm'
	rarity = 'common'

	def __init__(self):
		super().__init__(TheWingsOfTheLordOfTheStorm)

TheWingsOfTheLordOfTheStorm()