import os
os.chdir("D:\\Users\\thomas\\Desktop\\CS-DEV\\ProjetPendu")
from random import randint

def estDans(c,m):

    """
    Fonction qui verifie si une lettre est dans un mot donne
    Entrees :
        -c : la lettre a verifer
        -m : le mot dans lequel on cherche la lettre
    Sortie : Bool, true si la lettre est dans le mot, false sinon
    """

    flag = False
    n = len(m)
    k = 0

    while not(flag) and k < n:
        if m[k].lower() == c.lower():
            flag = True
        k += 1
    return flag




def affichage(m,l):
    """
    Affiche le mot m mais uniquement avec les lettres presentes dans la liste l
    Entree :
        -m le mot que l'on veut afficher
        -l la liste des lettres que l'on veut afficher
    Sortie : Renvoie le nombre de lettres affichees
    """

    n = len(m)
    p =1
    print(m[0],end = "")

    for k in range(1,n):

        if estDans(m[k],l):
            print(m[k],end = "")
            p += 1
        else:
            print("_",end = "")
    return p



def taille(nomFichier):
    """
    Compte le nombre de lignes d'un fichier texte
    Entree : Chaine de caractere comportant le nom du document text
    Sortie : Renvoye le nombre de ligne-1 du document
    """

    f = open(nomFichier)

    for k, ligne in enumerate(f):
        pass

    f.close()
    return k



def genMot():
    """
    Choisi un mot au hasard parmis le fichier choisi
    Sortie : Un mot aleatoire choisi dans le document texte
    """

    n = taille("mots.txt")

    fichier = open("mots.txt")

    ligneMot = randint(0,n)



    for i, ligne in enumerate(fichier):
        print(i,ligneMot)
        if i == ligneMot:
            mot = ligne.replace("\n","")


    fichier.close()

    return mot


def entreeLettre(l):
    """
    Demande a l'utilisateur de rentrer un lettre qu'il n'a pas deja choisie
    Entree : La liste des lettres deja choisies par l'utilisateur
    Sortie : La lettre que l'utilisateur a choisi et qui respecte les conditions
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    lettre = "1"

    while lettre.lower() not in alphabet or lettre in l:

        lettre = input("Choississez une lettre\n")

        if lettre.lower() not in alphabet:
            print("Merci de rentrer un lettte")
        elif lettre in l:
            print("Vous avez deja entre cette lettre,")
            print("voici les lettres que vous avez deja choisi :", l.split(""),"\n")

    return lettre



def insertion(mot,liste):
    """
    Remplie une liste de mot en gardant l'ordre alphabetique
    Entree : liste triee alphabetiquement et le mot que l'on souhaite inserer

    """

    n = len(liste)
    k = 0
    flag = True

    while flag and k < n:
        if mot < liste[k]:
            flag = False
            liste.insert(k,mot)
        k += 1

    if flag:
        liste.append(mot)




def dictionnaire(nom):
    """
    Trie un fichier texte en selon la taille des mots puis de leur ordre alphabetique
    en ne gardant que les mots d'au moins deux lettres
    Entree : nom du fichier
    Sortie : -
    """

    fichier = open(nom)

    #fichier.decode('cp932')

    listeMot = []

    longMax = 0

    for i, ligne in enumerate(fichier):
        print(ligne)
        listeMot += [ligne.replace("\n","")]
        longMax = max(longMax,len(ligne.replace("\n","")))

    fichier.close()


    print(listeMot)
    print(longMax)

    listeMotTriee = [ [] for k in range(longMax + 1)]

    for mot in listeMot:
        print(mot,len(mot),longMax,len(listeMotTriee))
        insertion(mot,listeMotTriee[len(mot)])


    for k in range(3):
        listeMotTriee[k] = []

    print(listeMotTriee)



    f = open((nom.split("."))[0] + "Triee.txt","w")

    #f.writelines(L) for L = listeMotTriee[longM][m] for m in range(len(listeMotTriee[longM])) for longM in range(longMax + 1)

    for longM in range(longMax + 1):
        for m in range(len(listeMotTriee[longM])):
            f.write(listeMotTriee[longM][m]+"\n")



    f.close()




