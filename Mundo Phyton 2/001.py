casa= float(input('Qual o Valor da Sua casa?' ))
salario= float(input('Qual o valor do seu salário? '))
anos= float(input('Quantos anos vc pretende pagar? '))
parcela = casa/(anos*12)
if parcela >= salario*30/100:
    print('Empréstimo Negado!')
else:
    print('Parabéns!! Sua parcela será de {:.2f}'.format(parcela))

