from module_links import intoxicated, ses_avatars

class Source(object):
	
	des = '£'
	
	def __init__(self):

		super().__init__()
		
	def act(self, obj):
		if obj in ses_avatars:
			if obj.count['Source'][0] == 40:
				obj.hlt = obj.full_hlt
				obj.count['Source'][0] = 0
				obj.mana = obj.full_mana
				
				if obj in intoxicated:
					del intoxicated[obj][1]
					del intoxicated[obj][0]
					del intoxicated[obj]