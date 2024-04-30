import re
import os


def merge_duplicate_titles(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'^#+\s+', markdown_text, flags=re.MULTILINE)[1:]

    # Inicializar diccionario para mantener el contenido de cada título único
    title_content_map = {}

    # Recorrer los bloques
    for block in blocks:
        # Extraer el título y el contenido del bloque
        lines = block.split('\n', 1)
        title = lines[0].strip()
        content = lines[1].strip() if len(lines) > 1 else ''

        # Agregar el contenido al título correspondiente en el diccionario
        if title in title_content_map:
            title_content_map[title] += '\n\n' + content  # Concatenar contenido con espacio
        else:
            title_content_map[title] = content


    

    # Construir el texto final combinando los títulos únicos y su contenido
    merged_text = '\n\n'.join(f'# {title}\n{content}' for title, content in title_content_map.items())

    return merged_text

def process_markdown_files(input_dir, output_dir):
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Procesar cada archivo Markdown en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)

            # Leer el contenido del archivo Markdown
            with open(input_file_path, "r", encoding="utf-8") as input_file:
                markdown_text = input_file.read()

            # Aplicar la función merge_duplicate_titles al contenido del archivo
            merged_markdown = merge_duplicate_titles(markdown_text)
            # Escribir el Markdown modificado en el archivo de salida
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(merged_markdown)


# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean2"

# Procesar todos los archivos Markdown en el directorio de entrada
process_markdown_files(input_directory, output_directory)
