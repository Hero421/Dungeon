from random import choice
from module_links import ways
from Methods.module_distributor import distributor

def random_moving(obj, *dirs):

	if 'all' in dirs:
		random_dir = choice(ways)
	else:
		random_dir = choice(dirs)
	distributor(obj, random_dir, 'mov')