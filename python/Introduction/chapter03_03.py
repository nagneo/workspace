# Chapter03-3
# python list
# important in data struction
# python do not provide array
# list type(ordered, enabble to duplicate, enable to change, enable to delete)

# declaration
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# Indexting
print('>>>>>> ' + 'Indexing')
print('1. d - ', type(d), d)
print('2. d - ', d[1])
print('3. d - ', d[0] + d[1] + d[1])
print('4. d - ', d[-1])
print('5. e - ', e[-1][1])
print('6. e - ', list(e[-1][1]))

# slicing
print('>>>>>> ' + 'slicing')
print('7. d - ', d[0:3])
print('8. d - ', d[2:])
print('9. e - ', e[2][1:3])

# operation of list
print('>>>>>> ' + 'operation')
print('10. c + d - ', c + d)
print('11. c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("12. 'Test' + c[0] - ", 'Test' + str(c[0]))

# compartion of value
print('14. ' + c == c[:3] + c[3:])

# which is same id
temp = c
print(c == temp)


# 리스트 수정, 삭제
print('>>>>>> ' + 'list ')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# list function
a = [5, 2, 3, 1, 4]

print('original : a - ', a)
a.append(6)
print('append : a - ', a)
a.sort()
print('sort : a - ', a)
a.reverse()
print('reverse : a - ', a)
print('index : a - ', a.index(5))
a.insert(2, 7)
print('insert : a - ', a)
a.reverse()
a.remove(1)
print('reverse and remove : a - ', a)
print('pop : a - ', a.pop())
print('pop : a - ', a.pop())
print('count : a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('extend : a - ', a)

# iteration exercise
while a:
    l = a.pop()
    print(2 is l)