import math

def d(D,n): #Convertir de meses o años a días
    return D/n

def h(H,n): #Convertir de meses o años a días
    return H/n

def Q(S,d,h): #Formula general de Q
    T = math.sqrt((2*S*d)/h) #Total
    return T

