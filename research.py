import functools
import json

class Research:
	"""docstring for Research"""
	def __init__(self, file="logs.txt"):
		self.file = file

	def __getattr__(self, atr):
		return f"{atr} not found"

	def __getattribute__(self, atr):
		print(f"Looking for {atr}...")
		return super().__getattribute__(atr)
		# return object.__getattribute__(self, atr)
	
	def __call__(self, func):
		@functools.wraps(func)
		def logger(*args, **kwargs):
			result = func(*args, **kwargs)
			# with open(args[0].file, 'a') as f:
			with open(self.file, 'a') as f:
				json.dump(result, f)
				f.write('\n')
		return logger

logger = Research()

@logger
def add_attribute(cls, attr):
	cls.new_attr = attr
	return cls.__dict__

