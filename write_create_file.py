"""
file = open('file/test.py', 'at')
file.write('Now the file has more content!')
file.close()

# Open and read the file after appending
file = open('file/test.py', 'rt')
print(file.read())
file.close()
"""

"""
file = open('file/test.py', 'wt')
file.write('Woops! I have deleted the content!')
file.close()

file = open('file/test.py', 'rt')
print(file.read())
"""

file = open('file/system.py', 'x')

if file :
	print('The file has been created!')
else :
	print('Cant create the file!')