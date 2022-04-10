# Chapter05-2
# python input
# Usage of Input
# basic type(str)

# 1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 2
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number", type(number), number * 3)
print("type of nanme", type(name))

# 3 - computation
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)


# 4
float_number = float(input("Enter a float number : "))

print("input float : ", float_number)
print("input type : ", type(float_number))


# 5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))