fruits = ['apple', 'banana', 'cherry']

for x in fruits :
	print(x)

for x in 'banana' :
	print(x)

for x in fruits :
	print(x)
	if x == 'banana' :
		break

for x in fruits :
	if x == 'banana' :
		break
	print(x)

for x in fruits :
	if x == 'banana' :
		continue
	print(x)

for x in range(6) :
	print(x)

for i in range(2, 6) :
	print(i)

for i in range(2, 30, 3) :
	print(i)

for x in range(6) :
	print(x)
else :
	print('loop is done!')

adj = ['red', 'big', 'tasty']

for x in adj :
	for y in fruits :
		print(x, y)

