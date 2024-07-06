limite = 127 #int(input("Entrez votre limite de calcul : "))

# Lecture du fichier resultats.txt
with open('resultats.txt', 'r') as file:
    lines = file.readlines()
    C = int(lines[0].split(': ')[1].strip())
    e = int(lines[1].split(': ')[1].strip())
    n = int(lines[2].split(': ')[1].strip())

M = 0

while M < limite:
    if M**e%n == C:
        print("M peut être égal à",M)
        M += 1
    else:
        M += 1