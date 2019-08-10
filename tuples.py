fruits = ('apple', 'grape', 'cherry')
print(fruits)
print(fruits[1])

for item in fruits :
	print(item)

if 'apple' in fruits :
	print('Yes, apple is exist!')

print(len(fruits))

del fruits

fruits = tuple(('cherry', 'cherry', 'palm', 'grape'))
print(fruits.count('cherry'))