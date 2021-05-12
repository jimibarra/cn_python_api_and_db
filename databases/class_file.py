class User():

	def __init__ (self, id, first_name, last_name, email):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	def __str__(self):
		return f"The user {self.id} has name {self.first_name} {self.last_name} and email {self.email}."
