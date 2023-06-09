bim1 = int(input('Nota primeiro bimestre: '))
while bim1 > 10:
    bim1 = int(input('Valor errado, informe novamente primeiro bimestre : '))
bim2 = int(input('Nota segundo bimestre: '))
while bim2 > 10:
    bim2 = int(input('Valor errado, informe novamente segundo bimestre : '))
bim3 = int(input('Nota terceiro bimestre: '))
while bim3 > 10:
    bim3 = int(input('Valor errado, informe novamente terceiro bimestre : '))
bim4 = int(input('Nota quarto bimestre: '))
while bim4 > 10:
    bim4 = int(input('Valor errado, informe novamente quarto bimestre : '))

media = (bim1 + bim2 + bim3 + bim4) / 4
if bim1 <= 10 and bim2 <= 10 and bim3 <= 10 and bim4 <= 10:
    print('Media: {}'.format(media))
else:
    print('Alguma nota foi digitada errada.')

# a = 0
# while a < 10:
#     print(a)
#     a += 1


# for num in range (101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)



# a = int(input('Informe um numero: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(a, x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('numero {} é primo: '.format(a))
# else:
#     print('número {} não é primo'.format(a))

# for x in range(1,101):
#     print(x)