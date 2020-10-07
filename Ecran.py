import pygame

from Emplacements import Emplacement

def run():
    ecran= pygame.display.set_mode((800,460))
    pygame.display.set_caption("Welcome to Mrpanam's Casino")
    img_fond=pygame.image.load("assets/slot.png")
    color_fond= (255, 255, 255)

    #chargement des emplacements avec img
    emps=pygame.sprite.Group()
    emp_g=Emplacement(306-80,260)
    emp_m=Emplacement(328,260)
    emp_d=Emplacement(348+80,260)
    emps.add(emp_g)
    emps.add(emp_m)
    emps.add(emp_d)

    while 1:

        ecran.fill(color_fond)
        ecran.blit(img_fond, (0, 0))
        emps.draw(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("lancement")



        pygame.display.flip()



