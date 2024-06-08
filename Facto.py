def factorize(n):
    factors = []
    divisor = 2
    
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
            
    return factors

# Exemple d'utilisation
x = 27773
print(f"Les facteurs de {x} sont : {factorize(x)}")
