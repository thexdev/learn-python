quantity = 3
item_no  = 567
price    = 49
text     = 'I want {} pieces of item number {} for {:.2f} dollars.'
print(text.format(quantity, item_no, price))

age  = 17
name = 'M. Akbar Nugroho'
text = 'His name is {1}. {1} is {0} years old.'
print(text.format(age, name))

order = 'I have a {carname}, it is a {model}'
print(order.format(carname = 'Ford', model = 'Mustang'))