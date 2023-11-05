import random
from time import sleep
def jogo():

    iniciar_jogo()

    palavra = aleatorizar()

    letras_acertadas = inicia_letras(palavra)

    print(letras_acertadas)
    print('-=-' * 10)

    enforcou = False
    acertou = False
    tentativa = 0

    while not enforcou and not acertou:
        jogada = jogada_do_jogador()
    
        if jogada in palavra:
            marca_acertos(letras_acertadas,palavra,jogada)
        
        else: #erros do jogador
            tentativa += 1
            desenha_forca(tentativa)
        
        enforcou = tentativa == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        
    if acertou:
        mensagem_ganhou()
    else:
        sleep(1)
        mensagem_perdeu(palavra)

    print('Fim do jogo!')

#construçao


def iniciar_jogo():
    print('-=-' * 7)
    print('Bem vindo ao jogo!')
    print('-=-' * 7)

def aleatorizar():
    with open('palavras.txt', 'r' , encoding='utf=8') as arquivo: #aleatorizar as palavras, trazendo as palavra de outro arquivo
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper() #sorteio aleatorio de palavras
    return palavra

def inicia_letras(palavra):
    return ['_' for letra in palavra]

def jogada_do_jogador():
    jogada = input('Qual a letra desejada? ').upper().strip()
    print('Jogando...')
    return jogada

def marca_acertos(letras_acertadas,palavra,jogada):
    posiçao = 0
    for letra in palavra: #busca a letra na palavra!
        if jogada == letra:
            letras_acertadas[posiçao] = letra #letra no final pois a variavel setada para a letra que o jogador jogar é 'Letra'
        posiçao += 1

def desenha_forca(tentiva):
    print("  _______     ")
    print(" |/      |    ")

    if(tentiva == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentiva == 2):
        print(" |      (_)   ")
        print(" |      |     ")
        print(" |            ")
        print(" |            ")

    if(tentiva == 3):
        print(" |      (_)   ")
        print(" |      ||   ")
        print(" |            ")
        print(" |            ")

    if(tentiva == 4):
        print(" |      (_)   ")
        print(" |      |||   ")
        print(" |            ")
        print(" |            ")

    if(tentiva == 5):
        print(" |      (_)   ")
        print(" |      |||   ")
        print(" |       |    ")
        print(" |            ")

    if(tentiva == 6):
        print(" |      (_)   ")
        print(" |      |||   ")
        print(" |       |    ")
        print(" |      |     ")

    if (tentiva == 7):
        print(" |      (_)   ")
        print(" |      |||   ")
        print(" |       |    ")
        print(" |      | |   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_ganhou():
    print("\033[33mParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \033[m")


def mensagem_perdeu(palavra):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era \033[31m{palavra}")
    print("    _______________         ")
    print("   |               |       ")
    print("  |                 |      ")
    print("/|                   |/|  ")
    print("||   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" |__      XXX      __|     ")
    print("   |      XXX      |       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   |_             _|       ")
    print("     |_         _|         ")
    print("       |_______|           \033[m")

if __name__ == '__main__':
    jogo()