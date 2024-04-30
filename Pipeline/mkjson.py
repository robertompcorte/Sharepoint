import os
import json

def extract_chunks_from_markdown(input_file):
    chunks = []
    current_title = None
    current_content = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            # Si encontramos un nuevo encabezado, guardamos el chunk actual (si existe)
            if current_title and current_content:
                chunks.append({
                    'title': current_title,
                    'content': '\n'.join(current_content)
                })
                current_content = []

            # Obtenemos el nuevo título desde la línea (quitando el '#' y espacios adicionales)
            current_title = line.lstrip('#').strip()
        else:
            # Agregamos la línea al contenido del chunk actual
            current_content.append(line)

    # Agregamos el último chunk después de terminar de leer el archivo
    if current_title and current_content:
        chunks.append({
            'title': current_title,
            'content': '\n'.join(current_content)
        })

    return chunks

def save_chunks_to_json(chunks, output_dir, source_file):
    filename_base = os.path.splitext(os.path.basename(source_file))[0]
    for idx, chunk in enumerate(chunks):
        output_filename = f'{filename_base}_{idx + 1}.json'
        output_file = os.path.join(output_dir, output_filename)
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(chunk, json_file, ensure_ascii=False, indent=4)

def process_markdown_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_file = os.path.join(input_dir, filename)
            chunks = extract_chunks_from_markdown(input_file)
            save_chunks_to_json(chunks, output_dir, input_file)

# Directorios de entrada y salida
input_directory = 'C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean3'
output_directory = 'C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\jsonchunks'

# Procesar archivos Markdown y guardar los chunks en formato JSON
process_markdown_files(input_directory, output_directory)
