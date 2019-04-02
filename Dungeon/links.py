from os import system

intoxicated = dict()

RARITYS = ['common', 'rare', 'Epic', 'GODLY']

TYPES_OF_ITEMS = [
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
	
	RARITY: {
	
		TYPE: list()
		for TYPE in TYPES_OF_ITEMS
	}
	
	for RARITY in RARITYS
}

WAYS = [
	'North', 
	'South', 
	'East' , 
	'West'
]

levels = list()
enemys = list()

esc = False

clear = lambda: system('cls')

game = None

ses_avatars = dict()

ses_area = None

res = False