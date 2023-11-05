import random
from time import sleep

def jogo():
    print('INICIANDO JOGO JOKENPO...')
    sleep(4)
    print('-=-=-\033[33mSUA OPÇÃO\033[m-=-=-\033[m')

    #opcoes para o jogador
    print('[ 0 ] \033[33mPEDRA\n\033[m[ 1 ] \033[33mPAPEL\n\033[m[ 2 ] \033[33mTESOURA\033[m')
    itens = ( 'Pedra', 'Papel', 'Tesoura' )
    jog = int(input('Qual a sua jogada? '))
    comp = random.randint(0 , 2)

    #interface
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)

    #o que cada um jogou
    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
    print(f' O computador escolheu \033[33m{itens[comp]}\033[m')
    print(f' O jogador escolheu \033[33m{itens[jog]}\033[m')
    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')

    #algoritimo
    if jog == comp:
        print('O jogo \033[33mEMPATOU\033[m') # jogo empate
    elif jog == 1 and comp == 0: # jogador jogou papel
        print('O jogador \033[33mGANHOU\033[m')
    elif jog == 2 and comp == 1: # jogador jogou tesoura
        print('O jogador \033[33mGANHOU\033[m')
    elif jog == 0 and comp == 2: # jogador jogou pedra
        print('O computador \033[33mGANHOU\033[m\nBoa Sorte na proxima vez')
    elif comp == 1 and jog == 0: # computador jogou papel
        print('O computador \033[33mGANHOU\033[m\nBoa Sorte na proxima vez')
    elif comp == 2 and jog == 1: # computador jogou tesoura
        print('O computador \033[33mGANHOU\033[m\nBoa Sorte na proxima vez')
    elif comp == 0 and jog == 2: # computador jogou pedra
        print('O computador \033[33mGANHOU\033[m\nBoa Sorte na proxima vez')
    else:
        print('Jogada invalida!')
    print('BOM JOGO')

if __name__ == '__main__':
    jogo()



