import os
import fitz

# Directorio del archivo PDF
pdf_path = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\new2documentos\\DocumentoImagenes.pdf"

def read_pdf_text(pdf_path):
    text_array = []  # Array para almacenar el texto

    # Abrir el archivo PDF
    with fitz.open(pdf_path) as doc:
        # Iterar sobre cada página del PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            text_array.append(text)  # Agregar el texto de la página al array

    return text_array

def print_pdf_text(text_array):
    # Imprimir el texto de cada página por pantalla
    for page_num, text in enumerate(text_array, start=1):
        print(f"Texto de la página {page_num}:")
        print(text)
        print("\n")  # Imprimir una línea en blanco entre páginas

# Leer el texto del PDF y almacenarlo en un array
pdf_text_array = read_pdf_text(pdf_path)

# Imprimir el texto por pantalla
print_pdf_text(pdf_text_array)
