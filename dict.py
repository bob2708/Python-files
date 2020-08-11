class MyList:
	"""docstring for Dict"""
	def __init__(self, orig_list):
		self.container = [] or orig_list

	def __getitem__(self, key):
		return self.container[key-1]

	def __setitem__(self, key, value):
		self.container[key] = value
		return "Success" 

	def __len__(self):
		return len(self.container)
