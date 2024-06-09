import random #importation de la bibliothèque random

    def is_prime(n) : #defini la fonction qui vérifie qu'un nombre est premier
        if n<2: 
            return False
        else:
            for i in range(2,n) :
                if (n%i) == 0 :
                    return False
            return True



    def gen_prime(x):
        n = 0
        while True:
            if is_prime(n):
                return n
            else:
                n = random.getrandbits(x)

    bits = int(bits_input) / 2
    bits = int(bits)

    p = gen_prime(bits)
    q = gen_prime(bits)

    m = p*q

    with open("result.txt", "w", encoding="utf-8") as fichier:
        fichier.write(f"{m}")

    return(p, q)