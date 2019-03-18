from os import system

intoxicated = {}

raritys = ['common', 'rare', 'Epic', 'GODLY']

types_of_items = [
	'Helmet' ,
	'Torso'  ,
	'Leggings',
	'Shoes'  ,
	'Sword'  ,
	'Drug'   ,
	'Wings'  ,
	'Stick'  ,
	'Ring'   ,
	'Resource'
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

levels = [[], []]
enemys = []

esc = False

clear = lambda: system('cls')

game = None

ses_avatars = {}

ses_area = None

res = False