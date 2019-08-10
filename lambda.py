x = lambda a, b : a * b

def myfunc(n) :
	return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
print(x(6, 10))