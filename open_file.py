class open_file:
	'''context manager exercise'''
	def __init__(self, filename, mode):
		self.f = open(filename, mode)

	def __enter__(self):
		return self.f	

	def __exit__(self, *args):
		print(args)
		self.f.close()
		return True

with open_file(".txt", 'w'):
	r.write("text")