import json
import os
import random

# Directorio que contiene los archivos JSON
directorio1 = './TopicosDeTablas/Ciencia y Tecnología'
directorio2 = './TopicosDeTablas/Datos bibliograficos Personas Relevantes'
directorio3 = './TopicosDeTablas/Datos Demográficos Globales'
directorio4 = './TopicosDeTablas/Educación y Cultura en el Mundo'
directorio5 = './TopicosDeTablas/Medio Ambiente,Animales, Plantas y Sostenibilidad'


# Lista para almacenar todas las muestras combinadas
muestras_combinadas = []

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(directorio1):
    if filename.endswith('.json'):
        with open(os.path.join(directorio1, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])
            print(len(data['muestras']))

# Iterar sobre cada archivo en el directorio
for filename1 in os.listdir(directorio2):
    if filename1.endswith('.json'):
        with open(os.path.join(directorio2, filename1), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])
            print(len(data['muestras']))

# Iterar sobre cada archivo en el directorio
for filename2 in os.listdir(directorio3):
    if filename2.endswith('.json'):
        with open(os.path.join(directorio3, filename2), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])
            print(len(data['muestras']))

# Iterar sobre cada archivo en el directorio
for filename3 in os.listdir(directorio4):
    if filename3.endswith('.json'):
        with open(os.path.join(directorio4, filename3), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])
            print(len(data['muestras']))

# Iterar sobre cada archivo en el directorio
for filename4 in os.listdir(directorio5):
    if filename4.endswith('.json'):
        with open(os.path.join(directorio5, filename4), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])
            print(len(data['muestras']))





# Revolver los elementos de manera aleatoria
random.shuffle(muestras_combinadas)

# Obtener el tamaño de cada conjunto
total_elementos = len(muestras_combinadas)
print("total de muestras: ",len(muestras_combinadas))
entrenamiento_size = int(0.8 * total_elementos)
validacion_size = int(0.1 * total_elementos)
test_size = total_elementos - entrenamiento_size - validacion_size

#Dividir los datos en conjuntos de entrenamiento, validación y test
conjunto_entrenamiento = muestras_combinadas[:entrenamiento_size]
conjunto_validacion = muestras_combinadas[entrenamiento_size:entrenamiento_size + validacion_size]
conjunto_test = muestras_combinadas[entrenamiento_size + validacion_size:]

# Crear los nuevos JSONs
with open('entrenamiento.json', 'w') as f:
    json.dump({'muestras': conjunto_entrenamiento}, f, indent=4)

with open('validacion.json', 'w') as f:
    json.dump({'muestras': conjunto_validacion}, f, indent=4)

with open('test.json', 'w') as f:
    json.dump({'muestras': conjunto_test}, f, indent=4)

print("Se han creado los archivos 'entrenamiento.json', 'validacion.json' y 'test.json' con los conjuntos de datos divididos correctamente.")
