from random import randint
from time import sleep
ct= ("computador", 'outro jogador')

op= ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

print('~'*10)
print('escolha um adversario: \n[0] - computador\n[1] - outro jogador')
jogador= print(int(input('qual sua opçao?: ')))
print('~'*10)
sleep(1)
print('Bem vindo ao ppt\nescolha uma opçao: \n[0] - pedra\n[1] - papel\n[2] - tesoura')
print('~'*10)
sleep(1)

if ct==0: #jogar contra o pc
    if op==0: 
        
    elif op==1:
    elif op==2: