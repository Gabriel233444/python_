#Single Comment

"""
This is a multi-line
comment 
"""

#Variables
x = 10
y = 'hello'
z = 5.50

#Data Types

#strings:-
a = 'gabriel' #single quotes
b = "james" #double quote
print(type(a))

#Integers:-
c = 5
d = 6
print(type(c))

#Floats:-
e = 5.5
f = 10.55556
print(type(f))

#Booleans:-
g = True
h = False
print(type(g))

#List:-
i = ['hello', 15, 20.50, True]
print(type(i))


#Tuples:-
j = ('hello', 15, 20.50, True)
print(type(j))

#Dictionary:-
k = {'key1':'hello', 'key2':15, 'key3':20.50, 'key4':True, 'key5':['cody', 18, 1.50]}
print(type(k))

#Set:-
l = {'hello', 15, 20.50, True}
print(type(l))

#Operators

#Arithmetic Operators:-
m = 10
n = 20
print(m + n)
print(m - n)
print(m * n)
print(m / n)
print(m % n)
print(m // n)
print(m ** n)

#Comparison Operators:-
print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)

#Logical Operators:-
print(m > n and m < n)
print(m > n or m < n)
print(not(m > n and m < n))

#Identity Operators:-
print( m is n)
print(m is not n)

#Membership Operators:-
print(10 in [n])
print(20 in [n])

#Assignment Operators:-
m+=10
print(m)
m-=20
print(m)
m*=30
print(m)
m/=40
print(m)
m%=50
print(m)
m//=60
print(m)
m**=70
print(m)

# Bitwise AND
result_and = 5 & 3  # Binary: 0101 & 0011 = 0001
print(result_and)  # Output: 1

# Bitwise OR
result_or = 5 | 3  # Binary: 0101 | 0011 = 0111
print(result_or)   # Output: 7

# Bitwise XOR
result_xor = 5 ^ 3  # Binary: 0101 ^ 0011 = 0110
print(result_xor)  # Output: 6

# Bitwise NOT
result_not = ~5  # Binary: ~0101 = 1010 (in two's complement form)
print(result_not)  # Output: -6

# Left Shift
result_left_shift = 5 << 1  # Binary: 0101 << 1 = 1010
print(result_left_shift)    # Output: 10

# Right Shift
result_right_shift = 5 >> 1  # Binary: 0101 >> 1 = 0010
print(result_right_shift)    # Output: 2


#Conditional Statements

#if & else:-
o = 50
if o < n :
    print('YES')
else:
    print('NO')

#if & elif & else:
p = 15.0
q = 15
if p is q:
    print('the first condition is correct')
elif p == q:
    print('condyion 2 met')
elif p <= q:
    print('condition 3 met')
elif p != q:
    print('condition 4 met')
else:
    print('None is correct')

if p == 15:
    print(True)
elif q == p:
    print('Middle')
else:
    print(False)

#Loop Statements

#for loop:-
for i in range(2, 10, 2):
    print(i)

for j in range(1, 20, 5):
    print(j)

k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for l in k:
    print(l)

#while loop:-   
r = 0
while r < 5:
    print(r)
    r = r + 1

"""s = 0
while s < 20:
    word = input('Enter a word: ')
    print(word)
    s = s + 1"""

#Break Statement
s = 0
while s != 20:
    print(True)
    s = s + 1
    break

temp = 0
while temp != -1000:
    temp = eval(input('Enter a temperature (-1000 to quit): '))
    print('In Fahrenheit that is', 9/5*temp+32)
    break

#String Methods

#Concatination
print('This ' + 'is ' + 'a ' + 'Ball')  

t ="""
    Yuji, Itadori, James, Panda,
    Yuta, Maki, Mai, Fushiguro,
    Megumi, Kiburasaki, Hanami,
    """

u ="""
    Nanami, Gojo, Satoru, Jogo,
    Mahito, Aoi, Choso, Sukuna,
    Uraume, Kenjaku, Getto, Hakari
    """

print(t + u)

#Repitition
print(u * 2)