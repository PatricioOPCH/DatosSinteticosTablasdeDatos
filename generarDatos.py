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

genai.configure(api_key="Colocar llave de API de Gemma")

model = genai.GenerativeModel('gemini-pro')


def agregar_o_crear_json(input_text, file_path):
    try:
        # Intenta dividir la cadena solo en la primera aparición del carácter '?'
        if '?' not in input_text:
            raise ValueError("El carácter '?' no encontrado en el texto de entrada.")

        table, text = input_text.split('?', 1)
        # Elimina espacios en blanco alrededor de 'table' y 'text'
        table = table.strip()
        text = text.strip()

        # Verificar si el archivo JSON ya existe
        if os.path.exists(file_path):
            # Si el archivo ya existe, cargar el JSON y añadir el nuevo objeto
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data["muestras"].append({
                    "id": str(uuid.uuid4()),
                    "table": table,
                    "texto": text
                })
            # Escribir los datos actualizados de vuelta al archivo JSON
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            # Si el archivo no existe, crear un nuevo archivo JSON con el objeto
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
        # Si ocurre un error, imprimir un mensaje de error con información detallada
        print(f"Error al procesar '{file_path}': {e}")
        return


import time



import unicodedata


def normalize_text(text):
    return unicodedata.normalize('NFD', text)

def limpiar_cadena(cadena):
    return cadena.replace('\n', '')
def limpiarcadenaDeasteriscos(cadena):
    return cadena.replace('*', '')

def colocarSaltodeLineaEnCadena(cadena):
    return cadena.replace('||', '|\n|')

def modificar_json(json_file_path, overwrite=False, output_file_path=None):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    for muestra in json_data["muestras"]:
        muestra["table"] = muestra["table"].replace("|", "-")
        muestra["texto"] = muestra["texto"].upper()

    if overwrite:
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
    elif output_file_path:
        with open(output_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
    else:
        raise ValueError("Debe especificar si desea sobrescribir el archivo original o proporcionar una ruta de salida para los cambios.")




def modificar_json(json_file_path, overwrite=False, output_file_path=None):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    for muestra in json_data["muestras"]:
        lines = muestra["table"].split("\n")
        filtered_lines = [line for line in lines if "|||" not in line]
        muestra["table"] = "\n".join(filtered_lines)

    # Escribir los cambios al archivo
    if overwrite:
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
    elif output_file_path:
        with open(output_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
    else:
        raise ValueError("Debe especificar si desea sobrescribir el archivo original o proporcionar una ruta de salida para los cambios.")










"""
Promprt utilizados en la generación de los datos, su uso es uno a la vez por lo que se comentan los demas que no se encuentan en uso
"""

#prompt_Unafila_TresCOLUMNAS= "genera una tabla de una fila con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla ten en cuenta de detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que no se omita información, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | Películas | Año | Actor || --- | --- | --- || Luna | 1999 | Juan Castillo |$La película Luna de 1999  contó con el actor Juan Castillo"
#prompt_Tresfila_TresCOLUMNAS = "genera una tabla de tres fila con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | Películas | Año | Actor || --- | --- | --- || Luna | 1999 | Juan Castillo || El secreto de sus ojos | 2009 | Ricardo Darín || Los reyes del mundo | 2022 | Carlos Andrés Castañeda | $ la película Luna de 1999  contó con el actor Juan Castillo, la película El secreto de sus ojos del 2009 contó con el actor Ricardo Darín y la película Los reyes del mundo del 2022 contó con el actor Carlos Andrés Castañeda "
#prompt_Tresfila_DosCOLUMNAS= "genera una tabla de tres fila, dos columnas con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla ten en cuenta de detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que no se omita información, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | País     | Capital || -------- | ------- || Francia  | París   || Italia   | Roma    || Japón    | Tokio   |$El país de Francia tiene por capital a París, el país de Italia tiene por capital a Roma y el país de Japón tiene por capital a Tokio"
#prompt_Dosfila_DosCOLUMNAS= "genera una tabla de dos fila, dos columnas con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla ten en cuenta de detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que no se omita información, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | País     | Capital || -------- | ------- || Francia  | París   || Italia   | Roma    |$El país de Francia tiene por capital a París y el país de Italia tiene por capital a Roma "
#prompt_Unafila_DosCOLUMNAS= "genera una tabla de Una fila, dos columnas con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla ten en cuenta de detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que no se omita información, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | País     | Capital || -------- | ------- || Francia  | París   |$El país de Francia tiene por capital a París "
#prompt_Tresfila_UnaCOLUMNAS= "genera una tabla de Una fila, dos columnas con datos aleatorios de tematicas diversas después una oración que describa el contenido de la tabla ten en cuenta de detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que no se omita información, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con $ como este ejemplo, respeta el formato que te di de ejemplo: | Películas               ||-------------------------|| Luna                    || El secreto de sus ojos || Los reyes del mundo     |$Las películas son: Luna, El secreto de sus ojos, Los reyes del mundo"
#origprompt_Tresfila_TresCOLUMNAS= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe ser de tres fila y tres columnas con informacion relacionada a la tematica " + topicoTabla + " después una oración que describa el contenido de la tabla ten en cuenta en detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que la información se presente detalladamente, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con & como este ejemplo, respeta el formato que te di de ejemplo: | Continente | Población (millones) | Idiomas principales                         ||------------|-----------------------|--------------------------------------------|| África     | 1.440                 | Árabe, Suahili, Inglés, Francés, Portugués || Asia       | 4.690                 | Chino mandarín, Hindi, Inglés, Bengalí, Español || Europa     | 747                   | Ruso, Inglés, Alemán, Francés, Italiano     |"
#prompt_Tresfila_TresCOLUMNAS= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe ser de una fila y una columna con informacion relacionada a la tematica " + topicoTabla + " después una oración que describa el contenido de la tabla ten en cuenta en detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que la información se presente detalladamente, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con & "
#prompt_Tresfila_doscolumnas= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe ser de tres fila y tres columnas con informacion relacionada a la tematica " + topicoTabla + " después una oración que describa el contenido de la tabla ten en cuenta en detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que la información se presente detalladamente, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con & "
#prompt_Tresfila_TresCOLUMNAS= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe ser de dos fila y dos columna con informacion relacionada a la tematica " + topicoTabla + " después una oración que describa el contenido de la tabla fila por fila ten en cuenta en detallar completamente la infromacion de la tabla pues es para narrarla a personas con discacidad visual por lo que es importante que la información se presente detalladamente, no pongas la tabla contiene, narra directamente la infromacion de la tabla para la descripcion solo usa la infromaacion contenida en la tabla, no pongas en la tabla saltos de linea asi \n , separa la tabla de la descripcion con ? , en tu respuesta respeta no tengas falta de ortografia es decir respeta tildes"


# La varible topicoTabla fué muy utlizada en este proceso debido a que si ella la 
# repetición de tablas era contante este permitio enriqueser los datos generados 
# y controlar las tematicas de las columnas de las tablas de datos

topicoTabla = ". los temas de las columas de las tablas son: Ventajas, Desventajas. por fila nombra una ventaja y desventaja de la educación online."


#ejemploTabla3filas2columnas= "| Enfermedades digestivas | Síntomas ||---|---|| Reflujo gástrico | Acidez, ardor de estómago || Síndrome del intestino irritable | Dolor abdominal, diarrea, estreñimiento || Enfermedad celíaca | Hinchazón, pérdida de peso, diarrea |?Esta tabla muestra tres enfermedades digestivas y sus síntomas asociados. La primera fila presenta el Reflujo gástrico, que se caracteriza por acidez y ardor de estómago. La segunda fila describe el Síndrome del intestino irritable, que se manifiesta con dolor abdominal, diarrea y estreñimiento. Finalmente, la tercera fila detalla la Enfermedad celíaca, cuyos síntomas incluyen hinchazón, pérdida de peso y diarrea."
#ejemploUNafilaunacoluma = "| Biografía de inventor destacado ||---|| Thomas Edison inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas. |?Esta tabla contiene una breve biografía del inventor destacado Thomas Edison, quien inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas."
#ejemplounafilastrescolumnas = "| Tecnología | Beneficios | Limitaciones ||---|---|---|| Inteligencia Artificial (IA) | Automatización de tareas, mejora de la eficiencia, toma de decisiones más informada | Sesgo potencial, alta dependencia de los datos, preocupaciones éticas |?La tabla proporciona información sobre una tecnología importante, destacando sus beneficios y limitaciones. La Inteligencia Artificial ofrece ventajas como la automatización, la eficiencia mejorada y la toma de decisiones basada en información, pero también tiene limitaciones como la de plantear preocupaciones de sesgo, alta dependencia de los datos y en la ética."
#ejemplotresfilastrescolumnasN22 = "| Tecnología | Beneficios | Limitaciones ||---|---|---|| Inteligencia Artificial (IA) | Automatización de tareas, mejora de la eficiencia, toma de decisiones más informada | Sesgo potencial, alta dependencia de los datos, preocupaciones éticas || Computación en la nube | Acceso a recursos informáticos potentes y escalables, reducción de costos, mayor flexibilidad | Posibles problemas de seguridad, latencia, dependencia de la conectividad || Internet de las cosas (IoT) | Conexión de dispositivos y recolección de datos, automatización de procesos, mejora de la experiencia del cliente | Preocupaciones de privacidad, complejidad de implementación, problemas de interoperabilidad |?La tabla proporciona información sobre tres tecnologías importantes (Inteligencia Artificial, Computación en la nube e Internet de las cosas), destacando sus beneficios y limitaciones. La Inteligencia Artificial ofrece ventajas como la automatización, la eficiencia mejorada y la toma de decisiones basada en información, pero también tiene limitaciones como la de plantear preocupaciones de sesgo, alta dependencia de los datos y en la ética. La Computación en la nube da beneficios como permitir el acceso a recursos informáticos potentes y escalables, reducción de costos, mayor flexibilidad, pero tiene limitaciones como que puede presentar problemas de seguridad, latencia y dependencia de la conectividad. El Internet de las cosas da beneficios como conectar dispositivos y recopila datos, automatización de procesos, mejora de la experiencia del cliente, pero también posee limitaciones como que genera inquietudes sobre la privacidad, complejidad de implementación, problemas de interoperabilidad."
#ejemplodosfilasunacolumnas = "| Disciplina científica y su objetivo ||------|| Biología tiene como objetivo estudiar la vida y los organismos vivos || Química tiene como objetivo estudiar la composición, estructura, propiedades y cambios de la materia |?La tabla contiene disciplinas científicas y sus objetivos. La fila superior contiene la Biología, cuyo objetivo es estudiar la vida y los organismos vivos. La fila inferior contiene la Química, cuyo objetivo es estudiar la composición, estructura, propiedades y cambios de la materia."
#ejemplotresfilaunacoluma = "| Disciplina | Enfoque ||---|---|| Biología | Estudio de los seres vivos y sus procesos |?La tabla presenta información sobre una disciplina y su enfoque: la disciplina de la biología, cuyo enfoque es el estudio de los seres vivos y sus procesos."
#ejemplotresfilasunacolumnas = "| Planetas || --- || Saturno es un planeta gaseoso con anillos || Urano es un planeta gaseoso con un eje de rotación inclinado || Plutón es un planeta enano que fue reclasificado de planeta en 2006 |?La tabla muestra tres planetas: Saturno que es un planeta gaseoso con anillos. Urano es un planeta gaseoso con un eje de rotación inclinado. Plutón es un planeta enano que fue reclasificado de planeta en 2006."



# Experimentos de prompts para mejorar los datos generdos Promts
#sintaxisTablaUnaFilaUnaColumna = "| Biografía de inventor destacado ||---|| Thomas Edison inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas. |?Esta tabla contiene una breve biografía del inventor destacado Thomas Edison, quien inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas."
#USprompt_Tresfila_TresCOLUMNAS= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe tener una columna y una fila , el cabezado de la columna tendra el tema y la fila deberan expresar informacon en relevancia con la tematica de la columna, " + topicoTabla + ", luego una oración que describa el contenido de la tabla fila por fila, usa solo la informacion puesta en la tabla no expandas el tema ,  la información se presente detalladamente pero solo en base a la informacion de la tabla no agregues infromacion que no este en la tabla, no pongas la tabla contiene, separa la tabla de la descripcion con ?, como el ejemplo:  "+ sintaxisTablaUnaFilaUnaColumna
#estructuraUnaColumnaTresFiLAS= "| País de origen de futbolistas famosos ||------|| Brasil con Pelé, Neymar Jr. || Argentina con Diego Maradona, Lionel Messi || Alemania con Franz Beckenbauer, Gerd Müller |?La tabla muestra los países de origen de futbolistas famosos, como Brasil con Pelé y Neymar Jr., Argentina con Diego Maradona y Lionel Messi, y Alemania con Franz Beckenbauer y Gerd Müller."
# Promts Datos bibliograficos Datos Demograficos globales
# prompt_Tresfila_TresCOLUMNAS= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe tener una columna y una fila , el cabezado de la columna tendra el tema y la fila deberan expresar informacon en relevancia con la tematica de la columna, " + topicoTabla + ", luego una oración que describa el contenido de la tabla fila por fila, usa solo la informacion puesta en la tabla no expandas el tema ,  la información se presente detalladamente pero solo en base a la informacion de la tabla no agregues infromacion que no este en la tabla, no pongas la tabla contiene, separa la tabla de la descripcion con ?, como el ejemplo:  "+ sintaxisTablaUnaFilaUnaColumna


# Titulo de la carpeta que seria la tematica tratada
direccion = "Educación y Cultura en el Mundo"


# Promts Datos bibliograficos Educación y Cultura en el Mundo
#sintaxis5TablaUnaFilaUnaColumna = "| Biografía de inventor destacado ||---|| Thomas Edison inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas. |?Esta tabla contiene una breve biografía del inventor destacado Thomas Edison, quien inventó la bombilla incandescente y tuvo más de 1.000 patentes registradas."
#sintaxis5TablaUnaFilatresColumna = "| Mamíferos || --- || León || Tigre |?La tabla muestra mamíferos, se nombra al león y el tigre.."
#ejemploesperanzador = "| País | PIB (miles de millones de dólares) | Indice de Desarrollo Humano ||---|---|---|| China | 14.723 | 0,761 || India | 3.186 | 0,645 || Estados Unidos | 22.675 | 0,920 |?La tabla presenta información de países, su PIB en miles de millones de dólares y su índice de desarrollo humano. China tiene un PIB de 14.723 miles de millones de dólares y un índice de desarrollo humano de 0,761. India tiene un PIB de 3.186 miles de millones de dólares y un índice de desarrollo humano de 0,645. Estados Unidos tiene un PIB de 22.675 miles de millones de dólares y un índice de desarrollo humano de 0,920."
#ejemploesperanzadortrescolumnasdosfilas = "| País | PIB (miles de millones de dólares) | Indice de Desarrollo Humano ||---|---|---|| China | 14.723 | 0,761 || India | 3.186 | 0,645 |?La tabla presenta información de países, su PIB en miles de millones de dólares y su índice de desarrollo humano. China tiene un PIB de 14.723 miles de millones de dólares y un índice de desarrollo humano de 0,761. India tiene un PIB de 3.186 miles de millones de dólares y un índice de desarrollo humano de 0,645."
#ejemplonuevo222= "| Movimiento | Autor | Obra artística ||---|---|---|| Renacimiento | Leonardo da Vinci | Mona Lisa || Barroco | Caravaggio | La vocación de San Mateo || Impresionismo | Claude Monet | Impresión, amanecer |?La tabla contiene información de movimientos, autores y obras artísticas representativas. El Renacimiento tiene al autor Leonardo da Vinci sus obras artística son la Mona Lisa. El Barroco tiene al autor Caravaggio sus obras artística son La vocación de San Mateo. El Impresionismo tiene al autor Claude Monet sus obras artística son Impresión, amanecer."

#Variable usada para determinar dentro del prompt un ejemplo de la estructura del dato a generar
ejemplo= "| Movimiento | Autor | Obra artística ||---|---|---|| Renacimiento | Leonardo da Vinci | Mona Lisa |?La tabla contiene información de movimientos, autores y obras artísticas representativas. El Renacimiento tiene al autor Leonardo da Vinci sus obras artística son la Mona Lisa."

dimensiones= "1 fila y 3 columnas"

prompt= "genera una tabla en formato marckdown escrita de manera seguida en una linea, la tabla debe tener"+dimensiones+", el cabezado de la columna tendra el tema y las filas deberan expresar informacion en relevancia con la tematica de la columna, " + topicoTabla + ", luego una oración que describa el contenido de la tabla fila por fila, usa solo la informacion puesta en la tabla no expandas el tema ,  la información se presente detalladamente pero solo en base a la informacion de la tabla no agregues infromacion que no este en la tabla, no pongas la tabla contiene, separa la tabla de la descripcion con ?, como el ejemplo:  "+ ejemplo


#Promts Medio Ambiente,Animales, Plantas y Sostenibilidad

iteraciones_totales = 1
iteraciones_por_minuto = 40
tiempo_por_iteracion = 60 / iteraciones_por_minuto  # Calcula el tiempo en segundos entre iteraciones
file_path = "./TopicosDeTablas/"+direccion+"/DosColumnasTresFilas.json"
for i in range(iteraciones_totales):
    # Hacer algo en este momento
    print(f"Iteración {i}")
    response = model.generate_content(prompt)
    agregar_o_crear_json(limpiarcadenaDeasteriscos(limpiar_cadena(normalize_text(str(to_markdown(response.text))))), file_path)
    # Hacer algo cada 40 iteraciones
    #if i % 40 == 0:        
    #    time.sleep(1)

