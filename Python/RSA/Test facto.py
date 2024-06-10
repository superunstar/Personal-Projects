import prime_gen
import facto
import os
import time

# clear le terminal
def clear_screen():
    os.system('clear') 
clear_screen()

# prend la valeur de la longueur de clé souhaitée en entrée
while True:
    bits = input("Entrez la longueur de clé souhaité : ")

    if bits.isdigit():
        bits = int(bits)
        break
    else:
        print("Err x001 : Verifiez que vous n'avez pas entré une lettre ou une valeur négative")
    

# divise la longueur de la clé par 2 puisque ce nombre sera ensuite 
bits = bits / 2
bits = int(bits)

p = prime_gen.gen_prime(bits)
q = prime_gen.gen_prime(bits)
n = p*q

if p > q:
    x = p
    p = q
    q = x

result = []

result.append(p)
result.append(q)

print("\nLes valeurs p et q sont :", p, "et", f"{q}, n est donc égal à :", n) 

debut = time.time()

n_facto = facto.factorize(n)

fin = time.time()

temps_ecoule = fin - debut

print("\nUne fois factorisé,", n, "donne", n_facto)

if result == n_facto:
    print("\nLe logiciel a bien reussi à retrouver les valeurs p et q en factorisant n\n\nTemps de factorisation :", temps_ecoule, "s\n")

else:
    print("\nLe logiciel n'a pas reussi à retrouver les valeurs p et q en factorisant n.\n")