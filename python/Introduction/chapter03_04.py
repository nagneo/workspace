# Chapter03-4
# tuple
# important 'comparison with list'
# tuple tyle(ordered, duplicateable, not change , not delete)

#A tuple (tuple) is a set of objects with an invariant order.
#Similar to the list type, but once created, the value cannot be changed.
#Check REPL.

#Like a list, various types can be included together.

# declaration
a = ()
b = (1,)
c = (11, 12,13,14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# indexing
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# delete X
# d[0] = 1500
# print('d - ', d)

# slicing
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# operation of tuple
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# function of tuple
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))

# Packing & Unpacking

# packing
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# unpacking
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)

# unpacking 2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')
print(x1, x2, x3, x4)

t2 = 1, 2, 3
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)
