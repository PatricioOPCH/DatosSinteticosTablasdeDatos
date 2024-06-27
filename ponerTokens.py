import json
import jsonlines as jl

def procesar_dataset(input_json, output_jsonl):
    # Cargar el archivo JSON de entrada
    with open(input_json, 'r') as file:
        dataset = json.load(file)

    # Filtrar y transformar los datos
    filtered_dataset = []
    for _, data in enumerate(dataset["muestras"]):
        if "contexto" not in data:
            text = f"Instruction:\n{data['table']}\n\nResponse:\n{data['texto']}"
            filtered_dataset.append({"text": text})

    # Escribir el resultado en un archivo JSONL
    with jl.open(output_jsonl, 'w') as writer:
        writer.write_all(filtered_dataset)

# Direcciones de entrada y salida
#input_json = 'input.json'
#output_jsonl = 'DatosConTokens/output.jsonl'

# Llamada a la función con las direcciones definidas para datos datos de entrenamiento, validacion y test

procesar_dataset('entrenamiento.json', './datosConTokensUltimaversion/entrenamiento.jsonl')
procesar_dataset('validacion.json', './datosConTokensUltimaversion/validacion.jsonl')
procesar_dataset('test.json', './datosConTokensUltimaversion/test.jsonl')

print("Se coloco el formato con los tokens del modelo correctamente")