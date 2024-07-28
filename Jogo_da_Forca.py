import os
palavra=input("Insira a palavra: ")
palavraescondida = []
letrasusadas = []
b="c"
vidas = int(input("Quantidade de vidas: "))
os.system("cls")

for letra in palavra:
    palavraescondida.append("_")
os.system("cls")

while "_" in palavraescondida and vidas>0 and b!=palavra:
    print("".join(palavraescondida))
    print ("-".join(letrasusadas))
    print(f"Vidas restantes:{vidas}")
    a=input("Insira uma letra, caso deseje chutar digite \"chute\": ")
    if a == "chute":
        b=input("Insira a palavra: ")
        if b!=palavra:
            vidas=0
    if a in palavra:
        for i in range(len(palavra)):
            if palavra[i] == a:
                palavraescondida[i] = a
    else:
        vidas = vidas-1
    letrasusadas.append(a)
    os.system("cls")
if vidas <= 0:
    print("Voce perdeu")
    print(f"Palavra correta: \"{palavra}\"")
else:
    print("Voce venceu")