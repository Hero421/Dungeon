from random import choice
from module_links import ways
from Methods.module_moving import moving

def random_moving(obj, *dirs):

	if 'all' in dirs:
		random_dir = choice(ways)
	else:
		random_dir = choice(dirs)
	moving(obj, random_dir)