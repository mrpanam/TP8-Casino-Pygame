import pygame

ecran= pygame.display.set_mode((800,460))
pygame.display.set_caption("Machine à sous")
img_fond=pygame.image.load("assets/slot.png")
color_fond= (0, 255, 255)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            quit()

    ecran.fill(color_fond)
    ecran.blit(img_fond, (0, 0))
    pygame.display.flip()



