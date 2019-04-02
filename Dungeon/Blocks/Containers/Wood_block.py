from Blocks.Containers.metaContainer import Container

from Items.Resources.Wood import Wood

class WoodBlock(Container):

	des = '/'

	def give(self, obj):

		obj.add_to_inventory([Wood() for _ in range(1, 5)])