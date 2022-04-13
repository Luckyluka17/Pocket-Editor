import os
import time
import codecs
import webbrowser as web
from tkinter import *
from tkinter import filedialog, messagebox

try:
    import pyautogui
except:
    messagebox.showerror('Pocket Editor', "Une erreur est survenue, un module est manquant !\n\nPour l'installer, exécutez le script 'install.py'.")
    exit()

file = None
nameoffile = []

# Commandes
def nouv():
    os.system("echo //Pocket Editor >script.ks")
    messagebox.showinfo("Kshell IDE", "Nouveau fichier créé ! Pour y accèder, ouvrez le dans l'éditeur.")

def ouvrir():
    file = filedialog.askopenfile(parent=window, mode='rb', title='Sélectionnez un fichier')
    if file != None:
        code.delete(1.0, END)
        code.insert(1.0, file.read())
        file.close()
        window.title(f"Pocket Editor - {file.name}")
    else:
        messagebox.showwarning("Pocket Editor", "Aucun fichier sélectionné !")

def save():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Fichier texte", "*.txt"), ("Javascript", "*.js"), ("Python", "*.py"), ("Kshell", "*.ks")])
    if file != None:
        file.write(code.get(1.0, END))
        file.close()
        messagebox.showinfo("Pocket Editor", "Fichier enregistré !")
    else:
        messagebox.showwarning("Pocket Editor", "Aucun fichier sélectionné !")

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
