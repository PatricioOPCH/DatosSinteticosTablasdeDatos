import json

def contar_elementos_json(direccion_json):
    with open(direccion_json, 'r', encoding='utf-8') as file:  # Especifica la codificación como 'utf-8'
        data = json.load(file)
        num_elementos = len(data["muestras"])
        return num_elementos

direccion = "Datos bibliograficos Personas Relevantes"

# Ejemplo de uso:
direccion_json = "./TopicosDeTablas/"+direccion+"/TresColumnasTresFilas.json"  # Reemplaza con la dirección correcta

direccion_test = "entrenamiento.json"  # Reemplaza con la dirección correcta
direccion_test1 = "test.json"
direccion_test2 = "validacion.json"
direccion_datasetFinal = "datasetfinal.json"
cantidad_elementos1 = contar_elementos_json(direccion_test  )
cantidad_elementos2 = contar_elementos_json(direccion_test1  )
#cantidad_elementos3 = contar_elementos_json(direccion_test2 )

cantidad_elementos3 = contar_elementos_json(direccion_json )
#print("Número de elementos dentro del arreglo 'muestras':", cantidad_elementos1 )
#print("Número de elementos dentro del arreglo 'muestras':", cantidad_elementos2 )
#print("Número de elementos dentro del arreglo 'muestras':", cantidad_elementos3 )

print("Número de elementos 'muestras':", cantidad_elementos3 )
