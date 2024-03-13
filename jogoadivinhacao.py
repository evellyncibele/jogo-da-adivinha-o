print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = 22

#Definindo o número de tentativas
numeroTentativas = 3

while(numeroTentativas > 0):
    print('Tentativa restante: ', numeroTentativas)

#Recebendo o chute do jogador
    chuteString = input('Digite um numero: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print('Você errou! o numero é menor')
    else:
        print('você errou! o numero secreto é mior')

    numeroTentativas = numeroTentativas - 1
