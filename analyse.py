from models import Partie, Echange, Joueur
import matplotlib.pyplot as plt
import settings


portefeuille_init = settings.PORTEFEUILLE_INIT
nb_echange = settings.NB_ECHANGES
parametres = settings.DEFAULT

Gentil = Joueur(0, 'gentil', portefeuille_init)
Mechant = Joueur(1, 'mechant', portefeuille_init)
Trader = Joueur(2, 'trader', portefeuille_init)
Copieur = Joueur(3, 'copieur', portefeuille_init)
Aleatoire = Joueur(4, 'aleatoire', portefeuille_init)


def affichage_argent(perso1, perso2, nb_echanges):
    """ """
    liste_argent1 = [perso1.portefeuille]
    liste_argent2 = [perso2.portefeuille]
    Echange(perso1, perso2, parametres, nb_echanges=1)
    liste_argent1.append(perso1.portefeuille)
    liste_argent2.append(perso2.portefeuille)
    i = 0
    while i < (nb_echanges - 1) and perso1.portefeuille > 0 and perso2.portefeuille > 0:
        Echange(perso1, perso2, parametres, nb_echanges=1)
        liste_argent1.append(perso1.portefeuille)
        liste_argent2.append(perso2.portefeuille)
        i += 1
    while len(liste_argent1) < nb_echanges+1:
        liste_argent1.append(perso1.portefeuille)
        liste_argent2.append(perso2.portefeuille)
    plt.plot([j for j in range(nb_echanges+1)], liste_argent1)
    plt.plot([k for k in range(nb_echanges+1)],liste_argent2)
    plt.xlabel("Tours")
    plt.ylabel("Argent")
    plt.show()
    return (liste_argent1,liste_argent2)


affichage_argent()

def moyenne_des_graphes(perso1, argent1, perso2, argent2, r1, r2, nb_echanges, nb_simulations=20):
    resultats = []
    
    for _ in range(nb_simulations):
        liste_argent1, liste_argent2 = affichage_argent(perso1, argent1, perso2, argent2, r1, r2, nb_echanges)
        resultats.append((liste_argent1, liste_argent2))
    
    nb_tours = nb_echanges + 1
    moy1 = [0] * nb_tours
    moy2 = [0] * nb_tours
    
    for i in range(nb_tours):
        moy1[i] = sum([resultats[j][0][i] for j in range(nb_simulations)]) / nb_simulations
        moy2[i] = sum([resultats[j][1][i] for j in range(nb_simulations)]) / nb_simulations
    
    plt.plot(range(nb_tours), moy1, label="Moyenne Perso1")
    plt.plot(range(nb_tours), moy2, label="Moyenne Perso2")
    plt.xlabel("Tours")
    plt.ylabel("Argent")
    plt.legend()
    plt.show()

    return moy1, moy2


#Changer le protefeuille initial ?






"""
def affichage_argent(partie, perso1, perso2):
    """ """
    liste_argent1 = [perso1.portefeuille]
    liste_argent2 = [perso2.portefeuille]
    partie.echange(perso1, perso2)
    recap_echange = partie.liste_transaction[-1]
    for resume in recap_echange :
        liste_argent1.append(liste_argent1[-1] + resume[perso1.identifiant]["gains"])
        liste_argent2.append(liste_argent2[-1] + resume[perso2.identifiant]["gains"])
        print(liste_argent1)
        print(liste_argent2)
    print(len)
    _ = plt.plot([j for j in range(partie.nb_echanges+1)], liste_argent1)
    _ = plt.plot([k for k in range(partie.nb_echanges+1)],liste_argent2)
    _ = plt.xlabel("Tours")
    _ = plt.ylabel("Argent")
    plt.show()
"""