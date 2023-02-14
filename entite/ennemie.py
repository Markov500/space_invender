import random
import pygame
class Ennemi(pygame.sprite.Sprite):
    def __init__(self,largEcran,hautEcran):
        super(Ennemi,self).__init__()
        self.fond=pygame.image.load("ressources/ennemi.png").convert()
        self.fond.set_colorkey((255,255,255),pygame.RLEACCEL)#Supprimer la couleur de fond
    
        self.rect=self.fond.get_rect(
            center=(
                        largEcran +50,#la position en X du centre de l'ennemi
                        random.randint(0,hautEcran)#la position en Y du centre de l'ennemi
                    )
        )#Retenir la position

        self.vitesse = random.randint(5,20) 

    def update(self):
        self.rect.move_ip(-self.vitesse, 0)
        
        if self.rect.right < 0:
            self.kill()