from loguru import logger

#keyword module to list them 
import keyword
print(keyword.kwlist)

#Data Types
a = 1
b = "1"
c = 1.2
d = True
e = [a,b,c,d]
f = (a,b,c,d,e)
g = {a:b, c:d}
h = {a,b,c,d}
i = None

print(type(a),a)  #<class 'int'> 1
print(type(b),b)  #<class 'str'> 1
print(type(c),c)  #<class 'float'> 1.2
print(type(d),d)  #<class 'bool'> True
print(type(e),e)  #<class 'list'> [1, '1', 1.2, True]
print(type(f),f)  #<class 'tuple'> (1, '1', 1.2, True, [1, '1', 1.2, True])
print(type(g),g)  #<class 'dict'> {1: '1', 1.2: True}
print(type(h),h)  #<class 'set'> {1.2, 1, '1'}
print(type(i),i)  #<class 'NoneType'> None

#type conversion
x = int("123")     # String → Integer
y = str(3.14)      # Float → String

#operators

#arithmetic operators
a = 400
b = 300
logger.info(a+b)
logger.info(a-b)
logger.info(a*b)
logger.info(a/b)
logger.info(a**b)
logger.info(a//b)
logger.info(a%b)

#comparison operators
logger.info(a==b)
logger.info(a!=b)
logger.info(a<=b)
logger.info(a<b)
logger.info(a>=b)
logger.info(a>b)


#logical Operators
# Logical Operators: and, or, not
x = 10
y = 5

# and → both conditions must be True
if x > 5 and y < 10:
    print("✅ Both conditions are True")

# or → at least one condition must be True
if x < 5 or y < 10:
    print("✅ At least one condition is True")

# not → reverses the result
is_sunny = False
if not is_sunny:
    print("☁️ It's not sunny today")
