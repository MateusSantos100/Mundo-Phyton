print('{:^40}'.format('Lojas Mateus'))
compra=float(input('Qual o Valor do Produto: R$ '))
print('Escolha a forma de Pagamento: \n1 para dinheiro \n2 para cartão\n'
      '3 para cartão em 2x \n4 para cartão em 3x ou mais')
pagar= int(input('Qual a sua forma de pagamento: '))

if pagar == 1:
    a= compra- (compra*10/100)
    print('A compra no valor de R${} ficou a R${:.2f},pois pagou em dinheiro e recebeu 10% de desconto'.format(compra,a))
elif pagar == 2:
    b= compra - (compra*5/100)
    print('A compra no valor de R${} ficou a R${:.2f},pois pagou em cartão a vista e recebeu 10% de desconto'
          .format(compra,b))
elif pagar == 3:
    c=compra/2
    print('A compra no valor de R${} ficou em 2x de R${:.2f} no cartão'.format(compra,c))
elif pagar==4:
    parcela=int(input('Digite quantas vezes no cartão: '))
    d= compra + (compra*20/100)
    t= d/parcela
    print('A compra no valor de R${} ficou em {}x de R${:.2f},pois pagou em cartão e recebeu 20% de juros'
          .format(compra,parcela,t))
else:
    print('\033[1:35m Opção inválida de Pagamento')