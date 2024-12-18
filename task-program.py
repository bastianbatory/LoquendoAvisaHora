import os
import re
import subprocess
import sys

python_path = sys.executable

dir = os.path.dirname(os.path.abspath(__file__))
audioDir = (dir + r'\audio')
#D:\AlarmasBot

print (audioDir)
archivos = [archivo for archivo in os.listdir(audioDir) if archivo.endswith('.wav')]

for archivo in archivos:
    date = archivo.replace(".wav", "")
    dateFormat = re.search(rf"(^..)(..)", date)
    dateDots = dateFormat.group(1) + ":" + dateFormat.group(2)
    comando = fr'schtasks /create /tn "Hora{date}" /tr "{python_path} {dir}\play.py {date}" /sc DAILY /st {dateDots} /f'
    print (comando)
    try:
        subprocess.run(comando, check=True)
        print(f"Tarea Aviso hora: {dateDots} agregada exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al agregar la tarea: {e}")