import math
def distribucionPoisson(lamdaa, k):
    """
    lamda = varianza
    k = número de éxitos
    """
    from math import factorial as fac
    return (lamdaa ** k) * (math.e ** (-lamdaa)) / fac(k)


def distribucionPoissonAcumulada(lamdaa, rango: list):
    acum = 0
    for i in range(rango[0], rango[1] + 1):
        acum += distribucionPoisson(lamdaa, i)
    return acum

print(distribucionPoisson(0.5, 0))
print(distribucionPoissonAcumulada(5*0.5, rango=[0, 2]))

