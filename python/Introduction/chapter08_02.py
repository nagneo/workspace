# Chapter08-2
# python external function
# commonly used in real programming
# types : sys, pickle, os, shutil, glob, temfile, time, random etc

# sys : control execution
import sys

# 1
print(sys.argv)

# 2 -force shot down
# sys.exit() 

# 3 - location of python package
print(sys.path)


# pickle : write file
import pickle

# 4 - write
f = open("test.obj", 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 5 - read
f = open("test.obj", 'rb')
data = pickle.load(f)
print(data)
f.close()


# os : environmental variables, directory(file) process, os task
# mkdir, rmdir(remove if empty), rename
import os

# 6
print(os.environ)
print(os.environ['USERNAME'])

# 7 (current location)
print(os.getcwd())


# time : process time
import time

# 8
print(time.time())

# 9 - casting
print(time.localtime(time.time()))

# 10 - simple expression
print(time.ctime())

# 11 - formatting expression
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 12 - time interval execution
for i in range(5):
	print(i)
	time.sleep(1)


# random : return random number
import random

# 13
print(random.random())

# 14
print(random.randint(1, 45))

# 15 - mix
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 16 - random
c = random.choice(d)
print(c)


# webbrowser : 본인 OS 의 웹 브라우저 실행
import webbrowser

# 예제17
webbrowser.open("http://google.com")

# 예제18(새창 실행)
webbrowser.open_new("http://google.com")