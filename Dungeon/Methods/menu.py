from Methods.choice_of import choice_of

choices1 = ['Resume', 'Settings', 'Quit']

def menu():

	idx = 0

	choice = choice_of(choices1)['item']

	if choice == 'Settings':
		