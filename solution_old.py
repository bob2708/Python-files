class FileReader:

	def __init__(self, path=None):
		self.path = path
	
	def read(self):
		try:
			f = open(self.path, "r", encoding='utf-8') 
			temp = f.read()
			f.close()
			return temp
		except FileNotFoundError:
			return ""
		except UnicodeDecodeError as une:
			raise une
		

