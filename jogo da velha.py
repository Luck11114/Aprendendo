import os
pos1 = '1'
pos2 = '2'
pos3 = '3'
pos4 = '4'
pos5 = '5'
pos6 = '6'
pos7 = '7'
pos8 = '8'
pos9 = '9'
vez = 1
fim = 0
jogador1 = ''
jogador2 = ''
def selecionado(selecao):#seleciona a forma dos jogadores
    if selecao == 'x':
        jogador1 = 'x'
        jogador2 = 'o'
        return jogador1,jogador2

    if selecao == 'o':
        jogador1 = 'o'
        jogador2 = 'x'
        return jogador1,jogador2
def tabela():#escreve toda tabela
    global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, jogador1, jogador2
    x=1
    matrix = [[pos1, pos2, pos3],
              [pos4, pos5, pos6],
              [pos7, pos8, pos9]]
    linhas = ["---------"]
    for linha in matrix:
        print(" | ".join(linha)) 
        if x < 3:
            x=x+1
            print("".join(linhas))   
def jogada(posicao):#troca os valores da tabela
    global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, vez, jogador1, jogador2
    if posicao == 1 and vez == 1:
        pos1 = jogador1
    if posicao == 1 and vez == 2:
        pos1 = jogador2
    if posicao == 2 and vez == 1:
        pos2 = jogador1
    if posicao == 2 and vez == 2:
        pos2 = jogador2
    if posicao == 3 and vez == 1:
        pos3 = jogador1
    if posicao == 3 and vez == 2:
        pos3 = jogador2
    if posicao == 4 and vez == 1:
        pos4 = jogador1
    if posicao == 4 and vez == 2:
        pos4 = jogador2 
    if posicao == 5 and vez == 1:
        pos5 = jogador1
    if posicao == 5 and vez == 2:
        pos5 = jogador2
    if posicao == 6 and vez == 1:
        pos6 = jogador1
    if posicao == 6 and vez == 2:
        pos6 = jogador2
    if posicao == 7 and vez == 1:
        pos7 = jogador1
    if posicao == 7 and vez == 2:
        pos7 = jogador2
    if posicao == 8 and vez == 1:
        pos8 = jogador1
    if posicao == 8 and vez == 2:
        pos8 = jogador2
    if posicao == 9 and vez == 1:
        pos9 = jogador1
    if posicao == 9 and vez == 2:
        pos9 = jogador2
def acabouounao():#checa se acabou ou não
    global fim
    if (pos1==pos2==pos3) or (pos1==pos4==pos7) or (pos1==pos5==pos9) or \
        (pos2==pos5==pos8) or (pos3==pos6==pos9) or (pos4==pos5==pos6) or \
        (pos7==pos8==pos9) or (pos7==pos5==pos3):
        fim = 1
        return fim
    elif (pos1 != '1') and (pos2 != '2') \
        and (pos3!='3') and (pos4 != '4') \
        and (pos5 != '5') and (pos6 != '6') \
        and (pos7 != '7') and (pos8 != '8') and (pos9 != '9'):
        fim = 2
        return fim
    else:
        fim = 3
        return fim
tabela()
jogador1, jogador2 = selecionado('x')
while (fim != 1 and fim !=2):
    print (f"Vez do jogador {vez}: ")
    a = int(input("Selecione a posicao que deseja jogar: "))
    jogada (a)
    acabouounao()
    os.system("cls")
    tabela()
    if vez == 1:
        vez = 2
    else: 
        vez = 1
os.system("cls")
if fim == 2:
    print ("Empate")
elif vez == 2:#Invertido porque foi necessário colocar a inversão das vezes no fim do while
    print ("Jogador um venceu")
else:
    print ("Jogador dois venceu")