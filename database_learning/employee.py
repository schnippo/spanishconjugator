class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
	@property
	def email(self):
		return '{}.{}@company.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last) 

	def __repr__(self):
		return "Employee('{}','{}','{}'".format(self.first,self.last, self.pay)

# john = Employee('John', 'Buttle', 50000)

# print(john.email)
# print(repr(john))