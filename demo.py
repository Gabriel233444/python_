#print('Hello world')

"""print('This is python')
print('This is python')
print('This is python')
print('This is python')
print('This is python')
print('This is python')"""

print('Python is awsome')
print(8 + 5)

#strings
print('This is a single quote')
print(type("This is a double quote"))

#integers
print(13)
print(type(50))

#float
print(13.0)
print(type(50.1))

#List
print(type(['This is a single quote', 13, 50.1]))
print([38, "hi", 45.800])

#Boolean
print(8 < 5)
print(type(8 > 6))

#Turple
print((38, "hi", 45.800))
print(type((38, "hi", 45.800)))

#Dictionary
print({'shola':38, 'john':"hi", 'joseph':45.800})
print(type({'shola':38, 'john':"hi", 'joseph':45.800}))

#Set
print({2, 3, 4, 5})
print(type({2, 3, 4, 5}))

#Arithmetic Operators
print(35 + 59)
print('true' + 'define')
print([36, 'hello',] + ['word', 39.5])
print((36, 'hi',) + ('hello',  18.50))

print(35 - 59)

print(35 * 59)
print('hi, ' * 5)

print(59 / 35)

print(59 // 35)

print(59 % 35)

print(59**2)

#Comparison Operator
print(8 == 8)
print(5 == 2)

print(8 != 10)
print(5 != 5)

print(5 > 2)
print(5 > 8)

print(5 < 10)
print(5 < 2)

print(5 > 3 and 5 < 10)
print(5 < 3 and 5 < 10)
print(5 < 3 and 5 > 10)

print(5 > 3 or 5 < 10)
print(5 < 3 or 5 < 10)
print(5 < 3 or 5 > 10)

print(not(5 < 3 or 5 > 10))

print('apple' is 'banana')
print(5 is not 3)

x = ['apple', 'banana']
print('apple' in x)
print('orange' not in x)

y = 5
j = 5
print(y)
y += 3
print(y)
y -= 3
print(y)
y *= 3
print(y)
y /= 3
print(y)
y %= 3
print(y)
j **= 3
print(j)
p = 5
p &= 3
print(p)
p |= 3
print(p)

#Conditionals
a = 5
b = 7
if a - b == 12:
    print(True)
elif a * b == 12:
    print('Sure dont u forget')
elif a / b == 12:
    print('Dont forget me')
elif a + b == 12:
    print('YH am the middle man')
else:
    print(False)
    
c = 5
d = 3
if c == d:
    print(True)
elif c <= d:
    print('Yh')
elif c >= d:
    print('Sure')
else:
    print(False)
    
for i in range(20):
    print('Hello')
    
e = 'Hello-Python'
for shola in e:
    print('Hello-World')
    
"""f = 0
while f < 5:
    enter = input('Enter a string: ')
    print(enter)
    f = f + 1"""

g = 1
while g < 20:
    print('Hi')
    g = g + 1
    
#String methods

#Concatination
print('Hello ' + 'World')

#Repitition
print('Hi ' * 5)

#indexing
h = 'Programming'
print(h[0])
print(h[1])
print(h[-1])
print(h[-2])


i = h.upper()
print(i)

j = 'PROGRRAM'
k = j.lower()
print(k)

print(j.count('R'))

print(j.isalpha())

#List
print(['list', 'brown'] + [20, 30] + [30.0, 5.0])
print(['hello', 'hi']*3)

l = ['trek', 'redline', 'specialized']
l.append('honda')
l.insert(1, 'BROWN')
#l.remove()
#l.reverse()
#l.sort()
print(l)
#m = l.pop()