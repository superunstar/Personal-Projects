def find_the_key(message, code):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_key = []
    
    # Calcul de la clé déchiffrée
    for i in range(len(message)):
        letter_pos = alphabet.index(message[i]) + 1
        key_digit = code[i] - letter_pos
        decrypted_key.append(str(key_digit))
    
    cle_str = ''.join(decrypted_key)
    
    # Recherche de la plus courte sous-chaîne répétée
    for i in range(1, len(cle_str) + 1):
        if cle_str[:i] * (len(cle_str) // i) == cle_str[:len(cle_str)]:
            return cle_str[:i]
    
    return cle_str

message = "scout"
clé = [20, 12, 18, 30, 21]

print(find_the_key(message, clé))  # Cela devrait afficher "1939"
