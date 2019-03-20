from Items.Resources.metaResource import Resource
from Items.Resources.Gold_Bar import GoldBar

class GoldOre(Resource):

	def __init__(self):
		super().__init__('Gold ore', 'You can melt a gold bar', 'common', GoldOre)
	
	def remelting(self, oven, obj, index):

		obj.backpack[index].remove(self)

		for slot in oven.slots:
			if len(slot) == 0:
				slot.append(GoldBar())
				break
			elif type(slot[0]) is GoldBar:
				slot.append(GoldBar())
				break
