import math

def d(D,n): #Convertir de meses o años a días
    d = D/n
    return d

def H(c,I): #Costo de mantenimiento
    H = c*I
    return H

def h(H,n): #Convertir de meses o años a días
    h = H/n
    return h

def Q(S,d,h): #Formula de cantidad economica de pedido sin escasez
    Q = math.sqrt((2*S*d)/h) #Total
    return Q

def CTU(S,d,h,Q): #Costo total unitario sin escasez
    CTU = (S*d)/Q + (h*Q)/2
    return CTU

def t(Q,d): #Tiempo entre pedidos sin escasez
    t = Q/d
    return t

def PR(L,d,t): #Periodo de reabastecimiento sin escasez
    n = L/t
    if L<t:
        PR = L*d
    else:
        PR = L-(n*t)
    return PR

def p(Ca,n):
    p = Ca/n
    return p

def Qs(S,d,h,p): #Formula de cantidad economica de pedido con escasez
    Qs = math.sqrt((2*S*d*(p+h))/(p*h))
    return Qs

