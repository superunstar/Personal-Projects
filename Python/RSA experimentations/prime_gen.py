import secrets

def miller_rabin(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False

    # Écriture de n comme (2^r)*d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Effectue le test k fois
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gen_prime(x):
    while True:
        n = secrets.randbits(x)
        if n % 2 == 0:  # Assure que le nombre généré est impair
            n += 1
        if miller_rabin(n):
            return n

result = gen_prime(50)
print(result)
