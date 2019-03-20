from pynput import keyboard
from pynput.keyboard import Key
from os import system

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

	for pair in pairs:
		if type(pair[0]) is str:
			if len(pair[0]) == 1:
				wait.append(keyboard.KeyCode(char=pair[0]))
		else:
			wait.append(pair[0])
		return_.append(pair[1])

	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()

	return input_

wait = []
return_ = []
input_ = None