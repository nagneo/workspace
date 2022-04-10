# Chapter05-1
# importance of python function 
# python function and lambda

# function definition expression
# def function_name(parameter):
#     code

# 1
def first_func(w1):
    print("Hello, ", w1)

word = "Goodboy"

first_func(word)

# 2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)
    

# 3 return multi variables

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y ,z)

# 4 return tuple
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))

# 5 return list
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(30)

print(type(p), p, set(q))

# 6  return dictionary
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 7 importance
# *args, **kwargs

# *args (unpacking)
def args_func(*args): # parameter name is freely determined.
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs (unpacking)
def kwargs_func(**kwargs): # parameter name is freely determined.
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

# combination of * and **
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

# nested function

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)

# not executable
# func_in_func(1000)

# Example of Lambda
# Save of memory, readability up, simple code
# function object create -> resource(memory) assign
# 람다는 즉시 실행 함수(Heap Initialize) -> memory initialize
# If it's overused, it's less legible

#def mul_func(x, y):
#    return x * y
    
#lambda x, y:x*y

# general function -> assign
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))

# lambda -> assign
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda_mul_func)
 

# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)