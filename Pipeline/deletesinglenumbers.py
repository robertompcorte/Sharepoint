import re
import os


def actualizar_numeros_sueltos(markdown_text):
    # Usar expresión regular para eliminar números sueltos debajo de comentarios de página
    updated_text = re.sub(r'(<!-- Página \d+ -->)\n(\d+)', r'\1\n', markdown_text)
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

            # Leer el contenido del archivo Markdown
            with open(input_file_path, "r", encoding="utf-8") as input_file:
                markdown_text = input_file.read()

            # Aplicar la función actualizar_numeros_sueltos al contenido del archivo
            updated_markdown = actualizar_numeros_sueltos(markdown_text)

            # Escribir el Markdown modificado en el archivo de salida
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(updated_markdown)


# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean2"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownclean3"

# Procesar todos los archivos Markdown en el directorio de entrada
process_markdown_files(input_directory, output_directory)
