from Avatar import Avatar

def create_player(ID, room=True):
	
	created_player = Avatar(ID, room=room)
	return created_player