# Chapter03-2
# string type

# create string
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# print string
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# length of string
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# empty string
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# usage of escape text
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'


# print escape string
print(escape_str1)
print(escape_str2)

# tal, new line
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"
print(raw_s1)
print(raw_s2)


#multiline
multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """
print(multi_str1)

# multiline(backslash)
multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
print(multi_str2)

# operation of strings
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# castinh
print(str(66))  # check type
print(str(10.1))
print(str(True))
print(str(complex(12)))

# function of string(upper, isalnum, startswith, count, endswith, isalpha,,, etc)
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('thon', ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("split: ", str_o4.split(' '))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# description of iteration (sequence)
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인

for i in im_str:
    print(i)

# slicing
str_sl = 'Nice Python'

# exercise of slicing [start: count]
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:]) #all
print(str_sl[1:4:2]) #[start, end (not incldue index of end), step]
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])


# Ascii code
a = 'z'

print(ord(a))
print(chr(122))
