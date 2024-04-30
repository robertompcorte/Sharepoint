import subprocess
import time

def ejecutar_scripts_con_retraso(scripts, delay=5):
    for script in scripts:
        print(f"Ejecutando script: {script}")
        try:
            subprocess.run(["python", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar {script}: {e}")
        print(f"Finalizado: {script}\n")
        time.sleep(delay)  # Espera 5 segundos antes de ejecutar el siguiente script

# Lista de scripts a ejecutar
scripts_a_ejecutar = ["deleteimages.py", "markcomonpag.py", "cleancode.py","eliminartitulosduplicados.py","deletesinglenumbers.py",]

# Llama a la función para ejecutar los scripts con un retraso de 5 segundos entre cada uno
ejecutar_scripts_con_retraso(scripts_a_ejecutar)
