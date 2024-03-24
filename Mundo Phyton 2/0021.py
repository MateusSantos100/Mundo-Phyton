soma=0
media=0
maior=0
velho=0
mulher=0
for p in range(1,5):
    print('-----------------')
    nome=str(input('NOME: ')).strip()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO [M/F] : ')).strip().upper()
    soma+= idade
    if p == 1 and sexo in 'Mm':
        maior = idade
        velho=nome
    if sexo in'Mm' and idade > maior:
        maior= idade
        velho = nome
    if sexo in 'Ff' and idade <20:
        mulher +=1
media= soma/4
print('A média da idade do grupo é igual a {}'.format(media))
print('A Idade do mais velho é {} anos e se chama {}'.format(maior,velho))
print('O total de mulheres menos de 20 é {}'.format(mulher))