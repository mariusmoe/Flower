import os

def run(**args):
	print "*[*] In environments module."
	files = os.listdir(".")

	return str(files)
