import os
import fitz

# Directorios
source_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\documentos"
noimages_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"

def remove_images(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_images()
        for img in img_list:
            page.delete_image(img[0])
    doc.save(output_pdf)

# Iterar sobre todos los archivos en source_dir y sus subdirectorios
for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        source_file_path = os.path.join(dirpath, filename)
        dest_file_path = os.path.join(noimages_dir, os.path.relpath(dirpath, source_dir), filename)

        # Asegurar que el directorio de destino exista
        os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
        _, ext = os.path.splitext(source_file_path)
        if ext.lower() == '.pdf':  # Solo procesar archivos PDF
            if "150RGB" not in source_file_path:  # Ignorar archivos que contienen '150RGB' en el nombre
                print("Removing images from", filename)
                try:
                    remove_images(source_file_path, dest_file_path)
                except Exception as ex:
                    print("Exception occurred:", ex)
        else:
            # Copiar el archivo sin modificar si no es un PDF
            with open(source_file_path, "rb") as source_file:
                with open(dest_file_path, "wb") as dest_file:
                    dest_file.write(source_file.read())

                