import json
import os

# Directorio que contiene los archivos JSON
directorio = './TopicosDeTablas/Ciencia y Tecnología'

# Lista para almacenar todas las muestras combinadas
muestras_combinadas = []

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(directorio):
    if filename.endswith('.json'):
        with open(os.path.join(directorio, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
            muestras_combinadas.extend(data['muestras'])

# Crear un nuevo diccionario con las muestras combinadas
nuevo_json = {'muestras': muestras_combinadas}

# Escribir el nuevo JSON en un archivo
with open('datasetfinal.json', 'w') as f:
    json.dump(nuevo_json, f, indent=4)

print("Se ha creado el nuevo archivo 'nuevo_archivo.json' con el contenido combinado de todos los archivos.")
