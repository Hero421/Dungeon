from Items.Resources.metaResource import Resource
from Items.Resources.Iron_bar import IronBar

class IronOre(Resource):

	def __init__(self):
		self.type_ = 'Resource'
		super().__init__('Iron ore', 'You can melt a iron bar', 'common', IronOre)
	
	def remelting(self, oven, obj, index):

		obj.backpack[index].remove(self)

		for slot in oven.slots:
			if len(slot) == 0:
				slot.append(IronBar())
				break
			elif type(slot[0]) is IronBar:
				slot.append(IronBar())
				break
