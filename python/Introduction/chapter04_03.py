# Chapter04-3
# Iteration 2
# While

# Expression
# while <expr>:
#    <statement(s)>

# 1.
n = 5
while n > 0:
    print(n, end=' ')
    n = n - 1
print()

# 2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(), end=' ')
print()

# 3. if 
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n, end=' ')
print('Loop Ended.')  
print()

# 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m, end=' ')
print('Loop Ended.')   

# 5
i = 1
while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1
print()


# While - else statemnet

# 6
n = 10
while n > 0:
    n -= 1
    print(n, end=' ')
    if n == 5:
        break
else:
    print('else out.') # example: n <= 0

# 7 
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.') # example: i >= len(a)
    
# infinity
# while True:
#     print('Foo')

# 8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())








