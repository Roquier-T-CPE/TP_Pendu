"""
Jeu du pendu avec affichage graphique
Fait par Thomas Roquier
Le 07/12/2020


TODO:
-Fonctions Victoires et Defaites en fin de parties
-Affichage des lettre deja deja entrees
-Amelioration interface graphique
-Possibilite de refaire une partie
"""
import os
os.chdir("/home/thomas/TP_Pendu")

from tkinter import Tk, Label, Button, Entry, StringVar, Canvas, PhotoImage, NW

from Fonctions import affichage2, genMot, verif, dessinePendu2


mw = Tk()
mw.title("Pendu")
mw.geometry('800x600+240+70')

listeImages = []

for k in range(1,9):
    listeImages.append(PhotoImage(file = "Images/bonhomme" + str(k) + ".gif"))

def main():
    """
    Fonction principale du jeu du pendu, qui s'execute a chaque
        actualisation

    """

    if verif(lettreVar.get(),listeLettres):
        listeLettres.append(lettreVar.get())

        print(listeLettres)

        affMot.set(affichage2(mot,listeLettres))

        if not (lettreVar.get() in mot):
            vie.set( int(vie.get())-1)


        dessinePendu2(canevas, vie.get(), listeImages)

        if affMot.get() == mot:
            pass

        if vie == 0:
            pass

    lettreVar.set("")


mot = genMot()
listeLettres = []
vie = StringVar()
vie.set("8")
lettreVar = StringVar()
affMot = StringVar()





lettreEnt = Entry(mw, textvariable = lettreVar)
texteLettre = Label(mw, text = "Lettre :")
but = Button(mw, text = "Go !", fg = "blue", command = main)

canevas = Canvas(mw, width = "300", height = "300", bg = "white")
canevas.bind("<Return>",lambda x : main())
afficheVie = Label(mw, textvariable = vie)

afficheMot = Label(mw, textvariable = affMot)


canevas.pack(side = "top")
afficheVie.pack()
afficheMot.pack(side = "top")
texteLettre.pack(side = "left")
lettreEnt.pack(side = "left")
but.pack(side = "left")


affMot.set(affichage2(mot,listeLettres))
dessinePendu2(canevas, vie.get(), listeImages)








mw.mainloop()




