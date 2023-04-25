import math
from probabilidad import Comb as combinatoria

def distribucionBinomial(n, p, q, x):
    """
    n = número de ensayos
    p = probabilidad de éxito
    q = probabilidad de fracaso
    x = cualquier valor
    """
    
    return combinatoria(n, x) * (p ** x) * (q ** (n - x))

def distribucionBinomialAcumulada(n, p, q, rango: list):

    acum = 0
    for i in range(rango[0], rango[1] + 1):
        acum += combinatoria(n, i) * (p ** i) * (q ** (n - i))
    return acum



print(distribucionBinomial(20.0, 0.1, 0.9, 2))
print(distribucionBinomialAcumulada(20.0, 0.1, 0.9, rango=[3,20]))