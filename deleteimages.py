import os
import pprint

import PyPDF2
import fitz

# Directorios

# Directorio para coger pdf
source_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\documentos"
#Directorio para pegar nuevo pdf
noimages_dir = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\newdocumentos"

def remove_images(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_images()
        for img in img_list:
            page.delete_image(img[0])

    doc.save(output_pdf)



for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        print("Procesando archivo:", filename)
        source_file_path = os.path.join(dirpath, filename)
        dest_file_path = os.path.join(noimages_dir, os.path.relpath(dirpath, source_dir), filename)

        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
        _, ext = os.path.splitext(source_file_path)
        if not os.path.exists(dest_file_path):
            if ext.lower() in ['.pdf']:
                if not "150RGB" in source_file_path:
                    print("Removing images from {}".format(filename))
                    try:
                        remove_images(source_file_path,dest_file_path)
                    except Exception as ex:
                        print("Exception occurred: {}".format(ex))
            else:
                #copy the file
                with open(source_file_path, "rb") as source_file:
                    with open(dest_file_path, "wb") as dest_file:
                        dest_file.write(source_file.read())

                