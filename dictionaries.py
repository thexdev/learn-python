computer = {
	'name' : 'COM-001',
	'model': 'UXVBM53',
	'year' : 2019
}

x = computer.get('model')

print(computer)
print(computer['name'])
print(x)

computer['name'] = 'ASUS X9071UV'

print(computer)

for detail in computer :
	print(computer[detail])

for x in computer.values() :
	print(x)

for key, value in computer.items() :
	print('{key} : {value}'.format(key = key, value = value))

if 'model' in computer :
	print('Yes, model is exist!')

print(len(computer))

computer['processor'] = 'Intel Core i9'
computer['color'] = 'red'
print(computer)

computer.pop('color')
print(computer)

com001 = dict(computer)
print(com001)

if com001 is computer :
	print('Yes, they are same!')
else :
	print('No, they arent same!')


com002 = dict(brand = 'Honda', model = 'Jazz', year = 2019)
print(com002)
