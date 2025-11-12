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

def Q (D,S,H): #Cantidad economica de pedido
    Q = math.sqrt((2 * D * S) / H)
    return Q