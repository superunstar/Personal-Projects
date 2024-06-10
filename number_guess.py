import random

random_number = random.randint(0, 100)

while True:
    choix = int(input("choisissez un nombre entre 0 et 100 : "))
    if choix == random_number:
        print("Bravo !")
        break
    elif choix < random_number:
        print("C'est plus !")
    elif choix > random_number:
        print("C'est moins !")