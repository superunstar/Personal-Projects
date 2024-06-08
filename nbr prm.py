from Crypto.Util import number
import math

def generate_prime(bits):
    return number.getPrime(bits)

def generate_prime_product(target_bits):
    # Estimation de la taille des nombres premiers
    prime_bits = target_bits // 2

    while True:
        # Génération de deux nombres premiers
        p = generate_prime(prime_bits)
        q = generate_prime(prime_bits)

        # Calcul du produit
        product = p * q

        # Vérification de la taille du produit
        if product.bit_length() == target_bits:
            return p, q, product

# Spécifiez le nombre de bits pour le produit
target_bits = 15

# Génération des nombres premiers et de leur produit
p, q, product = generate_prime_product(target_bits)

# Affichage des résultats
print(f"Premier nombre premier (p): {p}")
print(f"Deuxième nombre premier (q): {q}")
print(f"Produit (p * q) de {target_bits} bits:\n{product}")
print(f"Longueur en bits du produit: {product.bit_length()}")
