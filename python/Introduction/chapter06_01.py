# Chapter06-1
# python class
# OOP(object oriented programming), Self, instance method, instance variable

# understanding difference with class and instance
# namespace : space stored when you instantiate objects
# class variable : accessable to directly, share
# instance variable : exist independently by objects

# 1
class Dog: # object inheritance
    # property of class
    species = 'firstdog'
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# information of class
print(Dog)

# instantiation
a = Dog("mikky", 2)
b = Dog("baby", 3)

# comparison
print(a == b, id(a), id(b))

print('======================__dict__======================')
# namespace
print('dog1', a.__dict__)
print('dog2', b.__dict__)    
    
# check property of class
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 2
# self
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')


f = SelfTest()

# print(dir(f))
print(id(f))
#f.func1() # Exception (TypeError: SelfTest.func1() takes 0 positional arguments but 1 was given)
f.func2()
SelfTest.func1()
# SelfTest.func2() # Exception (TypeError: SelfTest.func2() missing 1 required positional argument: 'self')
SelfTest.func2(f)

# 3
# class variable, instance variable
class Warehouse:
    # class variable 
    stock_num = 0 # stock
    
    def __init__(self, name):
        # instance variable
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 4
class Dog: # object inheritance
    # property of class
    species = 'firstdog'
    
    # initiation / property of instance
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
        
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# instance creation
c = Dog('july', 4)
d = Dog('Marry', 10)
# call method
print(c.info())
print(d.info())
# call method
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))