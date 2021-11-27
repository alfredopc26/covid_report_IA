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