import random
import time
#categorias

acao = ['cortar', 'costurar', 'bater', 'coçar', 'lavar a cabeça', 'comer', 'beber', 'pentear-se', 'pintar', 'escrever', 'ler', 'correr', 'apagar', 'chamar', 'varrer', 'adormecer', 'tocar tambor', 'telefonar']
culturapop = ['harry-potter', 'cherife-wood', 'wanda-maximof', 'super-mario-world', 'senhor batata', 'os goonies', 'os simpsons' ]
pessoas = ['harison ford', 'madonna', 'ammy whinehose', 'fernanda montenegro', 'ayrton senna']

'''def tempo_por_rodada():
    tempoPorRodada = int(input('Qual a sua opção?'))
    if tempoPorRodada == 60:
        tempo = time.sleep(60)
    elif tempoPorRodada == 80:
        tempo = time.sleep(80)
    elif tempoPorRodada == 100:
        tempo = time.sleep(100)
    elif tempoPorRodada == 120:
        tempo = time.sleep(120)
    print(f'Você terá {tempo} segundos!')'''

def escolha_categoria():
    while True:
        escolha = int(input('Sua categoria: '))
        if escolha == 1:
            for c in range(3, 0, -1):
                print(c)
                time.sleep(1)
            print('Sua palavra é:')
            time.sleep(1)
            print(random.choice(acao))
        elif escolha == 2:
            for c in range(3, 0, -1):
                print(c)
                time.sleep(1)
            print('Sua palavra é:')
            time.sleep(1)
            print(random.choice(culturapop))
        elif escolha == 3:
            for c in range(3, 0, -1):
                print(c)
                time.sleep(1)
            print('Sua palavra é:')
            time.sleep(1)
            print(random.choice(pessoas))
        else:
            print('Opção inválida!')
            break

'''print('Vamos começar o jogo! Quantos para cada rodada?')
print('60 segundos')
print('80 segundos')
print('100 segundos')
print('120 segundos')'''


print('Escolha uma das categorias abaixo!')
print('[ 1 ] AÇÃO')
print('[ 2 ] CULTURA POP')
print('[ 3 ] PESSOAS')
print('')

escolha_categoria()
