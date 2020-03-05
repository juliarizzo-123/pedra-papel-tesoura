from random import randint
from time import sleep
escolha = 6
while escolha !=4:
  ct = ["computador" , 'outro jogador' ]

  op = ( 'pedra' , 'papel' , 'tesoura' )
  pc  =  randint ( 0 , 2 )

  print ( '~' * 20 )
  print ( 'Bem vindo ao ppt \n escolha um adversário: \n [0] - computador \n [1] - outro jogador \n [2] - pc vs cpu ' )
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
              print ( 'pedra vs pedra \n EMPATE!' )
          elif  jogador == 1 :
              print ( 'pedra vs papel \n VOCE GANHOU!' )
          elif  jogador == 2 :
              print ( 'pedra vs tesoura \n VOCE PERDEU!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')
          
      elif  pc == 1 :
          if  jogador == 0 :
              print ( 'papel vs pedra \n VOCE PERDEU!' )
          elif  jogador == 1 :
              print ( 'papel vs papel \n EMPATE!' )
          elif  jogador == 2 :
              print ( 'papel vs tesoura \n VOCE GANHOU!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')

      elif  pc == 2 :
          if  jogador == 0 :
              print ( 'tesoura vs pedra \n VOCE GANHOU!' )
          elif  jogador == 1 :
              print ( 'tesoura vs papel \n VOCE PERDEU!' )
          elif  jogador == 2 :
              print ( 'tesoura vs tesoura \n EMPATE!' )
          elif (jogador!=0 or jogador!=1 or jogador!=2):
            print('OPÇAO INVALIDA!!')

  elif escolha == 1:
      print('jorgar contra o outro jogador!')
      x=int(input("jogador 1: Qual sua opçao? : "))
      y=int(input("jogador 2: Qual sua opçao? : "))

      if x == 0 and y == 2:
        print("pedra vs tesoura \n jogador 1 GANHOU!!")
      elif x == 0 and y == 1:
        print("pedra vs papel \n jogador 2 GANHOU!!")
      elif x == 0 and y == 0:
        print("pedra vs pedra \n EMPATE!!")
  
      elif x == 1 and y == 0:
        print("papel vs pedra \n jogador 1 GANHOU!!")
      elif x == 1 and y == 2:
        print("papel vs tesoura \n jogador 2 GANHOU!!")
      elif x == 1 and y == 1:
        print("papel vs papel \n EMPATE!!")

      elif x == 2 and y == 1:
        print("tesoura vs papel \n jogador 1 GANHOU!!")
      elif x == 2 and y == 0:
        print("tesoura vs pedra \n jogador 2 GANHOU!!")
      elif x == 2 and y == 2:
        print("tesoura vs tesoura \n EMPATE!!")
      elif (x!=0 or x!=1 or x!=2) or (y!=0 or y!=1 or y!=2):
          print('OPÇAO INVALIDA!!')


  elif escolha == 2:
    op = ( 'pedra' , 'papel' , 'tesoura' )
    cpu  =  randint ( 0 , 2 )
    sleep(1)
    print ( 'pc vs cpu ' )
    pc  =  randint ( 0 , 2 )

    if pc == 0:
        if  cpu == 0 :
            print ( 'pedra vs pedra \n EMPATE!' )
        elif  cpu == 1 :
            print ( 'pedra vs papel \n cpu  GANHOU!' )
        elif  cpu == 2 :
            print ( 'pedra vs tesoura \n pc PERDEU!' )
        elif (cpu!=0 or cpu!=1 or cpu!=2):
          print('OPÇAO INVALIDA!!')
        
    elif  pc == 1 :
        if  cpu == 0 :
            print ( 'papel vs pedra \n cpu  PERDEU!' )
        elif  cpu == 1 :
            print ( 'papel vs papel \n EMPATE!' )
        elif  cpu == 2 :
            print ( 'papel vs tesoura \n cpu  GANHOU!' )
        elif (cpu!=0 or cpu!=1 or cpu!=2):
          print('OPÇAO INVALIDA!!')

    elif  pc == 2 :
        if  cpu == 0 :
            print ( 'tesoura vs pedra \n cpu GANHOU!' )
        elif  cpu == 1 :
            print ( 'tesoura vs papel \n cpu PERDEU!' )
        elif  cpu == 2 :
            print ( 'tesoura vs tesoura \n EMPATE!' )
        elif (cpu!=0 or cpu!=1 or cpu!=2):
          print('OPÇAO INVALIDA!!')

  else:
      print('OPÇAO INVALIDA!!')
else:
  print('volte sempre!!')
