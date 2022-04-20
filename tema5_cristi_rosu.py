# b1
# def add_no(n1, n2):
#     sum = n1 + n2
#     return sum
#
#
# n1 = int(input('n1:'))
# n2 = int(input('n2:'))
# print(f'Suma celor doua numere este {add_no(n1, n2)}.')

# b2
# def even_odd(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# x = int(input('Numar intreg:'))
# q = even_odd(x)
# if q:
#     print(f'Numarul este par.')
# else:
#     print(f'Numarul este impar.')

# b3
# def caractere(nume, prenume, nume_mijlociu):
#     l = len(nume) + len(prenume) + len(nume_mijlociu)
#     return l
#
#
# nume = input('Nume:')
# nume_mijlociu = input('Nume mijlociu:')
# prenume = input('Prenume:')
# print(f'Lungimea numelui intreg este de {caractere(nume, prenume, nume_mijlociu)} caractere.')

# b4
# def aria_dreptunghi(x, y):
#     a = x * y
#     return a
#
#
# x = float(input('Lungime:'))
# y = float(input('Latime:'))
# print(f'Aria dreptunghiului este {aria_dreptunghi(x, y)}.')

# b5
# def aria_cerc(r):
#     from math import pi         #sau definim pi == 3.14159
#     a = pi * r**2
#     return a
#
#
# r = float(input('Raza:'))
# print(f'Aria cercului cu raza {r} este {aria_cerc(r)}.')

# b6
# def char_in_str(x):
#     if x in string:
#         return True
#     else:
#         return False
#
#
# string = str(input('String:'))
# x = str(input('Caracter:'))
# if char_in_str(x):
#     print(f'Caracterul "{x}" se gaseste in stringul "{string}".')
# else:
#     print(f'Caracterul "{x}" nu se gaseste in stringul "{string}".')

# b7
# def upper_lower(string):
#     x = sum(1 for l in string if l.lower())
#     y = sum(1 for u in string if u.isupper())
#     print(f'Nr de caractere lower case este {x}.')
#     print(f'Nr de caractere upper case este {y}.')
#
#
# string = str(input('String:'))
# upper_lower(string)

# b8
# def pos(x):
#     print(x)
#     nr_pos = [n for n in x if n >= 0]
#     print(f'Numerele pozitive din sir sunt:', *nr_pos)
#
#
# sir = [int(x) for x in input('Numere separate de space:').split()]
# pos(sir)

# b9
# def compare(x, y):
#     if x > y:
#         print(f'Primul numar {x} este mai mare decat al doilea numar {y}.')
#     elif y > x:
#         print(f'Al doilea numar {y} este mai mare decat primul numar {x}.')
#     elif x == y:
#         print(f'Numerele sunt egale.')
#
#
# x = int(input('Primul numar:'))
# y = int(input('Al doilea numar:'))
# compare(x, y)


# atat am apucat...
