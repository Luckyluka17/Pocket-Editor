import os
import time
import codecs
import webbrowser as web
from tkinter import *
from tkinter import filedialog, messagebox
import pyautogui
from pypresence import Presence

try:
    RPC = Presence("964835207997952020")
    RPC.connect()
    RPC.update(
        state="Utilise Pocket Editor",
        details="Édite un fichier en Python",
        large_image="logo",
        small_image="py",
        large_text="Version 1.0.1",
        small_text="Python",
        start=time.time(),
        buttons=[{"label": "Télécharger", "url": "https://github.com/Luckyluka17/Pocket-Editor/releases"}, {"label": "Discord", "url": "https://discord.gg/qFfYvKHR5B"}]
    )
except:
    pass

file = None
nameoffile = []

# Commandes
def nouv():
    os.system("echo //Pocket Editor >script.py")
    messagebox.showinfo("Pocket Editor", "Nouveau fichier créé ! Pour y accèder, ouvrez le dans l'éditeur.")

def ouvrir():
    file = filedialog.askopenfile(parent=window, mode='rb', title='Sélectionnez un fichier', defaultextension=".py", filetypes=[("Python", "*.py")])
    if file != None:
        code.delete(1.0, END)
        code.insert(1.0, file.read())
        test = file
        file.close()
        window.title(f"Pocket Editor - {file.name}")
    else:
        messagebox.showwarning("Pocket Editor", "Aucun fichier sélectionné !")

def save():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Python", "*.py")])
    if file != None:
        file.write(code.get(1.0, END))
        file.close()
        messagebox.showinfo("Pocket Editor", "Fichier enregistré !")
    else:
        messagebox.showwarning("Pocket Editor", "Aucun fichier sélectionné !")

def executer():
    from execute import nom
    exec(codecs.open("execute.py", "r", "utf-8").read())

window = Tk()

window.title("Pocket Editor")
window.iconbitmap("logo.ico")
window.geometry("600x400")
exec(codecs.open('head.py', 'r', 'utf-8').read())

code = Text(
    bg="#374140",
    font=("Calibri", 12),
    fg="white"
)
code.pack(expand=1, fill="both")
code.focus_set()

window.config(menu=menubar, bg="#374140")
code.insert(1.0, "// Pocket Editor\n")
window.mainloop()
