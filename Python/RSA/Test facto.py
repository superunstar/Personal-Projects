import prime_gen
import facto
import os
import barre_charg

# clear le terminal
def clear_screen():
    os.system('clear') 
clear_screen()

# prend la valeur de la longueur souhaitée du nombre en entrée
while True:
    bits = input("Entrez la longueur de clé souhaité : ")

    if bits.isdigit():
        bits = int(bits)
        break
    else:
        print("Err x001 : Verifiez que vous n'avez pas entré une lettre ou une valeur négative")
    

# definie la variable result comme les nombres p et q
result = prime_gen.gen_prime(bits)

print(f"Les valeurs p et q sont : ", result) 

barre_charg.afficher_barre_de_chargement(1)

facto.factorize
