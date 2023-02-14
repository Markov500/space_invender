import pygame
class Missile(pygame.sprite.Sprite):
    def __init__(self, centreVaisseu):
        super(Missile,self).__init__()
        self.fond=pygame.image.load("ressources/missile.png").convert()
        self.fond.set_colorkey((255,255,255),pygame.RLEACCEL)#Supprimer la couleur de fond
    
        self.rect=self.fond.get_rect( center = centreVaisseu)#Retenir la position
    

    def update(self,lagEcran):
        self.rect.move_ip(20,0) 
        if self.rect.left > lagEcran:
            self.kill()