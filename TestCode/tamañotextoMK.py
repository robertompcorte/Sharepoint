import os
import fitz  # PyMuPDF

def pdf_to_markdown(input_dir, output_dir):
    # Obtener la lista de archivos PDF en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(input_dir, filename)
            markdown_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".md")
            
            # Variables para almacenar el texto y la frecuencia de texto más común
            markdown_text = ""
            text_frequency = {}
            
            # Abrir el archivo PDF
            with fitz.open(pdf_file) as pdf:
                # Iterar sobre las páginas del PDF
                for page in pdf:
                    # Obtener texto de la página
                    text = page.get_text()
                    
                    # Iterar sobre cada línea de texto en la página
                    for line in text.splitlines():
                        line = line.strip()
                        if line:  # Ignorar líneas vacías
                            # Obtener tamaño de fuente de la línea
                            font_size = 0
                            text_instances = page.search_for(line)
                            if text_instances:
                                font_size = text_instances[0][-1] - text_instances[0][-3]
                            
                            # Actualizar la frecuencia de cada tamaño de fuente
                            if font_size > 0:
                                if font_size in text_frequency:
                                    text_frequency[font_size] += 1
                                else:
                                    text_frequency[font_size] = 1
                
                # Generar el Markdown con metadatos y tamaño de fuente
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
                            # Comparar el tamaño de fuente con el tamaño más común
                            if font_size > 0:
                                markdown_text += f"{line.strip()}  <!-- Tamaño de fuente: {font_size:.2f}px -->\n\n"
                        else:
                            markdown_text += line.strip() + "\n\n"  # Agregar el texto tal cual
            
            # Escribir el texto formateado en un archivo Markdown
            with open(markdown_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)
                
            # Imprimir la frecuencia de tamaño de fuente por página
            print(f"Frecuencia de tamaño de fuente para '{filename}':")
            for size, count in text_frequency.items():
                print(f"{size:.2f}px - {count} veces")

# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdowntexto"

# Convertir todos los archivos PDF en el directorio de entrada a Markdown en el directorio de salida
pdf_to_markdown(input_directory, output_directory)
