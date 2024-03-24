n1=int(input('Digite um número: '))
n2=int(input('Digite um segundo número: '))
if n1> n2:
    print('\033[0:35mO Primeiro número {} é maior que o Segundo {}.'.format(n1,n2))
elif n2> n1:
    print('O segudo número {} é maior que o primeiro {}.'.format(n2,n1))
else:
    print('Os dois números são iguais')
