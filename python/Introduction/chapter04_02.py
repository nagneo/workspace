# Chapter04-2
# Iteration 
# FOR

# keypoint of coding
# pseudo code 
# for i in <collection>
#     <loop body>

for v1 in range(10):
    print("v1 is :", v1)

print()

for v2 in range(1, 11):
    print("v2 is :", v2)

print()

for v3 in range(1, 11, 2):
    print("v3 is :", v3)

print()

# 1 ~ 1000 sumation
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)
print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # sum(리스트)
print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))


# Iterables
# string, list, tuple, set, dictionary
# iterable return function : range, reversed, enumerate, filter, map, zip

# 1. list
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]
for name in names:
    print("You are", name)

# 2. tuple
lotto_numbers = (11, 19, 21, 28, 36, 37)
for number in lotto_numbers:
    print("Current number : ", number)

# 3. string
word = 'Beautiful'
for s in word:
    print('word : ', s)

# 4. dictionary
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print(key, ":", my_info[key])

for val in my_info.values():
    print(val)

# 5. string + if
name = 'FineApplE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue

    print("current type : ", type(v))
    print("multiply by 2:", v * 3)

# else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 45...")


# print multiplication table
for i in range(2, 10):
    print(i, end=': ')
    for j in range(2, 10):
        print('{:4d}'.format(i * j), end='')
    print()


# convert
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # ordered X
