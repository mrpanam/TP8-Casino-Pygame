import pygame
from Emplacements import Emplacement

from Lignes import ligne, check_ligne

pygame.init()
jetons = 1000
compteur=0
gaintotal=0
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

    result = ligne()
    emp_g.set_image(result[0].img)
    emp_m.set_image(result[1].img)
    emp_d.set_image(result[2].img)

    gain=check_ligne(result)
    '''if result[0].nom == result[1].nom == result[2].nom:
        jetons += result[0].gain
        print(f"gagne 3 {result[0].nom} vous avez obtenu  {jetons} jetons ")
    else:
        print("perdu ")'''
    return gain

while 1:

    ecran.fill(color_fond)
    ecran.blit(img_fond, (0, 0))
    emps.draw(ecran)
    text = police.render(str(jetons) + " jetons", True, (0, 0, 0))
    text2 = police.render("nb coup : " + str(compteur) , True, (0, 0, 0))
    text3= police.render("gain total : " + str(gaintotal) , True, (0, 0, 0))
    ecran.blit(text, (10, 0))
    ecran.blit(text2,(0,420))
    ecran.blit(text3,(600,0))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jetons >= 10:
                gain = lancement()
                print("lancement")
                jetons = jetons - 10 + gain
                compteur+=1
                gaintotal+=gain
    pygame.display.flip()
