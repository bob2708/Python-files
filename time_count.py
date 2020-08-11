import time

class time_count:
	"""Counts execution time"""
	def __init__(self):
		self.start_time = time.time()

	def __enter__(self):
		return self

	def __exit__(self, *args):
		print(args)
		print(f"Execution time is: {time.time() - self.start_time:.7f}")

for i in range(5,0,-1):
		print(i)
		time.sleep(1)

with time_count() as t:
	z = 0
	while (z<1000000):
		if z%30==0:
			print(time.time() - t.start_time)
		z += 1
	print('='*100)