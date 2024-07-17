#https://www.codewars.com/kata/592edfda5be407b9640000b2

def decode(code, key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Define the alphabet as a list of characters
    key1 = [int(char) for char in str(key)] # Convert the key to a list of its digits
    
    x = 0 # Initialize the position counter
    n = len(key1) # Get the length of the key list
    
    decrypted_message = [] # Initialize an empty list to store the decrypted message

    while x < len(code): # Loop through the code to decode each letter
        letter_position = (code[x] - 1) - key1[x % n] # Calculate the position of the decrypted letter in the alphabet
        letter = alphabet[letter_position] # Get the decrypted letter from the alphabet list
        decrypted_message.append(letter) # Append the decrypted letter to the decrypted message list
        x += 1 # Move to the next position in the code
        result = ''.join(decrypted_message) # Join the list of decrypted letters into a single string
    return result # Return the decrypted message



code = [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
clé = "1939"

print(decode(code, clé))
