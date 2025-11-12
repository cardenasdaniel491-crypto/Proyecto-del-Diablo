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
        ConvA = A / n
    elif op == 2: #De a a A
        ConvA = A * n
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