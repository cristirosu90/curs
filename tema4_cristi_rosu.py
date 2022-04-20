# b1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for elem in range(len(masini)):
#     print(f'Masina mea preferata este {masini[elem]}.')
# print('======================================')
# for elem1 in masini:
#     print(f'Masina mea preferata este {elem1}.')
# print('======================================')
# index = 0
# while index < len(masini):
#     elem2 = masini[index]
#     print(f'Masina mea preferata este {elem2}.')
#     index += 1
# print()

#b2
for i in range(len(masini)):
    if 0 < i < len(masini)-1:
        masini[i] = masini[i].upper()
#     # if i == 0:
#     #     masini[i] = masini[i].upper()
#     # elif i == len(masini)-1:
#     #     masini[i] = masini[i].upper()
else:
    print(masini)


# i = 1
# while i < len(masini)-1:
#     masini[i] = masini[i].upper()
#     i += 1
# print(masini)

#b3
