import statistics as stat
import numpy as np

arr_np = np.array([2 , 4 , 8 , 6 , 7 , 5 , 3])
media = stat.mean(arr_np)
print("Media: ", media)
totDesviacion = 0
for i in range(len(arr_np)):
    desviacion = arr_np[i]- media
    print("Desviacion: ", desviacion)
    totDesviacion = desviacion + totDesviacion

print("Total desviaciones: ", totDesviacion)