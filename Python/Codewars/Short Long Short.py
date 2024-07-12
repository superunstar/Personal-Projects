#https://www.codewars.com/kata/50654ddff44f800200000007

def solution(a, b):
    if isinstance(a or b, str): #Verify if inputs are strings or integers
        if len(a) < len(b): #If inputs are strings, compare lenght of each input wit len() function
            return (f"{a}{b}{a}") #If "b" lenght is greater than "a" lenght, return "a,b,a" scheme
        else:
            return (f"{b}{a}{b}") # If "a" lenght is greater than "b" lenght, return "b,a,b" scheme
    else:
        if a < b: #If inputs are integers, compare which value is the greater
            return (f"{a}{b}{a}") #If "b" value is greater than "a" value, return "a,b,a" scheme
        else:
            return (f"{b}{a}{b}") #If "b" value is greater than "a" value, return "b,a,b" scheme
    pass