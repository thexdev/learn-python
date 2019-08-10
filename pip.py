from camelcase import CamelCase

text = 'Hello, world!'
txt  = 'lorem ipsum sit dolor amet'
cc   = CamelCase()

print(cc.hump(txt))