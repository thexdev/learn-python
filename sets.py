fruits = {'apple', 'banana', 'cherry'}
print(fruits)

for item in fruits :
	print(item)

print('banana' in fruits)

fruits.add('orange')
print(fruits)

fruits.update(['palm', 'grape', 'strawberry'])
print(fruits)

print(len(fruits))

fruits.remove('banana')
print(fruits)

fruits.discard('palm')
print(fruits)

fruits.pop()
print(fruits)

del fruits

fruits = set(('apple', 'banana', 'cherry'))
print(fruits)