from pynput import keyboard
from pynput.keyboard import Key, KeyCode

def on_release(key):
	global input_, wait, return_
	if key in wait:
		input_ = (return_[wait.index(key)])
		return False

def smart_input(pairs):
	
	global input_, wait, return_

	wait = []
	return_ = []
	input_ = None

	for keycode, result in pairs.items():
		if type(keycode) is str:
			try:
				wait.append(getattr(Key, keycode))
			except:
				wait.append(KeyCode(char=keycode))
		else:
			wait.append(keycode)
			
		return_.append(result)

	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()

	return input_

wait = []
return_ = []
input_ = None