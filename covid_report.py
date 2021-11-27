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