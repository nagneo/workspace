# Chapter02-1
# Totally Basic of Python
# Usage of Print
# Reference : https://www.python-course.eu/python3_formatted_output.php
# Author: 

"""
Reference : Escape

\n : new line
\t : tab
\\ : char
\' : char
\" : char
\000 : null
...

"""
# print
print('Python Start!') 
print("Python Start!") 
print("""Python Start!""")
print('''Python Start!''')

print()

# separator option
print('P', 'Y', 'T', 'H','O','N', sep=' ')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end option
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file option
import sys

print('Learn Python', file=sys.stdout)

print()

# format option(d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s (string)
print('%10s' % ('nice',))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice',))
print('{:10}'.format('nice'))

print('{:_<10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonstudy',))
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d (integer)
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f (double)
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))