# Chapter02-2
# Totally Basic of Python
# Variables of Python

# Declaration and assignment
n = 700

# Print
print(n)
print(type(n))

# Multiple declaration
x = y = z = 700

# Pirn
print(x, y ,z)

# Declaration
var = 75

# Print
print(var)
print(type(var))

# Redeclaration interger value to string value
var = "Change Value"

# Print
print(var)
print(type(var))


# Object References
# variable assign statement
# 1. create object by type
# 2. carete value
# 3. print to console

# 예1)
print(300)

# 예2)
# n -> 777
n = 777

print(n)
print(type(n))

m = n
# m-> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400
# m-> 400, 777 <-n

print(m)
print(type(m))


# check id(identity) : identified value of object
m = 800
n  = 655

print("id(m): {}".format(id(m)))
print("id(n): {}".format(id(n)))


m = 800
n  = 800

# refenrence same object
print(id(m))
print(id(n))

# Variout declaration of variables
# Camel Case :  numberOfCollegeGraduates
# Pascal Case :  NumberOfCollegeGraduates
# Snake Case :  number_of_college_graduates

# Enable formats of variable name
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# Reserved word which can not be used as varialble 
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""