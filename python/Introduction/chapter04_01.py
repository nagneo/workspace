# Chapter04-1
# Control Statement
# IF

# basic
print(type(True))
print(type(False))

# Exercise
if True:
    print("Good")  # need to indent

if False:
    # not execute
    print("Bad")

if False:
    # not execute
    print("Bad")
else:
    # execute
    print("Good")

# relational operator
# >, >=, <, <=, ==, !=


x = 15
y = 10

# == (equal)
print(x == y)

# != (not equal)
print(x != y)

# >
print(x > y)

# >= 
print(x >= y)

# < 
print(x < y)

# <= 
print(x <= y)

# type of true, false
# True : "values", [values], (values), {values}, 1
# False : "", [], (), {}, 0, None

city = ""
if city:
    print("You are in:", city)
else:
    # print
    print("Please enter your city")

city = "Seoul"
if city:
    #print
    print("You are in:", city)
else:
    print("Please enter your city")

# logical operator
# and, or, not
# Reference : https://www.tutorialspoint.com/python/python_basic_operators.htm

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)  # a > b > c
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# priority of computation
# arithmetic > relational >logical

print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("Pass.")
else:
    print("Fail.")

# Example

id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin":
    print("Administrater authentication")

if id2 == "admin" and grade == "platinum":
    print("Platinum Administrator")


# multiple conditional statement
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('Fail')

# duplicated conditional stetement

grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print("Scholarship 100%")
    elif total >= 80:
        print("Scholarship 80%")
    else:
        print("Scholarship 70%")
else:
    print("Scholarship 50%")

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)  # key 
print("seoul" in e.values())  # value
