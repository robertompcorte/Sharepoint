# Este codigo sirve para coger el markdown sacado del conetenido del pdf
# e ir limpiando el markdonw y usable para luego poder tener categorías/temas mejor 
# organizadas y poder tener conjuntos que tengan sentido

# objetivo principal 
# Pasar de markdown puro -> markdown limpio y organizado


# importar
import re
import os

# importar input y poner output del proceso 
# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean"


# Funciones útiles para dejarl el markdown mejor

# Eliminar filas vacias en el markdown, para tener todo el texto junto y más compacto
def remove_empty_lines(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # Filtrar las líneas vacías eliminando espacios en blanco al principio y al final
    filtered_lines = [line.strip() for line in lines if line.strip()]

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(filtered_lines))



# Funcion para limpiar el texto, quitando caráctares raros o extraños

# También llama a las otras funciones para eliminar los titulos que no tengan contenido y por lo tanto no tiene potencial dividir en chunks
# que no tengan contenido porque van a ser chunks vacíos, o solo con un titulo

# La segunda función tienen el objetivo de eliminar los número de página que son redundantes porque 
# ya lo hemos agregado como un comentario

def clean_text(markdown_text):
    # Filtrar solo caracteres permitidos: letras, números, puntos, comas, letras con tildes, y otros caracteres específicos
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,áéíóúÁÉÍÓÚñÑ!?¿<>#-]', '', markdown_text)
    #cleaned_text = eliminar_titulos_sin_content(cleaned_text)
    cleaned_text = convert_empty_titles_to_normal_text(cleaned_text)

    return cleaned_text



# Esta funcion elimina lso #titulos qeu no tengan contenido es decir qeu despues del titulo venga otro titulo, o se usa esta o se usa convert_empty_titles_to_normal_text
def eliminar_titulos_sin_content(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'(^#+\s+.*)', markdown_text, flags=re.MULTILINE)

    filtered_blocks = []
    current_title = None
    current_content = []

    # Recorrer los bloques y procesar los títulos con su contenido
    for block in blocks:
        if block.startswith('#'):  # Es un título
            if current_title is not None and current_content:  # Agregar el bloque anterior procesado
                filtered_blocks.append(current_title)
                filtered_blocks.extend(current_content)

            current_title = block.strip()
            current_content = []
        elif block.strip():  # Es contenido de texto normal
            current_content.append(block.strip())

    # Agregar el último bloque procesado si tiene contenido
    if current_title is not None and current_content:
        filtered_blocks.append(current_title)
        filtered_blocks.extend(current_content)

    # Unir los bloques filtrados en un nuevo texto
    filtered_text = '\n'.join(filtered_blocks)

    return filtered_text



# Esta funcion en vez de eliminar el #titulo si no tiene contenido, lo pasa a texto normal, es decri sin # para no perder informacion que pueda se interesante
# o se usa esta o se usa eliminar_titulos_sin_content
def convert_empty_titles_to_normal_text(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'(^#+\s+.*)', markdown_text, flags=re.MULTILINE)

    filtered_blocks = []
    current_title = None
    current_content = []

    # Recorrer los bloques y procesar los títulos con su contenido
    for block in blocks:
        if block.startswith('#'):  # Es un título
            if current_title is not None:
                # Agregar el título anterior y su contenido si tiene contenido
                if current_content:
                    filtered_blocks.append(current_title)
                    filtered_blocks.extend(current_content)
                else:
                    # Si no hay contenido debajo del título, convertir el título en texto normal
                    filtered_blocks.append(current_title.strip("#").strip())  # Eliminar '#'

            # Actualizar el título actual
            current_title = block
            current_content = []
        elif block.strip():  # Es contenido de texto normal
            current_content.append(block.strip())

    # Agregar el último bloque procesado si tiene contenido
    if current_title is not None:
        if current_content:
            filtered_blocks.append(current_title)
            filtered_blocks.extend(current_content)
        else:
            # Si no hay contenido debajo del último título, convertirlo en texto normal
            filtered_blocks.append(current_title.strip("#").strip())  # Eliminar '#'

    # Unir los bloques filtrados en un nuevo texto
    filtered_text = '\n'.join(filtered_blocks)

    return filtered_text






# Para eliminar lo que se categorice como titulo cuando en realidad no es nada
def remove_hash_lines(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # Filtrar las líneas que contienen solo un carácter '#'
    filtered_lines = [line.strip() for line in lines if line.strip() != "#"]

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(filtered_lines))




def merge_duplicate_titles(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'(^#+\s+.*)', markdown_text, flags=re.MULTILINE)

    filtered_blocks = []
    current_title = None
    current_content = []

    # Recorrer los bloques y procesar los títulos con su contenido
    for block in blocks:
        if block.startswith('#'):  # Es un título
            if current_title is not None and current_content:  # Agregar el bloque anterior procesado
                filtered_blocks.append(current_title)
                filtered_blocks.extend(current_content)

            current_title = block.strip()
            current_content = []
        elif block.strip():  # Es contenido de texto normal
            current_content.append(block.strip())

    # Agregar el último bloque procesado si tiene contenido
    if current_title is not None and current_content:
        filtered_blocks.append(current_title)
        filtered_blocks.extend(current_content)

    # Unir los bloques filtrados en un nuevo texto
    filtered_text = '\n'.join(filtered_blocks)

    return filtered_text


# Funcion principal para la ejecución principal del código
def process_markdown_files(input_dir, output_dir):
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Procesar cada archivo Markdown en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)

            # Eliminar líneas vacías del archivo de entrada y guardar el resultado en un archivo temporal
            temp_output_file_path = os.path.join(output_dir, f"temp_{filename}")
            remove_empty_lines(input_file_path, temp_output_file_path)
            remove_hash_lines(temp_output_file_path, temp_output_file_path)

            # Leer el contenido del archivo Markdown filtrado
            with open(temp_output_file_path, "r", encoding="utf-8") as input_file:
                markdown_text = input_file.read()

            # Aplicar la función merge_duplicate_titles al contenido del archivo
            merged_markdown = merge_duplicate_titles(markdown_text)

            # Aplicar la limpieza de texto al Markdown combinado
            cleaned_markdown = clean_text(merged_markdown)

            # Escribir el Markdown modificado en el archivo de salida
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(cleaned_markdown)

            # Eliminar el archivo temporal
            os.remove(temp_output_file_path)



# Procesar todos los archivos Markdown en el directorio de entrada
process_markdown_files(input_directory, output_directory)