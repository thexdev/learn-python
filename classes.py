class Person :
	def __init__(self, name, age) :
		self.name = name
		self.age  = age

	def hello(self) :
		print('Hello, my name is ' + self.name)

p1 = Person('M. Akbar Nugroho', 17)

print(p1.name)
print(p1.age)

p1.hello()
p1.age = 18

print(p1.age)

del p1.age
del p1