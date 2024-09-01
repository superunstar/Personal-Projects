cle_str = "19391939"

for i in range(1, len(cle_str)):
        if cle_str[:i] * (len(cle_str) // i) == cle_str[:len(cle_str)]:
            print("FOUND! : " + cle_str[:i])