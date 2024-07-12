from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair(bits):
    """ Generate RSA key pair using pycryptodome """
    key = RSA.generate(bits)
    return key.publickey(), key


# Exemple d'utilisation
if __name__ == "__main__":
    # Générer les clés
    public_key, private_key = generate_keypair(4096)  # 2048 bits pour les clés
    
    
    # Message à chiffrer
    message = int(input("Entrez la valeur à chiffrer : "))
    
    e = public_key.e
    n = public_key.n
    C = message**e%n
    
    # Écrire dans un fichier texte
    with open('resultats.txt', 'w') as file:
        file.write(f"C : {C}\n")
        file.write(f"Valeur e : {public_key.e}\n")
        file.write(f"Valeur n : {public_key.n}\n")
    
    print("Résultats écrits dans le fichier 'resultats.txt'.")
