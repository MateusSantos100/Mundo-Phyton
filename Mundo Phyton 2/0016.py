primeiro = int(input('Digite o Promeiro Termo: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c) , end= (' - '))
print('FIM')
