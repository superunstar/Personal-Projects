#https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c

def xor(a, b):
    if a == True and b == True:
        return False
    elif a == False and b == False:
        return False
    else:
        return True

print(xor(True, False))
print(xor(True, True))
print(xor(False, False))

    
