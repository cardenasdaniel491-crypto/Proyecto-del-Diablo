import math

def H (c,I): #Costo de mantenimiento de inventario
    H = c * I
    return H

def ConvH (H,n,op): #Conversion de H a h y viceversa
    if op == 1: #De H a h
        ConvH = H / n
    elif op == 2: #De h a H
        ConvH = H * n
    return ConvH

def ConvD (D,n,op): #Conversion de D a d y viceversa
    if op == 1: #De D a d
        ConvD = D / n
    elif op == 2: #De d a D
        ConvD = D * n
    return ConvD

def ConvA (a,n,op): #Conversion de ca o a a anual y viceversa
    if op == 1: #De A a a
        ConvA = a / n
    elif op == 2: #De a a A
        ConvA = a * n
    return ConvA

def Q (D,S,H,a,op): #Cantidad Optima de Pedido
    if op == 1: #General
        arriba = 2 * D * S
        division = arriba / H
        Q = math.sqrt(division)
    elif op == 2: #Con escacez
        arriba = 2 * D * S * (H + a)
        abajo = H * a
        division = arriba / abajo
        Q = math.sqrt(division)
    elif op == 3: #Con produccion
        arriba = 2 * D * S
        abajo = H * (1 - (D / a))
        division = arriba / abajo
        Q = math.sqrt(division)
    return Q

def n(L,t):
    num = L/t
    n = math.floor(num) #para redondear hacia abajo
    return n

def PR(L,D,t,n,op): #Punto de reorden
    if op == 1: #General
        if L < t:
            PR = L * D
        elif L > t:
            PR = (L - n * t) * D
        else:
            PR = 0    
    elif op == 2: #Probabilistico
        PR = (L * D) + t # t = B
    return PR

def Sm (Q,D,a,S,H,op):
    if op == 1: #Con escacez
        arriba = 2 * S * D * a
        abajo = H * (H + a)
        division = arriba / abajo
        Sm = math.sqrt(division)
    elif op == 2: #Con produccion
        Sm = Q * (1 - (D / a))
    return Sm

def t1 (Q,D,a,op): #Tiempo de produccion
    if op == 1: #Sin produccion
        t1 = Q / D
    elif op == 2: #Con produccion
        t1 = Q / a
    return t1

def t2 (Sm,D): 
    t2 = Sm / D
    return t2

def InvProm (Q,D,H,a,op): #Costo de Mtt de Inventario Promedio
    if op == 1: #General
        InvProm = (Q / 2) * (H)
    elif op == 2: #Con escacez
        Arriba = Q * (1 - (a / D)) # a = Sm
        Abajo = 2
        InvProm = (Arriba / Abajo) * H
    elif op == 3: #Con produccion
        Arriba = Q * (1 - (D / a))
        Abajo = 2
        InvProm = (Arriba / Abajo) * H
    return InvProm