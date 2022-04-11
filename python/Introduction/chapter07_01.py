# Chapter07-1
# understanding of python exception handling
# type of exception
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# it is okay grammertically, but exception in runtime is important
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError
# print('error)
# print('error'))
#if True
#    pass

# NameError
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4]) #error 
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) #error

# KeyError

dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : use wrong property in class or module
import time
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError : operation with wrong type
# x = [1,2]
# y = (1,2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))

# base of handling exception
# try : code which have a possibility of causing error
# except errorname1: possible multi
# except errorname2:
# else : execute when try block has no error
# finally : execute always

name = ['Kim', 'Lee', 'Park']

# 1
try:
    z = 'Kim' 
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()

# 2
try:
    z = 'Cho' # 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()

# 3
try:
    z = 'Cho' # 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')
finally:
    print('Ok! finally')

print()

# 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Park':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')