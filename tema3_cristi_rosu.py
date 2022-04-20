# b1

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
print(list(reversed(note_muzicale)))
print()

#b2
do = 'do'
count_do = note_muzicale.count(do)
print(f'do apare de {count_do} ori')
print()

#b3
y = [3, 1, 0, 2]
z = [6, 5, 4]
yz = y + z
yz1 = [*y, *z]
print(yz)
print(yz1)
print()

#b4
yz.sort()
print(yz)
print()

#b5
if len(yz) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')
print()

#b6
yz.clear()

#b7
if len(yz) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')
print()

#b8
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(dict1.keys())
print()

#b9
Ana = dict1.get('Ana')
print(f'Ana a luat nota {Ana}.')
Gigel = dict1.get('Gigel')
print(f'Gigel a luat nota {Gigel}.')
Dorel = dict1.get('Dorel')
print(f'Dorel a luat nota {Dorel}.')
print()

#b10
dict1['Dorel'] = 6
Dorel = dict1.get('Dorel')
print(f'Dorel a luat nota {Dorel}.')
print()

#b11
dict1.pop('Gigel')
dict1.update({'Ionica': 9})
print(dict1)
print()

#b12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
print()

#b13
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din saptamana.')
else:
    print('Weekend nu este un subset al zilelor din saptamana.')
print()

#b14
print(f'Diferentele dintre cele doua seturi sunt: {set(zile_sapt) ^ set(weekend)}')
print()

#b15
print(f'Intersectia elementelor din cele doua seturi este: {set(zile_sapt) and set(weekend)}')
print()
