import chardet

def detect_encoding(data):
    result = chardet.detect(data)
    return result['encoding']

# Ejemplo de uso con un archivo
with open("C:\\Users\\roberto.martin\\Documents\\TestVSC\\DCH\\EliminarFotoPdf\\markdown", "rb") as file:
    data = file.read()
    encoding = detect_encoding(data)
    print(f"La codificación detectada es: {encoding}")
