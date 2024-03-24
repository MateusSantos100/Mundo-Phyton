num=int(input('Digite um número: '))
soma=0
for c in range (1,num+1):
    if num % c ==0:
      print('\033[35m' ,end=' ')
      soma+= 1
    else:
      print('\033[33m' ,end =' ')
    print('{}'.format(c) , end=' ')
print('\n \033[31m O número {} foi divisivel {} vezes'.format(num,soma))
if soma==2:
    print('\033[32m Ele é Primo')
