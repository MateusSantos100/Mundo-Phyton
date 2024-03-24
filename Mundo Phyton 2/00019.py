from datetime import date
a= date.today().year
maior=0
menor=0
for c in range (1, 8):
    ano=int(input('Digite o ano de nascimento da  [{}ª] pessoa: '.format(c)))
    s= date.today().year - ano
    if s >= 21:
        maior += 1
    elif s < 21:
        menor+= 1
print('TENHO {} DE PESSOAS MAIORES DE IDADE'.format(maior, end=(' ')))
print('TENHO {} DE PESSOAS MENORES DE IDADE'.format(menor))
