import random
a = random.randint (0,5)
x = int(input("Chute: "))
if (a==x):
    print ("You win")
else:
    print ("You lost")
    print ("Correct number:",a)