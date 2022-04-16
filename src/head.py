import pyperclip

"""
Menu du haut
"""

baop = ["print()"]

menubar = Menu(window)
fileBar = Menu(menubar, tearoff=0)
fileBar.add_command(label="Nouveau", command=nouv)
fileBar.add_command(label="Ouvrir", command=ouvrir)
fileBar.add_command(label="Enregistrer", command=save)
fileBar.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Fichier", menu=fileBar)
editMenu = Menu(menubar, tearoff=0)
editMenu.add_command(label="Copier", command=lambda: pyautogui.hotkey('ctrl', 'c'))
editMenu.add_command(label="Couper", command=lambda: pyautogui.hotkey('ctrl', 'x'))
editMenu.add_command(label="Coller", command=lambda: pyautogui.hotkey('ctrl', 'v'))
editMenu.add_command(label="Sélectionner tout", command=lambda: pyautogui.hotkey('ctrl', 'a'))
editMenu.add_command(label="--------", state="disabled")
editMenu.add_command(label="Annuler", command=lambda: pyautogui.hotkey('ctrl', 'z'))
editMenu.add_command(label="Rétablir", command=lambda: pyautogui.hotkey('ctrl', 'y'))
menubar.add_cascade(label="Edition", menu=editMenu)
affBar  = Menu(menubar, tearoff=0)
affBar.add_command(label="Couleur du texte :", state="disabled")
affBar.add_command(label="Blanc", command=lambda: code.config(foreground="white"))
affBar.add_command(label="Noir", command=lambda: code.config(foreground="black"))
affBar.add_command(label="Rouge", command=lambda: code.config(foreground="red"))
affBar.add_command(label="Vert", command=lambda: code.config(foreground="green"))
affBar.add_command(label="Couleur du fond :", state="disabled")
affBar.add_command(label="Blanc", command=lambda: code.config(background="white"))
affBar.add_command(label="Noir", command=lambda: code.config(background="black"))
affBar.add_command(label="Rouge", command=lambda: code.config(background="red"))
affBar.add_command(label="Vert", command=lambda: code.config(background="green"))
affBar.add_command(label="--------", state="disabled")
affBar.add_command(label="Rénitialiser", command=lambda: code.config(foreground="white", background="#374140"))
menubar.add_cascade(label="Affichage", menu=affBar)
pytoolsBar = Menu(menubar, tearoff=0)
pytoolsBar.add_command(label="print()", command=lambda: (
    pyautogui.press("enter"),
    pyperclip.copy("print()"),
    pyautogui.hotkey('ctrl', 'v'),
    pyautogui.press("enter")
    ))
pytoolsBar.add_command(label="input()", command=lambda: (
    pyautogui.press("enter"),
    pyperclip.copy("input()"),
    pyautogui.hotkey('ctrl', 'v'),
    pyautogui.press("enter")
))
pytoolsBar.add_command(label="def()", command=lambda: (
    pyautogui.press("enter"),
    pyperclip.copy("def maFonction(arg):"),
    pyautogui.hotkey('ctrl', 'v'),
    pyautogui.press("enter"),
    pyautogui.press("tab"),
    pyautogui.write("// Entrez votre code ici"),
    pyautogui.press("enter")
))
pytoolsBar.add_command(label="for", command=lambda: (
    pyautogui.press("enter"),
    pyperclip.copy("for i in range(1, 3):"),
    pyautogui.hotkey('ctrl', 'v'),
    pyautogui.press("enter"),
    pyautogui.press("tab"),
    pyautogui.write("// Entrez votre code ici"),
    pyautogui.press("enter")
))
pytoolsBar.add_command(label="while", command=lambda: (
    pyautogui.press("enter"),
    pyperclip.copy("while i < 3:"),
    pyautogui.hotkey('ctrl', 'v'),
    pyautogui.press("enter"),
    pyautogui.press("tab"),
    pyautogui.write("// Entrez votre code ici"),
    pyautogui.press("enter"),
))
menubar.add_cascade(label="Boite à outils Python", menu=pytoolsBar)
runBar = Menu(menubar, tearoff=0)
runBar.add_command(label="Executer le script", command=executer)
runBar.add_command(label="Executer dans un terminal", command=lambda: os.startfile("cmd.exe"))
menubar.add_cascade(label="Executer", menu=runBar)
helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Prise en main", command=lambda: web.open("https://github.com/Luckyluka17/Pocket-Editor/wiki/Prise-en-main"))
helpMenu.add_command(label="--------", state="disabled")
helpMenu.add_command(label="Discord", command=lambda: web.open("https://discord.gg/qFfYvKHR5B"))
helpMenu.add_command(label="YouTube", command=lambda: web.open("https://www.youtube.com/channel/UC-rPcYTZqLCOEkloQFXwgnQ"))
helpMenu.add_command(label="GitHub", command=lambda: web.open("https://github.com/luckyluka17"))
helpMenu.add_command(label="--------", state="disabled")
helpMenu.add_command(label="A propos", command=lambda: messagebox.showinfo("Pocket Editor", "Pocket Editor est un logiciel de développement de scripts Python.\n\nIl a été développé par Luckyluka17."))
menubar.add_cascade(label="Aide", menu=helpMenu)