from random import randint

def rarity_of(item):

	random_num = randint(1, 100)

	if random_num in range(25, 100):
		item.rarity = 'common'
	elif random_num in range(8, 25):
		item.rarity = 'rare'
	elif random_num in range(2, 8):
		item.rarity = 'Epic'
	elif random_num in range(0, 2):
		item.rarity = 'GODLY'