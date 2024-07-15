import json
import random

# Cargar el archivo JSON original
with open('transcrito.json', 'r', encoding="utf-8") as f:
    datos_originales = json.load(f)

# Convertir el diccionario en una lista
lista_datos_originales = list(datos_originales['muestras'])

print("Población: ", len(lista_datos_originales))

# Seleccionar elementos aleatorios
random.seed(12345)
elementos_aleatorios = random.sample(lista_datos_originales, 36)

print("Muestra:  ", len(elementos_aleatorios))
# Decodificar elementos UTF-8
elementos_decodificados = []
for i, muestra in enumerate(elementos_aleatorios):
    # Decodificar cada campo del elemento (table, texto, etc.)
    elemento_decodificado = {
        "id": muestra["id"],
        "table": muestra["table"],
        "texto": muestra["texto"],
        "orden": muestra["orden"]
    }
    elementos_decodificados.append(elemento_decodificado)

# Crear el nuevo diccionario con la lista de muestras en UTF-8
new_data = {
    "muestras": elementos_decodificados
}

# Escribir el nuevo archivo JSON en codificación UTF-8
with open("datos_tematicas_nuevas.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)

print("Archivo 'datos_tematicas_nuevas.json' generado exitosamente.")
