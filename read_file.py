file = open('file/test.py', 'rt')

# print(file.read(5))
# print(file.read())
# print(file.readline())

for x in file :
	print(x)

file.close()