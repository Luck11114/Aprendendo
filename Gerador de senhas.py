import random
quantidade = int (input("Insira a quantidade de senhas que deseja: "))
tamanho = int(input("Insira a quantidade de digitos que deseja na sua senha: "))
caracteres = "abcdefghojklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%¨&*()-_=+[{]}`~^/?;:\|]"
for qnt in range(quantidade):
    senhas = ''
    for caracter in range(tamanho):
        senhas += random.choice(caracteres)
    print (senhas)