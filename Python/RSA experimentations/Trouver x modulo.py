limite = 1000 #int(input("Entrez votre limite de calcul : "))

# Lecture du fichier resultats.txt
with open('resultats.txt', 'r') as file:
    lines = file.readlines()
    C = 91 #int(lines[0].split(': ')[1].strip())
    e = 7 #int(lines[1].split(': ')[1].strip())
    n = 143 #int(lines[2].split(': ')[1].strip())

M = 0

while M < limite:
    if M**e%n == C:
        print("M peut être égal à",M)
        M += 1
    else:
        M += 1