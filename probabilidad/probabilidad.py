def Comb(n, k):
    
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return Comb(n - 1, k - 1) + Comb(n - 1, k)

# print('------2 contadores 3 lisiados------')
# print(Comb(5,2)*Comb(9,3))
# print('---------Exactamente 2 contadores----------')
# print((Comb(5,2)*Comb(9,3))/Comb(14,5))
# print('---------Ningun contador------------')
# print((Comb(5,0)*Comb(9,5))/Comb(14,5))
# print('---------Ningun lisiado-------------')
# print((Comb(5,5)*Comb(9,0))/Comb(14,5))



def calcular_esperanza_varianza(datos):
    esperanza = 0
    for i in range(len(datos)):
        esperanza = esperanza + i*datos[i] 
    
    varianza= 0
    for i in range(len(datos)):
        varianza = varianza + ((i-esperanza)**2)*datos[i]

    return esperanza, varianza


# mis_datos = [1/8,3/8,3/8,1/8]
# mi_esperanza, mi_varianza = calcular_esperanza_varianza(mis_datos)
# print('-------------------------------------------------------')
# print("La esperanza matemática es:", mi_esperanza)
# print("La varianza es:", mi_varianza)

