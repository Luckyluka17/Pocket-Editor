import os

piplist = ["pyautogui"]

print("Installation de Python...")
os.system('curl https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe --output "%TMP%\python-3.9.10.exe" && "%TMP%\python-3.9.10.exe" /silent')
os.system("cls")

print("Téléchargements des modules nécessaires...")
for pip in piplist:
    os.system(f"pip install {pip}")

print("Terminé !")
os.system("pause")
exit()