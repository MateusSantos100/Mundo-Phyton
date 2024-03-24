soma = 0
cont = 0
for c in range (1, 7):
    n1=int(input('Digite o {} número: '.format(c)))
    if n1 %2 ==0:
        soma= n1 + soma
        cont= cont+ 1
print('Você informou {} números pares e a soma dos valores é {}'.format(cont,soma))
