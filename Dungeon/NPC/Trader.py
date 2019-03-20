class Trader(GameObject):
	
	stat = False
	des = '$'

	items = []
	
	def __init__(self):

		super().__init__()
		
	def act(self, obj):
		print('Здравствуй, одинокий путник! С чем ты ко мне пожаловал?')
		print('1. Что у тебя есть на продажу?')
		print('2. Есть ли для меня задание?')
		print('3. У меня тут много барахла, интересует?')

		choice = input()

		if self.stat == False:
			pass

		if choice == '1':
			count = 1
			for slot in self.items:
				if len(self.items) < 10:
					if len(str(self.items.index(slot))) == 1:
						print(str(count) + '.', slot, 'cost:', slot.cost)
						count += 1
				elif len(self.items) < 100:
					if len(str(self.items.index(slot))) == 1:
						print(str(count) + '. ', slot, 'cost:', slot.cost)
					if len(str(self.items.index(slot))) == 2:
						print(str(count) + '.', slot, 'cost:', slot.cost)

		sec_choice = input()

		obj.gold -= self.items[int(sec_choice)-1].cost
		obj.add_to_inventory([self.items[int(sec_choice)-1]])
		self.items[int(sec_choice)]
	 