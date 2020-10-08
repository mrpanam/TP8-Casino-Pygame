from Fruits import Fruit
import numpy as np


def ligne():

    Ananas = Fruit("ananas", 50, 0.2, "assets/ananas.png")
    Cerise = Fruit("cerise", 15, 0.25, "assets/cerise.png")
    Orange = Fruit("orange", 5, 0.4, "assets/orange.png")
    Pasteque = Fruit("pasteque", 150, 0.1, "assets/pasteque.png")
    Pomme_dore = Fruit("pomme_dore", 10000, 0.05, "assets/pomme_dore.png")

    liste_fruit = [Ananas, Cerise, Orange, Pasteque, Pomme_dore]
    liste_proba = [Ananas.proba, Cerise.proba, Orange.proba, Pasteque.proba, Pomme_dore.proba]

    tirage=np.random.choice(liste_fruit, 3, liste_proba)
    print(tirage)
    return tirage


def check_ligne(result):
    gain=0
    if result[0].nom == result[1].nom == result[2].nom:
        gain = result[0].gain
        print(f"gagne 3 {result[0].nom} vous avez obtenu  {result[0].gain} jetons ")
    else:
        print("perdu ")
    return gain