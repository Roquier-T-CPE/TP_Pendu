import os
os.chdir("D:\\Users\\thomas\\Desktop\\CS-DEV\\ProjetPendu")
from random import randint
from Fonctions import affichage, estDans, genMot


restart = "oui"


while restart == "oui":

    mot = genMot()

    listeLettres = ""

    nbCoups = 0
    nbLettres = affichage(mot,listeLettres)

    while nbLettres != len(mot) and nbCoups < 8:

        lettre = entreeLettre(listeLettres)



        nbCoups += 1
        if nbCoups!=1:
            listeLettres +=  ", " + lettre
        else:
                listeLettres += lettre


        nbLettres = affichage(mot,listeLettres)
        print("\nIl vous reste",8-nbCoups,"Chances")


    if nbLettres == len(mot):
        print("\nBravo !\nVous avez trouve en",nbCoups,"Coups")
    else:
        print("Dommage, vous n'avez pas trouve, le mot etait :",mot)


    restart = input("Voulez-vous rejouez ?\nEntrez oui si vous voulez refaire une partie\n")

