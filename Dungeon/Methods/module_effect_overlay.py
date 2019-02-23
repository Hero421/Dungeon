def effect_overlay(obj, num, degree, act):
	
	from module_links import intoxicated

	intoxicated[obj] = {'degree': None, 'num': None, 'type': None}   #  [when/how many moves, how much num, how]

	if degree == 'WTS':                     #  WTS - while this selecting
		intoxicated[obj]['degree'] = degree
	else:
		intoxicated[obj]['degree'] = int(degree)

	intoxicated[obj]['num'] = num
	intoxicated[obj]['type'] = act