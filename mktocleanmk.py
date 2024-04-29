import re
import os


# def clean_text(text):
#     # Define los caracteres especiales que deseas eliminar
#     special_characters = ['\uf0d8', '\uf0e0','\uf0fc','\u25D8']  # Agrega más caracteres según sea necesario

#     # Reemplaza los caracteres especiales con una cadena vacía
#     for char in special_characters:
#         text = text.replace(char, '')

#     return text

def clean_text(text):
    # Filtrar solo caracteres permitidos: letras, números, puntos, comas y letras con tildes
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,áéíóúÁÉÍÓÚñÑ!?¿<>-]', '', text)
    return cleaned_text


def merge_duplicate_titles(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'^#+\s+', markdown_text, flags=re.MULTILINE)[1:]

    # Inicializar lista para almacenar los bloques procesados
    processed_blocks = []

    # Recorrer los bloques
    for block in blocks:
        # Extraer el título y el contenido del bloque
        lines = block.split('\n', 1)
        title = lines[0].strip()
        content = lines[1].strip() if len(lines) > 1 else ''

        # Verificar si el contenido contiene un número sin comentario
        match = re.search(r'<!-- Página: (\d+) -->\s*(\d+)', content)
        if match:
            # Si se encuentra un número sin comentario, reemplazarlo con el comentario
            page_number = match.group(1)
            updated_content = re.sub(r'<!-- Página: \d+ -->\s*\d+', f'<!-- Página: {page_number} -->', content)
        else:
            # Si no se encuentra un número sin comentario, mantener el contenido original sin cambios
            updated_content = content

        # Limpiar el contenido del bloque manteniendo solo caracteres alfanuméricos y espacios
        cleaned_content = clean_text(updated_content)

        # Reconstruir el bloque con el título y el contenido limpio
        updated_block = f'# {title}\n{cleaned_content}'
        processed_blocks.append(updated_block)

    # Construir el texto final combinando los bloques procesados
    merged_text = '\n\n'.join(processed_blocks)

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
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean"

# Procesar todos los archivos Markdown en el directorio de entrada
process_markdown_files(input_directory, output_directory)
