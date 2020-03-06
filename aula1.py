from random import randint
from time import sleep
def jogadorvspc():
  print ( ' Escolha uma opção: \n [0] - Pedra \n [1] - Papel \n [2] - Tesoura' )
  jogador =int ( input ( 'Qual sua jogada?: ' ))
  print ( '~' * 20 )
  sleep(1)
  print ( 'Jogar contra o computador' )
  pc  =  randint ( 0 , 2 )

  if pc == 0:
      if  jogador == 0 :
          print ( 'PEDRA VS PEDRA \n EMPATE!' )
      elif  jogador == 1 :
          print ( 'PEDRA VS PAPEL \n VOCE GANHOU!' )
      elif  jogador == 2 :
          print ( 'PEDRA VS TESOURA \n VOCE PERDEU!' )
      elif (jogador!=0 or jogador!=1 or jogador!=2):
        print('OPÇAO INVALIDA!!')
      
  elif  pc == 1 :
      if  jogador == 0 :
          print ( 'PAPEL VS PEDRA \n VOCE PERDEU!' )
      elif  jogador == 1 :
          print ( 'PAPEL VS PAPEL \n EMPATE!' )
      elif  jogador == 2 :
          print ( 'PAPEL VS TESOURA \n VOCE GANHOU!' )
      elif (jogador!=0 or jogador!=1 or jogador!=2):
        print('OPÇAO INVALIDA!!')

  elif  pc == 2 :
      if  jogador == 0 :
          print ( 'TESOURA VS PEDRA \n VOCE GANHOU!' )
      elif  jogador == 1 :
          print ( 'TESOURA VS PAPEL \n VOCE PERDEU!' )
      elif  jogador == 2 :
          print ( 'TESOURA VS TESOURA \n EMPATE!' )
      elif (jogador!=0 or jogador!=1 or jogador!=2):
        print('OPÇAO INVALIDA!!')

def jogadorvsjogador():
  print('jogar contra o outro jogador! \n')
  print ( ' Escolha uma opção: \n [0] - Pedra \n [1] - Papel \n [2] - Tesoura \n ' ) 
  
  x=int(input("jogador 1: Qual sua jogada? : "))
  y=int(input("jogador 2: Qual sua jogada? : \n "))

  if x == 0 and y == 2:
    print("PEDRA VS TESOURA \n jogador 1 GANHOU!!")
  elif x == 0 and y == 1:
    print("PEDRA VS PAPEL \n jogador 2 GANHOU!!")
  elif x == 0 and y == 0:
    print("PEDRA VS PEDRA \n EMPATE!!")

  elif x == 1 and y == 0:
    print(" PAPEL VS PEDRA \n jogador 1 GANHOU!!")
  elif x == 1 and y == 2:
    print(" PAPEL VS TESOURA \n jogador 2 GANHOU!!")
  elif x == 1 and y == 1:
    print(" PAPEL VS PAPEL \n EMPATE!!")

  elif x == 2 and y == 1:
    print("TESOURA VS PAPEL \n jogador 1 GANHOU!!")
  elif x == 2 and y == 0:
    print("TESOURA VS PEDRA \n jogador 2 GANHOU!!")
  elif x == 2 and y == 2:
    print("TESOURA VS TESOURA \n EMPATE!!")
  elif (x!=0 or x!=1 or x!=2) or (y!=0 or y!=1 or y!=2):
      print('OPÇAO INVALIDA!!')

def pcvscpu():
  op = ( 'pedra' , 'papel' , 'tesoura' )
  cpu  =  randint ( 0 , 2 )
  sleep(1)
  print ( 'PC VS CPU' )
  pc  =  randint ( 0 , 2 )

  if pc == 0:
      if  cpu == 0 :
          print ( 'PEDRA VS PEDRA \n EMPATE!' )
      elif  cpu == 1 :
          print ( 'PEDRA VS PAPEL \n CPU  GANHOU!' )
      elif  cpu == 2 :
          print ( 'PEDRA VS TESOURA \n PC PERDEU!' )
      elif (cpu!=0 or cpu!=1 or cpu!=2):
        print('OPÇAO INVALIDA!!')
      
  elif  pc == 1 :
      if  cpu == 0 :
          print ( 'PAPEL VS PEDRA \n CPU  PERDEU!' )
      elif  cpu == 1 :
          print ( 'PAPEL VS PAPEL \n EMPATE!' )
      elif  cpu == 2 :
          print ( 'PAPEL VS TESOURA \n CPU  GANHOU!' )
      elif (cpu!=0 or cpu!=1 or cpu!=2):
        print('OPÇAO INVALIDA!!')

  elif  pc == 2 :
      if  cpu == 0 :
          print ( 'TESOURA VS PEDRA \n CPU GANHOU!' )
      elif  cpu == 1 :
          print ( 'TESOURA VS PAPEL \n CPU PERDEU!' )
      elif  cpu == 2 :
          print ( 'TESOURA VS TESOURA \n EMPATE!' )
      elif (cpu!=0 or cpu!=1 or cpu!=2):
        print('OPÇAO INVALIDA!!')


escolha = 6
while escolha != 4:
  ct = ["computador" , 'outro jogador' ]

  op = ( 'pedra' , 'papel' , 'tesoura' )
  pc  =  randint ( 0 , 2 )

  print ( '~' * 20 )
  print ( 'Bem vindo ao ppt \n Escolha um adversário: \n [0] - Computador \n [1] - Outro jogador \n [2] - PC vs CPU \n [4] - Sair do jogo' )
  escolha =int ( input ( 'Qual seu adversario?: ' ))
  print ( '~' * 20 )
  sleep(1)

  if  escolha == 0 : 
    jogadorvspc()
      
  elif escolha == 1:
    jogadorvsjogador()
      

  elif escolha == 2:
    pcvscpu()
    

  else:
      print('OPÇAO INVALIDA!!')
else:
  print('volte sempre!!')
