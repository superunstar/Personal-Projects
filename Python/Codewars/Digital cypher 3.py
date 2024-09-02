#https://www.codewars.com/kata/5930d8a4b8c2d9e11500002a/train/python

def find_the_key(message, code):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Define the alphabet as a list of characters
    message_list = [str(c) for c in message]
    
    x = 0
    n = len(code)
    
    decrypted_key = []
    
    while x < len(message):
        letter = message_list[x]
        letter_pos = alphabet.index(str(letter)) + 1
        if code[x%n] < letter_pos:
            result = letter_pos - code[x%n]
            decrypted_key.append(str(result))
        else:
            result = code[x%n] - letter_pos
            decrypted_key.append(str(result))
        
        x += 1 
    
    for i in range(1, len(code)):
        c = decrypted_key[i]
        if c == decrypted_key[0]:
            decrypted_key = decrypted_key[:i]
            decrypted_key = ''.join(decrypted_key)
            return int(decrypted_key)
        
        
message = "masterpiece"
clé = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

print(find_the_key(message, clé))