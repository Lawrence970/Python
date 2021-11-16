import sys
import math
import random



# list manipulation basics
x = random.random()
y = random.random()
z = x-y
len_z = len(str(z))
some = [x]
if len(some) < 2:
    some.append(y)
if x > y:
    some.append(z)
#print(x, y, z, len_z, some)



# string manipulation basics page 100ish
name = [1,2,3,4,5]
place = 'face'
split_name = str(name[1:3])
place = '4' + place[0:1]
#print(place)


# * self challenge { replace [0] of a str and REPLACE with [:3] in a str}

replace = "move"

replace_split = replace[-1] + replace[1:3] + replace[0]

#print(replace)
#print(replace_split)

# i want to do the same thing above but not by hard coding and with bigger words.

mid_of_word = "crocodile"

mid_of_word_len = str(len(mid_of_word))

sub_len = mid_of_word[1:len(mid_of_word)-1]


#! string manipulation. Change one letter of a str by turning it into a list, making the change, and turning it back to a str.

#old way
S = 'bushobama'
L = list(S)
L[1] = 'x'
change_back = ''.join(L)

#good way using bytearray
B = bytearray(b'spam')
B.extend(b'eggs')
B1 = B.decode()


# using .find() and .replace(); str operations.

U = 'undermyhat'
# .find() will return value of offset and -1 {if it is not valid}
find_in_U = U.find('under') # returns 0
find_in_U2 = U.find('myhat') # returns 5


# list nesting can be done to create matricies.

nesting_matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

r2c1 = nesting_matrix[1][0]
#print(r2c1)
#matricies can be operated on, for e.g. >>
col2 = [pos[1] for pos in nesting_matrix] #! this will find every value at [1] in every 'row'(list) and create a new list from those values. 
                                            #! called a comprehension.
col3_multi = [row[2] *2 for row in nesting_matrix] # this will create a new list from row 


# * self challenge {create a matrix with 10 odd numbers and 2 even numbers. locate the even numbers and take the sum storing in a variable sum_even}
matrix_0 = [[1,17,5,14], #need to know more i think.
            [73,48,21,87],
            [13,9,23,19]]

# you can do stuff like this with matricies

r3c4 = matrix_0[2][2:4] # the 3rd list item in matrix_0; the 3rd to 4th values in 3rd list.
# with that i can grab whatever i want.
#print(len(matrix_0)) # all three 'rows'
#print(len(matrix_0[0])) # all 4 values in one 'row'


#! lists are mutable and can contain anything in python
jumble = [5, [0,5,6], 'string', {object}]
type_jumble_0 = type(jumble[0]) # type will remain an int
j0_add = jumble[0] + 81 # works because type is int


#! the range() function is bult-in and generates sequential numbers.

my_range = range(4)
#print(my_range) >>> range(0, 4)
my_range_list = list(range(4))
#print(my_range_list) >>> [0,1,2,3]


#playing with list()

stringy = list('word')
#print(stringy) >>> ['w','o','r','d']


# generators: storing comprehensions into a variable.

G = (sum(row) for row in matrix_0)
# print(G) >>> <generator object <genexpr> at 0x000001C60C85E9D0> ????

#! Dictionaries

D = { # 'KEY' : VALUE
    'food': 'eggs',
    'quantity': 18,
    'list_in_D': [14,31,23]
}
#print(D) >>> entire dictionary
D['quantity'] += 1 # add 1 to VALUE of the KEY quantity
D['list_in_D'[1]] = 14 # change a value in the key 'list_in_D'


#im hungry
D['breakfast'] = 'eggs in oats'

Dget = D.get('breakfast')
# print(Dget)

ifD = D['x'] if 'x' in D else 0 # ifD = D['x'] ONLY IF 'x' is in D, otherwise ifD = 0

#print(D['x']) >>> KeyError: 'x'
print(ifD)

