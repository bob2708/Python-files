class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def __str__(self):
		return f"Привет, {self.name}. Твоя почта - {self.email}"

	# def __getattr__(self, name):
	# 	print('If not found')

	# def __getattribute__(self, name):
	# 	print('Always')

	def get_email_data(self):
		return {
			'name': self.name,
			'email': self.email
		}


