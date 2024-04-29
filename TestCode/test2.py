import re
import os

def remove_empty_lines(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # Filtrar las líneas vacías eliminando espacios en blanco al principio y al final
    filtered_lines = [line.strip() for line in lines if line.strip()]

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(filtered_lines))

        
def clean_text(markdown_text):
    # Filtrar solo caracteres permitidos: letras, números, puntos, comas, letras con tildes, y otros caracteres específicos
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,áéíóúÁÉÍÓÚñÑ!?¿<>#-]', '', markdown_text)
    cleaned_text = eliminar_titulos_sin_content(cleaned_text)
    cleaned_text = eliminar_numeros_suelto(cleaned_text)  # Eliminar números sueltos después de comentarios de página

    return cleaned_text


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


def eliminar_numeros_suelto(markdown_text):
    # Buscar y reemplazar números sueltos después de comentarios de página
    updated_text = re.sub(r'<!-- Página: (\d+) -->\s*(\d+)', r'<!-- Página: \1 -->', markdown_text)

    return updated_text


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


# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean"

# Procesar todos los archivos Markdown en el directorio de entrada
process_markdown_files(input_directory, output_directory)
