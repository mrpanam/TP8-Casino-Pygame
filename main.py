import pygame
from Emplacements import Emplacement

from Fruits import Fruit
import numpy as np
pygame.init()

jetons = 1000
Ananas = Fruit("ananas", 50, 0.2, "assets/ananas.png")
Cerise = Fruit("cerise", 15, 0.25, "assets/cerise.png")
Orange = Fruit("orange", 5, 0.4, "assets/orange.png")
Pasteque = Fruit("pasteque", 150, 0.1, "assets/pasteque.png")
Pomme_dore = Fruit("pomme_dore", 10000, 0.05, "assets/pomme_dore.png")

liste_fruit = [Ananas, Cerise, Orange, Pasteque, Pomme_dore]
liste_proba = [Ananas.proba, Cerise.proba, Orange.proba, Pasteque.proba, Pomme_dore.proba]

ecran = pygame.display.set_mode((800, 460))
pygame.display.set_caption("Welcome to Mrpanam's Casino")
img_fond = pygame.image.load("assets/slot.png")
color_fond = (255, 255, 255)
police = pygame.font.SysFont("comicsansms", 30)
emps = pygame.sprite.Group()
emp_g = Emplacement(306 - 80, 260)
emp_m = Emplacement(328, 260)
emp_d = Emplacement(348 + 80, 260)
emps.add(emp_g)
emps.add(emp_m)
emps.add(emp_d)


def lancement():
    global jetons
    result = np.random.choice(liste_fruit, 3, liste_proba)
    emp_g.set_image(result[0].img)
    emp_m.set_image(result[1].img)
    emp_d.set_image(result[2].img)

    print(result)
    if result[0].nom == result[1].nom == result[2].nom:
        jetons += result[0].gain
        print(f"gagne 3 {result[0].nom} vous avez obtenu  {jetons} jetons ")
    else:
        print("perdu ")


while 1:
    ecran.fill(color_fond)
    ecran.blit(img_fond, (0, 0))
    emps.draw(ecran)
    text = police.render(str(jetons) + " jetons", True, (0, 0, 0))
    ecran.blit(text, (10, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jetons>=10:
                lancement()
                print("lancement")
                jetons-=10
    pygame.display.flip()
