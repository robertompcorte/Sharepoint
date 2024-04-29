import pdfplumber

def pdf_to_markdown(input_path, output_path):
    with pdfplumber.open(input_path) as pdf:
        markdown_lines = []
        current_title = None

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    if line.strip():  # Saltar líneas vacías
                        if line.startswith("#"):
                            # Encontrar un nuevo título
                            if current_title is not None:
                                # Agregar el contenido previo con el título anterior
                                markdown_lines.append(f"## {current_title}\n")
                                markdown_lines.append("\n".join(current_content))
                                markdown_lines.append("")  # Línea en blanco entre secciones
                            
                            current_title = line.strip("# ").strip()
                            current_content = []
                        else:
                            # Agregar línea al contenido actual
                            current_content.append(line.strip())

        # Agregar el último título y su contenido al archivo Markdown
        if current_title is not None:
            markdown_lines.append(f"## {current_title}\n")
            markdown_lines.append("\n".join(current_content))

    with open(output_path, "w", encoding="utf-8") as markdown_file:
        markdown_file.write("\n".join(markdown_lines))


# Directorios de entrada y salida
input_pdf_path = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\documentos\\Presentacion Monitor Promocional.pdf"
output_md_path = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown\\cleanone.md"

# Convertir PDF a Markdown
pdf_to_markdown(input_pdf_path, output_md_path)
