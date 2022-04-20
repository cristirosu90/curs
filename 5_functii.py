# # functii
#
# # def f():
# #     print('===')
# #     print('yo!')
# #     print('===')
# #
# # for i in range(3):
# #     f()
# ###
#
# # def f(x):
# #     print(x + 3)
# #
# #
# # a = int(input('a='))
# # f(a)
# ###
# # def avg(l):
# #     s = 0
# #     for i in range(len(l)):
# #         s = s + l[i]
# #     a = s / len(l)
# #     print(a)
# #
# #
# # l = [4, 5, -5, 0, 9, 15, 19, -21]
# ###
#
# # def avg(l):
# #     s = 0
# #     for i in range(len(l)):
# #         s = s + l[i]
# #     a = s / len(l)
# #     return a
# #
# #
# # l = [4, 5, -5, 0, 9, 15, 19, -21]
# # y = avg(l)
# # print(f'Media aritmentica a valorilor din lista este {y}.')
# ###
# # def val_max(l):
# #     v_max = l[0]
# #     for i in range(len(l)):
# #         if l[i] > v_max:
# #             v_max = l[i]
# #     print(v_max)
# #     return v_max
# #
# #
# # l = [-4, -5, -5, -9, 15, -19, -21]
# # val_max(l)
# ###
#
#
def ptg(c1, c2, ip):
    if ip**2 == c1**2 + c2**2:
        #print('Triunghiul este dreptunghic.')
        return True
    else:
        #print('Triunghiul nu este dreptunghic.')
        return False


cat1 = int(input('Prima cateta:'))
cat2 = int(input('A doua cateta:'))
ip = int(input('Ipotenuza:'))
rez = ptg(cat1, cat2, ip)
if rez == True:
    print('Triunghiul este dreptunghic.')
else:
    print('Triunghiul nu este dreptunghic.')
# ###
#
# def strmultiplier(s, n):
#     return s * n
#
#
# sir  = str(input(' '))
# num = int(input(' '))
# print(strmultiplier(sir, num))
#
