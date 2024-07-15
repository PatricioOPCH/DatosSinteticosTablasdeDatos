import json

# Leer el archivo JSON de entrada en codificación UTF-8
with open("datos_tematicas_nuevas.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Crear una nueva lista de muestras con codificación UTF-8
new_muestras = []
for muestra in data["muestras"]:
    new_table = muestra["table"]
    new_texto = muestra["texto"]
    new_orden = muestra["orden"]
    new_muestra = {
        "id": muestra["id"],
        "table": new_table,
        "texto": new_texto,
        "orden": new_orden
    }
    new_muestras.append(new_muestra)

# Crear el nuevo diccionario con la lista de muestras en UTF-8
new_data = {
    "muestras": new_muestras
}

# Escribir el nuevo archivo JSON en codificación UTF-8
with open("datos_tematicas_nuevas_decodificado.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)

print("Archivo 'datos_tematicas_nuevas.json' generado exitosamente.")