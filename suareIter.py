class SquareIterator:
	def __init__(self, start, end):
		self.current = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.end:
			raise StopIteration("End of container")

		self.current += 1 
		return (self.current-1)**2

