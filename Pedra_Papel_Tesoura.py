import random
a = random.choice (["Pedra","Papel","Tesoura"])
player = (input("Pedra Papel ou Tesoura: "))
if (a==player):
    print (f"{a} x {player}")
    print ("Empate")
elif ((player=="Pedra" and a=="Tesoura") or (player=="Tesoura" and a=="Papel") or (player == "Papel" and a=="Pedra")):
    print (f"{player} x {a}")
    print ("Você venceu")
else:
    print (f"{player} x {a}")
    print ("Você perdeu")
    