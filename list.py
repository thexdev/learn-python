list_fruit = ['banana', 'apple', 'grape', 'cherry']
print('{} : {}'.format(list_fruit, type(list_fruit)))

list_fruit[0] = 'peach'
print('{} : {}'.format(list_fruit, type(list_fruit)))

for fruit in list_fruit :
	print(fruit)

if 'apple' in list_fruit :
	print('Yes, apple is exist!')

print(len(list_fruit))

list_fruit.append('orange')
print(list_fruit)

list_fruit.insert(1, 'palm')
print(list_fruit)

list_fruit.remove('palm')
print(list_fruit)

list_fruit.pop()
print(list_fruit)

list_fruit.pop(1)
print(list_fruit)

del list_fruit[0]
print(list_fruit)

fruits = list(list_fruit)
print(fruits)

newlist = list(('apple', 'banana', 'grape'))
print(newlist)

print(list_fruit.reveres())