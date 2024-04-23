import spacy
import json


# Cargar el modelo de idioma de spaCy (por ejemplo, 'es' para español)
nlp = spacy.load('es_core_news_sm')

# Función para generar embeddings de un texto utilizando spaCy
def generate_embeddings(text):
    doc = nlp(text)
    # Obtiene el vector promedio de los tokens
    return doc.vector.tolist()

# Ruta al archivo JSON con los chunks de texto
json_file_path = "ruta/al/archivo.json"

# Ruta al archivo de salida donde se guardarán los embeddings
output_file_path = "ruta/al/archivo_de_embeddings.json"

# Procesamiento del archivo JSON
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Lista para almacenar los embeddings de cada chunk
embeddings_data = []

# Generar embeddings para cada chunk de texto y agregarlos a la lista
for chunk in data:
    text = chunk['texto']  # Suponiendo que el texto está bajo la clave 'texto'
    embeddings = generate_embeddings(text)
    chunk['embeddings'] = embeddings
    embeddings_data.append(chunk)

# Guardar los datos con los embeddings en un nuevo archivo JSON
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(embeddings_data, output_file, ensure_ascii=False, indent=4)

print("Embeddings generados y guardados en", output_file_path)
