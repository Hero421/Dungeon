from Items.Swords.metaSword import Sword

class RustyBlade(Sword):

	name = 'Rusty Blade'

	def __init__(self):
		super().__init__('Rusty Blade', 'You have a tetanus shot, right?', 2, 'common', 0, None, RustyBlade)

RustyBlade()