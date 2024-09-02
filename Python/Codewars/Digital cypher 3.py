#https://www.codewars.com/kata/5930d8a4b8c2d9e11500002a/train/python

def find_the_key(message, code):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Define the alphabet as a list of characters
    message1 = message + message
    message_list = [str(c) for c in message1]
    
    x = 0
    n = len(code)
    
    decrypted_key = []
    
    while x < len(message1):
        letter = message_list[x]
        letter_pos = alphabet.index(str(letter)) + 1
        if code[x%n] < letter_pos:
            result = letter_pos - code[x%n]
            decrypted_key.append(str(result))
        else:
            result = code[x%n] - letter_pos
            decrypted_key.append(str(result))
        
        
        x += 1 
    
    cle_str = ''.join(decrypted_key)
    
    print(cle_str)
        
    for i in range(1, len(cle_str)):
        if cle_str[:i] * (len(cle_str) // i) == cle_str[:len(cle_str)]:
            print("success")
            print("F: " + cle_str[:i])
            return cle_str[:i]
        
        
message = "scout"
clé = [20, 12, 18, 30, 21]

print(find_the_key(message, clé))