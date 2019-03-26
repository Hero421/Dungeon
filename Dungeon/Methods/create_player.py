from Avatar import Avatar

def create_player(id_, room=True):
	
	created_player = Avatar(id_, room=room)

	return created_player