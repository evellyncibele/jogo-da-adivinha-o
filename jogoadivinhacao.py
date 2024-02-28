print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 22


chuteString = input('Digite um número')

print('Você digitou o número', chuteString)

#chute = int(chuteString)

if numeroSecreto == chute:
    print('Você acertou!')
elif(chute>numeroSecreto):
    print('Você errou! o numero é menor')
else:
    print('você errou! o numero secreto é mior')
