altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
imc= peso/(altura**2)
if imc < 18.5:
    print('O seu IMC é {:.1f} Kg/m².Você está abaixo do peso'.format(imc))
elif imc >=18.5 and imc <=25:
    print('O seu IMC é {:.1f} Kg/m². Você está no peso ideal'.format(imc))
elif imc >25 and imc <=30:
    print('O seu IMC é {:.1f} Kg/m² .Você está no Sobrepeso.'.format(imc))
elif imc >30 and imc <=40:
    print ('O seu IMC é {:.1f} Kg/m² . Você está com Obesidade.'.format(imc))
else:
    print('O seu IMC é {:.1f} Kg/m². Você está com Obesidade Mórbita'.format(imc))


