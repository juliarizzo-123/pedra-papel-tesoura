from random import randint
from time import sleep
ct= ("computador", 'outro jogador')

op= ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print('~'*10)
print('escolha um adversario: \n[0] - computador\n[1] - outro jogador')
escolha= print(int(input('qual sua opçao?: ')))
print('~'*10)
sleep(1)
print('Bem vindo ao ppt\nescolha uma opçao: \n[0] - pedra\n[1] - papel\n[2] - tesoura')
jogador= print(int(input('qual sua opçao?: ')))
print('~'*10)
sleep(1)

if escolha==0: 
    print('jogar contra o computador')
    pc=random.randint(0,2)
    if pc==0: 
        if jogador==0:
            print('EMPATE!')
        elif jogador==1:
            print('VOCE GANHOU!')
        elif jogador==2:
            print('VOCE PERDEU!')
        
    elif pc==1:
        if jogador==0:
            print('VOCE PERDEU!')
        elif jogador==1:
            print('EMPATE!')
        elif jogador==2:
            print('VOCE GANHOU!')

    elif pc==2:
        if jogador==0:
            print('VOCE GANHOU!')
        elif jogador==1:
            print('VOCE PERDEU!')
        elif jogador==2:
            print('EMPATE!')