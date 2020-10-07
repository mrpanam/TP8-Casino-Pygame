import pygame


class Fruit:

    def __init__(self, nom, gain, proba, img):
        self.nom = nom
        self.gain = gain
        self.proba = proba
        self.img = pygame.image.load(img)

    def __repr__(self):
        return self.nom
