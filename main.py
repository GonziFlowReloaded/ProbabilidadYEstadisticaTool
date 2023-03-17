import math
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

datos = """
147 95 93 127 143 101 123 73 135 129
185 92 115 126 157 93 133 51 125 132
"""

elementos = datos.replace(',', '').split()

#Aqui se convierte la lista de string a lista de float

arr_np = np.array(elementos, dtype=np.float32)


mayor = arr_np.max()
menor = arr_np.min()
print(arr_np)
print(sorted(arr_np))

print("El mayor valor es: ", mayor)
print("El menor valor es: ", menor)
print("El numero de elementos es: ", len(elementos))
k = 1 + 3.322 * math.log10(len(elementos))
k = round(k)


l = (float(mayor) - float(menor)) / k
l = round(l)

print("El valor de k es: ", k)
print("El valor de l(amplitud) es: ", l)
rango = mayor - menor
print("El rango es: ", rango)

#Aqui se forman los intervalos de clase
intervalos = []
for i in range(int(k)):
    intervalos.append([menor + i * l, menor + (i + 1) * l])

print("Los intervalos de clase son: ", intervalos)

def sturges_bins(data):
    n = len(data)
    k = int(1 + np.log2(n))
    range_data = max(data) - min(data)
    bin_width = range_data / k
    bins = [(min(data) + i * bin_width, min(data) + (i + 1) * bin_width) for i in range(k)]
    bins = [(round(b[0]), round(b[1])) for b in bins] # Redondear para evitar decimales extraños

    hist, _ = np.histogram(data, bins=[b[0] for b in bins] + [bins[-1][1]])

    # Imprimir los intervalos de clase y su frecuencia
    for i, bin in enumerate(bins):
        print(f"Intervalo {i+1}: {bin[0]} - {bin[1]} Posee: {hist[i]}")
    
    return bins, hist

intervalovichs, hist = sturges_bins(arr_np)
nombreIntervalos = []
for i in range(len(intervalovichs)):
    nombreIntervalos.append([intervalovichs[i][0], intervalovichs[i][1], hist[i]])




plt.plot([i[0] for i in intervalovichs], hist, 'o-')
plt.title('Poligono de frecuencias')
plt.xlabel('Intervalos de clase')
plt.ylabel('Frecuencia')

plt.show()

plt.hist(arr_np, bins=[i[0] for i in intervalovichs]+[intervalovichs[-1][1]], edgecolor='black', align='left')
plt.title('Histograma')
plt.xlabel('Intervalos de clase')
plt.ylabel('Frecuencia')
plt.xticks([i[0] for i in intervalovichs], [f"{i[0]} - {i[1]}" for i in intervalovichs], )
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
print("Q2: ", q2)
