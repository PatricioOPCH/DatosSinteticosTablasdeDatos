import subprocess

while True:
    try:
        subprocess.run(["python", "generarDatos.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"La ejecución del script generó un error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
