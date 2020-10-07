import pygame


class Emplacement(pygame.sprite.Sprite):

    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image= pygame.image.load("assets/orange.png")
        self.rect= self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y

    def set_image(self, image):
        self.image = image

