p = 0
q = 0

def neg_op(value):
    if value == 1:
        value -= 1
        return value
    else:
        value += 1
        return value
    
def conj_op():
    if p and q == 1:
        return 1
    else:
        return 0

def disj_op():
    if p + q == 0:
        return 0
    else:
        return 1
    

print("1 : operateur negation\n2 : operateur conjonction \n3 : operateur disjonction")
choice = input("Choisissez : ")

if choice == "1":
    choice2 = input("entrez la valeur que vous voulez negationner : ")
    if choice2 == "p":
        result = neg_op(p)
        print(f"la valeur de p negationner est : {result}")
    elif choice == "q":
        result = neg_op(q)
        print(f"la valeur de q negationner est : {result}")
elif choice == "2":
    result = conj_op()
    print(f"la valeur de la conjonction de p et q est : {result}")
elif choice == "3":
    result = disj_op()
    print(f"la valeur de la disjonction de p et q est : {result}")
else:
    print("veuillez choisir parmis les choix proposés.")