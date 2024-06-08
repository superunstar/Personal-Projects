# usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

def pgcd(a,b):
    while b>0:
        a,b=b,a%b      
    return a

tp_d=time()
n=584299
x,y,a,c=1,1,1,1

# Si la factorisation me marche pas
# Et si vous avez la certitude que votre nombre n'est pas premier
# Changez la valeur de c : essayez avec 3,5,7...

while a==1:
    x=(x**2+c)%n           # x = f(x)
    y=((y**2+c)**2+1)%n    # y = (f o f)(y)
    a=pgcd(n,abs(x-y))

temps = time()-tp_d
print("Le nombre",n,"se factorise ainsi :")
print("          ",a,"*",n/a)
print
print("Temps de travail :", temps,"s")