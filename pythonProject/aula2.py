a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print('Valor entrada a: {VarA}'
      '\nValor entrada b: {VarB}'.format(VarA = a, VarB = b))
soma = a + b
multiplicacao = a * b
divisao = b / a
resto = a % b

print(
    'Soma = {soma}'
    '\nMultiplicacao = {multip}'
    '\nResto = {rest}'
    '\nDivisão = {divi}'.format(soma = soma,
                                        multip = multiplicacao,
                                        divi = divisao,
                                        rest = resto)
)