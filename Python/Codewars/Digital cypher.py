#https://www.codewars.com/kata/592e830e043b99888600002d

def encode(message, key):    
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ciph = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    phrase = str(input("ent : "))

    x = 0

    crypted_message = []

    while x < 26:
        letter = str(alph[x])
        result = phrase.count(str(letter))
        if result > 0:
            while result != 0:
                letter = ciph[x]
                crypted_message.append(letter)
                result -= 1
            x += 1
        else:
            x += 1

    print(crypted_message)
