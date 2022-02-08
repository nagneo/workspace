# Chapter03-1
# number type variable

# Data type supported by python 
'''
int : integer
float : real number
complex : complex
bool : boolean
str : string(sequence)
list : list(sequence)
tuple : tuple(sequence)
set : set
dict : dictionary(map)
'''

# Data type
str1 = "Python"
bool = True
str2 = "Anaconda"
float = 10.0
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = 3, 5, 7
set = {7, 8, 9}

# Print data type
print(type(str1))
print(type(bool))
print(type(str2))
print(type(bool))
print(type(float))
print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))

# number operator
"""
+ 
- 
* 
/ 
// : quotient
% : remainder
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : square
....
"""

# Declare integer
i = 77
i2 = -14
big_int = 999999999999999999999999999999999999999

# Print integer
print(i)
print(i2)
print(big_int)

# Declare float
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# Print float
print(f)
print(f2)
print(f3)
print(f4)

# Exercise
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 

# -
print(">>>>> -")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)

# *
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)

# /
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)

# //
print(">>>>> //")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)

# %
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)

# **
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)

# Exercise of type casting
a = 3.
b = 6
c = .7
d = 12.7

# print type
print(type(a), type(b), type(c), type(d))

# type casting
del float
del int
del bool

print(float(b))  # integer -> float
print(int(c))  # float -> integer
print(int(d))  # float -> integer
print(int(True))  # Bool -> integer
print(float(True))  # Bool -> float
print(int(False))  # Bool -> integer
print(float(False))  # Bool -> float
print(complex(3))  # integer -> complex
print(complex('3'))  # character -> complex
print(complex(False))  # Bool -> complex

# Numerical calculation function
print(abs(-7))
x, y = divmod(100, 8)
print("divmod(100,8): {} {}".format(x, y))
print("pow(5,3): ".format(pow(5, 3)))

#import external module
import math

#ceil
print(math.ceil(5.1))   # The smallest integer among the numbers above x

#floor

#pi
print(math.pi)
