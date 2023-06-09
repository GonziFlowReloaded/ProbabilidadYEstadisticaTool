from prettytable import PrettyTable

datos = """
GBR
NY
FRA
MI
NY
WI
NJ
CA
GBR
NED
B.C
GBR
ITA
NY
NY
GER
NY
FRA
NY
SWE
NY
DEN
NED
NJ
FL
GER
GBR
GBR
NED
CA
BRA
VA
NY
FRA
NED
MA
PR
NY
KY
ITA
IL
NY
NY
NY
RSA
GBR
NY
NY
ITA
MA
NY
CA
CAN
GA
GBR
NY
MA
NY
FRA
MEX
GBR
MEX
NY
NY
NED
CT
NY
NY
NY
FRA
NY
MA
NY
GBR
MEX
GBR
ITA
KOR
GBR
MEX
SWE
GER
NY
GER
RSA
NY
NY
FRA
ITA
GBR
GBR
NED
MO
NY
NM
NY
GBR
NY
NY
NZL
GBR
NY
LAN
JPN
GER
GER
ITA
NJ
NY
FRA
NY
IL
ESP
NY
FRA
MI
MEX
ITA
GBR
NJ
MI
CAN
PA
NY
FRA
SUI
NY
NY
OR
TX
FL
NY
LA
NY
CAN
GBR
ITA
NY
FL
DEN
NY
FRA
SUI
NY
NY
GER
NJ
FRA
NJ
MA
VEN
FRA
FRA
NY
NY
NY
NY
GA
NED
MEX
NY
CA
FL
FRA
NJ
GBR
TX
FRA
NY
GBR
ITA
PER
NY
IL
GA
NY
IRL
GBR
GER
NY
NJ
JPN
MEX
NJ
MN
MN
FRA
IL
NY
DC
FRA
NED
NY
NJ
CA
NY
TN
NC
GBR
GA
MA
NY
NY
DC
FIN
NJ
MA
CA
FRA
JPN
NED
GBR
NJ
TX
FRA
NY
CA
CAN
MA
NY
PA
NY
NED
NOR
CT
FRA
CT
NJ
FL
FL
GBR
NED
NY
CA
NY
ITA
ITA
GBR
FRA
VEN
NY
OH
CA
DEN
JPN
NJ
IRL
NJ
ESP
CA

NY
ITA
NY
NY
NY
NED
FRA
OR
NY
NY
ITA
FL
NY
NY
NY
OH
MO
MA
FRA
IRL
GBR
FL
GBR
NY
NY
NY
MA
NJ
NJ
JPN
ARG
LA
NY
GBR
NY
ITA
NY
NY
GER
NY
NED
PA
CHI
AUS
NJ
NY
NJ
NJ
NY
PR
BEL
MA
GBR
NY
GA
MEX
NY
MEX
CAN
DEN
GBR
VA
ITA
IL
CA
NJ
GER
FRA
TX
NJ
CA
NY
NY
NY
NY
MI
NY
FL
GBR
VEN
MA
NY
FRA
CT
GBR
NY
ITA
FRA
NY
WA
IL
FRA
PA
FRA
NY
NY
VEN
NY
GER
GBR
IL
FRA
CHI
WA
VA
DC
ITA
FIN
ITA
NY
NY
CAN
NY
ITA
ITA
NED
NY
GA
MD
NC
AZ
GER
VA
SUI
NY
TX
CA
FRA
GBR
NY
TX
GBR
NY
MD
NY
TX
NY
CA
TX
NY
NOR
CT
MEX
SD
PER
DEN
FRA
FRA
GER
GBR
CT
ITA
MA
NY
NY
NY
NJ
VA
NY
ESP
NJ
ITA
NY
NY
OR
FRA
FRA
NY
NED
NJ
NY
AUT
CAN
SC
CAN
NED
VA
PER
CA
SWE
CAN
NY
ARG
SUI
NJ
PA
NY
ITA
WA
NY
GER
NY
NY
SUI
FRA
NOR
NY
NY
GBR
NY
GBR
NY
NJ
SWE
NY
NJ
NJ
NY
NY
ID
NY
GBR
MI
CAN
NY
NY
FRA
NED
VT
NJ
NJ
GBR
ITA
SWE
GBR
PER
NY
NY
CT
CA
NY
NY
NY
NY
PA
GBR
CA
NY
NJ
COL
ME
NY
NJ
NY
FRA
CA
NY
ITA
NOR
NY
FRA
NY
MA
NY
VA
NJ
CA
MN
CT
CT
NY
WI
PA
SC
PHI
BRA
CT
GBR
CA
GBR
NY
NJ
NED
MD
CO
CAN
GBR
CT
NED
FRA
GBR
NY
MEX
NED
NY
CT
CAN
GBR
MD
NY
CT
GER
TX
GBR
GBR
NY
VA
NY
NY
NY
FRA
NY
GBR
DC
NY
MA
NY
FL
ITA
GBR
NY
ITA
NY
GBR
ITA
SUR
VEN
NY
LA
MA
GBR
GBR
NJ
ITA
ITA
GA
NY
CAN
CA
ITA
NY
VA
FL
GBR
IRL
NJ
NY
RSA
ITA
NY
FRA
FRA
NJ
NY
CA
ITA
NY
GER
FRA
CT
NJ
GBR
NY
IL
MN
CO
CAN
MA
NY
NJ
CO
GBR
NY
NY
MEX
FRA
FRA
NY
ESP
NY
GBR
GBR
VT
NY
ITA
NY
ITA
NY
MA
FRA
NY
FL
GBR
GER
GBR
GBR
NY
NY
CAN
NY
NC
IL
ITA
VEN
TX
AUS
GBR
NED
FRA
NY
NJ
GBR
NJ
JPN
GA
NY
MEX
VA
ITA
GBR
BRA
FRA
NY
NY
CA
CAN
PA
MA
MO
NY
GER
NY
NED
NY
FRA
NJ
FRA
FRA
NY
NY
SWE
NY
NY
VEN
NJ
RSA
GBR
ITA
NY
ITA
NED
OH
NED
NED
NY
NY
NY
NY
NY
NY
JPN
NY
NY
NJ
ARG
FRA
IL
FIN
NJ
NED
NJ
CA
GER
NY
NED
TX
NY
GER
NY
NY
GBR
MO
NY
NY
IRL
NED
NY
NY
NJ
GBR
BRA
GBR
NY
COL
CO
NY
NY
CA
NY
OR
GBR
NY
SUI
ITA
MI
FRA
TX
SUR
GBR
GER
NY
ITA
NZL
NY
CA
LUX
WA
PR
NY
NJ
ITA
LUX
GBR
NED
AK
ITA
FL
NY
SUI
NY
GBR
NY
GAU
NY
GBR
NY
NY
NY
CA
GBR
FRA
NY
SUI
VEN
CA
DEN
CAN
ITA
FL
NED
NJ
CA
SUI
GA
NJ
MA
FRA
NY
FRA
NY
GBR
PA
CO
NY
NY
NJ
NY
NY
DEN
CA
FRA
CA
NY
NY
NED
SUI
NY
NED
NY
TX
GBR
NED
NY
NY
GBR
FL
NY
NY
NED
NY
NY
AUT
NY
RSA
FRA
WA
CA
ITA
ITA
NY
ITA
NY
GBR
NY
NY
MEX
NC
MA
NY
CA
NJ
TN
IL
BER
NED
CA
NJ
WI
VA
AUS
GBR
NED
VEN
ITA
MA
HI
NC
NY
ITA
GA
PAR
FRA
NY
FRA
NJ
GBR
FRA
NY
NOR
NED
CA
JPN
FRA
NY
CA
FRA
NY
NY
MEX
FRA
TN
NY
NY
NY
GER
NY
NED
NY
GER
NJ
NY
NY
NY
MA
NY
NY
GBR
FRA
FRA
CT
NM
GER
NY
NOR
ESP
JPN
NY
GBR
GBR
NY
MA
FRA
FRA
GBR
GBR
CA
NY
NY
NY
DC
NJ
AUT
NY
CT
CA
PER
NY
NY
PER
NY
TX
NY
GER
MN
CT
NY
IL
NJ
NY
NY
MD
FRA
AUT
NH
TX
CA
NY
GER
NY
NJ
NY
CT
OR
SUI
NJ
NY
CAN
TX
CA
GBR
NY
MA
ITA
MI
NY
CT
NY
CT
NY
NJ
FL
NY
FRA
ESP
ITA
SUI
MA
IN
NED
ITA
NY
TN
GER
NY
CAN
FRA
GBR
IRL
NY
GER

"""
elementos = datos.split()

arrayPaises = []
arrayPaises.append('EEUU')

for elemento in elementos:
    if elemento not in arrayPaises and len(elemento) == 3:
        arrayPaises.append(elemento)

arrayFreq = []
contador = 0
for elemento in elementos:
    if len(elemento) == 2:
        contador += 1

arrayFreq.append(contador)

for pais in arrayPaises:
    contador = 0
    for elemento in elementos:
        if elemento == pais:
            contador += 1
    arrayFreq.append(contador)

# print(arrayPaises)
# print(arrayFreq)
print(sum(arrayFreq))
del arrayFreq[1]


def tablaFrecuencias(paises, freq):
    n = len(paises)
    tabla = PrettyTable()
    tabla.add_column('País', paises)
    tabla.add_column('Frecuencia Absoluta', freq)

    # Calcular frecuencia relativa
    freq_relativa = [f / 1000 for f in freq]
    tabla.add_column('Frecuencia Relativa', freq_relativa)

    # Calcular frecuencia acumulativa absoluta
    freq_acum_abs = [sum(freq[:i+1]) for i in range(n)]
    tabla.add_column('Frecuencia Acumulativa Absoluta', freq_acum_abs)

    # Calcular frecuencia porcentual
    freq_porcentual = [f * 100 for f in freq_relativa]
    tabla.add_column('Frecuencia Porcentual', freq_porcentual)

    # Calcular frecuencia acumulativa porcentual
    freq_acum_porcentual = [round(sum(freq_porcentual[:i+1]), ndigits=3) for i in range(n)]
    tabla.add_column('Frecuencia Acumulativa Porcentual', freq_acum_porcentual)


    print(tabla)


tablaFrecuencias(arrayPaises, arrayFreq)