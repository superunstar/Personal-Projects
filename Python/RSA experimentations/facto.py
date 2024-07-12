def factorize(n): #defini la fonction "factorize"
    factors = [] #liste pour ranger les facteurs
    divisor = 2 
    
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
            
    return factors
