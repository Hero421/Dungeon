from os import system as sys
from time import sleep
from random import randint, choice
from pynput.keyboard import Key

from Methods.smart_input import smart_input

from links import clear

def gen_strings(items, index, items2=False, obj=None, inv=False, slot=None, coast=False):

	length = 0
	strings= list()

	if items2:
		items2 = gen_strings(items2, index-len(items))

	for item in items:

		if type(item) is list:new_length = 2 + 2 + len(item[0].name) + 2 + len(str(len(item)))
		elif item:            new_length = len(item.name)
		else:                 new_length = 2 + 2 + 5

		if new_length > length: length = new_length

	if inv:

		if obj.select:
			mark = ' <' if slot == 'select' else str()
			name = obj.select.name
			strings.append(f'{name}{mark}')

		for key in ['head', 'torso', 'wings', 'feet', 'shoes', 'rings']:
			item = getattr(obj, key)
			mark = ' <'       if slot == key  else str()
			name = item.name  if item          else '_____'
			dub_point = ':  ' if len(key) == 4 else ': '
			strings.append(f'{key}{dub_point}{name}{mark}')

		strings.append('')

	count = 0
	for item in items:
		mark = ' <' if count == index else str()
		add  = str()
		num  = str()
		if len(items) > 9:
			point = '.   ' if len(str(count+1)) == 1 else '.  '
		else: point = '.  '
		if not item: item = '_____'
		elif type(item) is list:
			if len(item) > 1: num = f' x{len(item)}'
			item  = f'{item[0].name}{num}'
		else:item = item.name
		if items2:
			if len(items2) > count:
				add = items2[count]
		residue = ' ' * (length - len(item) - len(mark))
		strings.append(f'{item}{mark}{residue}{add}')
		count += 1

	return strings

def choice_of(items, items2=False, idx=0, slot=None, obj=None, inv=False, coast=False):

	if inv:
		clothes = ['rings', 'shoes', 'feet', 'wings', 'torso', 'head']
		if obj.select:
			clothes.append('select')

	while True:

		clear()

		for string in gen_strings(items, idx, items2=items2, obj=obj, inv=inv, slot=slot, coast=coast):
			print(string)

		choices = {Key.up: 'up', Key.down: 'down', Key.left: 'left', Key.right: 'right', Key.shift_r: 'details', Key.enter: 'select', Key.esc: 'esc'}	
		choice = smart_input(choices)

		if choice == 'esc': return None,None,None, True

		elif choice == 'details':
			tmp = items[idx] if idx < len(items) else items2[idx-len(items)]
			item = tmp[0] if type(tmp) is list else tmp
			print()
			if item:
				item.print_details()
				smart_input({Key.enter: None, Key.esc: None, Key.shift_r: None})
			continue

		if not inv:
			if choice == 'up':
				if idx == 0: idx = len(items)-1
				elif idx == len(items): idx = len(items) + len(items2)-1
				else: idx -= 1

			elif choice == 'down':
				if idx == len(items)-1: idx = 0
				elif items2:
					if idx == len(items) + len(items2)-1: idx = len(items)
					else: idx += 1
				else: idx += 1

			elif choice == 'left' and items2:
				if not idx - len(items) < 0: idx -= len(items)

			elif choice == 'right' and items2:
				if idx > len(items2): idx = len(items) + len(items2)-1
				elif idx < len(items):idx += len(items)

			elif choice == 'select':
				if idx < len(items):
					item= items[idx]
					lst = 'fst'
				else:
					idx-= len(items)
					item= items2[idx]
					lst = 'sec'
				return item, idx, lst, False

		else:
			if choice == 'up':
				if (    obj.select and slot == 'select') or \
				   (not obj.select and slot == 'head'):
					idx  = len(items)-1
					slot = None
				elif idx < 1:
					idx -= 1
					slot = clothes[abs(idx)-1]
				else:
					idx -= 1
					solt = None

			elif choice == 'down':
				if idx < -1:
					idx += 1
					slot = clothes[abs(idx)-1]
				elif idx == len(items)-1:
					idx  = -len(clothes)+1
					slot = clothes[abs(idx)]
				else:
					idx += 1
					slot = None

			elif choice == 'select':
				if idx > 0:
					item = items[idx]
					return item, idx, slot, False