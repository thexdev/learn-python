import random

pos_int = 25  # possitive int
neg_int = -25 # negative int

print(type(pos_int))
print(type(neg_int))

pos_float = 2.5  # possitive float
neg_float = -2.5 # negative float
pow_float = 2e5  # power float

print(type(pos_float))
print(type(neg_float))
print(type(pow_float))

pos_complex = 25j  # possitive complex
neg_complex = -25j # negative complex

print(type(pos_complex))
print(type(neg_complex))

# Type conversion
a = 1

print(float(a))   # convert int to float
print(complex(a)) # convert int to complex

# Random number
print(random.randrange(3, 25))