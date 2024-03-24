frase=str(input('Digite uma Frase: ')).strip().upper()
n= frase.split()
junto=''.join(n)
inverso= ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} junto é {}'.format(junto, inverso))
if inverso == junto:
    print('Ele ´um palindromo')
else:
     print('Não é um palindromo')