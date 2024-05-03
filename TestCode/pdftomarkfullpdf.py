import os
import fitz  # PyMuPDF

def get_most_common_font_size(pdf_file):
    font_size_frequency = {}
    
    # Abrir el archivo PDF
    with fitz.open(pdf_file) as pdf:
        # Iterar sobre las páginas del PDF
        for page in pdf:
            # Obtener texto de la página
            text_instances = page.search_for("*")  # Buscar todas las instancias de texto en la página
            for instance in text_instances:
                font_size = instance[-1] - instance[-3]
                font_size_frequency[font_size] = font_size_frequency.get(font_size, 0) + 1
    
    # Obtener el tamaño de fuente más común en todo el PDF
    most_common_font_size = max(font_size_frequency, key=font_size_frequency.get)
    return most_common_font_size

def pdf_to_markdown(input_dir, output_dir):
    # Obtener la lista de archivos PDF en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(input_dir, filename)
            markdown_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".md")
            
            # Obtener el tamaño de fuente predominante en todo el documento
            most_common_font_size = get_most_common_font_size(pdf_file)
            print(f"Tamaño de letra predominante en el documento: {most_common_font_size:.2f}px")
            
            # Abrir el archivo PDF nuevamente para convertir a Markdown
            with fitz.open(pdf_file) as pdf:
                markdown_text = ""
                # Iterar sobre las páginas del PDF
                for page_number, page in enumerate(pdf, start=1):
                    # Obtener texto de la página
                    text = page.get_text()
                    
                    # Agregar metadatos como comentarios al inicio de la sección
                    markdown_text += f"<!-- Página: {page_number} -->\n"
                    
                    # Identificar títulos en el texto (basado en el tamaño de fuente predominante)
                    lines = text.split("\n")
                    for line in lines:
                        search_results = page.search_for(line)
                        if search_results:  # Verificar si se encontraron resultados
                            font_size = search_results[0][-1] - search_results[0][-3]
                            if font_size > most_common_font_size and line.strip():  # Considerar títulos si el tamaño de fuente es mayor que el predominante
                                markdown_text += "# " + line.strip() + "\n\n"  # Formatear como título en Markdown
                            else:
                                markdown_text += line.strip() + "\n\n"  # Agregar el texto tal cual
                    
            # Escribir el texto formateado en un archivo Markdown
            with open(markdown_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)

# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdownfull"

# Convertir todos los archivos PDF en el directorio de entrada a Markdown en el directorio de salida
pdf_to_markdown(input_directory, output_directory)
