import re

text = 'The rain in Spain'
x    = re.search('^The.*Spain$', text)
print(x)

x = re.findall('Spain', text)
print(x)

str = 'The rain in Spain'
x   = re.search("Portugal", str)
print(x)

x = re.split('\s', str)
print(x)

x = re.split('\s', str, 1)
print(x)

x = re.sub('\s', '9', str)
print(x)

x = re.sub('\s', '9', str, 2)
print(x)

x = re.search("ai", str)
print(x)