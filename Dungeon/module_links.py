import Dungeon

path_= list(Dungeon.__file__)

for count in range(11):
	del path_[-1]

path = ''

for ltr in path_:
	path += ltr

intoxicated = {}

raritys = ['common', 'rare', 'Epic', 'GODLY']

types_of_items = [
	'Helmet',
	'Torso' ,
	'Leggings',
	'Shoes' ,
	'Sword' ,
	'Drug'  ,
	'Wings' ,
	'Stick' ,
	'Ring'
]

items = {
	
	rarity: {
	
		type_of_item: []
		for type_of_item in types_of_items
	}
	
	for rarity in raritys
}

ways = [
	'up', 
	'right', 
	'down' , 
	'left'
]

used_items = []
levels = [[], []]
enemys = []

dirs_dict = {

	'w': 'up', 
	'd': 'right', 
	's': 'down', 
	'a': 'left'

}

hp = 3
game_count = 0

inv_bool = None
skl_bool = None

esc = False

chk = ''

game = None

location = {'row': None, 
			'elm': None}

ses_avatars = {}

ses_area = None

from os import system as os_sys
from platform import system as platform_sys

if platform_sys() == 'Windows':
	input(platform_sys())
	clear = lambda: os_sys('cls')
	uuid = '\\uuid\\'
elif platform_sys() == 'Linux':
	clear = lambda: os_sys('clear')
	uuid = '/uuid/'

res = False