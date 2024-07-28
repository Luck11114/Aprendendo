import time
import os
tempodesejado = int(input("Insira o tempo que deseja contar em segundos: "))
os.system("cls")
while tempodesejado != 0:
    horas, resto = divmod(tempodesejado, 3600) 
    minutos, segundos = divmod(tempodesejado, 60)
    print (f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
    tempodesejado = tempodesejado-1
    os.system("cls")
print ("Fim da contagem")