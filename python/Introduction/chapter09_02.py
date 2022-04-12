# Chapter09-2
# CSV file read and write

# CSV : MIME - text/csv

import csv
import os

# 1
scriptPath = os.path.dirname(__file__)
filePath = os.path.join(scriptPath, './resource/test1.csv')
with open(filePath, 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header Skip
    # check object
    print(reader)
    # check type
    print(type(reader))
    # check property
    print(dir(reader))  # __iter__
    print()

    for c in reader:
        # print(c)
        # check type
        print(type(c), end=' ')
        # list to str
        print(''.join(c))

# 2
filePath = os.path.join(scriptPath, './resource/test2.csv')
with open(filePath, 'r') as f:
    reader = csv.reader(f, delimiter='|')  # choose seperator
    # next(reader) Header skip
    # check

    for c in reader:
        # print(c)
        print(''.join(c))

# # 3 (Dict Conversion)
filePath = os.path.join(scriptPath, './resource/test1.csv')
with open(filePath, 'r') as f:
    reader = csv.DictReader(f)
    #check
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ check
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----')

# 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
writePath = os.path.join(scriptPath, './resource/write1.csv')
with open(writePath, 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    # dir check
    print(dir(wt))
    # type check
    print(type(wt))
    for v in w:
        wt.writerow(v)

# 5
writePath = os.path.join(scriptPath, './resource/write2.csv')
with open(writePath, 'w', newline='') as f:
    # field name
    fields = ['one', 'two', 'three']
    # Dict Writer declaration
    wt = csv.DictWriter(f, fieldnames=fields)
    # Herder Write
    wt.writeheader()

    for v in w:
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})
