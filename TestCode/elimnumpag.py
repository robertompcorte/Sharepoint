import re

def actualizar_numeros_sueltos(markdown_text):
    # Usar expresión regular para capturar el comentario de página y el número suelto
    updated_text = re.sub(r'(<!-- Página: \d+ -->)\n(\d+)', r'\1\n', markdown_text)
    return updated_text

# Ejemplo de uso:
markdown_text = '''
<!-- Página: 4 -->
4


hoalasd fasd asdfjalsj 

asdfasdf

<!-- Página: 7 -->
7

Búsqueda Promociones
<!-- Página 5 -->
5
Este listado, junto con el nombre de la
promoción, incluye unos iconos que
permiten obtener distinta información
de la promoción a la que están
asociados.

<!-- Página 6 -->
6
Muestra las
'''

# Aplicar la función para actualizar los números sueltos
resultado = actualizar_numeros_sueltos(markdown_text)
print(resultado)
