# b1
'''O variabila este un "recipient" virtual care poate contine
o valoare de un anumit tip,
valoare care poate fi schimbata.'''

# b2
a = 'variabila'
b = 13
c = 13.37
d = True
print()

# b3
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

# b4
print(round(c))
print(type(round(c)))
print()

# b5

print(f'Variabila "{a}" este string.')
print(f'Variabila "{b}" este integer.')
print(f'Variabila "{c}" este float.')
print(f'Variabila "{d}" este boolean.')
print()

# b6
nume = input('Nume:')
prenume = input('Prenume:')
x1 = len(nume + prenume)
print(f'Numele complet are {x1} caractere.')
print()

# b7
L = int(input('Lungime:'))
l = int(input('Latime:'))
print(f'Aria dreptunghiului este {L * l}.')
print()

# b8
e = 'Coral is either the stupidest animal or the smartest rock.'
x = input('x:')
x = int(x)  # must define, else string
length = len(e)
# print(len(e))
print(e[0:length - x])
print()

# b9
e = 'Coral is either the stupidest animal or the smartest rock.'
print(e[0:5] + e[-6:-1])
print()

# b10
e = 'Coral is either the stupidest animal or the smartest rock.'
the = ' the '
count_the = e.count(the)
print(f'Cuvantul "the" apare de {count_the} ori.')

'''def word_count(str):
   counts = dict()
   words = str.split()

   for word in words:
       if word in counts:
           counts[word] += 1
       else:
           counts[word] = 1

   return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))'''

print()

# b11
e = 'Coral is either the stupidest animal or the smartest rock.'
the_upper = ' THE '
print(e.replace(the, the_upper))
print()

# b12
e = 'Coral is either the stupidest animal or the smartest rock.'
rock = e.index('rock')
print(f'"rock" start index is {rock}')
print(e[0:53])
print()

# b13
# a = 'variabila'
# b = 13
# c = 13.37
# d = True
# y = a, b, c, d
# y = y.replace("'", " ")
# print(str(y))

# b14
num = '0123456789'
print(num[1:9:2])
print()

# c15
f = '0123456789'
# f = int(f)
assert f == int(f), 'Only numbers are allowed.'
print('This string only contains numbers.')

# c16
m = input('String de dimensiune impara:')
length = len(m)
mid = length // 2
print(m[mid])
print()

# c17

n = input('Multiple word string:')

# c18
q = input('String:')
q1 = q[0]
q11 = q1.capitalize()
for q1 in q:
    print(q11)
