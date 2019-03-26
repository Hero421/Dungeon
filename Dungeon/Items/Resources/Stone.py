from Items.Resources.metaResource import Resource
from Items.Resources.Raw_stone import RawStone

from Blocks.Trigers.Workbench import Workbench

class Stone(Resource):

	def __init__(self):

		self.type_= 'Resource'
		self.recept = {RawStone: 6, 'result': Stone, 'num': 1, 'pace': Workbench}
		
		super().__init__('Stone', 'Something', 'common', Stone)