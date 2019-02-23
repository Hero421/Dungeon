from module_links import intoxicated

def effect():

	for person in intoxicated:
		if intoxicated[person]['degree'] == 'WTS':
			if intoxicated[person]['type'] == 'set fire':
				person.status.append('set on fire')
				person.hlt -= intoxicated[person]['num']
		elif intoxicated[person]['degree'] > 0:
			if intoxicated[person]['type'] == 'spike hlt down':
				person.hlt -= intoxicated[person]['num']
				person.status.append('intoxicated')
			elif intoxicated[person]['type'] == 'potion hlt up' and person.hlt < person.full_hlt:
				person.status.append('regenerated')
				if person.hlt + intoxicated[person]['num'] < person.full_hlt:
					person.hlt += intoxicated[person]['num']
				else:
					for count in range(intoxicated[person]['num']):
						if person.hlt < person.full_hlt:
							person.hlt += 1

			intoxicated[person]['degree'] -= 1
		else:
			del intoxicated[person]
			if len(intoxicated) == 0:
				break