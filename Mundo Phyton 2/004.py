from datetime import date
ano=int(input('Qual o ano do seu nascimento? '))
a = date.today().year - ano
if a == 18 :
    print('Já está na hora de se alistar.')
elif a < 18:
    b= 18-a
    print('Você ainda não precisa se alistar , falta {} ano(s) para isso'.format(b))
else:
    c= a-18
    print('Você já passou {} ano(s) do tempo de alistamento'.format(c))

