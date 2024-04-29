import re

def merge_duplicate_titles(markdown_text):
    # Dividir el texto en bloques de acuerdo a los títulos
    blocks = re.split(r'^#+\s+', markdown_text, flags=re.MULTILINE)[1:]

    # Inicializar diccionario para mantener el contenido de cada título único
    title_content_map = {}

    # Recorrer los bloques
    for block in blocks:
        # Extraer el título y el contenido del bloque
        lines = block.split('\n', 1)
        title = lines[0].strip()
        content = lines[1].strip() if len(lines) > 1 else ''

        # Agregar el contenido al título correspondiente en el diccionario
        if title in title_content_map:
            title_content_map[title] += '\n\n' + content  # Concatenar contenido con espacio
        else:
            title_content_map[title] = content

    # Construir el texto final combinando los títulos únicos y su contenido
    merged_text = '\n\n'.join(f'# {title}\n{content}' for title, content in title_content_map.items())

    return merged_text

# Ejemplo de uso
input_markdown = """
# Búsqueda de acciones promocionales
Una vez realizada la búsqueda, se mostrará la línea correspondiente a la promoción o campaa de financiación deseada.

# Búsqueda de acciones promocionales
Control de publicación de mercancía.

# Búsqueda de acciones promocionales
Exportar Excel

# HOLA PACO
Exportar Excel

# Búsqueda de acciones promocionales
Resumen PDF
"""

merged_markdown = merge_duplicate_titles(input_markdown)
print(merged_markdown)
