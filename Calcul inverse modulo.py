import time

n = 143
e = 7
result = 91
x = 0

while True:
    if x ** e % n == result:
        print(f"x = {x}")
        break
    else:
        time.sleep(0.05)
        x += 1
        print(f"test x = {x}")