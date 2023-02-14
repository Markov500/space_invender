import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self, centreVaisseau):
        super(Explosion,self).__init__()
        self.fond=pygame.image.load("ressources/explosion.png").convert()

        self.nbrCycle=10
        self.fond.set_colorkey((255,255,255),pygame.RLEACCEL)#Supprimer la couleur de fond
    
        self.rect=self.fond.get_rect( center = centreVaisseau)#Retenir la position
    

    def update(self):
        self.nbrCycle-=1
        if self.nbrCycle == 0:
            self.kill()