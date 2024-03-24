from datetime import date
ano=int(input('Digite o ano do sue nascimento: '))
a=date.today().year -ano
if a <= 9:
    print('Sua idade é {} . Sua classificação é MIRIM'.format(a))
elif a <= 14:
    print('Sua idade é {} . Sua Clasificação é INFANTIL'.format(a))
elif a <= 19:
    print('Sua idade é {} . Sua classificação é JUNIOR'.format(a))
elif a <= 25:
    print('Sua idade é {} . Sua Classificação é SENIOR'.format (a))
else:
    print('Sua idade é {} . Sua Classificação é Master'.format(a))
