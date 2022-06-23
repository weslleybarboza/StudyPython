# lista = [1, 3, 15, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
# print(type(lista))
# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)
#
# soma = 0
# for x2 in lista:
#     print(x2)
#     soma += x2
# print(soma)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(min(lista_animal))
# print(max(lista_animal)) #busca pela ordem alfabética
if 'lobo' in lista_animal:
    print('Gato encontrado')
else:
    print('Não encontrado')
    lista_animal.append('lobo')
    print(lista_animal)