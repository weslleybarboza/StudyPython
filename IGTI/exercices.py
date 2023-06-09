#dicionario: chave:valor

cardapio = {"salada":20, "suco":5, "sorvete":10, "refrigerante":5}
print(cardapio)

cardapio.keys()
cardapio["salada"] = 30
cardapio["novo"]=5

dic = {}
dic["ana"] = 18
dic["jose"] = 23

tempo = {}
tempo["dias_da_semana"] = "segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"
tempo["meses"] = "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"

type(tempo["dias_da_semana"])

calendario = {}
calendario["meses"] = {}
calendario["meses"]["janeiro"] = 1
calendario["meses"]["fevereiro"] = 2

names = {
    "maria":18,
    "weslley":34,
    "jose":23
}

sorted(names)
dict(sorted(names.items()))
sorted(names.items(), key= lambda x:x[0], reverse=True)


#listas - podemos alterar o valor

lista = [1, 2, 3, 4, 5, 6, -1, -2, -3]
type(lista)
len(lista)

lista[3]

lista[2] = 200
print(lista[2])

lista.pop()
lista.reverse()
lista.insert(10, 398)
lista.remove(1)
lista.sort()
lista.sort?
lista.sort(reverse=True)

lista.append("ana")

1 in lista

lista = lista + [54, 43, 32, 12, 78]
lista.remove("ana")
lista.remove('')
lista.append([98, 97, 90, 43])
lista.extend([43,56, 12, 21, 45])
lista.append([11,22,33,44])
lista[-1]
lista[-7].append("JOSE")


lista2 = ["segunda",1,  "terça", 2, "quarta", 4, 5, "quinta", "sexta",7,  "sabado", "domingo"]

[dia for dia in lista2 if type(dia) == str]


#range

range?

intervalo = range(1, 10)
type(intervalo)
len(intervalo)

#para visualizar é necessário colocar no tipo que possibilita ver
list(intervalo)
tuple(intervalo)
set(intervalo)

#tuplas - imutaveis


#funcoes

def imc (altura, peso):
    imc = round( peso / altura**2, 1)
    print(f"seu imc é {imc}")

def imc_retorno (altura, peso):
    imc = round( peso / altura**2, 1)
    return imc

imc_retorno(1.81, 78)
imc(1.81, 78)


# parametros magicos
# *args
def funcao_teste (param, *args):
    print("Parametro normal", param)
    print("Parametro args", args)

funcao_teste("primeiro")
funcao_teste("primeiro", "segundo", "terceiro", "quarto")

# **kwargs
def funcao_teste2 (param, **kwargs):
    print("Parametro normal", param)
    print("Parametro args", kwargs)

funcao_teste2("primeiro")
funcao_teste2("primeiro", param1="segundo", param2="terceiro", param3="quarto")

#lambda - funcoes anonimas

soma = lambda x:x+10
soma(4)


invert = lambda x:x[::-1]
invert([3,4,5])
invert({1,2,3})
invert((1,2,3))
invert("weslley")


#datetime

import datetime as dt
# from datetime import date, timedelta as dt

data_now = dt.datetime.now()
data_now.hour
data_now.minute
data_now.day
data_now.second
data_now.microsecond
data_now.year
data_now.resolution
data_now.month
data_now.tzinfo
data_now.timestamp()
data_now.weekday()
data_now.isoweekday()
data_now.isoformat(sep='T', timespec='seconds')

dt.datetime.strftime(data_now, '%d/%m/%Y %H:%M:%S')
print(type(data_now))

mes = lambda x:x.strftime("%B")
mes(data_now)

data_now - dt.timedelta(10)


#map

map?


def convert_celsius_to_fa(temp):
    result = round((float(9)/5)*temp + 32, 2)
    return result
    # print(result)

convert_celsius_to_fa(23)

temperaturas = [22, 34, 12, 1, 6, 30, 23]
lista = map(convert_celsius_to_fa, temperaturas)
list(lista)

conversao = lambda temp: round((float(9)/5)*temp + 32, 2)
list(map(conversao, temperaturas))

#reduce

from functools import reduce
import operator as op

reduce?
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
reduce(op.add, [1, 2, 3, 4, 5])


#list comprehension

temperaturas2 = [23, 26, 28, 30, 32, 34, 36, 38]

#sem condicoes
[convert_celsius_to_fa(temp) for temp in temperaturas2]

#com condicoes
[convert_celsius_to_fa(temp) for temp in temperaturas2 if convert_celsius_to_fa(temp) > 20]

#dict comprehension

cardapio = {"salada":20, "suco":3, "sorvete":5, "refrigerante":2}
{item:round(cardapio[item]*1.2,2) for item in cardapio}


#desafio

numeros = list(range(1, 1001))

# max([div for div in range(1,11) if 10%div == 0])

{num:max([div for div in range(1,11) if num%div == 0]) for num in numeros}

#enumerate

enumerate?

elista1 = ["a", "b", "c"]
enumerate(elista1)
list(enumerate(elista1))


list(enumerate(elista1, start=5))

meses = "janeiro", "fevereiro", "março", "abril", "maio", "junho"

for index, mes in enumerate(meses, start=1):
    print("Mes", mes, "é o ", index)


#excessoes

numeros = [1,2,3,4,5]
len(numeros)
numeros[5]

#try except

try:
    print(numeros[5])
except:
    print("falhou, esse é um erro generico")
print('continuando')


try:
    print(numeros[5])
except Exception as e:
    print("falha:", e)
print('continuando')



arquivos = [("arq1", 20), ("arq2", 10), ("arq3", 0), ("arq4", '15')]
def calcula(arqs):
    resultados = list()
    for arq_name, arq_valor in arqs:
        try:
            resultado = 100 / arq_valor
        except Exception as e:
            resultado = 0
            msg = "Erro - {} está com valor inesperado: {}".format(arq_name, e)
            print(msg)
        resultados.append((arq_name, resultado))
    return resultados
print(calcula(arquivos))


def calcula(arqs):
    resultados = list()
    for arq_name, arq_valor in arqs:
        msg = ''
        try:
            resultado = 100 / arq_valor
        except ZeroDivisionError:
            resultado = -999
            msg = "Erro - {} está com divisao por zero.".format(arq_name) 
        except TypeError:
            resultado = -999
            msg = "Erro - {} o tipo do valor esta errado.".format(arq_name) 
        except Exception as e:
            resultado = 0
            msg = "Erro - {} está com valor inesperado: {}".format(arq_name, e)
        print(msg)
        resultados.append((arq_name, resultado))
    return resultados
print(calcula(arquivos))

#try/except/finally

def calcula(arqs):
    resultados = list()
    for arq_name, arq_valor in arqs:
        try:
            resultado = 100 / arq_valor
        except ZeroDivisionError:
            arq_valor = 1
            resultado = 100 / arq_valor
            msg = "{} Atenção: Valor 0 alterado para 1 , não é possível divisao por zero.".format(arq_name) 
        except TypeError:
            arq_valor = int(arq_valor)
            resultado = 100 / arq_valor
            msg = "{} Atenção: o tipo do valor foi alterado para int, o tipo estava errado.".format(arq_name) 
        except Exception as e:
            resultado = 0
            msg = "{} Erro desconhecido: {}".format(arq_name, e)
        else:
            msg = "{} processado.".format(arq_name)
        finally:
            print(msg)
            resultados.append((arq_name, round(resultado,2)))
    return resultados
print(calcula(arquivos))


