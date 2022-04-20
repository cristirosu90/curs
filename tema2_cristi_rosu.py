# b1
'''if/else permite verificarea unor conditii si executarea programului in functie de rezultatul verificarilor'''

# b2
x = int(input('x:'))
if x >= 0:
    print('x - pozitive')
else:
    print('invalid')
print()

# b3
x = int(input('x:'))
if x >= 0:
    print('x - pozitive')
elif x == 0:
    print('x=0')
else:
    print('x - negative')
print()

# b4
x = int(input('x:'))
if -2 <= x <= 13:
    print('valid')
else:
    print('invalid')
print()

# b5
x = int(input('x:'))
y = int(input('y:'))
if x - y < 5:
    print('valid')
else:
    print('invalid')
print()

# b6

x = int(input('x:'))
if not(5 < x < 27):
    print('valid')
else:
    print('invalid')
print()

# b7

x = int(input('x:'))
y = int(input('y:'))
if x == y:
    print('equal')
elif x < y:
    print('y is greater')
else:
    print('x is greater')
print()

# b8

x = int(input('x:'))
y = int(input('y:'))
z = int(input('y:'))
if x == y and x == z and y == z:
    print('equilateral')
elif x == y or x == z or y == z:
    print('isosceles')
else:
    print('scalene')
print()

# b9

import string
a = input('letter:')
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # fara asta output = 'a, 'is a consonant'' pt a = [0,...,9] bcs of  len(a) > 1 condition
if type(a) == int or type(a) == float or len(a) == 0 or len(a) > 1 or a in numbers or a in string.punctuation:
    print('please type a letter')
    #
elif a in vowels:
    print(a, 'is a vowel')
else:
    print(a, 'is a consonant')
print()

# b10
x = float(input('Nota RO:'))
if type(x) == str or x < 0 or x > 10: # to be resolved
    print('N/A')
elif 8 < x <= 9:
    print('Nota SUA: B')
elif 7 < x <= 8:
    print('Nota SUA: C')
elif 6 < x <= 7:
    print('Nota SUA: D')
elif 4 < x <= 6:
    print('Nota SUA: E')
elif 0 < x <= 4:
    print('Nota SUA: F')
elif 9 < x <= 10:
    print('Nota SUA: A')
print()

# b11
x = input('x:')
if len(x) >= 4:
    print(x, 'has at least four digits')
else:
    print(x, 'does not have at least four digits')
print()

# b12
x = int(input('x:'))
if type(x) == str:
    print('please input an integer')
elif len(str(x)) == 6:
    print(x, 'has exactly six digits')
elif len(str(x)) < 6 or len(str(x)) > 6:
    print(x, 'does not have exactly six digits')
print()

# b13

x = int(input('x:'))
if x % 2 == 0:
    print('x is an even number')
else:
    print('x is an odd number')
print()

# b14 ?

# b15

x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
if (x + y + z == 180) and not (x == 0 or y == 0 or z == 0):
    print('triangle')
elif x > 0 and y > 0 and z > 0:
    print('invalid angles')
else:
    print('invalid angles')
print()

# b16 n-am apucat, dar voi incerca
