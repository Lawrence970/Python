import random

int_0 = 48 # integer
float_0 = 1.5

# convert int_0 to hex
hex_0 = hex(int_0)
# print(hex_0) >>> 0x30

sum_0 = int_0 + float_0
# sum_1 = int_0 + hex_0 cant be done because hex_0 is a str now
# print(type(sum_0)) >>> <class 'float'>


x = int_0 / random.random()

if x > 150.0:
    y = x % 2
    y = int(y) # truncates float to int
    print(y)
else:
    print('x is less than 150.0')
