num=int(input('Digite um número inteiro: '))
print('Agora escolha a Base de Conversão: \n1 Para Binário. \n2 Para Octal \n3 Para Hexadecimal')
base=int(input('Escolha a base de conversão: '))
bi=bin(num)
o= oct(num)
h= hex(num)
if base == 1:
    print('O número {} em binário fica {}'.format(num,bi[2:]))
elif base == 2:
    print('O número {} em octagonal fica {}' .format(num,o[2:]))
elif base ==3:
    print('O número {} em Hexadecimal fica {}'.format(num,h[2:]))
else:
    print('informação errada')
