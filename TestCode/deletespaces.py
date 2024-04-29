import os
import fitz

# Directorios
source_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"
noimages_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\new2documentos"

def adjust_line_spacing(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text = page.get_text()
        lines = text.split("\n")
        adjusted_lines = [line.strip() for line in lines if line.strip()]
        adjusted_text = "\n\n".join(adjusted_lines)

        # Establecer los márgenes
        top_margin = 50  # Puedes ajustar este valor según sea necesario
        left_margin = 0.1 * page.rect.width  # Margen izquierdo
        right_margin = 0.9 * page.rect.width  # Margen derecho

        # Insertar el texto con los márgenes especificados
        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
        new_page.set_cropbox(page.rect)
        new_page.insert_text((left_margin, top_margin), adjusted_text)

    new_doc.save(output_pdf)

for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        print("Procesando archivo:", filename)
        source_file_path = os.path.join(dirpath, filename)
        dest_file_path = os.path.join(noimages_dir, os.path.relpath(dirpath, source_dir), filename)

        os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
        _, ext = os.path.splitext(source_file_path)
        if not os.path.exists(dest_file_path):
            if ext.lower() == '.pdf':
                if not "150RGB" in source_file_path:
                    print("Ajustando espacios en {}".format(filename))
                    try:
                        adjust_line_spacing(source_file_path, dest_file_path)
                    except Exception as ex:
                        print("Exception occurred: {}".format(ex))
            else:
                with open(source_file_path, "rb") as source_file:
                    with open(dest_file_path, "wb") as dest_file:
                        dest_file.write(source_file.read())
