class Person :
	def __init__(self, first_name, last_name) :
		self.first_name = first_name
		self.last_name  = last_name

	def print_name(self) :
		print('Hello, my name is {first} {last}'.format(first = self.first_name, last = self.last_name))


class Student(Person) :
	def __init__(self, first_name, last_name, graduation_year) :
		super().__init__(first_name, last_name)
		self.graduation_year = graduation_year

	def welcome(self) :
		print('Welcome! {first_name} {last_name} to the class of {graduation_year}!'.format(first_name = self.first_name, last_name = self.last_name, graduation_year = self.graduation_year))

x = Student('M. Akbar', 'Nugroho', 2019)
x.print_name()
x.welcome()