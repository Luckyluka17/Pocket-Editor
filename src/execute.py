from tkinter import ttk
import tkinter as tk
import os
from tkinter import messagebox

window1 = tk.Tk()
window1.title("Pocket Editor")
window1.iconbitmap("logo.ico")
window1.geometry("300x100")
window1.resizable(False, False)


ttk.Label(
    window1,
    text="Nom du fichier :",
    font=(None, 13),
).pack()

nom = ttk.Entry(
    window1,
    width=30,
)
nom.pack()

def executefile():
    if ".py" in nom.get():
        if os.path.isfile(nom.get()):
            os.system(f"python {nom.get()}")
        else:
            messagebox.showwarning("Pocket Editor", "Fichier introuvable !")
    else:
        if os.path.isfile(f"{nom.get()}.py"):
            os.system(f"python {nom.get()}.py")
        else:
            messagebox.showwarning("Pocket Editor", "Fichier introuvable !")

ttk.Label(
    window1,
    text=" ",
    font=(None, 13),
).pack()


bouton1 = ttk.Button(
    window1,
    text="Exécuter le script",
    command=executefile,
)
bouton1.pack()

window1.mainloop()