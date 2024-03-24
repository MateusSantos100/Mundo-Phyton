nota1=float(input('Digite a nota da sua AP1: '))
nota2=float(input('Digite a nota da sua AP2: '))
media= (nota1 + nota2) /2
if media < 5:
    print('VocÊ esta reprovado , pois sua média ficou {:.1f}.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você está de recuperação, pois sua média foi {:.1f}.'.format(media))
else:
    print('Você está aprovado!. Sua média foi {:.1f}'.format(media))
