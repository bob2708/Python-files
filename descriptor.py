class Descriptor:

	def __init__(self, filename="filename.txt"):
		self.filename = filename

	def __set__(self, obj, value):
		print
		with open(filename, 'a') as f:
			f.writeline(value)

	# def __get__(self, obj, cls):
	# 	print(obj, third)

	# def __delete__(self, obj):
	# 	print(obj)
		

class Class:

	attr = Descriptor()

	def __init__(self, save, do_not_save):
		self.save = save
		self.do_not_save = do_not_save
	

