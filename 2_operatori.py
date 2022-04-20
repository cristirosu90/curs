# # media
# x = int(input('Nota_1:'))
# y = int(input('Nota_2:'))
# z = int(input('Nota teza:'))
# media_parcurs = (x +y ) /2
# media_teza = (media_parcurs * 3 + z) / 4
# print(f"Media: {media_teza}")
#
# # if/else
# nota_trecere = 5
# if media_teza >= nota_trecere:
#     print('Ai promovat!')
# else:
#     print('Ne pare rau!')
#
# # elif
#
# numar = int(input())
# if numar>0:
#     print('pozitiv')
# elif numar<0:
#     print('negativ')
# else:
#     print('nul')

# op
a = int(input('a:'))
b = int(input('b:'))
op = input('operator:')
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
# elif op == '/':
#     if b == 0:
#         print('b este zero!')
#     else:
#         print(a / b)
elif op == '/' and b == 0:
    print('b este 0!')
else:
    print(a / b)
