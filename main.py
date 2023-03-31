import math
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from prettytable import PrettyTable

datos = """
datos
"""

# elementos = datos.replace(',', '').split()
elementos = datos.replace(',', '.').split()


arr_np = np.array(elementos, dtype=np.float32)


mayor = arr_np.max()
menor = arr_np.min()
print(arr_np)
print(sorted(arr_np))
arr_np = sorted(arr_np)

print("El mayor valor es: ", mayor)
print("El menor valor es: ", menor)
print("El numero de elementos es: ", len(arr_np))
k = 1 + 3.322 * math.log10(len(elementos))
k = round(k)


l = (float(mayor) - float(menor)) / k
l = round(l)

print("El valor de k es: ", k)
print("El valor de l(amplitud) es: ", l)
rango = mayor - menor

def sturges_bins(data):
    n = len(data)
    k = int(1 + np.log2(n))
    range_data = max(data) - min(data)
    
    bin_width = range_data / k
    
    bins = []
    for i in range(k):
        bins.append(min(data) + i * bin_width)
    bins.append(max(data))




    # Imprimir los intervalos de clase y su frecuencia
    for i, interval in enumerate(bins):
        try:
            print(f"Intervalo {i+1}: {interval} - {bins[i+1]}")
        except IndexError:
            pass

        
    return bins

intervalovichs = sturges_bins(arr_np)
print(intervalovichs)


def tabla_frecuencias(intervalos, frecuencias):
    tabla = PrettyTable(['Intervalo', 'Frecuencia', 'Fre. relativa', 'Fre. acumulada', 'Fre. relativa acumulada'])
    for i in range(len(intervalos)):
        try:
            tabla.add_row([f'{intervalos[i]}', f'{frecuencias[i]}', f'{round(frecuencias[i]/len(arr_np), ndigits=3)}', f'{sum(frecuencias[:i+1])}', f'{round(sum(frecuencias[:i+1])/len(arr_np), ndigits=3)}'])
        except IndexError:
            pass
    tabla.add_row(['Total', f'{len(arr_np)}', f'{round(sum(frecuencias)/len(arr_np), ndigits=3)}', f'{sum(frecuencias)}', f'{round(sum(frecuencias)/len(arr_np), ndigits=3)}'])
    
    print(tabla)
def contar_frecuencias(intervalos, datos):
    auxIntervalos = list(zip(intervalos[:-1], intervalos[1:]))
    frecuencias = [sum(1 for dato in datos if intervalo[0] <= dato < intervalo[1]) for intervalo in auxIntervalos]
    maximos = 0
    maximo = max(datos)
    for dato in datos:
        if dato == maximo:
            maximos += 1
    
    frecuencias[len(frecuencias)-1] += maximos
    return frecuencias, auxIntervalos



def str_intervalos(intervalos):
    str_intervalos = []
    for i in range(len(intervalos)):
        str_intervalos.append(str([round(intervalos[i][0], ndigits=3),round(intervalos[i][1], ndigits=3)]))
    return str_intervalos

frecuencias, intervalosComplejos = contar_frecuencias(intervalovichs, arr_np)
#Eliminar el ultimo elemento de la lista de frecuencias
# frecuencias.pop()

print(frecuencias)
30 == sum(frecuencias)

intervalosString = str_intervalos(intervalosComplejos)
auxIntervalo = []
for i in range(len(intervalovichs)-1):
    auxIntervalo.append(intervalovichs[i])



#Histograma

plt.hist(arr_np, bins=intervalovichs, align='left', edgecolor='black')
plt.title('Histograma')
plt.xlabel('Intervalos de clase')
plt.ylabel('Frecuencia')
plt.xticks(labels=intervalosString, ticks=auxIntervalo)
plt.show()

# Poligono de frecuencias
auxIntervaloString = []
auxIntervaloString = intervalosString.copy()
auxFreq = []
auxFreq = frecuencias.copy()
auxIntervaloString.append('  ')
auxIntervaloString.insert(0,' ')
auxFreq.insert(0, 0.00001)
auxFreq.append(0)
# Agregar en la 

plt.plot(auxIntervaloString, auxFreq, 'o-')
plt.title('Poligono de frecuencias')
plt.xlabel('Intervalos de clase')
plt.ylabel('Frecuencia')
plt.show()



# Calcular la media aritmética
media = stat.mean(arr_np)
print("La media aritmética es: ", media)

# Calcular la mediana
mediana = stat.median(arr_np)
print("La mediana es: ", mediana)

# Calcular la moda
moda = stat.mode(arr_np)
print("La moda es: ", moda)
medAbajo = []
medArriba = []
for num in arr_np:
    if num < mediana:
        medAbajo.append(num)

    elif num > mediana:
        medArriba.append(num)
#Se calcula q1 y q2
q1 = stat.median(medAbajo)
q2 = stat.median(medArriba)
print("Q1: ", q1)
print("Q3: ", q2)
#Se calcula desviacion media
desvMedia = 0
for num in arr_np:
    desvMedia += abs(num - media)
desvMedia = desvMedia / len(arr_np)
print("Desviacion media: ", desvMedia)
#Desviacion estandar
desvEstandar = 0
for num in arr_np:
    desvEstandar += (num - media) ** 2
desvEstandar = desvEstandar / len(arr_np)
desvEstandar = math.sqrt(desvEstandar)
print("Desviacion estandar: ", desvEstandar)

#Se calcula la variabilidad
variabilidad = 0
for num in arr_np:
    variabilidad += (num - media) ** 2
variabilidad = variabilidad / len(arr_np)
print("Variabilidad: ", variabilidad)
print("El rango es: ", rango)
print('Tabla de frecuencias: ')
tabla_frecuencias(intervalosString, frecuencias)



