key = "1445"

key1 = [int(char) for char in key]

x = 0

while True:
    result = key1[x]

    print(result)
    
    n = len(key1)
    
    x = (x + 1) % n


