import random
import numpy as np
import json

# Definir la semilla para replicabilidad
seed = 12345

# Cargar el JSON original
with open("transcrito.json", "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

# Obtener el total de elementos
total_elementos = len(data["muestras"])

# Calcular la cantidad de elementos a seleccionar (10%)
elementos_a_seleccionar = int(0.1 * total_elementos)

# Seleccionar aleatoriamente los elementos con la semilla indicada
random.seed(seed)
indices_seleccionados = random.sample(range(total_elementos), elementos_a_seleccionar)

# Crear el nuevo JSON ("muestra_para_revision_humana")
muestra_revision_humana = {"muestras": []}

for indice in indices_seleccionados:
    muestra_revision_humana["muestras"].append(data["muestras"][indice])

# Guardar el nuevo JSON en un archivo
with open("muestra_para_revision_humana.json", "w", encoding="utf-8") as archivo:
    json.dump(muestra_revision_humana, archivo, indent=4)

