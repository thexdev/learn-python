def hello() :
	print('Hello, Python!')

def show_name(name) :
	print(name)

def print_age(age = 17) :
	print('Your age is {age}'.format(age = age))

def extract_fruit(fruit) :
	for key, value in fruit.items() :
		print('{key} : {value}'.format(key = key, value = value))

def times_with_2(number = 0) :
	return 2 * number

def tri_recursion(k) :
	if k > 0 :
		result = k + tri_recursion(k - 1)
		print(result)
	else :
		result = 0
	return result

hello()
show_name('M. Akbar Nugroho')
print_age(25)
print_age()
extract_fruit({'name': 'apple', 'vitamins': ['C', 'B']})

print(times_with_2(3))
print(times_with_2(5))

print('========== Recursion Example Result ==========')
print(tri_recursion(6))