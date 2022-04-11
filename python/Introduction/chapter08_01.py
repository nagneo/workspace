# Chapter08-1
# python Built-In function
# exercise of commonly used functions
# if you use this, it will be mastered naturally
# str(), int(), tuple() : already studied

# abstract value
# abs()
print(abs(-3))

# all, any : iterable element check(true, false)
print(all([1,2,3])) # and
print(any([1,2,0])) # or

# chr : ascii -> character , ord : character -> ascii

print(chr(67))
print(ord('C'))

# enumerate : index + create Iterable object
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)


#  filter : extract value which is fit to condition in iterable objects
print('>>>>>>>>conv_pos')
def conv_pos(x):
    return abs(x) > 2
    
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : return address(reference) of object

print(id(int(5)))
print(id(4))

# len : return length of element
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# max, min : maximul value, minimum value
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))

# map
print('>>>>>>>>conv_abs')
def conv_abs(x):
    return abs(x)
    
print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x:abs(x),[1,-3,2,0,-5,6])))

# pow : return pow
print(pow(2,10))

# range :return iterable objects
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round
print(round(6.5781, 2))
print(round(5.6))

# sorted : return iterable objects after sorting 
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))

# sum : return summation of iterable objects
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# type : check type
print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : return iterable object after grouping
print(list(zip([10,20,30],[40,50,777])))
print(type(list(zip([10,20,30],[40,50,777]))[0]))