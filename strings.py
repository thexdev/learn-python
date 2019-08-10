print("Hello")
print('Hello')

a = 'Hello'
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)
print(b)
print(c)
print(a[0])
print(a[0:2]) # substring

e = ' Hello, world! '
print(e.strip())
print(len(e))    # print the length of variable 'e'
print(e.lower()) # change the variable to lowercase
print(e.upper()) # change the variable to uppercase
print(e.replace('H', 'J')) # replace H to J
print(e.split(','))

age = 25
txt = 'My namme is Akbar, and I am {}'
print(txt.format(age))

quantity = 3
item_no  = 253
price    = 49.95
my_order = 'I want {} pieces of item {} for {} dollars.'
print(my_order.format(quantity, item_no, price))

my_order = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(my_order.format(quantity, item_no, price))