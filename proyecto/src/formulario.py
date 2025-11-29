import math

def Q(D, S, H, a, modelo):
    """
    Calcula la cantidad económica de pedido
    modelo: 1=EOQ básico, 2=Con escasez, 3=Producción
    """
    try:
        if modelo == 1:  # EOQ básico
            return math.sqrt((2 * D * S) / H)
        elif modelo == 2:  # Con escasez
            return math.sqrt((2 * D * S * (H + a)) / (H * a))
        elif modelo == 3:  # Producción
            return math.sqrt((2 * D * S) / (H * (1 - D/a)))
        else:
            raise ValueError("Modelo no válido")
    except Exception as e:
        raise ValueError(f"Error en cálculo de Q: {str(e)}")

def Sm(Q, D, S, H, a, modelo):
    """
    Calcula el inventario máximo
    modelo: 1=Con escasez, 2=Producción
    """
    try:
        if modelo == 1:  # Con escasez
            return math.sqrt((2 * D * S * a) / (H * (H + a)))
        elif modelo == 2:  # Producción
            return Q * (1 - D/a)
        else:
            raise ValueError("Modelo no válido")
    except Exception as e:
        raise ValueError(f"Error en cálculo de Sm: {str(e)}")

def calcular_CTA(D, Q, S, H, modelo, **kwargs):
    """
    Calcula Costo Total Anual
    """
    try:
        if modelo == 1:  # EOQ básico
            return (D / Q) * S + (Q / 2) * H
        elif modelo == 2:  # Con escasez
            Sm_val = kwargs.get('Sm')
            return (D / Q) * S + H * (Sm_val / 2)
        elif modelo == 3:  # Producción
            a = kwargs.get('a')
            return ((D * S) / Q) + (Q / 2) * (1 - D/a) * H
        else:
            raise ValueError("Modelo no válido")
    except Exception as e:
        raise ValueError(f"Error en cálculo de CTA: {str(e)}")

def ConvD(D, dias, tipo):
    """Conversión de unidades de demanda"""
    try:
        if tipo == 1:  # Anual a diaria
            return D / dias
        elif tipo == 2:  # Diaria a anual
            return D * dias
        else:
            raise ValueError("Tipo de conversión no válido")
    except Exception as e:
        raise ValueError(f"Error en conversión: {str(e)}")

def calcular_costo_mantenimiento(C, I):
    """Calcula H a partir de C e I"""
    try:
        return C * (I / 100)
    except Exception as e:
        raise ValueError(f"Error en cálculo de H: {str(e)}")

def validar_entrada(valor, nombre, minimo=0, maximo=float('inf')):
    """Valida entradas numéricas"""
    try:
        valor_float = float(valor)
        if valor_float < minimo:
            raise ValueError(f"{nombre} debe ser ≥ {minimo}")
        if valor_float > maximo:
            raise ValueError(f"{nombre} debe ser ≤ {maximo}")
        return valor_float
    except ValueError:
        raise ValueError(f"{nombre} debe ser número válido")