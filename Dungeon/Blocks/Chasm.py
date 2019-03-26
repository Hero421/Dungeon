class Chasm(object):

	'''
	If an object has wings, it can fly over it.
	'''

	des = '~'

	def chk_walk(self, obj):

		from links import ses_avatars

		if obj in ses_avatars.values():
			if obj.inventory['wings']:
				return True

		return False