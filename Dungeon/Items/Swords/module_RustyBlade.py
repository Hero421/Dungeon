from Items.Swords.module_metaSword import metaSword

class RustyBlade(metaSword):

	name = 'Rusty Blade'

	def __init__(self):
		super().__init__('Rusty Blade', 'You have a tetanus shot, right?', 2, 'common', 0, None, RustyBlade)

RustyBlade()