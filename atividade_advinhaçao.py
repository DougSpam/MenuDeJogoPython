import random

def jogo():


    print('-=-' * 7)
    print('Bem vindo ao jogo!')
    print('-=-' * 7)
    print('Você tera 500 pontos iniciais, \npara cada diferença de valor do numero secreto\nsera diminuido do seus pontos\nquem acumular mais pontos, vence!')
    print('-=-' * 7)

    num_secreto = random.randint(1 , 100 ) #randomizar um numero
    total_de_tentativas = 0 
    pontos = 500
    tentativa = 1

    print(f'Qual nivel de dificuldade?') #opçoes de dificuldade
    print('[ 1 ] Facil\n[ 2 ] Medio\n[ 3 ] Dificil')

    dificuldade = int(input('Defina o nivel: ')) #definir nivel de dificuldade
    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    else:   
        total_de_tentativas = 5

    for tentativa in range(1 , total_de_tentativas + 1): #repitaçao das tentativas
        print(f'Tentativa {tentativa} de {total_de_tentativas}')
        jogador = int(input('Digite um numero entre 1 e 100: '))
        acertou = jogador == num_secreto
        maior = jogador > num_secreto
        print(f'Voce digitou: {jogador}')

        if jogador < 1 or jogador > 100 : #nao escolher menor q 1 , nem maior q 100
            print('Você so pode digitar um numero entre 1 e 100!')
            continue
        if acertou:
            print(f'Você acertou, e fez {pontos} pontos!')
            break
        else:
            if maior: #chutou maior o numero
                print('Você errou!, você chutou um numero maior do que o secreto')
                if tentativa == total_de_tentativas:
                    print(f'o numero secreto era {num_secreto}, e você fez no total {pontos}pontos!')
            else:       #chutou menor o numero!
                print('Você errou!, você chutou um numero menor do que o secreto')
                if tentativa == total_de_tentativas:
                    print(f'o numero secreto era {num_secreto}, e você fez no total {pontos}pontos!')
                pontos_perdidos = abs(num_secreto - jogador) #diferença ( perdas )
                pontos = pontos - pontos_perdidos

    print('Fim do jogo!')

if __name__ == '__main__':
    jogo()
