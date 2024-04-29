import os
import fitz  # PyMuPDF

def pdf_to_markdown(input_dir, output_dir):
    # Obtener la lista de archivos PDF en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(input_dir, filename)
            markdown_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".md")
            
            # Abrir el archivo PDF
            with fitz.open(pdf_file) as pdf:
                markdown_text = ""
                
                # Crear un diccionario para almacenar la frecuencia de cada línea de texto
                text_frequency = {}
                
                # Iterar sobre las páginas del PDF
                for page_number, page in enumerate(pdf, start=1):
                    # Obtener texto de la página
                    text = page.get_text()
                    
                    # Actualizar la frecuencia de cada línea de texto
                    lines = text.split("\n")
                    for line in lines:
                        line = line.strip()
                        if line:  # Ignorar líneas vacías
                            text_frequency[line] = text_frequency.get(line, 0) + 1
                
                # Obtener el texto más común en el PDF
                most_common_text = max(text_frequency, key=text_frequency.get)
                
                # Obtener el tamaño de fuente más común
                most_common_font_size = 0
                for page_number, page in enumerate(pdf, start=1):
                    text_instances = page.search_for(most_common_text)
                    if text_instances:
                        most_common_font_size = max(text_instances, key=lambda instance: instance[-1] - instance[-3])[-1] - text_instances[0][-3]
                        break
                
                # Iterar sobre las páginas del PDF nuevamente para generar el Markdown
                for page_number, page in enumerate(pdf, start=1):
                    # Obtener texto de la página
                    text = page.get_text()
                    
                    # Agregar metadatos como comentarios al inicio de la sección
                    markdown_text += f"<!-- Página: {page_number} -->\n"
                    
                    # Identificar títulos en el texto (basado en el tamaño de fuente)
                    lines = text.split("\n")
                    for line in lines:
                        search_results = page.search_for(line)
                        if search_results:  # Verificar si se encontraron resultados
                            font_size = search_results[0][-1] - search_results[0][-3]
                            # Comparar el tamaño de fuente con el tamaño del texto más común
                            if font_size > most_common_font_size:
                                markdown_text += "# " + line.strip() + "\n\n"  # Formatear como título en Markdown
                            else:
                                markdown_text += line.strip() + "\n\n"  # Agregar el texto tal cual
                    
            # Escribir el texto formateado en un archivo Markdown
            with open(markdown_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)

# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown"

# Convertir todos los archivos PDF en el directorio de entrada a Markdown en el directorio de salida
pdf_to_markdown(input_directory, output_directory)
