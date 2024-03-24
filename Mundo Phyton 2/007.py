reta1= float(input(' Qual o número da primeira reta: '))
reta2=float(input(' Qual o número da segunda reta: '))
reta3=float(input(' Qual o número da terceira reta: '))
if reta1 == reta2 == reta3:
    print('Elé é um Equilátero ,pois possuem os lados iguais')
elif reta1 != reta2 != reta3 != reta1:
    print('Ele é um Escaleno.')
else:
    print('Ele é um isósceles')
