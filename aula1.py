from random import randint
from time import sleep
escolha = 6
while escolha !=4:
  ct = ["computador" , 'outro jogador' ]

  op = ( 'pedra' , 'papel' , 'tesoura' )
  pc  =  randint ( 0 , 2 )

  print ( '~' * 20 )
  print ( 'Bem vindo ao ppt \n escolha um adversário: \n [0] - computador \n [1] - outro jogador \n [2] - computador vs computador' )
  escolha =int ( input ( 'qual sua opção ?:' ))
  print ( '~' * 20 )
  sleep(1)

  if  escolha == 0 :
      print ( ' escolha uma opção: \n [0] - pedra \n [1] - papel \n [2] - tesoura' )
      jogador =int ( input ( 'qual sua opção ?:' ))
      print ( '~' * 20 )
      sleep(1)
      print ( 'jogar contra o computador' )
      pc  =  randint ( 0 , 2 )

      if pc == 0:
          if  jogador == 0 :
              print ( 'EMPATE!' )
          elif  jogador == 1 :
              print ( 'VOCE GANHOU!' )
          elif  jogador == 2 :
              print ( 'VOCE PERDEU!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')
          
      elif  pc == 1 :
          if  jogador == 0 :
              print ( 'VOCE PERDEU!' )
          elif  jogador == 1 :
              print ( 'EMPATE!' )
          elif  jogador == 2 :
              print ( 'VOCE GANHOU!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')

      elif  pc == 2 :
          if  jogador == 0 :
              print ( 'VOCE GANHOU!' )
          elif  jogador == 1 :
              print ( 'VOCE PERDEU!' )
          elif  jogador == 2 :
              print ( 'EMPATE!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')

  elif escolha == 1:
      print('jorgar contra o outro jogador!')
      x=int(input("jogador 1: Qual sua opçao? : "))
      y=int(input("jogador 2: Qual sua opçao? : "))

      if x == 0 and y == 2:
        print("jogador 1 GANHOU!!")
      elif x == 0 and y == 1:
        print("jogador 2 GANHOU!!")
      elif x == 0 and y == 0:
        print("EMPATE!!")
  
      elif x == 1 and y == 0:
        print("jogador 1 GANHOU!!")
      elif x == 1 and y == 2:
        print("jogador 2 GANHOU!!")
      elif x == 1 and y == 1:
        print("EMPATE!!")

      elif x == 2 and y == 1:
        print("jogador 1 GANHOU!!")
      elif x == 2 and y == 0:
        print("jogador 2 GANHOU!!")
      elif x == 2 and y == 2:
        print("EMPATE!!")
      elif (x!=0 or x!=1 or x!=2) or (y!=0 or y!=1 or y!=2):
          print('OPÇAO INVALIDA!!')
  else:
      print('OPÇAO INVALIDA!!')
else:
  print('volte sempre!!')
