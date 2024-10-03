#Angel Saldaña Aguilar
#Itzel Noemi Rodriguez Torres
import pyautogui
import subprocess
import datetime

fecha = datetime.datetime.now()
x = fecha.strftime("%Y%m%d_%H%M%S")#YYYYMMDD_HHMMSS
# Captura de pantalla
try:
    screenshot = pyautogui.screenshot()
    screenshot.save("Captura_" + x + ".png")
    print(f"Captura de pantalla guardada como Captura_{x}.png")
except Exception as e:
    print("Error al capturar la pantalla:", e)
try:
    proceso = subprocess.run(["tasklist"], capture_output=True, shell=True, text=True)
    with open('lista_' + x + '.txt', 'w') as listas:
        listas.write(proceso.stdout)
    print(f"Lista de procesos guardada como lista_{x}.txt")
except Exception as e:
    print("Error al ejecutar el comando:", e)
finally:
    print("Operación completada.")