from json import load

from module_links import ses_avatars, enemys
from Methods.module_get_script_dir import get_script_dir
from Methods.module_turn import turn

def global_turn(id_):

	for avatar in ses_avatars.values():
		avatar.recovery()
		avatar.check()

	avatar = ses_avatars[str(id_)]

	avatar.choice = load(open(get_script_dir() + '\\uuid\\' + str(id_) + '.json', 'r'))

	for avatar in ses_avatars.values():
		turn(avatar)

	for enemy in enemys:
		enemy.act()
		enemy.check()