bim1 = int(input('Nota primeiro bimestre: '))
if bim1 > 10:
    bim1 = int(input('Valor errado, informe novamente primeiro bimestre : '))
bim2 = int(input('Nota segundo bimestre: '))
if bim2 > 10:
    bim2 = int(input('Valor errado, informe novamente segundo bimestre : '))
bim3 = int(input('Nota terceiro bimestre: '))
if bim3 > 10:
    bim3 = int(input('Valor errado, informe novamente terceiro bimestre : '))
bim4 = int(input('Nota quarto bimestre: '))
if bim4 > 10:
    bim4 = int(input('Valor errado, informe novamente quarto bimestre : '))

media = (bim1 + bim2 + bim3 + bim4) / 4
if bim1 <= 10 and bim2 <= 10 and bim3 <= 10 and bim4 <= 10:
    print('Media: {}'.format(media))
else:
    print('Alguma nota foi digitada errada.')

# bim1 = int(input('Nota primeiro bimestre: '))
# bim2 = int(input('Nota segundo bimestre: '))
# bim3 = int(input('Nota terceiro bimestre: '))
# bim4 = int(input('Nota quarto bimestre: '))
#
# media = (bim1 + bim2 + bim3 + bim4) / 4
# if bim1 <= 10 and bim2 <= 10 and bim3 <= 10 and bim4 <= 10:
#     print('Media: {}'.format(media))
# else:
#     print('Alguma nota foi digitada errada.')

# a = int(input('Entre com primeiro valor: '))
# b = int(input('Entre com segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Um dos valores informados é par')
# else:
#     print('Nenhum numero par digitado')

# a = int(input('Entre com primeiro valor: '))
# b = int(input('Entre com segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Um dos valores informados é par')
# else:
#     print('Apenas numeros impares')

# a = int(input('Informe o valor a: '))
# b = int(input('Informe o valor b: '))
# c = int(input('Informe o valor c: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior numero é {}'.format(b))
# else:
#     print('o maior numero é {}'.format(c))
# print('final do programa')
