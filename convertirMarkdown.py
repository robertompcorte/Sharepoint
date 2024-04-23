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
                # Extraer texto de cada página
                for page in pdf:
                    text = page.get_text()
                    # Identificar títulos en el texto (basado en el tamaño de fuente)
                    lines = text.split("\n")
                    for line in lines:
                        search_results = page.search_for(line)
                        if search_results:  # Verificar si se encontraron resultados
                            font_size = search_results[0][-1] - search_results[0][-3]
                            if font_size > 12 and line.strip():  # Ejemplo: considerar títulos si el tamaño de fuente es mayor que 12
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
