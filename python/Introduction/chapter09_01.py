# Chapter09-1
# file read and write

# read mode - r, write mode - w, add mode a, text mode - t, binary mode b
# relative path('../, ./'), abstract path ('C:\Django\example..')

# file read
# 1
import os

print('===============1===================')

scriptPath = os.path.dirname(__file__)
filename = os.path.join(scriptPath, './resource/it_news.txt')

f = open(filename, 'r', encoding='UTF-8')
# property
print(dir(f))
# encoding
print(f.encoding)
# file name
print(f.name)
# check mode
print(f.mode)
cts = f.read()
print(cts)
# **important** close
f.close()

# 2
print('===============2===================')

with open(filename, 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 3
# read() : read all , read(10) : 10Byte
print('===============3===================')
with open(filename, 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(30)
    print(c)
    c = f.read(40)
    print(c)
    f.seek(0,0)
    c = f.read(90)
    print(c)

print()

# 4
# readline : read a line
print('===============4===================')
with open(filename, 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


print()

# 5
# readlines : read all text and save as list by line
print('===============5===================')
with open(filename, 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
        
print()

# write

# 1
content1Path = os.path.join(scriptPath, './resource/contents1.txt')

with open(content1Path, 'w') as f:
    f.write('I love python\n')

# 2
with open(content1Path, 'a') as f:
    f.write('I love python2\n')
    
    
# 3
# writelines : list -> file
content2Path = os.path.join(scriptPath, './resource/contents2.txt')
with open(content2Path, 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
    
# 4
content3Path = os.path.join(scriptPath, './resource/contents3.txt')
with open(content3Path, 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)