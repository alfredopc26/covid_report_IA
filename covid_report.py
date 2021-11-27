# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd


url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Número de casos de Contagiados en el País
num_casos = data.shape[0]
print(f"El numero de casos en Colombia es: {num_casos}")

# Número de Municipios Afectados
mun_afectados = data['Nombre municipio'].unique().shape[0]
print(f"El numero de municipios afectados son: {mun_afectados}")

# Liste los municipios afectados (sin repetirlos)
def print_array(array):    
    
    for x in array:
        print(x)
        
        
print_array(data['Nombre municipio'].unique())

# Número de personas que se encuentran en atención en casa
filtered = data.query("(Estado=='Leve' or Estado == 'Moderado') and Recuperado=='Activo'")
fil = filtered.Estado.value_counts()

print(f"El numero de personas en casa es: {fil.Leve + fil.Moderado}")


# Número de personas que se encuentran recuperados
filtered = data.query(" Recuperado=='Recuperado' ")
fil = filtered.Recuperado.value_counts()

print(f"El numero de personas Recuperadas es: {fil.Recuperado}")
