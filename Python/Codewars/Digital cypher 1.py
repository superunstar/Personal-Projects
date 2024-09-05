#https://www.codewars.com/kata/592e830e043b99888600002d

def encode(message, key):    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Define all alphabet letters in a list.
    key1 = [int(char) for char in str(key)]  # Convert the key to a list of integers (each digit of the key).
    message1 = [str(chor) for chor in message]  # Convert the message to a list of characters.

    x = 0  # Initialize a counter for the message index.
    n = len(key1)  # Get the length of the key list.
    
    crypted_message = [] # Initialize an empty list to store the encoded message.

    while x < len(message):  # Loop through each character in the message.
        letter = str(message1[x])  # Get the current letter from the message.
        letter_position = alphabet.index(letter) + 1  # Find the position of the letter in the alphabet (1-based index).
        cipher_text = letter_position + key1[x%n]  # Encoded the letter by adding the key value (cyclically using modulo).
        crypted_message.append(cipher_text) # Append encoded value to the crypted_message list.
        x +=1  # Move to the next character in the message.
    return crypted_message


message = "masterpiece"
clé = "13143"

print(encode(message, clé))
