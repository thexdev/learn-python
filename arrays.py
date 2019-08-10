cars = ['volvo', 'toyota', 'mitstubishi', 'ferrari']
print(cars)

cars[0] = 'Honda'
print(cars)

x = len(cars)
print(x)

for x in cars : 
	print(x)

cars.append('suzuki')
print(cars)

cars.pop(1)
print(cars)

cars.remove('suzuki')
print(cars)

cars.reverse()
print(cars)