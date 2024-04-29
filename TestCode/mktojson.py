import spacy
import json
import os

# Cargar el modelo de idioma de spaCy (por ejemplo, 'es' para español)
nlp = spacy.load('es_core_news_sm')

# Función para generar embeddings de un texto utilizando spaCy
def generate_embeddings(text):
    doc = nlp(text)
    # Obtiene el vector promedio de los tokens
    return doc.vector.tolist()

# Directorios de entrada y salida
input_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown"
output_directory = "C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\json_with_embeddings"

# Crear el directorio de salida si no existe
os.makedirs(output_directory, exist_ok=True)

# Procesar cada archivo JSON en el directorio de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(".json"):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)
        
        # Procesamiento del archivo JSON
        with open(input_file_path, "r", encoding="utf-8") as file:
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
