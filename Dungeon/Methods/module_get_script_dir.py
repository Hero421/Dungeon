from inspect import getabsfile
from os.path import abspath, realpath, dirname
from sys import executable
import sys

def get_script_dir(follow_symlinks=True):
	if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
		path = abspath(executable)
	else:
		path = getabsfile(get_script_dir)
	if follow_symlinks:
		path = realpath(path)
	dir_ = list(dirname(path))
	for _ in range(8):
		del dir_[-1]
	true_dir = ''
	for elm in dir_:
		true_dir += elm
	return true_dir