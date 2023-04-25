import math
from scipy.stats import hypergeom

def combinacion(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def distHiperGeometrica(N, n, r, x):
    """
    N = número de elementos
    n = número de elementos de la muestra
    r = número de elementos de la población
    x = número de elementos de la muestra que son de la población
    """
    return (combinacion(r, x) * combinacion(N - r, n - x)) / combinacion(N, n)

print(distHiperGeometrica(100, 10, 20, 5))
print(hypergeom.pmf(5, 100, 10, 20))