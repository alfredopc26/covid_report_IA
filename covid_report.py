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
data.groupby('Ubicación del caso').size()
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
data['Ubicación del caso'].replace('casa','Casa',inplace=True)
Ub_caso = data[(data['Ubicación del caso'] == 'Casa')]
Ub_caso.groupby('Ubicación del caso').size()
print(f"El numero de personas en casa es: {Ub_caso.Casa}")


# Número de personas que se encuentran recuperados
filtered = data.query(" Recuperado=='Recuperado' ")
fil = filtered.Recuperado.value_counts()

print(f"El numero de personas Recuperadas es: {fil.Recuperado}")


# Número de personas que ha fallecido
filtered = data.query(" Recuperado=='Fallecido' ")
fil = filtered.Recuperado.value_counts()

print(f"El numero de personas Recuperadas es: {fil.Fallecido}")

# Ordenar de Mayor a menor por tipo de caso 
# (Importado, en estudio, Relacionado)
Tipo_contagio = data[(data['Tipo de contagio'] == 'Importado') | 
(data['Tipo de contagio'] == 'En estudio') | 
(data['Tipo de contagio'] == 'Relacionado')]
Tipo_contagio.groupby('Tipo de contagio').size().sort_values(ascending=True)

# 8. Número de departamentos afectados
data.groupby('Nombre departamento').size().count()

# 9. Liste los departamentos afectados(sin repetirlos)
print_array(data['Nombre departamento'].unique())

# 10 Ordene de mayor a menor por tipo de atención
Tipo_contagio.groupby('Tipo de contagio').size().sort_values(ascending=False)

# 11 Liste de mayor a menor los 10 departamentos con mas casos de contagiados
Dpto_size = data.groupby('Nombre departamento').size()
Dpto_size.sort_values(ascending = False).head(10)

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
fallecido = data[(data['Estado'] == 'Fallecido')]
f_dpto = fallecido.groupby('Nombre departamento').size()
f_dpto.sort_values(ascending = False).head(10)

#13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
recuperado = data[(data['Recuperado'] == 'Recuperado')]
r_dpto = recuperado.groupby('Nombre departamento').size()
r_dpto.sort_values(ascending = False).head(10)

#14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
Mun_size = data.groupby('Nombre municipio').size()
Mun_size.sort_values(ascending = False).head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
f_mun = fallecido.groupby('Nombre municipio').size()
f_mun.sort_values(ascending = False).head(10)

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
r_mun = recuperado.groupby('Nombre municipio').size()
r_mun.sort_values(ascending = False).head(10)

# 17. Liste agrupado por departamento y en orden de Mayor a menor las 
# ciudades con mas casos de contagiados

def group_dep(array):    
    
    for dept in array:
        print(dept)
        print("***----***")
        contagio = data[(data['Nombre departamento'] == dept )]
        a_mun = contagio.groupby('Nombre municipio').size()
        array_num = a_mun.sort_values(ascending = False)
        print(array_num)
        print("***----***")
        
group_dep(data['Nombre departamento'].unique())

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento

data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por
# ciudad por departamento

fil = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])
print(fil['Edad'].mean())

# 20. Liste de mayor a menor el número de contagiados por país de procedencia

pais_size = data.groupby('Nombre del país').size()
pais_size.sort_values(ascending = False)

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios

fecha_size = data.groupby('Fecha de diagnóstico').size()
fecha_size.sort_values(ascending = False)

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
filtered = data.query(" Recuperado=='Fallecido' or  Recuperado=='Recuperado'")
tasa = filtered.Recuperado.value_counts()

print(f"La tasa de mortalidad es: {tasa.Fallecido/num_casos}")
print(f"La tasa de recuperación es: {tasa.Recuperado/num_casos}")

# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento
def tasa_dept(array):
    
    for dept in array:
        print(dept)
        print("***----***")
        dep = data[(data['Nombre departamento'] == dept )]
        filtered = dep.query(" Recuperado=='Fallecido' or  Recuperado=='Recuperado'")
        tasa = filtered.Recuperado.value_counts()

        print(f"La tasa de mortalidad es: {tasa.Fallecido/num_casos}")
        print(f"La tasa de recuperación es: {tasa.Recuperado/num_casos}")
        print("***----***")
    

tasa_dept(data['Nombre departamento'].unique())