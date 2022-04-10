# Chapter06-3
# python package
# write package and usage
# python is configured by independent module seperated with package
# __init__.py : can detect as a package even if it's not existed, after Python3.3 -> but, recommended for backward compatibility
# relative path : ..(parent directory), .(current directory) -> only used in module

# 1
import sub.sub1.module1
import sub.sub2.module2

# usage
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

# usage
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # Alias

# usage
module1.mod1_test1()
module1.mod1_test2()

# usage
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 3
from sub.sub1 import *
from sub.sub2 import *

# usage
module1.mod1_test1()
module1.mod1_test2()

# usage
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()
