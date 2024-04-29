import re
def eliminar_titulos_sin_content(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'(^#+\s+.*)', markdown_text, flags=re.MULTILINE)

    filtered_blocks = []
    current_title = None
    current_content = []

    # Recorrer los bloques y procesar los títulos con su contenido
    for block in blocks:
        if block.startswith('#'):  # Es un título
            if current_title is not None and current_content:  # Agregar el bloque anterior procesado
                filtered_blocks.append(current_title)
                filtered_blocks.extend(current_content)

            current_title = block.strip()
            current_content = []
        elif block.strip():  # Es contenido de texto normal
            current_content.append(block.strip())

    # Agregar el último bloque procesado si tiene contenido
    if current_title is not None and current_content:
        filtered_blocks.append(current_title)
        filtered_blocks.extend(current_content)

    # Unir los bloques filtrados en un nuevo texto
    filtered_text = '\n'.join(filtered_blocks)

    return filtered_text

# Ejemplo de uso
markdown_text = """
# Promociones Diferidas


# Promociones Directas


# Promociones Directas de Financiación
Búsqueda de una promoción de Financiación

Consulta de las Condiciones de una Promoción

Consulta de mercancía participante de una Promoción de

Financiación
"""

filtered_markdown = eliminar_titulos_sin_content(markdown_text)
#print(filtered_markdown)





def convert_empty_titles_to_normal_text(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'(^#+\s+.*)', markdown_text, flags=re.MULTILINE)

    filtered_blocks = []
    current_title = None
    current_content = []

    # Recorrer los bloques y procesar los títulos con su contenido
    for block in blocks:
        if block.startswith('#'):  # Es un título
            if current_title is not None:
                # Agregar el título anterior y su contenido si tiene contenido
                if current_content:
                    filtered_blocks.append(current_title)
                    filtered_blocks.extend(current_content)
                else:
                    # Si no hay contenido debajo del título, convertir el título en texto normal
                    filtered_blocks.append(current_title.strip("#").strip())  # Eliminar '#'

            # Actualizar el título actual
            current_title = block
            current_content = []
        elif block.strip():  # Es contenido de texto normal
            current_content.append(block.strip())

    # Agregar el último bloque procesado si tiene contenido
    if current_title is not None:
        if current_content:
            filtered_blocks.append(current_title)
            filtered_blocks.extend(current_content)
        else:
            # Si no hay contenido debajo del último título, convertirlo en texto normal
            filtered_blocks.append(current_title.strip("#").strip())  # Eliminar '#'

    # Unir los bloques filtrados en un nuevo texto
    filtered_text = '\n'.join(filtered_blocks)

    return filtered_text

# Ejemplo de uso:
markdown_text = """
# titulo 1

# titulo 2
contenido de texto
"""

modified_text = convert_empty_titles_to_normal_text(markdown_text)
print(modified_text)