import os
import json
import uuid
import pathlib
import textwrap
import google.generativeai as genai

# Used to securely store your API key
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return text

genai.configure(api_key="AIzaSyCou9G86XNV-X_L1-_BTeoGi7F4cq55AoM")
model = genai.GenerativeModel('gemini-pro')

def agregar_o_crear_json(input_text, file_path):
    try:
        if '?' not in input_text:
            raise ValueError("El carácter '?' no encontrado en el texto de entrada.")

        table, text = input_text.split('?', 1)
        table = table.strip()
        text = text.strip()

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data["muestras"].append({
                    "id": str(uuid.uuid4()),
                    "table": table,
                    "texto": text
                })
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            data = {
                "muestras": [
                    {
                        "id": str(uuid.uuid4()),
                        "table": table,
                        "texto": text
                    }
                ]
            }
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

    except ValueError as e:
        print(f"Error al procesar '{file_path}': {e}")
        return

#promt = "ede"


#response = model.generate_content(promt)
#agregar_o_crear_json(limpiarcadenaDeasteriscos(limpiar_cadena(normalize_text(str(to_markdown(response.text))))), file_path)

# Leer el archivo JSON de nombre "transcrito.json"
with open("transcrito.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Leer las respuestas del modelo desde el archivo "respuestas.txt"
with open("respuestas.txt", "r", encoding="utf-8") as file:
    model_responses = file.read().splitlines()

# Crear una nueva lista de muestras con la evaluación humana
new_muestras = []
orden = 1
import time
for i, muestra in enumerate(data["muestras"]):
    referencia = muestra["texto"]
    respuesta_modelo = model_responses[i]
    # Esperar 10 segundos antes de procesar otra consulta

    time.sleep(20)
    # Llamar al modelo con un prompt que incluya la salida del modelo y la referencia
    prompt = f"Teniendo en cuenta esta salida del modelo '{respuesta_modelo}' y esta referencia '{referencia}', califica: Califica cada salida en una escala de 1 a 5, donde 1 significa 'Contiene muchas alucinaciones' y 5 significa 'No contiene alucinaciones'. Se calificara en este orden: integridad_informacion , coherencia_fluidez , precision_significado , alucinaciones y que le texto de salida tenga el formato: numero_asigando_para_integridad_informacion\nnumero_asigando_para_coherencia_fluidez\nnumero_asigando_para_precision_significado\nnumero_asigando_alucinaciones"
    response = model.generate_content(prompt)
    model_output = response.text.strip()

    # Procesar la respuesta del modelo
    # Procesar la respuesta del modelo
    try:
        output_lines = model_output.split("\n")
        if len(output_lines) != 4:
            raise ValueError("La respuesta del modelo no tiene el formato esperado.")

        integridad_informacion = int(output_lines[0].split(":")[1].strip().replace("%", ""))
        coherencia_fluidez = int(output_lines[1].split(":")[1].strip().replace("%", ""))
        precision_significado = int(output_lines[2].split(":")[1].strip().replace("%", ""))
        alucinaciones = int(output_lines[3].split(":")[1].strip().replace("%", ""))
        print(f"Formato aceptado: {integridad_informacion}%, {coherencia_fluidez}%, {precision_significado}%, {alucinaciones}")
    except (ValueError, IndexError):
        print(f"Error al procesar la respuesta del modelo: {model_output}")
        continue

    new_muestra = {
        "id": muestra["id"],
        "table": muestra["table"],
        "Ouput del modelo": respuesta_modelo,
        "referencia": referencia,
        "integridad_informacion": integridad_informacion,
        "coherencia_fluidez": coherencia_fluidez,
        "precision_significado": precision_significado,
        "alucinaciones": alucinaciones,
        "orden": orden,
        "valoracion promedio": (integridad_informacion + coherencia_fluidez + precision_significado + alucinaciones) / 4
    }
    new_muestras.append(new_muestra)
    orden += 1

# Crear el nuevo diccionario con la lista de muestras evaluadas
new_data = {
    "muestras": new_muestras
}

# Escribir el nuevo archivo JSON en codificación UTF-8
with open("evaluacion_humana.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)

print("Archivo 'evaluacion_humana.json' generado exitosamente.")