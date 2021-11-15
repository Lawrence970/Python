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


# self challenge { replace [0] of a str and REPLACE with [:3] in a str}

replace = "move"

replace_split = replace[-1] + replace[1:3] + replace[0]

#print(replace)
#print(replace_split)

# i want to do the same thing above but not by hard coding and with bigger words.

mid_of_word = "crocodile"

mid_of_word_len = str(len(mid_of_word))

sub_len = mid_of_word[1:len(mid_of_word)-1]


# string manipulation. Change one letter of a str by turning it into a list, making the change, and turning it back to a str.

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



