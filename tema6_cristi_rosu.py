# b1

# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Cercul {self.culoare} are raza {self.raza}.')
#
#     def aria(self):
#         from math import pi
#         a = pi * self.raza**2
#         return a
#
#     def diametru(self):
#         d = 2 * self.raza
#         return d
#
#     def circumferinta(self):
#         from math import pi
#         c = 2 * pi * self.raza
#         return c
#
# cerc1 = Cerc(5, 'albastru')
# #cerc1.descrie_cerc()
# print(f'{cerc1.descrie_cerc()} are aria {cerc1.aria()}, diametrul {cerc1.diametru()}, si circumferinta {cerc1.circumferinta()}.') #pending further investigation
# cerc2 = Cerc(4.2, 'verde')
#
# b2

# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f'Dreptunghiul {self.culoare} are lungimea {self.lungime} si latimea {self.latime}.')
#
#     def aria(self):
#         a = self.lungime * self.latime
#         return a
#
#     def perimetrul(self):
#         p = (self.lungime + self.latime) * 2
#         return p
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
# # dreptunghi1 = Dreptunghi(5, 7, 'rosu', 'alb')
# # dreptunghi1.descrie()
# # print(dreptunghi1.aria())
# # print(dreptunghi1.perimetrul())
# # dreptunghi1.schimba_culoarea()
# # dreptunghi1.descrie()
#
#
# dreptunghi2 = Dreptunghi(17, 3.5, 'roz',)
# dreptunghi2.descrie()
# print(f'Aria dreptunghiului {dreptunghi2.culoare} este {dreptunghi2.aria()}.')
# print(f'Perimetrul dreptunghiului {dreptunghi2.culoare} este {dreptunghi2.perimetrul()}.')
# dreptunghi2.schimba_culoarea('negru')
# dreptunghi2.descrie()

# b3

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print('Angajat:')

    def nume_complet(self):
        nume_complet = self.nume + ' ' + self.prenume
        return nume_complet

    def salariu_lunar(self):
        print(f'Salariu lunar: {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariu anual: {salariu_anual}')

    def marire_salariu(self):
        marire_salariu = 100 * 1000 / self.salariu
        return str(marire_salariu) + '%'


angajat1 = Angajat('Popescu', 'Ion', 2500)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu()
print(f'Angajatul {angajat1.nume_complet()} va primi o marire de {angajat1.marire_salariu()}.')
#
#
#
#
#
#
# class Factura:
#     serie = 'F'
#     def _init_(self, serie, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume.produs
#         self.numar_produs = numar_produs
#         self.cantitate = cantitate
#
#     def schimba_cantitatea(self):
#         self.schimba_cantitatea = int(input('Cantitate:'))
#         self.cantitate = self.schimba_cantitatea
#
#     def schimba_pretul(self):
#         self.schimba_pretul = int(input('Pret:'))
#         self.pret
