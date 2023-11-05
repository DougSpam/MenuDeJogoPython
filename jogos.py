import atividade_forca
import atividade_advinhaçao
import atividade_jokenpo
def escolha():
    print('-=-' * 7)
    print('Escolha um jogo!')
    print('-=-' * 7)
#menu
    print('[ 1 ] Forca\n[ 2 ] Advinhação\n[ 3 ] Jokenpo')
    print('-=-' * 7)

    escolha = int(input('Qual você escolhe? ')) #escolha do usuario

    if escolha == 1: #algoritimo de escolha
        print('Jogando forca')
        atividade_forca.jogo()
    elif escolha == 2:
        print('Jogando Adivinhação')
        atividade_advinhaçao.jogo()
    elif escolha == 3:
        atividade_jokenpo.jogo()

if __name__ == '__main__':
    escolha()