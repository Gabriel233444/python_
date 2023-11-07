#Single Line comment
#print('Hello world')
#print('Hello world')
#print('Hello world')
#print('Hello world')

#Multy line comment
"""print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')
print('Hello world')"""

#variables
v = 'Hello World'
b = 'How are you doing today'
print(v)
print(b)

#Data types

#Strings
var = "This is a double quote string"
boo = 'This is a single quote string'
print(var)
print(boo)

#Integers
i = 46
print(i)

#float
flo = 42.9837
print(flo)

#list
lis = ['banana', 50, 80.2]
print(lis)

#tuple
tu = ('banana', 50, 80.2)
print(tu)

#boolean
x = 8
y = 6
print(x < y)

#dictionary
dic = {'a':'banana', 'b':50, 'c':80.2, 'd':True}
print(dic)
print(type(dic))

#set
se = {'banana', 50, 80.2}
print(se)
print(type(se))

#Arithmetic Opreations
add1 = 1000
add2 = 30
print(add1 + add2)
print(add1 * add2)
print(add1 / add2)
print(add1 % add2)
print(add1**add2)
print(add1 // add2)

#Comparison Opreation
e = 30
q = 40
print(e == q)
print(e != q)
print(e > q)
print(e < q)
print(e >= q)
print(e <= q)

#Logical Opreators
print(e != q and e < q)#both statement are True
print(e > q or e < q) #one of the statement is True
print(not(e != q, e < q))#the ouput is true it return false

var1 = 50
var2 = 8
var3 = 10
var4 = 30

print(var1 == var2, var3 != var4)
print(var1 > var2, var3 < var4)
print(var1 >= var2, var3 <= var4)

print('*', '*', '*')
print('*', ' ', '*')
print('*', '*', '*')

#identity opreator
id1 = ["apple", "banana"]
id2 = ["apple", "banana"]
id3 = id1
print(id1 is id2)
print(id1 is id3)
print(id1 is not id2)

#membership opreator
print("banana" in id1)
print("orange" in id2)
print("orange" not in id2)
print("apple" not in id1)

#assignment operators
asi = 5
asi |= 3
print(asi)

#conditional statement
ball = 8

#if statement
if ball > 10:
    print('')

#if/else statement
if ball <= 10:
    print('ball is greater than ten')
else:
    print('ball is just a ball')

moon = 50
do = 80
sv = 10
cl = 12
if (moon or do) and (sv or cl) == 10:
    print(True)
else:
    print(False)


"""grade = eval(input('Enter your score:  '))
if grade >= 90:
    print('A')
elif grade >= 70:
    print('B')
elif grade >= 60:
    print('C')
elif grade >= 50:
    print('D')
else:
    print('F')

num = eval(input('Enter a number:  '))
if num >= 0:
    print('Valid number')
else:
    print('Invalid number')"""
    
    
ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in ran:
    print(i)

"""g = eval(input('Enter a Number: '))
if g in ran:
    print('Number in List')
else:
    print('Number not in List')"""
    
r = ['a', 'b', 'c', 'd', 'e', 'f']

for letters in r:
    print(letters)
    
#sla = 'letters'
#las = [1, 2, 3, 4, 5]

"""for i in range(20):
    bc = eval(input('Enter a number: '))
    if bc == 50:
        print('Number is greater than 10')
    elif bc <= 50:
        print('Number is less than 10')
    else:
        print('Just rest')"""
    
    
#abc = eval(input('Enter a number: '))
#for i in range(abc):
#    print(i)

"""temp = 0
while temp != -1000:
    temp = eval(input('Enter a temperature (-1000 to quit): '))
    print('In Fahrenheit that is', 9/5*temp+32)
    break
    
    
Temp = 0
while Temp != -1001:
    Temp = eval(input('Enter a temperature (-1001 to quit): '))
    if Temp != -1001:
        print('In Fahrenheit that is', 9/5*Temp+32)
    else:
        print('Bye!')
    
rang = 1
while rang < 51:
    print(rang)
    rang = rang + 1
    
for s in range(10):
    n = eval(input('Enter a number: '))
    if n<0:
        break

i = 0
num = 1
while i < 10 and num > 0:
    num = eval(input('Enter a number: '))"""
    
#String Concatination
print('AB' + 'CD')
print('A' + '7' + 'B')
print('a'+' '+'b')
    
"""s = ''
for i in range(10):
    t = input('Enter a letter: ')
    if t=='a' or t=='e' or t=='i' or t=='o' or t=='u':
        s = s + t
print(s)"""

print('Paul is a man ' + 'Obi is a boy ' + 'The box is big')

u = """This is a multy line comment, and it can also be used to 
    write bunch of text in form of a paragraph"""
print(u)

#string repitition
print('HH' * 4)
print("Hi, " * 3) 
print('Hello World ' * 6 + 'The sun is bright')

#indexing 
s = 'python programming'
print(s[-0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])

rr = 'functions'
print(rr[1:6])
print(rr[2:8])
print(rr[2:8:2])

for i in range(len(rr)):
    print(rr[i])
print(len(rr))

for c in rr:
    print(c)
    
rr = rr.upper()
print(rr)


p = 'PROGRAM'
d = p.lower()
c = p.replace('PROGRAM', 'Hello Program')
print(d)
print(c)
print(c.count('r'))
q = 'pppp\nccc\nffffff\nkkk'
print(q.count('p'))
print(q.count('c'))
print(q.count('f'))
print(q.count('k'))
print(q.count(' '))
print(q.isalpha())
print(q.index('c'))
print(q)

#List
print([7, 8, 9] + [3, 4, 5]) #list concatination
print([7, 8, 9]*3) #list repitition

L = ['trek', 'redline', 'specialized']
print(L[0])
L.append('honda')
print(L)

x = []
x.append('book')
x.append('bag')
x.append('box')
x.insert(1, 'brush')
x.insert(3, 'red')
x.insert(4, 'red')
x.insert(5, 'red')
x.remove('red')
x.remove('box')
z = x.pop()
n = x.pop()
j = x.pop()
print(x)
print('This item ' + z + ', ' + n + ', ' + j +', was removed from the list x')

box = ['L', 'L', 'L', 'P', 'P', 'K', 'M', 'J']
box.reverse()
box.sort(reverse=True)
brown = box.count('L')
black = box.index('L')
print(box)
print(len(box))
print(brown)
print(black)

m = ['book', 'brush', 'bag']
print(len(m))
print(min(m))
#print(max(m))

for magic in m:
    print(magic + ', Is an item in our list m')
    
dimension = ('twenty', '40')

print(set({1, 2, 3} | {3, 4}))
dope  = {1, 2, 3}
pope = {3, 4}
print(dope | pope)
print(dope & pope)
print(dope - pope)
print(dope ^ pope)
print(3 in dope)
dope.add(5)
pope.add(5)
dope.remove(1)
pope.remove(4)
print(dope)
print(pope)
print(dope.issubset(pope))
print(dope.issuperset(pope))

days = {'January':31, 'Febuary':28, 'March':31, 'April':30, 'May':31, \
    'June':30, 'July':31, 'August':31, 'September':30, 'October':31, \
        'November':30, 'December':31}

print(days)
print(days['January'])
print(days['September'])

D = {'A':100, 'B':200}
print(D)
D['A'] = 400
print(D)

"""k = {'dog':'has a tail and goes woof!',
     'cat':'says meow',
     'mouse':'chased by cats'
    }

for i in range(3):
    word = input('Enter a word between mouse, cat, dog: ')
    if word in k:
        print('The definition is: ', k[word])
    else:
        print('Word not in dictionary')
        
k2 = k.copy()
print(k2)

d1 = list(k)
d2 = list(k.values())
d3 = list(k.items())
print(d1)
print(d2)
print(d3)"""


"""from random import randint

secret_num = randint(1, 100)

for num_guess in range(5):
    guess = eval(input("Enter a number form 1- 100: "))
    if guess < secret_num:
        print('HIGHER', 4-num_guess, 'guesses left.\n')
    elif guess > secret_num:
        print('LOWER', 4-num_guess, 'guesses left.\n')
    else:
        print('you got it')
        break

else:
    print('you loose, The correct number is', secret_num)"""
    

def print_hello():
    print('Hello World')
    
def draw_box():
    print('*' * 15)
    print('*', ' '*11, '*')
    print('*', ' '*11, '*')
    print('*' * 15)

def hello(n):
    print('Hello World ' * n)
    
def concat(s, r, b, c=', it a brown ball'):
    print(s + r + b + c)
    
print_hello()
draw_box()
hello(5)
concat('This is a ', 'ball', ', it is big', ', it is black')

def num(n1, n2=5):
    print(n1 * n2)
    
num(5, 2)

def addi(y, z, q=5):
    global x
    x = 5
    return x * y + z * q

def multi(y, z):
    return x + y + z 
    
print(addi(10, 15))
print(multi(5, 10))

def glob(n):
    global w
    w = 3
    return n * 5 * w

def priv(y):
    return y + 5 + w

print(glob(5))
print(priv(5))

#Lambda function
#normal function
def f(x):
    return x * 2
print(f(5))

#Lambda function
g = lambda x : x * 2
print(g(5))

x2 = lambda a : a + 10
print(x2(10))

y1 = lambda a, b, c : a * b * c
print(y1(5, 6, 7))

#Using Lambda function with our nml function
def name(n):
    return lambda a : a * n

mydoubler = name(2)

print(mydoubler(11))

def sec(d):
    return lambda y : y * d

mytriplier = sec(3)

print(mytriplier(11))

#other topics
class Name:
    def __init__(self, first_name, last_name, middle_name):
        self.first = first_name
        self.last = last_name
        self.middle = middle_name
        
    def get_formatted_name(self):
        """Return a fool name, neatly formatted"""
        if self.middle:
            full_name = self.first + ' ' + self.middle + ' ' + self.last
        else:
            full_name = self.first + ' ' + self.last
        return full_name

    def build_person(self):
        person = {'first_name':self.first, 'last_name':self.last}
        return person
    
f5 = Name('Gabriel', 'Williams', 'Eshimoghe')

print(f5.get_formatted_name())
print(f5.build_person())


def day(days):
    if days:
        return days
    else:
        return 'days is not given'
    
print(day('Tuesday'))

class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    
    def minus(self):
        return self.a - self.b
    
e = Example(8, 6)
print(e.add())
print(e.minus())

class Calc:
    def __init__(self, a, b, c, d=9):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def mult(self):
        return self.a * self.b * self.c * self.d
    
    def div(self):
        return self.a / self.b / self.c / self.d
    
    def add(self):
        return self.a + self.b + self.c + self.d
    
    def sub(self):
        return self.a - self.b - self.c - self.d
    
v1 = Calc(8, 4, 5)
print(v1.mult())
print(v1.div())
print(v1.add())
print(v1.sub())

class Parent:
    def __init__(self, a):
        self.a = a
        
    def method1(self):
        return self.a * 2
    
    def method2(self):
        return self.a + '!!!'
    
class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def method3(self):
        return self.a + self.b
    
p = Parent('hi')
c = Child('five', 'bye')

print(p.method1())
print(p.method2())
print(c.method1())
print(c.method2())
print(c.method3())

class Elon_Musk:
    def __init__(self, d, e, f):
        self.d = d
        self.e = e
        self.f = f
        
    def m1(self):
        return self.d * self.e
    
    def m2(self):
        return '???' + self.d
    
    def m3(self):
        return self.f - self.e
    
class Mark(Elon_Musk):
    def __init__(self, d, e, f, g, h):
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        
    def m4(self):
        return self.g + self.h
    
    def m5(self):
        return self.h * 5
    
elon = Elon_Musk('Tesla', 8, 10)
mark = Mark('Facebook', 6, 8, 'Instagram', 'Thread')

print(elon.m1())
print(elon.m2())
print(elon.m3())
print()
print(mark.m1())
print(mark.m2())
print(mark.m3())
print(mark.m4())
print(mark.m5())

class Company:
    def __init__(self, name, description):
        self.names = name
        self.descr = description
        
    def name(self):
        return self.names
    
    def desc(self):
        return self.descr
    
class Year(Company):
    def __init__(self, name, description, year):
        self.names = name
        self.descr = description
        self.year = year
        
    def year_built(self):
        return self.year
    
class Owner(Year):
    def __init__(self, name, description, year, owner):
        self.names = name
        self.descr = description
        self.year = year
        self.owner = owner
        
    def founder(self):
        return self.owner
    
o = Owner('Tesla', 'an electric car company', '2021', 'elon musk')

print(o.name())
print(o.desc())
print(o.year_built())
print(o.founder())

#Exception 
try:
    a = eval(input('Enter a number: '))
    print(3/a)
except TypeError:
    print('unsupported data-type')
except NameError:
    print('Please enter a number.')
except ZeroDivisionError:
    print('Cant enter 0.')
print('Hi there')

try:
    b = eval(input('Enter a number: '))
    print(4/b)
except:
    print('A problem occurred')
else:
    print('No problem occurred')
    
try:
    c = 5/0
except Exception as e:
    print(e)
    
#import random #All the functions/methods of random
#from random import randint, choice #Specific functions/ methods of random
#from random import *

from functools import reduce
from random import randint
a = randint(1, 100)
print(a)

from time import time
start = time()
g1 = 5*5
print(g1)
print('It took', round(time() - start, 3), 'seconds.')

from datetime import datetime
d = datetime(1, 1, 1).now()
print(d)

#List Comprehension
L = [ i for i in range(5)]
print(L)

N = [n for n in range(1, 11)]
print(N)

string = 'Hello'
s = [c*2 for c in string]
print(s)

M = ['one', 'two', 'three', 'four', 'five', 'six']
m = [n[0] for n in M]
print(m)

s2 = 'Hi! This is a test'
print(s2.split())

m3 = 'This is a training of mind'
print(m3.split())

L1 = ['A', 'B', 'C']
print(''.join(L1))
print(' '.join(L1))
print(', '.join(L1))
print('***'.join(L1))

l1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(l1)

l2 = list(map(len, ['this', 'is', 'a', 'test']))
print(l2)

l3 = list(filter(lambda x: len(x)>2, ['this', 'is', 'a', 'test']))
print(l3)

from winsound import Beep
Beep(500,1000)

for namu in range(2, 10):
    if namu % 2 == 0:
        print("Found an even number", namu)
        continue
    print("Found a number", namu)
    
print("This string '{:>20s}', is a formatted string".format('There!'))
print("This integer '{:,d}', is a formatted string".format(1000000))
print("This float '{:^20f}', is a formatted string".format(365.50))

#printing 10 x 10 multiplication table
for loop in range(1, 11):
    for pool in range(1, 11):
        print('{:3d}'.format(loop*pool, end=' '))
    print()
  
for x in range(-50, 51):
    for y in range(-50, 51):
        if 2*x + 3*y == 4 and x-y == 7:
            print(x, y)
            
for j in range(1, 100):
    for k in range(1, 100):
        for l in range(1, 100):
            if j**2 + k**2 == l**2:
                print(j, k, l)
     

from string import punctuation

class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '')
        s = s.lower()
        self.words = s.split()
        
    def number_of_words(self):
        return len(self.words)    
    
    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)]==s])
    
    def number_with_length(self, n):
        return len([w for w in self.words if len(w)==n])
    
s = input('Enter some words: ')
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words: ', analyzer.number_of_words())
print('Number of words starting with "t": ', analyzer.starts_with('t'))
print('Number of words starting with "a": ', analyzer.starts_with('a'))
print('Number of 2-letter words: ', analyzer.number_with_length(2))
print('Number of 1-letter words: ', analyzer.number_with_length(1))

import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        names = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(names[self.value - 11], self.suit)

class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards
        
    def nextCard(self):
        return self.cards.pop(0)
    
    def hasCard(self):
        return len(self.cards)>0
    
    def size(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2, 15):
                self.cards.append(Card(v, s))
                
deck = Standard_deck()
deck.shuffle()

new_card = deck.nextCard()
print('\n', new_card)
choice = input("Higher (h) or lower (l): ")
streak = 0

while (choice=='h' or choice=='l'):
    if not deck.hasCard():
        deck = Standard_deck()
        deck.shuffle()
    
    old_card = new_card
    new_card = deck.nextCard()
    
    if (choice.lower()=='h' and new_card.value > old_card.value or \
        choice.lower()=='l' and new_card.value < old_card.value):
        streak = streak + 1
        print("Right! That's", streak, "in a row")
        
    elif (choice.lower()=='h' and new_card.value < old_card.value or \
        choice.lower()=='l' and new_card.value > old_card.value):
        streak = 0
        print('Wrong.')
        
    else:
        print('Push')
        
    print('\n', new_card)
    choice = input("Higher (h) or lower (l): ")